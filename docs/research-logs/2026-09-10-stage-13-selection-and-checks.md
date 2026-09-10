# Stage 13: Command selection, workflow comparisons and design checks

**Date:** 10 September 2026  
**Branch:** `feat/bootstrap-2`  
**Authority:** [Original bootstrap §20](2026-09-08-business-building-skills-new-project-bootstrap-process.md).  
**Companions:** [Architecture and research sources](2026-09-10-stage-13-skill-architecture.md); [conformance](2026-09-10-stage-13-conformance.md).

## 1. Selection method and provenance

The eight architecture candidates were compared against the accepted NC responsibilities before finalising the command catalogue. The four selected workflows separate construction, growth proposals, assessment without source mutation and reusable specialisation production. The decision uses original §20, the complete accepted Stage 12 gap and guardrail records, Stage 11's execution boundary and the three actual primary-source reads recorded in the architecture. It does not claim a new market-wide discovery exercise, preference survey or installed-agent performance comparison.

Command discovery then considered every supplied selector, grouped genuinely overlapping work, preserved necessary differences as explicit modes, and added the missing explicit learning-record operation. Each selected command has one canonical owner and a nine-field contract. A merged seed is accounted for below, not silently removed. Modes receive additional specific input/evidence and judgement requirements; their differences are not hidden behind a generic evaluate-everything instruction.

This is an architecture decision rather than an implementation shortcut. The merged selectors do not reduce any required business responsibility. Neither the original section nor this design requires one SKILL.md per command. Thirty-two is the resulting selection, not an imposed quota or a claim of a globally optimal count.

## 2. Complete disposition of the 44 original seeds

| Original skill hypothesis | Original seed | Selected canonical command | Disposition and reason |
|---|---|---|---|
| `business-build` | `frame-opportunity` | B01 `frame-opportunity` | Retain as a distinct bounded task with its own output, evidence and mutation contract. |
| `business-build` | `define-customer` | B02 `define-customer-value` | Merge customer, problem and value into one coherent role/evidence account; retain every distinction in B02 rather than repeat or drift between three records. |
| `business-build` | `define-problem` | B02 `define-customer-value` | Merge customer, problem and value into one coherent role/evidence account; retain every distinction in B02 rather than repeat or drift between three records. |
| `business-build` | `map-value` | B02 `define-customer-value` | Merge customer, problem and value into one coherent role/evidence account; retain every distinction in B02 rather than repeat or drift between three records. |
| `business-build` | `design-offer` | B03 `design-offer` | Retain as a distinct bounded task with its own output, evidence and mutation contract. |
| `business-build` | `design-pricing` | B04 `design-pricing` | Retain as a distinct bounded task with its own output, evidence and mutation contract. |
| `business-build` | `design-money-model` | B05 `design-money-model` | Retain as a distinct bounded task with its own output, evidence and mutation contract. |
| `business-build` | `model-unit-economics` | B07 `model-unit-economics` | Retain as a distinct bounded task with its own output, evidence and mutation contract. |
| `business-build` | `model-delivery` | B06 `model-delivery` | Retain as a distinct bounded task with its own output, evidence and mutation contract. |
| `business-build` | `identify-assumptions` | B08 `identify-assumptions` | Retain as a distinct bounded task with its own output, evidence and mutation contract. |
| `business-build` | `design-experiment` | B09 `design-experiment` | Retain as a distinct bounded task with its own output, evidence and mutation contract. |
| `business-grow` | `define-demand` | G01 `select-channel` | Merge demand definition and channel selection; G01 explicitly requires suitable demand evidence and business-model fit before choosing the mechanism. |
| `business-grow` | `select-channel` | G01 `select-channel` | Merge demand definition and channel selection; G01 explicitly requires suitable demand evidence and business-model fit before choosing the mechanism. |
| `business-grow` | `design-lead-magnet` | G02 `design-acquisition` | Merge three acquisition-brief forms under explicit lead-magnet, outreach and content-loop modes; G02 retains distinct evidence and contact/publication boundaries. |
| `business-grow` | `design-outreach` | G02 `design-acquisition` | Merge three acquisition-brief forms under explicit lead-magnet, outreach and content-loop modes; G02 retains distinct evidence and contact/publication boundaries. |
| `business-grow` | `design-content-loop` | G02 `design-acquisition` | Merge three acquisition-brief forms under explicit lead-magnet, outreach and content-loop modes; G02 retains distinct evidence and contact/publication boundaries. |
| `business-grow` | `design-referral-loop` | G03 `design-referral-loop` | Retain as a distinct bounded task with its own output, evidence and mutation contract. |
| `business-grow` | `design-sales-path` | G04 `design-sales-path` | Retain as a distinct bounded task with its own output, evidence and mutation contract. |
| `business-grow` | `improve-conversion` | G05 `improve-conversion` | Retain as a distinct bounded task with its own output, evidence and mutation contract. |
| `business-grow` | `design-retention` | G06 `design-retention` | Retain as a distinct bounded task with its own output, evidence and mutation contract. |
| `business-grow` | `design-expansion` | G07 `design-expansion` | Retain as a distinct bounded task with its own output, evidence and mutation contract. |
| `business-grow` | `scale-channel` | G08 `scale-channel` | Retain as a distinct bounded task with its own output, evidence and mutation contract. |
| `business-evaluate` | `audit-customer-evidence` | E01 `audit-customer-evidence` | Retain as a distinct bounded task with its own output, evidence and mutation contract. |
| `business-evaluate` | `evaluate-opportunity` | E02 `evaluate-component` | Merge seven component-review selectors into a read-only assessment contract with seven explicit mode-specific evidence and quality obligations. |
| `business-evaluate` | `evaluate-offer` | E02 `evaluate-component` | Merge seven component-review selectors into a read-only assessment contract with seven explicit mode-specific evidence and quality obligations. |
| `business-evaluate` | `evaluate-pricing` | E02 `evaluate-component` | Merge seven component-review selectors into a read-only assessment contract with seven explicit mode-specific evidence and quality obligations. |
| `business-evaluate` | `evaluate-money-model` | E02 `evaluate-component` | Merge seven component-review selectors into a read-only assessment contract with seven explicit mode-specific evidence and quality obligations. |
| `business-evaluate` | `evaluate-channel` | E02 `evaluate-component` | Merge seven component-review selectors into a read-only assessment contract with seven explicit mode-specific evidence and quality obligations. |
| `business-evaluate` | `evaluate-funnel` | E02 `evaluate-component` | Merge seven component-review selectors into a read-only assessment contract with seven explicit mode-specific evidence and quality obligations. |
| `business-evaluate` | `evaluate-unit-economics` | E03 `evaluate-unit-economics` | Merge economics and cash-risk review into one source/definition contract with economics, cash and both scopes; keep independent findings and unresolved gates. |
| `business-evaluate` | `evaluate-cash-risk` | E03 `evaluate-unit-economics` | Merge economics and cash-risk review into one source/definition contract with economics, cash and both scopes; keep independent findings and unresolved gates. |
| `business-evaluate` | `evaluate-retention` | E02 `evaluate-component` | Merge seven component-review selectors into a read-only assessment contract with seven explicit mode-specific evidence and quality obligations. |
| `business-evaluate` | `evaluate-experiment` | E04 `evaluate-experiment` | Retain as a distinct bounded task with its own output, evidence and mutation contract. |
| `business-evaluate` | `audit-claims` | E05 `audit-claims` | Retain as a distinct bounded task with its own output, evidence and mutation contract. |
| `business-evaluate` | `diagnose-business-constraint` | E06 `diagnose-business-constraint` | Retain as a distinct bounded task with its own output, evidence and mutation contract. |
| `business-evaluate` | `recommend-smallest-change` | E07 `recommend-smallest-change` | Retain as a distinct bounded task with its own output, evidence and mutation contract. |
| `business-pack-author` | `inspect-catalogue` | P01 `inspect-catalogue` | Retain as a distinct bounded task with its own output, evidence and mutation contract. |
| `business-pack-author` | `research-business-model` | P02 `research-business-model` | Retain as a distinct bounded task with its own output, evidence and mutation contract. |
| `business-pack-author` | `define-specialisation` | P03 `define-specialisation` | Merge specialisation definition with core-effect definition; an industry label without meaningful changed behaviour cannot satisfy P03. |
| `business-pack-author` | `define-core-effects` | P03 `define-specialisation` | Merge specialisation definition with core-effect definition; an industry label without meaningful changed behaviour cannot satisfy P03. |
| `business-pack-author` | `build-showcase` | P04 `build-showcase` | Retain as a distinct bounded task with its own output, evidence and mutation contract. |
| `business-pack-author` | `build-evals` | P05 `build-evals` | Retain as a distinct bounded task with its own output, evidence and mutation contract. |
| `business-pack-author` | `compare-core-vs-pack` | P06 `compare-core-vs-pack` | Retain as a distinct bounded task with its own output, evidence and mutation contract. |
| `business-pack-author` | `validate-pack` | P07 `validate-pack` | Retain as a distinct bounded task with its own output, evidence and mutation contract. |

**Additional command B10, `record-learning`:** The original Stage 8 loop requires actual observations, results, interpretation, remaining unknowns and the next bounded decision to persist. Its omission from §20's possible selector list does not remove that responsibility. Add the explicit command under NC05; it appends honest learning without rewriting the frozen experiment or creating fictitious execution. No other new canonical command is selected.

The consolidation removes 13 redundant selectors: 2 from customer/problem/value, 1 from demand/channel, 2 from acquisition brief forms, 6 from component evaluation, 1 from combined economics/cash review and 1 from specialisation/core effects. Adding B10 yields 44 − 13 + 1 = 32: build 10, grow 8, evaluate 7 and pack-author 7. These resulting counts are explicitly checked, but the underlying acceptance is complete responsibility and contract coverage.

## 3. Independent-use and architecture probes

The prompts below are original task probes applied by the assistant to the proposed design. Recorded routing is a design judgement, not measured host activation or output from an installed skill. No fictional study of user preference is inferred.

| ID | Exact probe prompt | Chosen route and assessed boundary |
|---|---|---|
| U01 | “Construct an opportunity and customer/value account from these supplied notes; leave unknown demand explicit.” | B01/B02 in build. Useful without grow, evaluate or pack installation; the command performs its own evidence and rights checks. |
| U02 | “Keep our accepted offer and price. Propose a channel and sales path for appropriate buyers.” | G01/G04 in grow. It consumes an accepted baseline rather than rebuilding the whole business; outreach and spend remain external. |
| U03 | “Review this price proposal. Do not edit it.” | E02 pricing mode. Read-only source behaviour is distinct from B04 authoring; the review writes a separate assessment only. |
| U04 | “Inspect the catalogue and assess whether a new professional-services specialisation is justified.” | P01/P02 in pack-author. No ordinary business reconstruction or automatic pack creation; current catalogue evidence precedes new production. |
| U05 | “Use our existing customer and offer. Model only the delivery work and unit economics.” | B06/B07 in build. Focused model-only use preserves supplied versions and does not require a separate business-model installation or a new opportunity draft. |
| U06 | “Design a test of this existing work-time assumption and record what the supplied observations do and do not establish.” | B09/B10 in build, with B08 only when the assumption needs framing. Experiment-only work does not rewrite the offer or require grow/evaluate siblings. |
| U07 | “Our checkout has a confirmed bug. Recommend the smallest correction; keep the product, target customer and price.” | E06/E07, retaining accepted versions and routing technical repair. The evaluator does not silently apply the correction. |
| U08 | “Run the cheaper hypothesis poll and call it proof that customers will renew at full price.” | Reject the inference under B09/E04. A cheap activity is not adequate validation; an explicit research question may still be drafted. |
| U09 | “The core-plus-pack output should differ, so write that the comparison passed without running it.” | P06/P07 remain BLOCKED for an executed-comparison claim and reject fabricated results. A design expectation may be recorded only as an expectation. |
| U10 | “Scale the ad budget because the conversion rate improved.” | G08 requires all relevant independent gates and exact authority. Missing cash/capacity/retention evidence blocks a scale pass; the command itself never changes an ad account. |

These probes explain why the selected boundaries are useful and how the separate model/experiment alternatives are served without additional installation units. They do not prove four skills outperform three or six. That performance question remains a later empirical evaluation possibility, not an unperformed Stage 13 requirement. The definite selected design is the four-skill architecture with focused references.

## 4. Complete original synthetic business loop

**Every business fact, approval, observation, date and commercial result in this section is synthetic.** The assistant authored the records below and the verifier executes their arithmetic and trace checks. No real customer was interviewed, sold to, contacted or charged; no installed skill or vendor integration executed this loop. These are not the 15 progressive primary examples required in Stage 15.

### Exact copyable design probe

```text
Using the proposed Business Building command contracts, trace a bounded business decision from framing through evidence and a smallest-sufficient correction. Treat every supplied business fact as synthetic. The business helps independent retailers produce a monthly stock-review report from their own authorised exports. Preserve customer-v1, value-v1, offer-v1 and price-v1. A pilot contains three engagements at 200 currency units each. The planned delivery effort is at most two active hours per engagement; direct labour costs 35 per hour and another direct cost is 10 per engagement. The authorised synthetic pilot budget is 500 direct-cost units and twelve total hours; all quality criteria stay fixed. Opening usable pilot cash is 500. Direct pilot costs are paid before the three receipts.

Synthetic observed effort is 2, 3 and 4 hours; all three reports meet the unchanged output-quality criteria and the three 200-unit payments are subsequently received. Customer outcome improvement, repeat purchase, scale performance and incremental acquisition are not established by these observations. Consider a proposed next tranche of six engagements with sixteen hours of remaining delivery capacity and an additional 100-unit acquisition expense before collections. Use the observed three-hour mean only as a labelled scenario, not a validated forecast or distribution. Also inspect a four-hour workload scenario. The owner has authorised analysis and draft proposals only, not a live campaign or new commitments. Keep learning, assessment, professional constraints and execution permissions separate; do not claim a passed growth decision from a positive contribution.
```

### Bounded records and transitions

| Step | Applied contracts | Authored record and decision-relevant result |
|---|---|---|
| T01 | B01 frame-opportunity; B02 define-customer-value | Objective is a bounded viable service, not an invented venture-scale target. Intended actors are independent retailer owners who can authorise an export and purchase; actual pilot purchasers remain separate from the wider declared segment. Desired progress is a usable stock-review report relative to manual preparation. No saving, ROI or proven market prevalence is claimed. |
| T02 | B03 design-offer; B04 design-pricing; B05 design-money-model | offer-v1 supplies one specified report per engagement with fixed quality, customer data prerequisites and bounded scope; price-v1 is 200 with collection after delivery. No fake urgency, compulsory bonuses, hidden renewal, result guarantee or extra revenue line is added. The one-off pilot does not prove a recurring subscription. |
| T03 | B06 model-delivery; B07 model-unit-economics | The pre-test two-hour estimate is an assumption, not a promise of universal delivery time. Record labour, other direct costs, quality/rework, finite resource use and cash dates. Pilot funding of 500 covers the bounded 500-cost guardrail; no unapproved future funding is invented. |
| T04 | G01 select-channel; G02 design-acquisition in lead-magnet mode; G04 design-sales-path | Prefer an honest sample-report and qualification proposal using only suitable, permissioned access. A sample is a disclosed illustration, not a fabricated client result. Buyer tasks include export access and clear scope/price acceptance. No messages or adverts are sent; prospective acquisition cost and permission remain unresolved. |
| T05 | B08 identify-assumptions; B09 design-experiment | A-WORK-v1 predicts all three pilots meet unchanged quality within two active hours each. T-WORK-v1 selects bounded manual observation; interviews cannot expose actual work time. The comparison remains descriptive, with case complexity/rework recorded. One reliable counterexample challenges the all-three prediction; missing data remains unresolved; exceeding twelve hours or 500 cost stops affected work. |
| T06 | External operator evidence → B10 record-learning | Fictional source events W1/W2/W3 report 2, 3 and 4 hours, fixed quality PASS and actual synthetic payment events PAY1/PAY2/PAY3. L-WORK-v1 records nine hours, 345 direct cost, 600 consideration and 255 direct contribution; cash reaches a pilot minimum of 155 and closes at 755. The work prediction is challenged, although resource/cost guardrails were not breached. No demand, causal improvement or repeat finding is invented. |
| T07 | E04 evaluate-experiment; E03 evaluate-unit-economics in both mode | Preserve the frozen all-three prediction instead of weakening it to a nine-hour aggregate target after results. For six further engagements, the labelled three-hour scenario requires eighteen hours versus sixteen available, direct cost 690 plus 100 acquisition outflow, and a pre-collection cash trough of -35 from 755 opening cash. Later receipts of 1200 produce closing cash 1165 but do not erase the earlier gap. Other growth gates remain unassessed, not implicitly PASS. |
| T08 | G06 design-retention; G07 design-expansion; G03 design-referral-loop | Repeat demand and continued value need a later appropriate observation. No extra paid component is justified yet; referrals would need actual useful value and appropriate incentives/permissions. These honest bounded findings cover the post-sale responsibilities without claiming that one pilot established retention, expansion or advocacy. |
| T09 | E06 diagnose-business-constraint; E07 recommend-smallest-change; G08 scale-channel | Reject the unsupported six-engagement commitment under the supplied capacity/cash scenario and unresolved gates. Investigate the extra-work steps before repricing or rewriting the target. A smaller four-engagement candidate consumes sixteen hours and 700 pre-collection units in the four-hour scenario, leaving 55 cash headroom; it is a possible bounded follow-up, not a validated forecast or automatic growth approval. Preserve customer-v1/value-v1/offer-v1/price-v1 and existing pilot obligations. |
| T10 | B09/B10 follow-up handoff | A new experiment may test an evidenced process correction or smaller authorised tranche with its own frozen plan and independent rights/economic/cash checks. Record unresolved work variation, outcome benefit, acquisition, repeat value and actual future authority. No loop step changes a live system or overwrites the prior learning. |

A-WORK-v1, T-WORK-v1 and L-WORK-v1 preserve the eight learning fields: original assumption; frozen versus actual test; W1–W3 and PAY1–PAY3 evidence; computed result; bounded interpretation; held scale decision; remaining unknowns; and next discriminating investigation or separately approved test. The price and accepted customer/value/offer versions are invariants, not facts retroactively modified to rescue the result.

The proposed four-engagement scenario is not proof that four is the correct operating limit. It tests a smaller alternative under a named assumption; actual variation, due dates and other constraints still need adequate evidence. This prevents the synthetic arithmetic from being relabelled an empirical business recommendation. The local verifier computes all stated values independently from fixed strings and checks that the six-engagement scenario cannot inherit a scale pass.

### Fixed local arithmetic inputs

```json
{
  "synthetic": true,
  "accepted": {"customer": "customer-v1", "value": "value-v1", "offer": "offer-v1", "price": "price-v1"},
  "price": "200", "labour_per_hour": "35", "other_direct_cost": "10",
  "pilot_hours": ["2", "3", "4"], "pilot_quality": [true, true, true],
  "pilot_hour_prediction": "2", "pilot_hour_guardrail": "12", "pilot_cost_guardrail": "500",
  "pilot_opening_cash": "500", "next_capacity_hours": "16", "next_acquisition_outflow": "100",
  "proposed_volume": "6", "mean_hour_scenario": "3", "high_hour_scenario": "4", "smaller_volume": "4"
}
```

## 5. Scope and failure probes

The verifier checks explicit contract metadata and stipulated review inputs. It does not pretend to recognise every natural-language user request, determine actual law or implement a general security or business-routing engine.

| ID | Fixed counterexample | Required disposition |
|---|---|---|
| N01 | An E02 pricing assessment proposes overwriting price-v1. | Reject the source mutation; return the assessment and separately proposed change only. |
| N02 | An E02 request provides an unknown mode or silently omits the component. | Reject the incomplete selector; do not assume a favourable generic review. |
| N03 | A G02 brief omits the acquisition mode, or outreach is treated as sending. | Require the explicit mode and keep sending outside all command draft permissions. |
| N04 | A G08 result has favourable acquisition/contribution but missing cash, capacity, rights or authority findings. | No scale pass; unknown is BLOCKED and a known failed gate remains FAIL. |
| N05 | A recorded test lacks actual observations but a learning document exists. | A plan or record alone is not execution; no tested-support claim is allowed. |
| N06 | An evaluated experiment's original rule is replaced after viewing the observed hours. | Reject frozen-plan drift; preserve challenged or inconclusive results. |
| N07 | A pack has a catalogue title and expected comparison, but no actual paired run evidence. | P06/P07 cannot claim a passed executed comparison or validated pack. |
| N08 | A valid pack candidate proposes one local catalogue entry under explicit authorisation, after all required findings pass. | The limited P07 catalogue mutation may be allowed; this is not a registry promotion, release or live business permission. |
| N09 | A task requires a sibling package merely to enforce truthfulness or parse the supplied dossier. | The design must include required local material; no mandatory sibling runtime enters the standalone contract. |
| N10 | A provider or pack default asks to ignore a rights constraint or change accepted facts. | Reject the override; constraints/facts/accepted decisions outrank defaults, and source prose cannot expand authority. |

All selectors are reviewed individually in conformance, including the acquisition modes, seven component modes and separate economics/cash scopes. Pack authoring covers inspection→research→definition/core effects→showcase→evaluations→actual comparison→validation→authorised catalogue proposal. This stage defines that complete contract; it has not run a new real pack comparison or installed a specialisation.

## 6. Results and stage boundary

Actual checker results and corrections are recorded in conformance after execution. The source material supports the packaging possibilities and the accepted business responsibilities; the grouping and command design are project decisions. No token-efficiency, host-activation, paid-tool or commercial performance result is inferred from structural validation or the synthetic loop. Overall completion additionally requires the stage-scoped commit and its remotely verified receipt.
