# Stage 14 — Extension Packs and Pack Authoring

**Version:** 1.0  
**Date:** 9 September 2026  
**Status:** Design complete  
**Branch:** `feat/bootstrap`

## 1. Decision

Extension Packs encode reusable **business-model production grammars**. They specialise core defaults where customer roles, pricing unit, acquisition/sales motion, delivery, retention, economics, cash or experiments materially differ.

A pack is not an industry label, persona, location or aesthetic. The core four skills remain fully usable without a pack.

## 2. Pack contract

A pack declares:

```text
pack_id / version
business-model thesis and applicability
activation cues and non-activation cases
customer/buyer/payer role changes
offer and pricing-unit defaults
acquisition/sales-path implications
delivery/capacity model
retention/repeat/expansion semantics
unit-economics and cash metrics
common assumptions and experiments
quality/failure criteria
professional/legal surfaces to flag
core commands affected
showcase and exact prompt
evals: activation, non-activation, precedence, differential, negative cases
```

Pack fields are defaults and constraints, not fabricated project facts. If a project supplies actual customer, price, channel or economic evidence, that evidence outranks the pack default.

## 3. Precedence

```text
verified legal / regulatory constraints
+ explicit project facts and instructions
→ approved business decisions
→ selected pack specialisation
→ core Business Building defaults
```

A pack cannot make an unlawful tactic acceptable, override an accepted one-off model with a subscription, or replace observed customer evidence with its “typical” buyer.

## 4. Candidate catalogue and qualification

| Candidate | Material specialisation | Decision |
|---|---|---|
| `professional-services` | Buyer/client often same account; scope and human capacity bind; project/retainer pricing; sales-assisted; collection timing and utilisation | **Initial pack** |
| `saas-business` | User/buyer/admin may differ; seat/usage/subscription pricing; activation/usage/support; recurring delivery; software cost and cohort metrics | **Initial pack** |
| `ecommerce-business` | Item/order economics; inventory/fulfilment/returns; checkout; working capital and consumer price/return surfaces | **Initial pack** |
| `marketplace-business` | Multiple sides, matching/liquidity, transaction control, take rate, disputes and principal/agent questions | **Initial pack** |
| `consumer-subscription` | Consumer recurring value, renewal/cancellation, cohort retention, app/direct distribution and heightened consumer-term clarity | **Initial pack** |
| `open-source-commercialisation` | Free adoption versus payer, services/support/education/sponsorship/marketplace options, contributor incentives and adoption tradeoffs | **Initial pack** |
| `creator-digital-product` | Audience-led acquisition, digital fulfilment, one-off/cohort/membership options, refund/support and creator capacity | **Candidate after core proof** |
| `local-service-business` | Geography, appointment capacity, local demand/reviews, repeat/referral and travel/fulfilment constraints | **Candidate after core proof** |
| `consulting-business` | Subset of professional services unless repeated evidence requires distinct IP/productisation/retainer grammar | **Merge initially** |
| `consumer-mobile-subscription` | Consumer-subscription + app-store/platform specialisation | **Defer as nested/derived pack question** |

Six initial catalogue profiles are enough to test distinct grammars without implementing them all at Stage 23. The first implemented pack should be `professional-services` because it directly supports the first vertical.

## 5. Pack authoring workflow

```text
inspect catalogue
→ show why core/existing pack is insufficient
→ research professional practice and counterexamples
→ identify only core behaviours that materially change
→ define economics/cash/capacity semantics
→ define activation and incompatible cases
→ create exact showcase prompt
→ write positive/negative/differential evals
→ compare core vs core+pack
→ validate structure and precedence
→ catalogue with maturity status
```

A pack is accepted only when the same prompt produces a useful, intended specialisation relative to core, without changing explicit facts. “More detailed” is not sufficient differential evidence.

## 6. Example differential: professional services

Core receives: “Design a business model for a solo technical consultant.” Core can produce a valid general service model.

With `professional-services`, the same prompt should additionally make human delivery capacity, non-billable sales/admin time, project/retainer scope, effective rate, payment timing and client concentration first-class. It must **not** invent a subscription, SaaS funnel or 100% utilisation target.

Negative case: a self-serve downloadable template should not activate professional-services merely because its creator is a consultant.

## 7. Packaging

Target later structure:

```text
extension-packs/<pack-id>/
├── PACK.md
├── references/     # only if required
├── examples/
└── evals/
```

The core skill reads the selected pack as contextual production guidance. Do not build a universal pack interpreter service. Deterministic validation can check metadata, references, prompt presence and eval coverage.

## 8. Pack maturity

Use explicit states such as `proposed`, `researched`, `implemented`, `benchmarked`. Catalogue presence must not imply implementation. Stage 18 specification 06 will own the canonical catalogue and status.

## 9. Exit

Packs now have activation, precedence, behavioural-difference, packaging and authoring contracts. They represent reusable business models rather than tags. Stage 15 can choose examples that prove both core breadth and meaningful pack interaction.

*Stage 14 · Version 1.0 · 9 September 2026.*
