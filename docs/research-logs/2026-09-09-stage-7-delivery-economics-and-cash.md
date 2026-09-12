# Stage 7 — Delivery, Retention, Economics and Cash

**Version:** 1.0 · **Date:** 9 September 2026 · **Status:** Design complete  
**Branch:** `feat/bootstrap`

## 1. Basis and decision

Inputs: the reviewed charter and Stages 3–6. Professional grounding is ACCA's distinction between contribution, fixed costs and sales assumptions, and its working-capital treatment; Stripe documents one vendor's configurable subscription metrics, not a universal definition. Sources checked on 9 September 2026 are listed below. The contracts, examples and safeguards in this log are independent project design.

Represent delivery feasibility, unit economics and dated cash separately. A favourable sales projection cannot override a capacity shortfall, unsupported retention or an unfunded obligation. The first implementation needs a small reproducible calculator, not an accounting engine, warehouse or custom billing system.

## 2. Delivery and continuing-value contract

| Responsibility | Required representation | Evidence / corrective question |
|---|---|---|
| Fulfilment | Accepted offer version, work units, sequence, dependencies, accountable owner and acceptance | Can the promised outcome or artefact actually be delivered? |
| Onboarding/time-to-value | Customer inputs, start event, first meaningful value, elapsed time | Is failure caused by missing inputs, unclear scope or the delivery process? |
| Quality/service level | Observable acceptance, support scope, escalation and review interval | Are defects, rework and failures recorded rather than hidden by completion counts? |
| Capacity | Available resources, non-delivery work, buffer, per-unit load and concurrency limits | Can sales, delivery, support and administration fit simultaneously? |
| Support/failure demand | Requests created by normal service and by avoidable failure | Does the operating cost include support and rework? |
| Retention/repeat | Eligible starting cohort, end state, window, exclusions and continuing value | Does continued payment reflect a benefit, or merely friction? |
| Renewal/expansion | Customer need, additional scope, cost, cannibalisation and terms | Does the extra transaction add viable value? |
| Referral | Permission, incentive, qualified outcome and downstream cost/value | Is the referred customer suitable, not merely another contact? |
| Refund/cancellation | Customer understanding, request/event dates, remedy and financial exposure | Can the promised remedy be honoured without obstructing exit? |

One-off models may mark retention not applicable, with a reason. They still need acceptance, support and obligation checks. Monthly customer, subscription and revenue cohorts are not interchangeable. Period comparisons must use compatible definitions and exposure windows.

## 3. Economic measurement contract

Every metric carries name, purpose, formula, input sources, unit, currency, period/cohort, cost boundary, observed/estimated/derived/synthetic basis and limitations. Record excluded costs explicitly. Use gross-margin labels only when the cost-of-sales definition is appropriate and explained; use contribution for the stated managerial variable-cost boundary.

| Measure | Project definition / required qualification |
|---|---|
| Gross sales | Sum of price × delivered/sold units under the stated recognition basis; not automatically collections |
| Net managerial sales | Gross sales less stated refunds/discounts; treatment of taxes and prior-period refunds must be explicit |
| Variable delivery cost | Direct variable labour, compute, goods, fees, support and rework within the declared boundary |
| Contribution before acquisition | Net managerial sales minus variable delivery costs |
| Contribution after acquisition | Previous amount minus matched acquisition and selling costs not already counted |
| Modelled operating result | Contribution after acquisition minus separately identified fixed costs; not audited profit |
| Cost to serve | Relevant delivery/support costs divided by the matching service unit/customer population |
| CAC | Defined acquisition and selling costs / matching new-customer count; a zero count produces undefined CAC |
| Acquisition payback | First period in which cumulative relevant customer contribution or cash recovers acquisition outlay; name which basis |
| Customer retention | Members of a defined starting cohort still meeting the specified active/value criterion / eligible starting cohort |
| Churn | Specified lost cohort members / eligible starting cohort, with reactivation and interval rules; vendor exports may differ |
| Repeat purchase | Eligible first purchasers with a later purchase within the stated horizon / eligible first purchasers |
| Refund or chargeback rate | Distinct affected eligible transactions or refunded value / matching transaction count or value; name denominator |
| Observed finite-horizon customer value | Cohort contribution over an observed horizon / cohort size, with cost and selection limits |
| Forecast LTV | Explicit future contribution scenarios using stated retention, costs, horizon and optional discount assumptions; never substitute revenue/churn mechanically |

Sales and support time cannot disappear because the founder performs them. Keep cash labour costs separate from imputed owner/opportunity cost and state which is included in each view. Avoid subtracting an acquisition expense both in variable cost and again in CAC/contribution after acquisition.

A single-product constant-price/constant-unit-cost break-even comparison may divide relevant fixed costs by positive unit contribution. It is not meaningful at a non-positive contribution or outside those assumptions. Multi-product mix, step costs and capacity require scenarios rather than an unqualified universal formula.

## 4. Cash-risk contract

For each dated interval record opening cash, expected/actual receipts, payments, required earmarked reserves, financing already committed, closing cash and usable headroom. Receivables are not cash. Do not assume debt, investment or a tax outcome that has not been supplied and authorised.

The schedule must account, where relevant, for customer prepayments, receivables and collection delays, supplier terms, inventory, payroll, advertising payment timing, taxes supplied by a qualified process, refunds/chargebacks, platform settlement and reserves, and fulfilment still owed.

Calculation semantics:

```text
closing[t] = opening[t] + receipts[t] - payments[t]
opening[t+1] = closing[t]
headroom[t] = closing[t] - required_reserve[t]
```

A reserve is an earmark, not a second cash payment. Do not deduct it again from next period's opening cash. Record whether payments already include a contingent refund or delivery obligation so it is not counted twice. Inspect the opening balance and intra-period timing when monthly aggregation could hide a shortfall. Ending-period surplus alone is insufficient.

Runway is the first forecast cash/headroom shortfall in the schedule. Cash divided by a single average burn rate is only an explicitly labelled steady-state approximation. No finite shortfall observed within a forecast horizon means 'not reached within this horizon', not infinite runway.

## 5. Small deterministic calculation interface

The initial local calculator will accept UTF-8 JSON and write a result to stdout without editing the input or contacting a provider. Decimal amounts are strings, non-negative where the field requires it; booleans, NaN, infinity and malformed amounts are errors. Currency conversion and statutory recognition are out of scope. Counts are non-negative integers. Unknown required inputs produce a clear blocked calculation rather than defaulting to zero.

Proposed fields, finalised in the repository contract before implementation:

```text
currency, period, basis, unit, cost_boundary
price, units, refunds, variable_cost_per_unit
acquisition_cost, new_customers, fixed_costs
capacity: available_hours, non_delivery_hours, buffer_hours, hours_per_unit
cash: opening, periods[{label, receipts, payments, reserve}]
```

Core arithmetic:

```text
gross_sales = price * units
net_sales = gross_sales - refunds
variable_cost = variable_cost_per_unit * units
contribution = net_sales - variable_cost
contribution_after_acquisition = contribution - acquisition_cost
operating_result = contribution_after_acquisition - fixed_costs
cac = acquisition_cost / new_customers, or null with reason when count = 0
usable_delivery_hours = max(0, available - non_delivery - buffer)
capacity_units = floor(usable_delivery_hours / hours_per_unit)
```

Capacity assumes homogeneous units and hours; other businesses may need different deterministic tools. A negative residual-hours balance is an explicit overcommitment warning, not silently healthy zero capacity. Per-unit refund attribution is not inferred; if refunds relate to earlier orders the input boundary must disclose that. Display rounding occurs at output, not each intermediate operation.

No script emits 'business viable' or 'safe to scale'. It reports arithmetic, capacity/cash warnings and limitations. Interpretation and approvals remain agent/human responsibilities. Stage 22 will test valid, missing, invalid, zero-denominator, negative-contribution, overloaded and reserve-sensitive cases.

## 6. Synthetic worked case and oracle

Two engagements at GBP 2,400 each, GBP 800 variable cost each, GBP 400 acquisition cost, no refunds and GBP 600 fixed cost produce gross/net sales 4,800; variable cost 1,600; contribution 3,200; after acquisition 2,800; modelled operating result 2,200; matched CAC 200 for two new customers.

With 80 available hours, 20 non-delivery hours, a 10-hour buffer and 25 hours per engagement, capacity is two engagements. The projected demand uses all planned delivery capacity; accepting more needs a new scoped capacity decision, not just a more optimistic revenue forecast.

Opening cash 1,000; first-period receipts 2,400 and payments 2,600 produce closing cash 800. A required reserve of 1,000 produces headroom -200. Second-period receipts 2,400, payments 1,000 and reserve 500 produce closing cash 2,200 and headroom 1,700. The later surplus does not remove the earlier headroom shortfall. These are transparent invented inputs, not actual traction or accounting records.

## 7. Diagnosis and exit

A growth recommendation must inspect fulfilled value, support/rework, capacity, unit/cost boundaries, acquisition and selling effort, retention where relevant, collection/payment timing and approval. Unknowns do not automatically mean the business fails; they block unsupported certainty or the affected commitment.

**Exit:** The contracts prevent revenue-only growth recommendations and provide reproducible calculation and failure fixtures for later implementation. No live financial advice, account access, customer data or payment execution is involved.

## Sources

Accessed 9 September 2026. ACCA supports the financial distinctions; Stripe establishes its own documented metric conventions. The calculation interface and fixture are this project's design.

- [ACCA: Cost-volume-profit analysis](https://www.accaglobal.com/gb/en/student/exam-support-resources/fundamentals-exams-study-resources/f5/technical-articles/CVP-analysis.html), contribution, fixed-cost recovery and assumptions.
- [ACCA: Working capital management](https://www.accaglobal.com/gb/en/student/exam-support-resources/fundamentals-exams-study-resources/f9/technical-articles/wcm.html), cash cycle and liquidity.
- [Stripe: Subscription analytics](https://docs.stripe.com/billing/subscriptions/analytics), metric/configuration definitions. No vendor benchmark or pricing forecast is adopted.

*Stage 7 · Version 1.0 · 9 September 2026.*
