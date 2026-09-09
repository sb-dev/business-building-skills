# Stage 5 — Offer, Pricing and Monetisation

**Version:** 1.0  
**Date:** 9 September 2026  
**Status:** Design complete  
**Branch:** `feat/bootstrap`

## 1. Basis and decision

Use [Stage 4](2026-09-09-stage-4-business-customer-and-value-model.md) for customer/value evidence and [Stage 3](2026-09-09-stage-3-professional-practice-and-evidence.md) S03, S07–S09, S13–S14, S16–S17 and S20–S21 for independent method, pricing, return, finance and business-model context. Stage 2 concepts OC2–OC5, MC1–MC3 and PC4–PC6 remain candidate inputs, not governing doctrine.

An offer is a **bounded value exchange with deliverable obligations**. Pricing is a hypothesis about that exchange under customer, economic and legal constraints. Monetisation specifies who pays, for which unit, when, and with what ongoing obligations. These must be reviewed together, not optimised as isolated copy or conversion tactics.

## 2. Offer contract

| Field | Required decision |
|---|---|
| Customer and buying context | Which declared/observed customer and decision participants the offer serves |
| Outcome | What is promised; distinguish a controlled deliverable from an uncertain business result |
| Mechanism | Why the proposed work could produce the outcome, with evidence and limits |
| Scope and deliverables | Included work, quantity, quality/acceptance, dependencies and exclusions |
| Time-to-value | Expected delivery/timing, assumptions and what starts the clock |
| Price and unit | Currency, amount/range, pricing unit, quantity and tax/fee treatment requiring review |
| Payment structure | Payment dates, deposits, usage/overage, renewal and collection assumptions |
| Obligations and remedies | Guarantee/refund conditions, process, exclusions and operational ability to honour them |
| Proof | Evidence for each material claim; testimonials require legitimate provenance and permission |
| Added components | Specific customer value, delivery cost and why each belongs |
| Scarcity or urgency | Factual capacity/deadline basis and expiry; omit where unsupported |
| Acceptance and authority | What the buyer must understand and which publication/contract approvals remain |

A material term cannot be hidden in a different artefact while the main price presentation implies otherwise. An internal draft may contain unresolved fields; an offer is not deployable until material obligations and claims are resolved and authorised.

A money-back guarantee, free trial and free plan are different choices. Preserve any explicit accepted project policy rather than adding a trial by default. An optional component or upsell cannot silently weaken the original included service.

## 3. Pricing decision framework

Start with the decision and compare the few alternatives that could change it. Record the current baseline, proposed change, why it may matter, affected customer group, downside and evidence needed.

| Lens or structure | Useful question | Constraint / failure mode |
|---|---|---|
| Cost-informed boundary | What costs and capacity must the transaction support? | A cost-plus calculation does not establish willingness to buy |
| Customer-value pricing | What benefit is attributable and valued? | Avoid unverified ROI promises or treating all generated savings as capturable price |
| Alternative/reference pricing | What does the customer actually compare? | Competitor prices are time-sensitive; avoid invented anchors or comparing different scope |
| Willingness to pay | What behaviour or elicitation supports the price? | Stated preference and real purchase differ; no universal adjustment factor |
| Tiering and packaging | Are there meaningful differences in needs/scope? | Do not create artificial complexity, misleading decoys or hidden essentials |
| Usage pricing | Does the unit match value and controllable costs? | Unpredictable bills, metering errors and unbounded service costs |
| Subscription | Is there continuing value and an understandable renewal? | Billing recurrence alone is not retention evidence |
| One-off purchase | Can value and obligations be satisfied in one exchange? | Underprice lifetime support or continuing delivery promises |
| Retainer | What capacity, access or deliverables are reserved? | Unlimited-work promises with finite capacity |
| Performance-linked fee | Is the outcome measurable, attributable and permitted? | Disputes, external dependencies, regulated implications and delayed cash |
| Freemium/free-to-paid | What is the tested path from free value to paid value? | Free usage is not paid demand; include cost to serve non-paying users |
| Discount | What specific behaviour is being tested or rewarded? | Margin erosion, unfair comparisons and fictitious reference prices |
| Payment timing | Can terms reduce risk without shifting unacceptable obligations? | Upfront receipts create future delivery/refund exposure |

Do not infer price elasticity, optimal price or guaranteed uplift without suitable evidence. A small price test changes one relevant factor where feasible; bundled changes must be identified as such. A statistically or practically inconclusive result remains inconclusive.

## 4. Monetisation taxonomy

Each candidate must instantiate the following contract:

```text
value_exchange
payer and beneficiary
pricing_unit and quantity
revenue_definition
relevant_direct_costs
contribution_boundary
receipt_and_payment_timing
retention_or_repeat_dependency
capacity_dependency
material_risks and approvals
```

The table supplies original analysis prompts, not forecasts or mandatory product choices. Source grounding is the business-model and financial distinction in Stage 3; legal applicability is deferred to Stage 9.

| Model | Exchange, payer and unit | Revenue and direct-cost boundary | Cash, retention and capacity | Main risk |
|---|---|---|---|---|
| One-off goods/digital product | Buyer pays per item/licence | Net sales less relevant returns, payment, production/delivery and support costs | Settlement versus production/inventory; repeat optional; fulfilment finite | Returns, piracy/licence ambiguity or indefinite support |
| Subscription | Subscriber pays per period/seat | Recurring net revenue less period delivery, payment and support cost | Prepaid/in-arrears timing; cohort retention necessary; service load persists | Churn, hidden renewal, annual cash mistaken for monthly profitability |
| Usage | Account pays per measured consumption unit | Unit charges less associated variable compute/service/metering cost | Usage/collection lag; repeat may vary; load-sensitive | Unbounded bill or cost exposure and disputed measurement |
| Fixed-scope service | Client pays per engagement | Project revenue less scoped labour, subcontracting and direct expenses | Milestones/deposits; repeat optional; operator hours bind | Scope creep, effective-rate erosion and late receipts |
| Retainer | Client pays for defined recurring access/work | Period fee less committed delivery/support resources | Cash and reserved capacity align by period; renewal matters | Selling the same scarce capacity twice |
| Licensing | Licensee pays for defined rights/period/use | Licence receipts less support, distribution and attributable obligations | Timing depends on contract; renewal varies; support/licensor capacity | Rights not owned, unenforceable scope or unsupported maintenance |
| Marketplace commission | Participant pays per eligible completed transaction | Platform revenue on stated principal/agent basis, not automatically total transaction value; subtract payment/dispute/service costs | Settlement, reserves and two-sided liquidity; repeat/matching matter | Unfunded incentives, disputes and confusing GMV with revenue |
| Advertising-funded | Advertiser pays per agreed media/action unit | Advertising receipts less production, distribution and sales/delivery costs | Collection may lag audience costs; audience quality persists | Privacy, attribution, editorial trust and weak buyer demand |
| Affiliate/referral revenue | Partner pays per verified eligible referral/sale | Commissions net of reversals and acquisition/content costs | Attribution windows and payment lag; partner dependence | Undisclosed incentives, low-quality traffic and unstable terms |
| Paid support/services around open source | Client pays for specified service/support | Service receipts less actual delivery and maintenance obligations | Capacity and collection timing; renewal only if value persists | Confusing free adoption with demand for paid support |
| Education/digital training | Learner or employer pays per course/cohort/access | Sales less teaching, platform, support and fulfilment costs | Cohort cash commitments; refunds and repeat vary | Unsupported outcomes and delivery burden |
| Sponsorship | Sponsor funds agreed visibility/support or contribution | Contracted receipts less agreed obligations | Concentration and renewal uncertainty; work/visibility constraints | Treating an uncommitted sponsor as predictable revenue |

Initial transaction, renewal, upsell, cross-sell and expansion are **events or changes in these exchanges**, not separate universal business models. Record incremental customer value, costs, obligations and cannibalisation before recommending an added transaction. Open-source commercialisation is a portfolio context, not itself a revenue mechanism.

## 5. Economic and ethical consistency checks

Before recommending a stronger offer or scale, ask whether the business can deliver the added scope, fund obligations, substantiate the promise and preserve the customer's understanding of price and conditions. Reject unsupported scarcity, fake testimonials, fabricated ROI and deliberately obscured renewal even when a conversion forecast is favourable.

Review customer fit, proof, contribution, available capacity and dated cash exposure separately. A positive contribution estimate is not whole-business profit. A guarantee must include the cost of unsuccessful delivery and the actual remedy. A legal review dependency blocks the relevant external commitment, not unrelated safe analysis.

## 6. Original worked comparison

**Synthetic arithmetic illustration:** a proposed service is priced at GBP 2,400, with GBP 800 of modelled variable delivery cost including the stated labour basis. Contribution before acquisition and fixed costs is GBP 1,600. This does not prove customers will buy or that the operator has capacity.

Adding a component costing GBP 500 with no price change reduces that contribution to GBP 1,100. Calling the component a bonus does not remove the cost. A full refund after delivery can leave no sales revenue while the delivery cost remains. The decision therefore needs evidence that the additional component is valued and a funded, deliverable remedy policy, not simply more persuasive wording.

No live price, offer or customer commitment is changed by this example. Stage 7 will define reproducible calculation contracts and non-cash labour treatment.

## 7. Failure and repair routes

| Failure | Repair scope |
|---|---|
| Customers misunderstand included work | Scope/wording and acceptance, preserving supported customer/problem evidence |
| Demand exists but delivery loses money | Price, cost or fulfilment model; do not assume more acquisition fixes it |
| Price test is inconclusive | Sampling/measurement/test design before price doctrine |
| Guarantee exceeds capability | Remedy, scope or required review; do not hide conditions |
| Expansion cannibalises viable work | Transaction sequence and capacity allocation |
| Recurring model lacks continuing value | Reconsider recurring exchange, not cancellation friction |

**Exit:** The offer, pricing and money-model contracts distinguish persuasion, customer value, economic viability, cash exposure and professional approval. The next stage can select channels and sales paths without silently changing the approved commercial exchange.

*Stage 5 · Version 1.0 · 9 September 2026.*
