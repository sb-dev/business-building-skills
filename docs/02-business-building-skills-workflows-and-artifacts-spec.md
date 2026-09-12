# Business Building Skills — Workflows and Artefacts Specification

**Version:** 1.0 · **Status:** Specified, not implemented · **Date:** 9 September 2026

## End-to-end workflow

```text
bounded decision / observed problem
→ current facts, accepted decisions and unknowns
→ customer/problem/value evidence
→ offer / price / monetisation
→ acquisition / sales path where relevant
→ delivery / continued value / economics / cash
→ material assumptions
→ cheapest adequate experiment or evidence request
→ observed result + measurement checks
→ interpretation and decision
→ constraint diagnosis
→ smallest responsible correction
→ preserve unaffected validated work
```

Greenfield and existing-business paths can skip or reorder stages according to the current uncertainty. Growth is not mandatory; stable or bounded-capacity businesses are valid objectives.

## Business brief

Minimum responsibilities: decision/objective; context; customer/buyer/user/payer/approver roles; problem and alternatives; value/proof; offer; acquisition/sales; delivery; economics/cash; continued value where relevant; assumptions/evidence; accepted decisions; constraints/authority.

Do not require one file per field. A bounded case may use one Markdown brief plus CSV/JSON for deterministic calculations.

## Evidence record

```text
claim_id
statement
basis: observed | reported | derived | assumed | synthetic
source_locator
as_of / window
population / scope
method
limitations
supports_or_challenges
```

Synthetic evidence never becomes observed. Derived evidence cites inputs and calculation/reasoning. Missing evidence is unknown, not pass/fail by default.

## Offer / pricing / money model

Record customer/buying context, controlled deliverable versus uncertain outcome, mechanism, scope/exclusions, time-to-value, price/unit, payment timing, obligations/remedies, proof, factual scarcity and required approvals.

Monetisation records payer/beneficiary, pricing unit, revenue definition, direct costs, contribution boundary, receipts/obligations, retention/repeat dependency, capacity and risk. No mandatory offer ladder or recurring model.

## Acquisition and sales

Represent named transitions with unit/population, entry/exit criteria, window and source. Person, account, opportunity and transaction are distinct. Channel selection considers access, intent, evidence, cost/time, permission, sales load, delivery capacity and downstream value.

Do not infer incremental effect from platform attribution alone. Lead volume is never a substitute for qualification and viable downstream outcomes.

## Delivery, retention and economics

Delivery model: promise, onboarding, steps, capacity unit, work/unit, rework/support, quality, bottleneck, service commitments and cost basis.

Retention/expansion: define cohort, start/continuation event, window, denominator, value signal, cancellation/refund, cost to serve and expansion/referral event. One-off models may mark retention not applicable.

Unit economics: currency, unit/cohort, period, revenue, variable/direct cost, contribution, acquisition/sales/support/refund costs, observed/forecast status and sensitivity. LTV forecasts require horizon and retention assumptions.

Cash: dated opening cash, receipts, supplier/inventory/payroll/acquisition/refund/tax inputs, working-capital timing and closing/minimum balance. Accounting/tax inputs come from authoritative systems/specialists where applicable.

## Assumptions and experiments

Assumption records uncertainty and consequence separately. Experiment records hypothesis, decision, population, cheapest adequate method, primary/guardrail signals, confounders, success/failure/inconclusive/stop conditions, cost/exposure, authority and instrumentation checks.

Learning records actual evidence, data-quality status, interpretation, alternative explanations, bounded decision and remaining unknowns. Activity without a changed/supported decision is not automatically learning.

## Diagnosis and repair

Validate measurement first; identify competing causes; preserve accepted decisions whose evidence still applies; gather distinguishing evidence; name a binding constraint only when supported; mutate the smallest responsible layer; reassess.

A failed channel does not automatically rewrite customer, offer, price and delivery. Contradictory customer evidence can reopen those dependencies explicitly.

## Professional handoff

Record issue, jurisdiction, business intention, wording/terms, evidence, data, assumptions, existing constraints, specific specialist question, blocked action, reviewer/authority, result and changed decision. A review is scoped; material changes can require re-review.

## Handoff between skills

`business-build` outputs an evidence-linked brief. `business-grow` consumes accepted customer/offer/economic constraints and may not silently rewrite them. `business-evaluate` audits any stage and returns findings, diagnosis and mutation scope. Pack defaults specialise but explicit facts and accepted decisions outrank them.
