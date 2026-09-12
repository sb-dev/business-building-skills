# Stage 18 — Canonical specification synthesis

**Date:** 12 September 2026  
**Branch:** `feat/bootstrap-2`  
**Starting boundary:** verified Stage 17 receipt `53ce5e1c8980786055d7a301375e9919fab2b04b`  
**Governing Stage 18 requirement:** current `main`, Stage 18 / bootstrap §25.

## 1. Goal

Generate six complete canonical specifications from persisted accepted research so later implementation can proceed without inventing business architecture in code.

This stage is a synthesis/publication stage. It does not implement skills, packs, examples, CI, installation or runtime integrations. It must nevertheless define those target contracts where the owning canonical specification requires them.

## 2. Authority and source-version note

The bootstrap specification on current `main` has changed elsewhere since the older bootstrap blob recorded by earlier progress receipts. Current `main` blob is `d2f50bb908ffedf374b7f753bdf4e818bbcb3b22`; the older accepted bootstrap copy on `feat/bootstrap-2` is `a0ac1b6c78a0cde8ccd9aca6fda6c5b0880c516d`.

The Stage 18 contract was reread from current `main`. Its prescribed six filenames, ownership lists, persisted-research-log requirement and exit criterion remain the same. This synthesis therefore uses the current Stage 18 contract while preserving the accepted Stage 1–17 research decisions from the verified branch. Unrelated later changes on `main` are not imported into accepted earlier-stage architecture.

## 3. Accepted source set actually inspected

All project sources below were read from immutable Stage 17 receipt `53ce5e1c8980786055d7a301375e9919fab2b04b`, except the current-main bootstrap requirement noted above.

### Domain, evidence and principles

- `2026-09-09-stage-01-domain-and-professional-boundary.md`
- `2026-09-09-stage-02-reconciliation-and-taxonomy.md`
- `2026-09-10-stage-03-claims-failures-and-principles.md`

### Business workflows and artefacts

- `2026-09-10-stage-04-business-customer-and-value-model.md`
- `2026-09-10-stage-05-offer-and-pricing-architecture.md`
- `2026-09-10-stage-05-money-model-taxonomy.md`
- `2026-09-10-stage-06-demand-lead-and-sales-architecture.md`
- `2026-09-10-stage-07-delivery-and-retention-model.md`
- `2026-09-10-stage-07-unit-economics-and-cash-contract.md`
- `2026-09-10-stage-08-assumptions-experiments-and-learning.md`
- `2026-09-10-stage-08-constraint-diagnosis-and-repair.md`
- `2026-09-10-stage-09-ethical-and-legal-handoffs.md`

### Reuse, execution, gaps and skills

- `2026-09-10-stage-10-reuse-decisions-and-boundaries.md`
- `2026-09-10-stage-11-execution-layer.md`
- `2026-09-10-stage-12-gap-analysis.md`
- `2026-09-10-stage-13-skill-architecture.md`
- `2026-09-10-stage-13-build-command-contracts.md`
- `2026-09-10-stage-13-grow-command-contracts.md`
- `2026-09-10-stage-13-evaluate-command-contracts.md`
- `2026-09-10-stage-13-pack-command-contracts.md`

### Extension Packs

- `2026-09-10-stage-14-pack-model.md`
- `2026-09-10-stage-14-candidate-catalogue.md`
- `2026-09-10-stage-14-pack-authoring.md`
- `2026-09-10-stage-14-design-probes.md`

### Examples, stress tests and benchmarks

- `2026-09-10-stage-15-selection-and-coverage.md`
- `2026-09-11-stage-16-stress-test-contract.md`
- `2026-09-11-stage-16-stress-test-a-kakeibo.md`
- `2026-09-11-stage-16-stress-test-b-fde-consultancy.md`
- `2026-09-11-stage-16-stress-test-c-production-skills-ecosystem.md`
- `2026-09-11-stage-17-benchmark-taxonomy.md`
- `2026-09-11-stage-17-case-contracts.md`
- `2026-09-11-stage-17-acceptance-gates.md`
- `2026-09-11-stage-17-regression-policy.md`

Earlier conformance/verification receipts remain accepted evidence of those stages; Stage 18 does not rerun their external research or relabel their design checks as installed-product evidence.

## 4. Canonical ownership decisions

The six files follow bootstrap ownership exactly:

| Canonical file | Exclusive primary ownership |
|---|---|
| `01-business-building-skills-system-spec.md` | mission, scope, book/evidence relationship, principles, business-system architecture, core skills, execution and legal/ethical boundaries, build order, system acceptance |
| `02-business-building-skills-workflows-and-artifacts-spec.md` | customer/value, offer/pricing, money model, acquisition, sales, delivery, retention/expansion, economics, cash, assumptions, experiments, learning, diagnosis, preservation/repair, handoffs |
| `03-business-building-skills-repository-and-contracts-spec.md` | repository layout, SKILL.md, commands, references, scripts, tool integration, self-containment, installation, CI, technical acceptance |
| `04-testing-and-benchmark-spec.md` | deterministic/reasoning/behavioural/adversarial testing, progressive examples, stress tests, pack evaluation, regressions, installation and release gates |
| `05-business-building-customisation-packs-spec.md` | pack model, dimensions, activation, precedence, effects, metrics, evaluation, packaging and authoring |
| `06-business-building-extension-pack-catalogue.md` | curated candidates, profiles, selection rationale, showcases/prompts, pack evals and maturity |

Cross-links are allowed; duplicated rules are limited to necessary invariants and summaries, with one canonical owner named above.

## 5. Key synthesis choices

### 5.1 Four skills and 32 commands are preserved

Stage 18 does not reopen the Stage 13 selection. It carries forward:

- `business-build` — 10 commands;
- `business-grow` — 8;
- `business-evaluate` — 7;
- `business-pack-author` — 7.

Commands remain logical task contracts rather than invented shell/slash APIs. The repository spec defines the target package/installation boundary without claiming host triggering has been tested.

### 5.2 Document-led execution remains the system boundary

Business reasoning stays in ordinary versioned artefacts. Existing systems/operators own CRM, sending, ads, analytics, billing, accounting, surveys, experiment assignment and other external effects. Optional integrations adapt tool semantics; they do not redefine business meaning or authority.

### 5.3 Packs remain mechanism specialisations

The catalogue carries eight independent research/design candidates and one merged consulting advisory mode. No pack is upgraded to implementation or installed maturity. The exact nine Stage-14 synthetic showcase prompts are preserved in Spec 06.

### 5.4 Benchmark design remains distinct from product benchmark evidence

Spec 04 incorporates the 15 progressive examples, three canonical stress tests, Stage-17 deterministic/reasoning/behavioural/adversarial/pack/regression contracts, installation and release gates. Stage 17's 85/85 reference-grader result is identified as benchmark-design integrity, not an installed-agent pass rate.

### 5.5 Canonical specs are implementation-ready, not implementation claims

Spec 03 defines a concrete target layout, skill-local packaging, CI and installation contract because §25 assigns those responsibilities to it. The bootstrap workspace is not claimed to satisfy that target yet; later scaffold/implementation/install stages must execute it.

## 6. Deferred work preserved

This stage does not:

- implement `skills/`, examples, benchmark runners or packs;
- create the public README design;
- perform cross-project review;
- scaffold production directories;
- execute the core vertical;
- run installed core-vs-pack comparisons;
- validate clean external installation;
- integrate Pactwright or promote registry maturity;
- conduct the final Stage 0–26 audit.

Those remain future tasks under their own governing stages. This deferral does not weaken any Stage 18 deliverable because the six specifications define the contracts those tasks must implement.

## 7. Stage 18 deliverables

Exactly six canonical documents are generated at the prescribed `docs/` paths. Stage 18 also persists this synthesis record, an exact verifier, execution results, conformance and the normal bootstrap progress evidence required by the execution contract.

## 8. Exit interpretation

Stage 18 passes only if all six canonical specs exist, own every assigned responsibility substantively, preserve accepted decisions, resolve their internal/research links, contain exact architectural counts where applicable, and avoid implementation/maturity claims not supported by prior evidence.

Implementation can then proceed from these specifications without inventing the business architecture in code.
