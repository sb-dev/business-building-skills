# Business Building Skills — Extension Pack Catalogue

**Status:** Canonical research/design catalogue  
**Derived from:** accepted Stage 14 candidate catalogue, pack model, source research and design probes  
**Boundary:** no catalogue pack is implemented or installed. Entries are mechanism-based research/design candidates for later implementation/evaluation.

## 1. Catalogue policy

The curated set contains **eight independent candidates plus one merged advisory mode**. A catalogue entry means the reusable mechanism is worth preserving as a specialisation design; it does not mean a package exists, installs, improves agent performance or is commercially optimal.

Selection hierarchy remains: verified constraints + explicit project facts/instructions → approved business decisions → selected pack defaults → core defaults. Core works without packs. Packs are selected by actual mechanism, not sector/location/technology labels.

Current entries:

| ID | Name | Disposition | Current maturity |
|---|---|---|---|
| PK01 | `saas-business` | retain independent candidate | research/design candidate — **NOT IMPLEMENTED** |
| PK02 | `consumer-mobile-subscription` | retain independent candidate | research/design candidate — **NOT IMPLEMENTED** |
| PK03 | `professional-services` | retain independent candidate | research/design candidate — **NOT IMPLEMENTED** |
| PK04 | `consulting-business` | merge into PK03 advisory mode | **NOT AN INDEPENDENT PACK**; mode **NOT IMPLEMENTED** |
| PK05 | `ecommerce-business` | retain independent candidate | research/design candidate — **NOT IMPLEMENTED** |
| PK06 | `marketplace-business` | retain independent candidate | research/design candidate — **NOT IMPLEMENTED** |
| PK07 | `creator-digital-product` | retain independent candidate | research/design candidate — **NOT IMPLEMENTED** |
| PK08 | `open-source-commercialisation` | retain independent candidate | research/design candidate — **NOT IMPLEMENTED** |
| PK09 | `local-service-business` | retain independent candidate | research/design candidate — **NOT IMPLEMENTED** |

## 2. PK01 — `saas-business`

### Profile and selection rationale
Fit: recurring access to a hosted software capability, with seat/account/usage/hybrid charging where service economics matter. Non-fit: one-time downloads or human-only engagements. Core already handles subscriptions/economics; the specialisation adds user/account/payer roles, consumed→billable→invoiced bridges, service-cost sensitivity and matched renewal/use evidence.

Core effects: B02/G04 separate user/account/payer/approver; B04/B07/E03 reconcile units and contribution; G06/G08/E02 join meaningful use, renewal/expansion and service quality without replacing growth gates.

Metrics: account/user/paid roles; consumed/billable/invoiced units; cohort contribution; renewal and meaningful-use evidence; marginal infrastructure/support burden; dated collections.

### Exact showcase prompt

> Assess the supplied two-account hosted-service cohort and metering reconciliation. Preserve accepted versions. Report account and aggregate contribution, mismatched usage units and what remains unknown before growth; do not change pricing or perform billing.

### Pack-specific evaluations
- activation: hosted recurring service with material account/usage mechanics;
- non-activation: one-time digital asset or human service;
- precedence: accepted project price/terms override pack defaults;
- changed behaviour: unit/revenue bridge and account-role checks appear;
- metrics: contribution and consumed/billed reconciliation are defined;
- negative: aggregate positive contribution cannot hide a loss-making high-usage account;
- core vs pack: same fixed task, pack must add specialised checks without removing core safeguards.

### Current maturity
Research/design candidate — **NOT IMPLEMENTED**. Stage-14 deterministic projection is design evidence, not installed-pack efficacy.

## 3. PK02 — `consumer-mobile-subscription`

### Profile and selection rationale
Fit: consumer recurring/prepaid app access where store-managed plans, payment, entitlement or recovery materially affect the decision. Non-fit: mobile UI on a direct-billed service with no relevant store mechanics. Distinct from generic SaaS because offer transitions, entitlement restoration/grace and channel-specific settlement need explicit treatment.

Core effects: B03/B04/E05 request actual offer/commitment/post-offer price/entitlement terms; G06/E02 distinguish paid renewal, entitlement continuation, grace and meaningful use; B07/E03/G08 reconcile gross payment, adjustments, platform charges/net proceeds, settlement and obligations without assuming a universal commission.

### Exact showcase prompt

> Assess this mobile subscription renewal cohort. Separate paid renewal, entitlement and meaningful use, reconcile net contribution and cash timing, and preserve all current access rights. Do not send messages, revoke access or recommend scale from billing alone.

### Pack-specific evaluations
- activation requires material store/subscription mechanics;
- non-activation for direct-only generic service;
- precedence preserves real channel rules/current accepted terms;
- changed behaviour explicitly separates due renewal/payment/entitlement/use;
- metrics distinguish due-cohort paid renewal and meaningful use;
- negative case rejects hidden renewal/cancellation obstruction;
- paired comparison must show specialised entitlement/cash questions, not fabricated platform fees.

### Current maturity
Research/design candidate — **NOT IMPLEMENTED**.

## 4. PK03 — `professional-services`

### Profile and selection rationale
Fit: bounded human expertise/time/quality and client participation materially determine delivery. Non-fit: scalable self-serve product without meaningful engagement work. Fixed-fee/time/milestone/retainer are alternatives, not mandatory models.

Core effects: B03/B06/G04 request deliverables, exclusions, change control, client inputs and acceptance; B04/B07/E03 compare pricing against priced/unpriced effort and separate contracted/delivered/accepted/invoiced/collected; G08/E06/E07 include sales/admin/support/client-delay exposure in shared capacity and prefer bounded intake/scope repair.

### Exact showcase prompt

> Assess two fixed-fee professional engagements against shared human capacity. Include delivery, non-billable time and all supplied costs. Distinguish a profitable comparison from feasible intake; preserve the accepted customer, price and scope.

### Pack-specific evaluations
- activate on material human engagement delivery;
- non-activate on self-serve product;
- accepted scope/price and client obligations outrank pack defaults;
- pack adds engagement acceptance/dependency/non-billable capacity semantics;
- metrics include effective rate, contribution, capacity and collection timing;
- negative case rejects profitable-but-infeasible intake;
- core-vs-pack comparison retains same economics while testing specialised client/dependency fields.

### Current maturity
Research/design candidate — **NOT IMPLEMENTED**.

## 5. PK04 — `consulting-business` advisory mode

### Profile and selection rationale
This is **NOT AN INDEPENDENT PACK**. It is an advisory/knowledge-transfer mode of PK03 because pricing/cash/capacity foundations remain professional-services while client sponsorship, adoption and transfer add reusable questions. A consultant title alone does not activate it.

Core effects: B03/G04 separate diagnostic question, sponsor expectations, recommendation deliverable and client decision; B06/E02 separate report delivery, acceptance, adoption and realised benefit; B09/E04/E07 test whether advice can change the decision/client can act without inventing ROI.

### Exact showcase prompt

> Assess the advisory engagement using the professional-services advisory mode. A report has been delivered but client acceptance is false, adoption and realised impact are unknown. Separate these findings and cost from the client outcome; do not claim ROI or acceptance.

### Mode-specific evaluations
- activate only on advisory/diagnosis/knowledge-transfer work;
- normal execution service remains PK03 without mode;
- client adoption/impact cannot be inferred from delivery;
- pricing/cash/capacity stay inherited from PK03;
- negative case rejects invented attributed ROI;
- paired run should add sponsorship/adoption/transfer semantics, not duplicate a second package.

### Current maturity
Merged research/design mode — **NOT IMPLEMENTED**.

## 6. PK05 — `ecommerce-business`

### Profile and selection rationale
Fit: physical goods with material stock, fulfilment, returns or supplier commitments. Non-fit: purely digital asset; intermediary matching without owned stock. Residual grammar is SKU/order/stock state, goods flow, reverse flow and working-capital exposure.

Core effects: B03/B06 request order promise, available/committed/incoming stock, lead time and return responsibility; B07/E03 reconcile own consideration, refunds, goods consumed, shipping, returns and stock purchases without confusing inventory expense with cash; G01/G08/E06 assess demand against stock/funding before replenishment.

### Exact showcase prompt

> Assess the goods cohort and stock-funded growth proposal. Reconcile sold, committed and available quantities, nonrecoverable returns, direct contribution and the lowest dated usable cash. Do not equate stock purchase cash with the cost of goods consumed or auto-order inventory.

### Pack-specific evaluations
- activate on owned-stock physical-goods mechanism;
- non-activate for purely digital/intermediary-only flow;
- preserve actual customer rights and supplier obligations;
- changed behaviour adds stock/fulfilment/reverse-flow bridge;
- metrics include defined stock reconciliation, fulfilled contribution, return rate, working-capital trough;
- negative case rejects positive ending cash when pre-collection stock funding fails;
- paired comparison uses identical demand/economics facts.

### Current maturity
Research/design candidate — **NOT IMPLEMENTED**.

## 7. PK06 — `marketplace-business`

### Profile and selection rationale
Fit: distinct sides whose matching/transaction progression and incentives determine value. Non-fit: direct seller with own stock merely listing many items. Residual grammar is side-specific qualification/outcomes, constrained matching, own-fee vs transaction-value/funds reconciliation, side-specific retention/quality.

Core effects: B02/G01/G04 request each side's progress/alternatives/eligibility/capacity; B05/B07/E03 separate transaction value, own consideration, seller funds, reserves/chargebacks/settlement; G06/G08/E02 measure eligible matching and failures/time-to-match without inferring network effects from registrations.

### Exact showcase prompt

> Assess the intermediary marketplace, keeping own fees separate from transaction value and third-party funds. Compute request matching and usable cash before and after already-restricted funds settle. Preserve unmet demand; no invented network effects or live transfers.

### Pack-specific evaluations
- activate only for real intermediary multi-sided mechanism;
- direct owned-stock sale non-activates;
- precedence preserves restrictions/third-party ownership of funds;
- changed behaviour adds side/match/funds semantics;
- metrics include matched eligible requests, side participation, own contribution and usable cash;
- negative case rejects GMV as revenue or supplier registrations as demand;
- paired comparison tests specialised matching questions with same core facts.

### Current maturity
Research/design candidate — **NOT IMPLEMENTED**.

## 8. PK07 — `creator-digital-product`

### Profile and selection rationale
Fit: reproducible digital work/course/assets/content with material rights, version, access, update, support or ongoing production obligations. Non-fit: creator identity alone; bespoke labour belongs to services; physical merchandise is separately ecommerce. Residual grammar makes content/version/access rights and continuing production/support first-class.

Core effects: B03/B04/E05 request exact content/version/licence/access/update/support and distinguish one-time vs membership; B06/B07/E03 include creation, maintenance, hosting/platform, support and refund work; G06/G07/E02 preserve continuing access/value and existing buyer entitlements.

### Exact showcase prompt

> Assess the digital-product promise over the full supplied horizon, including creation and promised updates/support. Existing buyers retain access to their purchased edition; a proposed edition change must not delete that right. No publishing or licence revocation is authorised.

### Pack-specific evaluations
- activate on material digital rights/version/access obligations;
- non-activate for bespoke services or physical-only sale;
- existing rights outrank pack/update defaults;
- changed behaviour adds rights/version/production/support horizon;
- metrics include net contribution, access defects, support load, cohort use/renewal where applicable;
- negative case rejects withdrawing paid access to sell an update;
- paired comparison holds fixed commercial facts while pack adds rights/production checks.

### Current maturity
Research/design candidate — **NOT IMPLEMENTED**.

## 9. PK08 — `open-source-commercialisation`

### Profile and selection rationale
Fit: commercial work coexists with open-source rights and materially different adopter/contributor/maintainer/sponsor/customer incentives. Non-fit: publicly readable source alone or proprietary hosted service with no ecosystem-rights issue. Residual grammar explicitly separates adoption/contribution/funding/paid scope and protects the commons while accounting for maintainer capacity.

Core effects: B02/B03/E05 request licence/right boundaries and stakeholder value; B05/B07/G08 reconcile commercial/funding exchanges, restricted funds, paid delivery and maintenance capacity; G01/G03/E02 distinguish adoption, contributors, retained users and paying customers without stars-as-demand inference.

### Exact showcase prompt

> Assess the supplied open-source commercial scenario, with support and sponsorship obligations. Keep adopters, contributors, payers and repository attention distinct. Show the recurring maintenance funding gap without treating stars as customers or withdrawing existing open-source rights.

### Pack-specific evaluations
- activate on genuine open-source commercial/incentive mechanism;
- public-code label alone non-activates;
- licence/project facts and accepted rights outrank pack defaults;
- changed behaviour adds stakeholder/rights/funding/maintenance semantics;
- metrics separate adoption/use, contributor health, paid demand and maintenance funding;
- negative case rejects stars as customers/revoking core rights/spending restricted funds;
- paired comparison holds same repo/service facts while pack adds ecosystem checks.

### Current maturity
Research/design candidate — **NOT IMPLEMENTED**.

## 10. PK09 — `local-service-business`

### Profile and selection rationale
Fit: delivery is materially constrained by geography, travel, appointments, facilities or location-specific resources. Non-fit: remote consultancy merely located in a city. Residual grammar is full door-to-door resource/cost accounting and serviceable geographic demand—not route-planner implementation.

Core effects: B03/B06/G04 request service area, visit scope, access, windows and travel/setup; B07/E03/G08 include travel/setup/idle gaps/materials/no-show/rework/shared resources in economics/capacity; G01/G03/G06 evaluate local discovery/referrals/repeat through serviceable delivered demand.

### Exact showcase prompt

> Assess five local-service visits including travel and setup. Compare full resource time with the supplied day and calculate direct contribution. A favourable margin is not a feasible route or appointment plan; preserve the accepted offer and do not schedule visits.

### Pack-specific evaluations
- activate on geographic/appointment/resource-constrained delivery;
- remote work non-activates despite city label;
- accepted service area/terms outrank pack defaults;
- changed behaviour adds door-to-door/territory/window semantics;
- metrics include full resource minutes, serviceable conversion, attendance and contribution;
- negative case rejects profitable aggregate hours as a verified feasible route;
- paired comparison keeps same visits/costs and adds local-service checks only.

### Current maturity
Research/design candidate — **NOT IMPLEMENTED**.

## 11. Cross-catalogue selection guidance

Use the exchange/mechanism, not organisation name:

- hosted recurring software → PK01;
- store-mediated consumer mobile subscription → PK02;
- bounded human engagement → PK03, optionally PK04 advisory mode;
- owned physical stock → PK05;
- multi-sided intermediation → PK06;
- digital rights/content/update access → PK07;
- open-source ecosystem + commercial obligations → PK08;
- geographic appointment/travel/resource delivery → PK09.

Hybrid businesses can use explicit component scopes and reconcile shared resources/costs; no inheritance tree or last-loaded-wins rule exists. A SaaS consultancy may scope PK01 and PK03 separately. A local-service marketplace scopes PK06 for intermediation and PK09 for provider delivery where relevant.

Reject label-only proposals such as “AI startup”, “finance company”, “fitness business” or “London business”. A regulated sector routes specialist questions above pack defaults rather than selecting a compliance exemption pack.

## 12. Catalogue maturity and implementation gate

Before any entry becomes an implemented pack, the implementation stage must provide:

1. actual self-contained package and compatible core/command versions;
2. activation/non-activation behaviour;
3. exact precedence and protected invariants;
4. named material core effects;
5. pack-specific metrics and deterministic checks;
6. positive/negative/incompatible cases;
7. actual paired core-vs-pack execution for measured behaviour claims;
8. exact showcase prompt/run evidence;
9. clean installation where product acceptance requires it;
10. accurate licence/source/maintenance status.

Catalogue entries must retain historical versions/withdrawal rules and never silently change accepted customer rights or project decisions.

## 13. Research lineage

- [Stage 14 pack model](research-logs/2026-09-10-stage-14-pack-model.md)
- [Stage 14 candidate catalogue](research-logs/2026-09-10-stage-14-candidate-catalogue.md)
- [Stage 14 pack authoring](research-logs/2026-09-10-stage-14-pack-authoring.md)
- [Stage 14 design probes](research-logs/2026-09-10-stage-14-design-probes.md)
- [Stage 17 pack-evaluation taxonomy](research-logs/2026-09-11-stage-17-benchmark-taxonomy.md)

Pack mechanics and authoring rules are canonical in [05 — Customisation Packs](05-business-building-customisation-packs-spec.md). This file owns the curated profile catalogue only.
