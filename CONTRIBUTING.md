# Contributing

This project needs observed failures more than extra theory.

Useful contributions include:

- a minimal case where the Skill invented, missed, overloaded, or overclaimed;
- clearer language for a first-time or non-technical user;
- a behavioral assertion that catches a real regression;
- safer handling of resumes, web queries, or inaccessible sources;
- privacy-safe aggregate baseline/Skill results;
- translations that preserve evidence boundaries rather than translating word-for-word.

## Start with an issue

Use the matching GitHub form:

- **Bug report** for installation, validation, or behavior failures;
- **User research feedback** for opt-in clarity, workload, or follow-through feedback;
- **Aggregate evaluation result** for paired findings without prompts or personal data;
- **Feature request** for a concrete user problem, not a framework wishlist.

Never post resumes, names, contact details, private prompts, raw model outputs, employer identities, proprietary JDs, confidential records, secrets, or private URLs.

## Before opening a pull request

1. Keep `SKILL.md` concise; move conditional detail into `references/`.
2. Use imperative language in Skill instructions.
3. Preserve the separation between market-source confidence and candidate evidence.
4. Add or update a case in `evals/cases.yaml` when behavior changes.
5. Do not convert a structural check or synthetic self-test into a benefit claim.
6. Keep examples fictional or explicitly opt-in and redacted.
7. Run:

```bash
python3 scripts/validate_repo.py
python3 skills/evidence-based-personal-advisor/scripts/summarize_evals.py --self-test
```

## Evaluation contributions

Use the [paired evaluation protocol](skills/evidence-based-personal-advisor/references/evaluation-and-user-feedback.md). Keep task, model, tool access, research window, and time budget comparable. Report per-metric results, missing fields, tokens/time/cost, and every hard failure—including null and negative findings.

Fewer than 10 complete pairs are debugging evidence. User ratings are experience evidence, not proof of source accuracy or causal impact.

## Pull requests

Keep one pull request focused on one user problem. Explain:

- the observed failure or unmet need;
- the behavior or artifact that changed;
- how it was tested;
- what remains model-, tool-, geography-, or platform-dependent.

By contributing, you agree that your contribution is licensed under the MIT License and follows the [code of conduct](CODE_OF_CONDUCT.md).
