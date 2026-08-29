<div align="center">

# Evidence-Based Career & Resume Advisor

### Research current roles and real JDs, compare them with your resume, and decide what to target, fix, and do first

[简体中文](README.zh-CN.md) · [Architecture](ARCHITECTURE.md) · [Roadmap](ROADMAP.md) · [Contributing](CONTRIBUTING.md)

![Status](https://img.shields.io/badge/status-beta-f59e0b)
![Version](https://img.shields.io/badge/version-0.4.0--beta-2563eb)
![Agents](https://img.shields.io/badge/agents-ChatGPT%20%7C%20Codex%20%7C%20Claude%20%7C%20DeepSeek-111827)
![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB)
![License](https://img.shields.io/badge/license-MIT-16a34a)

`v0.4.0-beta`

</div>

This cross-agent career Skill is built for students, job seekers, and career changers. It researches current industries, roles, and job descriptions, compares market requirements with the resume, projects, and skill evidence you provide, and helps you choose targets, close evidence gaps, and plan the next job-search actions.

> **Product position:** focused on job-market research, role fit, resume evidence diagnosis, skill prioritization, and capacity-bounded 30/60/90-day job-search plans. General education, personal-development, and life decisions unrelated to a target career are outside the current product scope.

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
- professionals comparing job locations, industries, roles, or career-skill investments;
- users who want sourced advice with visible uncertainty instead of motivational filler.

### Not built for

- automatic job applications, recruiter messages, or account automation;
- keyword-only ATS scoring;
- inventing resume achievements, metrics, or individual ownership;
- guaranteeing hiring, admissions, income, or other outcomes;
- general personal decisions, education planning, or life advice unrelated to a target career.

This is a **job-search decision and evidence-diagnosis tool, not a hiring predictor**. It researches, compares, and prioritizes. You review the evidence and keep the final decision.

## 2. What it does

| Function | What you receive | Built-in boundary |
|---|---|---|
| Role and industry research | Current official, company, job-board, and labor-market evidence with a cutoff date | No claim that every requested site was accessible |
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
| Career-skill investment | Target-JD gaps, course or certificate cost, time, and alternative proof paths | Whether to learn, build a project, use another proof path, or defer |
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

This repository keeps one canonical `SKILL.md` and reference set, then adds thin deployment adapters for ChatGPT, Codex, Claude, and DeepSeek. Career logic is not duplicated between agents.

The product display name is **Evidence-Based Career & Resume Advisor**. The technical identifier remains `evidence-based-personal-advisor` to preserve existing installations and invocation compatibility.

| Agent surface | Support in this repository | Deployment path |
|---|---|---|
| Codex | Native filesystem Skill | `scripts/install.py --agent codex` |
| ChatGPT | Universal OpenAI plugin containing the canonical Skill | `.codex-plugin/plugin.json` plus the ChatGPT package |
| Claude Code | Native filesystem Skill | `scripts/install.py --agent claude` |
| claude.ai | Custom Skill upload | Claude Skill zip |
| DeepSeek in Claude Code | Same Claude Code Skill, with DeepSeek as the model provider | Claude install plus DeepSeek's Claude Code integration |
| DeepSeek API | System-instruction adapter with optional built-in web search | `adapters/deepseek/run.py` |

This repository does not automatically upload the Skill or your resume to any provider. Material you submit while using an agent is processed under that provider's account, tool, and data settings; see [Privacy](#9-privacy-limitations-and-safe-use).

### 5.2 Requirements

- at least one supported agent surface listed above;
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
Evaluation cases: 9
```

Validation checks required files, frontmatter, version consistency, local-path leakage, broken relative links, symlinks, and common secret patterns. It does not prove that web research or recommendations are correct.

### 5.5 Install for Codex

macOS or Linux:

```bash
python3 scripts/install.py --agent codex
```

Windows PowerShell:

```powershell
python scripts\install.py --agent codex
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

### 5.6 Package for ChatGPT

ChatGPT and Codex share OpenAI's plugin format. This repository already contains the required `.codex-plugin/plugin.json` and canonical `skills/` directory.

Build the distributable plugin archive:

```bash
python3 scripts/package_skill.py --target chatgpt
```

The archive is created under `dist/`. Use it in the [OpenAI plugin authoring and publication workflow](https://developers.openai.com/plugins/build/plugins), or install the published plugin from the universal plugin directory when a listing is available. Packaging the archive locally does not publish or install it automatically.

After the plugin is installed, ChatGPT can choose the Skill automatically or you can select it explicitly with an `@` mention.

### 5.7 Install for Claude

Claude Code uses the same `SKILL.md` folder format:

```bash
python3 scripts/install.py --agent claude
```

The default destination is:

```text
~/.claude/skills/evidence-based-personal-advisor
```

For claude.ai, build an uploadable Skill archive:

```bash
python3 scripts/package_skill.py --target claude
```

Upload the resulting Claude archive through **Settings → Features** where custom Skills are available. Claude surfaces manage Skills separately, so a Claude Code installation does not automatically appear in claude.ai or the Claude API. See [Anthropic's Agent Skills documentation](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview).

Claude API Skill containers do not have network access. This project therefore does not claim recent job-market research on that surface unless the host application separately supplies a working search tool or retrieved evidence.

### 5.8 Run with DeepSeek

There are two supported routes:

1. **Recommended for an agent experience:** install the Claude Code Skill above, then configure Claude Code to use DeepSeek through [DeepSeek's official coding-agent integration](https://api-docs.deepseek.com/guides/coding_agents/). Claude Code handles Skill discovery; DeepSeek supplies the model.
2. **Direct API adapter:** run the included standard-library adapter against DeepSeek's Responses API.

Test the adapter without making a network request:

```bash
python3 adapters/deepseek/run.py --self-test
```

For a live request, set `DEEPSEEK_API_KEY` through your shell or secret manager, then pipe a sanitized text request through standard input:

```bash
python3 adapters/deepseek/run.py <<'EOF'
I am targeting [role] in [location]. Research recent JDs and compare them with
this redacted resume evidence: [facts only]. Prioritize my next three actions.
EOF
```

The adapter uses DeepSeek's `instructions` field and optional built-in `web_search`. It inlines the runtime references because the API does not load local Skill files progressively, so it normally consumes more input tokens than Codex or Claude Code. The repository does not claim native Skill upload support for the DeepSeek consumer web chat.

### 5.9 Install to a custom Skill directory

Use a custom destination only when your Codex environment is configured to discover that directory:

```bash
python3 scripts/install.py --agent codex --dest "/absolute/path/to/codex/skills"
```

Example for a personal macOS Skill library:

```bash
python3 scripts/install.py --agent codex --dest "$HOME/Desktop/codex/skill"
```

`--dest` must point to the parent Skill directory. The installer creates the final `evidence-based-personal-advisor` folder inside it.

For a custom Claude Code directory, use `--agent claude` with the corresponding parent path.

### 5.10 Verify the installed files

Default macOS/Linux installation:

```bash
test -f "$HOME/.codex/skills/evidence-based-personal-advisor/SKILL.md" && echo "Skill files installed"
```

Windows PowerShell:

```powershell
Test-Path "$HOME\.codex\skills\evidence-based-personal-advisor\SKILL.md"
```

Claude Code default installation:

```bash
test -f "$HOME/.claude/skills/evidence-based-personal-advisor/SKILL.md" && echo "Claude Skill files installed"
```

Then start a new Codex task and invoke the Skill explicitly:

```text
Use $evidence-based-personal-advisor to research current target roles and JDs, compare them with my resume evidence, and prioritize my job-search actions.
```

Local Skill discovery can vary by Codex environment and configuration. If the Skill is not listed or triggered, restart Codex, verify the destination, and use the explicit `$evidence-based-personal-advisor` invocation.

For ChatGPT, use an `@` mention after installing the plugin. For Claude Code, start a new session and ask it to use `evidence-based-personal-advisor`; Claude can also select the Skill automatically when the request matches.

### 5.11 Upgrade safely

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
python3 scripts/install.py --agent codex
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
python scripts\install.py --agent codex
```

Windows PowerShell rollback:

```powershell
Move-Item "$HOME\.codex\skills\evidence-based-personal-advisor" `
  "$HOME\.codex\skills\evidence-based-personal-advisor.failed"
Move-Item "$HOME\.codex\skills\evidence-based-personal-advisor.backup" `
  "$HOME\.codex\skills\evidence-based-personal-advisor"
```

For Claude Code, use the same procedure under `$HOME/.claude/skills` and reinstall with `--agent claude`. ChatGPT and claude.ai packages are upgraded through their respective plugin or Skill management surfaces.

### 5.12 Uninstall without immediate deletion

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

For Claude Code, move the corresponding folder out of `$HOME/.claude/skills`. Remove ChatGPT or claude.ai packages from their respective Skill or Plugin management screens.

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
| `standard` | Most role, resume, and job-search direction analyses | 8–15 contextual sources, 2–4 source types, 1–3 models |
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

**Target-role skill, certificate, or course decision**

```text
Use $evidence-based-personal-advisor to assess whether [skill/certificate/course]
is the best way to close [specific target-role gap]. Use current JDs to compare
price, time, and alternative project or portfolio evidence. Tell me whether to
learn now, test cheaply, build next, or defer.
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

1. **Claim-to-source routing** — industry trends, hiring scale, job requirements, compensation signals, and practitioner friction use different source hierarchies.
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
- Local installation does not mean offline inference. ChatGPT, Codex, Claude, DeepSeek, and enabled tools may send supplied material to their configured providers or services.
- The Skill instructs the active agent not to put resume text, identifiers, contact details, or confidential records into web searches.
- This is an instructional safeguard, not a network sandbox. Review generated queries when risk is material.
- The DeepSeek adapter sends the sanitized standard-input request and inlined Skill instructions to the configured DeepSeek endpoint. It never reads or uploads a resume file automatically.

### Research limits

- Job boards may require authentication, personalize results, block automation, or expose stale pages.
- The Skill has no bundled BOSS, LinkedIn, or Indeed crawler. It uses web access available in the active agent environment.
- Agent capabilities are not identical: login state, browser access, built-in search, file parsing, and citation behavior vary by product and account.
- The DeepSeek API adapter loads more instruction tokens and cannot reproduce filesystem-based progressive disclosure.
- JD samples are convenience samples, not statistically representative labor-market surveys.
- Job-ad frequency is a directional demand signal, not total hiring volume.
- Frameworks organize reasoning; they do not prove claims.
- Current sources can still be wrong, incomplete, or misinterpreted.

### User responsibility

- Verify important claims and generated career material before acting or submitting.
- Never accept invented metrics, ownership, credentials, or outcomes.
- Follow the terms of service of websites and data sources you access.
- Do not treat a role-fit assessment as a hiring probability or outcome guarantee.

See [SECURITY.md](SECURITY.md) for reporting and privacy guidance.

## 10. Validation status

| Evidence level | Current status |
|---|---|
| Repository structure and privacy checks | Passed locally; CI workflow is configured for GitHub |
| Codex and Claude Code installers | Passed isolated local installation tests |
| ChatGPT and Claude package generation | Passed archive structure checks |
| DeepSeek API adapter | Payload and parsing self-test passed; no live account call published |
| Behavioral compliance across model/tool versions | Nine scenarios exist; repeatable results are not yet published |
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
| ChatGPT package cannot be installed | Confirm the plugin is published or available through an enabled development/local source | Validate `.codex-plugin/plugin.json`; packaging alone does not create a listing |
| DeepSeek request fails before an answer | Check the API key, endpoint, model availability, and account access | Run `--self-test`, then retry without including personal data in logs |
| Answer is too long | Ask for `quick` mode and state weekly capacity | Request only the bottom line, three actions, and main uncertainty |
| Resume analysis invents facts | Stop using the output | Report a privacy-safe bug and remove unsupported claims |

## Project files

```text
evidence-based-personal-advisor/
├── .codex-plugin/plugin.json            # ChatGPT/Codex universal Plugin manifest
├── adapters/deepseek/run.py              # DeepSeek Responses API adapter
├── skills/evidence-based-personal-advisor/
│   ├── SKILL.md                         # Core decision router
│   ├── agents/openai.yaml               # Codex UI metadata
│   ├── references/                      # Conditional specialist guidance
│   ├── evals/cases.yaml                 # Nine behavioral scenarios
│   └── scripts/summarize_evals.py       # Local paired-result summary
├── examples/                            # Explicitly labeled examples
├── scripts/install.py                   # Transactional installer
├── scripts/package_skill.py             # ChatGPT and Claude archive builder
├── scripts/validate_repo.py             # Structure and privacy checks
├── ARCHITECTURE.md
├── ROADMAP.md
├── CHANGELOG.md
└── .github/                             # CI, issue forms, and PR checklist
```

## Contributing and license

Observed failures, clearer language, behavioral tests, translations, and privacy-safe aggregate evaluations are welcome. Start with [CONTRIBUTING.md](CONTRIBUTING.md) and follow the [code of conduct](CODE_OF_CONDUCT.md).

[MIT](LICENSE). Use it, inspect it, adapt it, and report where it fails.
