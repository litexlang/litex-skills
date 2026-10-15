#!/usr/bin/env python3
"""Prepare a fresh Generic Agent geometry run, or check its frozen Litex goal."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import shutil
import shlex
import platform
import subprocess
import sys
import tempfile

EXAMPLE = Path(__file__).resolve().parent
HUB = EXAMPLE.parents[1]
SPEC = json.loads((EXAMPLE / "experiment.json").read_text())


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def command(args: list[str], **kwargs) -> str:
    return subprocess.check_output(args, text=True, **kwargs).strip()


def prepare(args) -> None:
    output = args.output.expanduser().absolute()
    agent = args.agent.resolve()
    litex = args.litex_root.resolve()
    binary = litex / "target/release/litex"
    if output.exists() or output.is_symlink():
        raise ValueError(f"Refuse existing output: {output}")
    if any(output.resolve().is_relative_to(root) for root in (HUB, agent, litex)):
        raise ValueError("Put the run outside the hub, agent and verifier source directories")
    paths = {
        "generic_agent": ["agentmain.py", "agent_loop.py", "ga.py", "llmcore.py", "plugins", "assets", "ga_cli"],
        "litex": ["Cargo.toml", "Cargo.lock", "src", "docs", "examples", "showcases"],
    }
    for root, key in ((agent, "generic_agent"), (litex, "litex")):
        actual = command(["git", "-C", str(root), "rev-parse", "HEAD"])
        if actual != SPEC[key]["commit"]:
            raise ValueError(f"{key} revision differs from experiment.json: {actual}")
        if subprocess.run(["git", "-C", str(root), "diff", "--quiet", "HEAD", "--", *paths[key]]).returncode:
            raise ValueError(f"{key} has tracked runtime/reference changes; use a separate pinned checkout")
    for path in (agent / "agentmain.py", agent / "ga.py", binary):
        if not path.is_file():
            raise ValueError(f"Required installed file is missing: {path}")
    version = command([str(binary), "-version"])
    if version != SPEC["litex"]["version"]:
        raise ValueError(f"Unexpected Litex version: {version}")
    if not all((litex / name).is_dir() for name in ("docs", "examples", "showcases")):
        raise ValueError("The live Litex reference corpus is incomplete")
    manifest = {
        "schema_version": 1, "created_at": datetime.now(timezone.utc).isoformat(),
        "problem_id": SPEC["problem_id"], "agent_root": str(agent),
        "agent_commit": SPEC["generic_agent"]["commit"],
        "litex_root": str(litex), "litex_commit": SPEC["litex"]["commit"],
        "litex_binary": str(binary), "litex_version": version,
        "litex_binary_sha256": sha(binary), "python_version": sys.version,
        "platform": {"system": platform.system(), "release": platform.release(), "machine": platform.machine()},
        "unchanged_tracked_paths": paths,
        "model_label": args.model, "token_usage": None,
        "token_usage_note": "Not measured by preparation; record actual provider usage after the run.",
        "generation_status": "not_run",
        "inputs": {name: sha(EXAMPLE / "inputs" / name) for name in ("prefix.lit", "goal.lit")},
        "helper_sha256": sha(EXAMPLE / "litex_session.py"),
        "experiment_sha256": sha(EXAMPLE / "experiment.json"),
        "hub_revision": command(["git", "-C", str(HUB), "rev-parse", "HEAD"]),
        "hub_has_tracked_changes": subprocess.run(["git", "-C", str(HUB), "diff", "--quiet", "HEAD"]).returncode != 0,
    }
    # Validate/assemble in a temporary directory; reserve the final destination exclusively.
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".litex-geometry-", dir=output.parent) as temporary:
        stage = Path(temporary)
        subprocess.run([sys.executable, str(HUB / "scripts/export_skills.py"),
                        "--profile", "author", "--output", str(stage / "materials")], check=True)
        manifest["skills_pack_manifest_sha256"] = sha(stage / "materials/pack-manifest.json")
        for name in ("prefix.lit", "goal.lit"):
            shutil.copy2(EXAMPLE / "inputs" / name, stage / name)
        shutil.copy2(EXAMPLE / "problem.md", stage / "problem.md")
        shutil.copy2(EXAMPLE / "litex_session.py", stage / "litex_session.py")
        (stage / "run.json").write_text(json.dumps(manifest, indent=2) + "\n")
        template = (EXAMPLE / "prompt.template.md").read_text()
        replacements = {"@@RUN@@": str(output.resolve()), "@@CORPUS@@": str(litex),
                        "@@RUN_PY@@": repr(str(output.resolve())),
                        "@@CHECKER_PY@@": repr(str(EXAMPLE / "experiment.py"))}
        for marker, value in replacements.items():
            template = template.replace(marker, value)
        (stage / "prompt.md").write_text(template)
        (stage / "solution.lit").write_text("# Write accepted proof statements here; prefix and final goal are supplied by the checker.\n")
        output.mkdir()
        for child in stage.iterdir():
            child.rename(output / child.name)
    print(f"Prepared {output}. Configure your model in the agent checkout, then run:")
    print(f"  cd {shlex.quote(str(agent))}")
    print("  " + shlex.join(["python", "agentmain.py", "--func", str(output / "prompt.md"),
                              "--nobg", "--no-user-tools", "--nolog"]))
    print("No model request was made. Read README.md for quoted commands and result interpretation.")


def check(args) -> None:
    run = args.run.resolve()
    manifest = json.loads((run / "run.json").read_text())
    for name, digest in manifest["inputs"].items():
        if sha(EXAMPLE / "inputs" / name) != digest or sha(run / name) != digest:
            raise ValueError(f"Frozen input changed: {name}; prepare a fresh run")
    if sha(EXAMPLE / "experiment.json") != manifest["experiment_sha256"]:
        raise ValueError("Experiment specification changed; prepare a fresh run")
    binary = Path(manifest["litex_binary"])
    if sha(binary) != manifest["litex_binary_sha256"]:
        raise ValueError("Verifier binary changed; prepare a fresh run")
    proof = args.proof.resolve()
    source = (run / "prefix.lit").read_text() + "\n\n" + proof.read_text() + "\n\n" + (run / "goal.lit").read_text()
    # A fresh direct parent has no litex.config, so the composed gate is standalone.
    gates = run / "checks"
    gates.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".check-", dir=run) as temporary:
        target = Path(temporary) / "check.lit"
        target.write_text(source)
        cmd = [str(binary), "-lang", "en", "-strict", "-f", str(target)]
        try:
            result = subprocess.run(cmd, cwd=temporary, text=True, capture_output=True, timeout=60)
            stdout, stderr, exit_code = result.stdout, result.stderr, result.returncode
        except subprocess.TimeoutExpired as error:
            stdout = (error.stdout or b"").decode() if isinstance(error.stdout, bytes) else error.stdout or ""
            stderr, exit_code = "Verifier timed out after 60 seconds", None
        try:
            envelope = json.loads(stdout)
        except ValueError:
            envelope = None
        valid = (isinstance(envelope, dict) and envelope.get("kind") == "run"
                 and isinstance(envelope.get("success"), bool) and "session_error" in envelope)
        passed = (valid and exit_code == 0 and envelope["success"] is True
                  and envelope["session_error"] is None)
        record = {"schema_version": 1, "problem_id": SPEC["problem_id"],
                  "timestamp": datetime.now(timezone.utc).isoformat(),
                  "proof_path": str(proof), "proof_sha256": sha(proof),
                  "combined_source_sha256": hashlib.sha256(source.encode()).hexdigest(),
                  "command": cmd, "exit": exit_code, "recognized_pinned_contract": valid,
                  "verified_edge_theorem": bool(passed), "envelope": envelope,
                  "scope": SPEC["result_scope"],
                  "generation_note": "A verifier gate does not establish who generated the proof or measure an agent run."}
        for number in range(1, 1000000):
            saved = gates / f"{number:04d}"
            try:
                saved.mkdir()
                break
            except FileExistsError:
                continue
        else:
            raise ValueError("Too many checks in this run")
        record["replay_command"] = [str(binary), "-lang", "en", "-strict", "-f", str(saved / "check.lit")]
        (saved / "check.lit").write_text(source)
        (saved / "stdout.json").write_text(stdout)
        (saved / "stderr.txt").write_text(stderr)
        (saved / "result.json").write_text(json.dumps(record, indent=2) + "\n")
    print(f"{'PASS' if passed else 'FAIL'}: frozen edge-length theorem; evidence: {saved}")
    if not passed:
        raise SystemExit(1)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    prep = commands.add_parser("prepare", help="Create a new run without invoking a model")
    prep.add_argument("--agent", type=Path, required=True)
    prep.add_argument("--litex-root", type=Path, required=True)
    prep.add_argument("--output", type=Path, required=True)
    prep.add_argument("--model", required=True, help="Provider/model label only; never an API key")
    verify = commands.add_parser("check", help="Strictly check proof plus unchanged prefix and goal")
    verify.add_argument("--run", type=Path, required=True)
    verify.add_argument("--proof", type=Path, required=True)
    args = parser.parse_args()
    try:
        prepare(args) if args.command == "prepare" else check(args)
    except (OSError, ValueError, subprocess.SubprocessError) as error:
        print(f"Experiment failed: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
