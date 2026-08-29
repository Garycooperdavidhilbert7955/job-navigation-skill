# Contributing

Contributions that make the Skill clearer, safer, more evidence-aware, or more token-efficient are welcome.

## Before opening a pull request

1. Keep `SKILL.md` concise and move conditional detail into `references/`.
2. Do not add personal data, copied resumes, proprietary job descriptions, secrets, or local filesystem paths.
3. Do not weaken source transparency or permit unsupported candidate claims.
4. Add or update a behavioral case in `evals/cases.yaml` when changing workflow behavior.
5. Do not describe structural validation or synthetic self-tests as evidence of user benefit.
6. For effectiveness comparisons, use paired baseline/Skill runs and report cost, hard failures, missing data, and null or negative findings.
7. Keep raw prompts, resumes, names, contact details, employer identities, and model outputs out of the repository. Contribute only minimal, non-identifying aggregate results when users have opted in.
8. Run:

```bash
python3 scripts/validate_repo.py
python3 skills/evidence-based-personal-advisor/scripts/summarize_evals.py --self-test
```

## Pull requests

Explain the user problem, the behavioral change, and how you verified it. Prefer small, reviewable changes. Do not include generated research output as a permanent fixture unless it is a minimal, privacy-safe evaluation case.

By contributing, you agree that your contribution is licensed under the MIT License.
