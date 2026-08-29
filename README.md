# Evidence-Based Personal Advisor

> Stop asking AI for generic advice. Turn current evidence, proven frameworks, and your real constraints into decisions you can act on.

[简体中文](README.zh-CN.md) · [Skill source](skills/evidence-based-personal-advisor/SKILL.md) · [Contributing](CONTRIBUTING.md)

**Evidence-Based Personal Advisor** is an open-source Codex Skill for evidence-based career, education, and personal-development decisions. Codex researches current sources, compares them with the facts and constraints you provide, and produces a prioritized action plan.

It is especially useful for career direction, job-market research, JD sampling, resume-gap analysis, skill planning, career changes, and education choices.

## What you get

```text
Fact · High confidence: Recent first-party JDs repeatedly require SQL and funnel analysis.
Limit: The sample is directional because one job board blocked full access.
Your evidence: SQL coursework exists, but no inspectable business-analysis artifact (Grade U/B).
Do now: Publish one SQL + dashboard case; review application conversion after 20 targeted applications.
```

The goal is not a longer answer. It is a clearer decision: **what the evidence supports, what remains uncertain, what it means for you, and what to do next.**

## Why use it?

Most AI advice fails in one of three ways: it is generic, outdated, or overconfident. This Skill adds practical guardrails:

- **Current evidence:** prioritizes primary sources and records the research cutoff.
- **Calibrated confidence:** separates facts, inference, forecasts, and recommendations.
- **Personal fit:** tests advice against your goals, constraints, evidence, and opportunity cost.
- **Model discipline:** uses only 1–3 frameworks that can change the decision.
- **Token discipline:** offers quick, standard, and deep modes designed to limit unnecessary research; comparative token savings are not yet proven.
- **Career rigor:** deduplicates job ads and grades candidate evidence without inventing achievements.
- **Human-sized plans:** leads with one direction and no more than three immediate actions before optional detail.

## Who is it for?

- Students and early-career candidates choosing roles or closing skill gaps
- Professionals considering a career change
- Job seekers comparing current demand with their resume evidence
- People making consequential education or personal-development decisions
- Anyone who wants sourced advice instead of motivational filler

It is not intended for simple factual lookups, unsupported resume rewriting, diagnosis, or professional medical/legal/financial replacement.

## How it works

1. **Frame** the decision, context, constraints, and success criteria.
2. **Scope** the research as quick, standard, or deep.
3. **Search** primary sources first, then strong synthesis and market signals.
4. **Evaluate** authority, directness, recency, method, independence, and consistency.
5. **Select** the smallest useful set of business, academic, or practice models.
6. **Personalize** findings against the user's evidence and constraints.
7. **Prioritize** actions as do now, test cheaply, build next, or defer.
8. **Review** progress with measurable signals and a review date.

For career analysis, it additionally maps:

`job requirement → demand band → candidate evidence → evidence grade → gap type → next action`

Candidate evidence is graded from **A** (externally validated) to **U** (unsupported), preventing team, simulated, or forecast outcomes from being presented as verified individual achievements.

The first screen stays intentionally simple: one bottom line, up to three immediate actions, and the main uncertainty. A 30/60/90-day plan is capacity-bounded and keeps only the first seven days in the immediate layer.

## Install

Requirements: **Codex** and **Python 3.9+**.

From this GitHub page, choose **Code → Download ZIP** or clone using the URL shown under **Code**. Open a terminal in the extracted/cloned repository, then run:

```bash
python3 scripts/install.py
```

The installer copies the Skill to `${CODEX_HOME:-~/.codex}/skills/evidence-based-personal-advisor` and refuses to overwrite an existing installation.

The Skill becomes available on the next Codex turn.

## Use

Invoke it explicitly:

```text
Use $evidence-based-personal-advisor.

I am a new data-science graduate targeting AI product roles in Shenzhen.
Research the last six months of market and job-description trends, compare them
with my resume, identify evidence gaps, and give me a 30/60/90-day plan.
Distinguish facts, inference, and recommendations, and disclose research limits.
```

Or ask naturally once the Skill is installed:

```text
Help me compare these career options using current evidence and my constraints.
```

### Research modes

| Mode | Best for | Typical scope |
|---|---|---|
| `quick` | Orientation and low-stakes questions | 4–8 sources, 1–2 models |
| `standard` | Most career and personal decisions | 8–15 sources, 1–3 models |
| `deep` | Systematic comparison or consequential decisions | Broader sources, contradiction mapping, explicit limits |

## Repository layout

```text
skills/evidence-based-personal-advisor/
├── SKILL.md                 # Core workflow and guardrails
├── agents/openai.yaml       # Codex UI metadata
├── references/              # Loaded only when relevant
│   ├── evidence-protocol.md
│   ├── career-module.md
│   ├── evaluation-and-user-feedback.md
│   ├── model-router.md
│   └── output-contract.md
├── evals/cases.yaml         # Behavioral evaluation scenarios
└── scripts/summarize_evals.py # Paired evaluation report
```

## Validation status

The repository and installer have passed structural, privacy, and synthetic code checks. That means the Skill is installable and its evaluation machinery runs; it does **not** yet prove that the Skill improves accuracy, actionability, token use, or real-world outcomes.

Effectiveness requires paired runs using the same prompt, materials, model, tools, research window, and time budget: one neutral baseline without the Skill and one Skill condition. Reviewers score citation support, evidence calibration, personalization, actionability, and clarity/cognitive load while recording tokens, elapsed time, actual cost, and hard failures. Real-user feedback is opt-in and kept separate from factual accuracy.

Print a privacy-safe record template and summarize local JSONL results with:

```bash
python3 skills/evidence-based-personal-advisor/scripts/summarize_evals.py --template
python3 skills/evidence-based-personal-advisor/scripts/summarize_evals.py path/to/results.jsonl
```

Raw prompts, resumes, personal data, and model outputs should remain outside the public repository. Fewer than 10 complete pairs or 10 relevant users are treated as debugging evidence, not an effectiveness claim. See the [evaluation and user-feedback protocol](skills/evidence-based-personal-advisor/references/evaluation-and-user-feedback.md).

## Trust and limitations

- The Skill improves research discipline; it does not guarantee exhaustive search or correct source content.
- Job boards can be stale, duplicated, personalized, or inaccessible.
- Frameworks organize reasoning; they are not empirical evidence.
- Structural eval assertions do not demonstrate better decisions or user outcomes.
- Users should remove sensitive information before sharing resumes or personal records.
- High-stakes decisions still require qualified professional review where appropriate.

## Validate

```bash
python3 scripts/validate_repo.py
```

Validation checks the Skill structure, frontmatter, naming, required resources, evaluation cases, local-path leakage, and common secret patterns. GitHub Actions also runs the evaluation summarizer's synthetic self-test on every push and pull request.

## License

[MIT](LICENSE). Use, adapt, and improve it—with attribution.
