# Stage 12 — Gap Analysis and Over-Engineering Guardrails

**Version:** 1.0  
**Date:** 9 September 2026  
**Status:** Design complete  
**Branch:** `feat/bootstrap`

## 1. Decision

The research supports a **small native judgement layer** over existing execution systems. The major gaps are not CRM, analytics, payments or marketing automation. They are coherent evidence-to-decision behaviour, cross-layer economics/constraint reasoning and preservation-aware repair.

## 2. Gap matrix

| Capability | Coverage after Stages 1–11 | Native need |
|---|---|---|
| Book-to-capability synthesis | Covered provisionally; source-access gaps explicit | References/research only; no book-specific skill |
| Customer evidence discipline | Partially covered by research/design methods | Native evidence contract and audit behaviour |
| Opportunity/customer/value framing | Partially covered by generic tools | Native business decision framing |
| Offer/economics consistency | Missing as an integrated behaviour | Native |
| Pricing reasoning | Tools calculate/execute; judgement remains partial | Native reasoning + deterministic arithmetic |
| Monetisation model comparison | Partial external frameworks | Native bounded comparison |
| Channel/business-model fit | Marketing tools execute but do not own cross-system choice | Native |
| Lead quality/downstream evaluation | CRM/analytics provide state; semantics vary | Native interpretation |
| Sales-path design | CRM provides pipeline state | Native business path reasoning |
| Delivery-capacity checks | Operations tools may measure; cross-link to sales weak | Native judgement + deterministic model |
| Retention-aware acquisition | Metrics exist in tools | Native cross-layer interpretation |
| Unit economics | Spreadsheet/accounting tools calculate | Native input/evidence contract; deterministic tool executes |
| Cash-aware growth | Accounting tools provide data | Native decision gate; deterministic cash schedule |
| Assumption/observation separation | Not reliably provided by business SaaS | Native |
| Experiment quality | Experiment platforms execute some tests | Native selection/interpretation contract |
| Constraint diagnosis | Generic analytics show symptoms | Native cross-layer diagnosis |
| Smallest-change/preservation | Rarely encoded in execution tools | Native |
| Truthfulness/professional handoff | Specialist rules exist | Native issue spotting and handoff; legal conclusion external |
| Provider integrations | Widely covered externally | Reuse/optional adapters only |
| Pack specialisation | Not yet designed | Native Extension Pack contract, not runtime |

## 3. Native capability shortlist

The smallest coherent native responsibilities are:

1. **Build** — frame opportunity/customer/value; construct offer/pricing/monetisation/delivery/economics; identify assumptions and a bounded test.
2. **Grow** — design demand/channel/sales/retention/expansion decisions while checking downstream value, economics, capacity and authority.
3. **Evaluate** — audit evidence, calculations, offer/channel/economics/experiment quality; diagnose the current constraint; recommend the smallest responsible change.
4. **Pack authoring** — create reusable business-model specialisations only after core behaviour is stable.

This validates the bootstrap's lean four-skill hypothesis provisionally. It does not yet prove every candidate command deserves a separate file.

## 4. Reused capability shortlist

Use existing spreadsheets/scripts for arithmetic; CRM for customer/deal state; analytics for events; billing/payment systems for transactions; accounting for authoritative books; form/survey systems for collection; ad/email platforms for authorised execution; research tools for current external facts; legal/professional specialists for regulated conclusions.

Provider adapters remain optional. A manual handoff is a valid execution path.

## 5. Deferred ideas

Do not build during the core proof:

```text
universal business ontology or graph
custom CRM / customer database
custom ad or email platform
custom payment/billing system
custom analytics warehouse
custom accounting engine
universal pricing optimiser
universal experiment platform
cross-provider sync bus
persistent cross-project customer memory
one universal business score
multi-agent virtual executive team
autonomous outbound engine
mandatory Pactwright runtime
large Extension Pack catalogue before core differential proof
```

Revisit only when at least two independent real use cases demonstrate the same unmet need and reuse is simpler than independent handling.

## 6. Over-engineering tests

Before adding a native component ask:

1. Does an existing system already own the state or side effect well?
2. Is the missing value business judgement rather than execution?
3. Can the capability be expressed as a skill-local reference/command instead of a new service?
4. Does the first vertical require it now?
5. Can it be tested independently?
6. Does it preserve standalone installation?
7. Is a proposed abstraction demonstrated across multiple domains or merely aesthetically symmetric?

A “no” to immediate need is a reason to defer, not to scaffold an empty directory.

## 7. Core vertical implication

The first implementation should use a professional-service or small digital-product fixture:

```text
business idea
→ customer/problem evidence
→ offer and price
→ delivery/unit economics/cash
→ riskiest assumption
→ bounded experiment
→ evidence
→ evaluation
→ smallest justified change
```

No live acquisition automation is needed to prove the architecture.

## 8. Exit

Every proposed native responsibility maps to an evidenced gap. Execution infrastructure remains reused. Stage 13 can now design the smallest skill/command architecture without mirroring books, executive roles or SaaS categories.

*Stage 12 · Version 1.0 · 9 September 2026.*
