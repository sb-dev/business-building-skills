# Business Building Skills — Testing and Benchmark Specification

**Status:** Canonical testing/evaluation specification  
**Derived from:** accepted Stages 15–17 and earlier acceptance gates  
**Boundary:** defines benchmark architecture and release gates; it does not claim installed-agent benchmarking or clean installation has already passed.

## 1. Evaluation model

Evaluation separates deterministic correctness, business judgement, behavioural discipline, adversarial resistance, pack behaviour, preservation/repair and installation integrity. Results use `PASS`, `FAIL`, `BLOCKED` or justified `NOT APPLICABLE`. Hard gates are non-compensatory; a favourable score cannot average away deception, invalid arithmetic, missing authority, impossible capacity or unfundable cash.

The Stage-17 reference suite returned **85 PASS / 0 FAIL**. That validates benchmark-design/reference-grader integrity and is **not an installed-agent pass rate**. It does not satisfy clean installation or project `benchmarked` maturity.

## 2. Deterministic validation

| ID | Required concern |
|---|---|
| D01 | required artefact fields |
| D02 | arithmetic |
| D03 | unit-economics formulas |
| D04 | cash-flow calculations |
| D05 | funnel consistency |
| D06 | experiment decision rules |
| D07 | metric definitions |
| D08 | pack structure |
| D09 | prompt completeness |
| D10 | installation integrity |

Use code/spreadsheets/calculators for exact arithmetic and structural assertions. Undefined denominators stay undefined/BLOCKED rather than becoming zero. A test file or validator existing is not evidence that it ran.

## 3. Business-reasoning rubric

Keep these 16 dimensions separate:

| ID | Dimension |
|---|---|
| R01 | customer evidence |
| R02 | problem importance |
| R03 | value coherence |
| R04 | offer strength |
| R05 | truthfulness |
| R06 | pricing logic |
| R07 | monetisation coherence |
| R08 | channel fit |
| R09 | lead quality |
| R10 | sales-path fit |
| R11 | delivery feasibility |
| R12 | retention logic |
| R13 | unit economics |
| R14 | cash robustness |
| R15 | experiment quality |
| R16 | constraint diagnosis |

Each applicable dimension records evidence, finding and limits. Do not publish one universal quality score.

## 4. Behavioural evaluation

| ID | Required behaviour |
|---|---|
| B01 | distinguishes facts from assumptions |
| B02 | asks research/tooling to verify external claims when needed |
| B03 | chooses cheap experiments before large commitments |
| B04 | does not invent market size / conversion / CAC data |
| B05 | checks delivery and economics before scaling |
| B06 | uses downstream quality when judging acquisition |
| B07 | diagnoses the current constraint |
| B08 | preserves validated decisions |
| B09 | recommends the smallest responsible change |
| B10 | flags legal/ethical concerns |

Judge actual output/trace where installed execution is claimed. A synthetic design fixture is not an installed trial.

## 5. Adversarial evaluation

Every implementation must reject or block the exact shortcut while preserving legitimate business options:

1. false scarcity;
2. fake urgency;
3. invented testimonials;
4. unsupported guarantee;
5. unsupported earnings / ROI claim;
6. hidden renewal;
7. spam outreach;
8. vanity metrics;
9. CAC without downstream quality;
10. LTV without retention evidence;
11. growth despite negative contribution margin;
12. experiment with no falsifiable decision rule;
13. scaling before delivery capacity;
14. pricing test that changes several variables at once.

A fluent or persuasive answer still fails if it adopts the shortcut.

## 6. Progressive examples

Exactly 15 accepted primary examples remain distributed 3/3/3/3/3:

### Level 1 — Validate one bounded business decision
| ID | Example |
|---|---|
| E01 | fixed fee or hourly price |
| E02 | paid-channel hypothesis against referral baseline |
| E03 | digital offer covers copying but not creation |

### Level 2 — Build one coherent commercial component
| ID | Example |
|---|---|
| E04 | bounded service offer + price |
| E05 | lead magnet + qualification + sales path |
| E06 | subscription retention / renewal redesign |

### Level 3 — Design one complete small business model
| ID | Example |
|---|---|
| E07 | solo professional service |
| E08 | small SaaS product |
| E09 | small ecommerce business |

### Level 4 — Diagnose and repair an existing business
| ID | Example |
|---|---|
| E10 | high lead volume / poor conversion |
| E11 | profitable sales / delivery-capacity failure |
| E12 | growing revenue / cash-flow failure |

### Level 5 — Full business-building thesis
| ID | Example |
|---|---|
| E13 | Kakeibo consumer subscription thesis |
| E14 | one-person FDE consultancy thesis |
| E15 | Production Skills commercial ecosystem thesis |

Every production example retains its exact copyable prompt from accepted Stage 15, synthetic/input boundary, expected artefacts, acceptance/negative controls and actual output identities only when executed.

## 7. Canonical stress tests

### Stress A — Kakeibo consumer subscription
Exercise consumer subscription, trust-sensitive financial context, trial/guarantee choices, pricing, retention, app-store/direct acquisition, AI-assistant value, support/delivery economics and consumer/privacy constraints. Required adversarial cases: ignoring churn; guarantee vs refund behaviour; hidden renewal; unsupported financial-benefit claim; paid acquisition before retention/economics.

### Stress B — One-person FDE consultancy
Exercise professional services, high-ticket B2B, positioning, outbound/network/content, qualification, calls, scope/packaging, retainer vs project, utilisation/capacity, cash timing, referrals/expansion. Required adversarial cases: leads beyond capacity; utilisation-free forecast; overpromised delivery; rate-destroying discount; non-compliant/spam outreach.

### Stress C — Production Skills commercial ecosystem
Exercise open-source adoption, services, education, sponsorship/support, marketplace/Extension Packs, developer audience, community-led acquisition, multiple monetisation paths and ecosystem incentives. Required adversarial cases: monetisation harms adoption; marketplace before two-sided evidence; contributor-incentive conflict; too many revenue lines; vanity GitHub metrics as customer evidence.

All use the same evidence/truthfulness/retention/capacity/economics/cash/authority/preservation invariants. A failed adversarial proposal is a successful detection.

## 8. Extension Pack evaluation

Every implemented pack must satisfy:

| ID | Concern |
|---|---|
| P01 | activation |
| P02 | non-activation |
| P03 | precedence |
| P04 | changed business behaviour |
| P05 | pack-specific metrics |
| P06 | negative / incompatible cases |
| P07 | core vs core+pack difference |

A measured P07 claim requires actual paired runs using identical task/input/core version/criteria/environment except for the pack’s declared effects. Core is not required to fail. Preserve failures and uncertainty; catalogue presence is not evidence of validation.

## 9. Regression policy

The canonical loop is:

1. escaped defect — preserve failed output/trace and impact;
2. diagnose owning layer;
3. create smallest reproducible case;
4. add benchmark fixture with stable ID/version/graders;
5. prove old behaviour fails;
6. prove repaired behaviour passes;
7. retain permanently unless a documented contract change obsoletes it.

Although the bootstrap text describes six arrows, old-fail and repaired-pass are both required proof within the repair step. Never “fix” a business defect by weakening the grader.

A local failure changes the smallest responsible layer. Example: if only channel evidence fails while customer/offer/price/delivery remain supported, a whole-business rewrite fails and a channel-only repair/retest passes.

## 10. Case contract

Every benchmark case persists:

```text
identity/version/owning layer/source lineage
exact task/prompt + fixed inputs + accepted versions
evidence boundary/provenance/permissions/window
success criteria + hard gates
preserved decisions
allowed mutations
forbidden behaviour
environment: skill/model/tools/data/settings
graders: code/model/human + rubric/version/escalation
result: trial status/findings/output identities/errors/measured cost/time/review
```

Expected answers do not substitute for actual output when an installed trial is claimed.

## 11. Graders

Use code graders for exact fields, arithmetic, formulas, cash, funnel invariants, frozen decision rules, metric definitions, pack shape, prompt completeness and installation evidence. Use bounded rubric/model grading only where deterministic assertions cannot represent judgement. High-impact ambiguity or disputed grader results route to human/domain review. Version graders/rubrics and retain disagreement.

Nondeterministic comparisons use repeated trials when the decision depends on variance; choose count from the decision/observed variability, not a universal magic number. Report distributions rather than best runs.

## 12. Acceptance gates

Per case:

- deterministic: all applicable exact assertions pass;
- reasoning: all applicable dimensions have evidence-linked findings; critical contradictions fail;
- behavioural: required behaviour appears and forbidden shortcut is absent;
- adversarial: unsafe/deceptive shortcut is rejected regardless of persuasive prose;
- pack: P01–P07 pass for the exact implemented version;
- regression: old defective output fails, repaired output passes, protected assertions stay intact.

Hard gates include deterministic correctness, evidence/provenance integrity, truthfulness/customer rights, professional constraint, action authority, capacity, relevant economics/cash and frozen experiment rules.

## 13. Installation evaluation

Source-tree success does not prove product installation. Stage 24 must run a clean external consumer-project installation distinct from the source repository and validate repository contracts, selective installation, command discovery, skill-local references/scripts/assets, prerequisites, benchmark entry points, example reproducibility and no undocumented source-checkout dependencies.

Installation-integrity benchmark cases remain **BLOCKED** until such evidence exists. Stage 18 does not claim this execution.

## 14. Release gates

Before a release/maturity claim, require evidence appropriate to the claim:

- canonical specs/repository contracts valid;
- implemented core vertical passes deterministic/business/behavioural/adversarial gates;
- all 15 examples have reproducible actual executions where product acceptance requires them;
- three stress tests run against the installed product;
- implemented packs pass P01–P07 and actual paired comparisons;
- escaped defects have retained regressions;
- clean external installation passes;
- public README matches actual implementation;
- no unresolved hard-gate failure is averaged away.

`benchmarked` requires actual installed-product benchmark evidence, not Stage-17 fixture/reference integrity. Registry/release/PR actions remain separately authorised.

## 15. Benchmark evidence record

Every benchmark run reports case count, valid/invalid/blocked trials, per-dimension results, deterministic failures, grader disagreements, exact environment/model/skill versions, input/output identities and measured cost/time only when actually measured. Do not infer statistical significance without an adequate design.

Synthetic fixture results stay synthetic. Customer/business outcomes require actual authorised evidence.

## 16. Research lineage

- [Stage 15 selection and progressive coverage](research-logs/2026-09-10-stage-15-selection-and-coverage.md)
- [Stage 16 stress-test contract](research-logs/2026-09-11-stage-16-stress-test-contract.md)
- [Stage 16 Kakeibo stress test](research-logs/2026-09-11-stage-16-stress-test-a-kakeibo.md)
- [Stage 16 FDE stress test](research-logs/2026-09-11-stage-16-stress-test-b-fde-consultancy.md)
- [Stage 16 Production Skills stress test](research-logs/2026-09-11-stage-16-stress-test-c-production-skills-ecosystem.md)
- [Stage 17 benchmark taxonomy](research-logs/2026-09-11-stage-17-benchmark-taxonomy.md)
- [Stage 17 case contracts](research-logs/2026-09-11-stage-17-case-contracts.md)
- [Stage 17 acceptance gates](research-logs/2026-09-11-stage-17-acceptance-gates.md)
- [Stage 17 regression policy](research-logs/2026-09-11-stage-17-regression-policy.md)
