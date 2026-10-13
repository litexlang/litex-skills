#!/usr/bin/env python3
"""Check distributable skill entries, local Markdown links and snapshot hashes."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import unquote


def prose_lines(text: str):
    fence = None
    for number, line in enumerate(text.splitlines(), 1):
        marker = re.match(r"\s*(`{3,}|~{3,})", line)
        if marker:
            if fence is None:
                fence = marker[1][0]
            elif marker[1][0] == fence:
                fence = None
            continue
        if fence is None:
            yield number, line


def check(root: Path) -> list[str]:
    errors = []
    names = set()
    content_root = root / "sop_and_skills"
    entries = sorted((content_root / "skills").glob("*/SKILL.md"))
    if not entries:
        errors.append("No skill entrypoints found")
    for entry in entries:
        content = entry.read_text()
        front = re.match(r"\A---\n(.*?)\n---(?:\n|$)", content, re.S)
        name = re.search(r"^name:\s*([a-z0-9-]+)\s*$", front[1], re.M) if front else None
        description = re.search(r"^description:\s*\S", front[1], re.M) if front else None
        if not front or not name or not description:
            errors.append(f"{entry.relative_to(root)}: missing skill name/description frontmatter")
            continue
        if name[1] != entry.parent.name or name[1] in names:
            errors.append(f"{entry.relative_to(root)}: folder/name mismatch or duplicate name")
        names.add(name[1])

    links = 0
    for document in sorted(root.rglob("*.md")):
        relative = document.relative_to(root)
        if any(part in {".git", "private", "__pycache__"} for part in relative.parts):
            continue
        for number, line in prose_lines(document.read_text()):
            for match in re.finditer(r"\]\((<[^>]+>|[^\s)]+)(?:\s+[^)]*)?\)", line):
                destination = match[1].strip("<>")
                if re.match(r"[a-zA-Z][\w+.-]*:", destination) or destination.startswith("#"):
                    continue
                path = unquote(destination.split("#", 1)[0])
                if not path:
                    continue
                links += 1
                target = (document.parent / path).resolve()
                if not target.is_relative_to(root):
                    errors.append(f"{relative}:{number}: link escapes the hub: {destination}")
                elif not target.exists():
                    errors.append(f"{relative}:{number}: missing local target: {destination}")

    provenance = content_root / "references/provenance.json"
    snapshots = 0
    if not provenance.is_file():
        errors.append("Missing sop_and_skills/references/provenance.json")
    else:
        for relative, record in json.loads(provenance.read_text())["files"].items():
            path = (root / relative).resolve()
            if not path.is_relative_to(root) or not path.is_file():
                errors.append(f"Missing or invalid provenance target: {relative}")
                continue
            snapshots += 1
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
            if digest != record["packaged_sha256"]:
                errors.append(f"Snapshot changed without a provenance update: {relative}")

    receipts = 0
    for path in (content_root / "skills/litex-equality-inequality/references/evidence").rglob("*.summary.json"):
        data = json.loads(path.read_text())
        receipts += 1
        if (data.get("format") != "litex-hub-historical-receipt-summary-v1"
                or data.get("historical") is not True
                or data.get("full_verifier_payloads_included") is not False
                or not re.fullmatch(r"[0-9a-f]{64}", data.get("original_sha256", ""))):
            errors.append(f"Invalid historical receipt summary: {path.relative_to(root)}")
    print(f"Checked {len(entries)} skills, {links} local links, {snapshots} snapshot hashes and {receipts} receipt summaries.")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2], help="repository root containing sop_and_skills/")
    root = parser.parse_args().root.resolve()
    errors = check(root)
    if errors:
        for error in errors:
            print(error)
        return 1
    print("Hub package checks passed. Mathematical verification is a separate gate.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
