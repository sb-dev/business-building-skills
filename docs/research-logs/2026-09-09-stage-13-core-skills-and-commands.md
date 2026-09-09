# Stage 13 — Core Skills and Commands

**Version:** 1.0  
**Date:** 9 September 2026  
**Status:** Architecture complete  
**Branch:** `feat/bootstrap`

## 1. Decision

Adopt four core skills:

```text
business-build
business-grow
business-evaluate
business-pack-author
```

Do **not** add separate `business-model` or `business-experiment` skills. Their responsibilities are tightly coupled to build/evaluate workflows and do not yet demonstrate independent installation value. Do not mirror the five source books or executive job titles.

Commands are bounded operations invoked when independent testing, reuse or diagnosis benefits from a stable contract. They are not a workflow engine. A skill may perform a small internal step without creating a command file for it.

## 2. Shared command contract

Every implemented command declares:

```text
purpose
inputs and evidence required
facts/assumptions allowed
output / changed artefacts
allowed mutation scope
preservation dependencies
forbidden behaviour
calculation/tool requirements
approval / professional gates
failure states
acceptance checks
```

Shared rules: never invent customer/market/financial evidence; label synthetic fixtures; preserve metric definitions; deterministic arithmetic owns calculations; external side effects require authority; reviewed legal constraints outrank optimisation; packs specialise defaults but do not override explicit facts or accepted decisions.

## 3. `business-build`

**Mission:** turn an opportunity or bounded new proposition into a coherent, testable commercial system.

| Command | Input → output | Key acceptance / forbidden behaviour |
|---|---|---|
| `frame-opportunity` | Goal, context, constraints, available evidence → bounded decision and business hypothesis | Names owner objective and unknowns; no automatic growth objective |
| `model-customer-value` | Customer evidence → roles, problem/alternatives, value/proof model | Separates declared/observed/synthetic; no persona-as-evidence |
| `design-offer` | Customer/value model + delivery facts → offer, scope, obligations, proof | Deliverable and truthful; no fake scarcity/testimonials |
| `design-pricing-monetisation` | Offer + customer/economic evidence → price and transaction alternatives | No universal premium-price rule or hidden terms |
| `model-delivery-economics` | Offer + costs/capacity/timing → delivery, contribution and cash model | Deterministic calculations; visible assumptions/units |
| `design-business-experiment` | Material assumption + decision → falsifiable bounded test | Has success/failure/inconclusive/stop rules; no deceptive fake product |
| `build-business-brief` | Accepted outputs → coherent brief and next commitment | Preserves source/evidence links and unresolved blockers |

The end-to-end skill can invoke these in a different order when dependencies demand it. For an existing business, it should prefer `business-evaluate` rather than rebuilding from scratch.

## 4. `business-grow`

**Mission:** improve acquisition, sales and continued value without outrunning economics, capacity or authority.

| Command | Input → output | Key acceptance / forbidden behaviour |
|---|---|---|
| `select-channel` | Customer/offer + access/economics → ranked testable channel hypotheses | No all-channel default; permission and capacity considered |
| `design-acquisition-test` | Channel hypothesis → bounded demand test and measurement plan | Qualified/downstream signal, not vanity volume |
| `design-sales-path` | Buyer/process evidence → qualification and sales path | Distinguishes person/account/opportunity; no generic funnel imposed |
| `diagnose-conversion` | Path data + definitions → competing causes and smallest test | Measurement checked before causal story |
| `design-retention-expansion` | Delivered-value/cohort evidence → continued-value or expansion hypothesis | No forced recurring revenue or cancellation obstruction |
| `scale-channel` | Validated channel + delivery/economics/cash evidence → bounded scale decision | Scale blocked by capacity, negative contribution, cash or review gap |

Lead magnets, outreach messages, content and referral mechanics are tactics within `design-acquisition-test` unless later evidence proves independent command value. This avoids turning the repository into a marketing-playbook catalogue.

## 5. `business-evaluate`

**Mission:** audit a business decision/system, identify the current constraint and recommend the smallest justified change.

| Command | Input → output | Key acceptance / forbidden behaviour |
|---|---|---|
| `audit-evidence` | Claims/evidence → provenance, scope and uncertainty findings | Unknown ≠ pass; synthetic ≠ observed |
| `evaluate-offer-economics` | Offer/pricing/delivery/economic records → multidimensional findings | No one-number offer score |
| `evaluate-acquisition-sales` | Channel/path data → reach/quality/conversion/downstream findings | Attribution labelled; denominators compatible |
| `evaluate-retention-cash` | Cohort/cash/capacity data → continued-value and exposure findings | LTV horizon explicit; receipts ≠ profit |
| `evaluate-experiment` | Experiment + results → support/challenge/inconclusive and decision limits | Invalid instrumentation cannot produce confident success |
| `audit-claims` | Customer-facing claims/terms → substantiation and professional-review gaps | Issue spotting only; no invented legal conclusion |
| `diagnose-constraint` | Business objective + evidence → ranked explanations and supported constraint | Lowest metric not automatically bottleneck |
| `recommend-smallest-change` | Diagnosis + accepted decisions → mutation plan and preservation scope | No broad rewrite unless evidence requires it |

A full `business-evaluate` run composes only relevant commands. Not-applicable dimensions remain explicit.

## 6. `business-pack-author`

**Mission:** create a reusable business-model specialisation only when core defaults are insufficient.

Commands:

```text
inspect-catalogue
research-business-model
define-specialisation
define-core-effects
build-pack-showcase
build-pack-evals
compare-core-vs-pack
validate-pack
```

The authoring skill must prove material behavioural differences and negative/incompatible cases. It cannot use a pack to override verified legal constraints, explicit project facts or accepted business decisions.

## 7. Skill-local structure

Target only needed surfaces:

```text
skills/<skill>/
├── SKILL.md
├── commands/       # bounded reusable operations only
├── references/     # contracts/rubrics needed by this skill
├── scripts/        # deterministic calculations/validation only
└── evals/          # skill-local behavioural fixtures where useful
```

Do not create empty `assets/`, `scripts/`, `evals/` or command directories merely for symmetry. Shared domain facts should not be duplicated across skills; a small root testing fixture may exercise composition without becoming a runtime dependency.

## 8. First vertical

Implement in this order:

1. `business-build`: frame, customer/value, offer, delivery/economics, experiment, brief.
2. deterministic economics validator/calculator.
3. `business-evaluate`: evidence, offer/economics, experiment, constraint/smallest change.
4. one professional-service synthetic fixture proving build → evaluate → bounded correction.
5. `business-grow` only after the core vertical passes.
6. pack authoring after at least one pack differential is designed.

This ordering proves the central business loop before acquisition automation or catalogue breadth.

## 9. Rejected alternatives

- one skill per book;
- separate marketing, sales, finance and operations executive agents;
- separate experiment skill before independent-installation evidence;
- `business-model` skill duplicating build/evaluate;
- dozens of tactic commands for SEO, ads, outreach or CRM operations;
- universal orchestration skill coordinating providers.

## 10. Exit

The four-skill architecture covers the end-to-end loop with stable command responsibilities, explicit mutations and execution boundaries. Stage 14 can specialise business models through packs without changing these core responsibilities.

*Stage 13 · Version 1.0 · 9 September 2026.*
