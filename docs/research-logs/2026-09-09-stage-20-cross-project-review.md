# Stage 20 — Cross-Project Review

**Version:** 1.0 · **Date:** 9 September 2026 · **Status:** Review complete

## 1. Inputs

Compared the independently derived Business Building architecture with the current Production Skills Project Contract v1.2 and Cross-Domain Orchestration and Integration Specification v1.1, plus the domain boundaries already established for Deep Research, Legal, UI/UX, Software Engineering and Pactwright in the bootstrap.

The family contract requires standalone installable skills, domain-owned workflow/evaluation, Extension Packs, progressive examples, external installation validation and durable research logs. The cross-domain contract keeps composition in the consuming project and rejects a shared runtime by default. Business Building is consistent with both.

## 2. Boundary map

```text
Deep Research
→ gathers/synthesises external market, competitor and customer evidence

Business Building
→ decides what business evidence means for customer, offer, economics,
  acquisition, experiments and corrective action

Legal
→ researches applicable legal questions and returns constraints/conclusions

UI/UX Design
→ researches/designs user interactions and product/service experience

Software Engineering
→ implements software, data and integrations

Creative Production Skills
→ produce specialised brand/media/narrative/audio/video artefacts

Pactwright
→ optionally governs authorised delivery Contracts/Evidence

consuming project
→ owns project facts, selections, integrations, roadmap and final outcome
```

Business Building may perform proportionate research, drafting and arithmetic needed for a bounded decision. A handoff is warranted when specialist depth, implementation or professional authority is required; sibling repositories are not mandatory dependencies.

## 3. Handoff contracts

### Deep Research → Business Building

Minimum: research question, sources/locators, evidence classification, scope/population/date, contradictions and unresolved uncertainty. Business Building owns the commercial interpretation. It must not relabel a research finding as customer purchase evidence unless that is what was observed.

### Business Building → Legal

Minimum: jurisdiction, business intention, exact proposed wording/terms/practice, evidence, customer/data context and specific question. Legal returns scoped constraints/conclusion; Business Building adjusts the offer/channel/process. A changed material fact can reopen review.

### Business Building → UI/UX / Creative

Minimum: customer context, supported proposition, approved offer facts, experiment question, constraints and acceptance evidence. Specialist expression cannot silently change price, promise, target customer or approved terms.

### Business Building → Software Engineering

Minimum: commercial requirement, accepted business decisions, measurement definitions, authority/privacy constraints, expected behaviour and acceptance. Engineering owns implementation architecture. Business Building evaluates resulting evidence against the commercial hypothesis.

### Business Building ↔ Pactwright

Business Building can provide a business requirement, experiment, constraint or decision as input to authorised delivery. Pactwright owns lifecycle/Contract state. Business Building does not create a competing project graph or lifecycle runtime.

## 4. Repeated abstraction candidates

| Candidate | Evidence so far | Decision |
|---|---|---|
| Evidence-backed decision handoff | Appears in Business Building and family cross-domain handoffs | **Candidate**, not centralised yet; domain semantics differ |
| Assumption/evidence/decision record | Strong in Business Building; related patterns likely elsewhere | **Candidate** pending explicit second-domain comparison |
| Experiment contract | Business, UI/UX and software delivery can all experiment, but methods differ materially | **Retain domain-owned** until common minimum is demonstrated |
| Constraint diagnosis / smallest repair | Strong family pattern in production/evaluation work | **Candidate**; preserve domain-specific failure taxonomies |
| Validity/confidence metadata | Useful across research and business | **Candidate**; do not invent a universal score |
| Extension Pack precedence | Already family-level contract | **Reuse family abstraction**, do not redefine globally here |

No candidate justifies a universal business graph, experiment runtime, decision database or central evaluator.

## 5. Family conformance findings

- Four core skills satisfy the family requirement for installable domain skills.
- Skills remain self-contained targets; Stage 21 must avoid source-relative dependencies.
- Six canonical specs satisfy the family semantic responsibilities with domain-native filenames.
- Stage 15 provides the required 5×3 primary example design and exact prompts.
- Stage 14 provides first-class Extension Pack and authoring architecture.
- Stage 17 separates domain benchmark from integration QA and measured evidence.
- Stage 11 preserves standalone operation and provider independence.
- Stage 21 must scaffold only immediately useful production surfaces; no cosmetic empty directories.

## 6. No centralisation decisions

Reject for this project:

```text
shared Production Skills runtime
universal artefact/business graph
central provider router
universal pack interpreter
cross-project customer/evidence database
Pactwright-owned business truth
Business-Building-owned software/UX/legal workflow
```

Project-specific integration instances remain in the consuming project, consistent with the family specification.

## 7. Exit

Cross-project boundaries and reusable handoffs are explicit. Family-level candidates are recorded without premature extraction. The Business Building architecture can now be scaffolded as an independent Production Skills repository without becoming a universal business operating system.

### Family sources inspected

- `sb-dev/production-skills`, `docs/specs/02-production-skills-project-contract.md`, v1.2, 8 September 2026.
- `sb-dev/production-skills`, `docs/specs/04-cross-domain-orchestration-and-integration.md`, v1.1, 7 September 2026.

*Stage 20 · Version 1.0 · 9 September 2026.*
