#!/usr/bin/env python3
"""Install the bundled Codex Skill without overwriting an existing copy."""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


SKILL_NAME = "evidence-based-personal-advisor"
REPO_ROOT = Path(__file__).resolve().parents[1]
SOURCE = REPO_ROOT / "skills" / SKILL_NAME


def main() -> int:
    parser = argparse.ArgumentParser(description=f"Install {SKILL_NAME} for Codex")
    default_root = Path(os.environ.get("CODEX_HOME", Path.home() / ".codex")) / "skills"
    parser.add_argument("--dest", type=Path, default=default_root, help="Skills directory")
    args = parser.parse_args()

    destination = args.dest.expanduser().resolve() / SKILL_NAME
    if not SOURCE.is_dir():
        raise SystemExit(f"Skill source not found: {SOURCE}")
    if destination.exists():
        raise SystemExit(
            f"Destination already exists: {destination}\n"
            "Move or remove it explicitly before reinstalling."
        )

    symlinks = [path for path in SOURCE.rglob("*") if path.is_symlink()]
    if symlinks:
        listed = "\n".join(f"- {path.relative_to(SOURCE)}" for path in symlinks)
        raise SystemExit(f"Refusing to install a Skill containing symlinks:\n{listed}")

    validator = REPO_ROOT / "scripts" / "validate_repo.py"
    result = subprocess.run([sys.executable, str(validator)], check=False)
    if result.returncode:
        raise SystemExit("Repository validation failed; installation was cancelled.")

    destination.parent.mkdir(parents=True, exist_ok=True)
    staging_root = Path(tempfile.mkdtemp(prefix=f".{SKILL_NAME}-", dir=destination.parent))
    staged = staging_root / SKILL_NAME
    try:
        shutil.copytree(SOURCE, staged, symlinks=False, ignore=shutil.ignore_patterns(".DS_Store"))
        if destination.exists():
            raise SystemExit(f"Destination appeared during installation: {destination}")
        staged.rename(destination)
    finally:
        shutil.rmtree(staging_root, ignore_errors=True)
    print(f"Installed {SKILL_NAME} to {destination}")
    print("The Skill will be available on the next Codex turn.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
