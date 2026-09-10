# Stage 5 research and design checks

**Date:** 10 September 2026  
**Branch:** `feat/bootstrap-2`  
**Authority:** [Original bootstrap §12](2026-09-08-business-building-skills-new-project-bootstrap-process.md).  
**Outputs:** [Offer and pricing architecture](2026-09-10-stage-05-offer-and-pricing-architecture.md), [money-model taxonomy](2026-09-10-stage-05-money-model-taxonomy.md), [conformance](2026-09-10-stage-05-conformance.md).  
**Evidence boundary:** Source-grounded design, with explicitly synthetic arithmetic and manual design checks. No customer study, live price change, installed skill or commercial-effect benchmark is claimed.

## 1. Inputs and research method

The original specification on `main` was read before authoring, including all of §12 and the governing principles, acceptance gates and non-goals. Its blob remained `a0ac1b6c78a0cde8ccd9aca6fda6c5b0880c516d`. The accepted starting commit was `b555558b93d0c625018b48fa5694fa4f3872b887`. Stage 4's verified model is the immediate customer/value input.

Earlier material inspected: the [Stage 1 professional boundary](2026-09-09-stage-01-domain-and-professional-boundary.md), [Stage 2 matrix](2026-09-09-stage-02-source-to-capability-matrix.md), relevant pricing/revenue cards in the [Stage 3 practice map](2026-09-10-stage-03-professional-practice-map.md), its [evidence register](2026-09-10-stage-03-evidence-and-terminology.md), and the complete [Stage 4 model](2026-09-10-stage-04-business-customer-and-value-model.md) and completion receipt. In particular, the Offers pricing/packaging/guarantee rows, Money Models transaction/continuity/payment rows and cross-book reconciliation remain hypotheses qualified by Stage 3 research. The books were not reopened or republished in this stage.

Research proceeded through three question groups: pricing bases and payment/risk allocation; empirical limits of willingness-to-pay, bundling, returns and freemium; and payer/rights/settlement differences in licensing, marketplaces, advertising, referrals and open-source commercialisation. Targeted searches were followed by primary documentation, author/publisher pages and current official guidance. The register records the material actually available, not a claim to have read every linked paper, regulation or provider manual. No provider was selected or installed.

All external sources below were accessed on **10 September 2026**. Live guidance must be reverified before a later customer-specific decision. UK, US and Australian material retains its jurisdiction and purpose; it is not universal legal advice or approval to publish terms. Vendor documentation establishes that a charging mechanism exists, not its suitability or causal commercial benefit. Definitions and decision rules in the companion outputs are independently expressed project synthesis, not verbatim claims attributed to every source cited beside them.

## 2. Primary-source register and retained limits

<a id="r01"></a>
### R01: ACCA, Pricing 2: Practical aspects

[Primary source](https://www.accaglobal.com/gb/en/student/exam-support-resources/fundamentals-exams-study-resources/f5/technical-articles/pricing-2.html). Professional education; HTML sections on pricing influences, marginal/absorption/lifecycle/relevant costs and limitations of cost-plus read. Costs, customers and alternatives answer different questions. A computed price need not produce sales. **Application:** show cost scope and test demand separately. **Limit:** instructional methods, not a calibrated price recommendation for a particular business; no source examples or cost amounts are reused.

<a id="r02"></a>
### R02: Australian Government, Choose a pricing strategy

[Primary source](https://business.gov.au/products-and-services/choose-a-pricing-strategy). Official business guidance; pricing-goal, cost, market/competitor, capacity, strategy and testing material retrieved. **Application:** compare appropriate pricing bases against the business objective and available evidence. **Limit:** general guidance, not proof of demand. The page also refers to future Australian payment rules; those are not adopted as current rules or transposed to other jurisdictions. The project distinguishes markup from margin explicitly rather than treating them as interchangeable.

<a id="r03"></a>
### R03: Schmidt and Bijmolt, Accurately measuring willingness to pay for consumer goods

[Publisher article](https://link.springer.com/article/10.1007/s11747-019-00666-6), DOI `10.1007/s11747-019-00666-6`; published online 2019, journal volume 2020. Empirical meta-analysis; HTML abstract, methods/results discussion and contextual moderators inspected. Hypothetical and actual willingness to pay differ, with variation across settings and methods. **Application:** separate a survey answer, accepted quote and actual payment at specified terms. **Limit:** no pooled percentage becomes a universal correction factor, local demand estimate or guaranteed experimental sample size.

<a id="r04"></a>
### R04: Bakos and Brynjolfsson, Bundling Information Goods: Pricing, Profits and Efficiency

[Author-hosted abstract](https://pages.stern.nyu.edu/~bakos/big-abstract.html), 1999. Formal economic analysis; abstract and its conditions read, not the full paper. **Application:** evaluate customer usefulness and incremental delivery cost before bundling. **Limit:** the information-goods model does not establish that bonuses improve every service offer or that costly human delivery has negligible marginal cost.

<a id="r05"></a>
### R05: Janakiraman, Syrdal and Freling, The Effect of Return Policy Leniency on Consumer Purchase and Return Decisions

[Publisher DOI](https://doi.org/10.1016/j.jretai.2015.11.002), Journal of Retailing 92(2), 2016. Meta-analytic review; publisher-indexed abstract/highlights retrieved. The five dimensions of return-policy leniency do not have identical purchase/return effects. **Application:** distinguish remedy conditions and model refund consequences rather than assuming a generous guarantee creates profit. **Limit:** the DOI page returned an access error; no full-paper reading or local refund-rate estimate is claimed. Ordinary product returns are not evidence for an untested earnings guarantee.

<a id="r06"></a>
### R06: Rietveld, Creating and capturing value from freemium business models: A demand-side perspective

[Publisher abstract](https://sms.onlinelibrary.wiley.com/doi/abs/10.1002/sej.1279), first published 2017, journal issue 2018. Empirical digital-game study; abstract and managerial summary read. Reported freemium/premium differences and variation in paid options are setting-specific. **Application:** test free-to-paid economics, continued use and package fit rather than assuming free acquisition pays for itself. **Limit:** not a causal universal rule favouring either model; no unobserved conversion rate imported into this project.

<a id="r07"></a>
### R07: Stripe, Design a subscriptions integration

[Provider documentation](https://docs.stripe.com/billing/subscriptions/design-an-integration). Pricing-model and collection-choice descriptions read. Flat, seat, usage and mixed structures separate what is billed from when money is collected. **Application:** represent charging unit, cadence and payment structure independently. **Limit:** descriptive vendor capability, not provider selection, implementation verification or evidence of customer acceptance.

<a id="r08"></a>
### R08: Stripe, Set up tiered pricing

[Provider documentation](https://docs.stripe.com/subscriptions/pricing-models/tiered-pricing). Volume and graduated calculation sections read. **Application:** distinguish product-package tiers from quantity bands; test boundary quantities with the actual formula. **Limit:** a billing feature is not a profitable offer. The synthetic numbers below are original, not the provider's examples or fees.

<a id="r09"></a>
### R09: UK Cabinet Office / Government Commercial Function, Risk Allocation and Pricing Approaches guidance note

[Official HTML guidance](https://www.gov.uk/government/publications/the-sourcing-and-consultancy-playbooks/risk-allocation-and-pricing-approaches-guidance-note-html). Pricing/payment, outcome risk, volume uncertainty and allocation discussions inspected. **Application:** align a service commitment with scope control, measurable outcomes, capacity variation and who can manage the risk. **Limit:** public-procurement guidance informs commercial design questions; it is not a legal opinion on a private contract or a mandate to use performance fees.

<a id="r10"></a>
### R10: UK CMA, Providing clear and accurate information about prices: summary

[Official guidance](https://www.gov.uk/government/publications/price-transparency-cma209/providing-clear-and-accurate-information-about-prices-summary), updated 7 January 2026. Total-price, unavoidable-charge, calculation-method and periodic-price guidance read. **Application:** retain the complete customer obligation and payment schedule, not only an attractive instalment. **Limit:** UK consumer-price guidance; customer-specific application and exceptions require the proper review. No legal clearance is inferred from completing the architecture.

<a id="r11"></a>
### R11: ASA / CAP, Non-broadcast Code section 03: Misleading advertising

[Official code](https://www.asa.org.uk/type/non_broadcast/code_section/03.html). Substantiation, limitations, pricing/comparisons, availability, testimonials and guarantee provisions inspected, including 3.55–3.57. **Application:** require substantiated claims and usable remedy terms before publication. **Limit:** retain UK non-broadcast scope; source compliance questions go to the specialist, and compliance is not a commercial-effect result. This record does not reproduce the code or draft contract clauses.

<a id="r12"></a>
### R12: WIPO, IP Assignment and Licensing

[Official explanation](https://www.wipo.int/en/web/business/assignment-licensing). Licensing versus assignment and compensation descriptions read. **Application:** specify the rights, scope and payer before modelling licensing income; payment can take different contractual forms. **Limit:** owning an asset or seeing a licence example is not proof of authority to grant particular rights. The separately inspected WIPO Earn page does not replace the actual licence or chain-of-title review.

<a id="r13"></a>
### R13: Open Source Initiative, Frequently Answered Questions

[Organisation's FAQ](https://opensource.org/faq), commercial use and Commerce and Open Source sections read. Commercial activity and open-source permissions can coexist; services, maintenance and other complements differ from exclusive control of already granted code rights. **Application:** identify the paid complement and respect existing licences. **Limit:** source licensing explanations are not a project-specific legal determination; trademark, contributor rights and different components need their own assessment.

<a id="r14"></a>
### R14: Stripe, Collect application fees

[Provider documentation](https://docs.stripe.com/connect/marketplace/tasks/app-fees). Application-fee, payment-split and settlement discussion read. **Application:** distinguish platform fees from seller funds and model the platform's actual allocated processing/dispute costs. **Limit:** allocation differs with payment configuration and agreements; no single provider fee rate, principal/agent accounting conclusion or available-cash assumption is adopted. Embedded installation instructions were not executed.

<a id="r15"></a>
### R15: Google AdSense, Revenue per thousand impressions (RPM)

[Provider metric definition](https://support.google.com/adsense/answer/190515?hl=en). Definition and calculation explanation read. **Application:** preserve the denominator and distinguish normalised estimated revenue from final receipts. **Limit:** no RPM benchmark, audience value, fill rate or future ad income is supplied by this definition. Provider/platform rules and commercial rates remain context-specific inputs.

<a id="r16"></a>
### R16: US FTC, FTC's Endorsement Guides: What People Are Asking

[Official guidance](https://www.ftc.gov/business-guidance/resources/ftcs-endorsement-guides-what-people-are-asking). Affiliate/network marketing and material-connection disclosure sections read. **Application:** record the incentive and disclosure review alongside the commission mechanism. **Limit:** US guidance, not a universal disclosure template or evidence that any referred product is suitable. No outreach, endorsement or publication was authorised by this research.

<a id="r17"></a>
### R17: HubSpot, Affiliate Program Agreement

[Provider's English agreement](https://legal.hubspot.com/affiliate-program-agreement), modified 23 February 2026. Definitions, customer-transaction eligibility, acceptance/validity and commission/payment sections read. **Application:** separate referred traffic, qualifying events, conditional commission and payment; do not assume later expansion earns another commission. **Limit:** one programme's contract illustrates why terms matter, not an industry-wide rate, lock period or guaranteed income. No affiliate enrolment or agreement acceptance occurred.

### Search limitations and excluded material

The Amazon Associates schedule request failed with HTTP 503; no Amazon commission or payout facts are asserted. A Salesforce learning-centre link redirected to a generic resource page, so it was not used as a fully read definition article. The return-policy DOI returned 403/access errors; R05 is limited to the publisher-indexed abstract. Search results from secondary aggregators and promotional claims were not substituted for primary empirical evidence. No book files, private customer data, external commercial examples, full papers or screenshots were copied into the repository.

## 3. Reconciliation and design decisions

**Offer appeal versus fulfilment.** Accepted book concepts about outcomes, components, proof and risk reduction are retained as candidate choices, not a requirement to add every persuasion device. R04–R05 limit extrapolation about bundles and remedies; Stage 4 supplies the actual customer/value trace. An absent guarantee or bonus can be the correct choice. Delivery and cash feasibility cannot be inferred from apparent appeal.

**Several pricing lenses, not a price formula.** R01–R03 support separate cost, customer and alternative questions. The architecture compares price level, scope, unit and timing without silently changing all four. Survey responses do not become paid demand. A deliberately loss-making bounded learning offer is possible only as an explicitly funded, authorised choice, not as supposedly profitable scaling based on invented lifetime value.

**Revenue labels are not disjoint accounts.** The thirteen §12 labels mix transaction events, continuation, expansion, units and value mechanisms. A licence may be sold by subscription, renewed and expanded; these tags do not create four separate amounts. The taxonomy preserves each responsibility while recording each transaction once. R07–R09 and R12–R17 inform the mechanism-specific constraints; the no-double-count representation is project synthesis.

**Rights and counterparties change the model.** The party receiving value, paying, collecting funds and owing fulfilment need not be the same. Licensing, intermediary fees, ads, referrals and open-source complements require their own permission, settlement and incentive account. A high nominal margin does not resolve missing rights, deceptive terms or unavailable funds.

Rejected alternatives: a fixed four-step offer ladder for every business; a universal premium-price rule; adding all eight Stage 4 value dimensions or all fourteen offer components regardless of relevance; an invented target margin or LTV/CAC gate; a catalogue of thirteen independent revenue totals; interpreting customer billing as satisfaction; using stronger conversion to override legal/ethical blocks; and implementing a billing platform at this research stage. No current-stage user-owned decision is unresolved.

## 4. Synthetic check protocol

The fixtures below are original and entirely synthetic. Currency units are **CU**, not a jurisdiction or a provider's fees. Each fixture declares only the costs it includes. No residual is called net profit when shared costs, tax or other costs are omitted. Fixed demand/retention assumptions are hypothetical inputs, not forecasts. The deterministic checker in conformance executes the arithmetic; manual review tests the decision trace and preservation boundary. Neither is an installed-agent benchmark.

The fixture descriptions and expected outcomes are specified before execution. Actual output is appended after the checker runs; a numerical expectation alone does not establish a test pass.

### S01: higher conversion, lower contribution

Synthetic objective: compare direct contribution after the same acquisition cost, without exceeding 80 orders of capacity. There are 1,000 eligible opportunities. Baseline: 50 orders at CU100. Alternative: 60 orders at CU80 after a CU20 discount from the genuine CU100 comparison price. Both incur CU60 delivery cost per order, a 5% refund amount, a non-returned processing cost of 3% of charged revenue and CU900 acquisition cost. No shared fixed cost or tax is included. All collections/refunds/costs occur within the comparison period.

Expected baseline: CU5,000 gross, CU250 refunds, CU4,750 net, CU3,150 direct costs, CU1,600 direct contribution and CU700 after acquisition. Alternative: CU6,000 gross before CU1,200 discount, CU240 refunds, CU4,560 net, CU3,744 direct costs, CU816 contribution and **CU−84 after acquisition**. The alternative needs 118 whole orders to match baseline contribution at its CU13.60 unit contribution, beyond capacity. The synthetic conversion increase from 5% to 6% is not an empirical price effect. Disposition: reject this alternative for the declared objective; preserve the customer segment and underlying service rather than redesigning them.

### S02: positive contribution, unaffordable collection timing

Synthetic 100 contracts at CU1,000 each; CU650 cost per contract due day 14; payment otherwise due day 45; opening usable cash CU20,000. Shared costs, fees, taxes and defaults are excluded, not assumed absent in real work. Nominal direct contribution is CU35,000, but minimum cash is **CU−45,000**. Collecting 40% on day 0 leaves a CU−5,000 minimum; collecting 50% leaves CU5,000. Remaining balances arrive day 45. Total price and direct contribution do not change.

Disposition: block the unfunded schedule; compare only the implicated payment/capacity terms. Deposit acceptance and legal appropriateness remain untested, so the feasible synthetic schedule is not an approved customer-facing change or borrowing recommendation.

### S03: a guarantee creates a real exposure

Synthetic 40 orders at CU500, delivery CU300 per order and non-returned 3% processing cost. All delivery is incurred before cash refunds; opening cash other than these receipts is zero. Refund scenarios of 5%, 30% and 100% produce direct contribution of CU6,400, CU1,400 and CU−12,600 respectively. After delivery/processing, CU7,400 remains before refunds, not enough for every possible CU20,000 refund claim.

Disposition: positive expected contribution does not establish a funded remedy or justify an unsupported earnings promise. Model exposure, capability, terms and owner-approved funding; no universal 100%-reserve policy is imposed. Cash refund and store credit remain different remedies. Existing valid customer rights cannot be removed to make the scenario pass.

### S04: quantity tier cliff

Synthetic pricing: first band through 100 units at CU1; the higher-volume band at CU0.60; direct cost CU0.70 per unit; no other costs. For 150 units, volume pricing charges CU90 and produces CU−15 direct contribution. Graduated pricing charges CU130 and produces CU25. At the threshold, the volume bill changes from CU100 for 100 units to CU60.60 for 101 units.

Disposition: inspect the actual formula and boundaries before accepting the price. These quantity bands are not customer-package tiers. Do not silently substitute a graduated formula in an accepted contract or claim all volume pricing is inappropriate.

### S05: free participation is not free delivery

Synthetic monthly population: 100 paying accounts at CU10; paid direct cost CU3/account; 900 free accounts costing CU0.50 each; shared fixed cost CU200. Direct contribution is CU250; after the stated fixed cost the residual is CU50. Add 1,000 free accounts while holding paid accounts constant as a stress assumption: direct contribution becomes CU−250 and the residual CU−450. Acquisition, payment fees and tax are not modelled.

Disposition: free growth alone cannot justify scale. Review conversion/value evidence, resource funding and package boundaries. Do not automatically revoke accepted free entitlements or infer that a premium model would retain the same audience.

### S06: revenue counted once despite several labels

Synthetic canonical events: T1 CU20 first subscription licence; T2 CU35 comprising CU20 renewal and CU15 expanded seats; T3 CU40 complementary consultation. Tags respectively include initial/recurring/licensing, renewal/recurring/expansion/licensing, and services/cross-sell. Total gross commercial consideration is **CU95**, counted once by event, not once per tag. No statutory recognition conclusion is made; recognition periods remain an accounting input.

Disposition: preserve the event identifiers, line allocation and analytical tags. An expansion report may show CU15 while the renewal invoice shows CU35, but adding both again to total business revenue is invalid.

### S07: platform volume is not platform revenue

Synthetic intermediary scenario: CU10,000 seller transactions and a 12% platform fee. CU8,800 is owed to sellers; platform gross consideration is CU1,200. The platform bears CU300 processing, CU100 support and CU200 transaction losses. Its direct contribution is **CU600**. Seller funds are not free working capital. This is an expressly assumed intermediary arrangement, not an accounting principal/agent determination for a real platform.

Disposition: reject a CU10,000 platform-revenue claim and any spending plan that consumes seller funds. Correct the fee/cost/settlement account without automatically changing the customer proposition.

### S08: attractive arithmetic cannot authorise misleading or unlicensed offers

Synthetic submitted proposals: a refund guarantee with material conditions hidden until after payment; a perpetual resetting countdown presented as a real deadline; a licence sale with unverified contributor rights; an undisclosed paid recommendation presented as independent; and ad RPM estimates presented as collected cash. No actual business or person is represented.

Required disposition in each case: reject the unsupported claim or block the affected commitment, identify the missing disclosure/right/measurement, preserve any unaffected accepted offer, and request the appropriate owner/specialist review. A positive spreadsheet result is not a waiver. This is manual semantic review, not legal advice or an executed legal-skills test.

## 5. Executed results and semantic review

The deterministic checker was run with Python 3.13.5 in the document workspace, using the inspected eighteen-file remote-tree path manifest for links to accepted documents. It returned exit code 0: **46 PASS, 0 FAIL**. The exact script is preserved in conformance. These checks establish the stated coverage and synthetic arithmetic, not customer demand or legal compliance.

```text
PASS | offer: all 14 literal topics
PASS | offer: substantive definition and boundary
PASS | pricing: all 14 literal topics
PASS | pricing: substantive definition and boundary
PASS | 13 literal model headings
PASS | M01: ten substantive fields
PASS | M02: ten substantive fields
PASS | M03: ten substantive fields
PASS | M04: ten substantive fields
PASS | M05: ten substantive fields
PASS | M06: ten substantive fields
PASS | M07: ten substantive fields
PASS | M08: ten substantive fields
PASS | M09: ten substantive fields
PASS | M10: ten substantive fields
PASS | M11: ten substantive fields
PASS | M12: ten substantive fields
PASS | M13: ten substantive fields
PASS | 130 required model fields
PASS | 17 source records with resolvable local anchors
PASS | source access date and limitations explicit
PASS | all synthetic fixtures present
PASS | 16 failure and repair rows
PASS | no automatic ingredient/score rule
PASS | customer evidence and approved versions preserved
PASS | overlapping labels cannot duplicate transactions
PASS | cash/recognition/tax boundary explicit
PASS | current stage does not authorise implementation
PASS | all relative documentation links resolve
PASS | S01 baseline economics: (Decimal('5000'), Decimal('0'), Decimal('250.00'), Decimal('4750.00'), Decimal('3150.00'), Decimal('1600.00'))
PASS | S01 discounted economics: (Decimal('6000'), Decimal('1200.00'), Decimal('240.0000'), Decimal('4560.0000'), Decimal('3744.0000'), Decimal('816.0000'))
PASS | S01 acquisition-adjusted contribution: (Decimal('700.00'), Decimal('-84.0000'))
PASS | S01 capacity cannot restore baseline: 118
PASS | S02 minimum cash: [(Decimal('-45000'), Decimal('55000')), (Decimal('-5000.0'), Decimal('55000.0')), (Decimal('5000.0'), Decimal('55000.0'))]
PASS | S02 timing leaves total contribution unchanged
PASS | S03 refund stress contributions: [Decimal('6400.00'), Decimal('1400.00'), Decimal('-12600.00')]
PASS | S03 refund exposure not fully funded by sale proceeds
PASS | S04 distinct band calculations: (Decimal('90.00'), Decimal('130.00'))
PASS | S04 band contribution and cliff
PASS | S05 free-population contribution: [Decimal('250.0'), Decimal('-250.0')]
PASS | S05 stated fixed-cost residual
PASS | S06 canonical event total and expansion allocation: 95
PASS | S07 own fee and seller funds reconcile
PASS | zero/negative net has no misleading margin percentage
PASS | markup and margin denominators differ
PASS | reported fixture expectations match checked results
TOTAL 46 | PASS 46 | FAIL 0
GIT_BLOB | 2026-09-10-stage-05-offer-and-pricing-architecture.md | e7f4cc70e0f386ec04a9d36f717abbbb378d8916
GIT_BLOB | 2026-09-10-stage-05-money-model-taxonomy.md | d918595ea9d5f3b8f3670078bcf69b4f3be3014d
```

Manual review of S01–S07 traced the stated objective, input assumptions, calculated result and smallest responsible decision. Each retained the distinction between a hypothetical fixture and an observed commercial outcome. S01 preserves the segment while rejecting the loss-making discount; S02 repairs timing without pretending a deposit is accepted; S03 refuses an unsupported/funding-blind promise; S04 preserves actual contractual formula identity; S05 does not revoke free entitlements; S06 reconciles overlapping labels; S07 preserves counterparty funds. All seven passed the design review.

S08 was reviewed against the offer model, failure map and existing professional boundary:

| Synthetic proposal | Actual review disposition | Result |
|---|---|---|
| Material refund conditions appear only after payment | Block the proposed presentation; expose the terms and obtain required review. Existing valid remedy obligations remain intact. | PASS |
| Perpetually resetting countdown presented as a deadline | Reject the unsupported urgency claim; omit it unless a genuine documented constraint exists. The core offer need not be discarded. | PASS |
| Licence sale without confirmed contributor rights | Block the affected rights grant and request the missing rights/specialist evidence; no legal conclusion is invented. | PASS |
| Paid recommendation described as independent | Block the misleading presentation, retain the incentive facts and obtain the appropriate disclosure/claim review. | PASS |
| Estimated RPM presented as collected cash | Correct the evidence state and obtain actual settlement/receipt data; an estimated metric does not fund an obligation. | PASS |

The assistant performing the work conducted this review; no second agent, customer, accountant or lawyer participated. All four §12 outputs were checked after rereading the original Stage 5 section from `main`. Detailed direct conformance and publication requirements are recorded separately. There are no unresolved current-stage user decisions. No Stage 6 work is counted as complete here.
