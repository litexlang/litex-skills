"""A Litex PTY retained on Generic Agent's handler during one task (Unix)."""

from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import time

import pexpect


class LitexSession:
    def __init__(self, run_dir: str, timeout: int = 30):
        self.root = Path(run_dir).resolve()
        self.manifest = json.loads((self.root / "run.json").read_text())
        self.journal = self.root / "session.jsonl"
        self.accepted = self.root / "accepted.lit"
        self.usable = False
        prefix = (self.root / "prefix.lit").read_text()
        replay = self.accepted.read_text() if self.accepted.exists() else ""
        bootstrap = self.root / "session-prefix.lit"
        bootstrap.write_text(prefix + "\n\n" + replay)
        self.child = pexpect.spawn(
            self.manifest["litex_binary"],
            ["-lang", "en", "-strict", "-session", "-f", str(bootstrap)],
            cwd=str(self.root), encoding="utf-8", timeout=timeout, echo=False,
        )
        start = time.monotonic()
        index = self.child.expect_exact(["litex> ", pexpect.EOF, pexpect.TIMEOUT])
        self.usable = index == 0
        self._record({"event": "start", "replayed_source": replay,
                      "bootstrap_sha256": hashlib.sha256(bootstrap.read_bytes()).hexdigest(),
                      "ready": self.usable, "raw_output": self.child.before,
                      "elapsed_seconds": time.monotonic() - start})
        if not self.usable:
            self.child.close(force=True)
            raise RuntimeError("Litex startup failed; inspect session.jsonl and the accepted prefix")

    def _record(self, event: dict) -> dict:
        event = {"timestamp": datetime.now(timezone.utc).isoformat(),
                 "pid": self.child.pid, **event}
        with self.journal.open("a") as stream:
            stream.write(json.dumps(event, ensure_ascii=False) + "\n")
        return event

    def submit(self, source: str) -> dict:
        if not self.usable:
            raise RuntimeError("Session is unusable; deliberately reopen and replay accepted source")
        source = source.strip("\n")
        lines = source.splitlines()
        roots = [line for line in lines if line.strip() and not line.startswith((" ", "\t", "#"))]
        if (len(roots) != 1 or any(not line.strip() for line in lines)
                or roots[0].strip() in {"quit", "exit", ":quit"}):
            raise ValueError("Submit one top-level statement, without internal blank lines or REPL exit commands")
        start = time.monotonic()
        self.child.sendline(source + ("\n" if len(lines) > 1 else ""))
        index = self.child.expect_exact(["litex> ", pexpect.EOF, pexpect.TIMEOUT])
        raw = self.child.before
        self.usable = index == 0
        envelope = None
        brace = raw.find("{")
        if brace >= 0:
            try:
                envelope, _ = json.JSONDecoder().raw_decode(raw[brace:])
            except ValueError:
                pass
        accepted = self.usable and bool(re.search(r"(?m)^\s*(?:\.\.\.\s*)*success\s*$", raw))
        if envelope is not None:
            accepted = False  # This pinned REPL prints plain success; JSON is rejection evidence.
        result = self._record({
            "event": "submit", "source": source, "accepted": accepted,
            "session_ready": self.usable, "raw_output": raw, "envelope": envelope,
            "elapsed_seconds": time.monotonic() - start,
            "boundary": ("prompt" if index == 0 else "eof" if index == 1 else "timeout"),
        })
        if accepted:
            with self.accepted.open("a") as stream:
                stream.write(source + "\n\n")
        elif index == 2:
            self.child.close(force=True)
        return result

    def close(self) -> dict:
        if self.usable:
            self.child.sendline("quit")
            self.child.expect(pexpect.EOF)
        self.usable = False
        raw = self.child.before
        self.child.close(force=True)
        return self._record({"event": "close", "exit": self.child.exitstatus,
                             "signal": self.child.signalstatus, "raw_output": raw})
