# Contributing

Contributions that make the Skill clearer, safer, more evidence-aware, or more token-efficient are welcome.

## Before opening a pull request

1. Keep `SKILL.md` concise and move conditional detail into `references/`.
2. Do not add personal data, copied resumes, proprietary job descriptions, secrets, or local filesystem paths.
3. Do not weaken source transparency or permit unsupported candidate claims.
4. Add or update a behavioral case in `evals/cases.yaml` when changing workflow behavior.
5. Run:

```bash
python3 scripts/validate_repo.py
```

## Pull requests

Explain the user problem, the behavioral change, and how you verified it. Prefer small, reviewable changes. Do not include generated research output as a permanent fixture unless it is a minimal, privacy-safe evaluation case.

By contributing, you agree that your contribution is licensed under the MIT License.

