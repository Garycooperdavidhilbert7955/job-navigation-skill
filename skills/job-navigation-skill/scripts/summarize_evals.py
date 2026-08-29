#!/usr/bin/env python3
"""Summarize privacy-safe paired baseline and Skill evaluation records."""

from __future__ import annotations

import argparse
import json
import statistics
import sys
from collections import Counter
from pathlib import Path
from typing import Any, Iterable


METRICS = (
    "citation_support",
    "evidence_calibration",
    "personalization",
    "actionability",
    "clarity_and_load",
)
WEIGHTS = {
    "citation_support": 0.25,
    "evidence_calibration": 0.15,
    "personalization": 0.20,
    "actionability": 0.25,
    "clarity_and_load": 0.15,
}
CONDITIONS = ("baseline", "skill")
COST_FIELDS = ("input_tokens", "output_tokens", "duration_seconds", "cost_usd")
USER_FIELDS = (
    "usefulness",
    "perceived_effort",
    "first_action_recall",
    "seven_day_attempted",
    "thirty_day_follow_up",
)


def template() -> dict[str, Any]:
    return {
        "pair_id": "random-pair-code",
        "task_id": "non-identifying-task-code",
        "condition": "baseline-or-skill",
        "model": "model-and-version",
        "tool_profile": "tools-and-access-notes",
        "skill_version": "null-for-baseline",
        "evaluated_at": "YYYY-MM-DD",
        "participant_code": None,
        "scores": {metric: None for metric in METRICS},
        "reviewer_reason": {metric: "brief reason" for metric in METRICS},
        "hard_failures": [],
        "input_tokens": None,
        "output_tokens": None,
        "duration_seconds": None,
        "cost_usd": None,
        "user_feedback": {
            "usefulness": None,
            "perceived_effort": None,
            "first_action_recall": None,
            "seven_day_attempted": None,
            "thirty_day_follow_up": None,
        },
    }


def load_jsonl(path_arg: str) -> list[dict[str, Any]]:
    if path_arg == "-":
        lines = sys.stdin.read().splitlines()
        source = "stdin"
    else:
        path = Path(path_arg)
        lines = path.read_text(encoding="utf-8").splitlines()
        source = str(path)

    records: list[dict[str, Any]] = []
    for line_number, line in enumerate(lines, start=1):
        if not line.strip():
            continue
        try:
            value = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"{source}:{line_number}: invalid JSON: {exc.msg}") from exc
        if not isinstance(value, dict):
            raise ValueError(f"{source}:{line_number}: each line must be a JSON object")
        records.append(value)
    if not records:
        raise ValueError(f"{source}: no evaluation records found")
    return records


def validate_records(records: list[dict[str, Any]]) -> None:
    seen: set[tuple[str, str]] = set()
    for index, record in enumerate(records, start=1):
        pair_id = record.get("pair_id")
        task_id = record.get("task_id")
        condition = record.get("condition")
        if not isinstance(pair_id, str) or not pair_id.strip():
            raise ValueError(f"record {index}: pair_id must be a non-empty string")
        if not isinstance(task_id, str) or not task_id.strip():
            raise ValueError(f"record {index}: task_id must be a non-empty string")
        if condition not in CONDITIONS:
            raise ValueError(f"record {index}: condition must be baseline or skill")
        key = (pair_id, condition)
        if key in seen:
            raise ValueError(f"record {index}: duplicate pair_id and condition: {key}")
        seen.add(key)

        scores = record.get("scores")
        reasons = record.get("reviewer_reason")
        if not isinstance(scores, dict) or not isinstance(reasons, dict):
            raise ValueError(f"record {index}: scores and reviewer_reason must be objects")
        for metric in METRICS:
            score = scores.get(metric)
            if not isinstance(score, (int, float)) or isinstance(score, bool) or not 1 <= score <= 5:
                raise ValueError(f"record {index}: {metric} must be a number from 1 to 5")
            reason = reasons.get(metric)
            if not isinstance(reason, str) or not reason.strip():
                raise ValueError(f"record {index}: {metric} requires a reviewer reason")

        failures = record.get("hard_failures", [])
        if not isinstance(failures, list) or any(not isinstance(item, str) for item in failures):
            raise ValueError(f"record {index}: hard_failures must be a list of strings")
        for field in COST_FIELDS:
            value = record.get(field)
            if value is not None and (
                not isinstance(value, (int, float)) or isinstance(value, bool) or value < 0
            ):
                raise ValueError(f"record {index}: {field} must be null or non-negative")

        feedback = record.get("user_feedback", {})
        if not isinstance(feedback, dict):
            raise ValueError(f"record {index}: user_feedback must be an object")
        for field in ("usefulness", "perceived_effort"):
            value = feedback.get(field)
            if value is not None and (
                not isinstance(value, (int, float)) or isinstance(value, bool) or not 1 <= value <= 5
            ):
                raise ValueError(f"record {index}: {field} must be null or a number from 1 to 5")
        for field in ("first_action_recall", "seven_day_attempted", "thirty_day_follow_up"):
            value = feedback.get(field)
            if value is not None and not isinstance(value, bool):
                raise ValueError(f"record {index}: {field} must be null or boolean")
        if any(feedback.get(field) is not None for field in USER_FIELDS):
            participant = record.get("participant_code")
            if not isinstance(participant, str) or not participant.strip():
                raise ValueError(f"record {index}: opt-in feedback requires a non-identifying participant_code")


def mean(values: Iterable[float]) -> float | None:
    items = list(values)
    return statistics.fmean(items) if items else None


def fmt(value: float | None, digits: int = 2) -> str:
    return "not recorded" if value is None else f"{value:.{digits}f}"


def composite(record: dict[str, Any]) -> float:
    weighted_mean = sum(float(record["scores"][metric]) * WEIGHTS[metric] for metric in METRICS)
    return (weighted_mean - 1) * 25


def summarize(records: list[dict[str, Any]]) -> str:
    validate_records(records)
    by_key = {(record["pair_id"], record["condition"]): record for record in records}
    baseline_ids = {pair_id for pair_id, condition in by_key if condition == "baseline"}
    skill_ids = {pair_id for pair_id, condition in by_key if condition == "skill"}
    complete_ids = sorted(baseline_ids & skill_ids)
    paired = {
        condition: [by_key[(pair_id, condition)] for pair_id in complete_ids]
        for condition in CONDITIONS
    }

    lines = [
        "# Paired evaluation summary",
        "",
        f"- Records: {len(records)}",
        f"- Complete pairs: {len(complete_ids)}",
        f"- Unpaired baseline records: {len(baseline_ids - skill_ids)}",
        f"- Unpaired Skill records: {len(skill_ids - baseline_ids)}",
    ]
    if len(complete_ids) < 10:
        lines.append("- Claim status: debugging/preliminary only; fewer than 10 complete pairs")
    else:
        lines.append("- Claim status: eligible for a preliminary comparative claim, subject to review quality and limitations")

    if not complete_ids:
        lines.extend(["", "No complete baseline/Skill pairs are available for comparison."])
        return "\n".join(lines) + "\n"

    lines.extend([
        "",
        "## Quality (paired records only)",
        "",
        "| Measure | Baseline | Skill | Difference |",
        "|---|---:|---:|---:|",
    ])
    for metric in METRICS:
        baseline_mean = mean(float(item["scores"][metric]) for item in paired["baseline"])
        skill_mean = mean(float(item["scores"][metric]) for item in paired["skill"])
        difference = None if baseline_mean is None or skill_mean is None else skill_mean - baseline_mean
        lines.append(f"| {metric} (1–5) | {fmt(baseline_mean)} | {fmt(skill_mean)} | {fmt(difference)} |")
    base_composite = mean(composite(item) for item in paired["baseline"])
    skill_composite = mean(composite(item) for item in paired["skill"])
    composite_delta = None if base_composite is None or skill_composite is None else skill_composite - base_composite
    lines.append(f"| weighted quality (0–100) | {fmt(base_composite, 1)} | {fmt(skill_composite, 1)} | {fmt(composite_delta, 1)} |")

    lines.extend([
        "",
        "## Cost and time (paired records only)",
        "",
        "| Measure | Baseline | Skill | Difference | Missing baseline / Skill |",
        "|---|---:|---:|---:|---:|",
    ])
    for field in COST_FIELDS:
        baseline_values = [float(item[field]) for item in paired["baseline"] if item.get(field) is not None]
        skill_values = [float(item[field]) for item in paired["skill"] if item.get(field) is not None]
        baseline_mean = mean(baseline_values)
        skill_mean = mean(skill_values)
        difference = None if baseline_mean is None or skill_mean is None else skill_mean - baseline_mean
        missing = f"{len(complete_ids) - len(baseline_values)} / {len(complete_ids) - len(skill_values)}"
        lines.append(f"| {field} | {fmt(baseline_mean)} | {fmt(skill_mean)} | {fmt(difference)} | {missing} |")

    lines.extend([
        "",
        "## Hard failures (paired records only)",
        "",
        "| Condition | Records with ≥1 failure | Failure rate | Failure types |",
        "|---|---:|---:|---|",
    ])
    for condition in CONDITIONS:
        condition_records = paired[condition]
        failed = [item for item in condition_records if item.get("hard_failures")]
        counts = Counter(failure for item in condition_records for failure in item.get("hard_failures", []))
        failure_text = ", ".join(f"{name}: {count}" for name, count in sorted(counts.items())) or "none"
        lines.append(
            f"| {condition} | {len(failed)} | {len(failed) / len(condition_records):.1%} | {failure_text} |"
        )

    lines.extend([
        "",
        "## Opt-in user feedback (all records; not causal evidence)",
        "",
        f"Unique participant codes with feedback: {len({record['participant_code'] for record in records if isinstance(record.get('participant_code'), str) and any(record.get('user_feedback', {}).get(field) is not None for field in USER_FIELDS)})}",
        "",
        "| Measure | Baseline | Skill | Missing baseline / Skill |",
        "|---|---:|---:|---:|",
    ])
    for field in USER_FIELDS:
        values: dict[str, list[float]] = {condition: [] for condition in CONDITIONS}
        counts: dict[str, int] = {condition: 0 for condition in CONDITIONS}
        totals: dict[str, int] = {condition: 0 for condition in CONDITIONS}
        for record in records:
            condition = record["condition"]
            totals[condition] += 1
            value = record.get("user_feedback", {}).get(field)
            if isinstance(value, bool):
                values[condition].append(float(value))
                counts[condition] += 1
            elif isinstance(value, (int, float)) and not isinstance(value, bool):
                values[condition].append(float(value))
                counts[condition] += 1
        baseline_mean = mean(values["baseline"])
        skill_mean = mean(values["skill"])
        missing = f"{totals['baseline'] - counts['baseline']} / {totals['skill'] - counts['skill']}"
        lines.append(f"| {field} | {fmt(baseline_mean)} | {fmt(skill_mean)} | {missing} |")

    lines.extend([
        "",
        "## Required interpretation notes",
        "",
        "- Review model, tool, Skill-version, date, rater blinding, and access-limit differences before attributing the score difference to the Skill.",
        "- User ratings and follow-through are experience signals, not proof of factual accuracy or causality.",
        "- Report null and negative differences; do not exclude hard failures from the headline.",
    ])
    return "\n".join(lines) + "\n"


def self_test() -> None:
    records: list[dict[str, Any]] = []
    for pair_number in (1, 2):
        for condition, offset in (("baseline", 0), ("skill", 1)):
            score = min(5, 2 + pair_number + offset)
            records.append(
                {
                    "pair_id": f"pair-{pair_number}",
                    "task_id": f"task-{pair_number}",
                    "condition": condition,
                    "participant_code": f"participant-{pair_number}",
                    "scores": {metric: score for metric in METRICS},
                    "reviewer_reason": {metric: "synthetic self-test reason" for metric in METRICS},
                    "hard_failures": [] if condition == "skill" else ["excessive_length"],
                    "input_tokens": 100 + offset,
                    "output_tokens": 200 + offset,
                    "duration_seconds": 10 + offset,
                    "cost_usd": None,
                    "user_feedback": {"first_action_recall": condition == "skill"},
                }
            )
    report = summarize(records)
    required = ("Complete pairs: 2", "citation_support", "excessive_length: 2", "debugging/preliminary")
    if any(item not in report for item in required):
        raise AssertionError("self-test report is missing expected content")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("records", nargs="?", help="JSONL file path, or - for stdin")
    parser.add_argument("--template", action="store_true", help="print one privacy-safe record template")
    parser.add_argument("--self-test", action="store_true", help="run the embedded synthetic code test")
    args = parser.parse_args()

    try:
        if args.template:
            print(json.dumps(template(), ensure_ascii=False, indent=2))
            return 0
        if args.self_test:
            self_test()
            print("Self-test passed.")
            return 0
        if not args.records:
            parser.error("records is required unless --template or --self-test is used")
        print(summarize(load_jsonl(args.records)), end="")
        return 0
    except (OSError, ValueError, AssertionError) as exc:
        print(f"Evaluation summary failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
