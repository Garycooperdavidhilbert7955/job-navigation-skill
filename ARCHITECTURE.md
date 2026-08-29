# Architecture

Evidence-Based Personal Advisor is a small Codex Skill, not a hosted application. The architecture keeps the always-loaded instructions short and loads specialist guidance only when a task needs it.

## Design principles

1. **Evidence before framework** — collect decision-relevant evidence before selecting an analytical model.
2. **User facts stay separate** — market-source confidence never substitutes for proof of a user's skill or experience.
3. **Decision value per token** — stop when more research no longer changes the decision.
4. **Progressive disclosure** — keep the core router in `SKILL.md`; load career, evidence, output, or evaluation references conditionally.
5. **Human-sized output** — lead with one direction, no more than three actions, and the main uncertainty.
6. **Claims match validation** — repository checks, behavioral compliance, comparative improvement, and real-user benefit are four different evidence levels.

## Runtime flow

```text
User problem and supplied materials
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
 decision → ≤3 actions → limits → review loop
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

- Web and job-board access comes from the active Codex environment, not from this repository.
- User material may be sent to the AI provider selected by the user. The Skill instructs Codex not to place personal identifiers or resume text into web searches.
- Installation and repository tests check structure and common privacy leaks; they do not prove source correctness or advice quality.
- The user remains responsible for reviewing consequential decisions and generated career material.
