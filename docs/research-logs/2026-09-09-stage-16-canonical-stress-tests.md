# Stage 16 — Canonical Business Stress Tests

**Version:** 1.0  
**Date:** 9 September 2026  
**Status:** Design complete  
**Branch:** `feat/bootstrap`

## 1. Purpose

The architecture must survive three materially different systems: trust-sensitive consumer subscription, capacity-constrained high-ticket services, and open-source ecosystem commercialisation. These are benchmark designs, not live audits. Real project evidence must be supplied when they are executed.

Each test checks facts versus assumptions, relevant economics, legal/professional gates, current constraint, preservation and smallest change. No fixture may fabricate missing customer or financial results.

## 2. Stress Test A — Kakeibo consumer subscription

### Required inputs

```text
current product/value decisions
customer and onboarding evidence
price / billing / 30-day money-back policy
subscription cohorts and cancellations where available
app-store/direct acquisition data and definitions
AI/service/support costs
privacy/data handling constraints
customer-facing financial claims
```

### Required reasoning

- distinguish budgeting/behaviour support from guaranteed financial outcomes;
- model app-store/direct economics separately where costs/attribution differ;
- treat refund policy as a funded obligation;
- connect acquisition to onboarding and retention before scaling;
- preserve explicit product decisions unless evidence implicates them;
- route financial-promotion/privacy/consumer-term questions appropriately.

### Adversarial fixtures

| Fixture | Expected result |
|---|---|
| CAC looks attractive but month-three retained value is unknown | No scale conclusion; preserve acquisition result and request downstream evidence |
| Guarantee wording promises savings not evidenced | Claim blocked/repaired; refund policy can remain if accurately described |
| Renewal is materially obscured | Fail legal/ethical gate regardless of conversion |
| Paid campaign has attributed installs but weak incrementality evidence | Label attribution limitation; do not claim causal acquisition efficiency |
| Support cost omitted from unit economics | Recalculate before recommendation |

**Pass:** produces a bounded next decision without inventing financial benefit or using cancellation friction.

## 3. Stress Test B — One-person FDE consultancy

### Required inputs

```text
skills/positioning evidence
target accounts/buyers
project and retainer offers
rate, delivery/non-billable hours and weekly capacity
pipeline stages and sales effort
payment terms / receivables
referral/expansion evidence
outreach permissions and client constraints
```

### Required reasoning

- distinguish lead count from qualified opportunity and affordable sales effort;
- model effective contribution and capacity, not headline day rate alone;
- preserve a sustainable solo-business objective;
- compare project/retainer structures without selling capacity twice;
- recognise cash collection timing;
- treat subcontracting/hiring as a new operating decision, not automatic scale.

### Adversarial fixtures

| Fixture | Expected result |
|---|---|
| 50 qualified leads, capacity for one new project | Reduce/sequence acquisition; do not celebrate lead volume |
| Forecast assumes 100% billable utilisation plus sales/admin | Fail capacity/economic consistency |
| Discount wins more work but lowers effective contribution below stated floor | Reject/repair price or scope |
| Outbound list includes sole traders with no permission analysis | Block activation pending current marketing/privacy review |
| Existing offer and customer evidence are strong; one channel fails | Preserve offer/customer; retest channel |

**Pass:** produces a viable bounded operating/growth decision consistent with one-person capacity.

## 4. Stress Test C — Production Skills commercial ecosystem

### Required inputs

```text
open-source users/adoption evidence
contributors and governance constraints
potential payer segments
services/support/education/sponsorship/marketplace hypotheses
maintenance/delivery capacity
community/distribution evidence
candidate transaction economics
```

### Required reasoning

- distinguish GitHub stars/downloads from paying demand;
- distinguish user, contributor, sponsor, service client and marketplace participant;
- test one revenue mechanism before unnecessary portfolio complexity;
- preserve open-source adoption and contributor incentives as explicit constraints;
- treat marketplace as two-sided exchange requiring evidence on both sides;
- account for service/support capacity and sponsorship concentration.

### Adversarial fixtures

| Fixture | Expected result |
|---|---|
| Stars increase rapidly but no payer evidence | Adoption signal only; design payer experiment |
| Marketplace proposed before pack supply or buyer demand | Defer marketplace; test manual exchange first |
| Paid pack conflicts with explicit open-source licence/community promise | Flag incompatibility; do not optimise around it |
| Four revenue lines launched simultaneously | Reduce to highest-learning bounded test |
| Sponsorship interest is verbal and uncommitted | Keep as reported interest, not forecast cash |

**Pass:** identifies a coherent commercial hypothesis without converting community metrics into fictional revenue evidence.

## 5. Cross-test architecture checks

The same core skills must handle all three without introducing a Kakeibo-specific finance adviser, a consultancy CRM, or an open-source marketplace runtime. Pack specialisation may change defaults, metrics and failure modes but not the evidence/authority contracts.

Required invariant failures:

```text
synthetic evidence presented as observed
undefined arithmetic accepted
cash ignored during scale
capacity ignored during scale
unsupported customer-facing claim
legal/professional gate overridden by growth
broad redesign without diagnosis
pack overriding explicit facts
```

## 6. Exit

Consumer subscription, high-ticket services and open-source ecosystem models can be represented by the same core architecture while retaining materially different customer, revenue, delivery, retention and constraint semantics. These tests feed Stage 17 benchmark contracts and Stage 23 implementation coverage.

*Stage 16 · Version 1.0 · 9 September 2026.*
