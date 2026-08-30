#!/usr/bin/env python3
"""Install the bundled Skill for supported filesystem-based agents."""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


SKILL_NAME = "job-navigation-skill"
REPO_ROOT = Path(__file__).resolve().parents[1]
SOURCE = REPO_ROOT / "skills" / SKILL_NAME


def main() -> int:
    parser = argparse.ArgumentParser(description=f"Install {SKILL_NAME}")
    parser.add_argument(
        "--agent",
        choices=("codex", "claude", "cursor", "workbuddy"),
        default="codex",
        help="target agent (default: codex)",
    )
    parser.add_argument(
        "--dest",
        type=Path,
        help="override the parent Skills directory",
    )
    args = parser.parse_args()

    if args.dest is not None:
        target_root = args.dest
    elif args.agent == "codex":
        target_root = Path(os.environ.get("CODEX_HOME", Path.home() / ".codex")) / "skills"
    elif args.agent == "cursor":
        target_root = Path.home() / ".cursor" / "skills"
    else:
        # work-buddy runs inside Claude Code and therefore uses Claude's Skill directory.
        target_root = Path.home() / ".claude" / "skills"

    destination = target_root.expanduser().resolve() / SKILL_NAME
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
    print(f"Installed {SKILL_NAME} for {args.agent} to {destination}")
    print(f"Start a new {args.agent} task or session to pick up the Skill.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
