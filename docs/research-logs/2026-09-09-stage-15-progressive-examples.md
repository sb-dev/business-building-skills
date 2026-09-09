# Stage 15 — Five Progressive Example Levels

**Version:** 1.0  
**Date:** 9 September 2026  
**Status:** Design complete  
**Branch:** `feat/bootstrap`

## 1. Selection method

Candidate examples were screened for complementary coverage across customer evidence, offer/pricing, acquisition/sales, delivery/capacity, retention, economics/cash, experiments, legal/ethical boundaries, repair/preservation, B2B/B2C, sales motion and business model. Redundant marketing-only examples were removed.

The 15 selected examples are **synthetic learning cases** unless the prompt explicitly supplies real project evidence. Their outputs must never invent results. Exact prompts below are the future copyable starting prompts; fixture data may be supplied by the example directory at implementation time.

## 2. Level 1 — One bounded decision

### L1A — Price a fixed-scope service

Coverage: pricing, contribution, capacity, evidence, professional services.

**Exact prompt:**
> Compare £1,500 and £2,400 pricing for this fixed-scope onboarding audit using the supplied customer evidence, delivery-hour assumptions and costs. Show which facts are observed versus assumed, calculate contribution with a reproducible method, identify the riskiest pricing assumption, and design the cheapest honest test that could change the decision. Do not invent willingness-to-pay data.

### L1B — Select one acquisition channel

Coverage: channel fit, qualification, permission, downstream economics.

**Exact prompt:**
> Choose the best first acquisition-channel test for this B2B service from direct outreach, content, referrals and paid search. Use only the supplied customer/access evidence, budget and delivery capacity. Define the qualified signal, measurement window, stop condition and downstream checks. Do not recommend all channels or infer permission to contact anyone.

### L1C — Decide whether a guarantee is viable

Coverage: offer, risk allocation, cash exposure, claims/legal handoff.

**Exact prompt:**
> Evaluate the proposed money-back guarantee for this offer. Separate the deliverable we control from the customer's business outcome, model the stated refund exposure, identify evidence and professional-review gaps, and propose the smallest truthful alternative if the guarantee is not supportable. Do not optimise conversion by hiding conditions.

## 3. Level 2 — One coherent commercial component

### L2A — Service offer + price + delivery

**Exact prompt:**
> Design a bounded offer for a solo technical consultant using the supplied customer interviews and capacity constraints. Define scope, exclusions, proof, project-versus-retainer pricing options, delivery model, contribution and cash timing. Preserve unknown willingness to pay and finish with one falsifiable offer test.

### L2B — Lead resource + qualification + sales path

**Exact prompt:**
> Design an acquisition test for this B2B advisory offer using one useful downloadable diagnostic as the initial response mechanism. Define who it is for, what makes a response qualified, the sales-assisted path, privacy/permission assumptions, sales effort, downstream success metric and failure conditions. Treat downloads as contacts, not customers.

### L2C — Subscription retention redesign

**Exact prompt:**
> Diagnose the supplied subscription cohort where first-month conversion is healthy but month-three retention is weak. Separate onboarding, delivered value, billing, price and cancellation hypotheses; identify the cheapest evidence that distinguishes them; and propose the smallest responsible change. Do not use cancellation friction as a retention strategy.

## 4. Level 3 — Complete small business model

### L3A — One-person FDE consultancy

**Exact prompt:**
> Build a complete one-person Forward Deployment Engineer consultancy model from the supplied experience, target-client evidence and weekly capacity. Define customer/buyer, problem, offer, project/retainer pricing, acquisition and consultative sales path, delivery capacity, unit economics, cash timing, assumptions and first three experiments. Optimise for a sustainable solo business, not maximum lead volume.

### L3B — Small B2B SaaS

**Exact prompt:**
> Build a small B2B SaaS business model from this validated workflow problem and supplied pilot evidence. Distinguish user, buyer and approver; define subscription or usage pricing hypotheses, product-led versus sales-assisted acquisition, onboarding, recurring value, support/compute costs, cohort metrics, cash assumptions and the next falsifiable commitment. Do not invent product-market fit.

### L3C — Ecommerce physical product

**Exact prompt:**
> Build a small ecommerce business model for this supplied product and customer evidence. Include transparent price, order economics, payment fees, fulfilment, returns, inventory/working-capital exposure, acquisition hypotheses, checkout measurement and repeat-purchase assumptions. Identify the first constraint that should be tested before increasing ad spend.

## 5. Level 4 — Diagnose and repair an existing business

### L4A — Leads up, contribution down

**Exact prompt:**
> Audit this business where lead volume doubled but qualified opportunities and contribution fell. Validate the funnel definitions and attribution, compare channel cohorts, inspect sales effort and downstream value, diagnose the most supported constraint, and recommend the smallest change while preserving still-supported customer and offer decisions.

### L4B — Sales exceed delivery capacity

**Exact prompt:**
> Diagnose this professional-service business where demand and close rate are healthy but delivery deadlines and rework are worsening. Model capacity and contribution, distinguish the binding delivery constraint from acquisition symptoms, and recommend a bounded intake, scope, price or process change. Do not recommend more leads until capacity supports them.

### L4C — Revenue grows, cash fails

**Exact prompt:**
> Diagnose this growing ecommerce business using the supplied monthly orders, margins, inventory purchases, supplier terms, receivables/refunds and cash balances. Reconcile profit-like metrics with dated cash obligations, identify the exposure window and propose the smallest growth, payment-term or inventory change that keeps obligations fundable.

## 6. Level 5 — Full business-building thesis

### L5A — Kakeibo consumer subscription

**Exact prompt:**
> Evaluate and evolve the Kakeibo personal-finance app business using only the supplied product decisions and evidence. Model consumer value, 30-day money-back guarantee, subscription pricing, app-store/direct acquisition, onboarding and retention, AI-assistant delivery/support costs, unit economics, cash, privacy and financial-claim handoffs. Identify the riskiest assumption and smallest responsible next experiment without inventing financial-benefit claims.

### L5B — FDE consultancy growth system

**Exact prompt:**
> Evolve the proven one-person FDE consultancy from a viable first offer into a controlled growth system. Compare network, content, referral and bounded outbound channels; model qualification, sales capacity, project/retainer mix, utilisation, subcontracting boundary, cash collection, expansion and referral. Preserve the solo-business objective and reject growth that exceeds delivery quality or authorised outreach constraints.

### L5C — Production Skills commercial ecosystem

**Exact prompt:**
> Design and evaluate a commercial ecosystem around the open-source Production Skills family without weakening open-source adoption. Compare services, education, support/sponsorship and Extension Pack marketplace hypotheses; distinguish users, contributors and payers; model community-led acquisition, delivery capacity, cash and ecosystem incentives; and design experiments that validate one revenue path before adding another. Treat GitHub stars as adoption evidence only within their actual meaning, not as paying-customer demand.

## 7. Coverage matrix

Legend: ● primary, ○ secondary.

| Example | B2B | B2C | Offer/price | Acquisition/sales | Delivery | Retention | Econ/cash | Experiment | Legal/ethical | Diagnose/preserve | Pack candidate |
|---|---|---|---|---|---|---|---|---|---|---|---|
| L1A | ● |  | ● |  | ○ |  | ● | ● |  |  | services |
| L1B | ● |  | ○ | ● | ○ |  | ○ | ● | ○ |  | services |
| L1C | ○ | ○ | ● |  | ○ |  | ● | ○ | ● |  | consumer/services |
| L2A | ● |  | ● | ○ | ● |  | ● | ● | ○ |  | services |
| L2B | ● |  | ○ | ● |  |  | ○ | ● | ● |  | services |
| L2C |  | ● | ○ |  | ● | ● | ○ | ● | ● | ● | consumer-subscription |
| L3A | ● |  | ● | ● | ● | ○ | ● | ● | ○ |  | services |
| L3B | ● |  | ● | ● | ● | ● | ● | ● | ○ |  | SaaS |
| L3C |  | ● | ● | ● | ● | ○ | ● | ● | ● |  | ecommerce |
| L4A | ● | ○ | ○ | ● | ○ | ○ | ● | ○ |  | ● | core |
| L4B | ● |  | ● | ○ | ● |  | ● | ○ |  | ● | services |
| L4C |  | ● | ○ | ○ | ● | ○ | ● | ○ | ○ | ● | ecommerce |
| L5A |  | ● | ● | ● | ● | ● | ● | ● | ● | ● | consumer-subscription |
| L5B | ● |  | ● | ● | ● | ● | ● | ● | ● | ● | services |
| L5C | ● | ○ | ● | ● | ● | ● | ● | ● | ● | ● | open-source |

The set covers self-serve and sales-assisted paths, one-off and recurring revenue, digital and human delivery, organic/outbound/referral/paid hypotheses, short and long buying processes, cash-light services and working-capital-sensitive ecommerce. Marketplace mechanics appear explicitly in L5C and the Stage 16 stress test; a dedicated marketplace example can remain supplementary rather than displacing a stronger primary coverage combination.

## 8. Exit

The selected 15 form complementary progression from one decision to full-system design/repair. They exercise the business-building thesis rather than fifteen marketing tactics, and every primary example has an exact prompt suitable for later repository implementation.

*Stage 15 · Version 1.0 · 9 September 2026.*
