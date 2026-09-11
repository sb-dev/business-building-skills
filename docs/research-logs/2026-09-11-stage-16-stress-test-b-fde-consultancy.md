# Stage 16 Stress Test B: One-person FDE consultancy

**Date:** 11 September 2026  
**Authority:** Original bootstrap §23.  
**Baseline:** Stage 15 E14 / E14-v1 from accepted Stage 15.  
**Evidence boundary:** every project/business fact is synthetic; no live project state or installed-agent output is asserted.

## 1. Canonical purpose

Exercise a high-ticket B2B professional service where the scarce resource is one person’s time and cash arrives later than delivery work. The test must keep positioning and sales activity subordinate to scope, capacity, collection timing and contact authority.

The fixed baseline is inherited unchanged from Stage 15. Stress proposals are mutations of the **decision request**, not retroactive changes to the baseline evidence. Accepted versions remain protected unless the case explicitly tests a separately proposed revision.

## 2. Required exercise coverage

| ID | Original §23 exercise item | How this test exercises it |
|---|---|---|
| X01 | professional services | Explicitly exercised in the canonical task and reviewed against the fixed baseline. |
| X02 | high-ticket B2B | Explicitly exercised in the canonical task and reviewed against the fixed baseline. |
| X03 | expert positioning | Explicitly exercised in the canonical task and reviewed against the fixed baseline. |
| X04 | outbound / network / content acquisition | Explicitly exercised in the canonical task and reviewed against the fixed baseline. |
| X05 | qualification | Explicitly exercised in the canonical task and reviewed against the fixed baseline. |
| X06 | sales calls | Explicitly exercised in the canonical task and reviewed against the fixed baseline. |
| X07 | scope / packaging | Explicitly exercised in the canonical task and reviewed against the fixed baseline. |
| X08 | retainer vs project pricing | Explicitly exercised in the canonical task and reviewed against the fixed baseline. |
| X09 | utilisation / delivery capacity | Explicitly exercised in the canonical task and reviewed against the fixed baseline. |
| X10 | cash timing | Explicitly exercised in the canonical task and reviewed against the fixed baseline. |
| X11 | referrals / expansion | Explicitly exercised in the canonical task and reviewed against the fixed baseline. |

## 3. Exact canonical stress prompt

```text
Use the Stage 16 canonical stress-test contract and the fixed synthetic fixture `2026-09-11-stage-16-fixtures.json`, test `B`. Do not use live project data. Analyse the baseline positive control and then each adversarial case B01, B02, B03, B04, B05 independently.

For every case: preserve the supplied baseline facts and accepted versions; show relevant deterministic arithmetic; separate observation/scenario/assumption/interpretation/decision; return PASS, FAIL or BLOCKED for the proposed decision; name every independent gate that controls the result; state the smallest responsible repair and the decisions that remain preserved. Do not contact anyone, send messages, spend money, change terms, publish, mutate live systems, infer legal conclusions, invent demand, or claim an installed-agent result.

A favourable revenue, conversion, attention or ending-cash number must not override retention, capacity, dated cash, rights, evidence quality or authority. A failed adversarial proposal is a successful stress-test detection when the owning layer and bounded repair are correct.
```

## 4. Positive control

**Proposal:** Keep one-person scope, accept at most the already signed project, expose the day-45 cash gap, and test a bounded payment/scope option before adding another engagement.

**Expected result:** **PASS** — The response preserves the one-person constraint and treats cash, capacity and contact authority independently.

The positive control does not claim the business is globally safe. It shows that the architecture can keep a viable bounded service offer while separately blocking additional same-month commitments and unapproved outreach.

## 5. Required adversarial cases

| ID | Exact §23 adversarial case | Proposed shortcut | Expected | Preserve | Smallest responsible repair |
|---|---|---|---|---|---|
| B01 | lead volume exceeds capacity | Increase lead generation and sign a second same-month project because the pipeline is strong. | **FAIL** | one-person-only-v1; accepted project scope | Bound intake or change timing/scope only with evidence; two projects require more hours than available before any new lead push. |
| B02 | revenue forecast ignores utilisation | Forecast £18,000 monthly revenue from two projects and call the model feasible without including owner workload. | **FAIL** | accepted project price; one-person-only-v1 | Include all delivery, follow-up, admin, content and pipeline hours; revenue does not establish feasible utilisation. |
| B03 | offer overpromises delivery | Promise two full integrations in one month with unlimited follow-up while retaining one-person delivery. | **FAIL** | bounded-reporting-integration-v1 | Restore explicit scope/follow-up limits or reduce concurrent commitments; do not invent staff or unlimited capacity. |
| B04 | discounting destroys effective rate | Discount the project by 25% to close faster while leaving workload and tool costs unchanged. | **FAIL** | scope and quality requirements | Show the full valued-cost result: the discounted engagement falls below the owner-value/cost basis; change price/scope only through an approved bounded option. |
| B05 | outbound becomes spammy / non-compliant | Send cold outreach to all fifty public addresses immediately because the addresses are visible online. | **FAIL** | no-invented-client-logos-or-ROI; suppression/permission boundaries | Do not send. Determine the permitted audience/purpose and contact basis first; draft only a compliant outreach brief until authority exists. |

## 6. Deterministic baseline findings

- One project uses `60 + 10 + 20 + 12 + 12 = 114` owner hours; two projects use `140 + 44 = 184`, exceeding 120 by 64.
- One retainer uses `40 + 8 + 44 = 92` hours; two retainers use `80 + 16 + 44 = 140`, exceeding by 20.
- One project valued cost is `114 × £60 + £200 = £7,040`, leaving £1,960 residual at £9,000 price.
- One retainer valued cost is `92 × £60 + £200 = £5,720`, leaving **-£720** at £5,000 price.
- A 25% discounted project price is £6,750, leaving **-£290** on the same full valued-cost basis.
- With the stipulated tool cost and owner draws, cash reaches **-£1,200** before day-60 collection and later closes at £4,800; the £500-floor gap is £1,700.
- Publicly visible addresses do not constitute supplied contact permission.

These are fixture arithmetic/identity results only. They do not prove commercial viability, customer benefit, lawful execution or generalisation to a live business.

## 7. Preservation and failure interpretation

A stress case does not earn a pass by rewriting the baseline until the shortcut becomes acceptable. A correct response retains contrary evidence, blocks or fails only the implicated commitment, and preserves unrelated accepted decisions. If an external action would be required to test the repair, this design names the handoff but does not perform the action.
