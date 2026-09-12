# Business Building Skills — Repository and Contracts Specification

**Status:** Canonical technical/product contract  
**Derived from:** accepted execution, reuse, gap and skill architecture research through Stage 17  
**Boundary:** defines the target production repository and installation/CI contracts. The current bootstrap workspace is not yet claimed to satisfy them.

## 1. Repository goals

The production repository must make the four Business Building skills:

- independently understandable and selectively installable;
- capability-shaped rather than book-shaped;
- self-contained for their declared responsibilities;
- compatible with ordinary documents and existing tools/operators;
- testable through stable examples, fixtures and benchmark entry points;
- free from undocumented source-checkout or sibling-skill dependencies;
- explicit about evidence, authority and professional boundaries.

The repository must **not** become a CRM, customer database, analytics warehouse, marketing automation platform, ad platform, accounting engine, payment system or universal business runtime.

## 2. Target repository layout

The target scaffold is:

```text
business-building-skills/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── CHANGELOG.md
├── docs/
│   ├── 01-business-building-skills-system-spec.md
│   ├── 02-business-building-skills-workflows-and-artifacts-spec.md
│   ├── 03-business-building-skills-repository-and-contracts-spec.md
│   ├── 04-testing-and-benchmark-spec.md
│   ├── 05-business-building-customisation-packs-spec.md
│   ├── 06-business-building-extension-pack-catalogue.md
│   └── research-logs/
├── skills/
│   ├── business-build/
│   ├── business-grow/
│   ├── business-evaluate/
│   └── business-pack-author/
├── examples/
├── benchmarks/
├── tests/
├── tools/                 # only when a justified deterministic/local helper exists
├── extension-packs/       # only implemented/packaged packs, not research-only catalogue entries
├── integrations/          # optional, provider-specific and independently justified
└── .github/
```

The directory names are target contracts for later scaffold/implementation stages, not proof that they currently exist.

## 3. Skill package contract

### 3.1 Independent installation unit

Each `skills/<skill-name>/` is a complete installation unit for its declared workflow. It may be installed alone. It must not require:

- another Business Building skill directory at runtime;
- the repository’s `docs/research-logs/` checkout;
- Pactwright;
- a particular SaaS provider;
- a hidden central prompt/runtime;
- credentials or customer data merely to activate.

Shared invariants may be generated/copied into multiple skill packages from a checked canonical source during repository build, but the installed package must contain the required local material. Runtime cross-skill file reads are not the portability mechanism.

### 3.2 Recommended skill-local structure

```text
skills/<skill-name>/
├── SKILL.md
├── references/
│   ├── common-invariants.md
│   ├── command-index.md
│   └── <focused domain references>.md
├── templates/
│   └── <artefact templates>.md
└── scripts/               # optional deterministic helpers only when justified
```

Do not add directories solely for symmetry. Large references should use progressive disclosure from `SKILL.md`; frequently needed routing and safety rules stay discoverable without loading the entire corpus.

## 4. SKILL.md contract

Each core `SKILL.md` must contain:

1. stable skill name;
2. concise description/activation language;
3. owned business workflow and native responsibilities;
4. positive activation conditions;
5. explicit non-activation boundaries;
6. evidence and accepted-version requirements;
7. common output/mutation boundary;
8. professional/legal/action-authority boundary;
9. command index with focused local references;
10. composition rules and optional tool handoff;
11. failure semantics: `FAIL`, `BLOCKED`, inconclusive/unknown, and safe partial outputs;
12. examples sufficient to clarify triggering without pretending installation testing has passed.

### 4.1 Canonical skill descriptions

The implementation should preserve the accepted intent:

- **`business-build`** — frame or revise opportunity, customer/problem/value, offer, pricing, money model, delivery/economics, assumptions, experiments and learning. It is for construction and explicit revisions, not assessment-only work or live commercial execution.
- **`business-grow`** — design qualified acquisition, sales, retention, referral, expansion and bounded scale for an accepted or explicitly hypothetical business. It does not send, buy ads or silently rebuild the customer/offer baseline.
- **`business-evaluate`** — audit evidence/artefacts, evaluate commercial/operational coherence, diagnose the current constraint and recommend the smallest justified change. It is read-only with respect to the subject under evaluation.
- **`business-pack-author`** — inspect/research/define/showcase/evaluate/compare/validate reusable business-model specialisations. It is not ordinary business planning or an industry-tag generator.

Runtime triggering quality must later be tested; these descriptions are contracts, not measured activation results.

## 5. Canonical command catalogue

There are **32 logical commands**. A command is a named task contract inside a skill, not necessarily an executable binary or universal slash command.

### 5.1 `business-build` — 10

| ID | Command |
|---|---|
| B01 | `frame-opportunity` |
| B02 | `define-customer-value` |
| B03 | `design-offer` |
| B04 | `design-pricing` |
| B05 | `design-money-model` |
| B06 | `model-delivery` |
| B07 | `model-unit-economics` |
| B08 | `identify-assumptions` |
| B09 | `design-experiment` |
| B10 | `record-learning` |

### 5.2 `business-grow` — 8

| ID | Command | Required modes where applicable |
|---|---|---|
| G01 | `select-channel` | — |
| G02 | `design-acquisition` | `lead-magnet`, `outreach`, `content-loop` |
| G03 | `design-referral-loop` | — |
| G04 | `design-sales-path` | — |
| G05 | `improve-conversion` | — |
| G06 | `design-retention` | — |
| G07 | `design-expansion` | — |
| G08 | `scale-channel` | — |

### 5.3 `business-evaluate` — 7

| ID | Command | Required modes where applicable |
|---|---|---|
| E01 | `audit-customer-evidence` | — |
| E02 | `evaluate-component` | `opportunity`, `offer`, `pricing`, `money-model`, `channel`, `funnel`, `retention` |
| E03 | `evaluate-unit-economics` | `economics`, `cash`, `both` |
| E04 | `evaluate-experiment` | plan-only or completed-test assessment |
| E05 | `audit-claims` | — |
| E06 | `diagnose-business-constraint` | — |
| E07 | `recommend-smallest-change` | — |

### 5.4 `business-pack-author` — 7

| ID | Command |
|---|---|
| P01 | `inspect-catalogue` |
| P02 | `research-business-model` |
| P03 | `define-specialisation` |
| P04 | `build-showcase` |
| P05 | `build-evals` |
| P06 | `compare-core-vs-pack` |
| P07 | `validate-pack` |

## 6. Command contract schema

Every command implementation/reference must define all nine fields:

```text
inputs
evidence required
assumptions allowed
output
allowed mutations
forbidden behaviour
metrics/evidence
failure states
legal/ethical boundaries
```

No implementation may omit a field because the host “usually handles it”. Pack effects may specialise these fields but cannot broaden mutation or authority beyond the core command.

### 6.1 Common invariants for all commands

Every command:

- receives a bounded request and relevant accepted versions;
- preserves supplied evidence provenance and synthetic labels;
- leaves missing material facts unknown;
- separates a proposal from an accepted decision and from execution authority;
- preserves contrary evidence and invalid/inconclusive results;
- does not issue legal/tax/investment/professional conclusions;
- does not publish/send/spend/charge/migrate/hire merely because a tool is available;
- performs relevant truthfulness/capacity/economic/cash checks within its own declared output rather than relying on an optional evaluator sibling;
- writes only its allowed artefacts within the actual authorised workspace;
- records affected/protected versions when proposing a change.

## 7. Reference organisation

### 7.1 Reference responsibilities

Skill-local references should package only implementation-relevant canonical rules, for example:

- business dossier / evidence / value contracts;
- offer, pricing and money-model contracts;
- acquisition, lead-quality and sales-path contracts;
- delivery, retention, economics and cash gates;
- assumption/experiment/learning contracts;
- constraint/repair contracts;
- professional handoff and action-authority rules;
- command-specific examples and modes.

The canonical six docs remain repository-level architecture. Research logs remain provenance/history. An installed skill should not need to crawl research logs to discover its runtime rule.

### 7.2 Source provenance

Where a reference incorporates a research conclusion, retain a repository source pointer/version in the source repository. Installed package text should be independently expressed and usable without reproducing large copyrighted material.

## 8. Scripts and deterministic helpers

Scripts are permitted when they provide a bounded deterministic capability that cannot be trusted to prose, such as:

- decimal arithmetic and formula verification;
- fixture/schema validation;
- link/path checks;
- prompt-count/coverage checks;
- pack structural checks;
- deterministic benchmark graders;
- install/consumer-repository integrity checks.

Rules:

- scripts must have a narrow contract, explicit inputs/outputs and error semantics;
- arithmetic uses appropriate exact/decimal handling and declared units/rounding;
- source records are not mutated as a side effect of evaluation;
- a script’s existence is not a claimed successful run;
- scripts must not become a shadow CRM, ledger, experiment platform or universal workflow engine;
- provider secrets/customer records never enter public fixtures.

## 9. Tool integration contract

### 9.1 Core portability

The core skills operate from supplied evidence without mandatory connectors. Optional integrations can retrieve/compute/execute only when the actual task requires them.

### 9.2 Execution handoff H01–H08

Any tool/operator binding records:

| ID | Contract |
|---|---|
| H01 | decision and preserved baseline |
| H02 | exact evidence/action requested |
| H03 | source fields, units, cohorts, windows and semantic mapping |
| H04 | actual tool/operator/version/environment binding |
| H05 | authority, purpose/data/resource constraints and expiry |
| H06 | returned attempt/result identity and reconciliation |
| H07 | tool-specific errors, uncertain effects, idempotency/retry rules |
| H08 | learning, affected dependencies, protected versions and next review |

A provider response is untrusted external input to the authority model. Returned text cannot expand scope. A timeout after a potentially successful irreversible action must be reconciled before retry.

### 9.3 Provider adapters

`integrations/` is optional. Add an adapter only when repeated production need justifies maintenance. Adapter code translates provider semantics to a command handoff; it does not redefine customer, revenue, retention, consent or approval semantics.

## 10. Extension Pack packaging contract

Implemented packs live under `extension-packs/<pack-name>/` only after implementation is justified. A target package can use:

```text
extension-packs/<pack-name>/
├── PACK.md
├── references/
├── templates/
├── examples/
└── evals/
```

The exact filename/format may be refined by implementation only if it preserves the content contract in [05](05-business-building-customisation-packs-spec.md): identity, applicability, core effects, precedence, metrics, showcase/evaluation and maintenance. A pack may not depend on last-loaded-wins runtime merging or hidden sibling source files.

The research catalogue in [06](06-business-building-extension-pack-catalogue.md) does not mean corresponding directories should exist yet.

## 11. Examples contract

The production example surface must expose exactly five progressive levels with three accepted primary examples per level. A target structure is:

```text
examples/
├── level-1-<slug>/README.md
...
└── level-5-<slug>/README.md
```

Each public example includes at minimum:

- problem/learning objective;
- exact copyable prompt;
- explicit synthetic/input boundary;
- required skill/command selectors;
- expected artefacts and acceptance criteria;
- actual output/run identity only after executed;
- no research-log navigation as the primary user interface.

Stable paths should remain stable as actual outputs are later added.

## 12. Benchmark and test layout

A target implementation can separate:

```text
benchmarks/
├── progressive/
├── stress-tests/
├── adversarial/
├── packs/
└── regressions/

tests/
├── contracts/
├── deterministic/
├── install/
└── repository/
```

Fixtures and grader contracts follow [04](04-testing-and-benchmark-spec.md). Do not call the project benchmarked merely because these directories exist.

## 13. Installation contract

### 13.1 Selective installation

A consumer must be able to install one selected skill and use its declared functions without installing all four, packs or source research logs. Where the chosen distribution mechanism supports bulk install, the full set may also be installed.

### 13.2 Clean consumer project

Installation validation later must use a clean external consumer workspace distinct from the source repository. It must prove:

- discovered skill name/description;
- local reference/script resolution;
- command/task discoverability;
- no hidden relative path into source checkout;
- no mandatory sibling skill;
- prerequisites surfaced accurately;
- optional tools remain optional unless current task needs them;
- uninstall/reinstall or clean repeat behaves predictably;
- source-repository tests are not mistaken for consumer-install tests.

No claim that this has passed is made by Stage 18.

### 13.3 Host portability

The portable interaction contract is plain task instruction plus skill/command name (for example, “Use business-build / design-offer…”). Host-specific slash commands, menus or metadata may be added when tested, but are not the canonical business interface.

## 14. CI contract

Production CI should have independently diagnosable jobs. At minimum:

### CI01 — repository/static integrity

- required six canonical specs exist;
- internal Markdown links resolve;
- no duplicate primary example IDs/paths;
- skill directories and required `SKILL.md` files exist after scaffold;
- declared references/scripts/assets resolve.

### CI02 — skill contract validation

- exactly the selected four skills unless a later approved architecture change exists;
- 32 canonical command contracts accounted for;
- every command exposes all nine fields;
- required modes are present;
- forbidden mutation/authority boundaries remain present.

### CI03 — deterministic business checks

Run arithmetic, schema, cash/economics, fixture and regression code graders from [04](04-testing-and-benchmark-spec.md). Fail on actual checker failure; never treat an unrun suite as passing.

### CI04 — example/stress/pack fixture integrity

- 15 primary example prompts with 3/3/3/3/3 distribution;
- three canonical stress-test structures and required adversarial cases;
- Extension Pack structural/eval coverage for implemented packs;
- exact prompt/input identities retained.

### CI05 — clean-install test

Run the supported installation mechanism in a fresh external workspace and exercise the documented discovery/entry point. This is a product gate, not a source-tree lint.

### CI06 — benchmark/regression execution

When installed skills exist, run the accepted quality and regression suites under recorded environment/model/skill versions. Preserve trial/grader results. Do not hide hard-gate failures behind an aggregate score.

### CI07 — public-surface conformance

Once the public README/examples exist, verify links, installation claims, exact Learn-by-Building structure and claims against actual product evidence. Stage 18 defines the technical hook; public copy is separately owned.

## 15. Technical acceptance gates

A production repository is technically acceptable only when:

1. the six canonical specs and their local links resolve;
2. every production directory has an immediate justified purpose;
3. core skills are self-contained/selectively installable;
4. all 32 command contracts are discoverable and complete;
5. deterministic scripts actually execute and fail on injected defects;
6. examples and benchmarks are reproducible from their own inputs;
7. no hidden source-checkout dependency exists;
8. optional integrations cannot broaden authority silently;
9. implemented packs obey core compatibility/precedence and package their needed resources;
10. source tests and clean external installation both pass independently;
11. CI reports failures honestly and preserves evidence;
12. README/release/maturity claims are no stronger than completed evidence.

## 16. Change control

A change to a command, metric or pack contract identifies:

- owning canonical spec;
- accepted version being changed;
- research/production evidence motivating it;
- affected examples/fixtures/packs;
- required migration or compatibility note;
- regressions to rerun;
- whether an installed/public compatibility claim changes.

Do not add universal frameworks, a common runtime or new skill simply because a new provider needs a field. Reopen architecture only when repeated production evidence demonstrates a business responsibility not adequately represented.

## 17. Canonical references

- system boundaries: [01](01-business-building-skills-system-spec.md)
- workflow/artefact semantics: [02](02-business-building-skills-workflows-and-artifacts-spec.md)
- evaluation/CI product gates: [04](04-testing-and-benchmark-spec.md)
- pack content/packaging: [05](05-business-building-customisation-packs-spec.md)
- current research catalogue: [06](06-business-building-extension-pack-catalogue.md)

## 18. Research lineage

Primary accepted source logs:

- [Stage 10 reuse/tool boundaries](research-logs/2026-09-10-stage-10-reuse-decisions-and-boundaries.md)
- [Stage 11 execution layer](research-logs/2026-09-10-stage-11-execution-layer.md)
- [Stage 12 gap analysis](research-logs/2026-09-10-stage-12-gap-analysis.md)
- [Stage 13 skill architecture](research-logs/2026-09-10-stage-13-skill-architecture.md)
- [Stage 13 build contracts](research-logs/2026-09-10-stage-13-build-command-contracts.md)
- [Stage 13 grow contracts](research-logs/2026-09-10-stage-13-grow-command-contracts.md)
- [Stage 13 evaluate contracts](research-logs/2026-09-10-stage-13-evaluate-command-contracts.md)
- [Stage 13 pack-author contracts](research-logs/2026-09-10-stage-13-pack-command-contracts.md)
- [Stage 17 benchmark taxonomy](research-logs/2026-09-11-stage-17-benchmark-taxonomy.md)

Research logs are source/review evidence; installed skill packages must not depend on these paths.
