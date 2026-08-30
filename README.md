<div align="center">

# Job Navigation Skill

### Research current roles and real job descriptions (JDs), compare them with your resume, and decide what to target, fix, and do first

[简体中文](README.zh-CN.md) · [Architecture](ARCHITECTURE.md) · [Roadmap](ROADMAP.md) · [Contributing](CONTRIBUTING.md)

![Status](https://img.shields.io/badge/status-beta-f59e0b)
![Version](https://img.shields.io/badge/version-0.6.0--beta-2563eb)
![Agents](https://img.shields.io/badge/agents-ChatGPT%20%7C%20Codex%20%7C%20Claude%20%7C%20Cursor%20%7C%20WorkBuddy-111827)
![Command line](https://img.shields.io/badge/CLI-Python%203.11%2B-3776AB)
![License](https://img.shields.io/badge/license-MIT-16a34a)

`v0.6.0-beta`

</div>

This is a set of installable career-research instructions for AI tools, built for students, job seekers, and career changers. It researches current industries, roles, and job descriptions, compares market requirements with the resume, projects, and skill evidence you provide, and helps you choose targets, close evidence gaps, and plan the next job-search actions.

> **Product position:** focused on job-market research, role fit, resume evidence diagnosis, skill prioritization, and capacity-bounded 30/60/90-day job-search plans. General education, personal-development, and life decisions unrelated to a target career are outside the current product scope.

## 0. First use: no coding knowledge required

### What this is

- **Skill:** a folder of professional instructions that an AI tool can read. It is not a new chat app and does not train a model.
- **JD:** job description—the role and hiring requirements published by an employer.
- **Agent:** the AI tool you use, such as Codex, Claude Code, Cursor, or work-buddy.
- **Terminal / PowerShell:** a window for entering computer commands. The commands below only need to be copied, pasted, and run.
- **Repository:** the complete `job-navigation-skill` project folder downloaded and extracted from GitHub.

### Choose only the AI tool you already use

You do not need to install the Skill everywhere.

| Tool you use | Beginner difficulty | Recommended method |
|---|---:|---|
| claude.ai website | Easiest | Download the Claude ZIP and upload it if your account supports custom Skills |
| Cursor | Easy | Import from GitHub inside Cursor; no Python command required |
| Codex | One command | Download the repository and run the Codex installer |
| Claude Code | One command | Download the repository and run the Claude installer |
| work-buddy | One command | Use the Claude Code Skill directory that hosts work-buddy |
| ChatGPT | No general one-click route yet | This repository provides a developer Plugin package, but not a public store install button |

### Method A: do not open a terminal

**Cursor**

1. Copy the repository URL: `https://github.com/xinyu0115/job-navigation-skill`.
2. Open **Cursor Settings → Rules → Add Rule → Remote Rule (GitHub)**.
3. Paste the repository URL and import it.
4. Start a new chat and enter `/job-navigation-skill`, or select it with `@`.

**claude.ai website**

1. Open the [`v0.6.0-beta` release](https://github.com/xinyu0115/job-navigation-skill/releases/tag/v0.6.0-beta).
2. Download the ZIP whose filename contains `claude-skill`; do not extract it.
3. If your account provides custom Skills, upload the ZIP under **Settings → Features**.
4. Start a new chat and ask Claude to use `job-navigation-skill`.

If your interface does not contain that option, the feature may not be available for your current product version, account, or plan. That is not an installation mistake. Use the Codex, Claude Code, Cursor, or work-buddy command route below instead.

### Method B: copy one installation command

1. [Download the project ZIP directly](https://github.com/xinyu0115/job-navigation-skill/archive/refs/heads/main.zip), or select the green **Code → Download ZIP** button on GitHub.
2. Open your Downloads folder and double-click the ZIP to extract it.
3. Open a terminal in the extracted folder, whose name will look like `job-navigation-skill-main`:
   - **macOS:** open Terminal, type `cd ` with one trailing space, drag the folder into the Terminal window, and press Return.
   - **Windows:** open the folder, select the File Explorer address bar, type `powershell`, and press Enter.
4. Copy only the command for the tool you use:

| Tool | macOS / Linux | Windows PowerShell |
|---|---|---|
| Codex | `python3 scripts/install.py --agent codex` | `python scripts\install.py --agent codex` |
| Claude Code | `python3 scripts/install.py --agent claude` | `python scripts\install.py --agent claude` |
| Cursor | `python3 scripts/install.py --agent cursor` | `python scripts\install.py --agent cursor` |
| work-buddy | `python3 scripts/install.py --agent workbuddy` | `python scripts\install.py --agent workbuddy` |

A successful installation ends with output similar to:

```text
Validation passed.
Installed job-navigation-skill for codex to ...
```

If `python3` or `python` is not found, your computer does not currently have a usable Python installation. Install [Python 3.11 or later](https://www.python.org/downloads/); on Windows, select **Add Python to PATH** during installation. You can also use one of the no-terminal routes above.

### Your first message after installation

Close and reopen the AI tool, or start a new chat, then paste:

```text
Use $job-navigation-skill:
I am targeting [role] in [location]. Research recent roles and JDs, compare them with the
redacted resume I will provide, and identify role fit, evidence gaps, and my top three actions.
Separate facts, inferences, and recommendations.
```

Before uploading a resume, remove phone numbers, personal email addresses, identity numbers, exact home addresses, and unnecessary private links. Installing the Skill does not automatically read or upload your resume; only material you deliberately provide enters the conversation.

### Four common beginner misunderstandings

1. **Install it only once:** you do not need every platform version.
2. **work-buddy and Claude Code share one copy:** both use `~/.claude/skills`; do not duplicate the installation.
3. **The release ZIP is not a resume template:** it contains Skill files for an AI tool.
4. **Installation does not guarantee web access:** current job-market research still depends on the active AI tool's ability to search the web or open links you provide.

After the first successful invocation, you can jump directly to [Use it well](#6-use-it-well). The remaining installation sections are for troubleshooting, upgrades, removal, and publishing.

## Continue reading

- [1. Who this is for](#1-who-this-is-for)
- [2. What it does](#2-what-it-does)
- [3. Typical scenarios](#3-typical-scenarios)
- [4. What the result looks like](#4-what-the-result-looks-like)
- [5. Install, validate, and maintain](#5-install-validate-and-maintain)
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

## 5. Install, validate, and maintain

> If you successfully invoked the Skill after section 0, do not repeat the installation commands below. This section is for paths, validation, upgrades, removal, and publishing.

### 5.1 Understand the deployment model

This repository keeps one canonical `SKILL.md` and reference set, then packages it for ChatGPT, Codex, Claude, Cursor, and work-buddy. Career logic is not duplicated between agents.

The product display name and technical identifier are both **Job Navigation Skill** / `job-navigation-skill`. Version `0.5.0-beta` introduced a breaking rename: installations under the previous identifier require the one-time migration in [Safe upgrade](#511-safe-upgrade).

| Agent surface | Support in this repository | Deployment path |
|---|---|---|
| Codex | Native filesystem Skill | `scripts/install.py --agent codex` |
| ChatGPT | Universal OpenAI plugin containing the canonical Skill | `.codex-plugin/plugin.json` plus the ChatGPT package |
| Claude Code | Native filesystem Skill | `scripts/install.py --agent claude` |
| claude.ai | Custom Skill upload | Claude Skill zip |
| Cursor | Native Agent Skill | `scripts/install.py --agent cursor` or GitHub remote import |
| work-buddy | Claude Code-hosted compatibility | `scripts/install.py --agent workbuddy` |

This repository does not automatically upload the Skill or your resume to any provider. Material you submit while using an agent is processed under that provider's account, tool, and data settings; see [Privacy](#9-privacy-limitations-and-safe-use).

### 5.2 Requirements

- at least one supported AI tool listed above;
- no Python requirement for the no-terminal Cursor or claude.ai routes;
- Python 3.11 or later for command installation, validation, or packaging;
- a downloaded or cloned copy of this repository for command installation;
- network access only when your request needs current research.

No Python package installation is required. The installer and validation scripts use the standard library.

### 5.3 Download the repository for command installation

From the GitHub repository page, choose one method:

**Download ZIP**

1. Select **Code → Download ZIP**.
2. Extract the archive.
3. Open Terminal or PowerShell inside the extracted repository—not inside the nested Skill folder.

**Git clone**

1. Select **Code** on the GitHub repository page.
2. Copy the HTTPS or SSH URL.
3. Clone it with your Git client.
4. Open Terminal or PowerShell in the resulting `job-navigation-skill` folder.

The remaining commands in this manual assume that this repository folder is your current working directory.

### 5.4 Optional: validate separately

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
Skill: job-navigation-skill
Evaluation cases: 9
```

The installer runs validation automatically, so ordinary users can install directly. Maintainers and people troubleshooting a failure can run the command above separately. It checks required files, frontmatter, version consistency, local-path leakage, broken relative links, symlinks, and common secret patterns. It does not prove that web research or recommendations are correct.

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
${CODEX_HOME}/skills/job-navigation-skill
```

If `CODEX_HOME` is not set, it uses:

```text
~/.codex/skills/job-navigation-skill
```

The install is transactional: the repository is validated first, symlinks are rejected, files are copied to a temporary staging directory, and the existing destination is never overwritten.

### 5.6 For developers: package for ChatGPT

This section is for people developing or publishing a Plugin, not an ordinary ChatGPT installation path. ChatGPT and Codex share OpenAI's plugin format. This repository already contains the required `.codex-plugin/plugin.json` and canonical `skills/` directory.

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
~/.claude/skills/job-navigation-skill
```

For claude.ai, build an uploadable Skill archive:

```bash
python3 scripts/package_skill.py --target claude
```

Upload the resulting Claude archive through **Settings → Features** where custom Skills are available. Claude surfaces manage Skills separately, so a Claude Code installation does not automatically appear in claude.ai or the Claude API. See [Anthropic's Agent Skills documentation](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview).

Claude API Skill containers do not have network access. This project therefore does not claim recent job-market research on that surface unless the host application separately supplies a working search tool or retrieved evidence.

### 5.8 Install for Cursor and work-buddy

Cursor natively discovers Agent Skills. Install this Skill to its user-level directory:

```bash
python3 scripts/install.py --agent cursor
```

The default destination is:

```text
~/.cursor/skills/job-navigation-skill
```

You can also use **Cursor Settings → Rules → Add Rule → Remote Rule (GitHub)** and import this repository. Start a new chat after installation, then invoke `/job-navigation-skill` or mention it with `@`. See the [Cursor Agent Skills documentation](https://prod.cursor.com/docs/skills).

To build a portable Cursor archive:

```bash
python3 scripts/package_skill.py --target cursor
```

work-buddy runs inside Claude Code, so it uses the same Claude Code Skill directory instead of a separate package format:

```bash
python3 scripts/install.py --agent workbuddy
```

This installs to `~/.claude/skills/job-navigation-skill`. If you already installed the Skill with `--agent claude`, do not install a duplicate. Open a new Claude Code/work-buddy session so the Skill can be discovered. See the [work-buddy documentation](https://docs.work-buddy.ai/).

This repository does not claim a separate work-buddy-native Skill store or archive. For distribution, work-buddy users can use the Claude Skill archive because the host runtime is Claude Code.

### 5.9 Install to a custom Skill directory

Use a custom destination only when your Codex environment is configured to discover that directory:

```bash
python3 scripts/install.py --agent codex --dest "/absolute/path/to/codex/skills"
```

Example for a personal macOS Skill library:

```bash
python3 scripts/install.py --agent codex --dest "$HOME/Desktop/codex/skill"
```

`--dest` must point to the parent Skill directory. The installer creates the final `job-navigation-skill` folder inside it.

For a custom Claude Code, Cursor, or work-buddy directory, select the matching `--agent` value and pass the corresponding parent path. work-buddy and Claude Code normally share the same destination.

### 5.10 Verify the installed files

Default macOS/Linux installation:

```bash
test -f "$HOME/.codex/skills/job-navigation-skill/SKILL.md" && echo "Skill files installed"
```

Windows PowerShell:

```powershell
Test-Path "$HOME\.codex\skills\job-navigation-skill\SKILL.md"
```

Claude Code default installation:

```bash
test -f "$HOME/.claude/skills/job-navigation-skill/SKILL.md" && echo "Claude Skill files installed"
```

Cursor default installation:

```bash
test -f "$HOME/.cursor/skills/job-navigation-skill/SKILL.md" && echo "Cursor Skill files installed"
```

Then start a new Codex task and invoke the Skill explicitly:

```text
Use $job-navigation-skill to research current target roles and JDs, compare them with my resume evidence, and prioritize my job-search actions.
```

Local Skill discovery can vary by Codex environment and configuration. If the Skill is not listed or triggered, restart Codex, verify the destination, and use the explicit `$job-navigation-skill` invocation.

For ChatGPT, use an `@` mention after installing the plugin. For Claude Code or work-buddy, start a new session and ask it to use `job-navigation-skill`; Claude can also select the Skill automatically when the request matches. In Cursor, use `/job-navigation-skill` or `@`.

### 5.11 Upgrade safely

The installer intentionally refuses to overwrite an existing Skill. Use a recoverable upgrade:

**One-time migration from `v0.4.0-beta` or earlier:** the former Skill identifier was `evidence-based-personal-advisor`. Move that folder out of the active Skill directory before installing `job-navigation-skill`; do not leave both identifiers active because an agent may trigger the outdated copy.

```bash
mv "$HOME/.codex/skills/evidence-based-personal-advisor" \
  "$HOME/.codex/evidence-based-personal-advisor.pre-rename-backup"
python3 scripts/install.py --agent codex
```

For Claude Code and work-buddy, apply the same migration under `$HOME/.claude/skills`. For Cursor, use `$HOME/.cursor/skills`. For custom Skill directories, replace the parent path with the directory used in your installation.

1. Download or pull the new repository version.
2. Validate the new repository.
3. Move the installed Skill to a backup name.
4. Run the installer again.
5. Start a new Codex task and run one known prompt.
6. Remove the backup only after the new version works.

Default macOS/Linux example:

```bash
mv "$HOME/.codex/skills/job-navigation-skill" \
  "$HOME/.codex/skills/job-navigation-skill.backup"
python3 scripts/install.py --agent codex
```

Rollback:

```bash
mv "$HOME/.codex/skills/job-navigation-skill" \
  "$HOME/.codex/skills/job-navigation-skill.failed"
mv "$HOME/.codex/skills/job-navigation-skill.backup" \
  "$HOME/.codex/skills/job-navigation-skill"
```

For a custom destination, replace `$HOME/.codex/skills` with the same parent directory used during installation.

Windows PowerShell upgrade:

```powershell
Move-Item "$HOME\.codex\skills\job-navigation-skill" `
  "$HOME\.codex\skills\job-navigation-skill.backup"
python scripts\install.py --agent codex
```

Windows PowerShell rollback:

```powershell
Move-Item "$HOME\.codex\skills\job-navigation-skill" `
  "$HOME\.codex\skills\job-navigation-skill.failed"
Move-Item "$HOME\.codex\skills\job-navigation-skill.backup" `
  "$HOME\.codex\skills\job-navigation-skill"
```

For Claude Code or work-buddy, use the same procedure under `$HOME/.claude/skills` and reinstall with `--agent claude` or `--agent workbuddy`. For Cursor, use `$HOME/.cursor/skills` and `--agent cursor`. ChatGPT and claude.ai packages are upgraded through their respective plugin or Skill management surfaces.

### 5.12 Uninstall without immediate deletion

Move the installed folder out of the active Skill directory:

```bash
mv "$HOME/.codex/skills/job-navigation-skill" \
  "$HOME/.codex/job-navigation-skill.uninstalled"
```

Restart Codex and confirm the Skill is no longer discovered. Delete the moved copy later only if you no longer need rollback.

Windows PowerShell:

```powershell
Move-Item "$HOME\.codex\skills\job-navigation-skill" `
  "$HOME\.codex\job-navigation-skill.uninstalled"
```

For Claude Code or work-buddy, move the corresponding folder out of `$HOME/.claude/skills`. For Cursor, move it out of `$HOME/.cursor/skills`. Remove ChatGPT or claude.ai packages from their respective Skill or Plugin management screens.

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
Use $job-navigation-skill.

I am targeting [role] in [geography] by [date]. Research the last [time window]
of industry and job trends, sample recent JDs, and compare them with my redacted
resume. Identify role fit, skill gaps, evidence gaps, and the three highest-value
actions. Separate facts, inference, and recommendations. I can spend [hours]
per week. Disclose inaccessible sources and the research cutoff.
```

**Career change**

```text
Use $job-navigation-skill to compare [option A], [option B], and
[option C]. My transferable evidence is [brief facts]. My constraints are
[time/budget/location/risk]. Use current market evidence and recommend the
cheapest experiments that could change the decision before I commit.
```

**Target-role skill, certificate, or course decision**

```text
Use $job-navigation-skill to assess whether [skill/certificate/course]
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
- Local installation does not mean offline inference. ChatGPT, Codex, Claude, Cursor, work-buddy, and enabled tools may send supplied material to their configured providers or services.
- The Skill instructs the active agent not to put resume text, identifiers, contact details, or confidential records into web searches.
- This is an instructional safeguard, not a network sandbox. Review generated queries when risk is material.

### Research limits

- Job boards may require authentication, personalize results, block automation, or expose stale pages.
- The Skill has no bundled BOSS, LinkedIn, or Indeed crawler. It uses web access available in the active agent environment.
- Agent capabilities are not identical: login state, browser access, built-in search, file parsing, and citation behavior vary by product and account.
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
| Codex, Claude Code, Cursor, and work-buddy installer paths | Passed isolated local installation tests; work-buddy shares Claude Code's destination |
| ChatGPT, Claude, and Cursor package generation | Passed archive structure checks |
| Behavioral compliance across model/tool versions | Nine scenarios exist; repeatable results are not yet published |
| Better than a neutral baseline | Not established |
| Improves real user outcomes | Not established |

There are no fabricated adoption numbers here. Until at least 10 complete paired tasks and 10 relevant users produce usable data, accuracy, actionability, and token savings remain design goals—not proven benefits.

To test the local evaluation machinery:

```bash
python3 skills/job-navigation-skill/scripts/summarize_evals.py --self-test
python3 skills/job-navigation-skill/scripts/summarize_evals.py --template
```

Read the [evaluation protocol](skills/job-navigation-skill/references/evaluation-and-user-feedback.md) before collecting results. Raw prompts, resumes, employer identities, and complete model outputs do not belong in the public repository.

## 11. Maintenance and troubleshooting

| Problem | Check | Next step |
|---|---|---|
| `python3` not found | Run `python --version` | Use `python` on Windows or install a supported Python version |
| Validation fails | Read the first reported missing file, link, local path, or secret | Restore/fix that exact item; do not bypass validation |
| Destination already exists | The installer protects an existing installation | Use the backup-and-upgrade procedure above |
| Skill files exist but Codex does not show it | Confirm the parent directory is a Skill directory for that environment | Start a new task, invoke `$job-navigation-skill`, then restart Codex if needed |
| Requested platforms are inaccessible | Check authentication and platform restrictions | Provide exported links/text or accept a narrower, clearly labeled sample |
| ChatGPT package cannot be installed | Confirm the plugin is published or available through an enabled development/local source | Validate `.codex-plugin/plugin.json`; packaging alone does not create a listing |
| Cursor does not discover the Skill | Confirm it is under `~/.cursor/skills/` and contains `SKILL.md` | Start a new chat and invoke `/job-navigation-skill` or mention it with `@` |
| work-buddy does not discover the Skill | Confirm Claude Code can see `~/.claude/skills/job-navigation-skill` | Do not duplicate the install; start a new Claude Code/work-buddy session |
| Answer is too long | Ask for `quick` mode and state weekly capacity | Request only the bottom line, three actions, and main uncertainty |
| Resume analysis invents facts | Stop using the output | Report a privacy-safe bug and remove unsupported claims |

## Project files

```text
job-navigation-skill/
├── .codex-plugin/plugin.json            # ChatGPT/Codex universal Plugin manifest
├── skills/job-navigation-skill/
│   ├── SKILL.md                         # Core decision router
│   ├── agents/openai.yaml               # Codex UI metadata
│   ├── references/                      # Conditional specialist guidance
│   ├── evals/cases.yaml                 # Nine behavioral scenarios
│   └── scripts/summarize_evals.py       # Local paired-result summary
├── examples/                            # Explicitly labeled examples
├── scripts/install.py                   # Transactional installer
├── scripts/package_skill.py             # ChatGPT, Claude, and Cursor archive builder
├── scripts/validate_repo.py             # Structure and privacy checks
├── ARCHITECTURE.md
├── ROADMAP.md
├── CHANGELOG.md
└── .github/                             # CI, issue forms, and PR checklist
```

## Contributing and license

Observed failures, clearer language, behavioral tests, translations, and privacy-safe aggregate evaluations are welcome. Start with [CONTRIBUTING.md](CONTRIBUTING.md) and follow the [code of conduct](CODE_OF_CONDUCT.md).

[MIT](LICENSE). Use it, inspect it, adapt it, and report where it fails.
