# Joel Abraham

Operations, logistics, compliance, and systems automation.

I build practical software for workflows where physical operations, systems of record, and compliance requirements have to stay aligned: shipping documentation, scheduling, inventory data, defect tracking, audit evidence, and secure multi-tenant applications.

Current positioning: Operations & Compliance Specialist — 15+ years of continuous hands-on operations across warehouse/freight logistics, global shipping compliance, and multi-campus facilities, now security-certified (Security+ · A+ · AWS CCP · ISC2 CC).

- LinkedIn: https://linkedin.com/in/joel-abraham-cv
- Portfolio: https://secureyour.tech
- Email: hire.joel.abraham@gmail.com

---

## Focus areas

| Area | What I work on |
|---|---|
| Operations systems | ERP/WMS data integrity, exception workflows, SOPs, reporting, handoff controls |
| Logistics automation | Shipping-document workflows, Commercial Invoice/SLI-style data, search and retrieval |
| Business systems | SQL reporting, dashboards, process automation, CSV/JSON workflows, data reconciliation |
| Secure application design | Supabase/Postgres, RLS, RBAC, auditability, migration safety, verification scripts |
| AI-assisted development | Agent-directed builds under explicit architecture, schema, test, and safety constraints |

---

## Featured projects

### SquadLogic - youth sports operations platform

Operational scheduling and roster-management platform for youth sports administrators.

Built to convert registration data into balanced rosters, practice schedules, game schedules, facility workflows, reporting, and administrative coordination.

- Live: https://squadlogic.secureyour.tech/
- Repo: https://github.com/JoelA510/SquadLogic
- Stack: React, Vite, Supabase, PostgreSQL, Edge Functions, RBAC, RLS, Vitest, Playwright-BDD
- Operational value: replaces spreadsheet-heavy scheduling workflows with structured import, generation, review, and reporting flows
- Engineering value: CI gates, bundle checks, advisor linting, security documentation, and test coverage around high-risk workflows

### AIAdvocate - privacy-first legislative tracking app

Production Expo/Supabase application for survivor-focused California legislation.

The app provides plain-language bill summaries, representative lookup, vote history, outreach tooling, localization, and privacy-conscious data flows.

- Live: https://www.ai-advocate.org/
- Repo: https://github.com/JoelA510/AIAdvocate
- Stack: Expo Router, React Native, Supabase, PostgreSQL, Edge Functions, pg_cron, pgvector, i18next, OpenAI summaries
- Security/governance value: RLS-protected writes, RPC/edge-function mutation paths, no survivor-identifying information collected, documented operational runbooks
- Engineering value: scheduled ingestion, vote syncing, bilingual summarization, semantic search, verification SQL, release process documentation

### PlanterPlan - structured workflow and migration architecture

Supabase-backed workflow platform for multi-phase planning, task management, role-based access, and safe schema evolution.

- Repo: https://github.com/JoelA510/PlanterPlan-Alpha
- Stack: React, TypeScript, Supabase, PostgreSQL, RLS, Vitest, Playwright
- Operational value: converts a complex multi-phase process into structured projects, phases, tasks, teams, dates, and reporting
- Engineering value: single-source-of-truth architecture docs, safe migration protocol, ADRs, testing strategy, and machine-readable agent context

### Helmets Clash - browser strategy game prototype

Turn-based fantasy hex-strategy game that runs entirely in the browser: 2-4 seats (human or AI), four asymmetric factions, procedural maps with deterministic seeds, autosave, and replay support.

- Repo: https://github.com/JoelA510/helmets-clash-web
- Status: active prototype
- Stack: React, TypeScript, Vite, Tailwind CSS, Vitest, Playwright, axe-core
- Engineering value: typed game core decoupled from the view layer; agents work from task packets against a living spec, ADRs, and a development log

---

## Technical toolkit

| Category | Tools and practices |
|---|---|
| Working languages | SQL, IBM AS/400 Control Language |
| AI-augmented development | TypeScript, JavaScript, and C# — shipped via agent-directed workflows (AI Advocate, SquadLogic, Helmets Clash) |
| Frontend | React, React Native, Expo, Vite, TanStack Router/Query, Tailwind CSS |
| Backend | Supabase, PostgreSQL, Edge Functions, Hono, FastAPI, Prisma |
| Data | SQL reporting, CSV/JSON processing, ETL-style scripts, dashboards, reconciliation workflows |
| Security | RLS, RBAC, access-policy design, verification SQL, audit-ready SOPs, Security+ foundation |
| Testing | Vitest, Playwright, Playwright-BDD, Jest, CI quality gates |
| Operations | JD Edwards EnterpriseOne, AS/400, WMS workflows, export documentation, HTSUS, Schedule B, ECCN |

---

## How I build

I use AI-assisted development, but not as a substitute for architecture or review.

My usual pattern:

1. Define the operational workflow and failure modes.
2. Lock the schema, permissions, and data boundaries.
3. Generate or refactor code against explicit constraints.
4. Run type checks, tests, linting, and targeted verification scripts.
5. Review the result for security, maintainability, and real workflow fit.
6. Document the operational runbook and follow-up risks.

This matters because most of my projects sit near high-friction boundaries: physical operations vs. systems of record, public clients vs. protected data, automation speed vs. auditability, and AI-generated code vs. production reliability.

---

## Current target roles

I am most aligned with roles that combine operations knowledge, systems thinking, reporting, and automation:

- Operations Analyst
- Logistics Analyst
- Business Systems Analyst
- Technical Operations Specialist
- ERP/WMS Analyst
- Inventory Control Analyst
- Quality / Hardware Lifecycle / RMA Coordinator
- IT Support / Junior Systems Administrator
- GRC Analyst or SOC Tier 1, when the role values operations/compliance background

---

## Selected certifications

- CompTIA Security+
- CompTIA A+
- ISC2 Certified in Cybersecurity (CC)
- AWS Certified Cloud Practitioner
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
