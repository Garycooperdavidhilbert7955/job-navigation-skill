# Security and privacy

This Skill may process resumes, transcripts, career histories, or other sensitive material. Share only what the decision needs and remove unnecessary identifiers first.

## Never publish or commit

- resumes, transcripts, portfolios containing personal identifiers, or raw prompts;
- names, phone numbers, personal email addresses, IDs, exact home addresses, or private URLs;
- complete model outputs tied to an identifiable person;
- API keys, access tokens, passwords, cookies, or session data;
- confidential employer, client, student, or research-participant information;
- proprietary job-description collections or content that cannot be redistributed.

## Runtime boundary

The Skill is installed locally, but Codex and its enabled tools may send supplied material to the AI provider or services configured in the user's environment. This repository does not control those systems. Review provider settings and terms before supplying sensitive material.

The Skill instructs Codex not to place resume text, identifiers, contact details, or confidential records into web searches. This is an instructional safeguard, not a network sandbox. Review generated queries and outputs when risk is material.

## Reporting a vulnerability

Use this repository's **GitHub Security Advisory** feature for vulnerabilities, secret exposure, installer issues, or privacy failures that should not be public. Do not open a public issue containing exploit details or affected user data.

Include a minimal reproduction, affected version or commit, likely impact, and any safe mitigation. Remove personal data and rotate exposed credentials before reporting.

Public behavior bugs that contain no sensitive information can use the Bug report form.
