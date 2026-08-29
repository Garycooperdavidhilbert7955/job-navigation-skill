# Career and job-market module

Use for role research, resume analysis, career entry/change, and skill planning.

## Minimum personal inputs

Extract from the resume and prompt: target role(s), target geography/work authorization, languages, education, projects, internships/work, tools, demonstrated outcomes, constraints, and time available. Do not equate “no formal work experience” with “no evidence”: inspect coursework, projects, volunteering, competitions, freelance work, and leadership.

If target role or geography is absent and cannot be inferred safely, ask one concise question. A market analysis without them is usually misleading.

If resume-gap analysis, resume tailoring, or candidate-to-JD comparison is requested but no resume/CV or factual background is provided, ask the user to supply it before producing the candidate comparison. Continue with role or market research only if it remains independently useful, and clearly label it as a market-side analysis. Do not infer unstated education, experience, skills, constraints, or achievements, and do not generate a candidate evidence-gap matrix without candidate evidence.

## Market evidence stack

For a requested six-month window, prioritize:

1. Official labor statistics and occupational taxonomies for baseline role definitions and scale.
2. Current industry reports with disclosed methods for trend context.
3. Recent first-party employer career pages for actual requirements.
4. Major job boards relevant to geography: BOSS直聘, LinkedIn, Indeed, or local equivalents.
5. Practitioner/community sources only for hypotheses about hidden norms.

Search both local-language and English titles and synonyms. Record query date, location, title, seniority, company, posting date, source URL, and whether the ad is first-party.

If direct access to a platform is blocked, do not fabricate results or silently substitute snippets. State the limitation, use accessible company pages/search results, and invite the user to provide exported links or text.

## Sampling

Default standard sample: target 20–40 unique ads across at least three source types and a mix of company sizes; fewer is acceptable for a narrow market if disclosed. Deduplicate by company, title, location, and substantially identical description. Separate entry-level from experienced roles. Exclude stale, undated, inaccessible, clearly duplicated, and irrelevant ads; report material exclusions.

Do not force an equal quota per platform: access, relevance, and duplication vary. Aim for multiple usable ads from each user-requested platform, but prioritize verifiable first-party postings. Report usable counts by source and explain any platform shortfall. Count the same employer/title/location/substantially identical description once even when syndicated across platforms. Use the employer posting date, not the crawl, refresh, or search-index date.

Do not claim statistical representativeness from convenience samples. Use frequency bands rather than false precision when extraction quality is uneven:

- Core: appears in roughly 50% or more of usable ads.
- Common: roughly 25–49%.
- Emerging/niche: below 25% but strategically relevant.

## Extraction schema

Extract only decision-useful fields:

- responsibilities and deliverables;
- hard skills, tools, domain knowledge;
- soft skills with behavioral context;
- education, experience, language, certification;
- preferred versus required;
- portfolio/work-sample signals;
- AI/automation-related task changes;
- salary only when comparable and legally available.

Normalize synonyms but retain examples. Distinguish skills from tools and credentials.

Convert the normalized fields into four hiring categories before comparing the candidate:

- `must-have`: explicit required qualifications and role-defining deliverables;
- `hard/technical`: methods, tools, domain knowledge, data, product, or operational capabilities;
- `behavioral`: communication, ownership, collaboration, judgment, and execution stated in observable context;
- `preferred/bonus`: non-mandatory experience, credentials, portfolio, language, or domain signals.

Keep `must-have` separate from frequency: an infrequent legal, language, work-authorization, or graduation-window requirement can still be disqualifying.

## Candidate evidence strength

For early-career candidates, grade the evidence behind each claimed capability separately from source confidence:

- `A — externally validated`: real users/clients or production-like context, clear individual responsibility, inspectable artifact, and measured result or independent feedback.
- `B — verified individual work`: individual course, research, open-source, competition, or personal project with inspectable code/report/output and evaluation or instructor/reviewer feedback.
- `C — bounded team contribution`: team project with credible artifacts and a clearly supportable personal contribution, but incomplete ownership or outcome attribution.
- `D — design/simulation only`: proposal, prototype, forecast, ROI/NPV scenario, or planned implementation without verified deployment or realized outcome.
- `U — unsupported`: vague assertion, unverifiable metric, unclear authorship, or a requirement copied from a JD without candidate evidence. Exclude from the resume until substantiated.

Evidence grade is not a judgment of personal potential. It controls claim strength. Never turn D-level projections into realized business results or assign an entire team outcome to one candidate. Upgrade evidence by adding artifacts, individual contribution boundaries, reproducible evaluation, external feedback, or real-user outcomes.

## Resume evidence-gap matrix

Build rows for material requirements and columns:

`requirement | hiring category | demand band | match status | candidate evidence | evidence grade | gap type | recommended proof | action priority`

Match status:

- `strong`: direct, relevant evidence at A or B level;
- `transferable`: adjacent evidence demonstrates the underlying capability;
- `partial`: some evidence exists but scope, recency, depth, or proof is insufficient;
- `missing`: no supported evidence;
- `disqualifying constraint`: an unmet must-have such as work authorization, graduation window, required license, or language threshold.

Gap types:

- `skill`: capability not yet demonstrated;
- `evidence`: likely capability but no credible artifact or metric;
- `communication`: evidence exists but wording/placement is weak;
- `experience`: requires real context that a course alone cannot replace;
- `constraint`: location, work authorization, language, degree, or timing;
- `not a gap`: irrelevant preference or low-value keyword.

Prioritize using demand frequency × importance to outcomes × current gap × feasibility. Do not recommend learning every listed technology.

Keep the three axes distinct:

- `match status` answers how closely the candidate fits;
- `gap type` explains why the fit is incomplete;
- `action priority` answers what to do (`do now`, `test cheaply`, `build next`, or `defer/avoid`).

Example: `SQL analysis | hard/technical | core | partial | coursework queries | B | evidence | publish a funnel analysis artifact | do now`.

## Advice for early-career candidates

Favor proof-generating actions: scoped projects using real or realistic data, public artifacts, case studies, internships, volunteering, competitions, informational interviews, and targeted applications. Each project should demonstrate a market-required task, include a clear deliverable, and produce evidence that can be cited truthfully on the resume.

Create a 30/60/90-day plan only when useful:

- 0–30: validate role fit, repair communication gaps, build one small work sample.
- 31–60: close the highest-value skill/evidence gap and obtain external feedback.
- 61–90: ship a stronger artifact, run targeted applications, measure conversion, iterate.

Track application funnel metrics: qualified applications, response rate, screen rate, interview-stage conversion, recurring rejection reasons, and portfolio engagement. Avoid interpreting very small samples as stable rates.
