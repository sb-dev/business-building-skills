# Stage 8 — Assumptions, Experiments, Learning and Constraint Diagnosis

**Version:** 1.0  
**Date:** 9 September 2026  
**Status:** Design complete  
**Branch:** `feat/bootstrap`

## 1. Decision

Use an explicit assumption → test → evidence → interpretation → decision loop. Uncertainty and consequence remain separate dimensions. No opaque universal risk score is introduced.

An experiment is useful only when its possible outcomes can change a decision. Activity, traffic, conversations or generated artefacts are not learning by themselves.

## 2. Assumption register

Each material assumption records:

```text
assumption_id
statement
category
current basis: observed | reported | derived | assumed | synthetic
uncertainty: low | medium | high, with rationale
consequence_if_wrong: low | medium | high, with rationale
decision_affected
evidence_refs
owner
next_test_or_commitment
status: open | supported | challenged | superseded
```

Candidate categories include customer existence, problem importance, reachability, offer comprehension, willingness to pay, channel economics, sales-path feasibility, delivery, received value, retention/repeat behaviour, unit economics, cash timing and scalability.

Prioritisation is a transparent ordering decision: high-consequence/high-uncertainty assumptions normally deserve earlier evidence, but cost, reversibility, dependencies and professional constraints may change the sequence. Do not multiply ordinal labels into a fake precision score.

## 3. Experiment contract

```text
experiment_id
assumption_id
hypothesis
decision_that_can_change
target_population / unit
method and cheapest adequate representation
baseline / comparison where relevant
primary signal and denominator
secondary/guardrail signals
sample/duration rationale where relevant
known confounders
success condition
failure condition
inconclusive condition
stop conditions
cost/exposure limit
authority and required reviews
instrumentation/data-quality checks
```

The cheapest test must still be valid for the claim. Interviews can test understanding and problem context but not establish a population conversion rate. A landing-page interest test must not imply a product exists when it does not. An A/B test needs suitable assignment, measurement and population; low-volume enterprise sales may require a different design.

Where sample size or duration is statistically material, use appropriate deterministic/statistical tooling and document assumptions. Do not invent a universal minimum sample size.

## 4. Learning record

After execution preserve:

```text
what actually happened
observed evidence and source
measurement/data-quality status
result: supports | challenges | inconclusive
interpretation and alternative explanations
decision: preserve | revise | repeat | pause | stop | commit
confidence and limits
what remains unknown
next action and allowed mutation scope
```

Success criteria must exist before interpreting results. A test with invalid instrumentation is inconclusive even if its headline metric is attractive. Negative evidence can produce a high-quality stop decision. A positive result supports only the claim and population actually tested.

## 5. Constraint taxonomy and diagnosis

Candidate constraint layers:

```text
customer/problem evidence
reach/channel
qualification/sales process
offer/proof
price/monetisation
delivery/onboarding
capacity/quality
retention/continued value
unit economics
cash/working capital
measurement/experiment quality
professional/legal authority
```

Diagnosis sequence:

1. Define the business objective and failing observation.
2. Validate the metric, denominator, period and data source.
3. Identify plausible layers and interactions.
4. Preserve accepted decisions whose evidence still applies.
5. Gather the cheapest evidence that distinguishes leading explanations.
6. Name the current binding constraint only when supported.
7. Propose the smallest responsible change and mutation scope.
8. Measure whether the targeted condition improves without unacceptable guardrail damage.
9. Reassess the next constraint.

A bottleneck is relative to an objective. The lowest metric is not automatically the binding constraint. Several constraints may interact; where evidence cannot isolate one, record the diagnosis as provisional.

## 6. Repair routing

| Evidence pattern | Owning layer | First repair |
|---|---|---|
| Relevant audience cannot be reached | Channel/access | Test a different authorised access route |
| Reach exists, customer problem not recognised | Customer/problem or positioning | Revisit evidence/message before increasing volume |
| Qualified interest, offer misunderstood | Offer/proof | Clarify scope/outcome and retest |
| Offer accepted, economics fail | Price/cost/delivery | Recalculate and change the responsible economic input |
| Sales exceed capacity | Delivery/capacity | Constrain intake or repair bottleneck |
| Contribution positive, cash fails | Timing/working capital | Change supported payment/growth timing |
| First value delivered, continuation weak | Continued value | Investigate outcomes/onboarding before cancellation friction |
| Experiment cannot distinguish outcomes | Experiment design | Repair measurement/test before business redesign |

## 7. Preservation contract

An accepted decision records conditions under which its evidence applies. A repair may mutate only the fields/layers named in its scope. Downstream dependencies are reviewed, not automatically rewritten.

If a channel test fails, preserve customer, offer, price and delivery decisions unless evidence implicates them. If new evidence contradicts a previously accepted customer premise, reopen that premise and explicitly review dependent decisions. Preservation is disciplined change control, not attachment to old choices.

## 8. Synthetic fixture

A fictional service gets 20 qualified conversations but zero purchases. The price was changed at the same time as the sales script, and half the conversations were with a different segment. The result cannot isolate price or script effects. The correct record is inconclusive for both causal hypotheses, while still observing zero purchases in the mixed cohort.

The next test should not redesign customer, offer, price, brand and channel simultaneously. First restore a coherent target population and change one consequential variable where feasible.

## 9. Exit

The project now has an assumption register, falsifiable experiment contract, evidence-preserving learning record, constraint taxonomy and repair-routing model. Stage 9 adds professional/legal handoff gates; later commands must implement these semantics without inventing evidence.

*Stage 8 · Version 1.0 · 9 September 2026.*
