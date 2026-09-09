# Stage 11 — Execution Layer

**Version:** 1.0  
**Date:** 9 September 2026  
**Status:** Design complete  
**Branch:** `feat/bootstrap`

## 1. Decision

Use a **provider-neutral orchestration boundary**, not a universal runtime. Skills own business reasoning and produce explicit artefacts/briefs. Deterministic tools own arithmetic and validation. External systems own their state and side effects.

The same business workflow must remain usable when Stripe is replaced by another billing system, a CRM is replaced by a spreadsheet, or no provider integration exists. Provider adapters are optional integrations, not core semantics.

## 2. Responsibility split

### Generative / business-judgement layer

```text
frame decision and objective
model customer/problem/value
design offer/pricing/monetisation hypotheses
select channel and sales-path hypotheses
identify required evidence
interpret defined metrics and uncertainty
design experiment and decision rule
diagnose competing constraints
preserve accepted decisions
propose smallest responsible correction
prepare legal/specialist handoff
```

### Deterministic layer

```text
arithmetic and unit conversions
unit-economics formulas
cash schedules
funnel consistency
schema/frontmatter validation
experiment-rule checks
pack/repository validation
fixture comparison
```

Use small scripts or spreadsheet formulas with test fixtures. Do not embed accounting judgement into a calculator.

### External system layer

```text
CRM state
email/SMS sending
ad serving and campaign experiments
web/product analytics collection
billing/payment state
accounting records
survey collection
scheduling
data warehouse / BI state
```

The external system returns data plus its definition/provenance. The skill interprets that data for the business decision without claiming the provider metric is universally defined.

## 3. Tool handoff contract

Every optional integration or manual handoff exposes:

```text
purpose
required inputs and evidence IDs
provider-independent operation name
side_effect: read | draft | external-write
required authority / approval reference
provider and account/project identifier where applicable
expected result shape and metric definitions
failure / timeout / partial-result handling
provenance and as-of time
```

A missing provider yields a copyable/manual handoff, not a failed core skill. An external-write operation is never inferred from a read credential or a generated plan.

## 4. Data contracts

Prefer Markdown for reasoning and reviewable decisions; CSV/JSON/YAML only where deterministic tools need structure. Do not introduce a database for the core vertical.

Numbers passed between systems carry currency/unit, period, population/cohort, source, observed/assumed status and calculation definition. Provider-specific identifiers may live in consumer-project artefacts or optional integrations, not canonical examples.

Personal data stays in the authorised source system where practical. Core skills should request aggregates or de-identified evidence unless identity is necessary for the task.

## 5. Failure semantics

| Failure | Required behaviour |
|---|---|
| Provider unavailable | Produce manual/provider-neutral next step; preserve unresolved execution state |
| Metric definition missing | Do not interpret number as comparable; request definition |
| Partial external write | Report exact known state and require reconciliation; do not claim atomic success |
| Calculation input missing | Show unknown and sensitivity/required input rather than inventing value |
| Approval absent | Allow safe analysis/draft, block side effect |
| Professional review absent | Block affected commitment, not unrelated work |
| Conflicting data sources | Preserve both, identify precedence/recency issue and request resolution |

## 6. Installation implications

Core installation requires only Agent Skills-compatible files plus a lightweight deterministic runtime chosen at Stage 13/18. Provider SDKs must not be mandatory dependencies for core installation. Optional integrations document credentials and permissions separately.

A clean external project must not depend on checking out this source repository after installation. Skill-local references/scripts must resolve from the installed skill.

## 7. Rejected alternatives

- universal CRM/analytics/accounting schema;
- central provider registry required by every skill;
- automatic multi-provider sync;
- hidden autonomous side effects after a recommendation;
- provider-specific business logic in core commands;
- multi-agent executive hierarchy as the execution model.

These add coordination state before evidence shows it is needed.

## 8. Exit

Business judgement, deterministic calculation and external side effects now have explicit ownership. Changing providers does not require redesigning the business workflow. Stage 12 can identify only the native gaps that remain after this reuse boundary.

*Stage 11 · Version 1.0 · 9 September 2026.*
