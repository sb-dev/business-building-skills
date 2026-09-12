# Business Building Skills — Customisation / Extension Packs Specification

**Status:** Canonical Extension Pack contract  
**Derived from:** accepted Stage 14 pack model, authoring workflow and Stage 17 pack-evaluation architecture  
**Boundary:** defines reusable business-model specialisation. It does not assert that any catalogue pack is implemented or installed.

## 1. Pack model

A Business Extension Pack is an optional, self-contained set of instructions/resources that specialises existing Business Building command contracts for a recurring **business mechanism**.

A pack may change:

- which roles/questions are material;
- evidence required;
- artefact detail;
- pricing/money/delivery/retention semantics;
- applicable metrics;
- capacity/cash checks;
- experiment types;
- evaluation criteria.

A pack does **not**:

- supply local customer facts;
- replace the core business dossier;
- create new action authority;
- weaken truthfulness, rights, economics, cash or professional gates;
- replace core commands with broader mutation permissions;
- execute CRM, payment, accounting, marketing or production systems;
- make an industry/location label a valid specialisation by itself.

Core must remain useful without any pack.

## 2. Qualification rule

A proposed pack qualifies for design only when all are supported:

1. a recurring business mechanism exists beyond a label;
2. core/current catalogue handling has a bounded insufficiency for that mechanism;
3. named effects materially specialise existing canonical commands;
4. economic, operational, capacity and cash consequences are coherent;
5. fit and non-fit/activation boundaries are explicit;
6. core invariants and precedence are preserved;
7. a discriminating showcase/evaluation design exists.

A pack claimed **implemented/validated** must additionally provide actual packaged resources, compatible versions, actual required execution and evaluation evidence. Research catalogue presence is never enough.

No minimum number of changed dimensions is required; one meaningful reusable effect can justify a pack, while fourteen superficial differences cannot.

## 3. Minimum pack record

Every pack version contains or resolves these responsibilities:

| Concern | Required content |
|---|---|
| identity and scope | stable mechanism name, version, owner, supported core/command versions, purpose, maturity/evidence date |
| applicability | positive mechanism facts, selection/confirmation rule, excluded/non-activation cases, unknown-fact behaviour, scoped component/decision |
| catalogue justification | comparison with core/existing packs, exact inadequacy, overlap, why a mode/revision is insufficient |
| core effects | trigger, affected command, required inputs, changed question/output/check, inherited invariants, evidence basis, positive/negative comparison |
| business/metric semantics | relevant units, cohorts/windows, formulas, cost identities, cash timing, assumptions and source limits |
| constraints/precedence | applicable findings/facts/decisions, forbidden overrides, conflicts and re-review triggers |
| showcase/evaluation | exact prompt/input/versions, conditions, criteria, actual results where executed, negative/non-activation/precedence cases, repair record |
| distribution/maintenance | local resources/scripts/assets, prerequisites/licences, reproduction, compatibility, retirement/review triggers, accurate maturity |

“Apply SaaS best practices” is not a core effect. A source URL is not a core effect. An effect must be observable in a named command’s business behaviour.

## 4. Fourteen business-model dimensions

These are permitted specialisation dimensions. Every candidate is assessed against all fourteen, but a pack may explicitly inherit a dimension unchanged.

| ID | Dimension | Legitimate specialisation | Invariant |
|---|---|---|---|
| D01 | customer / buyer structure | mechanism-specific user/payer/approver/supplier/contributor roles | roles require evidence; no invented personas |
| D02 | offer grammar | mechanism-specific entitlements, deliverables, acceptance, ongoing obligations | truthfulness, proof and exclusions remain explicit |
| D03 | pricing unit | seats, usage, engagements, visits, licences, fees, etc. | unit is evidence-led, not mandatory/default price |
| D04 | money model | recurring, usage, service, intermediary/funding distinctions | canonical transactions and own consideration prevent double counting |
| D05 | channel priorities | mechanism-specific fit questions and constraints | no universal SEO/ad/outreach mandate |
| D06 | sales path | mechanism-specific qualification, approval, transaction/acceptance states | seller activity/listing is not buyer commitment |
| D07 | delivery model | service, entitlement, inventory, matching or content-access dependencies | operator owns fulfilment; pack does not execute |
| D08 | retention model | renewal/repeat/matched-side/continued access semantics | continued billing alone is never value evidence |
| D09 | unit economics | mechanism-specific cost/cohort/fee bridges | preserve canonical definitions and no unsupported LTV/CAC |
| D10 | capacity constraints | human, technical, inventory, geographic, maintenance limits | no invented staff or schedulability from nominal hours |
| D11 | cash behaviour | collection/settlement/stock/refund/obligation timing | profit/closing cash cannot hide an earlier cash gap |
| D12 | core metrics | mechanism-appropriate numerator/denominator/unit/window | no universal business score |
| D13 | experiment types | mechanism-specific adequate tests | freeze decision rules/guardrails; hypothetical ≠ executed |
| D14 | quality criteria | acceptance/access/supply/version/client-transfer criteria | safety/truthfulness/rights remain core, not optional pack gates |

## 5. Activation contract

Activation is separate from applicability and separate again from action authority.

### 5.1 Selection

1. inspect actual task/project facts;
2. identify candidate mechanism and component scope;
3. check known core/pack compatibility;
4. apply a pack only when explicitly selected or allowed by an approved selection policy;
5. otherwise propose the candidate and continue an adequate core path;
6. if mechanism facts are unknown, ask/record the missing fact rather than invent activation;
7. if an explicitly requested pack is incompatible, do not apply it; explain the mismatch and continue/stop within core as appropriate.

A business name, sector, technology, city or founder job title is insufficient activation evidence unless it entails the actual mechanism.

### 5.2 Pack state annotation

When active, the decision record stores:

```text
pack name/version
supported core version
affected command/component scope
activation evidence
applied defaults
skipped defaults + reason
conflicts / blocked defaults
pack-specific metrics/evaluation references
```

Do not create a second authoritative business dossier.

## 6. Precedence

Apply proposed defaults in this exact order:

1. **verified legal/regulatory constraints + explicit project facts/instructions**;
2. **approved business decisions**;
3. **selected Extension Pack defaults**;
4. **core Business Building defaults for genuinely open choices**.

Important qualification: core mandatory evidence, truthfulness, customer rights, mutation and independent growth gates are **invariants**, not low-priority defaults. A pack cannot override them.

Examples:

- pack prefers £100/month, accepted project price is £80 → preserve £80 unless an authorised evidence-led pricing change is made;
- pack prefers renewal, explicit instruction requires one-time licence → preserve one-time exchange;
- pack recommends outreach, actual recipient permission/constraints unresolved → action remains blocked;
- pack proposes a commercially attractive guarantee, substantiation/operational/legal constraints fail → reject/block guarantee.

## 7. Core effects

A core effect must name:

```text
effect_id
trigger / activation condition
affected canonical command
required additional inputs
changed question / output / check
pack-specific metric or artefact detail
inherited invariants
source/evidence basis
positive comparison
negative/incompatible comparison
```

Packs specialise existing B/G/E command contracts; they do not invent replacement commands unless later architecture evidence explicitly reopens the core design.

## 8. Composition

Use at most one primary grammar for a bounded exchange by default.

For hybrid businesses, component composition requires a reconciliation record:

- payer/value exchange per component;
- shared inputs/resources/costs;
- overlapping obligations;
- pack/version/scope per component;
- precedence conflict handling;
- canonical transaction/cost identities to prevent double counting.

There is no last-loaded-wins rule. An unresolved overlap blocks the conflicting default.

Examples:

- SaaS + professional services: separate hosted-service and engagement exchanges, reconcile shared support/sales costs;
- creator product + coaching: digital access versus finite human service;
- marketplace + owned stock: intermediary fee flow versus own inventory sale;
- local-service marketplace: marketplace matching versus provider route/capacity.

`consulting-business` is an advisory mode of `professional-services`, not runtime inheritance or a second mandatory package.

## 9. Pack-aware metrics

Pack-specific metrics inherit the canonical metric contract:

```text
name/version + decision
formula/event rule
unit
numerator/denominator
population/cohort/window
currency / cost basis where relevant
source/assumption
realised vs forecast
calculation method
limitations
review trigger
```

A pack can require additional bridges (for example consumed → billable → invoiced units, matched eligible requests, door-to-door resource minutes) but cannot redefine the core meaning of evidence, contribution, cash or action authority for convenience.

## 10. Pack evaluation

Every implemented pack is evaluated on all seven Stage-17 concerns:

| ID | Concern | Pass condition |
|---|---|---|
| P01 | activation | fits actual mechanism/scope at compatible versions |
| P02 | non-activation | core handles non-fit case without false pack trigger/dependency |
| P03 | precedence | higher-priority facts/constraints/approved decisions remain intact |
| P04 | changed business behaviour | named effects materially change relevant questions/artefacts/checks |
| P05 | pack-specific metrics | units/denominators/windows/economics/cash reconcile |
| P06 | negative / incompatible cases | invalid/harmful cases fail while legitimate mechanism remains possible |
| P07 | core vs core+pack difference | actual paired run on identical task/data/criteria/version evidence exists |

Also verify preservation/repair. A pack-induced local defect is repaired at the pack layer unless evidence identifies a core defect.

### 10.1 Core-vs-pack comparison

Both conditions receive identical:

- task and fixed input;
- core version;
- deterministic tools;
- professional/truthfulness/rights gates;
- evaluation criteria;
- permitted operations.

The pack condition adds only the declared specialised effect. Retain actual outputs/settings/failures. **Core is not required to fail**: it may reach the same correct decision; a useful pack may provide systematic specialised coverage rather than a different conclusion.

Do not manufacture pack superiority by removing information/safeguards from core.

## 11. Packaging

A target implemented pack is self-contained under `extension-packs/<name>/`, for example:

```text
extension-packs/<name>/
├── PACK.md
├── references/
├── templates/
├── examples/
└── evals/
```

The exact later file format may change mechanically, but must retain the minimum pack record, local resources and reproduction entry points.

Packaging rules:

- no hidden dependency on a sibling skill checkout;
- declare compatible core/command versions;
- package required local references/templates/scripts/assets;
- document licences and prerequisites accurately;
- no secrets or customer/private evidence in public assets;
- no provider-specific runtime requirement unless the pack mechanism truly depends on it and that dependency is explicit;
- no automatic registry/release/maturity promotion from packaging alone.

## 12. Pack authoring workflow — 11 steps

Use the existing `business-pack-author` P01–P07 commands. The dependency sequence is:

| Step | Required activity | Durable output |
|---|---|---|
| A01 inspect catalogue | read actual catalogue/candidates/compatibility | inspection record |
| A02 prove existing pack insufficient | compare core, existing pack, bounded mode/revision, new candidate | insufficiency/selection decision |
| A03 research business-model practice | inspect relevant primary/professional/empirical evidence and limits | source/research record |
| A04 define changed core behaviour | activation, non-activation and named command effects | specialisation/effect definition |
| A05 define economics and constraints | payer/unit/cost/cash/capacity/retention/metrics/professional limits | business semantics record |
| A06 build showcase | fixed scenario visibly exercising effects and safeguards | showcase package |
| A07 include exact prompt | literal self-contained task/inputs/versions/scope | exact prompt |
| A08 create positive / negative evals | activation/non-activation/precedence/metrics/incompatible/preservation cases | frozen eval bank |
| A09 compare core vs core+pack | actually run both compatible conditions where an executed claim is required | paired run record |
| A10 validate | structural/calculation/behaviour/package review at exact version | PASS/FAIL/BLOCKED validation report |
| A11 catalogue | add/revise entry with honest maturity, only under catalogue-edit authority | versioned catalogue entry |

For a small typo-only revision, unchanged research need not be repeated, but all acceptance affected by the changed claim/version must be rerun.

## 13. Showcase contract

A reproducible showcase contains:

```text
exact prompt
fixed input identities and synthetic/observed labels
accepted decisions and rights
core + pack versions
selected condition and activation basis
tool/host/settings where actually executed
permitted operations
frozen criteria
actual outputs/failures where executed
source/read limitations
repair/decision
```

An authored expected output is not an executed showcase. Failed runs remain visible.

## 14. Lifecycle: update, withdrawal, merge, retirement

### 14.1 Update
A pack update does not automatically revise prior business decisions. Record changed effects/compatibility/evidence, review affected consumers and rerun relevant pack comparisons before accepting the new version.

### 14.2 Withdrawal
Withdrawal stops future default application but preserves customer rights, obligations, historical outputs and valid accepted decisions made under the prior version.

### 14.3 Merge/retire
Merge or retire when core or another candidate now serves the full mechanism with less duplication. Do not preserve a pack merely because it already exists.

### 14.4 Core defect
Change core only when production/evaluation evidence demonstrates a core defect across its intended scope. Then rerun affected packs; do not patch every pack independently to conceal core drift.

## 15. Maturity labels

Catalogue/pack maturity must describe evidence truthfully. At minimum distinguish:

```text
research/design candidate
implemented package
installed/structurally validated
behaviourally evaluated
paired core-vs-pack evaluated
release/registry status if separately authorised
```

A research candidate is not an implemented pack. A generated directory is not a behavioural validation. A deterministic design projection is not an installed LLM comparison.

## 16. Rejected pseudo-packs

Reject a proposal based solely on:

```text
AI startup
finance company
fitness business
London business
book/author identity
provider bundle
executive/job title
```

A legitimate mechanism inside such a project may still select an existing pack: e.g. hosted metered service → SaaS, scheduled geographic delivery → local service, inventory sale → ecommerce. Regulated-sector questions remain specialist constraints rather than a “finance pack” exemption.

## 17. Canonical references

- system boundaries/core skills: [01](01-business-building-skills-system-spec.md)
- business artefact/economic semantics: [02](02-business-building-skills-workflows-and-artifacts-spec.md)
- packaging/install/CI: [03](03-business-building-skills-repository-and-contracts-spec.md)
- pack evaluation and release gates: [04](04-testing-and-benchmark-spec.md)
- curated research catalogue: [06](06-business-building-extension-pack-catalogue.md)

## 18. Research lineage

Primary accepted source logs:

- [Stage 13 pack-author command contracts](research-logs/2026-09-10-stage-13-pack-command-contracts.md)
- [Stage 14 pack model](research-logs/2026-09-10-stage-14-pack-model.md)
- [Stage 14 pack-authoring contract](research-logs/2026-09-10-stage-14-pack-authoring.md)
- [Stage 14 candidate catalogue](research-logs/2026-09-10-stage-14-candidate-catalogue.md)
- [Stage 14 design probes](research-logs/2026-09-10-stage-14-design-probes.md)
- [Stage 17 benchmark taxonomy](research-logs/2026-09-11-stage-17-benchmark-taxonomy.md)

The pack contract preserves core safeguards and does not upgrade research candidates to implementation status.
