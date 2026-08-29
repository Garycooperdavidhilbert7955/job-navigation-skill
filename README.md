<div align="center">

# Evidence-Based Personal Advisor

### Current evidence → your actual situation → a few actions you can finish

[简体中文](README.zh-CN.md) · [Architecture](ARCHITECTURE.md) · [Roadmap](ROADMAP.md) · [Contributing](CONTRIBUTING.md)

![Status](https://img.shields.io/badge/status-beta-f59e0b)
![Version](https://img.shields.io/badge/version-0.2.0--beta-2563eb)
![Codex Skill](https://img.shields.io/badge/Codex-local_skill-111827)
![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB)
![License](https://img.shields.io/badge/license-MIT-16a34a)

`v0.2.0-beta`

</div>

I did not need AI to sound more certain. I needed it to understand my situation, research what is true now, show where the evidence stops, and tell me what to do first.

This project turns that workflow into a local Codex Skill.

> **Product position:** career-first evidence-based decision support. Career and job-market research is the first complete module. Education and personal-development questions use the general research workflow but do not yet have dedicated, validated modules.

## Manual map

- [1. Who this is for](#1-who-this-is-for)
- [2. What it does](#2-what-it-does)
- [3. Typical scenarios](#3-typical-scenarios)
- [4. What the result looks like](#4-what-the-result-looks-like)
- [5. Deploy locally](#5-deploy-locally)
- [6. Use it well](#6-use-it-well)
- [7. How it works](#7-how-it-works)
- [8. Technical design and defensibility](#8-technical-design-and-defensibility)
- [9. Privacy, limitations, and safe use](#9-privacy-limitations-and-safe-use)
- [10. Validation status](#10-validation-status)
- [11. Maintenance and troubleshooting](#11-maintenance-and-troubleshooting)

## 1. Who this is for

### Best fit

- students and recent graduates choosing a role or building evidence for one;
- job seekers comparing current JDs with a resume or portfolio;
- career changers deciding which direction to test before paying for a long course;
- professionals comparing locations, industries, roles, or skill investments;
- users who want sourced advice with visible uncertainty instead of motivational filler.

### Not built for

- automatic job applications, recruiter messages, or account automation;
- keyword-only ATS scoring;
- inventing resume achievements, metrics, or individual ownership;
- guaranteeing hiring, admissions, income, or other outcomes;
- replacing qualified medical, legal, financial, or mental-health professionals.

This is a **decision filter, not an oracle**. It researches, compares, and prioritizes. You review the evidence and keep the final decision.

## 2. What it does

| Function | What you receive | Built-in boundary |
|---|---|---|
| Current research | Recent official, academic, company, and market evidence with a cutoff date | No claim that every requested site was accessible |
| Evidence calibration | Facts separated from inference, forecasts, and recommendations | A framework is never treated as empirical proof |
| Personal fit | Findings compared with your stated goals, constraints, and evidence | No unstated skill, experience, or achievement is invented |
| Career-market analysis | Deduplicated JD requirements, demand bands, required/preferred split | Job-ad frequency is not called total labor-market demand |
| Resume evidence review | Skill, evidence, communication, experience, and constraint gaps | Team or simulated outcomes are not rewritten as personal results |
| Skill prioritization | `do now`, `test cheaply`, `build next`, and `defer` | It does not recommend learning every tool in every JD |
| Action planning | One direction, at most three immediate actions, effort, and completion proof | The plan is reduced when time or energy is limited |
| Review loop | Near-term behavior signals, downstream outcomes, and a review trigger | One rating or before/after story is not treated as causal proof |

## 3. Typical scenarios

| Scenario | Give the Skill | It should return |
|---|---|---|
| New graduate choosing roles | Degree, projects, location, target date, weekly capacity | Suitable role families, evidence gaps, and a small market test |
| Resume vs. current market | Redacted resume plus target role and geography | JD requirement matrix, candidate evidence grades, and priorities |
| Career change | Transferable experience, constraints, options, risk tolerance | Direction comparison, cheap validation experiments, and defer list |
| Industry or role trend | Geography, time window, titles/synonyms, decision to make | Sourced trend signals, contradictions, limits, and implications |
| Skill/course choice | Candidate gaps, course details, price, time, alternatives | Whether to learn, test first, choose another proof path, or defer |
| 30/60/90-day plan | Target, baseline, weekly capacity, deadline | Capacity-bounded milestones with only the first week shown as immediate work |

### What happens if information is missing?

- If resume-gap analysis is requested without a resume or factual background, the Skill asks for it before creating a candidate comparison.
- If role or geography is missing and materially changes the market, it asks one concise career-scope question at a time.
- If a platform is blocked, it reports the failure and narrows the claim instead of fabricating results.

## 4. What the result looks like

The first screen is designed for a tired or inexperienced user:

```text
BOTTOM LINE
Test AI operations before making AI product manager your only target.
Your current analytics evidence is stronger than your product-ownership evidence.

NEXT THREE ACTIONS
1. Rewrite one project as user problem → decision → result. 2 hours.
2. Tag repeated requirements in 10 usable first-party JDs. 90 minutes.
3. Ask two practitioners to critique that case. 45 minutes.

MAIN UNCERTAINTY
Two requested job boards were inaccessible, so this is a directional sample.
```

Supporting detail follows only when useful:

```text
FACT · Medium confidence
[Current market observation with a nearby citation and date]

YOUR EVIDENCE
[Only what the supplied resume, project, or portfolio supports]

INFERENCE
[Why the overlap points toward one role family]

RECOMMENDATION
[A personalized, reversible next step]

REVIEW
Revisit after 10 targeted applications or two practitioner interviews.
```

The goal is not a longer answer. It is a decision you can inspect: **what is known, what is uncertain, what it means for you, and what happens next.**

See the [fictional abbreviated example](examples/early-career-ai-role-brief.md). It demonstrates output shape only; it is not current market evidence or a success claim.

## 5. Deploy locally

### 5.1 Understand the deployment model

This repository packages a **local Codex Skill**. It copies a folder containing `SKILL.md`, references, eval definitions, metadata, and a local evaluation script into a Codex Skill directory.

It does not upload the Skill, your resume, or evaluation records to the [OpenAI Skills API](https://developers.openai.com/api/reference/python/resources/skills/methods/create). Material you later provide to Codex may still be processed by the AI provider and enabled tools; see [Privacy](#9-privacy-limitations-and-safe-use).

### 5.2 Requirements

- Codex desktop or another Codex environment that supports local Skills;
- Python 3.11 or later;
- a downloaded or cloned copy of this repository;
- network access only when your request needs current research.

No Python package installation is required. The installer and validation scripts use the standard library.

### 5.3 Download the repository

From the GitHub repository page, choose one method:

**Download ZIP**

1. Select **Code → Download ZIP**.
2. Extract the archive.
3. Open Terminal or PowerShell inside the extracted repository—not inside the nested Skill folder.

**Git clone**

1. Select **Code** on the GitHub repository page.
2. Copy the HTTPS or SSH URL.
3. Clone it with your Git client.
4. Open Terminal or PowerShell in the resulting `evidence-based-personal-advisor` folder.

The remaining commands in this manual assume that this repository folder is your current working directory.

### 5.4 Validate before installation

macOS, Linux, or PowerShell:

```bash
python3 scripts/validate_repo.py
```

On Windows, use `python` instead of `python3` if that is how Python is registered:

```powershell
python scripts\validate_repo.py
```

Expected output:

```text
Validation passed.
Skill: evidence-based-personal-advisor
Evaluation cases: 8
```

Validation checks required files, frontmatter, version consistency, local-path leakage, broken relative links, symlinks, and common secret patterns. It does not prove that web research or recommendations are correct.

### 5.5 Install to the default Codex Skill directory

macOS or Linux:

```bash
python3 scripts/install.py
```

Windows PowerShell:

```powershell
python scripts\install.py
```

The installer resolves the destination as:

```text
${CODEX_HOME}/skills/evidence-based-personal-advisor
```

If `CODEX_HOME` is not set, it uses:

```text
~/.codex/skills/evidence-based-personal-advisor
```

The install is transactional: the repository is validated first, symlinks are rejected, files are copied to a temporary staging directory, and the existing destination is never overwritten.

### 5.6 Install to a custom Skill directory

Use a custom destination only when your Codex environment is configured to discover that directory:

```bash
python3 scripts/install.py --dest "/absolute/path/to/codex/skills"
```

Example for a personal macOS Skill library:

```bash
python3 scripts/install.py --dest "$HOME/Desktop/codex/skill"
```

`--dest` must point to the parent Skill directory. The installer creates the final `evidence-based-personal-advisor` folder inside it.

### 5.7 Verify the installed files

Default macOS/Linux installation:

```bash
test -f "$HOME/.codex/skills/evidence-based-personal-advisor/SKILL.md" && echo "Skill files installed"
```

Windows PowerShell:

```powershell
Test-Path "$HOME\.codex\skills\evidence-based-personal-advisor\SKILL.md"
```

Then start a new Codex task and invoke the Skill explicitly:

```text
Use $evidence-based-personal-advisor to research my decision using current evidence and my constraints.
```

Local Skill discovery can vary by Codex environment and configuration. If the Skill is not listed or triggered, restart Codex, verify the destination, and use the explicit `$evidence-based-personal-advisor` invocation.

### 5.8 Upgrade safely

The installer intentionally refuses to overwrite an existing Skill. Use a recoverable upgrade:

1. Download or pull the new repository version.
2. Validate the new repository.
3. Move the installed Skill to a backup name.
4. Run the installer again.
5. Start a new Codex task and run one known prompt.
6. Remove the backup only after the new version works.

Default macOS/Linux example:

```bash
mv "$HOME/.codex/skills/evidence-based-personal-advisor" \
  "$HOME/.codex/skills/evidence-based-personal-advisor.backup"
python3 scripts/install.py
```

Rollback:

```bash
mv "$HOME/.codex/skills/evidence-based-personal-advisor" \
  "$HOME/.codex/skills/evidence-based-personal-advisor.failed"
mv "$HOME/.codex/skills/evidence-based-personal-advisor.backup" \
  "$HOME/.codex/skills/evidence-based-personal-advisor"
```

For a custom destination, replace `$HOME/.codex/skills` with the same parent directory used during installation.

Windows PowerShell upgrade:

```powershell
Move-Item "$HOME\.codex\skills\evidence-based-personal-advisor" `
  "$HOME\.codex\skills\evidence-based-personal-advisor.backup"
python scripts\install.py
```

Windows PowerShell rollback:

```powershell
Move-Item "$HOME\.codex\skills\evidence-based-personal-advisor" `
  "$HOME\.codex\skills\evidence-based-personal-advisor.failed"
Move-Item "$HOME\.codex\skills\evidence-based-personal-advisor.backup" `
  "$HOME\.codex\skills\evidence-based-personal-advisor"
```

### 5.9 Uninstall without immediate deletion

Move the installed folder out of the active Skill directory:

```bash
mv "$HOME/.codex/skills/evidence-based-personal-advisor" \
  "$HOME/.codex/evidence-based-personal-advisor.uninstalled"
```

Restart Codex and confirm the Skill is no longer discovered. Delete the moved copy later only if you no longer need rollback.

Windows PowerShell:

```powershell
Move-Item "$HOME\.codex\skills\evidence-based-personal-advisor" `
  "$HOME\.codex\evidence-based-personal-advisor.uninstalled"
```

## 6. Use it well

### 6.1 Prepare only the context the decision needs

- goal and geography;
- decision deadline;
- weekly time, budget, risk tolerance, and non-negotiable constraints;
- redacted resume, portfolio, transcript, or project evidence;
- definition of success and what you want to avoid.

Remove phone numbers, personal email addresses, IDs, exact home addresses, private links, and unrelated confidential material.

### 6.2 Choose a research mode

| Mode | Use it for | General research scope |
|---|---|---|
| `quick` | Orientation, “give me a direction,” cheap tests | 4–8 useful sources, 1–2 models, short answer |
| `standard` | Most career and education decisions | 8–15 contextual sources, 2–4 source types, 1–3 models |
| `deep` | Explicitly systematic or consequential comparisons | Broader inclusion rules, contradiction mapping, explicit limitations |

For standard career analysis, the career module additionally targets 20–40 deduplicated JD records when access and market size permit. JD record count and contextual-source count are separate controls. Fewer JDs are acceptable when disclosed; neither number is a quota.

Research stops when two successive rounds add no decision-changing evidence.

### 6.3 Prompt templates

**Resume and current market**

```text
Use $evidence-based-personal-advisor.

I am targeting [role] in [geography] by [date]. Research the last [time window]
of industry and job trends, sample recent JDs, and compare them with my redacted
resume. Identify role fit, skill gaps, evidence gaps, and the three highest-value
actions. Separate facts, inference, and recommendations. I can spend [hours]
per week. Disclose inaccessible sources and the research cutoff.
```

**Career change**

```text
Use $evidence-based-personal-advisor to compare [option A], [option B], and
[option C]. My transferable evidence is [brief facts]. My constraints are
[time/budget/location/risk]. Use current market evidence and recommend the
cheapest experiments that could change the decision before I commit.
```

**Education or course decision**

```text
Use $evidence-based-personal-advisor to assess whether [course/program] is the
best way to close [specific gap]. Compare price, time, alternative proof paths,
and current role demand. State that this is using the general workflow rather
than a dedicated validated education module.
```

## 7. How it works

```text
your question and redacted materials
                │
                ▼
decision framing and research budget
                │
                ▼
claim → best source type → current evidence
                │
                ▼
deduplication, confidence, contradiction checks
                │
                ▼
market evidence ↔ your inspectable evidence
                │
                ▼
one direction → ≤3 immediate actions → review loop
```

For career analysis, the evidence chain is:

```text
JD requirement → demand band → candidate evidence → evidence grade
→ gap type → recommended proof → action priority
```

Candidate evidence uses a separate A/B/C/D/U scale so that a confident market claim cannot manufacture proof that the candidate has a skill.

## 8. Technical design and defensibility

The defensibility is not the number of frameworks. It is the combination of procedures, boundaries, and tests:

1. **Claim-to-source routing** — laws, market scale, job requirements, causal claims, and practitioner friction use different source hierarchies.
2. **Two independent evidence axes** — source confidence and candidate evidence strength are never merged.
3. **JD normalization and deduplication** — syndicated postings are counted once, required and preferred signals stay separate, and posting dates are distinguished from page refresh dates.
4. **Evidence-first model routing** — business, academic, and practice frameworks are selected only after evidence collection and removed when they do not change the action.
5. **Human-sized delivery** — the answer begins with one direction, no more than three immediate actions, effort, and completion proof.
6. **Failure-aware research** — blocked sources, sparse samples, contradictions, and inaccessible platforms are reported as limits instead of silently hidden.
7. **Validation ladder** — structural validity, behavioral compliance, baseline improvement, and real-user benefit are four separate claims.
8. **Privacy-safe evaluation** — local JSONL aggregation records scores, costs, and failures without requiring resumes or raw prompts in the public repository.

Read [ARCHITECTURE.md](ARCHITECTURE.md) for the runtime and evaluation flows.

## 9. Privacy, limitations, and safe use

### Privacy

- The repository does not receive or collect your resume or evaluation data.
- Local installation does not mean offline inference. Codex and enabled tools may send supplied material to the configured AI provider or services.
- The Skill instructs Codex not to put resume text, identifiers, contact details, or confidential records into web searches.
- This is an instructional safeguard, not a network sandbox. Review generated queries when risk is material.

### Research limits

- Job boards may require authentication, personalize results, block automation, or expose stale pages.
- The Skill has no bundled BOSS, LinkedIn, or Indeed crawler. It uses web access available in the active Codex environment.
- JD samples are convenience samples, not statistically representative labor-market surveys.
- Job-ad frequency is a directional demand signal, not total hiring volume.
- Frameworks organize reasoning; they do not prove claims.
- Current sources can still be wrong, incomplete, or misinterpreted.

### User responsibility

- Verify important claims and generated career material before acting or submitting.
- Never accept invented metrics, ownership, credentials, or outcomes.
- Follow the terms of service of websites and data sources you access.
- Use qualified professional review for medical, legal, financial, or other high-stakes decisions where appropriate.

See [SECURITY.md](SECURITY.md) for reporting and privacy guidance.

## 10. Validation status

| Evidence level | Current status |
|---|---|
| Repository structure and privacy checks | Passed locally; CI workflow is configured for GitHub |
| Installer and evaluation summarizer execute | Passed local installation and synthetic self-tests |
| Behavioral compliance across model/tool versions | Eight scenarios exist; repeatable results are not yet published |
| Better than a neutral baseline | Not established |
| Improves real user outcomes | Not established |

There are no fabricated adoption numbers here. Until at least 10 complete paired tasks and 10 relevant users produce usable data, accuracy, actionability, and token savings remain design goals—not proven benefits.

To test the local evaluation machinery:

```bash
python3 skills/evidence-based-personal-advisor/scripts/summarize_evals.py --self-test
python3 skills/evidence-based-personal-advisor/scripts/summarize_evals.py --template
```

Read the [evaluation protocol](skills/evidence-based-personal-advisor/references/evaluation-and-user-feedback.md) before collecting results. Raw prompts, resumes, employer identities, and complete model outputs do not belong in the public repository.

## 11. Maintenance and troubleshooting

| Problem | Check | Next step |
|---|---|---|
| `python3` not found | Run `python --version` | Use `python` on Windows or install a supported Python version |
| Validation fails | Read the first reported missing file, link, local path, or secret | Restore/fix that exact item; do not bypass validation |
| Destination already exists | The installer protects an existing installation | Use the backup-and-upgrade procedure above |
| Skill files exist but Codex does not show it | Confirm the parent directory is a Skill directory for that environment | Start a new task, invoke `$evidence-based-personal-advisor`, then restart Codex if needed |
| Requested platforms are inaccessible | Check authentication and platform restrictions | Provide exported links/text or accept a narrower, clearly labeled sample |
| Answer is too long | Ask for `quick` mode and state weekly capacity | Request only the bottom line, three actions, and main uncertainty |
| Resume analysis invents facts | Stop using the output | Report a privacy-safe bug and remove unsupported claims |

## Project files

```text
evidence-based-personal-advisor/
├── skills/evidence-based-personal-advisor/
│   ├── SKILL.md                         # Core decision router
│   ├── agents/openai.yaml               # Codex UI metadata
│   ├── references/                      # Conditional specialist guidance
│   ├── evals/cases.yaml                 # Eight behavioral scenarios
│   └── scripts/summarize_evals.py       # Local paired-result summary
├── examples/                            # Explicitly labeled examples
├── scripts/install.py                   # Transactional installer
├── scripts/validate_repo.py             # Structure and privacy checks
├── ARCHITECTURE.md
├── ROADMAP.md
├── CHANGELOG.md
└── .github/                             # CI, issue forms, and PR checklist
```

## Contributing and license

Observed failures, clearer language, behavioral tests, translations, and privacy-safe aggregate evaluations are welcome. Start with [CONTRIBUTING.md](CONTRIBUTING.md) and follow the [code of conduct](CODE_OF_CONDUCT.md).

[MIT](LICENSE). Use it, inspect it, adapt it, and report where it fails.
