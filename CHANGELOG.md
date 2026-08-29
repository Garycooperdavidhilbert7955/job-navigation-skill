# Changelog

This project is in public beta. Versions describe repository milestones, not proof of effectiveness.

## 0.5.0-beta — 2026-08-30

- Renamed the project, Skill identifier, Plugin identifier, repository, install directory, invocation, and package filenames to `job-navigation-skill`.
- Added repository and homepage metadata to the OpenAI Plugin manifest.
- Documented the one-time migration required for installations using the previous Skill identifier.
- Kept `v0.4.0-beta` available as a rollback release; the identifier change is intentionally breaking.

## 0.4.0-beta — 2026-08-29

- Added a universal ChatGPT/Codex plugin manifest around the canonical Skill.
- Extended the transactional installer to target Codex or Claude Code.
- Added uploadable ChatGPT plugin and Claude Skill archive generation.
- Added a standard-library DeepSeek Responses API adapter with optional built-in web search.
- Kept one canonical `SKILL.md` and reference set so platform packages do not drift.
- Documented platform-specific capability and privacy limits; actual account uploads and live DeepSeek API calls remain environment-dependent.

## 0.3.0-beta — 2026-08-29

- Narrowed the product from general personal decision support to job-market research, role fit, resume evidence diagnosis, and career-skill prioritization.
- Rewrote the English and Chinese first-use experience around students, job seekers, and career changers.
- Updated Skill triggering and Codex interface metadata to exclude unrelated education, personal-development, and life decisions.
- Added a behavioral scope test for unrelated personal and life decisions.
- Kept the technical identifier `evidence-based-personal-advisor` for installation and invocation compatibility.

## 0.2.0-beta — 2026-08-29

- Added a paired baseline/Skill evaluation protocol.
- Added privacy-safe reporting for quality, tokens, time, cost, and hard failures.
- Added opt-in immediate, 7-day, and 30-day user-feedback signals.
- Changed the answer contract to one direction and no more than three immediate actions before optional detail.
- Expanded behavioral scenarios from four to eight.
- Added public-beta documentation, architecture, roadmap, and GitHub feedback templates.

## 0.1.0-beta — 2026-08-29

- Published the initial Codex Skill, installer, validation workflow, career module, evidence protocol, model router, and output contract.
