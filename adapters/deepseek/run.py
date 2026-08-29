#!/usr/bin/env python3
"""Run the career Skill through the official DeepSeek Responses API."""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SKILL = ROOT / "skills" / "evidence-based-personal-advisor"
INSTRUCTION_FILES = (
    SKILL / "SKILL.md",
    SKILL / "references" / "career-module.md",
    SKILL / "references" / "evidence-protocol.md",
    SKILL / "references" / "model-router.md",
    SKILL / "references" / "output-contract.md",
)
DEFAULT_ENDPOINT = "https://api.deepseek.com/responses"


def build_instructions() -> str:
    sections = [
        "Apply the following career-advisor Skill as system-level instructions. "
        "The referenced files are inlined below because this API adapter does not provide filesystem access."
    ]
    for path in INSTRUCTION_FILES:
        sections.append(f"\n--- BEGIN {path.relative_to(SKILL)} ---\n")
        sections.append(path.read_text(encoding="utf-8"))
        sections.append(f"\n--- END {path.relative_to(SKILL)} ---\n")
    return "".join(sections)


def build_payload(prompt: str, model: str, web_search: bool) -> dict[str, object]:
    payload: dict[str, object] = {
        "model": model,
        "instructions": build_instructions(),
        "input": prompt,
    }
    if web_search:
        payload["tools"] = [{"type": "web_search"}]
        payload["tool_choice"] = "auto"
    return payload


def extract_text(response: dict[str, object]) -> str:
    texts: list[str] = []
    for item in response.get("output", []):
        if not isinstance(item, dict) or item.get("type") != "message":
            continue
        for part in item.get("content", []):
            if isinstance(part, dict) and part.get("type") == "output_text":
                value = part.get("text")
                if isinstance(value, str):
                    texts.append(value)
    if not texts:
        raise ValueError("DeepSeek response contained no assistant output_text.")
    return "\n".join(texts)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", default="deepseek-v4-pro")
    parser.add_argument("--endpoint", default=DEFAULT_ENDPOINT)
    parser.add_argument("--no-web-search", action="store_true")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        payload = build_payload("Sanitized test prompt", args.model, not args.no_web_search)
        assert payload["instructions"]
        assert payload["input"] == "Sanitized test prompt"
        assert "--- BEGIN references/evaluation-and-user-feedback.md ---" not in str(
            payload["instructions"]
        )
        mock_response = {
            "output": [
                {
                    "type": "message",
                    "content": [{"type": "output_text", "text": "Test response"}],
                }
            ]
        }
        assert extract_text(mock_response) == "Test response"
        print("DeepSeek adapter self-test passed.")
        return 0

    prompt = sys.stdin.read().strip()
    if not prompt:
        raise SystemExit("Provide the sanitized job-search request on standard input.")
    api_key = os.environ.get("DEEPSEEK_API_KEY")
    if not api_key:
        raise SystemExit("DEEPSEEK_API_KEY is not set.")

    request = urllib.request.Request(
        args.endpoint,
        data=json.dumps(build_payload(prompt, args.model, not args.no_web_search)).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=300) as result:
            response = json.loads(result.read().decode("utf-8"))
        print(extract_text(response))
    except (urllib.error.URLError, json.JSONDecodeError, ValueError) as error:
        print(f"DeepSeek request failed: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
