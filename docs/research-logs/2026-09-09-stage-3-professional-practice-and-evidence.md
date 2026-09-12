# Stage 3 — Professional Practice and Evidence

**Version:** 1.0  
**Date:** 9 September 2026  
**Status:** Research synthesis complete for architectural decisions; context-specific efficacy and source-access gaps remain  
**Branch:** `feat/bootstrap`

## 1. Decision

Retain the twelve capability responsibilities from [Stage 2](2026-09-09-stage-2-five-book-capability-extraction-and-reconciliation.md), but ground their implementation in professional evidence, explicit measurement definitions and bounded experiments rather than book authority. Add no skills at this stage.

The independent evidence supports investigating customers before committing, treating business models as hypotheses, checking economic and operational constraints, and examining measurement validity before causal interpretation. It does not establish a universal growth formula, guaranteed profitable offer, universal payback period, or one experiment appropriate to every business. The records below distinguish empirical findings, professional methods, vendor conventions and our design decisions.

This stage does not close the missing full-book access recorded in the [Stage 2 source register](2026-09-09-stage-2-source-register.md). It supplies independent grounds for neutral capabilities without pretending to verify unseen passages.

## 2. Findings and conditions of use

### Customer evidence and positioning

The UK service-research guidance recommends selecting research methods against actual questions and using evidence from likely users and existing service activity. Its setting is public-service design, not proof of commercial demand. SBA guidance separately addresses demand, alternatives, saturation and price context. Together these support a distinction between understanding a need and demonstrating an economically reachable market. [S01–S02]

Strategyzer's value-proposition material provides a practitioner method for relating customer activities and difficulties to an offering. It is a design aid, not a measurement instrument that converts subjective ratings into willingness to pay. Adopt independently expressed customer/outcome/alternative/evidence fields; do not reproduce the proprietary canvas or make it mandatory. [S03]

**Decision:** Positioning identifies whose decision is being influenced, the alternative they actually consider, the relevant difference and its proof. A persona, keyword count, broad market size or completed canvas cannot independently validate that proposition. Interview findings should be attributed and bounded by recruitment and context; observed purchase behaviour answers a different question from stated preference.

### Experimentation and disciplined stopping

The 2024 Camuffo and colleagues replication reports four randomised trials involving 759 firms, with effects on idea termination and a nuanced pattern of strategic changes. The inspected institutional abstract supports disciplined reconsideration, not a guaranteed profit uplift or a rule to pivot constantly. [S04]

Microsoft's experimentation work shows the role of properly designed controlled tests, while its sample-ratio-mismatch research identifies data-quality failures that can invalidate apparent results. Those publications concern online products; low-volume services and enterprise procurement may require different designs. [S05–S06]

**Decision:** Every test needs a decision it can change, a relevant population, a measurement plan, predeclared interpretation rules and an inconclusive outcome. Validate assignment and instrumentation before interpreting an A/B result. Qualitative discovery is not an underpowered A/B test. A paid pilot may establish feasibility for one customer without proving general demand. Stopping can be a successful learning outcome.

### Pricing, guarantees and conversion

Schmidt and Bijmolt's consumer-goods meta-analysis finds differences between hypothetical and real willingness to pay, with variation by elicitation method and context. Do not transfer its aggregate bias estimate into an automatic correction factor for an individual SaaS or consultancy offer. [S07]

The return-policy meta-analysis by Janakiraman and colleagues distinguishes dimensions of leniency and their effects on purchasing and returns. It does not prove that stronger promises always increase profit, or justify applying retail return findings to professional-service outcome guarantees. [S08]

Baymard's public checkout research identifies usability and cost-presentation problems through user research and benchmarking. Its commercial research summary and mixed study contexts are useful for generating diagnostic hypotheses, not forecasting a particular merchant's uplift. No advertised conversion improvement is adopted as an expected result. [S09]

**Decision:** Compare price and package hypotheses using customer response, relevant costs, obligations and downside. Evaluate conversion together with delivered value and subsequent behaviour. Distinguish message comprehension, willingness to buy, technical completion and suitability of the offer. A guarantee is an obligation with a remedy, not merely persuasive copy.

### Acquisition and attribution

Blake, Nosko and Tadelis's eBay field experiments found materially different paid-search effects across customer groups and divergence from conventional attribution estimates. This is evidence against equating attributed sales with incremental sales, not proof that paid search never works. [S10]

Google's Search documentation describes the platform's preference for helpful audience-oriented content. It establishes platform guidance, not a guaranteed route to customers or revenue. [S11]

The referral study by Schmitt, Skiera and Van den Bulte tracks customers at a German bank and reports differences in value and retention across acquisition groups and segments. It is not a randomised demonstration that every referral programme causes the same effect. [S12]

**Decision:** A channel is a hypothesis about reaching the right people at acceptable effort and economics. Separate impressions, contacts, qualified opportunities, customers and retained contribution. Record attribution method and uncertainty. Compare referral incentives with downstream customer quality and cost. No default requires paid ads, outbound, content or multiple channels simultaneously.

### Delivery, finance and business-model structure

ACCA's cost-volume-profit treatment distinguishes contribution and fixed-cost recovery, including assumptions about sales mix. Its working-capital treatment separates collection and payment timing; its throughput discussion illustrates constraints and the possibility that expanding a bottleneck is not financially worthwhile. These are professional analysis methods, not universal parameter values. [S13–S15]

IFRS's public clarification of performance obligations and principal-versus-agent questions establishes why formal revenue treatment can require accounting judgement. The repository will not implement statutory revenue recognition; managerial cash schedules must not be labelled audited accounts. [S16]

Stripe's subscription-analytics documentation provides configurable metric conventions. Its MRR treatment is a vendor definition, not a universal standard; exported definitions, discount settings and treatment of usage or delinquency must accompany data. [S17]

GitLab's public qualification and customer-experience practices demonstrate a concrete enterprise-sales and customer-value operating model. They are one company's practice, not causal evidence or a process to impose on all services. [S18–S19]

Teece's business-model work and Hagiu/Wright's platform analysis provide conceptual grounds for distinguishing value creation, delivery, capture and control over transactions. The inspected abstracts do not establish that a marketplace is preferable to selling a service directly. [S20–S21]

**Decision:** Model the actual payer, user, unit of delivery, obligations and decision rights. A recurring price does not create recurring value. Marketplace transaction volume is not necessarily platform revenue. A solo service must price capacity, non-billable work and collection timing. An operating model should remain useful without software automation or a platform business.

## 3. Professional-practice map

This table is an independent production design informed by the cited sources. Suggested metrics and repair actions are candidate checks, not claims that each source prescribes the complete row. Each commitment remains subject to Stage 1 authority boundaries.

| Practice and decision | Inputs and cheapest useful evidence | Working artefact and measurement | Commitment, failure and repair | Dependencies / sources |
|---|---|---|---|---|
| Customer discovery: which problem merits further work? | Likely users, current behaviour, recruitment limits; observations and focused interviews | Customer/problem record; observed difficulties and alternatives | Do not commission a full build from synthetic personas; investigate missing participants | All models; S01–S02 |
| Market research: is demand reachable? | Segment, geography, substitutes, external data and dates; bounded desk review | Market/alternative brief; addressable access and uncertainty | Broad market totals are not achievable sales; narrow the decision and collect local evidence | All; S02 |
| Positioning: why choose this offer? | Buying context, competing alternatives, proof; comprehension conversation | Positioning statement with evidence links | Do not change the entire segment after one copy failure; distinguish relevance from expression | Buyer/user may differ; S02–S03 |
| Value proposition: what benefit is supported? | Desired outcome, barriers, actual delivery capability | Value/proof map; outcome and time/effort evidence | Claims outrun delivery; narrow or substantiate the promise | S01, S03 |
| Pricing: what price/structure should be tested? | Costs, alternatives, customer response and constraints; limited price conversations or authorised test | Price comparison; response and contribution by compatible unit | Stated WTP is not realised demand; use a relevant behavioural test | S07, S13 |
| Revenue models: who pays for what? | Payer, user, unit, frequency, obligations | Transaction model; gross receipts, net revenue and contribution separately | Forced recurring billing or unsupported extra transactions; simplify the exchange | S16–S17, S20 |
| B2B sales: how does buying progress? | Decision participants, budget/process evidence, delivery needs | Qualification and sales-path brief; stage progression, effort and cycle | Assume one contact can purchase; identify actual approvals and scope | S18 |
| Consumer conversion: where does purchase fail? | Instrumented path, support evidence, usability observation | Conversion diagnosis; denominators, payment failures and comprehension | Treat every abandonment as pricing failure; repair observed friction first | S09 |
| Demand generation: which channel hypothesis fits? | Audience access, intent, offer, cost/time limits | Channel-test brief; qualified response and eventual customer quality | Scale reach without useful progression; test audience/channel fit | S02, S10 |
| Performance marketing: is activity incremental? | Spend, attribution rules, customer history, feasible control | Incrementality question and acquisition economics | Attributed revenue mistaken for causality; use a feasible control or label uncertainty | S10 |
| Content/organic acquisition: what useful demand can content serve? | Real questions, expertise, search/access constraints | Content experiment brief; relevant visits and downstream action | Mass production without useful audience value; narrow topic and verify quality | S11 |
| Referrals/partnerships: do incentives acquire suitable customers? | Referrer relationship, reward, contribution and permissions | Partner/referral hypothesis; retained quality and total incentive cost | Count referred contacts rather than customer value; change incentive or selection | S12 |
| Sales operations: what state and handoff are needed? | Current pipeline, definitions, owners and source records | Minimal stage definitions and handoff; age, completeness and loss reasons | Create a new CRM instead of fixing definitions; use an existing tool | S18 |
| Customer success/retention: is value continuing? | Cohort usage/outcomes, cancellations, service issues | Continued-value review; renewal, retained outcomes and cost to serve | Confuse lock-in with value; repair onboarding or service weakness | S17, S19 |
| Unit economics: does the relevant unit contribute? | Comparable revenue, variable costs, sales/support costs and periods | Reproducible economic worksheet; contribution and sensitivity | Omitted costs or incompatible CAC denominators; reconstruct boundaries | S13 |
| Management accounting: what decision does a cost support? | Avoidable/fixed/variable costs, relevant range and mix | Decision-cost schedule; break-even scenarios | Treat contribution as whole-business profit; add fixed obligations separately | S13, S16 |
| Cash/working capital: can obligations be met? | Dated receipts, payables, inventory, tax inputs and reserves | Cash schedule; minimum balance and exposure windows | Spend advance receipts before fulfilment; cap growth or change supported terms | S14, S16 |
| Operations/capacity: can promised work be delivered? | Available hours, work per unit, rework, support and buffer | Capacity model; load, bottleneck and quality | Raise demand beyond capacity; reduce accepted load or repair the limiting process | S15 |
| Service design: does the whole experience work? | User journey including support/offline steps | Service/handoff brief; task outcome and failure demand | Optimise a screen while support fails; repair the responsible cross-channel step | S01 |
| Subscription businesses: does payment track continued value? | Renewal terms, cohorts, cancellations, delivery and fees | Subscription model; retention, recurring contribution and obligations | Extrapolate indefinite lifetime from little evidence; restrict horizon and show downside | S17, S19 |
| Marketplaces: should exchange be intermediated? | Both sides, transaction control, matching, dispute costs | Multi-sided model; completed matches, liquidity and platform contribution | Build marketplace before demonstrated exchange; test mediated transactions honestly | S16, S21 |
| SaaS: is repeatable software value economically supportable? | Usage, service costs, active cohorts, support and billing definitions | SaaS operating model; activation, outcome retention and cost to serve | Ignore usage costs or import vendor metric semantics silently | S17, S19 |
| Ecommerce: is a fulfilled order viable? | Basket, returns, shipping, payment fees and inventory | Order economics and cash schedule; net contribution and returns | Optimise checkout against unprofitable orders; repair pricing, cost or supply | S08–S09, S13–S14 |
| Professional services: can one operator honour the scope? | Delivery/non-billable hours, rates, terms, pipeline and skills | Scope/capacity proposal; effective rate, utilisation and receipts | Forecast full utilisation plus unlimited sales; constrain workload and revise scope | S13–S15, S18 |
| Experiments/A-B tests: can evidence change a decision? | Hypothesis, population, measurement/assignment plan | Experiment record; decision signal, data quality and guardrails | Invalid instrumentation or post-hoc criteria; repair test, not declare success | S04–S06 |
| Product-market fit: how repeatable is value and demand? | Customer, repeat behaviour, acquisition/delivery evidence | Bounded fit assessment, not one score | Declare fit from a survey threshold or a few wins; state the scope of support | S03–S04, S17 |
| Business-model innovation: which relationship should change? | Current model, alternatives, evidence and constraints | Alternative-model comparison and smallest adequate test | Redesign every component at once; isolate a consequential relationship | S20–S21 |

## 4. Evidence policy

Maintain two distinct assessments: **what a source can establish** and **whether it applies to this decision**. A binding contract can constrain execution without demonstrating demand; a controlled experiment can support a causal estimate in one population without settling legality or cross-market transfer.

For each material claim capture ID, statement, source locator, observed/assumed/synthetic status, collection/publication date, population, method, limitations and the decision affected. Corroborating sources must be independent where independence is claimed. A vendor's docs prove a documented behaviour, not commercial effectiveness.

For a causal claim prefer applicable, well-designed causal evidence; inspect measurement and external validity. For customer understanding use relevant observations and qualitative evidence with recruitment limits. For arithmetic use reproducible calculations from attributable inputs. For legal activation use current jurisdiction-specific review. For an untested commercial mechanism preserve hypothesis status even when supported by an expert framework.

Absence of evidence is not automatic evidence of failure. Equally, unknown evidence is not a pass. Synthetic fixtures are useful for testing skill behaviour and must never be represented as actual customers, interview results, willingness to pay or business traction.

## 5. Terminology map

| Ambiguous term | Operational meaning required here |
|---|---|
| Lead | Define whether it is a contact, expressed interest or qualified prospect; preserve denominator |
| Conversion | Named transition, population, window, attribution and exclusions |
| Value | Customer benefit, delivered outcome, or economic value; specify which |
| Revenue | Accounting/reported or managerial measure with basis; not automatically cash received |
| Contribution | Revenue less the stated variable-cost boundary; not net profit |
| CAC | Specified acquisition costs divided by a matched acquired-customer population; label attribution |
| LTV | Observed finite-horizon contribution or explicit forecast; never silently mix them |
| Retention | Named customer/revenue/outcome cohort and time window; gross and net are different |
| Payback | Define cash or contribution recovery and horizon; not a universal ratio target |
| Validation | Evidence supporting a bounded claim under stated conditions, not permanent certainty |
| Constraint | An evidenced limiting relationship for the chosen objective; not just the worst-looking metric |
| Approval | Permission for a bounded action; not proof of effectiveness or professional sign-off |

## 6. Failure taxonomy and repair ownership

| Failure | First investigation | Smallest responsible repair |
|---|---|---|
| F01 Unsupported customer/market claim | Provenance, recruitment, observed versus synthetic | Collect relevant evidence or narrow the claim |
| F02 Offer/proof mismatch | Outcome, delivery capability and wording | Remove or substantiate unsupported promise |
| F03 Invalid price inference | Elicitation method, segment and alternatives | Test an explicit price hypothesis |
| F04 Acquisition vanity | Qualification, attribution and downstream value | Correct channel/measurement before scale |
| F05 Sales-path mismatch | Buyer authority, cycle, qualification and friction | Repair stage or handoff |
| F06 Unviable delivery | Capacity, quality, rework and scope | Reduce load or fix the binding delivery step |
| F07 Economic boundary error | Costs, units, periods and cohorts | Recalculate before recommendation |
| F08 Cash-timing failure | Obligations versus receipts | Constrain spend/growth or revise authorised terms |
| F09 Retention/value failure | Cohort outcomes, cancellations and support | Repair value or onboarding, not cancellation friction |
| F10 Invalid experiment | Assignment, instrumentation, confounders and rule | Repair or repeat; keep outcome inconclusive |
| F11 Overbroad redesign | Alternative causes and accepted decisions | Restrict mutation scope to evidenced causes |
| F12 Authority/professional gap | Action scope, approvals and legal dependencies | Block affected execution and issue a review brief |

## 7. Reconciliation of Stage 2 conflicts

T01 and T06 retain bounded learning but reject inadequate quality. T02 adds attribution and capacity checks to lead quality. T03 and T08 require a dated obligation/cash view, not a short-payback slogan. T04 remains evidence-led pricing. T05 retains guarantee options without a universal profit claim. T07 keeps comparison questions without summed-score gates. T09 retains preservation but permits evidence-supported structural change. T10 preserves stable and bespoke business objectives. T11 remains a non-negotiable truthfulness boundary, irrespective of claimed commercial results.

The evidence does not justify changing the Stage 1 ownership boundary. It does justify explicit measurement validation within acquisition, economics, experiments and diagnosis. No new universal score, ontology or executive-agent team is needed.

## 8. Limits and next-stage handoff

Research depth is uneven. Full methods/data were not inspected for every paper; several sources are accessible abstracts, institutional summaries or practitioner documentation. No new field study was conducted. No quantitative effect in a cited study becomes a default product forecast. Positioning, enterprise selling and customer success remain primarily method/practice evidence in this pass. Model-specific performance, legal conclusions and each business's actual demand remain open.

Stages 4–8 must translate the decisions into small working models and checkable contracts. Stage 9 must verify current legal handoff surfaces. Stage 10 must assess tools and licences separately from the quality of their marketing. Stages 17 and 22–24 must distinguish deterministic fixtures, authored examples and actual agent executions.

**Exit assessment:** All required professional-practice areas have an explicit decision/input/artefact/metric/commitment/failure/repair map. The core principles have grounds independent of the five-book corpus, with limits recorded. This satisfies the architectural research exit, not universal empirical validation.

## 9. Sources inspected

Access date for all web sources: 9 September 2026. Undated pages are live professional/vendor guidance. No paywalled full text, embedded videos or PDF figures are represented as inspected in this stage.

- **S01:** Government Digital Service, [Plan user research for your service](https://www.gov.uk/service-manual/user-research/plan-user-research-for-your-service) and [Learning about users and their needs](https://www.gov.uk/service-manual/user-research/start-by-learning-user-needs). Professional guidance; method and evidence selection sections.
- **S02:** US Small Business Administration, [Plan your business: market research and competitive analysis](https://www.sba.gov/counseling/plan-your-business/). Professional guidance; market research section. Original business-guide URL redirected here.
- **S03:** Strategyzer, [The Value Proposition Canvas](https://www.strategyzer.com/library/the-value-proposition-canvas). Creator's public explanation; tool not reproduced.
- **S04:** Camuffo et al. (2024), [A Scientific Approach to Entrepreneurial Decision Making: Large Scale Replication and Extension](https://openaccess.city.ac.uk/id/eprint/32437/), Strategic Management Journal 45(6), 1209–1237, DOI 10.1002/smj.3580. Institutional abstract inspected; full paper not claimed read.
- **S05:** Kohavi et al. (2009), [Online Experimentation at Microsoft](https://www.microsoft.com/en-us/research/publication/online-experimentation-at-microsoft/). Author organisation publication summary.
- **S06:** Fabijan et al. (2019), [Diagnosing Sample Ratio Mismatch in Online Controlled Experiments](https://www.microsoft.com/en-us/research/publication/diagnosing-sample-ratio-mismatch-in-online-controlled-experiments-a-taxonomy-and-rules-of-thumb-for-practitioners/). Author organisation publication summary.
- **S07:** Schmidt and Bijmolt (2020; online 2019), [Accurately measuring willingness to pay for consumer goods](https://link.springer.com/article/10.1007/s11747-019-00666-6). Open HTML article; abstract, method context and limitations.
- **S08:** Janakiraman, Syrdal and Freling (2016), [The Effect of Return Policy Leniency on Consumer Purchase and Return Decisions](https://www.sciencedirect.com/science/article/pii/S0022435915000822), DOI 10.1016/j.jretai.2015.11.002. Publisher-indexed abstract/highlights; full page retrieval failed, full methods not claimed inspected.
- **S09:** Baymard Institute, [Cart and Checkout Usability Research](https://baymard.com/research/checkout-usability). Public research/method summary, not premium dataset or report.
- **S10:** Blake, Nosko and Tadelis (2014 working paper; 2015 journal version), [Consumer Heterogeneity and Paid Search Effectiveness](https://www.nber.org/papers/w20171). Author working-paper abstract and publication record.
- **S11:** Google Search Central, [Creating helpful, reliable, people-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content). Platform guidance, not efficacy study.
- **S12:** Schmitt, Skiera and Van den Bulte (2011), [Referral Programs and Customer Value](https://journals.sagepub.com/doi/10.1509/jm.75.1.46). Publisher abstract and study context.
- **S13:** ACCA, [Cost-volume-profit analysis](https://www.accaglobal.com/gb/en/student/exam-support-resources/fundamentals-exams-study-resources/f5/technical-articles/CVP-analysis.html). Professional education; contribution, break-even and mix assumptions.
- **S14:** ACCA, [Working capital management](https://www.accaglobal.com/gb/en/student/exam-support-resources/fundamentals-exams-study-resources/f9/technical-articles/wcm.html). Professional education; cash cycle and liquidity/profitability tradeoffs.
- **S15:** ACCA, [Throughput accounting](https://www.accaglobal.com/gb/en/student/exam-support-resources/fundamentals-exams-study-resources/f5/technical-articles/throughput-constraints2.html). Indexed professional text; no embedded table values used.
- **S16:** IFRS Foundation (2016), [Clarifications to IFRS 15 Revenue from Contracts with Customers](https://www.ifrs.org/projects/completed-projects/2016/clarifications-to-ifrs-15-revenue-from-contracts-with-customers/). Public scope/clarification notice; not a complete current standards review.
- **S17:** Stripe, [Subscription analytics](https://docs.stripe.com/billing/subscriptions/analytics). Metric definitions and configuration sections; vendor conventions.
- **S18:** GitLab, [Sales discovery and qualification questions](https://handbook.gitlab.com/handbook/sales/qualification-questions/) and [Sales](https://handbook.gitlab.com/handbook/sales/). Public operating practice, not a universal sales method.
- **S19:** GitLab, [Customer Experience](https://handbook.gitlab.com/handbook/customer-success/). Public mission and outcome measures.
- **S20:** Teece (2010), [Business Models, Business Strategy and Innovation](https://www.sciencedirect.com/science/article/pii/S002463010900051X), DOI 10.1016/j.lrp.2009.07.003. Publisher-indexed abstract; full page retrieval failed.
- **S21:** Hagiu and Wright (2015), [Multi-Sided Platforms](https://doi.org/10.2139/ssrn.2794582). Author-deposited abstract retrieved in search; direct page retrieval failed. Conceptual model, not a claim of empirical marketplace superiority.

*Stage 3 · Version 1.0 · 9 September 2026.*
