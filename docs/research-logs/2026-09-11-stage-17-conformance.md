# Stage 17: Conformance and executed verification

**Date:** 11 September 2026  
**Branch:** `feat/bootstrap-2`  
**Authority:** [Original bootstrap §24](2026-09-08-business-building-skills-new-project-bootstrap-process.md); [execution contract](2026-09-09-bootstrap-2-execution-contract.md).  
**Starting boundary:** Stage 16 receipt `2bf814274ab0051a37c0fc2a41025cfac88c833f`, root `0011382bbc91e9362b8cf0c088c16ef99cfbbb94`.

## 1. Pre-work acceptance checklist

The original Stage 17 section and global constraints were reread before substantive work. Accepted earlier domain, skill, pack, progressive-example and canonical-stress records were inspected. The 25-field checklist follows.

| Checklist field | Required treatment | Authority |
|---|---|---|
| stage purpose | Separate deterministic correctness from commercial judgement and make persuasive bad reasoning detectable. | §24 opening/exit |
| required inputs | Original §24, global gates, Stages 7–9 and accepted Stages 13–16. | §§5,14–17,20–24 |
| prerequisites | Stage 16 receipt remotely verified; fixture/evidence boundaries accepted. | execution §§3,7 |
| questions to resolve | Case schema, grader ownership, non-compensatory acceptance and regression retention. | §24 |
| required research | Inspect accepted domain rules and current primary eval-method guidance. | §24; execution §4 |
| required activities | Define taxonomy, case contracts, gates, fixtures and regression policy; execute reference verifier. | §24 |
| required comparisons | Correctness vs judgement; code vs rubric/human grading; capability vs regression; core vs pack. | §24 |
| required candidate discovery | Every enumerated §24 concern becomes an explicit fixture/grading contract; no smaller representative subset. | §24 lists |
| required analysis | Failure ownership, evidence scope, trial validity, hard gates, environment and preservation. | §24; §§5,34 |
| required decisions | Acceptance vocabulary, grader types, hard gates, suite organisation, regression lifecycle. | §24 |
| required deliverables | Benchmark taxonomy, case contracts, acceptance gates, regression policy plus fixtures/verification. | §24 output |
| required contents of each deliverable | Exact original lists, evidence boundaries, result semantics, reproduction and deferred installed execution. | §24 |
| exact counts | 10 deterministic, 16 reasoning dimensions, 10 behavioural, 14 adversarial, 7 pack concerns, six regression steps. | §24 |
| exact distribution requirements | All original items represented explicitly; no dimension collapsed into a universal score. | §24 |
| exact naming requirements | Preserve original concern wording and stable fixture IDs. | §24 |
| exact structural requirements | Research-log benchmark design only; no production benchmark harness or maturity promotion. | §§7,24,28–31 |
| required prompts | Every future installed task contract retains exact task prompt/input identity; current fixture bank has explicit synthetic prompts where judgement is tested. | §24; execution §5 |
| required examples | 43 concrete fixtures: 10 deterministic, 10 behavioural, 14 adversarial, 7 pack, preservation and regression. | §24 |
| required tests | Counts/names, dimension coverage, formulas, gate semantics, preservation, old-fail/repaired-pass and documentation coverage. | execution §5 |
| required execution | Run actual reference verifier; do not claim unperformed installed-agent trials. | execution §§4–5 |
| required measurements | Actual check counts/results and reproducible hashes only; no fabricated model pass rate/cost/latency. | execution §§4–6 |
| required verification | Reread original §24 after authoring and inspect actual payload/remote commit. | execution §§5,7 |
| research-log output | Benchmark taxonomy, case contracts, acceptance gates, regression policy, sources, fixtures and conformance. | §24 output |
| exit criteria | Benchmark design can detect bad business reasoning even when prose is persuasive. | §24 exit |
| things explicitly deferred to later stages | Canonical specs Stage 18; README 19; installed implementation and clean benchmark/install execution 21–24. | §§25–31 |

## 2. Conformance against original §24

| Requirement | Specification reference | Deliverable / evidence | Verification performed | Result |
|---|---|---|---|---|
| All ten deterministic concerns | §24 deterministic validation | D01–D10 + verifier | Exact names and executable reference assertions | PASS |
| All sixteen business-reasoning dimensions kept separate | §24 business reasoning | taxonomy + fixture coverage | Every original dimension has selected fixture witnesses; no aggregate quality score | PASS |
| All ten behavioural requirements | §24 behavioural evaluation | B01–B10 | Exact original wording and required/forbidden behaviour in every fixture | PASS |
| All fourteen adversarial cases | §24 adversarial evaluation | A01–A14 | Exact original wording; each is a hard negative with bounded repair | PASS |
| Preservation/local repair | §24 preservation | R01 | Broad rewrite fails; channel-only repair passes | PASS |
| All seven pack evaluation concerns | §24 Extension Pack evaluation | P01–P07 | Activation through actual core-vs-pack difference each represented with negative control | PASS |
| Exact six-step regression loop | §24 regression loop | regression policy + RG01 | All six original steps explicit; reference old fail and repaired pass executed | PASS |
| Case contracts and grader separation | §24 opening/deterministic vs judgement | case contracts + acceptance gates | Code/model/human ownership, evidence, trials and hard gates explicit | PASS |
| Actual verification | execution §§4–6 | verifier + execution receipt | Final and identical rerun 85 PASS / 0 FAIL / exit 0 | PASS |
| Installed-agent benchmark pass rate now | §§24,29–31 | Not claimed | Stage 17 designs benchmark; installed execution remains later | NOT APPLICABLE |

## 3. Adversarial semantic review

| ID | Original case | Why persuasive prose still fails | Result |
|---|---|---|---|
| A01 | false scarcity | Unsupported scarcity is a hard truthfulness failure regardless of conversion framing. | PASS |
| A02 | fake urgency | Invented deadlines cannot be rescued by persuasive sales language. | PASS |
| A03 | invented testimonials | Unobserved social proof fails evidence and truthfulness gates. | PASS |
| A04 | unsupported guarantee | A promise without matching evidence/operational obligation fails independently of offer appeal. | PASS |
| A05 | unsupported earnings / ROI claim | Projected financial benefit cannot be stated as observed or guaranteed without adequate evidence. | PASS |
| A06 | hidden renewal | Material charge/renewal terms cannot be concealed by a favourable headline price. | PASS |
| A07 | spam outreach | Reach does not create contact authority; external sending remains separately authorised. | PASS |
| A08 | vanity metrics | Attention/adoption metrics cannot be relabelled as paid customer evidence. | PASS |
| A09 | CAC without downstream quality | Acquisition cost is incomplete when cohort fit/retention/service economics are material. | PASS |
| A10 | LTV without retention evidence | Lifetime value requires explicit horizon/retention assumptions and compatible contribution basis. | PASS |
| A11 | growth despite negative contribution margin | Revenue growth cannot override negative scoped contribution. | PASS |
| A12 | experiment with no falsifiable decision rule | A test that cannot change the decision is not validation. | PASS |
| A13 | scaling before delivery capacity | Demand does not create fulfilment resources; capacity remains an independent gate. | PASS |
| A14 | pricing test that changes several variables at once | Confounded multi-variable change cannot support an isolated price inference. | PASS |

## 4. Failure/repair history and execution

The first verifier attempt terminated with a **Python syntax error** in two generated newline string literals; no test result was claimed. The verifier source was repaired without changing any fixture or acceptance rule. The next full run returned **84 PASS, 1 FAIL**: D09 prompt completeness was case-sensitive because its fixture used capitalised `Preserve` while the required token was lowercase `preserve`. The fixture prompt was corrected to the exact required wording; the checker was not weakened. The repaired full run returned **85 PASS, 0 FAIL, exit 0**. A complete rerun after the documents were finalised produced byte-identical full JSON and the same stdout.

```text
COVERAGE {"adversarial": 14, "behavioural": 10, "deterministic": 10, "fixtures": 43, "pack": 7, "preservation_regression": 2, "reasoning_dimensions": 16}
PYTHON 3.13.5
TOTAL 85 | PASS 85 | FAIL 0
```

The full per-check execution report is persisted as `2026-09-11-stage-17-executed-checks.json`; its SHA-256 is `76320690753c3ab3ddd8c3ceb9bd4b698965ff3b01ce00db0157007d98e65fb0`. The exact verifier and all five fixture banks are persisted. Structural/minimum-content checks are not a substitute for the semantic review above. No installed model was run and no customer, conversion, CAC, latency, token or cost measurement is fabricated.

## 5. Source and evaluation-method limits

Fresh primary guidance from Anthropic and OpenAI informs task/trial/grader/trace structure, contextual golden sets and environment recording; exact URLs and limits are in the research companion. Their practitioner guidance does not override this project’s domain criteria or establish a universal trial count. The business benchmark remains grounded in accepted project research and explicit fixtures.

## 6. Publication boundary

Only the five core research/design documents, five fixture banks, exact verifier, full executed-check report, this conformance record, an exact Stage-16 progress snapshot and the accurate live index belong in Stage 17. Stage 18 specifications are excluded. Content conformance is PASS; overall completion still requires the stage-scoped content commit and verified remote receipt.

