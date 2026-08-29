#!/usr/bin/env python3
"""Build uploadable ChatGPT plugin and Claude Skill zip archives."""

from __future__ import annotations

import argparse
import subprocess
import sys
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_NAME = "evidence-based-personal-advisor"
SKILL = ROOT / "skills" / SKILL_NAME
EXCLUDED_PARTS = {".DS_Store", "__pycache__"}


def included_files(root: Path) -> list[Path]:
    return sorted(
        path
        for path in root.rglob("*")
        if path.is_file()
        and not path.is_symlink()
        and not any(part in EXCLUDED_PARTS for part in path.parts)
        and path.suffix != ".pyc"
    )


def write_zip(destination: Path, entries: list[tuple[Path, Path]]) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(destination, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for source, archive_path in sorted(entries, key=lambda item: item[1].as_posix()):
            archive.write(source, archive_path.as_posix())


def build(target: str, output_dir: Path, version: str) -> Path:
    if target == "claude":
        destination = output_dir / f"{SKILL_NAME}-claude-skill-{version}.zip"
        entries = [(path, path.relative_to(SKILL)) for path in included_files(SKILL)]
    else:
        destination = output_dir / f"{SKILL_NAME}-chatgpt-plugin-{version}.zip"
        plugin_manifest = ROOT / ".codex-plugin" / "plugin.json"
        entries = [(plugin_manifest, Path(".codex-plugin/plugin.json"))]
        entries.extend(
            (path, Path("skills") / path.relative_to(ROOT / "skills"))
            for path in included_files(ROOT / "skills")
        )
    write_zip(destination, entries)
    return destination


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", choices=("chatgpt", "claude", "all"), default="all")
    parser.add_argument("--output", type=Path, default=ROOT / "dist")
    args = parser.parse_args()

    validation = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "validate_repo.py")],
        check=False,
    )
    if validation.returncode:
        raise SystemExit("Repository validation failed; packaging was cancelled.")

    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    targets = ("chatgpt", "claude") if args.target == "all" else (args.target,)
    for target in targets:
        archive = build(target, args.output.expanduser().resolve(), version)
        print(f"Built {target}: {archive}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
