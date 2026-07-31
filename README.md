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
| AI-assisted development | Agent-directed builds under explicit architecture, schema, test, and safety constraints |

---

## Featured projects

### FormWaypoint — export documentation, entirely client-side

Converts a combined Commercial Invoice & Packing List (CIPL) into a completed carrier Shipper's Letter of Instruction (SLI). The document is parsed locally and the carrier's own blank PDF is filled locally: no backend, no account, and no network call carrying shipment data.

- Repo: https://github.com/JoelA510/FormWaypoint (MIT)
- Stack: TypeScript, React, Vite, Tailwind, `pdfjs-dist` / `pdf-lib`, IndexedDB, Vitest
- Carriers: Nippon Express USA and CEVA Logistics SLI forms. FedEx Ship Manager and UPS WorldShip are served by a generated keying sheet rather than an import file, because per-installation import maps fail silently or transpose values.
- Validation: every Schedule B number is checked against the U.S. Census Bureau AES commodity concordance (9,746 codes in the committed dataset) for ten digits, active status, and required unit of quantity. Quantities, weights, and values must sum back to the totals printed on the source document before anything is generated.
- What it refuses to do is the design: it never assigns EAR99 or NLR, never converts an HTSUS number into a Schedule B number, never adopts a classification from a historical filing, never infers country of origin or hazmat/routed-export status, never treats a blank as zero, and never applies a signature. An export declaration is signed under penalty; a form that looks complete and is wrong is the worst thing this tool could produce.
- Verification: 200 automated tests pass in a clean checkout. A further 122 tests validate the tool against five real, manually-processed shipments — expected values taken from the SLIs actually filed — and run only against documents held locally, which are never committed.

### AI Advocate — privacy-first legislative tracking app

Production Expo/Supabase application for survivor-focused California legislation, built for the nonprofit Love Never Fails. Plain-language bill summaries, representative lookup, vote history, outreach tooling, localization, and privacy-conscious data flows.

- Live: https://www.ai-advocate.org/
- Repo: https://github.com/JoelA510/AIAdvocate
- Stack: Expo Router, React Native, Supabase, PostgreSQL, Edge Functions, pg_cron, pgvector, i18next, OpenAI summaries
- Security/governance value: anonymous session tokens instead of accounts, Postgres RLS with RLS-respecting RPCs and edge functions, API quotas, and a risk register tying each identified risk to a control and a monitoring signal. No PII is stored anywhere in the system.
- Engineering value: scheduled ingestion, vote syncing, bilingual summarization, semantic search, verification SQL, documented release process and operational runbooks
- Scale and scope, stated plainly: roughly 30 accounts at last count. No external security review has been conducted.

### SquadLogic — youth sports operations platform

Operational scheduling and roster-management platform for youth sports administrators. Converts registration data into balanced rosters, practice schedules, game schedules, facility workflows, reporting, and administrative coordination.

- Live: https://squadlogic.secureyour.tech/
- Repo: https://github.com/JoelA510/SquadLogic
- Stack: React, Vite, Supabase, PostgreSQL, Edge Functions, RBAC, RLS, Vitest, Playwright-BDD
- Operational value: replaces spreadsheet-heavy scheduling workflows with structured import, generation, review, and reporting flows
- Engineering value: CI gates, bundle checks, advisor linting, security documentation, and test coverage around the workflows most expensive to get wrong

### Phased Launch Planner — structured multi-phase workflow tool

Supabase-backed workflow platform for multi-phase planning, task management, role-based access, and safe schema evolution.

- Private project: source and deployment are not public
- Stack: React, TypeScript, Supabase, PostgreSQL, RLS, TanStack Query, Zod, Playwright
- Architecture: projects modeled as root-level tasks in a recursive tree, deep-cloning of entire template task trees into active instances, and denormalized `root_id` indexing to avoid expensive recursive queries
- Engineering value: single-source-of-truth architecture docs, safe migration protocol, ADRs, testing strategy, and machine-readable agent context

### Helmets Clash — browser strategy game prototype

Turn-based fantasy hex-strategy game that runs entirely in the browser: 2-4 seats (human or AI), four asymmetric factions, procedural maps with deterministic seeds, autosave, and replay support.

- Repo: https://github.com/JoelA510/helmets-clash-web
- Status: active prototype
- Stack: React, TypeScript, Vite, Tailwind CSS, Vitest, Playwright, axe-core
- Engineering value: typed game core decoupled from the view layer; agents work from task packets against a living spec, ADRs, and a development log

---

## Operations track record

The software above is downstream of the day job, not a substitute for it.

| Work | Detail |
|---|---|
| Export classification | HTSUS, Schedule B, and ECCN classification for robotics shipments across APAC/EMEA/LATAM, with audit-ready records behind every declaration |
| Item database remediation | Leading the update of an outdated JD Edwards item database to current HTS codes, including Section 232 provisions (country of smelt, semiconductor performance thresholds): 689 items physically inspected, weighed, and classified as of July 2026, plus batch corrections across the remainder |
| Change control | Running log of corrected weights and HTS codes across a database of ~140,000 unique part numbers, with lookup tools that make erroneous ERP edits stand out and get reverted before they become customs holds |
| Legacy automation | Self-taught IBM AS/400 Control Language; automated a weekly reporting and data-entry process from 16 person-hours (two people, eight hours each) down to a single five-hour review |
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
| Testing | Vitest, Playwright, Playwright-BDD, axe-core, CI quality gates |
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
