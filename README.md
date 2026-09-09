# Business Building Skills

**Status:** Specified and scaffolded. Core skills are not yet proven by executed benchmarks.

Turn business ideas and operating problems into evidence-backed offers, acquisition systems and viable economic decisions.

This repository is an open-source Agent Skills project for forming, testing, growing and repairing businesses without treating persuasive tactics, vanity metrics or generated assumptions as evidence.

## What it is designed to do

- frame customers, problems and value from traceable evidence;
- design deliverable offers, pricing and monetisation;
- model delivery, unit economics, capacity and cash;
- select acquisition and sales hypotheses using downstream quality;
- design falsifiable business experiments;
- diagnose constraints and preserve still-supported decisions;
- specialise behaviour through business-model Extension Packs.

## Evidence and commitment model

Facts, assumptions and synthetic fixtures stay distinct. Arithmetic is deterministic where appropriate. External writes require explicit authority. Legal, tax and regulated conclusions are handed to the relevant specialist. Growth cannot override truthfulness, delivery capacity or cash constraints.

## Installation target

The repository follows the standard multi-skill layout used by the Agent Skills ecosystem. After Stage 24 validates clean installation, the intended commands are:

```bash
npx skills add https://github.com/sb-dev/business-building-skills --list
npx skills add https://github.com/sb-dev/business-building-skills --skill business-build
npx skills add https://github.com/sb-dev/business-building-skills --skill business-grow
npx skills add https://github.com/sb-dev/business-building-skills --skill business-evaluate
npx skills add https://github.com/sb-dev/business-building-skills --skill business-pack-author
```

These commands are documented as the target installation path, not yet a Stage 24 installation result.

## Learn by Building

The progressive example design contains five levels × three primary examples with exact prompts. The first implementation target is a bounded professional-service pricing/economics decision. See [Stage 15](docs/research-logs/2026-09-09-stage-15-progressive-examples.md).

## Core skills

| Skill | Responsibility |
|---|---|
| `business-build` | Opportunity → customer/value → offer/pricing → delivery/economics → experiment |
| `business-grow` | Channel → acquisition → sales/conversion → retention/expansion → bounded scale |
| `business-evaluate` | Evidence/economics audit → experiment review → constraint → smallest change |
| `business-pack-author` | Research and validate reusable business-model Extension Packs |

## Extension Packs

The initial researched catalogue includes professional services, SaaS, ecommerce, marketplaces, consumer subscriptions and open-source commercialisation. Catalogue presence does not mean a pack is implemented. See [pack contract](docs/05-business-building-customisation-packs-spec.md) and [catalogue](docs/06-business-building-extension-pack-catalogue.md).

## Execution boundary

Use existing CRM, messaging, ads, analytics, billing, accounting, forms and scheduling systems for their state and side effects. Business Building Skills owns the business judgement connecting them. Provider accounts are optional; a human-readable handoff remains valid.

## Evaluation

The benchmark design separates deterministic calculations, business reasoning, preservation, adversarial behaviour, pack differentials and clean installation. No benchmark score is claimed until an agent has actually executed the cases. See [testing specification](docs/04-testing-and-benchmark-spec.md).

## Canonical stress tests

Architecture is tested against three deliberately different models: Kakeibo consumer subscription, one-person FDE consultancy and the Production Skills open-source commercial ecosystem. These are designed stress tests, not completed benchmark results.

## Source lineage

The initial corpus is *$100M Offers*, *$100M Leads*, *$100M Money Models*, *The Personal MBA* and *The Lean Startup*. The repository encodes independently expressed capabilities rather than book-shaped prompts. Stage 2 records exactly which source material was accessible and the remaining full-book gaps.

## Documentation

- [System](docs/01-business-building-skills-system-spec.md)
- [Workflows and artefacts](docs/02-business-building-skills-workflows-and-artifacts-spec.md)
- [Repository and contracts](docs/03-business-building-skills-repository-and-contracts-spec.md)
- [Testing and benchmark](docs/04-testing-and-benchmark-spec.md)
- [Extension Pack contract](docs/05-business-building-customisation-packs-spec.md)
- [Extension Pack catalogue](docs/06-business-building-extension-pack-catalogue.md)
- [Bootstrap research](docs/research-logs/README.md)

## Boundary

This is not a CRM, marketing automation platform, accounting package, payment processor, legal/tax/investment-advice system, market-data vendor or autonomous executive team.

## Contributing and licence

See [CONTRIBUTING.md](CONTRIBUTING.md). Apache-2.0; see [LICENSE](LICENSE).
