# Joel Abraham

Operations, logistics, compliance, and systems automation.

I build practical software for workflows where physical operations, systems of record, and compliance requirements have to stay aligned: export documentation, shipping data, scheduling, inventory integrity, defect tracking, audit evidence, and secure multi-tenant applications.

Current positioning: Operations & Compliance Specialist — 15+ years of continuous hands-on operations across warehouse/freight logistics, global shipping compliance, and multi-campus facilities, now security-certified (Security+ · A+ · AWS CCP · ISC2 CC).

- LinkedIn: https://linkedin.com/in/joel-abraham-cv
- Portfolio: https://secureyour.tech
- Email: hire.joel.abraham@gmail.com

---

## Focus areas

| Area | What I work on |
|---|---|
| Export & trade compliance | HTSUS, Schedule B, ECCN classification; AES commodity data; carrier documentation workflows |
| Operations systems | ERP/WMS data integrity, exception workflows, SOPs, reporting, handoff controls |
| Business systems | SQL reporting, lookup tools and change logs, process automation, CSV/JSON workflows, reconciliation |
| Secure application design | Supabase/Postgres, RLS, RBAC, auditability, migration safety, verification scripts |
| AI-assisted development | Agent-directed builds under explicit architecture, schema, test, and safety constraints, and the checks that hold agents to them |

---

## Featured projects

### FormWaypoint — export documentation that never leaves the machine

Converts a combined Commercial Invoice & Packing List (CIPL) into a completed carrier Shipper's Letter of Instruction (SLI). The document is parsed locally and the carrier's own blank PDF is filled locally: no backend, no account, and no network call carrying shipment data. It runs in the browser or as a Windows desktop app, whose only network call downloads the public Schedule B dataset from census.gov.

- Repo: https://github.com/JoelA510/FormWaypoint (MIT)
- Stack: TypeScript, React, Vite, Tailwind, `pdfjs-dist` / `pdf-lib`, IndexedDB, Vitest, Tauri 2 desktop shell
- Inputs and carriers: three CIPL formats in; Nippon Express USA and CEVA Logistics SLI forms out, with continuation sheets for long shipments. FedEx Ship Manager and UPS WorldShip are served by a generated keying sheet rather than an import file, because per-installation import maps fail silently or transpose values.
- Validation: every Schedule B number is checked against the U.S. Census Bureau AES commodity concordance (9,746 codes in the committed dataset) for ten digits, active status, and required unit of quantity. Quantities, weights, and values must sum back to the totals printed on the source document before anything is generated.
- Dangerous goods by air: classifies lithium batteries from the operator's own answers (nothing starts pre-answered) and prepares a Shipper's Declaration for a qualified person to check and sign. That output is marked unverified: its figures come from course materials rather than the licensed IATA DGR, it has not been used for a real consignment, and downloads stay disabled until the operator acknowledges this.
- What it refuses to do is the design: it never assigns EAR99 because no ECCN appeared, never assigns NLR because EAR99 was chosen, never converts an HTSUS number into a Schedule B number, never adopts a classification from a historical filing, never infers country of origin or hazmat/routed-export status, never treats a blank as zero, and never applies a signature. An export declaration is signed under penalty; a form that looks complete and is wrong is the worst thing this tool could produce.
- Verification: 1,111 automated tests pass in a clean checkout (November 2026). A further 104 tests replay six real, manually processed shipments, with expected values taken from the SLIs actually filed; they run only where those documents are held locally and skip everywhere else.
- Status: pre-release (0.1.0). The desktop installer is built in CI but not yet published as a release.

### AI Advocate — privacy-first legislative tracking app

Production Expo/Supabase application for survivor-focused California legislation, built for the nonprofit Love Never Fails. Plain-language bill summaries in English and Spanish, representative lookup, vote history, and outreach tooling.

- Live: https://www.ai-advocate.org/
- Repo: https://github.com/JoelA510/AIAdvocate
- Stack: Expo Router, React Native, Supabase, PostgreSQL, Edge Functions, pg_cron, pgvector, i18next, OpenAI summaries and embeddings
- Data sources: as of November 2026, bill text, status, and history come from the California Legislature's public data archive, read by ranged requests into a 1+ GB zip from inside Edge Function limits. LegiScan is the fallback and OpenStates supplies legislators and votes.
- Security/governance value: the public app uses anonymous sessions instead of accounts, and admin screens are web-only, a split CI enforces. Postgres RLS with locked-down RPCs, a shared rate gate on every external API call (also CI-enforced), and a [risk register](https://github.com/JoelA510/AIAdvocate/blob/main/docs/risk-register.md) tying each identified risk to a control and a monitoring signal.
- Privacy: no names, emails, or addresses are collected. What is stored (saved bills, reactions, vote-alert subscriptions, and a push-notification token for users who allow notifications) is tied to an anonymous session.
- Engineering value: scheduled ingestion with daily health alerting, vote syncing, bilingual summarization that source refreshes cannot overwrite, semantic search, verification SQL, and a documented release process
- Scale and scope, stated plainly: roughly 30 accounts at last count, on free-tier infrastructure. No external security review has been conducted.

### SquadLogic — youth sports scheduling platform

Turns a youth recreational league's registration export into balanced teams and conflict-aware practice and game schedules, with field management, scores and standings, and printable reports. It is an administrator's tool by design: coaches and families do not sign in, and it stores no birthdates or guardian contacts.

- Live: https://squadlogic.secureyour.tech/
- Repo: https://github.com/JoelA510/SquadLogic
- Stack: React, Vite, Supabase, PostgreSQL, Edge Functions, RBAC, RLS, Vitest, Playwright-BDD, pgTAP
- Operational value: replaces spreadsheet-heavy scheduling with structured import, generation, review, and publishing. A published game is pinned, so regenerating the schedule never moves it, and a game that cannot be placed is surfaced as time-TBD with a reason rather than dropped.
- Engineering value: every scheduling change is run against an anonymized full-season regression corpus (567 published games across 9 Saturdays, 132 teams). State changes go through audited RPCs, CI is the only writer of database migrations, and six required checks gate every merge.
- Status: v1.2.0 (October 2026), with a schedule-expansion plan in progress. No external security review has been conducted.

### agent-ready-template — the process the other projects are built under

A project template for AI-driven development: agents write most of the code, and the template supplies the process, checks, and structure that keep that work honest. One half is process (prompts, workflow skills, ADRs, a definition of done, and a standards catalog that scores a repository), delivered into other repositories by a script that updates only the files the target has not edited. The other half is an interface starter: design tokens and accessible React primitives in one Storybook.

- Repo: https://github.com/JoelA510/agent-ready-template (MIT)
- Storybook: https://joela510.github.io/agent-ready-template/
- Stack: TypeScript, React, Radix UI, Tailwind CSS, Style Dictionary, Storybook, Vitest, Playwright, axe-core
- What is in it: 10 workflow skills (plan, root-cause, adversarial review, pre-PR, verify, and others), 58 standards across 10 stack packs, 20 ADRs, and 49 UI components
- The rule that matters: a check is not trusted until it has been shown failing on a planted defect. Agents must also label every claim as statically reviewed, executed, or fully validated.
- Verification: 1,264 tests pass in a clean checkout (November 2026)
- Status: v1.0.0 (October 2026). FormWaypoint and SquadLogic take their workflow skills from it. Its trial runs, including the ones where its own scorecard was wrong, are logged in the repository.

### Phased Launch Planner — structured multi-phase workflow tool

Supabase-backed workflow platform for multi-phase planning, task management, role-based access, and safe schema evolution.

- Private project: source and deployment are not public
- Stack: React, TypeScript, Supabase, PostgreSQL, RLS, TanStack Query, Zod, Playwright
- Architecture: projects modeled as root-level tasks in a recursive tree, deep-cloning of entire template task trees into active instances, and denormalized `root_id` indexing to avoid expensive recursive queries
- Engineering value: single-source-of-truth architecture docs, safe migration protocol, ADRs, testing strategy, and machine-readable agent context

### Helmets Clash — browser strategy game prototype

Turn-based fantasy hex-strategy game that runs entirely in the browser: 2-4 seats (human or AI), four asymmetric factions, procedural maps with deterministic seeds, autosave, and replay support.

- Live: https://helmets-clash.secureyour.tech/
- Repo: https://github.com/JoelA510/helmets-clash-web
- Status: prototype
- Stack: React, TypeScript, Vite, Tailwind CSS, Vitest, Playwright, axe-core
- Engineering value: typed game core decoupled from the view layer; agents work from task packets against a living spec, ADRs, and a development log

---

## Operations track record

The software above is downstream of the day job, not a substitute for it.

| Work | Detail |
|---|---|
| Export classification | HTSUS, Schedule B, and ECCN classification for robotics shipments across APAC/EMEA/LATAM, with audit-ready records behind every declaration |
| Item database remediation | Leading the update of an outdated JD Edwards item database to current HTS codes, including Section 232 provisions (country of smelt, semiconductor performance thresholds): 984 items physically inspected, weighed, and classified as of September 2026, plus batch corrections across the remainder |
| Shipping & receiving | Outbound international shipping across FedEx, UPS, DHL, Nippon Express, and CEVA with air waybills, bills of lading, and commercial invoices; delivery acceptance and parts release to engineers under J-SOX separation-of-duties controls; earlier, receiving pallet and roll freight at a Hayward freight facility; certified forklift operator |
| Change control | Running log of corrected weights and HTS codes across a database of ~140,000 unique part numbers, with lookup tools that make erroneous ERP edits stand out and get reverted before they become customs holds |
| Legacy automation | Self-taught IBM AS/400 Control Language; automated a month-end billing data-entry process from 16 person-hours (two people, eight hours each) down to a single five-hour review |
| WMS rollout | Drove warehouse management system adoption from 2 of ~100 storage customers to standard warehouse-wide practice: initial intake of all stored goods, scan-log sync functions submitted to corporate IT, and training for the rest of the office |
| Scheduling at scale | Board-level scheduling for a youth soccer club of ~1,400 players across ~144 teams: every season started on time, zero field double-bookings, zero conflicts for sole coaches of multiple teams |

---

## Technical toolkit

| Category | Tools and practices |
|---|---|
| Working languages | SQL, IBM AS/400 Control Language |
| AI-augmented development | TypeScript, JavaScript, and C# — shipped via agent-directed workflows (FormWaypoint, AI Advocate, SquadLogic, Helmets Clash) |
| Frontend | React, React Native, Expo, Vite, TanStack Query, Tailwind CSS |
| Backend | Supabase, PostgreSQL, Edge Functions |
| Data | SQL reporting, CSV/JSON/XLSX processing, ETL-style scripts, change logs, reconciliation workflows |
| Security | RLS, RBAC, access-policy design, verification SQL, audit-ready SOPs, risk registers, Security+ foundation |
| Testing | Vitest, Playwright, Playwright-BDD, pgTAP, axe-core, CI quality gates |
| Operations | JD Edwards EnterpriseOne, AS/400, WMS workflows, export documentation, HTSUS, Schedule B, ECCN, Section 232, AES |

---

## How I build

I use AI-assisted development, but not as a substitute for architecture or review.

My usual pattern:

1. Define the operational workflow and its failure modes.
2. Lock the schema, permissions, and data boundaries.
3. Generate or refactor code against explicit constraints.
4. Run type checks, tests, linting, and targeted verification scripts.
5. Review the result for security, maintainability, and real workflow fit.
6. Document the operational runbook and follow-up risks.

That pattern is written down as prompts, skills, and scored standards in [agent-ready-template](https://github.com/JoelA510/agent-ready-template), so each project starts from the same rules instead of my memory of them.

This matters because most of my projects sit near high-friction boundaries: physical operations vs. systems of record, public clients vs. protected data, automation speed vs. auditability, and AI-generated code vs. production reliability. The rule that falls out of that, and the one FormWaypoint is built around, is that a system handling regulated data should refuse to guess rather than produce a confident wrong answer.

---

## Current target roles

I am most aligned with roles that combine operations knowledge, systems thinking, reporting, and automation:

- Operations Analyst
- Logistics / Trade Compliance Analyst
- Business Systems Analyst
- Technical Operations Specialist
- ERP/WMS Analyst
- Inventory Control Analyst
- Quality / Hardware Lifecycle / RMA Coordinator
- IT Support / Junior Systems Administrator
- GRC Analyst or SOC Tier 1, when the role values an operations/compliance background

---

## Selected certifications

- CompTIA Security+
- CompTIA A+
- ISC2 Certified in Cybersecurity (CC)
- AWS Certified Cloud Practitioner
- Dangerous Goods: Lithium Cells & Batteries (Labelmaster; DOT 49 CFR, IATA DGR, IMDG), August 2026
- Cybersecurity Pre-Apprenticeship, ITBiz Tech Academy (Class Salutatorian)
- Google AI Essentials

---

## What this GitHub is meant to show

This profile is not just a code sample archive.

It is evidence of a working pattern:

- understand the real operational workflow
- model the data cleanly
- automate the repetitive parts
- protect sensitive boundaries
- test what can fail
- document how to operate and recover the system
