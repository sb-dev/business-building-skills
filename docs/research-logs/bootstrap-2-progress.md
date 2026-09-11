# Bootstrap 2 progress

**Repository:** `sb-dev/business-building-skills`  
**Working branch:** `feat/bootstrap-2`  
**Authority:** [Original bootstrap v1.1](2026-09-08-business-building-skills-new-project-bootstrap-process.md), blob `a0ac1b6c78a0cde8ccd9aca6fda6c5b0880c516d`; [execution contract](2026-09-09-bootstrap-2-execution-contract.md).

## Current boundary

Stages 1–17 are COMPLETE. Stage 17's benchmark design, fixture banks, executed reference-grader checks, content commit and remote identities have been verified. Stages 18–26 have not started. This remains a bootstrap research workspace, not an installed, benchmarked or mature product.

| Stage | Durable evidence | State |
|---|---|---|
| 0–16 | [Preserved progress and completion receipts](2026-09-11-bootstrap-2-progress-through-stage-16.md), including Stage 16 and earlier history | COMPLETE; Stage 0 is the workspace |
| 17 | [taxonomy](2026-09-11-stage-17-benchmark-taxonomy.md); [case contracts](2026-09-11-stage-17-case-contracts.md); [acceptance gates](2026-09-11-stage-17-acceptance-gates.md); [regression policy](2026-09-11-stage-17-regression-policy.md); [research](2026-09-11-stage-17-research-and-sources.md); five fixture banks; [conformance](2026-09-11-stage-17-conformance.md); [verifier](2026-09-11-stage-17-verifier.py); [execution receipt](2026-09-11-stage-17-executed-checks.json) | COMPLETE |
| 18–26 | No accepted outputs | NOT STARTED |

## Preserved state

The preceding live index is preserved byte-for-byte as `2026-09-11-bootstrap-2-progress-through-stage-16.md`, reusing blob `50b8a12e15c91de7c28b64fd420c720e06c3415f`. Stage 17 starts from verified Stage 16 receipt `2bf814274ab0051a37c0fc2a41025cfac88c833f`, root `0011382bbc91e9362b8cf0c088c16ef99cfbbb94`; its content parent is `5ba862bb1d025e6c471c31df190f42e650db6118`.

## Stage 17 content verification

All original §24 lists are represented literally: 10 deterministic validation concerns, 16 separate business-reasoning dimensions, 10 behavioural requirements, 14 adversarial cases, 7 Extension Pack evaluation concerns and the six-step regression loop. The bank contains 43 explicit synthetic fixtures: 10 deterministic, 10 behavioural, 14 adversarial, 7 pack, one preservation and one regression fixture.

Acceptance is non-compensatory: correctness, evidence integrity, truthfulness/rights, professional constraints, action authority, delivery/capacity, relevant economics/cash and frozen experiment rules cannot be averaged away. Business reasoning is reported as a dimension vector, never one universal quality score. Deterministic assertions use code graders; bounded judgement may use calibrated rubric/model or human review later, with grader/version/environment evidence retained.

The first verifier attempt had a syntax defect and produced no claimed result. After repair, one prompt-completeness fixture failed its exact token requirement; the prompt was corrected without weakening the checker. Final and repeated runs returned **85 PASS, 0 FAIL, exit 0** on Python 3.13.5 and byte-identical full JSON. The complete per-check execution report is persisted and reproducible from the exact verifier and fixture banks. No installed-agent pass rate, latency/token/cost, clean installation, customer outcome or benchmarked maturity is claimed.

The verified content commit contains the complete Stage 17 research/design files, five fixture banks, verifier/results, conformance, exact Stage-16 progress snapshot and this live index only. The pre-receipt live index remains in Git history at blob `377881df6cd3e1a406d85aa3cb6b020bb0dd2944`; its pending state is superseded by the receipt below.

## Stage 17 completion receipt

**Stage:** 17, Design Evals, Benchmarks and Regression Fixtures  
**Status:** COMPLETE  
**Content commit:** `62b0ba5032f33782cbe65c4aa99ab367ecb15149`  
**Message:** `docs: complete stage 17 eval benchmarks and regression fixtures`  
**Parent:** `2bf814274ab0051a37c0fc2a41025cfac88c833f`  
**Root tree:** `442f50285181645a8bf0bd7b6b89725edee43e49`  
**Verification date:** 11 September 2026  
**Remaining Stage 17 blockers:** none

| Requirement | Specification reference | Evidence | Verification performed | Result |
|---|---|---|---|---|
| Deterministic validation concerns | §24 deterministic validation | D01–D10 and exact verifier | All 10 names, formulas, boundary cases and BLOCKED installation evidence rule executed | PASS |
| Separate business-reasoning dimensions | §24 business reasoning | 16-dimension taxonomy and fixture witnesses | All 16 dimensions have explicit coverage; no universal score used | PASS |
| Behavioural evaluation | §24 behavioural evaluation | B01–B10 | All 10 original behaviours represented with required and forbidden behaviour | PASS |
| Adversarial evaluation | §24 adversarial evaluation | A01–A14 | All 14 original cases retained as hard failures with bounded repairs | PASS |
| Preservation and smallest responsible repair | §24 preservation and repair | R01 | Broad rewrite fails; channel-only repair passes while protected decisions remain intact | PASS |
| Extension Pack evaluation | §24 Extension Pack evaluation | P01–P07 | All 7 required concerns represented with negative controls and explicit evidence boundaries | PASS |
| Six-step regression loop | §24 regression loop | regression policy and RG01 | Exact loop documented; old defective output fails and repaired local output passes permanent fixture | PASS |
| Actual executable verification | execution §§4–6 | verifier and full executed-check report | Final and repeated runs: 85 PASS / 0 FAIL / exit 0 on Python 3.13.5; persisted JSON SHA-256 `76320690753c3ab3ddd8c3ceb9bd4b698965ff3b01ce00db0157007d98e65fb0` | PASS |
| Stage-scoped content commit | execution §7 | branch ref, commit and comparison | Exactly one commit ahead of Stage 16 receipt; 14 additions plus live progress modification only | PASS |
| Intended immutable identities | execution §7 | immutable file reads/tree | Stage 17 documents, five banks, verifier/results, conformance, snapshot and pre-receipt index resolve to intended blob identities | PASS |
| Honest maturity boundary | §§24,29–35 | taxonomy, gates and conformance | No installed-agent pass rate, clean-install pass, release, PR or `benchmarked` maturity claimed | PASS |

| Path under `docs/research-logs/` | Verified content blob |
|---|---|
| `2026-09-11-stage-17-benchmark-taxonomy.md` | `6c103033234518a42e23dbf6334d66b541bf8ce6` |
| `2026-09-11-stage-17-case-contracts.md` | `ff55c169a5c247bec25ea23c34e1bd0ffd8adbb4` |
| `2026-09-11-stage-17-acceptance-gates.md` | `1564dfe987773bc0146383d760100b502b56dfcb` |
| `2026-09-11-stage-17-regression-policy.md` | `90e2db5f5d3b3501783a78e1a96bdf8f1516e366` |
| `2026-09-11-stage-17-research-and-sources.md` | `66d6a793c9b336d6bcd597aa127164c8ce1a0c32` |
| `2026-09-11-stage-17-deterministic-fixtures.json` | `941cdbaab35a5c4efc192fbff0d06528e6e5015a` |
| `2026-09-11-stage-17-behavioural-fixtures.json` | `137db9d8c2089d52516c12044f823c35dd3b76f4` |
| `2026-09-11-stage-17-adversarial-fixtures.json` | `3224520e09b1058c8aced95ee4ba34d065e64695` |
| `2026-09-11-stage-17-pack-fixtures.json` | `781db78d1b08ac18efde01674353eff6b367ed87` |
| `2026-09-11-stage-17-regression-fixtures.json` | `620f7f6d828cfe12a2c844e86c081559bb7c88b7` |
| `2026-09-11-stage-17-verifier.py` | `121da1f61ed4150c7918de25138550bdfd135698` |
| `2026-09-11-stage-17-executed-checks.json` | `9f54f0ea0cea57b53924941951675f0774785b26` |
| `2026-09-11-stage-17-conformance.md` | `d8b99928352515e4d145771ac8814e4b46464c6b` |
| `2026-09-11-bootstrap-2-progress-through-stage-16.md` | `50b8a12e15c91de7c28b64fd420c720e06c3415f` |
| `bootstrap-2-progress.md` before receipt | `377881df6cd3e1a406d85aa3cb6b020bb0dd2944` |

This receipt changes only the live progress index. Verify its returned commit, parent, branch ref and resulting file. Stage 18 remains untouched.

## Resumption and authority

Use only `feat/bootstrap-2`. Complete and remotely verify the current stage before beginning the next. Retry transient errors; repair ordinary failures without weakening criteria. After Stage 17's verified receipt, stop for user verification. Do not begin Stage 18 until the user explicitly asks to continue. No PR, merge, release or maturity promotion is included.
