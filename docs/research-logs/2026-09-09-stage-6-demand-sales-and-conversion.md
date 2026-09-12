# Stage 6 — Demand, Sales and Conversion

**Version:** 1.0 · **Date:** 9 September 2026 · **Status:** Design complete  
**Branch:** `feat/bootstrap`

## 1. Basis and decision

Read with [Stage 3](2026-09-09-stage-3-professional-practice-and-evidence.md), [Stage 4](2026-09-09-stage-4-business-customer-and-value-model.md) and [Stage 5](2026-09-09-stage-5-offer-pricing-and-monetisation.md). The customer, offer and permission boundary are inputs, not variables to rewrite whenever a channel disappoints.

Use one acquisition hypothesis at a time where that is adequate. Represent an observable path from suitable audience to delivered customer value, not an obligatory marketing funnel. Stages may be skipped, repeated or combined in an actual buying process; do not force a consumer checkout or enterprise procurement model onto every business.

## 2. Acquisition-path contract

For each named transition record its definition, population/unit, entry and exit criteria, observation window, source, deduplication rule and missing-data limitations:

```text
audience → reached → responded → prospect → qualified
→ buying decision → customer → delivered value → continuing value where relevant
```

Person, account, opportunity and transaction are different units. Repeated visits are not necessarily different prospects. A partner may introduce an account that contains several buyers. A sales report may contain purchases initiated before the measured campaign. These distinctions must remain visible before calculating conversion or acquisition cost.

The channel brief contains target customer, supported proposition, offer version, intended next action, access route, evidence for channel fit, permitted audience/data, budget and time limits, owner, measurement plan, capacity implications and stop conditions. Its output is a proposed test or approved bounded action, not implicit permission to send, publish or spend.

## 3. Channel-selection evidence

The following is the project's selection framework. It is not a performance ranking or a claim that any channel will work. A candidate progresses only when its required access, evidence and authority are available.

| Channel | Evidence needed to select it | Cheapest adequate representation/test | Distinct cost or failure to check |
|---|---|---|---|
| Direct outreach | Relevant reachable buyers and a permitted contact route | Reviewed message and small authorised contact set | Research/sales time, suppression, complaints and unsuitable responses |
| Content | Specific customer questions and credible expertise | One useful artefact with an explicit relevant next step | Production/distribution effort and no downstream intent |
| Community | Relevant community, participation norms and permission | Helpful participation or a consented research invitation | Trust damage, moderation burden and promotional restrictions |
| Search | Query intent related to the actual offer and attainable discovery | One useful page and its attributable response path | Search interest differs from paid demand; long measurement latency |
| Paid media | Plausible audience/intent, reliable events and spending authority | Bounded campaign only after the measurement and exposure review | Attributed versus incremental sales, creative/testing cost and cash exposure |
| Partnerships | Complementary audience, incentive alignment and responsibilities | Partner conversation and explicit referral/service brief | Concentration, claims made by partners and delayed receipts |
| Affiliates | Verifiable qualifying action, disclosure and reward economics | Small authorised partner arrangement | Fraud, reversals, incentive cost and low-quality transactions |
| Referrals | Evidence of delivered value and appropriate customer relationship | Clear voluntary referral request or introduction | Reward cost, privacy and treating contacts as retained customers |
| Events | Concentrated relevant participants and a purposeful interaction | A bounded session or meeting plan | Travel/preparation/follow-up cost and weak attribution |
| Marketplaces | Buyers transact for this category and platform rules fit | Accurate listing or manual mediated transaction | Fees, disputes, ranking dependence and platform restrictions |
| Platform distribution | Relevant distribution surface and compatible rules | One compliant listing/integration proposition | Dependency, approval delays, fees and access changes |
| Product-led acquisition | Existing use can legitimately expose others to useful value | One observable invitation or share use case | User permission, support/usage cost and free activity without paid demand |
| Existing audience | Current audience overlaps the intended customer and can be contacted | Relevant announcement or bounded offer test | Audience size mistaken for suitability or consent |

Compare the plausible shortlist on customer access, intent, evidence quality, cash/effort, time to learning, sales load, delivery capacity, permission and downstream value. Keep dimensions separate. Reject a channel whose required permission or affordable exposure is absent; label an unmeasured channel untested rather than bad.

## 4. Qualification and sales-path model

A qualification record names the business problem, fit evidence, intended outcome, buying roles/process, timing, resource constraints and reason to progress or stop. Use only proportionate data. An income or demographic guess is not qualification evidence. Not qualified is different from not yet understood.

| Sales path | Required distinction | Decision-useful evidence |
|---|---|---|
| Self-serve | Understanding, suitability, checkout and technical completion | Step-level denominators, errors and customer feedback |
| Sales-assisted | Where assistance is needed and its cost | Reasons for contact, resolved obstacles and support/sales hours |
| Consultative | Discovery before a scoped proposal | Recognised problem, decision criteria and deliverable agreement |
| Enterprise | Users, sponsor, purchaser and review/approval roles | Actual buying process, procurement/security constraints and timeline |
| Inbound | Interest is not automatically qualified intent | Source, question, fit and progression |
| Outbound | Seller initiation is not buyer demand | Relevant response, permission and progression rather than send volume |
| Marketplace-mediated | Platform governs parts of discovery and transaction | Listing fit, actual transactions, disputes, fees and settlement |
| Partner-led | Responsibilities cross organisational boundaries | Attribution, qualifying criteria, promises and handoff acceptance |

These dimensions can combine: inbound enterprise consultative selling is a coherent path. Do not create separate mutually exclusive funnels merely because the labels differ.

GitLab's public discovery questions provide a concrete example of investigating objectives, decision process, budget and time-to-value. They are vendor practice, not evidence that its complete process is optimal for another business. [E01]

## 5. Measurement and diagnosis

For an eligible cohort, transition conversion = distinct eligible entities reaching the next named state / distinct eligible entities entering the prior state. A zero denominator is undefined, not 0%. Cumulative nested counts must not increase unless re-entry or different populations are explicitly modelled. Report sample size and missingness; do not pool incompatible windows or units.

Inspect volume, fit, intent, qualification, conversion, acquisition spend, attributable sales effort, time-to-close and downstream delivery/retention quality. Blended acquisition cost and channel-attributed cost need separate labels. A channel with few eventual purchases may not be observable yet when the sales cycle is long.

Paid-search experiments at eBay show why attributed purchases cannot automatically be treated as causal advertising effects. Their specific results are not forecasts for this repository's users. [E02]

| Symptom | Competing explanations | First bounded correction |
|---|---|---|
| Little relevant reach | Access, audience, discovery or measurement | Verify reach definition and access before altering offer |
| Reach without useful response | Audience, proposition comprehension or next step | Inspect relevance and message; preserve supported offer facts |
| Many responses, little qualification | Incentive attracts wrong people, ambiguous fit or poor qualification | Repair incentive/qualification rather than increase contact volume |
| Qualified interest without purchase | Price/scope, trust, authority, timing or technical friction | Investigate actual losses and buying process |
| Purchases without contribution | Cost boundary, refunds, acquisition/sales cost or price | Recalculate economics before scale |
| Purchases without delivered/continuing value | Mis-sold scope, onboarding, quality or product value | Repair delivery/value rather than obstruct cancellation |

A diagnosis includes measurement checks, candidate causes, supporting and contradicting evidence, proposed mutation scope and the next distinguishing test. It does not infer causality from a single metric.

## 6. Synthetic boundary check

A fictional service reaches 40 distinct prospects, receives 12 replies, identifies 4 qualified opportunities and wins 1 engagement. The windows and entities are assumed matched for this fixture only. Reply conversion is 30%; qualified opportunity conversion from replies is one third; purchase conversion from qualified opportunities is 25%. None establishes population rates or acceptable economics.

An extra 80 replies generated by a free resource are not comparable until fit and eventual progression are known. If delivery capacity is one engagement, even better measured acquisition cannot justify accepting unlimited work. The immediate decision may be preserving the channel and reducing acquisition activity, not scaling it.

## 7. Exit and handoff

The channel, lead-quality and sales-path contracts distinguish reach, suitability, offer comprehension, buying process and downstream viability. Stage 7 supplies delivery, contribution and cash checks. Stage 8 supplies experiment interpretation; Stage 9 resolves jurisdiction-specific execution questions. No live outreach, campaigns, payments or platform settings were changed.

### Sources checked

Accessed 9 September 2026. Broader channel hypotheses use Stage 3's cited professional-practice map; the selection table and diagnostics above are independent design synthesis.

- E01: [GitLab Sales Discovery and Qualification Questions](https://handbook.gitlab.com/handbook/sales/qualification-questions/), objectives, customer decision and time-to-value sections; public operating practice.
- E02: Blake, Nosko and Tadelis, [Consumer Heterogeneity and Paid Search Effectiveness](https://www.nber.org/papers/w20171), also Stage 3 S10; scope-limited field-experiment evidence, not a universal channel ranking.

*Stage 6 · Version 1.0 · 9 September 2026.*
