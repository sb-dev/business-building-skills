# Stage 14: Fixed design probes and comparison method

**Date:** 10 September 2026  
**Branch:** `feat/bootstrap-2`  
**Authority:** Original bootstrap §21; [pack model](2026-09-10-stage-14-pack-model.md), [catalogue](2026-09-10-stage-14-candidate-catalogue.md), [authoring contract](2026-09-10-stage-14-pack-authoring.md).

## 1. Method and frozen criteria

All businesses, people, amounts, observations, permissions and outcomes below are **synthetic**. They are original stipulated cases, not customer research, a trial of a live business or installed-agent output. The Python verifier performs a bounded **deterministic design projection**: both conditions calculate the same common economic/resource report from the same fixed facts; the second condition additionally returns named mechanism-specific checks. This tests the proposed decomposition, arithmetic and preservation contract. It does not test whether an LLM following a pack actually produces better reasoning.

The core-only condition is not deprived of any facts or safeguards. It can correctly identify all economic and operational failures, and a competent agent may infer the specialised questions without a pack. Consequently the comparison does not claim superiority, token savings, causal business benefit or installed-pack validation. The specialised fields demonstrate concrete distinctions worth testing in later host evaluations, not proof of future performance. Those actual installed paired runs remain mandatory when the implementation stage requires them.

Before running the checks, the acceptance rules are: the common report must be identical between conditions; input and accepted-version fingerprints must remain unchanged; each named specialised calculation/state must match the specified fixture facts; no external action or scale approval is granted; all nine candidates including the merged advisory mode are exercised; invalid, missing and incompatible inputs must not become favourable values. Numbers are currency amounts in GBP only within these invented cases. Direct contribution is not statutory profit. A scenario includes labelled future costs, not fabricated observed payments.

Each exact task below is run under two declared conditions: **core-only at the stated core contract version**, and **core-plus the named candidate design at 2026-09-10**. PK04 is the catalogue reference for the professional-services advisory mode, not an independently installed pack. The task text and input record do not change. No shell/slash command for an unimplemented skill is asserted. The local reproduction command is:

```bash
python docs/research-logs/2026-09-10-stage-14-verifier.py /path/to/workspace
```

## 2. Exact copyable tasks

### S01 — PK01

```text
Assess the supplied two-account hosted-service cohort and metering reconciliation. Preserve accepted versions. Report account and aggregate contribution, mismatched usage units and what remains unknown before growth; do not change pricing or perform billing.
```

Use the exact same-ID input record in §3 under both declared conditions.

### S02 — PK02

```text
Assess this mobile subscription renewal cohort. Separate paid renewal, entitlement and meaningful use, reconcile net contribution and cash timing, and preserve all current access rights. Do not send messages, revoke access or recommend scale from billing alone.
```

Use the exact same-ID input record in §3 under both declared conditions.

### S03 — PK03

```text
Assess two fixed-fee professional engagements against shared human capacity. Include delivery, non-billable time and all supplied costs. Distinguish a profitable comparison from feasible intake; preserve the accepted customer, price and scope.
```

Use the exact same-ID input record in §3 under both declared conditions.

### S04 — PK04

```text
Assess the advisory engagement using the professional-services advisory mode. A report has been delivered but client acceptance is false, adoption and realised impact are unknown. Separate these findings and cost from the client outcome; do not claim ROI or acceptance.
```

Use the exact same-ID input record in §3 under both declared conditions.

### S05 — PK05

```text
Assess the goods cohort and stock-funded growth proposal. Reconcile sold, committed and available quantities, nonrecoverable returns, direct contribution and the lowest dated usable cash. Do not equate stock purchase cash with the cost of goods consumed or auto-order inventory.
```

Use the exact same-ID input record in §3 under both declared conditions.

### S06 — PK06

```text
Assess the intermediary marketplace, keeping own fees separate from transaction value and third-party funds. Compute request matching and usable cash before and after already-restricted funds settle. Preserve unmet demand; no invented network effects or live transfers.
```

Use the exact same-ID input record in §3 under both declared conditions.

### S07 — PK07

```text
Assess the digital-product promise over the full supplied horizon, including creation and promised updates/support. Existing buyers retain access to their purchased edition; a proposed edition change must not delete that right. No publishing or licence revocation is authorised.
```

Use the exact same-ID input record in §3 under both declared conditions.

### S08 — PK08

```text
Assess the supplied open-source commercial scenario, with support and sponsorship obligations. Keep adopters, contributors, payers and repository attention distinct. Show the recurring maintenance funding gap without treating stars as customers or withdrawing existing open-source rights.
```

Use the exact same-ID input record in §3 under both declared conditions.

### S09 — PK09

```text
Assess five local-service visits including travel and setup. Compare full resource time with the supplied day and calculate direct contribution. A favourable margin is not a feasible route or appointment plan; preserve the accepted offer and do not schedule visits.
```

Use the exact same-ID input record in §3 under both declared conditions.

## 3. Fixed inputs

Empty cash-event arrays mean **no cash schedule was supplied**, not zero obligations or cash feasibility. The shared capacity record is an arithmetic bound, not a verified schedule. Hypothetical consideration in the unaccepted advisory engagement is not a recognised invoice or collected cash. In S05, all four returned items are stipulated unsaleable; there is no return-to-stock recovery, and the stock-purchase cash covers ten ending units as well as the sold units. In S06, the usable-cash schedule excludes seller funds and separately restricts the refund reserve; settling those already restricted amounts must not subtract them from usable cash again. S07 includes a future-update cost scenario, not an observed update expense. S08's sponsorship is stipulated consideration for defined sponsor deliverables, not a generic assumption about donations, grants or accounting recognition.

<!-- FIXTURES BEGIN -->
```json
[
  {
    "id": "S01",
    "synthetic": true,
    "pack": "PK01",
    "core_contract": "stage-13@475f63b061b04bb1e7cb2616b1d39539473e25bf",
    "pack_design": "2026-09-10",
    "prompt": "Assess the supplied two-account hosted-service cohort and metering reconciliation. Preserve accepted versions. Report account and aggregate contribution, mismatched usage units and what remains unknown before growth; do not change pricing or perform billing.",
    "currency": "GBP",
    "period": "2026-01-01/2026-01-31",
    "gross": "200",
    "discount": "0",
    "refund": "0",
    "costs": [
      {
        "id": "account-a",
        "amount": "30"
      },
      {
        "id": "account-b",
        "amount": "130"
      }
    ],
    "opening_usable_cash": "0",
    "cash_events": [],
    "resources": [],
    "facts": {
      "account_net": [
        "100",
        "100"
      ],
      "account_cost": [
        "30",
        "130"
      ],
      "consumed_units": 15000,
      "billable_units": 12000,
      "invoiced_units": 11000
    },
    "accepted": {
      "customer": "segment-v1",
      "offer": "offer-v1",
      "price": "price-v1",
      "rights": "rights-v1"
    },
    "growth_gate_evidence": "incomplete; no scale approval",
    "allowed_external_actions": []
  },
  {
    "id": "S02",
    "synthetic": true,
    "pack": "PK02",
    "core_contract": "stage-13@475f63b061b04bb1e7cb2616b1d39539473e25bf",
    "pack_design": "2026-09-10",
    "prompt": "Assess this mobile subscription renewal cohort. Separate paid renewal, entitlement and meaningful use, reconcile net contribution and cash timing, and preserve all current access rights. Do not send messages, revoke access or recommend scale from billing alone.",
    "currency": "GBP",
    "period": "2026-01-01/2026-01-31",
    "gross": "900",
    "discount": "0",
    "refund": "20",
    "costs": [
      {
        "id": "platform-charge",
        "amount": "90"
      },
      {
        "id": "service",
        "amount": "80"
      }
    ],
    "opening_usable_cash": "0",
    "cash_events": [
      {
        "id": "service-out",
        "date": "2026-01-10",
        "amount": "-80"
      },
      {
        "id": "net-settlement",
        "date": "2026-01-20",
        "amount": "790"
      }
    ],
    "resources": [],
    "facts": {
      "eligible": 100,
      "paid": 90,
      "entitled": 95,
      "meaningful_use": 60
    },
    "accepted": {
      "customer": "segment-v1",
      "offer": "offer-v1",
      "price": "price-v1",
      "rights": "rights-v1"
    },
    "growth_gate_evidence": "incomplete; no scale approval",
    "allowed_external_actions": []
  },
  {
    "id": "S03",
    "synthetic": true,
    "pack": "PK03",
    "core_contract": "stage-13@475f63b061b04bb1e7cb2616b1d39539473e25bf",
    "pack_design": "2026-09-10",
    "prompt": "Assess two fixed-fee professional engagements against shared human capacity. Include delivery, non-billable time and all supplied costs. Distinguish a profitable comparison from feasible intake; preserve the accepted customer, price and scope.",
    "currency": "GBP",
    "period": "2026-01-01/2026-01-31",
    "gross": "1000",
    "discount": "0",
    "refund": "0",
    "costs": [
      {
        "id": "delivery-labour",
        "amount": "600"
      },
      {
        "id": "shared-labour",
        "amount": "120"
      },
      {
        "id": "other",
        "amount": "80"
      }
    ],
    "opening_usable_cash": "0",
    "cash_events": [],
    "resources": [
      {
        "id": "consultant",
        "available": "22",
        "shared": "4",
        "required": "20"
      }
    ],
    "facts": {
      "delivery_hours": [
        "8",
        "12"
      ],
      "nonbillable_hours": "4"
    },
    "accepted": {
      "customer": "segment-v1",
      "offer": "offer-v1",
      "price": "price-v1",
      "rights": "rights-v1"
    },
    "growth_gate_evidence": "incomplete; no scale approval",
    "allowed_external_actions": []
  },
  {
    "id": "S04",
    "synthetic": true,
    "pack": "PK04",
    "core_contract": "stage-13@475f63b061b04bb1e7cb2616b1d39539473e25bf",
    "pack_design": "2026-09-10",
    "prompt": "Assess the advisory engagement using the professional-services advisory mode. A report has been delivered but client acceptance is false, adoption and realised impact are unknown. Separate these findings and cost from the client outcome; do not claim ROI or acceptance.",
    "currency": "GBP",
    "period": "2026-01-01/2026-01-31",
    "gross": "1000",
    "discount": "0",
    "refund": "0",
    "costs": [
      {
        "id": "advisory-labour",
        "amount": "600"
      }
    ],
    "opening_usable_cash": "0",
    "cash_events": [],
    "resources": [],
    "facts": {
      "report_delivered": true,
      "client_acceptance": false,
      "adoption": null,
      "realised_impact": null,
      "milestone_requires_acceptance": true
    },
    "accepted": {
      "customer": "segment-v1",
      "offer": "offer-v1",
      "price": "price-v1",
      "rights": "rights-v1"
    },
    "growth_gate_evidence": "incomplete; no scale approval",
    "allowed_external_actions": []
  },
  {
    "id": "S05",
    "synthetic": true,
    "pack": "PK05",
    "core_contract": "stage-13@475f63b061b04bb1e7cb2616b1d39539473e25bf",
    "pack_design": "2026-09-10",
    "prompt": "Assess the goods cohort and stock-funded growth proposal. Reconcile sold, committed and available quantities, nonrecoverable returns, direct contribution and the lowest dated usable cash. Do not equate stock purchase cash with the cost of goods consumed or auto-order inventory.",
    "currency": "GBP",
    "period": "2026-01-01/2026-01-31",
    "gross": "1000",
    "discount": "0",
    "refund": "200",
    "costs": [
      {
        "id": "goods-consumed",
        "amount": "400"
      },
      {
        "id": "outbound",
        "amount": "100"
      },
      {
        "id": "returns-handling",
        "amount": "20"
      }
    ],
    "opening_usable_cash": "100",
    "cash_events": [
      {
        "id": "stock-purchase",
        "date": "2026-01-01",
        "amount": "-600"
      },
      {
        "id": "outbound-cash",
        "date": "2026-01-02",
        "amount": "-100"
      },
      {
        "id": "return-cash",
        "date": "2026-01-03",
        "amount": "-20"
      },
      {
        "id": "collections",
        "date": "2026-01-10",
        "amount": "1000"
      },
      {
        "id": "refunds",
        "date": "2026-01-15",
        "amount": "-200"
      }
    ],
    "resources": [],
    "facts": {
      "received_units": 30,
      "sold_units": 20,
      "returned_unsaleable": 4,
      "ending_physical": 10,
      "committed": 2,
      "recoverable_returns": 0
    },
    "accepted": {
      "customer": "segment-v1",
      "offer": "offer-v1",
      "price": "price-v1",
      "rights": "rights-v1"
    },
    "growth_gate_evidence": "incomplete; no scale approval",
    "allowed_external_actions": []
  },
  {
    "id": "S06",
    "synthetic": true,
    "pack": "PK06",
    "core_contract": "stage-13@475f63b061b04bb1e7cb2616b1d39539473e25bf",
    "pack_design": "2026-09-10",
    "prompt": "Assess the intermediary marketplace, keeping own fees separate from transaction value and third-party funds. Compute request matching and usable cash before and after already-restricted funds settle. Preserve unmet demand; no invented network effects or live transfers.",
    "currency": "GBP",
    "period": "2026-01-01/2026-01-31",
    "gross": "40",
    "discount": "0",
    "refund": "0",
    "costs": [
      {
        "id": "platform-operations",
        "amount": "20"
      }
    ],
    "opening_usable_cash": "100",
    "cash_events": [
      {
        "id": "own-fee-receipt",
        "date": "2026-01-10",
        "amount": "40"
      },
      {
        "id": "operating-payment",
        "date": "2026-01-11",
        "amount": "-20"
      },
      {
        "id": "restrict-refund-reserve",
        "date": "2026-01-12",
        "amount": "-20"
      }
    ],
    "resources": [],
    "facts": {
      "eligible_requests": 10,
      "matched_requests": 4,
      "transaction_value": "400",
      "bank_after_operations": "480",
      "seller_funds": "360",
      "refund_reserve": "20"
    },
    "accepted": {
      "customer": "segment-v1",
      "offer": "offer-v1",
      "price": "price-v1",
      "rights": "rights-v1"
    },
    "growth_gate_evidence": "incomplete; no scale approval",
    "allowed_external_actions": []
  },
  {
    "id": "S07",
    "synthetic": true,
    "pack": "PK07",
    "core_contract": "stage-13@475f63b061b04bb1e7cb2616b1d39539473e25bf",
    "pack_design": "2026-09-10",
    "prompt": "Assess the digital-product promise over the full supplied horizon, including creation and promised updates/support. Existing buyers retain access to their purchased edition; a proposed edition change must not delete that right. No publishing or licence revocation is authorised.",
    "currency": "GBP",
    "period": "2026-01-01/2026-01-31",
    "gross": "500",
    "discount": "0",
    "refund": "0",
    "costs": [
      {
        "id": "creation",
        "amount": "300"
      },
      {
        "id": "platform",
        "amount": "50"
      },
      {
        "id": "support",
        "amount": "80"
      },
      {
        "id": "promised-updates-scenario",
        "amount": "60"
      }
    ],
    "opening_usable_cash": "350",
    "cash_events": [
      {
        "id": "creation-cash",
        "date": "2026-01-01",
        "amount": "-300"
      },
      {
        "id": "sales-cash",
        "date": "2026-01-10",
        "amount": "500"
      },
      {
        "id": "platform-cash",
        "date": "2026-01-11",
        "amount": "-50"
      },
      {
        "id": "support-cash",
        "date": "2026-01-12",
        "amount": "-80"
      },
      {
        "id": "updates-scenario-cash",
        "date": "2026-01-31",
        "amount": "-60"
      }
    ],
    "resources": [],
    "facts": {
      "sales": 10,
      "existing_access_promised": true,
      "proposed_access_removal": true,
      "future_update_cost_is_scenario": true
    },
    "accepted": {
      "customer": "segment-v1",
      "offer": "offer-v1",
      "price": "price-v1",
      "rights": "rights-v1"
    },
    "growth_gate_evidence": "incomplete; no scale approval",
    "allowed_external_actions": []
  },
  {
    "id": "S08",
    "synthetic": true,
    "pack": "PK08",
    "core_contract": "stage-13@475f63b061b04bb1e7cb2616b1d39539473e25bf",
    "pack_design": "2026-09-10",
    "prompt": "Assess the supplied open-source commercial scenario, with support and sponsorship obligations. Keep adopters, contributors, payers and repository attention distinct. Show the recurring maintenance funding gap without treating stars as customers or withdrawing existing open-source rights.",
    "currency": "GBP",
    "period": "2026-01-01/2026-01-31",
    "gross": "3000",
    "discount": "0",
    "refund": "0",
    "costs": [
      {
        "id": "paid-support",
        "amount": "1800"
      },
      {
        "id": "maintenance",
        "amount": "1200"
      }
    ],
    "opening_usable_cash": "0",
    "cash_events": [],
    "resources": [],
    "facts": {
      "support_consideration": "2000",
      "sponsorship_consideration": "1000",
      "secured_recurring_maintenance_funding": "500",
      "monthly_maintenance_need": "1000",
      "adopters": 1000,
      "contributors": 20,
      "payers": 3,
      "stars": 5000,
      "existing_open_source_rights": true
    },
    "accepted": {
      "customer": "segment-v1",
      "offer": "offer-v1",
      "price": "price-v1",
      "rights": "rights-v1"
    },
    "growth_gate_evidence": "incomplete; no scale approval",
    "allowed_external_actions": []
  },
  {
    "id": "S09",
    "synthetic": true,
    "pack": "PK09",
    "core_contract": "stage-13@475f63b061b04bb1e7cb2616b1d39539473e25bf",
    "pack_design": "2026-09-10",
    "prompt": "Assess five local-service visits including travel and setup. Compare full resource time with the supplied day and calculate direct contribution. A favourable margin is not a feasible route or appointment plan; preserve the accepted offer and do not schedule visits.",
    "currency": "GBP",
    "period": "2026-01-01/2026-01-31",
    "gross": "300",
    "discount": "0",
    "refund": "0",
    "costs": [
      {
        "id": "full-cycle-labour",
        "amount": "120"
      }
    ],
    "opening_usable_cash": "0",
    "cash_events": [],
    "resources": [
      {
        "id": "operator-day",
        "available": "360",
        "shared": "0",
        "required": "400"
      }
    ],
    "facts": {
      "visits": 5,
      "service_minutes": 45,
      "travel_minutes": 25,
      "setup_minutes": 10,
      "labour_per_minute": "0.30"
    },
    "accepted": {
      "customer": "segment-v1",
      "offer": "offer-v1",
      "price": "price-v1",
      "rights": "rights-v1"
    },
    "growth_gate_evidence": "incomplete; no scale approval",
    "allowed_external_actions": []
  }
]
```
<!-- FIXTURES END -->

## 4. Expected discriminating distinctions

| Case | Common core result to preserve | Additional specialised check, not a new permission |
|---|---|---|
| S01 | Aggregate consideration 200, direct cost 160, contribution 40; incomplete growth evidence. | Account contributions 70 and -30; 1,000 billable units not yet invoiced and 3,000 consumed units outside the billable count. |
| S02 | Net consideration 880, direct contribution 710; cash trough -80 and closing 710. | Paid renewal 90%, entitlement 95% and meaningful use 60% on the stated due cohort, not one satisfaction rate. |
| S03 | Direct cost 800, contribution 200; resource headroom -2 hours. | Total work is 24 hours including four non-billable hours; scoped net consideration per total hour is 1000/24, not 1000/20. |
| S04 | Hypothetical engagement contribution 400, with cash schedule and other growth evidence absent. | Delivered report does not satisfy the false acceptance condition; adoption and economic impact remain unknown. |
| S05 | Net consideration 800, direct contribution 280; lowest cash -620, closing 180. | Ten physical units remain, two committed and eight available. A defined gross-sold/received ratio is 20/30; it is not asserted to equal a provider's differently based report. |
| S06 | Own-fee contribution 20 and closing usable cash 100. | Match rate 4/10; bank 480 minus seller funds 360 and reserve 20 leaves 100. Seller and reserve settlement preserve that same usable balance. |
| S07 | Contribution 10 across the declared horizon; cash minimum 50 and closing 360 under the supplied scenario. | A proposed removal conflicts with existing access rights; the future update cost remains explicitly hypothetical. |
| S08 | Consideration 3000 and direct costs 3000 reconcile to zero contribution. | Secured recurring maintenance funding is 500 short of the 1000 need. Three payers are not 1000 adopters, 20 contributors or 5000 stars. |
| S09 | Direct contribution 180; resource headroom -40 minutes. | Full service cycle is 400 minutes, of which only 225 are hands-on. The remaining 175 minutes cannot be omitted from capacity or labour cost. |

## 5. Negative, non-activation and precedence review

Every candidate receives a non-fit and unknown-fit check, a no-selection check and a compatible positive control in the local rule model. These checks consume stipulated facts; they do not perform natural-language classification or prove real user approval. The four original label-only cases have no mechanism facts and therefore cannot activate a pack. Consulting resolves to its advisory mode, not a separate required installation.

Precedence cases preserve an accepted price against a pack default, preserve explicit one-time pricing against a subscription preference, allow a genuinely open default, and expose conflicting applicable constraints/facts rather than rewriting either. A pack cannot request an external action, waive a mandatory core gate or turn unreviewed source prose into an applicable legal conclusion. The exact control model is only a local check of these declared distinctions.

Manual semantic review also covers incompatible hybrid scopes, duplicated shared costs, no-effect labels, a pack depending on a missing sibling for safeguards, absent paired evidence and a new provider version being mistaken for permission to change accepted decisions. Appropriate repairs target the effect, evidence, mapping or comparison record; they do not regenerate the entire business. The conformance companion records the actual run and review rather than treating these expected distinctions as completed tests.

## 6. Qualification admission controls

The final verifier additionally exercises a stipulated reviewed local-service packet with one explicit B06 effect, source locators, positive/negative cases and all inherited safeguards. It admits that complete design packet, declines a redundant new pack when an adequate existing option is stipulated, and rejects label-only, no-effect, replacement-execution and unknown-command proposals. Removing any inherited safeguard fails; removing a required review, case or source locator blocks admission. These are checks of the declared admission rule, not evidence that software has assessed real source quality or a candidate's semantic adequacy. The manual candidate review supplies that substantive assessment. No whole-business or legal approval is produced.
