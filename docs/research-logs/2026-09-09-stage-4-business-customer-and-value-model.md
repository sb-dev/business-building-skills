# Stage 4 — Business, Customer and Value Model

**Version:** 1.0  
**Date:** 9 September 2026  
**Status:** Design complete  
**Branch:** `feat/bootstrap`

## 1. Inputs and decision

Inputs are the reviewed Stage 1 charter, Stage 2 capability families K01–K12 and [Stage 3](2026-09-09-stage-3-professional-practice-and-evidence.md), especially S01–S03 and S20–S21. This log defines an independent working representation; it does not reproduce a commercial canvas or claim that the representation itself is empirically validated.

Use a small **business brief plus evidence and decisions**, with an optional machine-readable economic input when calculations are needed. A bounded task can live in one Markdown document. The following are information responsibilities, not mandatory separate files, database tables or a universal graph.

Default consumer location is a user-selected case directory, for example `business/service-test/`. Never overwrite an unrelated existing directory. Do not store customer personal data in the skills repository or examples.

## 2. Business brief contract

| Field | Required content | Unknown handling |
|---|---|---|
| Decision | The bounded choice, owner objective and reason it matters now | Clarify when missing; do not substitute growth as the objective |
| Context | Greenfield/existing, geography/jurisdiction where relevant, business model and time horizon | Label assumptions; jurisdiction-sensitive execution remains blocked |
| Customer roles | Target segment, observed audience, buyer, user, payer, approver and beneficiary where different | Do not invent organisational authority |
| Problem and alternatives | Desired progress, current behaviour, competing approaches and doing nothing | Hypothesis until attributable evidence supports it |
| Value | Relevant benefit dimensions, promised outcome and proof | An attractive description is not outcome evidence |
| Offer | Scope, exclusions, delivery mechanism, price and material obligations | Draft state; Stage 5 supplies the detailed contract |
| Demand and sales | Plausible route to suitable prospects and purchase decision | Hypothesis; no implied live outreach permission |
| Delivery | Work required, capacity, quality, support and dependencies | Unknown delivery cost blocks a confident scale recommendation |
| Economics and cash | Revenue/cost unit, time window, cash obligations and key uncertainties | Separate estimates from actuals; Stage 7 defines arithmetic |
| Continuing value | Repeat, renewal, expansion and referral dependencies, or not applicable | Do not manufacture recurring value for a one-off offer |
| Assumptions and decisions | Consequential uncertainties, current evidence and accepted choices | Stage 8 supplies test/learning semantics |
| Constraints and authority | Approved scope, budget, exclusions, preservation rules and required reviews | Drafting permission is not execution permission |

An entry is adequate when the next decision can be understood and tested. Do not demand every field be fully known before analysis; identify which missing facts block which commitments.

## 3. Customer evidence

Keep **declared target** separate from **observed customer**. One buyer may pay for several users; an influencer may not approve expenditure. For marketplaces, explicitly distinguish each participating side and which party controls price, delivery and dispute resolution.

A customer-evidence item records:

```text
claim_id
statement
basis: observed | reported | assumed | derived | synthetic
source_locator
as_of / observation_window
population / scope
collection_method
limitations
supports_or_challenges: decision or assumption IDs
```

A derived claim also cites its input claims and calculation or reasoning. A reported interview preference remains reported, not observed purchasing behaviour. A synthetic fixture remains synthetic even when its scenario describes fictional observations. No consumer case may be relabelled as actual market evidence because it resembles a realistic business.

Customer evidence may come from interviews, sales discussions, support issues, search/demand data, usage, conversion, retention, alternatives or willingness-to-pay studies. Their evidential roles differ. Search volume can indicate interest in a query; it does not directly establish demand for this offer. A signed purchase establishes a particular commitment, not general population conversion.

For sensitive material, prefer de-identified excerpts or aggregates and reference the authorised source rather than copying unnecessary personal data. Retention and disclosure constraints travel with the evidence.

## 4. Value model

Record only relevant dimensions:

| Dimension | Question | Evidence that may bear on it |
|---|---|---|
| Functional | What can the customer accomplish? | Task outcome, delivered artefact or observed completion |
| Economic | What monetary benefit/cost is supported? | Attributable costs or measured effect with limits |
| Emotional | What experience matters to the customer? | Reported experience, not an invented sentiment |
| Social/status | What identity or relationship consequence matters? | Customer explanation in its context |
| Risk reduction | Which uncertainty or downside is reduced? | Reliability, remedy and supported probability information |
| Time reduction | Which elapsed time changes? | Comparable start/end definitions and observations |
| Effort reduction | Which customer work is removed? | Task steps, burden or effort observations |
| Uncertainty reduction | What decision becomes better informed? | Evidence produced and the decision it changes |

Do not combine these into one universal value score. Separate the promised outcome, mechanism, evidence and limits. Where an economic benefit is unverified, phrase it as a hypothesis rather than a guaranteed saving or return.

## 5. Change and preservation rules

A decision record has an ID, chosen option, rationale, evidence references, acceptance date, accountable approver, applicable conditions, mutation scope and superseded decision if any. Evidence strength is not approval status.

When the target customer changes, review proposition, offer, channel, sales path, delivery assumptions and economics for affected dependencies. Review does not mean overwrite all of them. Record retained decisions with reasons. When price changes, inspect conversion, cash, obligations and economics without casually rewriting the problem model.

A bounded command declares the fields or files it may change before producing a patch or proposed replacement. Preserve unrelated accepted text and measurements. Contradictory project facts require resolution; do not silently choose whichever makes the recommendation easier.

Use simple IDs and local references to make these relationships inspectable. No automatic cross-project customer graph, persistent universal customer database or new lifecycle engine is introduced.

## 6. Working template

```markdown
# Business brief: <case>

## Decision and objective
<Choice, accountable owner, horizon, success criterion and constraints.>

## Customer, problem and alternatives
<Roles; declared segment; observed evidence; current alternative.>

## Value and offer
<Supported outcome; scope; exclusions; price; delivery; proof and limits.>

## Acquisition and sales
<Channel hypothesis; qualification; purchase path; permission limits.>

## Delivery, economics and cash
<Relevant unit, capacity, costs, obligations and unknowns.>

## Continuing value
<Repeat/renewal/expansion/referral dependency or justified non-applicability.>

## Evidence
| ID | Statement | Basis | Source/window | Scope and limits |
|---|---|---|---|---|

## Decisions and next test
<Accepted choices; unresolved assumptions; bounded next action; approvals.>
```

This template may be shortened or expanded for the task. Empty headings do not constitute completed business analysis.

## 7. Original worked representation

**Synthetic fixture, not a real business:** a solo analyst is considering a fixed-scope onboarding audit for small software teams. The buyer is provisionally an operations lead; users are team members performing onboarding. The desired progress is identifying avoidable handoff failures. The current alternative is internal ad hoc review. No customer interviews or purchases have occurred.

The value proposition is therefore a candidate diagnostic service, not a proven saving. The offer may promise the specified audit artefact and review session, but cannot promise a measured revenue increase. Delivery hours, price and acquisition route remain assumptions to calculate and test. The first consequential uncertainty may be whether the buyer recognises the problem and will pay for this scope; the cheap test is selected in Stage 8 after inspecting the other constraints.

This representation distinguishes roles, assumptions, deliverable commitments and outcome claims without inventing traction or importing a software-product lifecycle.

## 8. Checks and exit

Boundary checks: a persona without observed sources remains assumed; a changed segment triggers a scoped dependency review; an interview quotation is not a conversion rate; an approved offer is not market validation; a one-off transaction does not require a retention metric; a synthetic case cannot enter a real evidence register as observed data.

**Exit:** Later offer and growth decisions can trace back to specific customer/value evidence, while unknowns and accepted decisions remain explicit. Stages 5–8 refine the component contracts without changing this lightweight representation. No schemas, skills or production directories are created by this design stage.

*Stage 4 · Version 1.0 · 9 September 2026.*
