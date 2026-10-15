#!/usr/bin/env python3
"""Pure-API smoke test for litex-basics against the mini task suite."""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
HUB = HERE.parent.parent
DEFAULT_SKILL = HUB / "skills/litex-basics/SKILL.md"
DEFAULT_TASKS = HERE / "tasks.json"
DEFAULT_ENV = HUB.parent / "litex-ai-benchmark（10-13最后版本）" / ".env.local"
DEFAULT_LITEX = HUB.parent / "litex-ai-benchmark（10-13最后版本）" / "standards/toolchain/litex"
DEFAULT_BASE = "https://cc-vibe.com/v1"
DEFAULT_MODEL = "claude-opus-4-6"


def load_dotenv(path: Path) -> None:
    if not path.is_file():
        return
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip())


def extract_litex(text: str) -> str:
    blocks = re.findall(r"```(?:litex)?\s*\n(.*?)```", text, flags=re.S | re.I)
    if blocks:
        return blocks[0].strip() + "\n"
    # bare candidate: keep non-empty lines that look like Litex
    lines = [ln for ln in text.splitlines() if ln.strip() and not ln.strip().startswith("```")]
    return ("\n".join(lines).strip() + "\n") if lines else ""


def call_api(base_url: str, api_key: str, model: str, system: str, user: str,
             max_tokens: int, timeout: float) -> tuple[str, dict]:
    endpoint = base_url.rstrip("/") + "/chat/completions"
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        "temperature": 0,
        "max_tokens": max_tokens,
    }
    body = json.dumps(payload).encode()
    req = urllib.request.Request(
        endpoint, data=body, method="POST",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        doc = json.loads(resp.read().decode())
    msg = (doc.get("choices") or [{}])[0].get("message") or {}
    content = msg.get("content") or ""
    return content, doc


def check_litex(litex_bin: Path, source: str) -> dict:
    proc = subprocess.run(
        [str(litex_bin), "-lang", "en", "-strict", "-e", source],
        capture_output=True, text=True, timeout=60,
    )
    raw = proc.stdout.strip() or proc.stderr.strip()
    try:
        doc = json.loads(raw)
    except json.JSONDecodeError:
        return {"ok": False, "exit_code": proc.returncode, "raw": raw[:2000], "parse_error": True}
    ok = doc.get("run_result") == "success" and proc.returncode == 0
    return {"ok": ok, "exit_code": proc.returncode, "document": doc, "raw": raw[:4000]}


def pattern_ok(source: str, task: dict) -> tuple[bool, list[str]]:
    problems = []
    for needle in task.get("must_contain") or []:
        if needle not in source:
            problems.append(f"missing:{needle}")
    for needle in task.get("must_not_contain") or []:
        if needle and needle in source:
            problems.append(f"forbidden:{needle}")
    return (not problems), problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skill", type=Path, default=DEFAULT_SKILL)
    parser.add_argument("--tasks", type=Path, default=DEFAULT_TASKS)
    parser.add_argument("--env-file", type=Path, default=DEFAULT_ENV)
    parser.add_argument("--api-key-env", default="CLAUDE_API_KEY3")
    parser.add_argument("--base-url", default=DEFAULT_BASE)
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--litex-bin", type=Path, default=DEFAULT_LITEX)
    parser.add_argument("--max-tokens", type=int, default=2048)
    parser.add_argument("--timeout", type=float, default=120)
    parser.add_argument("--task-id", action="append", help="Run only these task ids")
    parser.add_argument("--offline-fixture", action="store_true",
                        help="Skip API; use fixture answers from tasks (for harness check)")
    parser.add_argument("--out", type=Path, default=HERE / "results")
    args = parser.parse_args()

    load_dotenv(args.env_file)
    for k in list(os.environ):
        if "proxy" in k.lower():
            del os.environ[k]
    os.environ["NO_PROXY"] = "*"

    skill = args.skill.read_text()
    suite = json.loads(args.tasks.read_text())
    tasks = suite["tasks"]
    if args.task_id:
        wanted = set(args.task_id)
        tasks = [t for t in tasks if t["id"] in wanted]

    api_key = os.environ.get(args.api_key_env)
    if not args.offline_fixture and not api_key:
        print(f"Missing {args.api_key_env}", file=sys.stderr)
        return 2
    if not args.litex_bin.is_file():
        print(f"Missing litex binary: {args.litex_bin}", file=sys.stderr)
        return 2

    mode = "offline" if args.offline_fixture else "live"
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S_%f") + "_" + mode
    out = args.out / stamp
    out.mkdir(parents=True, exist_ok=True)

    system = (
        "You write Litex code only. Follow the Litex basics skill below.\n"
        "Reply with a single ```litex fenced block and no extra prose.\n\n"
        + skill
    )

    fixtures = {
        "M01": "have points set = cart(R, R)\n",
        "M02": "have fn vec(A, B cart(R, R)) cart(R, R) = (B(1) - A(1), B(2) - A(2))\n",
        "M03": "have p cart(R, R) = (2, 3)\np(1) = 2\np(2) = 3\n",
        "M04": "have fn reciprocal(x R: x != 0) R = 1 / x\n",
        "M05": "have S set = {1, 2}\n1 $in S\n",
    }

    rows = []
    passed = 0
    for task in tasks:
        tid = task["id"]
        user = task.get("prompt_en") or task.get("prompt_zh")
        print(f"[{tid}] {task['name']}", flush=True)
        started = time.monotonic()
        if args.offline_fixture:
            content = f"```litex\n{fixtures[tid]}```"
            raw_doc = {"fixture": True}
            api_s = 0.0
        else:
            content, raw_doc = call_api(
                args.base_url, api_key, args.model, system, user,
                args.max_tokens, args.timeout,
            )
            api_s = time.monotonic() - started
        source = extract_litex(content)
        (out / f"{tid}_response.txt").write_text(content)
        (out / f"{tid}_candidate.lit").write_text(source)
        (out / f"{tid}_api.json").write_text(json.dumps(raw_doc, ensure_ascii=False, indent=2) + "\n")

        pat_ok, pat_problems = pattern_ok(source, task)
        verify = check_litex(args.litex_bin, source) if source.strip() else {
            "ok": False, "exit_code": -1, "raw": "empty candidate",
        }
        (out / f"{tid}_verify.json").write_text(json.dumps(verify, ensure_ascii=False, indent=2) + "\n")
        ok = bool(source.strip()) and pat_ok and verify.get("ok")
        if ok:
            passed += 1
            print(f"  PASS  api={api_s:.1f}s", flush=True)
        else:
            print(f"  FAIL  api={api_s:.1f}s patterns={pat_problems} litex_ok={verify.get('ok')}", flush=True)
        rows.append({
            "id": tid,
            "name": task["name"],
            "success": ok,
            "api_seconds": api_s,
            "pattern_ok": pat_ok,
            "pattern_problems": pat_problems,
            "litex_ok": verify.get("ok"),
            "candidate": source,
        })

    summary = {
        "schema_version": "1.0",
        "suite": suite["name"],
        "skill": str(args.skill),
        "model": args.model if not args.offline_fixture else "offline-fixture",
        "api_key_env": args.api_key_env,
        "passed": passed,
        "total": len(rows),
        "tasks": rows,
        "finished_at": datetime.now(timezone.utc).isoformat(),
    }
    (out / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n")
    print(f"\n{passed}/{len(rows)} passed → {out / 'summary.json'}", flush=True)
    return 0 if passed == len(rows) else 1


if __name__ == "__main__":
    raise SystemExit(main())
