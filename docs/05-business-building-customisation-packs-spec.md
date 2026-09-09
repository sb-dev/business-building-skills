# Business Building Skills — Customisation / Extension Packs Specification

**Version:** 1.0 · **Status:** Target pack contract · **Date:** 9 September 2026

## Purpose

Extension Packs specialise core Business Building behaviour for reusable business-model grammars. Core works without packs. Packs are not industry labels, themes, personas or provider integrations.

## Pack dimensions

A valid pack may change defaults for customer/buyer/payer structure, offer grammar, pricing unit, monetisation, acquisition priorities, sales path, delivery/capacity, continued value, unit economics, cash behaviour, assumptions/experiments and quality criteria.

## Precedence

```text
verified legal/regulatory constraints
+ explicit project facts/instructions
→ approved business decisions
→ selected pack
→ core defaults
```

Pack defaults never fabricate facts or override a reviewed constraint.

## Activation

Activation requires a project fact/instruction or an explicitly selected pack. Similar vocabulary alone is insufficient. Each pack defines positive cues, negative/incompatible cases and what happens when applicability is uncertain.

## Integration

PACK.md identifies affected core commands and only the behaviour that changes. The core skill consumes pack context; no universal pack interpreter service is required.

## Packaging

```text
extension-packs/<id>/
├── PACK.md
├── references/     # optional
├── examples/
└── evals/
```