#!/usr/bin/env python3
"""Export a non-overwriting Litex skill pack; author is the default profile."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import sys
import tempfile
from urllib.parse import unquote

sys.dont_write_bytecode = True
from check_hub import prose_lines


def selection(root: Path, profile: str) -> tuple[list[str], set[Path]]:
    data = json.loads((root / "profiles.json").read_text())
    chosen = data["profiles"][profile]
    names = list(data["skills"]) if chosen == "all" else chosen
    files: set[Path] = set()
    if profile == "maintainer":
        for scope in data["maintainer_source_scopes"]:
            source = root / scope
            if not source.exists():
                raise ValueError(f"Missing source scope: {scope}")
            files.update([source] if source.is_file() else source.rglob("*"))
    else:
        for name in names:
            source = root / "skills" / name
            patterns = data["portable_payloads"].get(name, data["portable_default_payload"])
            for pattern in patterns:
                matches = list(source.glob(pattern))
                if not matches:
                    raise ValueError(f"Missing payload: {name}/{pattern}")
                for match in matches:
                    files.update([match] if match.is_file() else match.rglob("*"))
    files = {p for p in files if p.is_file() and not any(
        part in {"__pycache__", ".DS_Store", ".git"} for part in p.relative_to(root).parts
    )}
    for path in files:
        if path.is_symlink() or not path.resolve().is_relative_to(root):
            raise ValueError(f"Unsupported source symlink: {path}")
    return names, files


def check_links(root: Path, files: set[Path]) -> None:
    """Validate the selected pack, rather than links satisfied only by source archives."""
    for document in sorted(p for p in files if p.suffix == ".md"):
        for number, line in prose_lines(document.read_text()):
            for match in re.finditer(r"\]\((<[^>]+>|[^\s)]+)(?:\s+[^)]*)?\)", line):
                destination = match[1].strip("<>")
                if re.match(r"[a-zA-Z][\w+.-]*:", destination) or destination.startswith("#"):
                    continue
                path = unquote(destination.split("#", 1)[0])
                if not path:
                    continue
                target = (document.parent / path).resolve()
                present = target in files or (target.is_dir() and any(
                    selected.is_relative_to(target) for selected in files
                ))
                if not target.is_relative_to(root) or not present:
                    raise ValueError(
                        f"{document.relative_to(root)}:{number}: unpackaged link: {destination}"
                    )


def export(root: Path, profile: str, output: Path) -> tuple[int, int]:
    # Do not resolve the final component: an existing dangling symlink also counts.
    output = output.expanduser().absolute()
    if output.exists() or output.is_symlink():
        raise FileExistsError(f"Destination already exists: {output}")
    if output.resolve().is_relative_to(root):
        raise ValueError("Choose an output directory outside the source repository")
    names, files = selection(root, profile)
    check_links(root, files)
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".litex-pack-", dir=output.parent) as temporary:
        stage = Path(temporary)
        hashes = {}
        for source in sorted(files):
            relative = source.relative_to(root)
            target = stage / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
            hashes[str(relative)] = hashlib.sha256(target.read_bytes()).hexdigest()
        (stage / "pack-manifest.json").write_text(json.dumps({
            "schema_version": 1, "profile": profile, "skills": names,
            "files": hashes,
            "note": "Copied source hashes; mathematical and agent behavior gates are separate."
        }, indent=2) + "\n")
        (stage / "INSTALL.md").write_text(
            f"# Litex {profile} skill pack\n\n"
            "Read `skills/litex-basics/SKILL.md` first. "
            "Copy the selected sibling skill directories from `skills/` "
            "into your agent's skill directory, preserving their names and relative layout. "
            "Inspect existing installations and merge local guidance before replacing anything.\n\n"
            "The starter works with a Litex executable. For deeper reading set "
            "`LITEX_REFERENCE_ROOT` to a matching golitex checkout with docs/, examples/ "
            "and showcases/. Do not resolve ../golitex from an installed skill directory.\n\n"
            "Only load the task skill and topic needed. The basics and author packs omit "
            "maintainer instructions and historical archives; the explicit maintainer pack "
            "preserves the complete source scopes and their shared references. For that pack, "
            "retain the pack layout and follow its hub index for shared resources.\n"
        )
        # Exclusive reservation also rejects a destination created during preparation.
        output.mkdir()
        for child in stage.iterdir():
            child.rename(output / child.name)
    return len(names), len(files)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", choices=("basics", "author", "maintainer"), default="author")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        skills, files = export(Path(__file__).resolve().parents[1], args.profile, args.output)
    except (OSError, ValueError, KeyError) as error:
        print(f"Export failed: {error}", file=sys.stderr)
        return 1
    print(f"Exported {skills} skills and {files} source files to {args.output} ({args.profile}).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
