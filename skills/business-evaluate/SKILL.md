---
name: business-evaluate
description: Audit business evidence, offers, acquisition, economics, cash and experiments; diagnose the current constraint; and recommend the smallest responsible change while preserving still-supported decisions.
license: Apache-2.0
compatibility: Provider-neutral. Requires Python 3.11+ only for bundled deterministic validation; can consume exported data from external systems.
---

# Business Evaluate

Diagnose before redesigning.

## Workflow

1. Identify objective, accepted decisions and failing observation.
2. Audit evidence classification/provenance and metric definitions.
3. Recompute decision-driving arithmetic where relevant using `business-build` output or supplied exports.
4. Check offer/delivery/economics/cash/experiment consistency.
5. List competing causes with supporting/contradicting evidence.
6. Name a binding constraint only when supported.
7. Recommend the smallest mutation and state what remains preserved.

## Rules

Unknown, insufficient evidence and not-applicable are distinct. A lowest metric is not automatically the constraint. An invalid experiment is inconclusive. Truthfulness, authority and arithmetic errors are gates, not dimensions to average away.

## Commands

The initial implemented vertical provides `audit-evidence`, `evaluate-offer-economics`, `evaluate-experiment`, `diagnose-constraint`, and `recommend-smallest-change`. Remaining growth/claims commands are expanded at Stage 23.

Read `references/evaluation.md` for the compact rubric.
