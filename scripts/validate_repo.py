#!/usr/bin/env python3
"""Run dependency-free structural and privacy checks for the repository."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_NAME = "evidence-based-personal-advisor"
SKILL = ROOT / "skills" / SKILL_NAME
TEXT_SUFFIXES = {
    ".md", ".yaml", ".yml", ".py", ".txt", ".json", ".toml", ".sh", ".bash", ".zsh"
}
REQUIRED = [
    ROOT / "README.md",
    ROOT / "README.zh-CN.md",
    ROOT / "LICENSE",
    ROOT / "CONTRIBUTING.md",
    ROOT / "SECURITY.md",
    ROOT / "CODE_OF_CONDUCT.md",
    ROOT / "ARCHITECTURE.md",
    ROOT / "ROADMAP.md",
    ROOT / "CHANGELOG.md",
    ROOT / "VERSION",
    ROOT / ".github" / "PULL_REQUEST_TEMPLATE.md",
    ROOT / ".github" / "ISSUE_TEMPLATE" / "bug-report.yml",
    ROOT / ".github" / "ISSUE_TEMPLATE" / "feature-request.yml",
    ROOT / ".github" / "ISSUE_TEMPLATE" / "user-feedback.yml",
    ROOT / ".github" / "ISSUE_TEMPLATE" / "evaluation-result.yml",
    ROOT / "examples" / "README.md",
    ROOT / "examples" / "early-career-ai-role-brief.md",
    SKILL / "SKILL.md",
    SKILL / "agents" / "openai.yaml",
    SKILL / "references" / "evidence-protocol.md",
    SKILL / "references" / "career-module.md",
    SKILL / "references" / "model-router.md",
    SKILL / "references" / "output-contract.md",
    SKILL / "references" / "evaluation-and-user-feedback.md",
    SKILL / "evals" / "cases.yaml",
    SKILL / "scripts" / "summarize_evals.py",
]


def fail(message: str, errors: list[str]) -> None:
    errors.append(message)


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    try:
        block = text.split("---\n", 2)[1]
    except IndexError:
        return {}
    values: dict[str, str] = {}
    for line in block.splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            values[key.strip()] = value.strip().strip('"').strip("'")
    return values


def main() -> int:
    errors: list[str] = []
    eval_text = ""

    for path in REQUIRED:
        if not path.is_file():
            fail(f"Missing required file: {path.relative_to(ROOT)}", errors)

    if SKILL.name != SKILL_NAME:
        fail("Skill folder name does not match the expected skill name", errors)

    version_file = ROOT / "VERSION"
    if version_file.is_file():
        version = version_file.read_text(encoding="utf-8").strip()
        if not re.fullmatch(r"\d+\.\d+\.\d+(?:-[a-z0-9.-]+)?", version):
            fail("VERSION must use semantic version form, optionally with a prerelease suffix", errors)
        for readme in (ROOT / "README.md", ROOT / "README.zh-CN.md"):
            if readme.is_file() and version not in readme.read_text(encoding="utf-8"):
                fail(f"Version {version} is missing from {readme.name}", errors)

    if (SKILL / "SKILL.md").is_file():
        skill_text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        metadata = parse_frontmatter(skill_text)
        if metadata.get("name") != SKILL_NAME:
            fail("SKILL.md frontmatter name does not match the folder name", errors)
        if len(metadata.get("description", "")) < 80:
            fail("SKILL.md description is missing or too weak for reliable triggering", errors)
        if len(skill_text.splitlines()) > 500:
            fail("SKILL.md exceeds the 500-line progressive-disclosure limit", errors)

    agent_file = SKILL / "agents" / "openai.yaml"
    if agent_file.is_file():
        agent_text = agent_file.read_text(encoding="utf-8")
        if f"${SKILL_NAME}" not in agent_text:
            fail("agents/openai.yaml default prompt must mention the Skill explicitly", errors)

    eval_file = SKILL / "evals" / "cases.yaml"
    if eval_file.is_file():
        eval_text = eval_file.read_text(encoding="utf-8")
        if len(re.findall(r"^\s*- id:\s*", eval_text, flags=re.MULTILINE)) < 8:
            fail("At least eight behavioral evaluation cases are required", errors)

    local_path_patterns = [
        re.compile(r"/Users/[^/\s]+/"),
        re.compile(r"/home/[^/\s]+/"),
        re.compile(r"[A-Za-z]:\\Users\\"),
    ]
    secret_patterns = [
        re.compile(r"(?i)(api[_-]?key|access[_-]?token|password|secret)\s*[:=]\s*['\"][^'\"]{8,}"),
        re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
        re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b"),
    ]

    for path in ROOT.rglob("*"):
        if path.is_symlink():
            fail(f"Repository must not contain symlinks: {path.relative_to(ROOT)}", errors)
            continue
        if not path.is_file() or ".git" in path.parts:
            continue
        if path.name == ".DS_Store":
            fail(f"macOS metadata must not be committed: {path.relative_to(ROOT)}", errors)
            continue
        if path.suffix.lower() not in TEXT_SUFFIXES:
            if path.suffix or path.stat().st_size > 1_000_000:
                continue
            raw = path.read_bytes()
            if b"\x00" in raw:
                continue
            text = raw.decode("utf-8", errors="replace")
        else:
            text = path.read_text(encoding="utf-8", errors="replace")
        if path.resolve() != Path(__file__).resolve():
            for pattern in local_path_patterns:
                if pattern.search(text):
                    fail(f"Local absolute path found in {path.relative_to(ROOT)}", errors)
                    break
        for pattern in secret_patterns:
            if pattern.search(text):
                fail(f"Possible secret found in {path.relative_to(ROOT)}", errors)
                break
        if path.suffix.lower() == ".md":
            for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
                if target.startswith(("http://", "https://", "mailto:", "#")):
                    continue
                clean_target = target.split("#", 1)[0]
                if clean_target and not (path.parent / clean_target).resolve().exists():
                    fail(
                        f"Broken relative link in {path.relative_to(ROOT)}: {target}",
                        errors,
                    )

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Validation passed.")
    print(f"Skill: {SKILL_NAME}")
    case_count = len(re.findall(r"^\s*- id:\s*", eval_text, flags=re.MULTILINE))
    print(f"Evaluation cases: {case_count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
