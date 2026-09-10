# Stage 4: Business-system, customer and value model

**Date:** 10 September 2026  
**Branch:** `feat/bootstrap-2`  
**Authority:** [Original bootstrap v1.1](2026-09-08-business-building-skills-new-project-bootstrap-process.md), §11; applicable §§1–5, 7, 34–36.  
**Record type:** Domain-model design and synthetic traceability review, not observed customer research or an implemented skills product.  
**Acceptance:** [Stage 4 conformance](2026-09-10-stage-04-conformance.md); remote completion belongs in [bootstrap progress](bootstrap-2-progress.md).

## 1. Goal, inputs and evidence boundary

Define the smallest useful representation connecting customer, value and the rest of a business. A later offer or growth recommendation must identify whose progress it serves, the alternative it displaces, the supporting observations and the unresolved assumptions. Unknown demand remains unknown; a complete model description is not a validated business.

The original specification was read from `main`; its blob is `a0ac1b6c78a0cde8ccd9aca6fda6c5b0880c516d`. The accepted branch boundary was `885b14b5738f39a878a299542fd870186548d8be`, tree `66a938f557e460b5ad1dc86cc91bb53a3301724d`. The remote tree, baseline comparison and completion receipts identify accepted Stages 1–3. No failed-attempt branch or artefact was used.

Inputs read for the current design were the [Stage 1 charter](2026-09-09-stage-01-domain-and-professional-boundary.md), especially ownership, customer/operator distinctions, authority and exclusions; the [Stage 2 capability taxonomy](2026-09-09-stage-02-reconciliation-and-taxonomy.md), especially C01–C06 and C15–C22; relevant source-located rows in the [Stage 2 matrix](2026-09-09-stage-02-source-to-capability-matrix.md); and the [Stage 3 practice map](2026-09-10-stage-03-professional-practice-map.md), [evidence hierarchy](2026-09-10-stage-03-evidence-and-terminology.md), [claims analysis](2026-09-10-stage-03-claims-failures-and-principles.md), conformance and progress records. In particular P01–P07 and U01–U03 constrain customer, alternatives, value, payment and role inference.

These are accepted repository research inputs, not a claim to have re-interviewed customers, reopened all five books or independently replicated the Stage 3 studies. No new external market assertion is needed for this design. Primary-source findings retain their Stage 3 attribution and reading limits. The model below is project synthesis, not terminology attributed verbatim to any author. Synthetic probes in §9 test the design's reasoning and traceability; they do not validate demand, prices or commercial outcomes.

## 2. Representation and limits

Use one business dossier in an ordinary document. It contains a compact business map, customer/role notes, claim/evidence rows, selected value statements and decision/change notes. Small cases can keep all of this inline. Split documents only when their contents need independent ownership or become difficult to review; use ordinary references rather than a new graph service, database, runtime or universal ontology.

The dossier header identifies the business or bounded initiative, accountable owner, objective, decision in scope, version/date, operating context and relevant existing obligations. Record geography, currency, period, unit of analysis and data-use restrictions when they affect the decision. Unknown context is explicit. Do not infer the owner's desired income, growth ambition, jurisdiction or permission to act.

A field can be **known observation**, **hypothesis**, **mixed evidence**, **unknown**, or **not applicable with reason**. This describes its contents, not commercial approval. A proposed value statement may be a hypothesis supported by some observations; do not relabel its entire causal promise an observation. A field can contain several separately labelled claims. No empty cell silently means zero, false or not applicable.

A model is ready for a bounded next decision when that decision's material dependencies have usable evidence or an explicit uncertainty that the proposed test is authorised to investigate. It is not ready for unrestricted scale merely because every row has text. No universal sample size, confidence percentage, startup score or automatic approval threshold is introduced.

### 2.1 Complete business map

All fifteen §11 candidate concerns are retained because each connects customer/value choices to an important downstream dependency. This is an explicit design choice, not a claim that §11 mandates fifteen independent entities. They fit in one table; a simple business may reference the same compact statement from several rows.

| ID | Business concern | Minimum useful content | Trace and review rule |
|---|---|---|---|
| B01 | target customer | Intended segment, inclusion/exclusion criteria, buying/use context and important role differences. | Link customer claims and observations; never substitute everyone who visited or downloaded for the intended paying population. |
| B02 | problem / desired progress | Situation, problem or desired change, importance, frequency and consequences, with unknowns visible. | Link observed behaviour and participant accounts separately; do not turn interview frequency into population prevalence. |
| B03 | alternative / status quo | What people actually do instead, including workarounds, in-house provision, deferral and doing nothing; switching costs and relevant limitations. | Distinguish observed alternatives from researched competitors and untested assumptions; verify material current competitor facts before use. |
| B04 | value proposition | For which role and context, what progress is proposed relative to which alternative, through which plausible mechanism, with what burden and uncertainty. | Every material benefit links to the value and claim records in §§5–6; appealing wording is not delivered value. |
| B05 | offer | Current or proposed outcome, bounded scope and obligations; reference an existing approved offer where one exists. | Record hypothesis or accepted version and its customer/value basis. Detailed component architecture belongs to Stage 5. |
| B06 | acquisition channel | Where suitable people could encounter the proposition, why that is plausible and what actual reach evidence exists. | Reachability is separate from fit, permission to contact and paid demand. Channel architecture belongs to Stage 6. |
| B07 | sales / conversion path | The expected or observed progression to an informed purchase, relevant actors and unresolved buying steps. | Link actual buyer actions rather than seller activity alone; preserve buyer/user distinctions. Stage 6 defines the detailed path. |
| B08 | price / revenue mechanism | Who pays, for what unit, by what mechanism and when; distinguish proposed, quoted, contracted and collected amounts. | Link actual price/context evidence or mark the hypothesis. No invented willingness to pay or hidden renewal terms. Stage 5 owns detailed choices. |
| B09 | delivery mechanism | What must happen to produce the promised progress, who participates and what dependencies constrain delivery. | Link capability and outcome evidence; a demo or promise is not proof of repeatable fulfilment. Stage 7 owns detailed delivery. |
| B10 | cost structure | Relevant direct, acquisition, delivery, support and fixed-cost categories, with period/unit and missing items. | Do not equate revenue with profit or omit human labour because it is unpaid. Stage 7 owns calculation definitions and scenarios. |
| B11 | retention / repeat / expansion | Why continuing or additional value might be wanted; observed repeat/use/renewal behaviour and its period. | Separate voluntary continued value, repeat purchase, expansion and continued billing. Stage 7 supplies detailed measures. |
| B12 | referral / advocacy | Why an eligible customer or partner would recommend the exchange; whether this is observed or only hoped for. | Recommendations, referrals and suitable incremental customers are different events; disclose incentive assumptions. Stages 6–7 own deeper analysis. |
| B13 | operational constraints | Capacity, competence, quality, access, supplier and customer-participation limits material to the promise. | Cite operator facts or explicit assumptions; customer enthusiasm does not authorise commitments beyond capacity. |
| B14 | cash timing | Dates or relative timing of usable collections and obligations, including refunds and delivery commitments. | Separate order, invoice, accounting revenue and available cash; growth cannot erase a timing gap. Stage 7 owns detailed cash modelling. |
| B15 | key assumptions | Decision-critical unresolved links across the map, their consequences and the evidence needed to resolve them. | Reference the relevant claims and decision. Stage 8 owns experiment/learning and constraint-diagnosis architecture. |

The map is a connected view, not a serial process that postpones economics or risk until after selling. Customer evidence may arrive through support, delivery or cancellation as well as discovery. Legal and ethical constraints can restrict any row. Stage 9 develops the specialist handoff; this stage preserves Stage 1's existing boundary without providing legal conclusions.

## 3. Customer and role model

The first two distinctions below describe populations; the remaining four describe roles. They are not six mutually exclusive personas. The same person may occupy several roles, and different people may occupy each role. Avoid a separate actor record unless the distinction changes value, evidence, purchase, use, authority or delivery.

| ID | Required distinction | Representation and evidence discipline |
|---|---|---|
| CR01 | declared target customer | The intended segment is a business hypothesis or bounded accepted choice. State eligibility and exclusion criteria, context and why the segment is being considered. It is not an observed population merely because the owner declared it. |
| CR02 | observed customer | Identify actual purchasing or using customers through a stated event definition, period and provenance. Label interviewed prospects, visitors and non-buyers separately, not as customers. Classify observed fit as fits, does not fit or undetermined; out-of-target customers do not automatically redefine the target. |
| CR03 | buyer | The actor conducting or agreeing the purchase in this context. Record the actual action and process constraints; do not assume a keen user can agree scope or terms. A purchasing agent can be distinct from the budget authority. |
| CR04 | user | The actor receiving or using the product/service and experiencing relevant effort, outcomes and harms. Usage observations support use claims; they do not by themselves establish purchasing authority or willingness to pay. |
| CR05 | economic decision-maker | The actor controlling the relevant budget or economic approval. Capture evidence of that authority or mark it unknown; an influential title is not proof of budget ownership. |
| CR06 | influencer | An actor affecting selection, trust or acceptance without necessarily buying, paying or using. Record the mechanism and evidence of influence, not an invented stakeholder hierarchy. |

Record a **payer** separately when the entity transferring funds differs from the buyer or economic decision-maker. Add a procurement, security or other gatekeeper only when its actual constraints matter. These are conditional annotations, not mandatory extra personas. The skill operator, project owner and specialist reviewer are separate Stage 1 roles, not customer personas.

For each material segment/role claim retain the inclusion rule, relevant evidence, exceptions and uncertainty. Recruitment through a founder's network, a support queue or a free-user community is recorded as a sampling context. Preserve observations from unsuitable prospects and non-adopters when they challenge the proposition; do not discard them merely to improve an apparent fit rate.

For consumer work, buyer, user, economic decision-maker and payer can coincide; state that rather than inventing four people. They can also differ, for example when a parent pays for another person's use. For B2B, record role distinctions that affect adoption and agreement, without assuming every business needs an enterprise sales process. A marketplace represents each materially different side's progress, payer and alternatives; participants on one side are not proof of demand on the other.

## 4. Evidence model

### 4.1 Small evidence record

Use a short evidence ID and a locator to an authorised source, not a copied customer database. A material record contains: evidence type; observation or attributed account; source/locator and collection date; population/role/segment; context and period; method/exposure or sample basis; relevant measure and denominator where applicable; limitations/counter-evidence; permitted use/access restrictions; and the claims it bears on. A linked operational record may supply these fields without duplication.

Keep raw observation, metric, interpretation, confidence and decision separate. Confidence is a reasoned account of relevance, limitations and contrary evidence, not an AI-generated probability. Missing source access is a limitation; missing evidence is not a zero outcome. Duplicate reports of the same event share provenance rather than being counted as independent corroboration.

Evidence can **support**, **challenge**, or **leave unresolved** a claim. That relationship is specific to a claim and context: one payment supports payment at those terms but leaves long-term retention unresolved. Records also identify **synthetic** material explicitly. Synthetic records are useful for design checks and can never be promoted into observed customer evidence.

Do not publish private transcripts, personal identifiers, confidential commercial terms or operational credentials in this open-source repository. Keep only approved, minimal, redacted evidence or controlled locators. Data access is not permission for publication, outreach or a new use. Material legal/data questions are handed off under Stage 1; no jurisdiction is silently assumed.

### 4.2 All nine evidence classes

| ID | Evidence class | What to capture | Appropriate inference and important limit |
|---|---|---|---|
| E01 | interviews | Recruitment context, role, neutral question/topic, concrete account of recent behaviour, relevant counterexamples and consent/access boundary. | Supports reported needs and context; stated intention and sample frequency are not population demand, actual payment or a causal benefit. |
| E02 | sales calls | Prospect fit, roles, actual problem/alternative, objections, quote/terms discussed and documented buyer next action. | Supports buying-process and objection hypotheses; seller activity, politeness and an unsigned proposal are not a paid customer. |
| E03 | support issues | Affected customer/cohort, issue, severity, recurrence, resolution and known coverage bias. | Reveals delivery problems and unmet needs; support users are a selected population, and silence does not prove satisfaction. |
| E04 | search / demand evidence | Query or demand signal, geography/audience, date/window, source definitions and intended commercial relevance. | Supports discoverability or expressed interest at that scope; search volume is not reachable unique buyers, permission to contact or willingness to pay. |
| E05 | usage data | Defined meaningful action, unit, exposed/eligible population, period, instrumentation limits and relation to the desired outcome. | Supports observed use; logins or feature activity are not automatically achieved value, paid demand or voluntary preference. |
| E06 | conversion data | Conversion event, numerator, denominator, cohort/source, offer/price/terms, window and exclusions such as test traffic. | Supports observed progression under those conditions; aggregation, selection and attribution do not establish an intervention's causal lift. |
| E07 | retention data | Starting cohort, eligibility, elapsed time, repeat/use/payment event, cancellations, refunds and known missing outcomes. | Supports the defined observed persistence; continued billing is not necessarily continuing value or an unlimited lifetime forecast. |
| E08 | competitive alternatives | Observed workaround or actual comparison, relevant current competitor facts, date, price/scope and switching burden. | Supports context-specific alternatives; a competitor's advertised claim is attributed marketing, not independently verified performance. Doing nothing remains an alternative. |
| E09 | willingness-to-pay evidence | Payer/authority, actual price, scope, terms, context and event: hypothetical statement, quote acceptance, deposit, completed payment or refund. | State which event occurred. Only actual payment is collected-payment evidence; it does not prove willingness at another price, full-price renewal or satisfaction. |

No business must collect all nine classes before making any decision. Cover the classes relevant to the claim and consequence; state why other classes are not applicable or not yet available. The nine-class table defines capability coverage, not a nine-step mandatory research campaign or a substitute for Stage 8's experiment design.

## 5. Value model

A value statement identifies **role + context + desired progress + alternative + proposed mechanism + benefit + customer burden + evidence/uncertainty**. Distinguish desired, perceived/promised and actually delivered value. An attractive promise without outcome evidence remains a value hypothesis, even when the problem itself is well evidenced.

Select only relevant dimensions below. A statement may involve several dimensions, but do not add them into one value score or double-count the same benefit. For example, less staff time and a claimed salary saving are not two independent cash benefits; saved time may improve capacity without reducing payroll. Price is the cost of the exchange, not a direct measurement of customer value.

| ID | Value dimension | Operational question and possible evidence | Constraint on the claim |
|---|---|---|---|
| V01 | functional value | What task or outcome becomes possible or better relative to the current alternative? Observe task completion, outcome quality or failure reduction under stated conditions. | Feature presence is not task success. State dependencies and whose outcome is measured. |
| V02 | economic value | What relevant cost, revenue, loss or resource consequence changes for the customer? Use the customer's attributable, time-bounded records or a labelled scenario. | Do not promise ROI from invented inputs, treat time saved as realised cash automatically, or present operational modelling as investment advice. |
| V03 | emotional value | Which experienced concern, confidence, frustration or enjoyment changes? Use attributed accounts and suitable experience research. | Do not diagnose mental health, infer inner states from clicks or guarantee an emotional outcome. |
| V04 | social/status value | What relevant identity, belonging, recognition or social consequence does the customer report or demonstrate in context? | Do not impose status motivations, exploit vulnerability or infer protected/personal traits unnecessarily. |
| V05 | risk reduction | Which probability, exposure or consequence is reduced, by which actual mechanism, and what residual risk remains? | A guarantee may transfer a remedy obligation without reducing the underlying failure probability. Do not claim risk elimination. |
| V06 | time reduction | Which elapsed delay or time-to-value changes relative to which baseline? Record start/end definitions and dependencies. | Distinguish calendar delay from active effort; do not extrapolate a single fast demonstration into a universal delivery promise. |
| V07 | effort reduction | Which customer actions, attention, coordination or physical/cognitive workload changes? Observe the burden and costs shifted elsewhere. | Less customer work may require more staff work, integration or setup; preserve the total delivery and economic consequences. |
| V08 | uncertainty reduction | What decision-relevant unknown becomes better understood, using what credible information and stated limits? | More confidence is not necessarily more accuracy. Do not turn research or prediction into a certainty guarantee. |

For each selected dimension record the baseline/alternative, desired change, outcome indicator, evidence IDs, adverse trade-offs and remaining uncertainty. Evidence may support the problem but not the proposed mechanism or achieved benefit; express those as separate claims. If no customer evidence supports a dimension, leave it a hypothesis or omit it rather than inventing a need.

## 6. Decision traceability and bounded approval

Use ordinary IDs and links. A **claim** records a specific assertion, role/segment/context, whether it is an observation, interpretation or hypothesis, supporting/challenging evidence, limitations and decision relevance. A **decision** records the choice and scope, owner, version/date, alternatives considered, claim/evidence basis, unresolved dependencies, approval boundary and review trigger. This is the minimum linking discipline needed for §11's exit, not a general decision-engine schema.

The required trace is:

```text
source observation or attributed account
→ evidence record with context and limitations
→ customer/problem or value claim
→ bounded offer or growth decision
→ downstream dependencies and review trigger
```

Trace back through every material link. A later recommendation must name the particular claim and evidence, not cite an entire book, a generic source list or this model as proof of local demand. External market facts must be current and verified where material; the fact that Stage 3 accessed a page is not an evergreen verification of its current prices or availability.

A useful decision state is draft, approved for a bounded test, accepted within stated scope, superseded, or withdrawn. These states do not upgrade evidence. A human can approve a limited test precisely because a claim is uncertain. An accepted decision has an evidence/context boundary and remains reviewable; it is not a universally validated fact. Tool availability, owner enthusiasm and writing the decision record are not execution authority.

Before releasing a downstream recommendation, check:

1. The intended customer, actual observed population and material roles are explicit.
2. The problem, alternative, proposed mechanism and achieved benefit are not conflated.
3. Supporting and challenging observations resolve to authorised sources; synthetic material remains synthetic.
4. The evidence supports the actual scope, terms and consequence being proposed, or the recommendation is explicitly limited to resolving that uncertainty.
5. Delivery, costs, capacity, cash, truthfulness and professional constraints do not contradict the proposition.
6. Existing approved choices remain intact unless implicated; the named owner and specialist approvals are present before an external action.

A broken evidence link blocks an evidence-backed claim. It does not block honest documentation of an unknown or an appropriately authorised test proposal. Stage 8 will define how such tests are selected and interpreted; Stage 4 does not pre-empt that architecture.

## 7. Changes and downstream review

A new observation does not automatically rewrite the target customer. First record whether it supports, challenges or falls outside the existing claim. A target change means changing segment inclusion, desired progress, buying/use context or a material role assumption, not merely fixing spelling.

When such a change is proposed, record the old and new versions, reason, affected claims and approval owner. Review the downstream rows below. **Review is not automatic replacement:** retain an unaffected accepted choice with an explicit reason, revise only an implicated assumption, or block a commitment until material missing evidence is obtained. Keep old evidence tied to its original population; do not relabel it as proof for the new segment.

| Affected concern | Required review after a material customer/role change |
|---|---|
| B02–B04: problem, alternative, value | Is the same progress important to this population, are alternatives different, and does the proposed mechanism still address it? Reassess selected value dimensions and claim scope. |
| B05: offer | Check outcome, scope, proof, exclusions and obligations against the changed needs and roles. Preserve the accepted offer version until a change is approved. |
| B06–B07: acquisition and sales | Reassess audience access, fit, appropriate channel, buying authority, trust and process. Prior clicks or conversion from another population do not establish current fit. |
| B08: price/revenue | Reassess payer, unit, willingness-to-pay evidence and terms; earlier paid amounts do not establish willingness in a new segment. |
| B09–B10: delivery and costs | Reassess the work, integration, customer participation, service standard and relevant costs needed for the changed promise. |
| B11–B12: continued value and advocacy | Review repeat/use/renewal needs, expansion fit and referral incentives; keep earlier cohorts separate. |
| B13–B14: capacity and cash | Review sales/delivery load, timing of collections, refunds and obligations; attractive demand cannot override a capacity or cash block. |
| B15: assumptions and evidence | Identify which hypotheses and accepted inferences need renewed evidence, which remain supported and what decision is currently blocked. |
| Human/legal boundary | Review relevant data-use, claims, vulnerable-user and specialist constraints without issuing legal conclusions. Obtain the required owner/specialist decisions before execution. |

Changes to observed evidence alone can prompt a bounded review without changing the declared segment. Conversely, a segment change requires review even when the document still uses the same marketing label. This prevents cosmetic naming from hiding a substantive business-model change.

## 8. Use across starting points and business types

**Greenfield:** complete the map with explicit hypotheses and unknowns. Attribute supplied claims to their source; distinguish owner beliefs from customer accounts. Select the next bounded decision based on the unresolved link, not pressure to make every row look validated. No customer evidence is manufactured to populate the dossier.

**Existing business:** start with current obligations, accepted versions and traceable operating evidence. Reconcile periods, cohorts and units before making cross-row inferences. A new support issue may implicate delivery or onboarding without invalidating an accepted segment, offer or acquisition channel. Preserve the old evidence and decision history when revising.

**Simple consumer or professional-service exchange:** role and mechanism rows can be short when actors coincide or there is one transaction. **Subscription or SaaS:** keep user/account/payer distinctions and observed use versus continued collection visible. **Marketplace or partner-mediated exchange:** add only the side/counterparty distinctions that change value, incentives or evidence. These are applications of the same small representation, not business-model packs or separate mandatory ontologies.

Stage 5 receives B04–B05/B08, selected value claims, role evidence, alternative comparisons, proof gaps and delivery/economic constraints. Stage 6 receives the same evidence basis plus B06–B07 and the distinction between audience access, observed fit and buying authority. Neither stage may convert a hypothesis in this dossier into a fact simply to support a more persuasive offer or faster growth.

## 9. Executed synthetic design probes

All people, businesses, events, amounts and outcomes in this section are **synthetic**. They are original reasoning probes, not collected customer evidence, primary progressive examples, agent benchmarks or proof that the proposed business works. The assistant manually traced each case against §§2–7; the conformance checker verifies their required trace/disposition fields separately.

### Probe A: service user is not the economic buyer

**Synthetic setup:** A fictional reporting service is considering small agencies. Two staff members describe manual report preparation. One operations director signs a limited pilot approval; no budget authority or payment is recorded. Staff report a four-hour task; no delivered time saving has been measured.

| Map | Synthetic dossier entry |
|---|---|
| B01 | Declared segment: small agencies with recurring client reports; the two staff are interviewed users/prospects, not observed paying customers. |
| B02 | Report preparation is described as burdensome; its frequency outside these accounts and economic importance to the budget owner are unknown. |
| B03 | Current alternative: manual preparation; in-house automation and doing nothing are untested alternatives. |
| B04 | Hypothesis: reduce preparation effort while maintaining report quality; economic savings are not established. |
| B05 | Proposed bounded reporting pilot; no production service or performance guarantee is approved. |
| B06 | Existing business contacts are a possible channel; reachability and contact permission require separate evidence/authority. |
| B07 | Staff discovery followed by budget/process clarification; signed pilot interest is not a completed paid sale. |
| B08 | Payer, price and collection terms unknown; no price is inferred from the staff's enthusiasm. |
| B09 | Manual preparation/review by a service operator; repeatable delivery and client participation still require evidence. |
| B10 | Relevant labour, tooling, acquisition and support categories identified; amounts and contribution unknown. |
| B11 | Repeat need is hypothesised from recurring reports; no renewal, repeat payment or retained cohort exists. |
| B12 | Referral is untested, not assumed because contacts were friendly. |
| B13 | Operator capacity, data access and quality approval need confirmation before promises. |
| B14 | Pilot approval is not cash; collection and delivery dates remain unknown. |
| B15 | Material unknowns: budget authority, paid demand, achievable effort reduction, delivery quality and cost. |

**Trace:** synthetic interview records A-E1/A-E2 → claim A-C1, staff report preparation effort → value hypothesis A-V1, reduce active effort relative to manual preparation → decision A-D1, seek the missing authority and outcome evidence before proposing a paid commercial commitment. A-E3 is the signed pilot approval and supports only that stated approval event.

**Disposition:** Proceed only with an appropriately authorised evidence-gathering step; block claims of a paid customer, proved economic value or a guaranteed time saving. Preserve the segment hypothesis rather than pivoting solely because staff cannot approve a budget.

**Observed design-check result:** The model distinguishes CR03/CR04/CR05, interview versus commitment versus payment, V06 versus V07 and B14 cash. Every business-map field can be populated honestly without invented values. PASS.

### Probe B: continued billing is not established customer value

**Synthetic setup:** A fictional consumer subscription shows 12 eligible subscriptions at the start of a month, nine successful renewals and meaningful-use events for four accounts in the same starting cohort during that month. One payer reports forgetting the subscription; user/payer identity is not confirmed for every account. No comparison group exists.

**Trace:** synthetic billing record B-E1 → B-C1, nine successful renewal events in that defined cohort; synthetic usage record B-E2 → B-C2, four accounts show the defined use event; interview B-E3 → B-C3, one payer reports forgetting → decision B-D1, inspect the value/use and role gap before describing billed retention as evidence of satisfaction or scaling acquisition.

**Disposition:** Preserve the observed billing and usage facts within the fixture; reject the inference that nine renewals establish nine satisfied users. Do not declare the four active accounts representative of all users or infer why other accounts did not use the service. No new legal conclusion or unauthorised cancellation action is taken.

**Observed design-check result:** E05/E07/E09 retain different meanings; B11 links to value, capacity and cash rather than a single retention score. The data does not justify a causal claim or a segment rewrite. PASS.

### Probe C: a material target change triggers review, not a total rewrite

**Synthetic setup:** A fictional service has an accepted small-agency offer and proposes serving large regulated enterprises after one inbound enquiry. Prior evidence covers small agencies only. The enquiry indicates interest but supplies no budget, procurement, security or deployment evidence.

**Trace:** synthetic enquiry C-E1 → C-C1, one out-of-target prospect asked about the service → proposed customer change C-D1 → review B02–B15 and the human/legal boundary. Record the old target and offer as accepted within their original scope; mark enterprise needs, budget, sales path, delivery dependencies, costs and cash timing unresolved.

**Disposition:** Block an enterprise-ready or validated-enterprise-demand claim. Preserve existing small-agency work and its evidence. Any enterprise discovery is a separate authorised test of the new hypothesis, not retroactive validation from existing customers.

| Impact review | Recorded synthetic disposition |
|---|---|
| B02–B04 | Enterprise problem importance, alternatives and benefits remain unproved; the small-agency claims retain their original scope. |
| B05 | Preserve the accepted small-agency offer; do not add enterprise obligations or claim that it meets procurement requirements. |
| B06–B07 | Record one inbound enquiry, not a validated enterprise channel or complete sales path; buying roles and process remain unknown. |
| B08 | Enterprise payer, budget, price acceptance and payment terms need new evidence; do not transfer small-agency payment evidence. |
| B09–B10 | Enterprise deployment, access, support and service-standard requirements could change work and cost; obtain relevant facts before quoting. |
| B11–B12 | Enterprise renewal, expansion and referral hypotheses require their own context; existing small-agency cohorts remain separate. |
| B13–B14 | Capacity, longer approval/collection possibilities and obligations must be assessed rather than assumed; no cash forecast is asserted. |
| B15 and human/legal boundary | Record the new evidence gaps and responsible approver; route material security/data/regulated-claim questions, without deciding legality or changing the existing service. |

**Observed design-check result:** Every downstream group in §7 is reviewed above; no automatic replacement or silent evidence transfer occurs. One enquiry neither requires nor justifies a pivot. PASS.

### Probe D: evidence on one marketplace side does not validate the other

**Synthetic setup:** A fictional service marketplace interviews three providers willing to list spare capacity. No buyer interviews, purchases, completed matches or payments exist. Providers are potential suppliers, not evidence of consumer demand.

**Trace:** synthetic provider interviews D-E1 → D-C1, those providers stated listing interest under the discussed conditions → value hypothesis D-V1, useful matching could reduce providers' idle capacity → decision D-D1, keep buyer progress, willingness to pay, matching and platform economics unresolved.

**Disposition:** Reject claims of marketplace liquidity, paying demand or platform revenue. Represent buyer and provider roles separately without requiring a universal platform ontology. Do not count a provider's hypothetical full sale value as platform revenue or collected cash.

**Observed design-check result:** The small dossier accommodates two-sided dependencies while keeping scope bounded. Interview interest does not become transactional evidence. PASS.

## 10. Decisions, alternatives and boundaries

Retain a single compact dossier instead of a universal business ontology, graph service or CRM. Retain all fifteen candidate concerns as fields, not fifteen software entities. Preserve six customer distinctions without forcing six people. Use claim-specific evidence relationships, not a global validation badge. Select relevant value dimensions, not a mandatory eight-part sales formula or a numerical Value Equation. Require change impact review, not automatic regeneration of every business choice.

Rejected alternatives include: a one-page canvas with no provenance (cannot meet the traceability exit); a large mandatory entity schema (unnecessary for bounded decisions); segment identity derived automatically from all traffic (confuses observation and intent); enthusiasm as payment proof (exceeds evidence); complete billing as satisfaction (ignores value and roles); approval as truth (confuses authority with evidence); and a new customer label that silently carries old-segment proof forward (breaks scope).

No current-stage user decision is unresolved. Customer-specific prices, data, authority and jurisdictions in future tasks are explicitly required inputs, not missing bootstrap evidence that this stage pretends to possess. The design does not authorise outreach, experiments, spending, publication of customer claims or changes to any live business.

Detailed offer/pricing architecture remains Stage 5; acquisition/sales Stage 6; delivery/economics/cash Stage 7; experiments/learning/diagnosis Stage 8; legal handoffs Stage 9; tools, execution and command/pack design Stages 10–14; primary examples, stress tests and benchmarks Stages 15–17; six canonical specifications Stage 18; and production scaffolding/implementation/installation their later stages. No such stage is marked complete by this model. This is a completed Stage 4 design, not a partially implemented production system.

**Exit assessment:** A downstream decision can trace from an identified customer/role and value claim to a source-located observation, retain the alternative and uncertainty, distinguish authorised testing from substantiated commitment, and review affected decisions after a customer change. All four synthetic probes exercised these distinctions without claiming customer validation. See conformance for the original-specification review, executed checks and publication boundary.
