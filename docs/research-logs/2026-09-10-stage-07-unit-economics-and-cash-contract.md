# Stage 7: Unit-economics contract and cash-risk model

**Date:** 10 September 2026  
**Branch:** `feat/bootstrap-2`  
**Authority:** [Original bootstrap v1.1, §14](2026-09-08-business-building-skills-new-project-bootstrap-process.md), especially explicit LTV/CAC assumptions, calculation ownership and the growth exit.  
**Companions:** [Delivery and retention models](2026-09-10-stage-07-delivery-and-retention-model.md), [research and checks](2026-09-10-stage-07-research-and-checks.md), [conformance](2026-09-10-stage-07-conformance.md).  
**Boundary:** Managerial decision contracts, not statutory accounting, tax advice, a payment system or an approved real-business forecast. Source references R01–R22 resolve through the research companion.

## 1. Ownership, evidence and compatibility

Business Building defines the decision, units, assumptions, comparison and required interpretation. Deterministic calculation tools execute the arithmetic; operational/accounting systems supply source records; qualified professionals determine applicable accounting, legal and tax treatment. An agent may organise and calculate a supplied scenario within its brief, but cannot invent missing records, choose an accounting policy on behalf of a client, or treat a model result as authority to spend, charge, borrow or hire.

Keep the [Stage 4 evidence contract](2026-09-10-stage-04-business-customer-and-value-model.md) and [Stage 6 acquisition contract](2026-09-10-stage-06-demand-lead-and-sales-architecture.md). Source, assumption, measurement, interpretation and decision remain separate. Every material external fact needs appropriate current verification; a historical source register is not an evergreen market-data feed. A scenario can be useful with labelled assumptions, but critical unknowns block a substantiated growth claim.

### 1.1 Preserve the Stage 5 commercial definitions

The accepted [offer/pricing architecture](2026-09-10-stage-05-offer-and-pricing-architecture.md) defines `G` as gross commercial consideration for the business's own exchange, `D` as discounts, `F` as reducing refunds/credits, `N = G - D - F`, `K` as the declared directly attributable cost scope and `C = N - K` as direct contribution. Preserve those exact meanings. `C - A - H` is a residual after declared acquisition and other costs, not automatically net profit. Adjustments, labour and commissions must not be deducted twice.

**N is not automatically recognised revenue, and direct costs are not necessarily all variable costs.** A comparison can allocate committed labour to an engagement even when that labour does not create a new cash outflow. Equally, a future capacity step can turn an apparently fixed resource into an incremental commitment. Record the decision horizon and alternatives, not only the accounting label. R08 supports relevant-cost distinctions; R10's revenue-recognition overview demonstrates why delivery and payment events must not be collapsed. Neither source supplies a treatment decision for a particular customer contract here.

### 1.2 Cost and revenue bridges

Retain one canonical identity for each commercial event, adjustment, cost and obligation. The same item can appear in different **views**, but within one total it appears once. Each material cost record contains the amount or calculation, currency, period, source/assumption, purpose, unit/cohort attribution, behaviour over the decision horizon, cash timing and allocation basis. Mark costs excluded from a view. Do not create an accounting ledger in this repository.

Use separate, explicitly reconciled views:

| View | Meaning and reconciliation |
|---|---|
| Commercial exchange | Stage 5 G, D, F, N and declared K/C for the stated transaction or obligation horizon. These amounts can precede or follow recognised revenue and cash. |
| Accounting gross margin | Supplied recognised net revenue R and matched cost of sales S under the applicable accounting policy: gross profit R - S, margin (R - S) / R when R > 0. Record policy, period and classification. Business synthesis does not certify it. |
| Variable-cost contribution | For a declared aligned revenue basis B and included variable costs V: B - V. If B is recognised revenue, call it a period contribution; if B is commercial N, identify that horizon instead. Show acquisition inclusion separately. Do not silently relabel Stage 5 K as V. |
| Decision-relevant change | Difference between feasible alternatives in future receipts, avoidable costs, additional fixed commitments and opportunity consequences. Sunk or unchanged allocated costs do not become new cash outflows merely because a cost report contains them. |
| Whole-business sustainability | Include the resources and fixed obligations needed to continue, even when a short-run incremental decision is positive. Reconcile total cash compensation, facilities, maintenance and other material costs; missing categories prevent a net-profit conclusion. |
| Cash | Actual or forecast usable collections and payments on dates, plus verified funding. Recognition, non-cash allocation and opportunity costs are not themselves cash movements. |

A bridge identifies the difference in recognition timing, discounts/refunds, cost classification/allocation, included acquisition/shared costs and cash dates. Do not add results from these views: they are alternative descriptions of the same underlying business, not independent income streams. If the bridge is unavailable, report the views as non-comparable and request the missing data rather than picking the most favourable margin.

For a constrained employee, compare the complete alternative cash/contribution consequences. Do not both deduct an unchanged salary as incremental expenditure and charge the full foregone margin of displaced work. Conversely, removing salary from an incremental-cash view does not create free long-term labour or extra hours. The delivery model records the real shared resource constraint.

## 2. Metric contract: all twelve required economic concerns

Every metric carries: name/version and decision; formula or event rule; unit; numerator/denominator; population/cohort and attribution; period and elapsed observation age; currency/conversion; revenue and cost basis; included/excluded components; source/assumption; realised versus forecast status; calculation method/rounding; limitations; owner and review trigger. These fields may link to shared definitions instead of duplicating them. Undefined, unavailable and not applicable are distinct from zero.

| ID | Required metric concern | Definition and required evidence | Interpretation, failure and repair |
|---|---|---|---|
| UE01 | revenue per customer / transaction | For an aligned scope, divide the declared own-revenue basis by the defined distinct customer or transaction count. Label commercial N, recognised R, recurring run rate and collections separately. Preserve refunds, discounts, tax/pass-through treatment and mixed currencies. | A customer average is not a transaction average or cash per sale. More than one invoice can belong to one customer. Repair unit, period or party attribution before diagnosing pricing; never call marketplace gross volume own revenue without the appropriate basis. |
| UE02 | gross margin | Use (R - S) / R for positive supplied recognised net revenue R and matching cost of sales S. Disclose accounting basis and cost classification, including material fulfilment, hosting or labour treatment. R10; the bridge above. | A direct-commercial or variable-cost residual is not necessarily accounting gross margin. Positive gross profit can coexist with losses after acquisition/fixed costs or negative cash. Request professional treatment where classification is unresolved. |
| UE03 | contribution margin | Preserve Stage 5 direct contribution C/N when N > 0. Where variable-cost contribution is needed, separately define (B - V)/B and reconcile V against K and A. Include volume-dependent costs and capacity-step effects in the actual decision. R08–R09. | Do not improve the percentage by changing exclusions or counting fixed allocations as avoidable cash. Negative or zero revenue makes these margin percentages not meaningful; retain absolute amounts and causes. |
| UE04 | cost to serve | Declare attributable onboarding, delivery, infrastructure/materials, support, rework, remedies and service-management costs for the customer/transaction/cohort and horizon. Show direct, allocated and incremental views as needed. R03–R04, R08. | A low marginal software cost does not prove low support or human cost. Average cost can hide heavy-use or high-failure cohorts. Repair the implicated workload, scope, classification or population rather than assuming every customer costs the mean. |
| UE05 | customer acquisition cost | Reuse Stage 6 A divided by matched new paid customers where the count is positive. Identify media, production, sales/partner effort, tools, commissions, allocation, unsuccessful/pending work and lag. Cash-only CAC is a separate view. | Zero customers means the ratio is not defined, not zero acquisition cost. Renewal/expansion and free signups are not new paid customers. A labelled attribution is not a causal incremental estimate. Incomplete scope or time windows block acceptance of a CAC claim. |
| UE06 | payback period | State acquisition outflow/cost basis, start event, per-customer or cohort unit and recovery basis. Locate the first observed or forecast date when cumulative contribution or net service cash covers that acquisition amount; identify which basis is used. | Booking value is not cash recovery. If the horizon ends before recovery, say not reached within that horizon. Repeated later refunds/costs can reverse first recovery; do not equate first crossing with permanent cash safety. |
| UE07 | retention / churn | Use the delivery companion's point, continuous-survival or due-renewal cohort definitions. State exit event, reactivation, voluntary/involuntary classification, window, missing observations and counts, with the exact source-event and eligibility rules. R11, R13–R15. | A provider's rolling churn denominator is not necessarily a starting-cohort exit probability. No constant-hazard or unlimited-life forecast follows from one window. Reconcile the event/population before recommending retention spend. |
| UE08 | repeat purchase | Report original customers with a qualifying subsequent retained purchase / eligible original customers over equal follow-up, alongside repeat transaction count and frequency. State refund, same-order, reactivation and cutoff rules. R12. | No purchase yet is not established permanent churn in a noncontractual model. Do not pool immature customers with fully observed ones and call the result a comparable rate. Keep latent departure and observed repeat behaviour distinct. |
| UE09 | lifetime value assumptions | State whether the number means revenue, gross profit, direct contribution, variable contribution or discounted cash; define entry population, horizon, retention/repeat model, margin/cost evolution, expansion, discounting and evidence. Use realised-to-date separately from a forecast. R11–R14. | A revenue dashboard LTV does not pay acquisition or service costs. Unobserved retention, heterogeneity and changing economics can invalidate simple extrapolation. Use finite scenarios or unknown rather than a confident lifetime multiplier without support. |
| UE10 | refund / chargeback rate | Define request versus issued versus settled refund; amount-based versus count-based rate; original payment/order cohort versus event-date activity; duplicates, partial refunds, dispute outcomes and cutoff. Preserve actual fees and recovery timing. R19–R20. | A dispute can arrive after the sale cohort closes. Do not subtract a refunded/disputed principal twice or erase an event because a dispute was won. Repair identity/window handling before attributing a changed rate to customer quality. |
| UE11 | sales cost | Include prospecting/qualification, calls, proposals, specialist reviews, concessions administration and commissions across won/lost/pending work. Record time valuation, cash cost, allocation and role capacity. Reuse Stage 6 A. | Sales cost per win can hide unfinished or unsuccessful work. A commission already in A is not added again to K. Separate acquisition, renewal and expansion effort and compare like windows. |
| UE12 | support cost | Account for demand type, handling/resolution/rework effort, channels, tools, escalations, fixed coverage and incremental load. Attribute to appropriate cohorts while reconciling shared staffing and failure costs. R03–R04, R06. | Cost per closed ticket alone can reward premature closure or obstructed access. Include unresolved work and quality. Avoid subtracting a salary both through cost allocation and as an extra cash expense in the same view. |

No universal margin, LTV/CAC ratio, payback limit, retention percentage or acceptable dispute rate is introduced. Any real threshold needs the owner's objective, evidence, model context, obligations and appropriate specialist constraints. Existing provider reports are evidence with definitions, not the repository's authoritative business truth.

## 3. LTV, CAC and payback acceptance

### 3.1 Finite, explicit customer-value scenarios

Prefer a directly observed cohort contribution-to-date where sufficient. To forecast, choose a finite horizon justified by the decision and evidence. One permitted scenario representation is:

```text
forecast contribution value over T periods
  = sum_t(expected cohort contribution in period t / (1 + discount_rate)^t)
    / original acquisition cohort size
```

The expected cohort contribution includes the chosen revenue/cost basis, retention or repeat behaviour, refunds, customer mix, expansion and support. State time-zero convention and whether costs occur before or after delivery/collection. Costs that survive churn, such as committed coverage or exit remedies, cannot disappear just because revenue stops. Acquisition is excluded from this value by default and shown once as a separate deduction for the acquisition decision. A source using an after-acquisition definition must be labelled and reconciled, not charged CAC again.

This is arithmetic over explicit assumptions, not a universal customer-behaviour model. Retention probability, purchase frequency, average order value and cost may interact; multiplying independent averages can be misleading. Account for joint scenarios when dependence matters. Record observed coverage, censored cases, selection, population changes and forecast uncertainty. A short cohort does not supply evidence for an indefinite tail. Discount rate and currency are supplied scenario choices, not investment or financing advice.

For an intentionally simple constant-contribution illustration, assume contribution m occurs immediately in period zero, the customer leaves with probability c after each period, all future contribution ceases at departure, and per-period discount rate r is nonnegative. Then:

```text
finite value(T) = sum for t = 0..T-1 of m * ((1-c)/(1+r))^t
```

Only if the stationarity and horizon assumptions are justified and the ratio is below one does the infinite geometric sum exist: `m*(1+r)/(r+c)`. At r=0 and c>0 this is m/c. When c=0 and r=0 there is no finite infinite-horizon value; the finite sum is still m*T. A revenue-based ARPU cannot be substituted for m without changing the result's meaning. A rolling churn ratio with entrants in the denominator cannot automatically be substituted for c. Invalid probabilities, missing horizon or inconsistent period units are rejected rather than repaired with made-up defaults.

The project does not make the infinite formula the default, calibrate a survival model, or assert a realistic discount rate here. R12–R13 justify distinguishing behavioural models and their settings; the displayed equations follow from the stated scenario and are checked deterministically. More complex modelling belongs in an appropriate existing calculation/research tool with auditable assumptions, not a custom universal LTV engine.

### 3.2 Comparable acquisition and payback

Before accepting LTV/CAC, identify numerator and denominator cost bases, acquisition cohort and time window, currency, maturity, allocation and missing costs. A customer-value forecast and historical blended CAC can be compared only with the transfer limitation visible. Average past CAC and retention do not demonstrate the marginal economics of a larger future campaign. A positive ratio never overrides current capacity, customer rights or cash dates.

For cash payback, use acquisition outflow plus dated customer receipts minus the cash costs and refunds necessary for that cohort's service under the stated scope. Show other obligations and funding in the business cash model rather than disguising them as customer receipts. A first recovery date is one result; minimum subsequent balance and remaining obligation exposure are separate. An annual receipt that covers acquisition today may leave tomorrow's fulfilment unfunded.

## 4. Cash-risk model: all eleven concerns

Use a dated cash calendar supported by source records and explicit scenarios, not a profit total relabelled cash. The time horizon must encompass the commitment it informs and its material collection, delivery, renewal and refund consequences. A rolling near-term view can coexist with a longer obligation view; truncating a prepaid service at collection is not sufficient.

| ID | Required cash concern | Required representation and evidence | Risk, decision and bounded repair |
|---|---|---|---|
| CA01 | customer prepayment | Record actual cleared receipt, restrictions, customer/offer, remaining service and refund obligations, and permitted use. Pair early collections with future cost/capacity scenarios and a source-located schedule of outstanding obligations. R10, R17, R19. | Prepayment improves timing, not necessarily contribution or free cash. Do not spend all proceeds on acquisition without funding existing promises. Review pace, reserves or approved terms before assuming more sales solve the gap. |
| CA02 | receivables | Separate quote, contract, invoice, due date, disputed/overdue amount and actual collection. Forecast clearing dates with supported assumptions, delay/default scenarios and collection effort, including the payer and evidence of any revised agreement. R16–R17. | An invoice is not money available for payroll. Repair collection, billing accuracy, timing or approved credit terms; do not change a validated value proposition because the payer is late. |
| CA03 | supplier terms | Record committed orders, deposits, credit conditions, due dates, currency, minimum quantities, early-payment effects and supplier capacity/reliability. Identify source agreements, cancellation conditions, fulfilment dependencies and the owner authorised to renegotiate. R16–R17. | Never assume unused or interest-free supplier credit exists. Delayed payment can change availability, price or terms. Compare feasible agreed alternatives; the agent cannot unilaterally postpone an obligation. |
| CA04 | inventory | Track opening stock, purchases, lead times, landed cash costs, usable/sold/returned/lost stock and replenishment commitments. Align sales and recovery assumptions with actual stock and fulfilment. R16, R17. | Purchasing inventory uses cash before or independently of its expense as cost of sales. In a direct cash schedule, do not deduct both the supplier payment and an additional inventory-change adjustment for the same outflow. |
| CA05 | payroll | Use approved gross compensation, employee deductions, net pay, employer costs and remittance/benefit dates. Record hiring start, notice/commitment and actual availability separately, alongside the approved payroll source and period. R17, R21. | Net pay plus withheld amounts remitted is not paid in addition to gross pay: reconcile the components once. Employer charges and benefits can be extra. No salary, tax rate or worker classification is guessed. |
| CA06 | refund exposure | Link actual and potential remedies to eligible cohorts, request/settlement lags, dispute fees, recoverable stock, remaining service and usable funds. Use mutually coherent base and downside cases. R19–R20. | A pending processor balance cannot necessarily fund an immediate refund. A reserve is a cash restriction or planning floor, not itself a second expense when the refund is later paid. Do not assume refunds and continued full service occur together unless the obligation actually requires both. |
| CA07 | advertising spend timing | Reuse Stage 6 cost scope but record cash charging, deposits/credits, billing thresholds where relevant, payment dates and conversion/collection lags. Reconcile campaign billing with actual cash charges and remaining card payables. R17; accepted Stage 6. | Attributed revenue may arrive later or never. Card payment postponement is a dated payable, not cancelled spend or guaranteed free finance. Bound growth by verified funding and obligations, not a headline return ratio. |
| CA08 | tax obligations | Obtain applicable jurisdiction/entity/activity, basis, amount or approved estimate, tax periods, due and clearing dates, withheld/collected amounts and reviewer. R21–R22 are examples of jurisdiction-specific schedules, not defaults. | Unknown tax is not zero. Do not choose rates, eligibility, exemptions or filing treatment; request qualified inputs and assess sensitivity. A tax-related cash gap cannot be solved by ignoring or silently deferring payment. |
| CA09 | working capital | Distinguish formal current assets less current liabilities from the selected operating measure, often inventory plus trade receivables less trade payables. State inclusions, measurement dates and changes. R16. | A healthy ratio does not prove available cash or appropriately valued stock. Avoid counting customer/counterparty funds as unrestricted assets. Repair the actual stock, collection or obligation timing; reconcile any indirect bridge to the direct calendar. |
| CA10 | cash conversion | Where meaningful, calculate inventory, receivable and payable days with matched average balances, period flows and day basis. Cash conversion cycle is inventory days + receivable days - payable days. R16. | A negative cycle can coexist with poor margins and future obligations. Do not force inventory days into a pure service model, use incompatible denominators or infer clearing dates from an annual average alone. |
| CA11 | runway | Show the first date usable cash breaches the required floor in the dated scenario. A cash/net-burn ratio is only a labelled approximation when burn is positive, comparable and sufficiently stable. R17–R18. | Zero/negative average burn does not establish infinite safety; seasonal payments or refund obligations can create a near-term breach. Report minimum cash, breach date, funding gap and assumptions instead of relying on an average. |

### 4.1 Direct cash calculation and controls

Start from reconciled opening cash. Identify restricted/customer/partner amounts separately and declare whether the main schedule is total bank cash or usable business cash. Do not count a transfer of counterparty funds as business revenue. Remove restricted amounts once in a usable-cash view; when a restricted obligation settles, reduce the corresponding restricted balance as well so the same obligation does not drain usable cash twice.

For ordered dates/events under one consistent basis:

```text
closing_cash_t = opening_cash_t + receipts_t + authorised_funding_t - payments_t
opening_cash_next = closing_cash_t
headroom_t = usable_cash_t - required_floor_t
funding_gap = max(0, -min_t(headroom_t))
```

Separate customer collections, tax/pass-through receipts and financing. Financing availability, draw dates, fees, covenants, repayment and authority require evidence. A possible investment or unused credit limit is not actual cash. Do not infer suitable borrowing or approval from a positive forecast.

Order materially different dates within a month. When same-day ordering is uncertain and liquidity is tight, examine the adverse order rather than netting away an intra-day risk. A positive month-end balance can hide inability to pay earlier. Missing dates, inconsistent signs, duplicate event IDs or mismatched currencies fail validation; do not silently coerce them into favourable values.

Keep direct and indirect cash methods separate. The direct calendar uses actual/forecast receipts and payments. An indirect reconciliation starts from a defined profit basis and adjusts non-cash items and working capital. Do not deduct an inventory purchase, then deduct the same cost again through cost of sales and the inventory movement. A specialist or existing accounting tool provides the accounting bridge where needed; the skills compare its reconciled results, not rebuild the ledger.

Compare a baseline supported by current obligations with downside cases relevant to the commitment: slower receipts, weaker retention, higher usage/support, supplier delays, refunds/chargebacks, reduced availability or a capacity step. Preserve joint consistency. For example, a cancelled service may require a refund and cessation of some future work, while sunk work and other obligations remain. Do not add mutually exclusive worst cases and call the result an expected forecast, or omit a plausible coupled failure because single-variable sensitivities look safe.

### 4.2 Cash conversion and runway details

For period length d and aligned positive denominators, use inventory days = average inventory / cost of sales * d; receivable days = average trade receivables / credit sales * d; payable days = average trade payables / credit purchases * d. The balances and flows must use compatible currency and tax bases. A cost-of-sales proxy for credit purchases or closing-balance proxy for average stock is disclosed, not silently treated as observed equivalence. R16's exam assumptions are not assumptions for a live business.

Zero flow can make a ratio undefined even when the balance is meaningful. A genuinely inventory-free business can state inventory days not applicable, with the reasoning for any zero component used in a simplified cycle. Large seasonal swings, mixed cash/credit sales and long work in progress can make average-day measures poor forecasts of dated payments. The cash calendar remains the decision basis.

A stationary runway approximation divides opening usable cash above a declared floor by positive comparable periodic net burn. State period, excluded one-off payments and forecast limitations. If burn is zero or negative, the ratio is not a useful finite runway estimate; examine the dated obligations and possible downside instead. Growth can consume working capital faster than it earns cash even with positive unit contribution. No generic number of months is an approval threshold.

## 5. Deterministic calculation handoff

The smallest useful calculation handoff has these fields, whether implemented by a spreadsheet, calculator, existing accounting system or temporary verification script:

| ID | Handoff field | Contract |
|---|---|---|
| HC01 | decision and scope | State the business decision, accepted versions, calculation view, alternatives, horizon and material obligations. |
| HC02 | inputs and provenance | Provide source-located observations and separately labelled assumptions; units, currency, cohort, dates, exclusions and access boundary are explicit. |
| HC03 | definitions and formulas | Supply metric versions, cost/adjustment identities, revenue recognition boundary, allocation, timing convention and formula. No unexplained dashboard number is sufficient. |
| HC04 | calculation method | Identify tool/version or reproducible method, input representation, rounding policy and prerequisites. Use decimal money arithmetic or verified spreadsheet formulas; retain unrounded intermediate values where appropriate. |
| HC05 | validation and reconciliation | Check signs, ranges, uniqueness, units, matching periods, totals, balance bridges, zero denominators and boundary cases before interpreting results. |
| HC06 | outputs and scenarios | Return absolute amounts, denominators, ratios where defined, minimum dated cash/headroom, capacity consequences, base/downside results and error states. |
| HC07 | professional and authority boundary | Identify treatment requiring accounting/tax/legal input, unresolved facts and exact permitted action. Calculation success cannot grant commercial approval. |
| HC08 | evidence and review | Preserve the executed input/output identities, run result, limitations, owner, decision and trigger for recalculation. Do not claim a script was executed merely because it exists. |

Choose a simple calculator for a bounded verified expression, a transparent spreadsheet for linked scenarios, or an established operational/accounting tool for actual records and policy-driven reporting. The specific tool landscape and execution selection belong to Stages 10–11. This stage establishes responsibilities and demonstrates arithmetic with private verification code; it introduces no product runtime or custom accounting engine. Sensitive raw business data stays in its authorised location; public examples are synthetic or explicitly approved/redacted.

## 6. Independent growth gates and repair routing

A recommendation to increase revenue-producing commitments must state the amount, timing, existing obligations and decision owner. Apply every relevant gate below; no weighted score can offset a blocking failure. Unknown material facts produce **BLOCKED**, adverse evidence **FAIL**, adequate bounded support **PASS**; **NOT APPLICABLE** needs a reason grounded in the business mechanism. These are evaluation results, not autonomous execution states.

| ID | Gate | Required evidence and consequence |
|---|---|---|
| GG01 | evidence and definition integrity | Customer, offer, cohort, cost and time-window inputs are traceable and compatible. Undefined CAC or unsupported LTV blocks the conclusion; repair records/definitions before changing the business. |
| GG02 | deliverable value and quality | The accepted promise has relevant delivery/outcome evidence, feasible dependencies and appropriate quality/recovery controls. Unsupported benefits or unsafe service block the affected commitment. |
| GG03 | operational capacity | Existing plus proposed sales, onboarding, delivery and support work fits each resource and material due-date/service-level constraint under justified scenarios. Bound intake or repair the responsible constraint; don't invent extra staff. |
| GG04 | economics and sustainability | Contribution and wider resource funding are coherent on explicit bases; marginal scale effects and excluded costs are visible. Negative contribution cannot be labelled profitable growth. A deliberately funded test is separately authorised and labelled, not a waiver. |
| GG05 | retention, expansion and downstream quality | The business's dependence on repeat value is evidenced or bounded as an explicit test. Billing, new acquisition and expansion cannot hide cohort decay, refunds or excessive cost to serve. One-off models justify which repeat assumptions are not needed. |
| GG06 | cash and obligation coverage | Dated usable cash covers existing and proposed obligations and the declared floor over an adequate horizon and relevant downside. Missing tax/funding data or a negative headroom blocks safe-scale claims even when margins are positive. |
| GG07 | customer rights, professional constraints and authority | Truthful terms, accepted entitlements, relevant specialist constraints and the responsible owner's permission remain intact. Conversion, a model pass or tool access cannot authorise spend, outreach, changed cancellation terms or a new contract. |

A whole-gate exemption is allowed only for GG05 when no repeat, renewal or expansion dependency is used in the proposed decision. Other gates may contain inapplicable submeasures, but still require their own supported conclusion. Record the result of each relevant gate, evidence, uncertainty, affected layer, retained decisions and permitted next step. A gate can permit a specifically bounded test only when its own actual resource, risk and authority requirements are satisfied; speculative lifetime profit does not fund an experiment. Recalculate affected gates after a repair. Broader redesign is justified only when the evidence shows the dependencies cannot be repaired locally.

The original synthetic checks in the research companion exercise distinct failures: workload hidden by revenue, misleading cost labels, expansion masking exits, unjustified lifetime extrapolation, payback reversal, profitable but unfundable timing, and defined-but-immature repeat/dispute measures. They test this design and arithmetic, not actual business success or an installed agent. The complete assumption/experiment/learning architecture belongs to Stage 8; these contracts provide its economic and operational inputs.

**Exit:** revenue growth is not recommended without separate fulfilment, quality, capacity, economics, retention, cash and authority checks. A responsible result may be retain, a bounded correction, a proposed authorised test, or blocked growth. The current-stage conformance and remotely verified commit establish Stage 7 completion, not the existence of this document alone.
