<div align="center">

# Evidence-Based Personal Advisor

### Current research → your actual evidence → a few actions you can finish

[简体中文](README.zh-CN.md) · [How it works](ARCHITECTURE.md) · [Roadmap](ROADMAP.md) · [Contributing](CONTRIBUTING.md)

![Status](https://img.shields.io/badge/status-public_beta-f59e0b)
![Version](https://img.shields.io/badge/version-0.2.0--beta-2563eb)
![Codex Skill](https://img.shields.io/badge/Codex-Skill-111827)
![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB)
![License](https://img.shields.io/badge/license-MIT-16a34a)

`v0.2.0-beta`

</div>

I did not need AI to sound more confident. I needed it to understand my situation, research the world as it is now, show where the evidence stops, and tell me what to do first.

So I turned that workflow into a Codex Skill.

Now it is open source—and deliberately still a beta.

---

> **Important:** this is a decision filter, not an oracle. It searches, compares, and prioritizes. It should say “the evidence is not strong enough” when sources are blocked, stale, conflicting, or too sparse. You review the result and keep the final decision.

## What is this?

**Evidence-Based Personal Advisor** turns Codex into a research-driven decision partner for career, education, and personal-development questions.

Give it a goal, your constraints, and the evidence you actually have. It can then:

- research current official, academic, company, and market sources;
- separate sourced facts from inference, forecasts, and recommendations;
- compare market requirements with your real projects, skills, and limitations;
- use only the analytical models that can change the decision;
- expose contradictions, blocked sources, and low-confidence claims;
- return one direction and no more than three immediate actions before optional detail;
- set a review date so the recommendation can change when reality changes.

Career research is the strongest module today: recent job-description sampling, deduplication, role comparison, resume-evidence gaps, skill prioritization, and capacity-bounded 30/60/90-day plans.

## What comes back?

```text
BOTTOM LINE
Test AI operations before making AI product manager your only target.
Your analytics evidence is stronger than your product-ownership evidence.

NEXT THREE ACTIONS
1. Turn one project into a user problem → decision → result case. 2 hours.
2. Tag repeated requirements in 10 usable first-party JDs. 90 minutes.
3. Get two practitioners to critique that case. 45 minutes.

EVIDENCE
Fact · Medium confidence: [current, cited market signal]
Your evidence: [only what the supplied material supports]
Inference: [why the overlap points to one role family]

MAIN LIMIT
Two requested job boards were inaccessible; the sample is directional.

REVIEW
Revisit after 10 targeted applications or two practitioner interviews.
```

The goal is not a longer answer. It is a decision you can inspect: **what is known, what is uncertain, what it means for you, and what happens next.**

See the [fictional abbreviated example](examples/early-career-ai-role-brief.md) for the output shape. It is not market evidence or a success claim.

## What it does

| Capability | What the Skill does | What it refuses to pretend |
|---|---|---|
| Current research | Uses recent first-party and authoritative sources when time matters | That every platform or page was accessible |
| Evidence calibration | Labels central claims high, medium, or low confidence | That a famous framework proves a claim |
| Personalization | Compares findings with supplied constraints and inspectable evidence | That unstated skills or achievements exist |
| Career analysis | Deduplicates JDs and separates required, preferred, and contextual signals | That posting frequency equals total labor demand |
| Action planning | Leads with ≤3 actions, effort, and proof of completion | That a user has unlimited time or energy |
| Outcome review | Tracks behavior and outcome signals at a review point | That a rating or one before/after story proves causality |
| Evaluation | Compares baseline and Skill runs with cost and failure reporting | That structural tests prove real-world benefit |

## Quick start

Requirements: **Codex** and **Python 3.9+**.

Download or clone this repository, open a terminal inside it, and run:

```bash
python3 scripts/install.py
```

The installer validates the repository, copies the Skill to `${CODEX_HOME:-~/.codex}/skills/evidence-based-personal-advisor`, and refuses to overwrite an existing installation.

On the next Codex turn:

```text
Use $evidence-based-personal-advisor.

I am a new data-science graduate targeting AI product or AI operations roles
in Shenzhen. Research the last six months of industry and job trends, sample
recent JDs, compare them with my resume, identify evidence gaps, and give me a
30/60/90-day plan. Separate facts, inference, and recommendations. Disclose
source confidence and access limits. I can spend 6 hours per week.
```

Or ask naturally after installation:

```text
Help me compare these career options using current evidence and my constraints.
```

## Give it useful context

The Skill gets better when the decision is concrete. Share only what is necessary:

- goal and geography;
- decision deadline;
- weekly time, budget, and non-negotiable constraints;
- resume, portfolio, transcript, or project evidence after removing unnecessary identifiers;
- what success would look like and what you want to avoid.

If a resume-gap analysis is requested without a resume or factual background, the Skill must ask for it. It must not construct a fictional candidate profile.

## Three research modes

| Mode | Use it for | Typical scope |
|---|---|---|
| `quick` | Orientation, “give me a direction,” low-stakes tests | 4–8 useful sources, 1–2 models, short answer |
| `standard` | Most career and education decisions | 8–15 useful sources, 2–4 source types, 1–3 models |
| `deep` | Explicitly systematic or consequential comparisons | Broader inclusion rules, contradiction map, explicit limitations |

These are scope controls, not quotas. Research stops when two successive rounds add no decision-changing evidence.

## Career workflow

```text
recent sources and deduplicated JDs
                 │
                 ▼
normalized hiring requirements
                 │
                 ▼
your inspectable evidence (A/B/C/D/U)
                 │
                 ▼
match, proof gap, skill gap, or experience gap
                 │
                 ▼
do now · test cheaply · build next · defer
```

Candidate evidence is deliberately separate from source confidence. A strong market source can reveal that a candidate has weak proof; a well-documented project can remain strong candidate evidence even when market demand is uncertain.

Read the [architecture](ARCHITECTURE.md) for the complete runtime and evaluation flow.

## Privacy and control

This is a locally installed Skill, not a hosted resume service. The repository does not receive or collect your data.

That does **not** mean inference is offline: material you give Codex may be processed by the AI provider and tools active in your environment. Review their terms and settings. The Skill instructs Codex to keep resume text, identifiers, contact details, and confidential records out of web searches and external queries.

It does not send applications, contact employers, publish files, or collect evaluation data automatically. You decide what to share and what to act on.

## What is actually validated?

| Claim level | Current status |
|---|---|
| Repository structure and privacy checks | Passed locally and enforced in GitHub Actions |
| Installer and evaluation summarizer execute | Passed local install and synthetic self-tests |
| Behavioral compliance across models/tools | Evaluation scenarios exist; repeatable results are not yet published |
| Better than a neutral baseline | Not yet established |
| Improves real user outcomes | Not yet established |

There are no fabricated adoption numbers here. Until at least 10 complete paired tasks and 10 relevant users produce usable data, accuracy, actionability, and token savings remain design goals—not proven benefits.

## Evaluate it instead of trusting it

The evaluation protocol holds prompt, materials, model, tools, research window, and time budget constant across a neutral baseline and a Skill run. It measures:

- citation support;
- evidence calibration;
- personalization;
- actionability;
- clarity and cognitive load;
- tokens, elapsed time, actual cost, missing data, and hard failures.

Print a privacy-safe local record template:

```bash
python3 skills/evidence-based-personal-advisor/scripts/summarize_evals.py --template
```

Summarize paired JSONL records:

```bash
python3 skills/evidence-based-personal-advisor/scripts/summarize_evals.py path/to/results.jsonl
```

Raw prompts, resumes, names, employer identities, and model outputs do not belong in this public repository. Read the [evaluation protocol](skills/evidence-based-personal-advisor/references/evaluation-and-user-feedback.md) before reporting results.

## Project structure

```text
evidence-based-personal-advisor/
├── skills/evidence-based-personal-advisor/
│   ├── SKILL.md                         # Core decision router
│   ├── agents/openai.yaml               # Codex UI metadata
│   ├── references/                      # Loaded only when relevant
│   ├── evals/cases.yaml                 # Eight behavioral scenarios
│   └── scripts/summarize_evals.py       # Local paired-result summary
├── examples/                            # Clearly labeled output-shape examples
├── scripts/install.py                   # Transactional, non-overwriting installer
├── scripts/validate_repo.py             # Structure, link, privacy, and secret checks
├── ARCHITECTURE.md
├── ROADMAP.md
├── CHANGELOG.md
└── .github/                             # CI, issue forms, and PR checklist
```

## FAQ

**Is this a job-search automation system?**

No. It researches and advises. It does not auto-apply, message recruiters, or track applications.

**Does it scrape BOSS, LinkedIn, or Indeed?**

The Skill has no bundled crawler. Codex uses the web access available in the active environment and must disclose blocked, personalized, or inaccessible sources.

**Will it rewrite my resume?**

It can diagnose evidence gaps and help rewrite supported material. It must not invent achievements, individual ownership, or metrics.

**Why not add more decision frameworks?**

Because frameworks are cheap and validation is scarce. The [roadmap](ROADMAP.md) prioritizes paired tests, failures, and real-user feedback.

**Can I use it outside career decisions?**

Yes, but career research is the most developed module. Broader effectiveness has not been established.

## Contributing

Useful contributions include failure cases, clearer language, new behavioral tests, source-evaluation improvements, translations, and privacy-safe aggregate evaluation results. Start with [CONTRIBUTING.md](CONTRIBUTING.md) and follow the [code of conduct](CODE_OF_CONDUCT.md).

Do not open a public issue containing a resume, raw prompt, contact information, private URL, or confidential record. Use the provided issue forms for bugs, opt-in user research, and aggregate evaluations.

## Disclaimer

This Skill produces research-based recommendations, not truth or guaranteed outcomes. Sources can be wrong, incomplete, stale, inaccessible, or misinterpreted; models can hallucinate. Review generated claims and career material before acting. Medical, legal, financial, and other high-stakes decisions still require qualified professional review where appropriate.

See [SECURITY.md](SECURITY.md) for private reporting and privacy guidance.

## License

[MIT](LICENSE). Use it, inspect it, adapt it, and report where it fails.
