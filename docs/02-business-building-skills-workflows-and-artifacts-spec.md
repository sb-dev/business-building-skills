# Business Building Skills — Workflows and Artifacts Specification

**Status:** Canonical workflow specification  
**Derived from:** accepted Stages 4–9 and cross-cutting contracts from Stages 1–3 and 10–17  
**Boundary:** defines business artefacts and reasoning workflows; it does not execute live operations or issue professional conclusions.

## 1. Workflow model

Business Building is document-led. A bounded task starts from an accountable objective, exact decision scope, accepted versions and obligations, authorised evidence, material unknowns, and action/professional boundaries. It ends in a bounded disposition: retain, revise proposal, test, reject, block, no change, contain harm, or request specialist/owner evidence. A completed artefact is not proof that a hypothesis is true and is not authority to execute it.

Shared evidence states are **known observation**, **hypothesis**, **mixed evidence**, **unknown**, and **not applicable with reason**. Always keep assumption, observed evidence, metric/calculation, interpretation, decision, confidence/limitations and action authority separate. Synthetic fixtures remain synthetic.

## 2. Business dossier

A dossier records initiative, accountable owner, objective/decision/horizon, version/date, material geography/currency/unit, evidence/data-use constraints, obligations, and optional Extension Pack/version/scope.

### 2.1 Fifteen-part business map

| ID | Concern | Minimum contract |
|---|---|---|
| B01 | target customer | segment, inclusion/exclusion, context, material roles |
| B02 | problem / desired progress | situation, importance, frequency/consequence, evidence, unknowns |
| B03 | alternative / status quo | workaround, competitor, in-house, deferral/no action, switching burden |
| B04 | value proposition | role/context, desired progress, alternative, mechanism, benefit, burden, evidence limits |
| B05 | offer | outcome, bounded scope, obligations, detailed-offer reference |
| B06 | acquisition channel | mechanism, audience fit, reach evidence, permission boundary |
| B07 | sales / conversion path | buyer tasks, roles, evidence, unresolved steps |
| B08 | price / revenue mechanism | payer, unit, complete terms, proposed/quoted/contracted/collected state |
| B09 | delivery mechanism | work, dependencies, owner, repeatability evidence |
| B10 | cost structure | direct/acquisition/delivery/support/fixed costs with unit/horizon |
| B11 | retention / repeat / expansion | continuing-value mechanism and observed/predicted events |
| B12 | referral / advocacy | value basis, mechanism, incentive assumptions |
| B13 | operational constraints | capacity, competence, quality, access, suppliers, customer dependencies |
| B14 | cash timing | dated usable collections/obligations, refunds, future service commitments |
| B15 | key assumptions | decision-critical unresolved links and discriminating evidence |

The map is connected, not a mandatory serial questionnaire.

## 3. Customer and value artefacts

Distinguish only material roles: declared target customer, observed customer, buyer, user, economic decision-maker, influencer, payer/gatekeeper. A generated persona is never an observed customer.

An evidence record contains evidence ID, authorised source/locator, date, evidence type, population/role/cohort, method/exposure/sample basis, observation/account, measure + denominator, limitations/counter-evidence, permitted use/access constraints, affected claims and synthetic flag.

A value record uses:

```text
role + context + desired progress + alternative + proposed mechanism
+ benefit + customer burden + evidence / uncertainty
```

Relevant value dimensions may include functional, economic, emotional, social/status, risk, time, effort and uncertainty reduction. Never sum them into one value score.

A target-customer revision preserves the current version/evidence, versions the proposal, separates transferable evidence, reviews value/offer/channel/sales/delivery/economics/professional dependencies, then obtains accountable approval before replacement.

## 4. Offer and pricing artefacts

### 4.1 Offer record

| ID | Component |
|---|---|
| O01 | customer |
| O02 | outcome |
| O03 | scope |
| O04 | mechanism |
| O05 | deliverables |
| O06 | time-to-value |
| O07 | price |
| O08 | payment structure |
| O09 | risk reversal |
| O10 | guarantee / refund terms |
| O11 | bonuses / added components |
| O12 | proof / credibility |
| O13 | constraints / exclusions |
| O14 | truthful urgency / scarcity only where real |

Review relevance, substantiation, clarity, deliverability, direct economics, cash/capacity and rights/professional constraints independently. Conversion cannot compensate for a failed hard gate.

### 4.2 Commercial arithmetic

```text
G = gross commercial consideration for the business's own exchange
D = explicit discount
F = refunds / credits reducing consideration
N = G - D - F
K = declared directly attributable cost scope
C = N - K
contribution margin = C / N when N > 0
```

A residual after acquisition/shared costs is not automatically net profit. Cash is separately dated; accounting/tax treatment stays external.

### 4.3 Pricing workflow

Compare only a decision-relevant set: cost-informed, value-based, reference/competitor, willingness-to-pay, tiering, packaging, usage, subscription, one-time, retainer, performance-linked, free-to-paid, discounting or payment timing. Fix current terms, establish value/payer, expose cost/capacity/cash/proof/rights, include no change, run deterministic scenarios, inspect complete terms, choose retain/revise/test/reject/block, and version accepted changes. No universal premium-price or margin threshold exists.

## 5. Money-model artefact

Canonical labels: initial transaction; recurring revenue; upsell; cross-sell; expansion; renewal; usage; services; licensing; marketplace/intermediary fees; advertising; affiliate/referral revenue; open-source commercialisation.

For each exchange record value exchange, payer, pricing unit, gross consideration, direct costs, margin/contribution basis, cash timing, retention dependency, capacity dependency and obligations. Separate own consideration, pass-through funds and restricted funding; a deposit is not a second sale; analytic labels must not duplicate totals; added monetisation requires genuine incremental value and feasible obligations.

## 6. Acquisition and channel workflow

Preserve the lifecycle:

```text
target audience
→ awareness / reach
→ response / engagement
→ lead / prospect
→ qualification
→ sales conversation / conversion path
→ customer
```

Channel classes: direct outreach, content, community, search, paid media, partnerships, affiliates, referrals, events, marketplaces, platform distribution, product-led acquisition, existing audience.

A channel record contains mechanism, audience fit, source/permission, evidence, full effort/cost, lag, downstream quality, capacity/cash consequences and bounded next test. Do not recommend all channels.

Lead quality keeps separate: volume, fit, intent, qualification, conversion, acquisition cost, sales effort, time-to-close, retention / downstream quality. Unknown authority is not failed qualification; organic is not costless.

## 7. Sales workflow

Supported annotations: self-serve, sales-assisted, consultative, enterprise, inbound, outbound, marketplace-mediated, partner-led.

Record accepted offer/terms; buyer/user/payer/approval roles; entry/qualification evidence; buyer tasks/evidence; truthful proof/material terms; seller/operator owner; next action; won/lost/open/no-decision semantics; sales effort/time-to-close; and delivery handoff/obligations. Separate message quality, offer quality, technical checkout and sales execution. Refusal is not automatically an objection to overcome.

## 8. Delivery and capacity artefacts

Cover fulfilment, onboarding, time-to-value, quality control, capacity, service levels, support, retention, repeat purchase, renewal, expansion, referral, refunds/cancellations and failure demand. For each step record prerequisite, responsible resource, work/setup/rework, waiting/dependency, output/acceptance, failure signal, recovery owner and evidence window.

```text
required_r = existing_r + shared_r + setup_r + Σ(quantity_j × work_rj)
headroom_r = available_r - protected_reserve_r - required_r
closing backlog = opening backlog + accepted incoming - completed - cancelled
```

Capacity arithmetic is necessary but does not prove schedulability.

## 9. Retention and expansion artefacts

A cohort record includes entry event/date, unit, eligibility, offer/price version, first-value event, observation horizon, payment/use/outcome states, renewal eligibility, cancellation/refund/dispute, reactivation/expansion, source coverage, costs and unresolved cases.

Keep point retention, continuous survival, due-cohort renewal, repeat purchase, reactivation, expansion, continued billing and meaningful use/value distinct.

```text
GRR = (B - L - Q) / B
NRR = (B - L - Q + E) / B
```

New customers are excluded from the starting cohort. NRR >100% does not prove absence of churn, profitability or welfare. Expansion requires genuine extra need, explicit acceptance and marginal delivery/support/cash review.

## 10. Unit-economics artefact

Every economic metric states metric/version + decision; formula/event rule; unit + numerator/denominator; cohort/attribution; period/observation age; currency; revenue/cost basis; included/excluded components; source/assumption; realised vs forecast; calculation method/rounding; limitations; owner/review trigger.

Required concerns include revenue per customer/transaction, gross margin, contribution margin, cost to serve, CAC, payback, retention/churn, repeat purchase, LTV assumptions, refunds/chargebacks, sales cost and support cost. Undefined denominator ≠ zero. LTV exposes basis/horizon; CAC exposes scope/denominator. Historical averages do not establish marginal scale economics.

## 11. Cash artefact

Use a dated usable-cash calendar covering applicable customer prepayment, receivables, supplier terms, inventory, payroll, refund exposure, advertising spend timing, tax obligations, working capital, cash conversion and runway. Preserve date/window, amount/currency, usable/restricted state, source/assumption and linked obligation; track minimum headroom, not only closing cash. Prepayments retain future obligations and restricted funds are not growth cash.

A scale decision evaluates independent gates for evidence/definition integrity, deliverable value/quality, operational capacity, economics/sustainability, retention/downstream quality, dated cash/obligation coverage, and customer rights/professional constraints/action authority. Unresolved applicable gate = **BLOCKED**; contradicted gate = **FAIL**. Do not average them.

## 12. Assumption register

Record ID/version, bounded assertion, role/context/horizon, linked decisions/dependencies, supporting/challenging evidence, uncertainty, consequence if wrong, owner and next discriminating evidence/review trigger.

Ten coverage classes:

```text
customer exists
problem matters
customer can be reached
offer is understood
customer will pay
channel is economical
delivery works
customer receives promised value
customer stays / repeats
economics remain viable at scale
```

Uncertainty and consequence remain separate.

## 13. Experiment contract

Every experiment retains ID/version, decision, accepted baseline, owner, freeze time, allowed operations and exactly:

1. assumption;
2. hypothesis;
3. cheapest valid test;
4. target population;
5. success/failure signal;
6. guardrails;
7. duration/sample requirements where relevant;
8. confounders;
9. decision rule.

Freeze criteria before interpretation. Preserve amendments and already-visible data. Outcomes may support, challenge, remain inconclusive, be invalid/uninterpretable, or stop on guardrail. Every outcome maps to a bounded next decision; if every result means success, the experiment is invalid.

## 14. Learning record

```text
assumption
test / explicit absence of a controlled test
observed evidence
result
interpretation
decision
what remains unknown
next experiment / commitment
```

Keep frozen plan and raw evidence immutable. Activity alone is not learning; an operational choice under uncertainty does not prove a hypothesis.

## 15. Constraint diagnosis

Candidate routes:

```text
demand
lead quality
conversion
price
retention
delivery capacity
gross margin
cash
sales capacity
fulfilment quality
onboarding
product value
trust
measurement / evidence integrity
experiment design / inference
```

Procedure: state objective/horizon/baseline; reconcile definitions/cohorts/costs/cash/source integrity; enumerate rival causes and discriminating evidence; ask what improves if each limitation is relieved and what binds next; classify diagnosis as supported/provisional/inconclusive; choose no change, containment, local repair, bounded test or justified coupled change. A logging defect is not product failure and multiple constraints may coexist.

## 16. Preservation and repair record

Every repair contains RR01–RR08:

| ID | Contract |
|---|---|
| RR01 | responsible layer/evidence + rival explanations |
| RR02 | smallest sufficient change + smaller/no-change alternative |
| RR03 | preserved decisions/obligations |
| RR04 | dependency impact: retain/review/revise/block |
| RR05 | approval/execution owner |
| RR06 | bounded resources, exposure, reversibility |
| RR07 | verification + decision rule |
| RR08 | learning + regression handoff |

Preservation is not immobility: adequate evidence can justify coordinated change, but affected scope and new hypotheses must be explicit.

## 17. Legal/professional handoff

For a sensitive issue:

```text
identify issue
→ preserve facts
→ state business intention
→ surface assumptions
→ route bounded professional question
→ consume attributed constraint
→ adjust proposal/process
```

The issue packet records exact action/claim/version, roles, possible jurisdictions, dates, evidence locators/access restrictions, contrary facts, current findings, reviewer questions, interim protection, owner and blocked dependency. The returned finding records reviewer/remit, factual/version boundary, jurisdiction/source status, effective dates, conclusion/limits, required/prohibited action, unresolved conditions and re-review trigger.

Truthfulness, professional constraint and action authority remain separate findings.

## 18. Cross-domain execution handoff

When evidence/calculation/action is outside Business Building, annotate H01–H08:

```text
H01 decision and protected baseline
H02 requested evidence/action
H03 source and semantic mapping
H04 tool/operator binding
H05 authority and constraints
H06 returned result/reconciliation
H07 failure/retry conditions
H08 learning/change impact
```

A read-only export may be enough. No API is mandatory. Reconcile ambiguous irreversible effects before retry.

## 19. Canonical workflows

### 19.1 Greenfield build

```text
frame opportunity
→ customer/problem/value
→ offer + price/money model
→ delivery/economics/cash
→ material assumptions
→ cheapest adequate authorised experiment
→ returned evidence/learning
→ evaluation
→ retain/revise/test/reject/block
```

### 19.2 Existing-business diagnosis

```text
preserve accepted versions
→ symptom/objective
→ reconcile measurement/evidence
→ evaluate implicated components/economics
→ rival constraints
→ supported/provisional diagnosis
→ smallest responsible change
→ approval/external execution
→ returned evidence
→ regression fixture if a reasoning defect escaped
```

### 19.3 Growth workflow

```text
accepted customer + offer + price
→ bounded channel hypothesis
→ acquisition/sales path
→ lead quality + full acquisition effort
→ retained value/economics/capacity/cash
→ independent growth gates
→ bounded test/increase or stop
```

### 19.4 Extension Pack authoring

Pack production uses the separate contract in [05 — Customisation Packs](05-business-building-customisation-packs-spec.md). Ordinary business work must not require a pack.

## 20. Artefact acceptance

An artefact is complete for its bounded purpose when facts/assumptions/unknowns are explicit; source/version identities exist; units/cohorts/windows/bases are coherent; contradictions are retained; mutation/authority boundaries are respected; professional constraints are attributed; relevant economics/capacity/cash/rights remain independent gates; affected/protected layers are explicit; experiments can change decisions; and synthetic design evidence is never represented as customer/installed-product evidence.

Repository/command implementation lives in [03 — Repository and Contracts](03-business-building-skills-repository-and-contracts-spec.md). Evaluation rules live in [04 — Testing and Benchmark](04-testing-and-benchmark-spec.md).

## 21. Research lineage

Primary accepted source logs:

- [Stage 4 business/customer/value model](research-logs/2026-09-10-stage-04-business-customer-and-value-model.md)
- [Stage 5 offer/pricing architecture](research-logs/2026-09-10-stage-05-offer-and-pricing-architecture.md)
- [Stage 5 money-model taxonomy](research-logs/2026-09-10-stage-05-money-model-taxonomy.md)
- [Stage 6 demand/lead/sales architecture](research-logs/2026-09-10-stage-06-demand-lead-and-sales-architecture.md)
- [Stage 7 delivery/retention model](research-logs/2026-09-10-stage-07-delivery-and-retention-model.md)
- [Stage 7 unit-economics/cash contract](research-logs/2026-09-10-stage-07-unit-economics-and-cash-contract.md)
- [Stage 8 assumptions/experiments/learning](research-logs/2026-09-10-stage-08-assumptions-experiments-and-learning.md)
- [Stage 8 constraint diagnosis/repair](research-logs/2026-09-10-stage-08-constraint-diagnosis-and-repair.md)
- [Stage 9 ethical/legal handoffs](research-logs/2026-09-10-stage-09-ethical-and-legal-handoffs.md)

This canonical specification expresses the accepted workflow contracts independently while retaining these logs as provenance.
