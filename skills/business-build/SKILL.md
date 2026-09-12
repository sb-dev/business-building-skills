---
name: business-build
description: Build a coherent, evidence-backed business proposition from an opportunity through customer/value, offer/pricing, delivery/economics and a falsifiable next experiment. Use for new offers, new business models, pricing/monetisation design or a bounded new commercial proposition.
license: Apache-2.0
compatibility: Provider-neutral. Requires Python 3.11+ only for the bundled deterministic economics script; external research, billing, CRM or messaging tools are optional.
---

# Business Build

Turn a business opportunity into a testable commercial system without inventing market evidence.

## Activation

Use for greenfield opportunities, new offers/segments, pricing or monetisation decisions, and bounded commercial experiments. For an existing-business failure whose current system is already defined, prefer `business-evaluate` first.

## Evidence contract

Every decision-relevant claim is `observed`, `reported`, `derived`, `assumed`, or `synthetic`. Preserve source/window/scope and limitations. Synthetic fixtures never become observed customer evidence.

## Workflow

1. **Frame** — state the decision, owner objective, horizon, constraints, known facts and consequential unknowns.
2. **Customer/value** — distinguish target, observed customer, buyer/user/payer/approver; record problem, alternatives, supported value and proof.
3. **Offer** — define controlled deliverable versus uncertain outcome, scope/exclusions, time-to-value, price, payment, obligations/remedies and claim evidence.
4. **Delivery/economics** — define unit, capacity, work/unit, relevant costs, contribution and dated cash assumptions. Use `scripts/economics.py` for arithmetic when applicable.
5. **Assumptions** — identify the uncertainty that could materially change the next commitment; uncertainty and consequence stay separate.
6. **Experiment** — choose the cheapest adequate honest test; define population/unit, signal/denominator, success, failure, inconclusive and stop conditions.
7. **Brief** — preserve accepted decisions, evidence references, unresolved blockers and the bounded next action.

Read [`references/contracts.md`](references/contracts.md) for the compact artefact and experiment contracts.

## Commands

Command files in `commands/` are bounded reusable operations. Use only those needed; do not run every command mechanically.

## Approval and professional gates

Drafting and analysis do not authorise publication, customer contact, spend, contract changes or data collection. Block unsupported claims, fake scarcity/testimonials and hidden material terms. Route legal/tax/regulated conclusions to the relevant specialist.

## Failure behaviour

Unknown calculation input → expose unknown/sensitivity, not a fabricated value. Missing customer evidence → label hypothesis. Provider absent → produce manual handoff. Contradictory evidence → preserve conflict and request/perform resolution. Existing accepted decision → change only when evidence implicates it.

## Output

Produce a concise evidence-linked business brief and next commitment. Do not claim market validation merely because the brief is coherent.
