# Architecture

Job Navigation Skill is a cross-agent Skill package for job-market research, role fit, resume evidence diagnosis, and career-skill prioritization—not a hosted application. One canonical Skill is packaged for ChatGPT, Codex, Claude, Cursor, and work-buddy. Its display name, folder, manifest name, and invocation share the `job-navigation-skill` identifier.

## Design principles

1. **Evidence before framework** — collect decision-relevant evidence before selecting an analytical model.
2. **User facts stay separate** — market-source confidence never substitutes for proof of a user's skill or experience.
3. **Decision value per token** — stop when more research no longer changes the decision.
4. **Progressive disclosure where supported** — keep the core router in `SKILL.md`; filesystem-based agents load references conditionally.
5. **Human-sized output** — lead with one direction, no more than three actions, and the main uncertainty.
6. **Claims match validation** — repository checks, behavioral compliance, comparative improvement, and real-user benefit are four different evidence levels.

## Runtime flow

```text
                       canonical Skill
             SKILL.md + references + scripts
                            │
          ┌─────────────────┼─────────────────┐
          ▼                 ▼                 ▼
 ChatGPT/Codex Plugin  Claude Skill      Cursor Skill
                            │
                            ▼
                  work-buddy via Claude Code
                            │
                            ▼
                     same career workflow
```

```text
Job-search goal and supplied materials
              │
              ▼
      SKILL.md decision router
              │
      ┌───────┼────────┐
      ▼       ▼        ▼
  evidence  career   model
  protocol  module   router
      └───────┼────────┘
              ▼
   current sources + user facts
              │
              ▼
       output contract
              │
              ▼
 target direction → ≤3 actions → limits → review loop
```

## Evaluation flow

```text
Same sanitized task, model, tools, date, and budget
                 │
          ┌──────┴──────┐
          ▼             ▼
    neutral baseline   Skill run
          └──────┬──────┘
                 ▼
 blinded review + hard-failure check + cost record
                 │
                 ▼
 aggregate report; no claim below the predefined gate
```

The summarizer never runs a model and never collects data automatically. It only validates and aggregates JSONL records supplied locally by an evaluator.

## Trust boundary

- Web and job-board access comes from the active agent environment, not from this repository.
- User material may be sent to the AI provider selected by the user. The Skill instructs the active agent not to place personal identifiers or resume text into web searches.
- ChatGPT/claude.ai uploads and Codex, Claude Code, and Cursor filesystem installs are separate deployment boundaries; installing one does not synchronize the others. work-buddy shares the Claude Code runtime and Skill directory.
- Installation and repository tests check structure and common privacy leaks; they do not prove source correctness or advice quality.
- The user remains responsible for reviewing consequential decisions and generated career material.
