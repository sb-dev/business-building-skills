# Stage 17: Evaluation case contracts

## 1. Canonical task record

Every benchmark case must persist these fields:

| Field | Contract |
|---|---|
| identity | Stable case ID, version, owning layer, source/defect lineage and suite membership. |
| task | Exact copyable prompt plus fixed input artefacts and accepted business versions. |
| evidence boundary | Synthetic/observed/source-derived status, provenance, permissions, date/window and unresolved facts. |
| success criteria | Independent deterministic assertions, business-dimension findings, behavioural requirements and hard gates. |
| preserved decisions | Accepted versions/rights that must remain unchanged unless evidence implicates them. |
| allowed mutations | Exact files/state the trial may change; assessment-only cases remain read-only. |
| forbidden behaviour | Fabricated facts/results, hidden external effects, criterion weakening and unrelated redesign. |
| environment | Skill/model version, tools, data snapshot, runtime configuration and any nondeterminism controls. |
| graders | Code/model/human grader IDs, rubric versions, required evidence and escalation rule. |
| result | Trial status, per-grader findings, trace/output identities, errors, cost/time only if measured, and review decision. |

A case is not complete because it has an expected answer. When an installed trial is claimed, actual output/trace evidence must exist. Current Stage-17 fixture files are **case definitions and reference-grader checks**, not installed-agent trials.

## 2. Grader selection

Use code-based graders for exact fields, arithmetic, formulas, cash calendars, funnel invariants, decision-rule execution, metric definitions, pack shape, prompt completeness and installation evidence. Use rubric/model grading only for bounded natural-language judgement where deterministic assertions cannot capture adequacy. High-impact ambiguity, specialist conclusions or disputed grader results route to human/domain review. Calibrate model/human graders against stable exemplars and retain disagreements; do not silently tune a rubric to make a preferred candidate pass.

## 3. Trial protocol

A deterministic task can use one reproducible execution. Nondeterministic model behaviour requires repeated trials when the comparison decision depends on variance; the number is chosen from the decision and observed variability rather than a universal magic count. Compare models/prompts/skills only under compatible fixtures and environments. Keep attempted, failed, timed-out and invalid trials distinct from clean failures of business reasoning.

## 4. Failure ownership

Classify a failure before repair: fixture/spec defect, grader defect, tool/environment defect, evidence deficiency, business-reasoning defect, permission/professional block, or implementation defect. Repair the owning layer first. An evaluator defect must not be 'fixed' by changing the business answer; a business-reasoning defect must not be hidden by weakening a grader.

## 5. Fixture banks

The current Stage-17 bank contains 43 explicit fixtures: 10 deterministic, 10 behavioural, 14 adversarial, 7 pack, one preservation case and one regression case. Every original §24 list item has a direct fixture or grading contract. The verifier checks exact counts, names, required fields, dimension coverage and reference calculations.
