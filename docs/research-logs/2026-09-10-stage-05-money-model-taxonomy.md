# Stage 5: Money-model taxonomy

**Date:** 10 September 2026  
**Branch:** `feat/bootstrap-2`  
**Authority:** [Original bootstrap §12](2026-09-08-business-building-skills-new-project-bootstrap-process.md).  
**Companions:** [Offer/pricing architecture and economic definitions](2026-09-10-stage-05-offer-and-pricing-architecture.md), [sources and checks](2026-09-10-stage-05-research-and-checks.md), [conformance](2026-09-10-stage-05-conformance.md).

## Use and accounting boundary

All thirteen required labels are retained, each with all ten required fields. They are not thirteen mutually exclusive businesses or independent revenue accounts. Initial transaction and renewal are events; recurring revenue is a pattern; upsell, cross-sell and expansion describe changes; usage describes a unit; services/licensing/platform/ad/referral describe exchanges; open-source commercialisation describes a wider setting. Combine only what a real exchange needs.

Record each transaction once with an identifier, date/period, payer, accepted terms, consideration and adjustments; attach analytical labels separately. Allocate distinct invoice lines where useful. Do not add overlapping renewal/expansion/subscription/licence reports into total revenue. A fee earned by the platform and proceeds owed to a seller belong to different parties.

In every card, gross revenue means the explicitly stated gross commercial consideration **G** for the business's own exchange, not automatically accounting revenue recognised in that period. Use **N = G − D − F**, **C = N − K** and **margin = C/N for N > 0** under the companion's declared cost scope. D is discounts; F is refunds/credits, recorded once; K is the stated direct cost. Zero/negative N does not receive a spurious margin percentage. Show acquisition/shared costs separately. Taxes, total customer obligation, principal/agent treatment and recognition timing must be reconciled with appropriate inputs; this taxonomy does not certify them.

Each dependency is a question for the actual business, not an assumed favourable answer. Unknown amounts, rates, retention, capacity, rights or payout dates remain unknown. No card supplies a market price, success rate or universal margin target. Source identifiers R01–R17 resolve in the research companion; the ten-field cards are project synthesis grounded in those sources and accepted Stages 2–4.

## M01: initial transaction

**Meaning:** The first exchange with a defined customer, whether standalone or the first event in a longer relationship. Basis: Stage 2 offer/entry research, Stage 3 P04–P06, Stage 4 E09; R01–R03.

| Field | Definition and decision implication |
|---|---|
| value exchange | A stated first outcome, product, access or service for the customer's consideration. The entry exchange must have honest standalone scope; future purchases are optional unless clearly part of the agreed commitment. |
| payer | The actual person/entity owing payment, linked to buyer and budget authority. A trial user or interested employee is not automatically the payer. |
| pricing unit | Defined first order, item, account, project or starting period, with included quantity and total terms. Do not mix lead, order and customer units. |
| gross revenue | G is the first transaction's own consideration before declared adjustments, counted once. A deposit is a collection event against it, not a second sale. |
| direct costs | Product/service fulfilment, onboarding, transaction handling and directly attributable support/remedy costs. Show acquisition separately and include economically relevant human work. |
| margin | Compute C and C/N on the explicit scope. An intentionally negative entry contribution needs an authorised funded purpose; hoped-for repeat value does not make it positive. |
| cash timing | Record deposit, delivery, balance, refunds and settlement dates. Prepayment may precede fulfilment; invoiced consideration may remain uncollected. |
| retention dependency | None is required to describe a standalone sale. A model relying on later recovery must name the repeat-value hypothesis and evidence rather than assume it. |
| capacity dependency | Initial onboarding, sales handoff, stock or first-delivery load may constrain growth even when later service is inexpensive. Validate peak and customer-participation demands. |
| risk | Discount-only demand, misleading entry terms, uncosted onboarding, cash gaps and assuming the first purchase proves renewal. Keep paid evidence scoped to the actual terms. |

## M02: recurring revenue

**Meaning:** Repeated consideration associated with continuing value or entitlements; not necessarily the same as repeated payment of one finite debt. Basis: Stage 2 continuity research, Stage 4 E07; R07.

| Field | Definition and decision implication |
|---|---|
| value exchange | Continuing access, availability, replenishment or service during defined periods. Specify the delivered continuing benefit, not merely permission to keep billing. |
| payer | Account holder, employer, household or other contracting payer. Distinguish the people using the ongoing service from the party renewing or paying. |
| pricing unit | Account, seat, membership, entitlement or specified service quantity per period. Billing frequency and minimum commitment length are separate fields. |
| gross revenue | G is the applicable recurring consideration for the stated periods/accounts, with adjustments shown. Do not count annual prepayment and monthly allocations as additional receipts or revenue. |
| direct costs | Continuing delivery/hosting, support, account service, usage, payment handling and remedy costs. State which costs vary with accounts, active users or workload. |
| margin | Evaluate C and C/N by comparable period/cohort, including unusually costly customers. Forecast contribution remains conditional on retained accounts and cost assumptions. |
| cash timing | Upfront versus arrears collection, failed payments, pauses, refunds and provider settlement create different cash paths; annual receipts leave future service obligations. |
| retention dependency | Central when future periods drive viability. Distinguish observed use, voluntary renewal, continued billing and forecast retention; no indefinite lifetime extrapolation. |
| capacity dependency | Concurrent service, support, reliability and renewal administration must support the active base, not just new sales. Bursts may differ from average utilisation. |
| risk | Inertia mistaken for value, hidden renewal terms, underfunded future delivery and forecasts that ignore churn, support burden or collection failures. |

## M03: upsell

**Meaning:** A move to a higher-value or higher-scope version of the same underlying offer for a suitable customer. Basis: Stage 2 expansion/packaging rows and Stage 3 P06; R01.

| Field | Definition and decision implication |
|---|---|
| value exchange | Additional relevant capability, service standard or scope beyond the accepted baseline. Identify the customer's need and the genuine option to retain the current offer. |
| payer | Existing or prospective payer authorised to increase commitment. A user's interest in a premium feature is not budget approval. |
| pricing unit | Upgrade difference or replacement package price for stated quantity/period. Record proration and treatment of previously paid entitlements where applicable. |
| gross revenue | G is the incremental consideration or clearly reconciled replacement transaction, not both the full new price and the same uplift again. |
| direct costs | Incremental fulfilment, higher service/support level, onboarding and payment/change administration. Existing baseline costs remain in the whole-account view, not charged twice. |
| margin | Compare incremental C with the retained baseline and whole-account economics. Account for cannibalisation, migration work and customers who would otherwise buy the higher package. |
| cash timing | Record when upgrade fees are due and when new obligations start. Credits, refunds and later settlement can defer or reduce usable uplift. |
| retention dependency | The upgrade should add continuing value where the relationship continues; higher billing alone does not establish improved retention or satisfaction. |
| capacity dependency | Premium service, specialist support or additional consumption can be disproportionately costly. Confirm capacity for the upgraded population rather than average base usage. |
| risk | Pressure-selling, fake premium choices, hidden downgrades to the accepted base, uncosted support and double-counted revenue. Preserve existing promises. |

## M04: cross-sell

**Meaning:** A distinct complementary exchange, not an essential part of an earlier promise withheld until after purchase. Basis: Stage 2 complementary-offer research, Stage 3 P06; R04 and R16 where referral incentives apply.

| Field | Definition and decision implication |
|---|---|
| value exchange | A separate related need is met by another product/service. Explain complementarity and optionality; identify a third-party supplier where one is involved. |
| payer | The relevant customer or another authorised budget owner for the complementary purchase; do not assume authority transfers from the first transaction. |
| pricing unit | Separate item, service, project or entitlement, with its own complete terms and any genuine combined-price adjustment. |
| gross revenue | G is this business's own complementary consideration. Where the business only refers the sale, record the commission mechanism under M12 rather than the supplier's whole sale. |
| direct costs | Complementary delivery, integration, support, supplier charges, payment and coordination. Include obligations introduced by selling the combination. |
| margin | Compute incremental and combined C using a consistent cost allocation. A bundle discount must not appear as full revenue in both component reports. |
| cash timing | The second supplier's payment dates can precede customer collection. Record refunds, settlement and any dependency on completing the first exchange. |
| retention dependency | May improve relevance or deepen relationships, but is not inherently required. Test whether the complement supports continued value rather than asserting a retention lift. |
| capacity dependency | Delivery interfaces, specialist availability and support ownership matter; a partner's advertised capacity is not a committed fulfilment resource. |
| risk | Hidden mandatory extras, weak partner quality, conflicts of interest, undisclosed commissions and customers paying twice for previously included work. |

## M05: expansion

**Meaning:** Growth in an existing account's paid footprint, such as more seats, locations, capacity or covered work; may include but is not identical to an upsell. Basis: accepted Stage 2–4 expansion concepts; R07.

| Field | Definition and decision implication |
|---|---|
| value exchange | Extend a useful existing exchange to additional eligible users, units, locations or needs. Confirm those additions receive value rather than merely increasing contracted quantity. |
| payer | Existing contracting payer or newly authorised business unit, with budget, purchasing and allocation responsibility explicit. |
| pricing unit | Added seat, location, capacity block, coverage or agreed scope difference per period. Distinguish committed quantity from measured active usage. |
| gross revenue | G for expansion analysis is the incremental paid footprint. The total account invoice may be larger; aggregate it once and reconcile baseline plus net expansion. |
| direct costs | Additional provisioning, rollout, integration, support, usage and account-management work. Identify non-linear capacity steps rather than assuming zero incremental cost. |
| margin | Compare incremental C, total-account C and any volume concession to the existing base. Expanded revenue need not improve account contribution. |
| cash timing | New delivery may start before a co-termed renewal payment. Record proration, payment milestones, customer acceptance and delayed collection. |
| retention dependency | Depends on continuing value in both original and added populations; expansion cannot erase contraction/churn elsewhere in the account or cohort. |
| capacity dependency | Concurrent seats, sites, support load and rollout work may create new constraints. Check the marginal expansion rather than an average historical account. |
| risk | Shelfware, expansion without adoption, giving discounts to all units unintentionally, concentration and counting the uplift again inside renewal totals. |

## M06: renewal

**Meaning:** A decision/event extending an expiring entitlement or relationship; distinguish it from an instalment under an already accepted term. Basis: Stage 4 continued-value evidence; R07, R10.

| Field | Definition and decision implication |
|---|---|
| value exchange | Continued value over a new term with stated scope and any changes. The customer's understanding of renewal and exit matters alongside the transaction event. |
| payer | The current authorised renewal/budget decision-maker and paying entity; authority and needs may have changed since the first purchase. |
| pricing unit | Renewed account, licence, membership or service term, including quantities, price changes and any separate expansion lines. |
| gross revenue | G is the new term's consideration, counted once; it is not an additional total on top of the same recurring-revenue ledger. Separate expansion and discount attribution. |
| direct costs | Future-term fulfilment and support, renewal service/administration, payment handling and obligations retained from the prior term. Do not assume renewal has zero selling cost. |
| margin | Evaluate C for the renewed scope and price, not historic acquisition-period margin alone. Include concessions and changed delivery costs before calling renewal attractive. |
| cash timing | Advance renewal, arrears and late payments differ. A notice, signed renewal or invoice is not yet usable cash; preserve possible cancellation/refund consequences. |
| retention dependency | A renewal is scoped retention evidence, not proof of satisfaction or infinite continuation. Keep eligible starting cohort, dates and non-renewals visible. |
| capacity dependency | Continuing service and clustered renewal workload must be resourced. Annual sales peaks do not justify unavailable support throughout the new term. |
| risk | Surprise price/term changes, hidden automatic renewal, inertia treated as consent/value, forecast renewals booked as cash and double counting recurring totals. |

## M07: usage

**Meaning:** Consideration varies with defined consumption or activity, potentially combined with a base commitment. Basis: R07–R08.

| Field | Definition and decision implication |
|---|---|
| value exchange | Customer obtains a measured service or consumed resource; establish why the billable unit is intelligible and reasonably related to the exchange. |
| payer | Contracting account responsible for consumption, which may be generated by several users or systems. Define authorised usage and budget visibility. |
| pricing unit | Explicit event/unit and measurement period, aggregation, included allowance, bands, overage, cap and correction policy. Volume and graduated formulas differ. |
| gross revenue | G follows the actual quantity formula plus any base fee, without adding a second hypothetical per-unit estimate to the same transaction. Reconcile credits once. |
| direct costs | Metered resource, delivery, infrastructure, supplier, support and transaction costs with their own units. The supplier's charging unit may differ from the customer's. |
| margin | Calculate C across zero, threshold, normal and high usage and relevant customer mixes. An average margin can hide loss-making bands or expensive bursts. |
| cash timing | Prepaid credits, arrears invoices and supplier settlement create distinct funding needs. Credit expiry, refunds and reconciliation are term-dependent, not automatically available income. |
| retention dependency | Future consumption depends on continued use and value; unused commitments do not prove customer benefit or a reliable future usage stream. |
| capacity dependency | Peak throughput, concurrency and supplier limits can bind despite low average usage. Include measurement and dispute-handling capacity. |
| risk | Bill shock, disputed/duplicate measurements, price cliffs, unbounded supplier cost, opaque overages and consumption forecasts mistaken for committed receipts. |

## M08: services

**Meaning:** Human or operational work, access to expertise or reserved capability supplied under a bounded service agreement. Basis: R01, R09 and accepted delivery/retainer research.

| Field | Definition and decision implication |
|---|---|
| value exchange | Defined work, deliverable, outcome support or reserved availability. Clarify whether the buyer pays for time, result, capacity or a combination. |
| payer | Client entity or individual agreeing the service, with budget and acceptance authority. End users or beneficiaries may be different parties. |
| pricing unit | Hour/day, milestone, project, retained capacity, service period or verified performance component, with scope and change terms. |
| gross revenue | G is the agreed fee or verified billable quantity/outcome for the period. Quoted pipeline, unapproved extras and potential success fees are not completed sales. |
| direct costs | Delivery labour, subcontractors, travel/materials, tooling, rework, support and directly attributable coordination. Disclose founder time and subcontractor obligations. |
| margin | Compare C by actual workload and realistic billable capacity; separate incremental cash from opportunity/full-cost views. Do not call uncosted owner labour profit. |
| cash timing | Deposits, milestone acceptance, retainers and arrears can leave payroll/subcontractor costs ahead of collection. Performance disputes may extend the gap. |
| retention dependency | Not necessary for a standalone project; repeat or retained service requires an ongoing need and dependable quality, not an assumed permanent client. |
| capacity dependency | Qualified people, scheduling, bottleneck expertise and client participation constrain delivery. More signed work does not create additional usable hours. |
| risk | Scope creep, uncertain acceptance, underpriced rework, misallocated outcome risk, concentration and impossible unlimited-service promises. Route regulated work and contractual questions. |

## M09: licensing

**Meaning:** Permission to exercise defined rights under agreed conditions, distinct from transferring ownership. Basis: R12; R13 for open-source boundaries.

| Field | Definition and decision implication |
|---|---|
| value exchange | Authorised use of specified software, content, IP or another right, with scope, term, territory and restrictions established by the actual grant. |
| payer | Licensee or authorised intermediary owing the fee; users and downstream recipients may have different rights and obligations. |
| pricing unit | Licence, seat, installation, permitted use, territory, period or contractually defined royalty base. Specify whether maintenance/hosting is included or separate. |
| gross revenue | G is the business's own licence consideration or verified contractual royalty amount. Do not count the licensee's whole downstream sales as licensor revenue. |
| direct costs | Rights acquisition/royalty obligations, delivery, rights administration, metering/audit, included support and enforcement-related provision where relevant and evidenced. |
| margin | Compute C under the actual rights and service scope; low reproduction cost does not erase support, maintenance or third-party royalties. |
| cash timing | Upfront fees, minimum commitments and arrears royalties differ; usage reporting, audit and collection can delay receipts while obligations continue. |
| retention dependency | Term licences require continuing utility for renewal; a perpetual licence may have no repeat fee while still carrying specified continuing obligations. |
| capacity dependency | Rights clearance, distribution, support and update commitments may constrain volume even where digital reproduction itself is cheap. |
| risk | Missing chain of title, incompatible licences, excessive promises, uncollectible royalties and confusing software permissions with trademark or other rights. Required specialist review blocks the affected grant. |

## M10: marketplace take rate

**Meaning:** The platform's own consideration for enabling an exchange between other parties, under an explicitly described role and payment arrangement. Basis: R14 and Stage 4 multi-sided model.

| Field | Definition and decision implication |
|---|---|
| value exchange | Matching, trust, transaction support or related platform service connects distinct sides. Specify who supplies the underlying product and who owes refunds/fulfilment. |
| payer | Seller, buyer, both or another party paying the platform fee under actual terms. The payment processor is not thereby the economic customer. |
| pricing unit | Percentage of a defined eligible transaction base, fixed completed-transaction fee or clearly separated service charge; specify exclusions and cancellations. |
| gross revenue | G for an intermediary fee comparison is the platform fee, not gross merchandise value or seller funds. Actual principal/agent accounting classification requires appropriate evidence/review. |
| direct costs | Allocated payment costs, identity/trust operations, support, dispute/fraud losses, incentives and transaction services. State which party bears each cost. |
| margin | Calculate C from own fee consideration after adjustments and K. A high headline take rate does not show contribution after subsidies or losses. |
| cash timing | Customer receipt, held funds, seller transfer, refunds and processor settlement must reconcile. Funds owed to others are not unrestricted operating cash. |
| retention dependency | Repeated useful participation may be needed on both sides; supply listings do not prove buyer demand or repeat completed matching. |
| capacity dependency | Liquidity in the relevant time/location/category, transaction operations and trust/support capacity can constrain viable volume. Avoid a universal marketplace-liquidity score. |
| risk | Miscounted GMV, seller-fund misuse, disintermediation, fraud, one-sided incentives and unclear refund/regulated-payment responsibilities. |

## M11: advertising

**Meaning:** A third party pays for a defined advertising placement, exposure, action or sponsorship rather than necessarily paying for the audience's primary product. Basis: R15; Stage 1 claims/privacy boundary.

| Field | Definition and decision implication |
|---|---|
| value exchange | Advertiser purchases specified access or placement; the audience receives a separate product/experience. Preserve the distinction and the effect on audience trust/value. |
| payer | Advertiser, agency or network owing the placement/action payment. Audience members are not automatically the advertising payer. |
| pricing unit | Agreed placement/period, valid impression, click, qualifying action or sponsorship deliverable. Distinguish bought CPM from a publisher's estimated RPM reporting ratio. |
| gross revenue | G is payable advertising consideration for valid contractual events/placements. Estimated RPM multiplied by traffic is a scenario, not verified receipts; use the correct denominator. |
| direct costs | Content/audience service, ad delivery, sales/agency/network share, moderation, measurement and attributable traffic costs; avoid double counting a net network payout and its gross fee base. |
| margin | Evaluate C after declared shares, invalid-event adjustments and delivery costs. Higher exposure can harm the underlying product, which needs separate outcome evidence. |
| cash timing | Reporting, validation, adjustments, payout thresholds and payment cycles may delay cash. Record actual terms rather than assuming every dashboard estimate is immediately payable. |
| retention dependency | Audience relevance and continued participation affect future inventory; advertiser renewal depends on its own value evidence. Neither follows automatically from raw traffic. |
| capacity dependency | Suitable inventory, user-experience limits, sales/moderation and measurement quality bound monetisable exposure. Do not equate all page views with sold valid impressions. |
| risk | Privacy/consent and child-user issues, misleading sponsored content, invalid traffic, network concentration and estimated earnings presented as collected income. |

## M12: affiliate / referral revenue

**Meaning:** Consideration for a qualifying introduction/action defined by another party's programme or agreement. Basis: R16–R17; Stage 2 partner/referral research.

| Field | Definition and decision implication |
|---|---|
| value exchange | A relevant introduction or recommendation connects an audience/customer with a provider. Identify both the customer benefit and the incentive paid to the referrer. |
| payer | Merchant, provider, network or other contracting party owing commission. The referred customer may pay the merchant, not the referrer's whole business sale. |
| pricing unit | Accepted lead, eligible signup, completed sale, defined revenue share or other explicitly qualifying event; attribution and eligibility terms are material inputs. |
| gross revenue | G is eligible commission consideration, not referred merchant sales. Pending, rejected, duplicate or disputed events remain separate evidence states; expansion does not automatically earn another fee. |
| direct costs | Relevant content/outreach, qualification, account/programme administration, tracking and payment costs. Include commission reversals in adjustments rather than silently inflating gross income. |
| margin | Calculate C on eligible net commission and attributable cost, with clearly labelled allocation for shared audience work. No universal commission rate or conversion assumption. |
| cash timing | Eligibility validation, locking/reversal periods and payout conditions can separate a referral from cash. Verify actual dates and requirements before funding commitments. |
| retention dependency | Some arrangements pay once; others depend on referred-customer continuity. The actual programme determines the dependency, not the label affiliate. |
| capacity dependency | Credible audience access, qualification, provider capacity and relationship maintenance constrain repeatable introductions. Traffic volume alone does not guarantee eligible events. |
| risk | Undisclosed incentives, unsuitable recommendations, attribution loss, disallowed tactics, provider rule changes and contingent commission mistaken for earned/collected cash. |

## M13: open-source commercialisation

**Meaning:** A paid value exchange around an open-source project, not a presumption that every user owes payment or that existing granted rights can be withdrawn. Basis: R13; R12 for separate rights; accepted business-family independence boundary.

| Field | Definition and decision implication |
|---|---|
| value exchange | Hosting, support, implementation, training, maintenance, assurances or another clearly identified paid complement. Separate open permissions from paid services or legitimately separate components. |
| payer | Organisation/person buying that complement or a sponsor under its own arrangement. A contributor, downloader or community user is not automatically a commercial customer. |
| pricing unit | Hosted account/usage, support tier, service project, training event or agreed sponsorship period. Define actual entitlement rather than charging for undefined community goodwill. |
| gross revenue | G is own paid-complement consideration or an explicitly classified sponsorship receipt, counted once under its underlying mechanism. Downloads, stars and community activity are not revenue. |
| direct costs | Maintenance attributable to commitments, hosting, support, security response, integration and delivery labour. Unpaid community contributions are not unlimited guaranteed capacity. |
| margin | Compute C for the paid complement and separately expose maintenance/shared obligations. A profitable service line does not automatically fund every community promise. |
| cash timing | Subscription, project, support and sponsorship schedules differ. Received support fees or donations may carry conditions; no grant or contribution is assumed freely available. |
| retention dependency | Continued usefulness, maintenance, reliability and trust may support repeat purchase/sponsorship. Community adoption is not proof of paid retention or upgrade demand. |
| capacity dependency | Maintainer expertise, support commitments, security work and hosted operations can bind. Do not sell response guarantees dependent on uncommitted volunteer time. |
| risk | Licence/contributor-rights conflicts, confusing trademarks with code rights, unsupported maintenance promises, alienating users by removing accepted value and mistaking adoption for monetisation proof. |

## Selection and sequence rule

Start from the evidenced customer/value exchange and the owner's objective, not the desire to use more models. Select a sufficient mechanism; state any genuinely different payer/side and what value each receives. Compare it against a simpler or unchanged option. Add another revenue step only when it addresses a real additional need with credible delivery, marginal economics, cash and rights. Preserve a no-purchase or unchanged option where applicable and existing commitments in all cases.

Before accepting a combined model, reconcile event identities, line allocations, D/F adjustments, direct/shared costs, future service obligations and counterparty funds across all cards used. Check that the first exchange is not subsidised by invented retention or that payment to one party is not booked as another's revenue. The offer/pricing failure map and synthetic S01–S08 exercise these distinctions. Full operational accounting, experiments and legal handoffs remain their later stages; none of the ten fields above is left for them to invent.
