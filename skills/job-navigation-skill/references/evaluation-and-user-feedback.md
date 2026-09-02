# Effectiveness evaluation and user feedback

Read this file when evaluating the Skill, running a beta, comparing it with a baseline, or reviewing user outcomes. Do not load it for ordinary advice.

## Claims ladder

Keep four claims separate:

1. **Structurally valid** — files, frontmatter, references, and eval definitions pass validation.
2. **Behaviorally compliant** — observed outputs satisfy predefined assertions on tested model/tool versions.
3. **Comparatively better** — paired tests outperform a no-Skill baseline on predefined measures.
4. **Helpful in practice** — real users understand, act on, and benefit from the advice over time.

Never use evidence from a lower rung to claim a higher rung. A synthetic script self-test proves only that the measurement code runs.

## Trigger evaluation

Keep discovery tests separate from output-quality tests. Run `evals/trigger-cases.yaml` without explicitly naming the Skill and record whether the host selected it. Include colloquial Chinese and English prompts, missing-material cases that should still trigger a guardrail, and nearby out-of-scope requests. Report false negatives and false positives by agent/model/version; a case definition alone is not evidence that automatic discovery works.

## Paired baseline protocol

For every comparison:

- use the same sanitized user prompt, attachments, model/version, tool access, geography, research cutoff, and time budget;
- run a neutral baseline without this Skill and a Skill condition without adding hints about the expected answer;
- randomize order across tasks when practical and hide the condition from human reviewers;
- preserve inaccessible-source and tool-error information;
- record output tokens, elapsed time, and actual cost when available; use `null`, never estimates presented as measurements;
- score outputs before looking at aggregate results and retain negative or null results.

Use at least 10 complete pairs for a preliminary comparative claim. Treat smaller samples as debugging evidence. Include diverse job-search tasks: missing resume, sparse sources, career change, early-career candidate, conflicting evidence, user-capacity constraints, and a target-role skill or course investment before making broad claims.

## Evaluation measures

Score each quality measure from 1–5 using a written reviewer reason:

- `citation_support`: cited sources actually support pivotal claims and coverage limits are disclosed;
- `evidence_calibration`: fact, inference, forecast, and recommendation are not conflated;
- `personalization`: advice uses only supplied user evidence and material constraints;
- `actionability`: actions are prioritized, feasible, measurable, and have fast feedback;
- `clarity_and_load`: a new user can identify the decision and first action without decoding jargon or a long task list.

Record hard failures separately:

- `fabricated_user_fact`
- `unsupported_citation`
- `sensitive_query_leak`
- `false_completeness`
- `missed_material_constraint`
- `unusable_action_plan`
- `excessive_length`
- `inaccessible_source_not_disclosed`

Do not let a high average score hide a hard failure. Report per-metric differences, hard-failure rates, and cost/time differences rather than only one composite score.

## Real-user layer

Recruit users from the actual first-release audience before expanding scope. For career beta testing, include students, recent graduates, and career changers with different levels of AI and job-search familiarity.

Collect only opt-in, minimal, non-identifying measures:

- immediate: first-action recall, usefulness 1–5, perceived effort 1–5, and the action judged unrealistic;
- 7-day: whether the first action was attempted or completed and why not;
- 30-day: portfolio/interview/application signals relevant to the plan, plus material context changes.

Treat ratings and self-reports as user-experience evidence, not proof of factual accuracy or causality. Report attrition and missing follow-ups. Do not store prompts, resumes, names, contact details, employer identities, or raw model outputs in a public repository.

## Preliminary success gate

Predefine the gate before evaluation. A reasonable beta gate is:

- no increase in hard-failure rate;
- improvement in citation support and actionability without a material decline in clarity;
- users can state the first action and the plan fits their declared weekly capacity;
- token, time, and cost tradeoffs are reported, even when worse;
- no effectiveness claim if fewer than 10 paired tasks or 10 relevant users have usable data.

These are product release criteria, not statistical or scientific proof. Change thresholds only prospectively and document why.

## Recording and reporting

Use `scripts/summarize_evals.py` with privacy-safe JSONL records. Keep raw results outside the public repository. A record must identify the task and condition but must not contain the prompt or personal content.

Report:

1. sample size and missing fields;
2. baseline versus Skill quality measures;
3. token, time, and cost differences;
4. hard failures by type;
5. user comprehension and follow-through;
6. null/negative findings and access limitations;
7. model, tool, Skill version, and evaluation dates.
