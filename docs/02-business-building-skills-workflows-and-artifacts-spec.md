# Business Building Skills — Workflows and Artifacts Specification

**Contract version:** 1.0 · 12 September 2026  
**State:** Complete canonical specification; implementation and installed validation are separate gates.  
**Authority:** [Bootstrap §25](research-logs/2026-09-08-business-building-skills-new-project-bootstrap-process.md#25-stage-18--generate-six-canonical-specifications), accepted research through Stage 17 at `ff97f73866012b296bc4a142e0de6258a7906c94`.  
**Specification set:** [01](01-business-building-skills-system-spec.md) · [02](02-business-building-skills-workflows-and-artifacts-spec.md) · [03](03-business-building-skills-repository-and-contracts-spec.md) · [04](04-testing-and-benchmark-spec.md) · [05](05-business-building-customisation-packs-spec.md) · [06](06-business-building-extension-pack-catalogue.md)

Owns the business dossier and all customer/value, offer/pricing, money, acquisition/sales, delivery/retention, economics/cash, assumption/experiment/learning, diagnosis/repair and semantic handoff contracts. A field or source-system label never silently changes meaning when passed to another command.

“Must” states a requirement; “may” permits a bounded option. Examples and authored controls remain synthetic. A specification, complete record or passing calculation does not establish customer validation, installed behaviour, professional clearance or permission for an external action. Earlier research dates, source IDs and stage references record provenance; the ownership table in specification 01 identifies the current normative document. Where an incorporated record names an earlier stage, implement its completed contract in this specification set, not a missing future design.

## 1. Operating procedure and minimal records

Start with the bounded decision, accountable objective, existing obligations, accepted versions and actual evidence. Select only the necessary command in specification 03. Build or review the relevant connected records below, then return evidence limits, separate quality/growth findings, preserved decisions and the smallest justified next step. Never require a new business to generate favourable observations for empty cells, or an existing business to repeat every discovery activity before a local repair.

The ordinary loop is: frame the decision; distinguish observations and claims; identify material dependencies; construct the necessary commercial component; calculate economics, capacity and dated cash; choose the riskiest relevant assumption; compare adequate tests; freeze the selected plan; obtain required execution authority; inspect actual returned evidence; record learning; assess and propose a bounded correction. Existing evidence or a hard constraint can resolve a question without a new experiment. An inconclusive result may justify no further spending while remaining inconclusive.

| Record | Identity and minimum envelope | Change rule |
|---|---|---|
| Dossier | Initiative, owner/objective, bounded decision, version/date, context, unit/period/currency where relevant, obligations and fifteen-concern business map | Organise supplied evidence; revise accepted scope only with the relevant authority |
| Evidence | ID, actual observation/account, locator/date, population/role, method/window, denominator, limitations/counter-evidence and permitted use | Preserve source and corrections; synthetic remains synthetic |
| Claim | ID/version, precise assertion, context, observation/interpretation/hypothesis classification, evidence relationship and uncertainty | New scope is a new version; do not relabel old observations |
| Decision | ID/version, choice, alternatives, owner, evidence, unresolved dependencies, authority and review trigger | Draft, approved for bounded test, accepted within scope, superseded or withdrawn; status never upgrades evidence |
| Calculation | HC01–HC08 below, immutable input/output identities and actual execution | Recalculate changed inputs; a formula or stale cache is not a run |
| Experiment / learning / repair | EX01–EX09 / LR01–LR08 / RR01–RR08 with linked source and accepted versions | Freeze before observations; retain failed, stopped, corrected and superseded entries |

Field content can be known observation, hypothesis, mixed evidence, unknown or not applicable with reason. Empty is never zero. Assessment uses PASS/FAIL/BLOCKED/justified NOT APPLICABLE; it is separate from evidence state, interpretation and authority. Scoped local IDs are namespaced by record family: business-map B01 is not build-command B01; evidence E01 is not example E01 or evaluation-command E01; pricing P01 is not pack-author command P01. Include the family when the context is ambiguous.

The following modules adopt the accepted record content. Their local subsection numbers and source IDs are retained for traceability. Cross-stage references map to these completed modules: Stage 4 → module 2; Stage 5 → modules 3–4; Stage 6 → module 5; Stage 7 → modules 6–7; Stage 8 → modules 8–9; Stage 9 → module 10; execution Stage 11 → specification 03. Their complete normative content is present here. Original synthetic research probes and old completion claims are not implementation requirements.

## 2. Customer, problem, alternatives and value

Adopted contract and source-ID context: [2026-09-10-stage-04-business-customer-and-value-model.md](research-logs/2026-09-10-stage-04-business-customer-and-value-model.md).

### 2. Representation and limits

Use one business dossier in an ordinary document. It contains a compact business map, customer/role notes, claim/evidence rows, selected value statements and decision/change notes. Small cases can keep all of this inline. Split documents only when their contents need independent ownership or become difficult to review; use ordinary references rather than a new graph service, database, runtime or universal ontology.

The dossier header identifies the business or bounded initiative, accountable owner, objective, decision in scope, version/date, operating context and relevant existing obligations. Record geography, currency, period, unit of analysis and data-use restrictions when they affect the decision. Unknown context is explicit. Do not infer the owner's desired income, growth ambition, jurisdiction or permission to act.

A field can be **known observation**, **hypothesis**, **mixed evidence**, **unknown**, or **not applicable with reason**. This describes its contents, not commercial approval. A proposed value statement may be a hypothesis supported by some observations; do not relabel its entire causal promise an observation. A field can contain several separately labelled claims. No empty cell silently means zero, false or not applicable.

A model is ready for a bounded next decision when that decision's material dependencies have usable evidence or an explicit uncertainty that the proposed test is authorised to investigate. It is not ready for unrestricted scale merely because every row has text. No universal sample size, confidence percentage, startup score or automatic approval threshold is introduced.

#### 2.1 Complete business map

All fifteen §11 candidate concerns are retained because each connects customer/value choices to an important downstream dependency. This is an explicit design choice, not a claim that §11 mandates fifteen independent entities. They fit in one table; a simple business may reference the same compact statement from several rows.

| ID | Business concern | Minimum useful content | Trace and review rule |
|---|---|---|---|
| B01 | target customer | Intended segment, inclusion/exclusion criteria, buying/use context and important role differences. | Link customer claims and observations; never substitute everyone who visited or downloaded for the intended paying population. |
| B02 | problem / desired progress | Situation, problem or desired change, importance, frequency and consequences, with unknowns visible. | Link observed behaviour and participant accounts separately; do not turn interview frequency into population prevalence. |
| B03 | alternative / status quo | What people actually do instead, including workarounds, in-house provision, deferral and doing nothing; switching costs and relevant limitations. | Distinguish observed alternatives from researched competitors and untested assumptions; verify material current competitor facts before use. |
| B04 | value proposition | For which role and context, what progress is proposed relative to which alternative, through which plausible mechanism, with what burden and uncertainty. | Every material benefit links to the value and claim records in §§5–6; appealing wording is not delivered value. |
| B05 | offer | Current or proposed outcome, bounded scope and obligations; reference an existing approved offer where one exists. | Record hypothesis or accepted version and its customer/value basis. Module 3 defines the complete offer components. |
| B06 | acquisition channel | Where suitable people could encounter the proposition, why that is plausible and what actual reach evidence exists. | Reachability is separate from fit, permission to contact and paid demand. Module 5 defines the complete channel architecture. |
| B07 | sales / conversion path | The expected or observed progression to an informed purchase, relevant actors and unresolved buying steps. | Link actual buyer actions rather than seller activity alone; preserve buyer/user distinctions. the acquisition/sales module (5) defines the detailed path. |
| B08 | price / revenue mechanism | Who pays, for what unit, by what mechanism and when; distinguish proposed, quoted, contracted and collected amounts. | Link actual price/context evidence or mark the hypothesis. No invented willingness to pay or hidden renewal terms. the offer/pricing and money modules (3–4) owns detailed choices. |
| B09 | delivery mechanism | What must happen to produce the promised progress, who participates and what dependencies constrain delivery. | Link capability and outcome evidence; a demo or promise is not proof of repeatable fulfilment. the delivery/economics modules (6–7) owns detailed delivery. |
| B10 | cost structure | Relevant direct, acquisition, delivery, support and fixed-cost categories, with period/unit and missing items. | Do not equate revenue with profit or omit human labour because it is unpaid. the delivery/economics modules (6–7) owns calculation definitions and scenarios. |
| B11 | retention / repeat / expansion | Why continuing or additional value might be wanted; observed repeat/use/renewal behaviour and its period. | Separate voluntary continued value, repeat purchase, expansion and continued billing. the delivery/economics modules (6–7) supplies detailed measures. |
| B12 | referral / advocacy | Why an eligible customer or partner would recommend the exchange; whether this is observed or only hoped for. | Recommendations, referrals and suitable incremental customers are different events; disclose incentive assumptions. Stages 6–7 own deeper analysis. |
| B13 | operational constraints | Capacity, competence, quality, access, supplier and customer-participation limits material to the promise. | Cite operator facts or explicit assumptions; customer enthusiasm does not authorise commitments beyond capacity. |
| B14 | cash timing | Dates or relative timing of usable collections and obligations, including refunds and delivery commitments. | Separate order, invoice, accounting revenue and available cash; growth cannot erase a timing gap. the delivery/economics modules (6–7) owns detailed cash modelling. |
| B15 | key assumptions | Decision-critical unresolved links across the map, their consequences and the evidence needed to resolve them. | Reference the relevant claims and decision. the experiment/repair modules (8–9) owns experiment/learning and constraint-diagnosis architecture. |

The map is a connected view, not a serial process that postpones economics or risk until after selling. Customer evidence may arrive through support, delivery or cancellation as well as discovery. Legal and ethical constraints can restrict any row. Module 10 defines the specialist handoff; the professional boundary in specification 01 applies throughout.

### 3. Customer and role model

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

### 4. Evidence model

#### 4.1 Small evidence record

Use a short evidence ID and a locator to an authorised source, not a copied customer database. A material record contains: evidence type; observation or attributed account; source/locator and collection date; population/role/segment; context and period; method/exposure or sample basis; relevant measure and denominator where applicable; limitations/counter-evidence; permitted use/access restrictions; and the claims it bears on. A linked operational record may supply these fields without duplication.

Keep raw observation, metric, interpretation, confidence and decision separate. Confidence is a reasoned account of relevance, limitations and contrary evidence, not an AI-generated probability. Missing source access is a limitation; missing evidence is not a zero outcome. Duplicate reports of the same event share provenance rather than being counted as independent corroboration.

Evidence can **support**, **challenge**, or **leave unresolved** a claim. That relationship is specific to a claim and context: one payment supports payment at those terms but leaves long-term retention unresolved. Records also identify **synthetic** material explicitly. Synthetic records are useful for design checks and can never be promoted into observed customer evidence.

Do not publish private transcripts, personal identifiers, confidential commercial terms or operational credentials in this open-source repository. Keep only approved, minimal, redacted evidence or controlled locators. Data access is not permission for publication, outreach or a new use. Material legal/data questions are handed off under Stage 1; no jurisdiction is silently assumed.

#### 4.2 All nine evidence classes

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

No business must collect all nine classes before making any decision. Cover the classes relevant to the claim and consequence; state why other classes are not applicable or not yet available. The nine-class table defines capability coverage, not a nine-step mandatory research campaign or a substitute for the experiment/repair modules (8–9)'s experiment design.

### 5. Value model

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

### 6. Decision traceability and bounded approval

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

A broken evidence link blocks an evidence-backed claim. It does not block honest documentation of an unknown or an appropriately authorised test proposal. Module 8 defines how such tests are selected and interpreted.

### 7. Changes and downstream review

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

### 8. Use across starting points and business types

**Greenfield:** complete the map with explicit hypotheses and unknowns. Attribute supplied claims to their source; distinguish owner beliefs from customer accounts. Select the next bounded decision based on the unresolved link, not pressure to make every row look validated. No customer evidence is manufactured to populate the dossier.

**Existing business:** start with current obligations, accepted versions and traceable operating evidence. Reconcile periods, cohorts and units before making cross-row inferences. A new support issue may implicate delivery or onboarding without invalidating an accepted segment, offer or acquisition channel. Preserve the old evidence and decision history when revising.

**Simple consumer or professional-service exchange:** role and mechanism rows can be short when actors coincide or there is one transaction. **Subscription or SaaS:** keep user/account/payer distinctions and observed use versus continued collection visible. **Marketplace or partner-mediated exchange:** add only the side/counterparty distinctions that change value, incentives or evidence. These are applications of the same small representation, not business-model packs or separate mandatory ontologies.

the offer/pricing and money modules (3–4) receives B04–B05/B08, selected value claims, role evidence, alternative comparisons, proof gaps and delivery/economic constraints. the acquisition/sales module (5) receives the same evidence basis plus B06–B07 and the distinction between audience access, observed fit and buying authority. Neither stage may convert a hypothesis in this dossier into a fact simply to support a more persuasive offer or faster growth.

## 3. Offer and pricing

Adopted contract and source-ID context: [2026-09-10-stage-05-offer-and-pricing-architecture.md](research-logs/2026-09-10-stage-05-offer-and-pricing-architecture.md).

### 2. Offer model: fourteen components

Each row is a reviewable concern, not a mandatory sales device. Optional bonuses, guarantees and urgency can be absent with a reason. Retain the offer version, linked customer/value claims, supporting/challenging evidence, dependencies, owner and review trigger. A short dossier can hold the entire offer inline.

| ID | Component | Minimum useful definition | Evidence and acceptance rule |
|---|---|---|---|
| O01 | customer | Intended segment, eligibility/exclusions, relevant buyer/user/payer roles and context. | Link the customer/value module (2) claims. A friendly prospect, user or audience member is not automatically an authorised buyer or paying customer. |
| O02 | outcome | Desired progress relative to the current alternative, with observable success and meaningful limits. | Separate intended, promised and demonstrated outcomes. State dependencies outside the provider's control; never invent earnings or customer results. |
| O03 | scope | Included work, quantities, service boundaries, customer responsibilities and change procedure. | The smallest scope must still deliver the stated value. Do not remove an essential component then sell it as an undisclosed mandatory add-on. |
| O04 | mechanism | How the proposed work produces progress, who participates and what assumptions connect actions to outcomes. | A plausible explanation is not causal proof. Identify the weakest link and delivery evidence rather than presenting proprietary-sounding language as validation. |
| O05 | deliverables | Concrete outputs/access/services, acceptance criteria, quality standard and responsible operator. | Confirm capability and capacity for the sold volume. Specify support and handover obligations; an unbuilt feature or template is not a delivered result. |
| O06 | time-to-value | Start event, expected first useful outcome, completion window and customer/supplier dependencies. | Distinguish elapsed time from active effort. Quote supported ranges or a labelled hypothesis, not an exceptional best-case demonstration as a guarantee. |
| O07 | price | Currency, unit, actual payable amount or transparent calculation, applicable mandatory charges and material conditions. | Preserve complete price information alongside any per-unit illustration. Reference-price, tax and presentation questions retain their jurisdiction and review boundary. |
| O08 | payment structure | Deposit, milestones, instalments, billing cadence, due dates, renewal amount/basis and collection conditions. | Separate amount owed, invoiced and collected. Show total obligation, termination/renewal implications and dated cash exposure; a monthly instalment is not necessarily a cancellable monthly contract. |
| O09 | risk reversal | Which customer uncertainty or exposure is reduced, by what mechanism and which residual risk remains. | A demonstration, staged commitment, trial or remedy can address different risks. Do not call transferred or conditional risk eliminated. Model resulting provider exposure. |
| O10 | guarantee / refund terms | Eligibility, promised remedy, conditions, time window, evidence needed, request route and fulfilment responsibility. | Test ability to honour the promise and present material limits before commitment. Refund, repair, replacement and credit differ. Existing rights and any required specialist review remain constraints. |
| O11 | bonuses / added components | Optional component's actual use, incremental burden, availability and relationship to the core outcome. | Retain only useful components with deliverable capacity and cost. Do not invent standalone prices or imply a necessary part of the paid package is an unconditional free gift. |
| O12 | proof / credibility | Relevant demonstrations, measured outcomes, authorised testimonials or attributed qualifications with scope and date. | Evidence must support the exact claim and population. Synthetic examples are labelled; permission and claim review apply. A refund promise is not proof that an outcome occurs. |
| O13 | constraints / exclusions | Capacity, suitability, prerequisites, access, geography, service limits and material restrictions. | Limits must not contradict the headline outcome or be concealed. Out-of-scope demand needs a separately approved option, not an improvised sales promise. |
| O14 | urgency / scarcity only where truthful | Actual capacity limit, stock, cohort/date or other verifiable reason that availability changes. | Record the source, expiry and what actually happens afterwards. If no genuine limit exists, omit urgency. Reset timers and fabricated shortages fail even when conversion improves. |

R04–R05 support caution about bundles and remedies; R09 concerns payment/risk alignment; R10–R11 identify price, substantiation and guarantee review surfaces. These are constraints on the project synthesis, not a claim that these sources define the fourteen-row model.

#### Offer review result

Record separate findings for customer relevance, proof, clarity, deliverability, direct economics, cash/capacity and rights/ethical/legal questions. Use **supported within scope**, **hypothesis requiring a bounded test**, **inadequate evidence**, or **contradicted/blocked**, with reasons. Do not average these into an offer score. An economically sound but unsupported promise remains blocked; an honestly described hypothesis can support an authorised small test without becoming a proven offer.

### 3. Economic definitions used in this stage

Every comparison states period, currency, population/unit, price version and cost scope. The following are operational decision definitions, not a replacement for accounting treatment or the full the delivery/economics modules (6–7) model.

- **Gross commercial consideration G:** the declared pre-adjustment amount for the business's own exchange in the period. Show discounts separately. Exclude pass-through amounts from an intermediary's own fee comparison; keep taxes and total customer payment reconciled separately. A notional list price is not evidence that customers paid it.
- **Adjustments D and F:** D is the explicit discount from that declared basis; F is refunds or other credits reducing this consideration. Record cash refunds and non-cash credits separately and do not subtract one adjustment twice. **N = G − D − F** is net commercial consideration for the stated comparison.
- **Direct cost K:** named delivery, labour, fulfilment, usage, support, payment, loss or other directly attributable costs included in this comparison. Identify timing and variability; do not omit founder effort because no salary is currently drawn. Show opportunity cost or committed labour separately where an incremental-cash view differs.
- **Direct contribution C = N − K.** **Contribution margin = C / N** when N is positive; otherwise the percentage is not meaningful. This label is not certified accounting gross margin. Acquisition cost A and separately declared shared/incremental cost H may be shown as **C − A − H**, without calling that residual net profit when costs remain excluded.
- **Cash:** dated usable receipts minus dated obligations, refunds and permitted transfers, plus opening usable cash. Contract value, invoice value, accounting revenue, conditional commission and collected cash are different states. A positive C does not guarantee positive cash at every date.

A price markup uses a cost denominator; margin uses the corresponding revenue denominator. Specify which is intended. No universal target margin, cost allocation, return rate, payback period or LTV multiplier is introduced. Relevant incremental cost may differ from fully allocated cost; long-run viability still requires funding the wider system. An explicitly funded loss-making test is not a profitable scale recommendation. Actual recognition, tax, principal/agent classification and contractual entitlements are supplied or professionally reviewed, not guessed.

### 4. Pricing decision framework: fourteen approaches

The first rows concern evidence and pricing bases; others concern package, unit, cadence or terms. They can be combined, but each additional choice must have a reason. Product tiers and quantity bands are not interchangeable.

| ID | Pricing approach | Decision, inputs and comparison | Failure / boundary |
|---|---|---|---|
| P01 | cost-informed boundaries | Compare relevant incremental, capacity/opportunity and sustainable full-cost views against price and owner objective. State cost coverage and sensitivity. Basis: R01. | A cost-plus result neither proves demand nor automatically sets the best price. Bound and fund any deliberate negative contribution; do not conceal unpaid delivery work. |
| P02 | value-based pricing | Use evidenced customer progress, alternatives, payer context and value distribution to propose a price or unit. Basis: the customer/value module (2), R02–R03. | Customer value is not the seller's cost or a fabricated ROI number. No automatic right to capture all theoretical value; test actual acceptance and outcomes. |
| P03 | competitor/reference pricing | Compare dated, like-for-like alternatives with scope, unit, terms, quality and switching burden visible. Basis: R01–R02. | A competitor's headline price is not equivalent total cost, local willingness to pay or proof of superiority. Reverify material current facts and truthful anchors. |
| P04 | willingness-to-pay | Separate stated research, quotes, deposits, payments and refunds at actual scope/terms; use evidence appropriate to the decision. Basis: R03 and the customer/value module (2) E09. | Do not turn survey intention, discounted sales or one segment's purchase into full-price demand elsewhere. No universal hypothetical-bias correction. |
| P05 | tiering | Compare genuinely useful packages for different needs and the marginal scope/price between them; include no purchase or the current offer. Basis: R01, Stage 2 packaging research. | Avoid fake premium decoys, hidden essentials and automatic tier proliferation. Quantity-tier maths is a separate choice requiring boundary tests under R08. |
| P06 | packaging | Combine or separate components according to progress, comprehension, fulfilment cost and joint use. Compare an adequate simpler option. Basis: R04. | More components need not create more delivered value. Low-marginal-cost information bundling cannot justify uncosted human service bundles. |
| P07 | usage pricing | Define billable event/unit, measurement source, corrections, bands, caps/overages and customer cost visibility. Compare demand variation with marginal cost. Basis: R07–R08. | A technically measurable event may not track value; usage bills and provider costs can diverge. Test zero, threshold and high-use cases and dispute handling. |
| P08 | subscription | Define continuing entitlement, period, renewal amount/basis, cancellation/expiry and separate billing cadence. Use cohort value and obligations. Basis: R07, the customer/value module (2) E07. | An annual commitment billed monthly is not necessarily monthly cancellation. Continued collection is not proof of continuing value; no invented lifetime revenue. |
| P09 | one-time purchase | State the purchased output/right, included support/updates and their end conditions; compare lifetime obligations with one receipt. Basis: R01, Stage 2–3 delivery research. | One payment does not imply zero future cost or perpetual updates. Avoid selling unlimited continuing service for an unexamined fixed receipt. |
| P10 | service retainers | Define reserved capacity, response standard, included work, unused allocation, additional work and review period. Basis: R09. | Availability itself may have value but must be explicit. Do not promise unlimited throughput, count every reserved hour as incremental cash cost, or ignore opportunity cost. |
| P11 | performance-linked structures where lawful/appropriate | Specify measurable outcome, baseline, attribution, control, verification, fee cap/floor, collection and dispute conditions. Compare fixed, variable or mixed structures. Basis: R09. | No fee guarantee based on an outcome outside control; investigate metric gaming, customer harm, delayed payment and sector-specific restrictions before commitment. |
| P12 | freemium / free-to-paid | Define free value/limits, paid incremental value, eligibility, conversion path and cost of both populations. Compare a direct paid option and bounded trial where relevant. Basis: R06–R07. | Free adoption is not paid demand; no hidden conversion or unsupported future cross-subsidy. Preserve accepted entitlements when reviewing changes. |
| P13 | discounting | Specify genuine reference, actual total reduction, duration/eligibility and expected incremental demand. Compare contribution after cannibalisation, refunds and workload. Basis: R01–R02, R10–R11. | Higher conversion may reduce contribution or exceed capacity. No fabricated original price, perpetual false deadline or extrapolation to undiscounted willingness to pay. |
| P14 | payment timing | Compare deposits, milestones, instalments and renewal collections with obligations, default, fees and customer acceptance. Basis: R09–R10. | Earlier cash does not necessarily improve margin; later instalments are not cash received. A feasible schedule still needs contractual and customer approval. |

#### Decision procedure

1. **Fix the decision boundary.** State the objective, accepted version and exact issue. Review existing obligations; do not rewrite the customer or product because a payment schedule is failing.
2. **Establish the exchange.** Link O01–O06 to the customer/value module (2) evidence and alternatives. Identify the actual payer and authority. Distinguish evidence for the problem from evidence for the mechanism or result.
3. **Expose constraints.** State costs, capacity, cash dates, rights and truthfulness issues before optimising price. Unknown critical inputs block commitment or become the purpose of an authorised test.
4. **Compare a small adequate option set.** Include the unchanged offer where viable. Vary scope, price, unit, cadence or payment terms deliberately, showing which changed. Do not force all fourteen approaches or all thirteen money models.
5. **Evaluate coherent scenarios.** Recompute N, K, C and dated cash; expose customer mix, usage, refunds, collections, labour and retention assumptions. Compare contribution per eligible opportunity and capacity as well as per sale. Use actual source definitions; hypothetical scenarios remain hypothetical.
6. **Check the complete promise.** Proof, price/renewal terms, remedies, constraints and truthful availability must agree across proposal, marketing brief and fulfilment brief. Capture professional questions without certifying legality.
7. **Choose retain, revise, test, reject or block.** Name the owner, evidence, uncertainty and smallest responsible change. Where a test is needed, state the unresolved claim and required evidence; the experiment/repair modules (8–9) defines the full experiment architecture. Approval is limited to its stated action, budget and context.
8. **Preserve and review.** Version accepted terms. Name triggers such as changed customer, supplier cost, billable unit, utilisation, refund exposure or renewal behaviour. Review implicated dependencies and retain unaffected accepted choices with reasons.

No live prices, subscriptions, contracts, payments, audiences or customer records may be changed merely because this procedure produces a recommendation. The Stage 1 human/professional boundary remains in force.

### 5. Failure modes and smallest sufficient repair

| ID | Failure signal / invalid inference | Evidence to inspect | Smallest responsible response |
|---|---|---|---|
| F01 | Conversion improves while contribution deteriorates. | Price/discount, eligible population, mix, refunds, direct and acquisition costs. | Correct the affected price/package/channel assumption; retain customer/value choices unless implicated. Synthetic S01 exercises this. |
| F02 | Attractive package exceeds delivery capacity or quality. | Included work, use distribution, labour, support burden and available slots. | Bound scope/volume or delivery mechanism; do not add unsupported scarcity language to disguise the problem. |
| F03 | Profitable contract creates a cash shortfall. | Dated collections, deposits, obligations, usable opening cash and refund exposure. | Review payment timing or growth pace before changing the whole offer. S02. |
| F04 | Guarantee increases appeal but cannot be substantiated or honoured. | Promised result, control, conditions, eligible claims, remedy cost and funds. | Withdraw/revise unsupported future promise through approval; preserve existing rights and obtain specialist review. S03/S08. |
| F05 | Bonus or reference value is invented. | Actual standalone sale/availability, customer usefulness and incremental cost. | Remove unsupported comparison; retain useful components on honest terms. |
| F06 | Survey willingness to pay is treated as sales. | E09 event, price, scope, sample and payer authority. | Relabel evidence and propose the missing bounded validation; do not apply a universal correction factor. |
| F07 | Headline price conceals renewal, mandatory fee or commitment. | Full customer obligation and disclosure sequence. | Block publication until terms and presentation agree and required review is complete. S08. |
| F08 | Quantity boundary unexpectedly lowers revenue or margin. | Exact billing formula, quantity range and per-unit cost. | Correct/test the implicated pricing formula, with approval before changing existing terms. S04. |
| F09 | Free growth is counted as funded growth. | Free/paid populations, delivery cost, conversion and cohort value. | Review free-to-paid hypothesis, budget or package boundaries, not assumed future scale. S05. |
| F10 | Renewal or expansion is counted twice. | Canonical transaction, invoice lines, adjustment IDs and analytical tags. | Repair aggregation and reissue affected conclusions; no needless offer redesign. S06. |
| F11 | Marketplace volume or seller balances are treated as own revenue/cash. | Roles, contractual allocation, fee basis, transfers and settlement obligations. | Separate own fee economics and counterparty funds; obtain accounting review where needed. S07. |
| F12 | Ongoing billing is taken as proof of ongoing value. | Usage/outcomes, renewal, cancellation and customer accounts by cohort. | Investigate delivery or fit before scaling acquisition or making a satisfaction claim. |
| F13 | Licence income assumed without rights or permissions. | Asset, contributor/licence chain, scope, territory and existing grants. | Block the affected grant; obtain rights review without rewriting an unaffected service offer. S08. |
| F14 | Estimated ad metrics or pending commission are called collected income. | Defined exposure/eligible event, validation, adjustments, settlement and actual receipts. | Correct evidence state and cash schedule; do not spend hypothetical collections. S08. |
| F15 | Paid recommendation presented as independent proof. | Incentive, relationship, genuine experience and disclosure context. | Block misleading presentation; obtain required review rather than hiding the incentive. S08. |
| F16 | New monetisation removes previously promised core value. | Accepted scope, entitlements, optionality and customer impact. | Restore the boundary; justify only incremental value and obligations before an upsell/cross-sell. |

## 4. Money-model taxonomy and sequencing

Adopted contract and source-ID context: [2026-09-10-stage-05-money-model-taxonomy.md](research-logs/2026-09-10-stage-05-money-model-taxonomy.md).

### Use and accounting boundary

All thirteen required labels are retained, each with all ten required fields. They are not thirteen mutually exclusive businesses or independent revenue accounts. Initial transaction and renewal are events; recurring revenue is a pattern; upsell, cross-sell and expansion describe changes; usage describes a unit; services/licensing/platform/ad/referral describe exchanges; open-source commercialisation describes a wider setting. Combine only what a real exchange needs.

Record each transaction once with an identifier, date/period, payer, accepted terms, consideration and adjustments; attach analytical labels separately. Allocate distinct invoice lines where useful. Do not add overlapping renewal/expansion/subscription/licence reports into total revenue. A fee earned by the platform and proceeds owed to a seller belong to different parties.

In every card, gross revenue means the explicitly stated gross commercial consideration **G** for the business's own exchange, not automatically accounting revenue recognised in that period. Use **N = G − D − F**, **C = N − K** and **margin = C/N for N > 0** under the companion's declared cost scope. D is discounts; F is refunds/credits, recorded once; K is the stated direct cost. Zero/negative N does not receive a spurious margin percentage. Show acquisition/shared costs separately. Taxes, total customer obligation, principal/agent treatment and recognition timing must be reconciled with appropriate inputs; this taxonomy does not certify them.

Each dependency is a question for the actual business, not an assumed favourable answer. Unknown amounts, rates, retention, capacity, rights or payout dates remain unknown. No card supplies a market price, success rate or universal margin target. Source identifiers R01–R17 resolve in the research companion; the ten-field cards are project synthesis grounded in those sources and accepted Stages 2–4.

### M01: initial transaction

**Meaning:** The first exchange with a defined customer, whether standalone or the first event in a longer relationship. Basis: Stage 2 offer/entry research, Stage 3 P04–P06, the customer/value module (2) E09; R01–R03.

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

### M02: recurring revenue

**Meaning:** Repeated consideration associated with continuing value or entitlements; not necessarily the same as repeated payment of one finite debt. Basis: Stage 2 continuity research, the customer/value module (2) E07; R07.

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

### M03: upsell

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

### M04: cross-sell

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

### M05: expansion

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

### M06: renewal

**Meaning:** A decision/event extending an expiring entitlement or relationship; distinguish it from an instalment under an already accepted term. Basis: the customer/value module (2) continued-value evidence; R07, R10.

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

### M07: usage

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

### M08: services

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

### M09: licensing

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

### M10: marketplace take rate

**Meaning:** The platform's own consideration for enabling an exchange between other parties, under an explicitly described role and payment arrangement. Basis: R14 and the customer/value module (2) multi-sided model.

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

### M11: advertising

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

### M12: affiliate / referral revenue

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

### M13: open-source commercialisation

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

### Selection and sequence rule

Start from the evidenced customer/value exchange and the owner's objective, not the desire to use more models. Select a sufficient mechanism; state any genuinely different payer/side and what value each receives. Compare it against a simpler or unchanged option. Add another revenue step only when it addresses a real additional need with credible delivery, marginal economics, cash and rights. Preserve a no-purchase or unchanged option where applicable and existing commitments in all cases.

Before accepting a combined model, reconcile event identities, line allocations, D/F adjustments, direct/shared costs, future service obligations and counterparty funds across all cards used. Check that the first exchange is not subsidised by invented retention or that payment to one party is not booked as another's revenue. The offer/pricing failure map and synthetic S01–S08 exercise these distinctions. Accounting treatment remains specialist-owned; the experiment and legal handoff modules below govern those responsibilities.

## 5. Acquisition, lead quality and sales

Adopted contract and source-ID context: [2026-09-10-stage-06-demand-lead-and-sales-architecture.md](research-logs/2026-09-10-stage-06-demand-lead-and-sales-architecture.md).

### 2. Acquisition lifecycle: all seven candidate stages

The seven original candidate stages are retained as useful distinctions, not seven mandatory screens, forms or populated records. Some stages are anonymous or unobserved; a self-serve customer can buy without becoming an identified sales lead. Multiple people may represent one account, and one customer may later enter a new buying journey. Keep individual, account, opportunity and transaction units distinct.

| ID | Candidate stage | What is represented and what supports it | Invalid promotion / review boundary |
|---|---|---|---|
| D01 | target audience | Intended eligible population and context, grounded in the customer/value module (2) customer/problem/alternative claims. A market-size estimate states source, date, method and uncertainty. | An addressable market estimate is not reachable audience, contact permission or observed demand. Do not invent a market size to fill the map. |
| D02 | awareness / reach | Defined exposure or discoverability within a stated medium, period and population. Record impressions, reported unique reach or observed visits as the different measures they are. | Impressions are not unique people and technical delivery does not prove attention or comprehension. Cross-platform uniqueness may remain unknown. |
| D03 | response / engagement | A specific observed response, meaningful use or interaction, with source and event definition. Include negative responses and evidence-quality limitations. | Automated opens, accidental clicks, giveaway entries and polite replies do not establish fit, purchase intent or willingness to pay. |
| D04 | lead / prospect | A potential buying relationship with enough context to investigate, within permitted use. Record provenance, role, relevance and contactability separately. | Being in a database is not qualification or permission to contact. Do not turn every community member or free user into a sales prospect. |
| D05 | qualification | An evidence-based suitability assessment for this offer and next step: problem, fit, intent, authority/payer, practical timing and delivery constraints as relevant. | Qualification criteria are contextual, not a universal score or a seller's wish. Unknown budget/authority is not proven inability to buy. A clear no or opt-out is respected. |
| D06 | sales conversation / conversion path | The actual buying tasks, responsible parties, current evidence and agreed next action, whether a checkout or a complex evaluation. | Calls, proposals and repeated follow-ups are seller activity, not buyer commitment. A forecast probability or CRM label does not establish an order. |
| D07 | customer | A stated purchase, agreement or actual-use event with its exact meaning preserved. Identify paid customers separately from users and contracted-but-unpaid accounts. | A closed deal does not prove collection, activation, delivered value, retention or profit. Pass obligations and evidence to delivery and keep results connected to the originating journey. |

R01 describes configurable vendor lifecycle states, not universal definitions; this model keeps events and evidence authoritative over labels. Observed transitions may skip stages, branch, pause, re-enter or end in rejection/no decision. Capture dates, relevant reasons and open status without treating an unfinished journey as a failed one. Do not infer a monotone real-world buying process from a software property's update rules.

Post-purchase activation, actual payment, support, refunds, retention and expansion feed back into channel quality without replacing the seven candidate stages. the delivery/economics modules (6–7) owns their full operational model. Preserve the source/offer/cohort and observation horizon so that later customer quality can challenge an acquisition claim. An acquired customer is not counted again as newly acquired merely because they renew or expand.

### 3. Channel model: all thirteen classes

Each class gets a mechanism, contextual fit, evidence needed and operational limits. These classes overlap: content can be discovered through search and distributed on a platform; an existing audience can receive direct outreach; an affiliate can also be a partner. Describe the combination, allocate costs consistently and count people/accounts/transactions once at the appropriate level. Direct outreach includes warm and cold variants, not two substitute classes that displace another original requirement.

| ID | Channel class | Mechanism and conditional suitability | Evidence, cost/lag and decision limits |
|---|---|---|---|
| CH01 | direct outreach | Targeted communication to a relevant potential buyer or introducer, with relationship, medium and authority explicit. A bounded service or B2B sale may justify individual research and conversation. Basis: Stage 2 L01/L05/L10, R05/R12. | Inspect contact provenance, permissible use, actual fit, meaningful replies and buyer actions. Include research, sending, follow-up and sales time, complaints and suppression. Public data, an old relationship or a referral is not blanket permission; no volume-first automation. |
| CH02 | content | Useful explanation, demonstration or evidence helps a relevant audience understand a problem and credible option. Appropriate when actual expertise and reusable customer questions can support it. Basis: Stage 2 L04, R06/R07. | Inspect audience questions, comprehension and suitable downstream actions, not output count alone. Include creation, maintenance, distribution and expert time; benefits may be delayed. A direct offer may be simpler than a lead magnet. Never fabricate expertise, examples or customer proof. |
| CH03 | community | Participation in a group with shared needs can create understanding, trust and appropriate voluntary discovery. Distinguish serving an existing community from taking on responsibility for a new one. Basis: R07/R08. | Observe relevant participation and useful outcomes within community norms. Cost includes moderation, responsiveness and continuing obligations. Membership and contribution are not marketing consent, buying intent or free delivery labour; do not turn the community into an unsolicited lead list. |
| CH04 | search | A buyer's expressed query can connect to an informative page, product or provider through organic or paid discovery. Query intent, region and available alternatives determine fit. Basis: R03/R06/R09. | Inspect dated query/context and meaningful downstream behaviour. Separate branded/non-branded demand and paid placement from organic presence. Content work, competition and discovery lag matter; rankings, volume and attributed purchases do not prove incremental suitable demand. |
| CH05 | paid media | Purchased exposure, access or response opportunities can test a bounded audience/message/offer combination when budget, tracking and delivery constraints permit. Basis: R02/R03/R14. | Compare qualified paid-customer outcomes and downstream contribution after media, creative, agency and sales costs. Record targeting/exposure/attribution limits, refunds and cash timing. Reach or reported return on ad spend is not incremental profit; approval is required before spend or scale. |
| CH06 | partnerships | Complementary organisations coordinate access, credibility, delivery or commercial activity for a mutually specified purpose. Useful where the partner resolves a genuine customer or buying-process dependency. Basis: Stage 2 L11, Stage 3 P12, R10. | Inspect audience overlap, incentives, actual introductions, responsibilities and partner capacity. Include enablement, coordination, revenue sharing and deal lag. An agreement or partner logo is not an activated channel; preserve claim/data authority and avoid double-counted co-sold deals. |
| CH07 | affiliates | A party promotes or refers an eligible exchange for a defined commission or other incentive. Appropriate only when the audience benefits, the arrangement is credible and the economics cover it. Basis: the offer/pricing and money modules (3–4) M12 and its agreement research, R17. | Inspect programme eligibility, attribution, reversals, disclosure and net suitable acquisitions. Include commissions, administration and associated refunds/fraud; nominal referred sales are not own affiliate revenue. Paid recommendations must not masquerade as independent proof. |
| CH08 | referrals | A customer or other trusted participant introduces a suitable prospect, organically or through a specified incentive. Delivered value and genuine relevance precede solicitation. Basis: Stage 2 L09, Stage 3 P12, R04. | Keep organic baseline, referred-customer quality, reward/handling cost and repeated or self-referrals visible. Better observed referred-customer value does not prove an incremental programme effect. Avoid rewarding existing demand or inferring permission to repeatedly contact the introduced person. |
| CH09 | events | Relevant in-person or online gatherings enable discovery, demonstration and conversations with appropriate participants. Event type and audience fit matter more than attendance scale. Basis: R13 and R07. | Assess participant/buyer relevance, agreed follow-ups and mature outcomes. Include fees, preparation, travel, staffing and follow-up effort; dates and sales lag constrain evaluation. Badge scans, registrations and audience access do not automatically authorise marketing or establish an opportunity. |
| CH10 | marketplaces | Buyers and suppliers transact or discover options through an intermediary with its own access, trust, ranking and commercial rules. Appropriate when the relevant side has an actual reason to use that venue. Basis: the customer/value module (2) multi-sided model, the offer/pricing and money modules (3–4) M10, R10/R16. | Inspect both-side fit, search/matching, eligible transactions, own fees/costs and settlement obligations. Listing is not liquidity; gross merchandise value is not own revenue. Customer ownership, data access, disputes and platform dependence can limit measurement and delivery. |
| CH11 | platform distribution | A platform's catalogue, feed, ecosystem or store distributes discovery/access to an eligible product or service. It can combine with search, content, paid media or a marketplace. Basis: R09/R16. | Verify actual eligibility, listing terms, relevant exposure, qualified adoption and transaction rights. Include integration/listing/maintenance and review delays. Downloads and distribution permission are not paid demand; do not promise placement or bypass platform restrictions. |
| CH12 | product-led acquisition | Direct experience of useful product value can lead to evaluation, adoption, suitable invitations or purchase, sometimes alongside human assistance. Free access is one possible mechanism, not a universal prerequisite. Basis: the customer/value module (2) E05/E09, the offer/pricing and money modules (3–4) P12/M13, R11. | Inspect meaningful activation, user/buyer distinction, invitation permission and actual paid continuation. Include trial/free-user delivery, support and abuse costs. Usage alone is not buying authority, and open-source adoption is not paid-complement demand. Preserve accepted free entitlements. |
| CH13 | existing audience | An already reachable customer, subscriber, follower or professional audience may contain suitable demand under its actual relationship and permitted purpose. It is a starting asset, not proof of current fit. Basis: Stage 2 L01/L03, the customer/value module (2) roles, R05/R15. | Reassess relevance, freshness, engagement quality and existing permissions; separate new acquisition from renewal/reactivation/expansion. Include maintenance and contact effort. Subscriber count, email opens or historical purchase do not establish current intent or unrestricted reuse. |

This is researched option coverage, not a recommendation that every business use thirteen channels. Select only mechanisms with a plausible customer/value path and evidence appropriate to the commitment. Provider documentation establishes mechanisms and constraints, not a provider ranking or a measured local acquisition result.

### 4. Lead-quality model: all nine dimensions

Track these dimensions separately at the appropriate contact/account/opportunity and cohort level. Each finding is observed within scope, hypothesised, mixed, unknown or not applicable with a reason. Critical authority, suitability and rights gaps cannot be cancelled out by a high engagement score. No protected-trait inference, covert enrichment or fabricated persona is required.

| ID | Dimension | Measure or evidence required | Interpretation and diagnostic use |
|---|---|---|---|
| LQ01 | volume | Count the defined unique unit/event, channel/source, period and eligible population; record duplicate, test, automated and unknown-identity treatment. | Distinguish exposures, contacts, accounts, opportunities and paying customers. Volume locates flow but cannot establish quality; repeated touches are not new prospects. |
| LQ02 | fit | Evidence that the relevant population has the problem, context, eligibility and constraints the accepted offer serves, including exceptions. | Compare intended and observed fit. A prospect can be interested but unsuitable; unfamiliar or unknown characteristics do not justify invented exclusion criteria. |
| LQ03 | intent | Attributed recent buying/use behaviour, meaningful request, concrete evaluation or agreed next step, with event and date. | Separate curiosity, free interest, politeness and automated opens from an intention to buy. Intent is time/context-specific, not a personality trait inferred from a click. |
| LQ04 | qualification | Versioned, necessary criteria for this offer/next step: fit, problem relevance, authority/payer, feasibility and timing as applicable; supporting/challenging evidence and missing facts. | Use qualified, not qualified, further evidence needed, or deferred with reason. Budget unknown is not inability to buy; declining the next step is not a reason for coercive persistence. |
| LQ05 | conversion | Defined movement or buying event and matched numerator/denominator, cohort, offer version and elapsed window; won/lost/open/no-decision separately. | A lead-to-order rate differs from order-to-payment or checkout completion. Aggregate changes can reflect mix or censoring rather than better messaging, offer or sales execution. |
| LQ06 | acquisition cost | Declared attributable acquisition costs and cost basis per suitable new customer over a matched horizon; separately report cost per lead or qualified opportunity when used. | Distinguish cash spend, valued internal effort, allocated production and sales costs. Organic is not costless. Attributed cost per acquisition is not automatically incremental acquisition cost. |
| LQ07 | sales effort | Actual person-hours, specialist/partner work and repeated tasks by path/cohort, with valuation, capacity and allocation basis. | Time per win alone can hide wasted effort on losses or pending work. A cheap channel may consume the scarce operator time needed to deliver customer value. |
| LQ08 | time-to-close | Declared start and end events, dates, open age, won/lost/deferred status and observation cutoff. Report the distribution and population, not just a closed-won average. | Short observation windows undercount slow paths. Open opportunities are not zero-duration sales or definitive losses. A faster sale may still collect later. |
| LQ09 | retention / downstream quality | Link acquired cohort and accepted offer to activation, payment, meaningful outcomes, refunds, service burden, repeated value and contribution over a stated horizon. | A converted customer may be unsuitable or unprofitable to serve. Preserve new/renewal/expansion distinctions and do not replace observed cohorts with assumed lifetime value. |

For a simple self-serve exchange, necessary qualification may occur through visible eligibility and product requirements rather than a salesperson. Complex buying can require distinct user, procurement, budget and payer evidence. Do not copy an enterprise budget checklist into every consumer purchase. Timing and ability/authority to buy remain substantive inputs under LQ03/LQ04/LQ08; they do not replace any of the original nine dimensions.

### 5. Sales-path model: all eight paths

The labels describe different aspects of a journey. Self-serve/sales-assisted/consultative/enterprise concern buying complexity and assistance; inbound/outbound concern initiation; marketplace-mediated/partner-led concern mediation. A real journey can combine them. Record the actual combination and handoffs rather than forcing a false mutually exclusive classification.

| ID | Sales path | Fit, stages and buyer evidence | Controls, failure and handoff |
|---|---|---|---|
| SP01 | self-serve | A sufficiently understandable offer can be evaluated and purchased without a required salesperson. Observe discovery, relevant evaluation, transparent terms, checkout/order, payment and subsequent activation separately. Basis: the offer/pricing and money modules (3–4), R09/R11. | Accessible information and a functioning path matter; a broken payment step is not automatically a weak offer. Avoid hidden fees, obstructive cancellation and unnecessary qualification forms. Handover the actual accepted scope and service obligations. |
| SP02 | sales-assisted | A mainly understandable exchange benefits from targeted human clarification, demonstration or buying help. Record the customer's question, evidence supplied and agreed next action. Basis: R01/R12. | Track assistance cost, response/ownership and actual buyer progress. Unanswered suitable enquiries can indicate execution capacity, not lack of demand. Do not assume all self-serve buyers need a call. |
| SP03 | consultative | A consequential or context-specific need requires discovery of progress, alternatives and constraints before a suitable proposal. Buyer-confirmed needs and evaluation criteria precede recommended scope. Basis: R12, the customer/value module (2). | Questions explore rather than manufacture urgency or exploit vulnerability. Distinguish a real problem with the offer from poor explanation. Agree bounded next steps and preserve a legitimate no-purchase option. |
| SP04 | enterprise | Multiple actors, budget, procurement, security or implementation dependencies may require an agreed evaluation and approval path. Record user, economic decision-maker, buyer/payer and genuine gatekeepers only where they matter. Basis: the customer/value module (2) roles, R10/R16. | A champion, pilot or proposal is not full budget authority, contract, payment or rollout. Capture scope/acceptance, ownership, procurement dates, delivery/cash constraints and specialist questions without inventing a universal enterprise checklist. |
| SP05 | inbound | A potential buyer initiates a relevant enquiry or action. Qualify its source/context, respond within actual capacity, support appropriate evaluation and document the chosen path. Basis: R01, Stage 3 P08. | Inbound does not imply qualified demand or unlimited permission for unrelated contact. Review enquiry routing, response, expectations and fit before redesigning acquisition or pricing. |
| SP06 | outbound | An authorised targeted approach precedes a voluntary response, fit assessment and agreed buying step. Distinguish attempt, delivered communication, meaningful reply, qualification and customer action. Basis: Stage 2 L05/L10, R05/R12. | Respect purpose, contact restrictions and opt-outs; no escalating follow-up simply because a sales target is unmet. Include research/rejection effort and stop an unsuitable or disallowed mechanism, preserving valid relationships. |
| SP07 | marketplace-mediated | The intermediary participates in discovery, trust, quoting, order or settlement. Identify actual supplier, contracting payer, platform role, acceptance and fulfilment sequence. Basis: R10/R16, the offer/pricing and money modules (3–4) M10. | Differentiate submitted offer, authorised purchase, completed transaction and own fee/settlement. Platform approval does not prove buyer fit or legal clearance. Preserve counterparty funds and dispute/support responsibilities. |
| SP08 | partner-led | A partner owns or shares the customer relationship or buying work under explicit commercial and information boundaries. Document introductions, qualification, proposal ownership, customer approval and delivery handoff. Basis: R10, Stage 3 P12. | An activated partner and an accepted buyer are different events. Avoid conflicting promises, unapproved data sharing, duplicated deal attribution and uncosted partner obligations; retain a named owner for customer outcomes. |

For each active path keep a brief versioned record: selected labels; customer/offer references; entry evidence; required buyer tasks; seller/partner responsibilities; material questions and proof; current state; next mutually agreed action/date; exit event; loss/defer reason; downstream obligations and review trigger. Record evidence of commitment, not an invented win probability. Existing pipeline systems can provide authorised source records; these skills do not become their system of record or silently mutate them.

### 6. Measurement and economics contract

Every displayed measure states the question, source, event definition, unit, period/cohort, observation age, exclusions, cost/attribution basis and uncertainty. These can be links to existing definitions. Missing evidence is not zero; a zero denominator yields **not defined**, not a favourable or unfavourable rate. Anonymous reach can remain aggregate. Do not collect additional personal data solely to make every arrow linkable.

For the same eligible cohort and elapsed window, report transitions such as qualified opportunities / eligible prospects and paid new customers / qualified opportunities, with actual counts. Do not divide this month's sales from old leads by this month's newly created leads and label the result a cohort conversion rate. A closed-deal win rate, won / (won + lost), excludes open work; disclose that selection and separately show the full cohort's won/lost/open state. Reopened and duplicated records need a consistent event rule.

Define acquisition cost **A** as the selected cost scope: media and other direct spend, consistently allocated creation/tools/partner rewards and valued acquisition/sales effort as appropriate. Distinguish incurred expense, cash outflow and non-cash time/opportunity cost. Present a cash-only view separately where useful. Do not count the same commission or salary under both A and the offer/pricing and money modules (3–4)'s direct cost K. Include unsuccessful/pending acquisition work in the relevant cohort/window and declare delayed outcomes. No universal CAC, payback or LTV/CAC target is introduced.

When the new paid-customer denominator is positive, **attributed acquisition cost per customer = A / new paid customers** under the stated attribution/cohort basis. Cost per lead or per qualified opportunity has a different denominator. When no customers have yet been observed, retain the cost and count and mark the ratio not defined; do not fabricate zero-cost acquisition. A causal incremental acquisition cost requires a credible additional-customer estimate, not merely a source label.

Reuse the offer/pricing and money modules (3–4)'s **N = G − D − F**, **C = N − K** and dated cash definitions. Compare aggregate and unit contribution after the same declared A, customer quality, sales/delivery capacity and cash timing. Define which shared costs remain excluded; never label a partial residual net profit. Gross revenue divided by ad spend is not contribution, incremental return or cash available to spend. A profitable observed average is not evidence that the next tranche of audience or capacity has the same economics.

Record source and attribution rule separately from causal interpretation: first/last touch, fractional allocation, customer report or another stated method has its own meaning, lookback and missing coverage. R14 documents configurable attribution; R02–R03 show why such observations need not recover causal effect. Assign canonical transaction IDs and reconcile credit. Analytical channel labels can overlap; total business sales and costs do not multiply with the number of labels or platforms claiming credit. Cross-device/offline gaps remain explicit rather than repaired with invented certainty.

Intent proxies need instrumentation checks. R15 documents a concrete case in which remote email content may load without engagement; do not equate an open with interest or try to circumvent privacy protections. Time-to-close and retained quality require comparable observation horizons. These precautions are needed before a plausible causal story or an apparent bottleneck becomes an accepted diagnosis.

### 7. Channel-selection evidence and decision procedure

The research companion records actual source findings/limits, comparisons across all thirteen classes, and three completed **synthetic selection decisions**. Sources establish plausible mechanisms and context-dependent risks, not the best channel for an unspecified real business. Without local evidence, the responsible result is a bounded hypothesis or missing-input finding, not a fabricated winner.

1. **Set the decision.** Start from the actual objective, accepted customer/value/offer and current constraint. Preserve an effective existing channel as a comparison; consider doing no new acquisition when delivery or cash is the binding problem.
2. **Compare appropriate candidates.** Use CH01–CH13 to identify mechanisms consistent with where the relevant buyers seek help, buy or already participate. Record why excluded classes are presently unsuitable or unproved. Do not launch all channels or treat a founder preference as evidence.
3. **Record the evidence chain.** For each serious candidate, link customer access/fit, the meaningful next action, credible message/proof, buying path, cost/effort, time-to-close, downstream value/capacity/cash, source uncertainty and permissions. External research and local observations remain separate.
4. **Use independent findings, not a magic score.** Compare suitable reach, qualified progression, full declared cost, resource bottleneck, lag and retained economics. Permission, truthfulness, missing critical evidence and delivery constraints are gates, not weaknesses a large projected audience can offset.
5. **Make the smallest responsible decision.** Retain, revise, run an authorised bounded test, reject for this context, or block pending a necessary fact/approval. Specify the claim being tested, evidence that would challenge it, budget/time/customer-harm guardrails and review point. the experiment/repair modules (8–9) develops the full experiment architecture; no campaign is executed by selecting a hypothesis.
6. **Verify what changed.** Compare cohorts, definitions and offer versions. Test whether the result is reach, mix/qualification, message, offer, execution or downstream cost/quality rather than automatically trying another channel. Preserve rejected options and reasons so a context change can trigger review without erasing history.

A decision record names the owner/date, actual business context, compared candidates and unchanged alternative, source/local evidence, assumptions, chosen state/rationale, explicit costs/capacity/cash, permitted next action, stop/review criteria and unaffected decisions preserved. It is sufficient to link existing evidence instead of creating new templates for every channel.

### 8. Diagnostic model and smallest responsible repair

Begin with measurement, cohort age, identity, audience mix, offer/version changes and external constraints. Apparent funnel leakage is not itself proof of a cause. More than one constraint may exist. Distinguish **supported local finding**, **working hypothesis**, **inconclusive**, and **blocked by missing evidence/authority**; no forced root-cause label or universal stage-conversion threshold.

| ID | Problem class | Evidence and rival explanations | Bounded response and preserved decisions |
|---|---|---|---|
| DG01 | reach | Suitable people are not demonstrably exposed to the proposition. Check actual availability/distribution, intended population, query/placement and delivered exposure. Missing tracking, time lag and irrelevant targeting can mimic low reach. | Repair the implicated access/distribution/measurement hypothesis or test a suitable alternative. Do not expand traffic into an unproved or undeliverable offer, and do not rewrite an already supported customer need without evidence. |
| DG02 | qualification | Responses arrive but few meet relevant need, eligibility, intent or practical buying requirements. Inspect source mix, lead-magnet incentives, role and explicit disqualification reasons. A changed criterion or unknown authority can mimic poor fit. | Correct targeting, expectation-setting, incentive or qualification evidence. Preserve a sound offer for genuinely suitable customers; do not label an unknown or delayed buyer incapable or apply coercive pressure. |
| DG03 | offer | Suitable buyers understand the proposition but evidence challenges its value, scope, price/terms, proof, mechanism or delivery feasibility. Compare alternatives and stated/observed reasons. Confusing message, broken checkout and insufficient authority are rival explanations. | Return the implicated component to the offer/pricing and money modules (3–4)/4 with evidence. Revise or test only what fails, retaining substantiated value/terms elsewhere; legal or fulfilment blocks are not resolved by more persuasive copy. |
| DG04 | conversion | Qualified, appropriately informed buyers do not complete the actual next step. Inspect path function, accessible terms, response/ownership, approval/partner handoffs and buyer-agreed tasks. Cohort immaturity and genuine no decision may be legitimate explanations. | Fix the implicated path or sales work, clarify a real unanswered question, or retain deferred status. Do not invent urgency, conceal terms or assume every refusal is an objection to overcome. |
| DG05 | downstream economics | Customer acquisition occurs but realised contribution, cash timing, workload, activation, refunds or retained value does not support the objective. Check cost scope, collected amounts, cohort quality and marginal capacity. Attribution/mix errors can imitate an economic change. | Pause unjustified scale; repair the evidenced price, delivery, targeting, payment or cost dependency through its owner. Preserve effective communication and suitable acquisition rather than redesigning everything. |

#### Message, offer and sales execution are separate responsibilities

**Message quality:** Does the intended audience accurately understand the real, substantiated offer and next step? Compare actual wording and participant comprehension; misleading interpretation or a concealed material term requires correction, not stronger persuasion. A low click rate alone is insufficient evidence that the message is wrong.

**Offer quality:** Once accurately understood, is the exchange relevant, credible, deliverable and economically coherent for the appropriate buyer? A repeated objection can reveal a genuine mismatch. More polished wording does not repair missing value, false proof, unsuitable price/scope or impossible obligations.

**Sales execution:** Can a suitable, informed buyer complete the legitimate tasks with clear ownership, usable tools, timely responses and necessary approvals? Inspect real events, errors and handoffs. Activity quotas, a script, a demo or a CRM stage cannot substitute for observed buyer progress. R12 supplies a practitioner method, not universal proof that a prescribed script will win.

A small repair can alter a message while preserving the offer; fix a payment defect without repricing; establish budget authority without replacing the target segment; or pause growth while delivery catches up. Reassess downstream effects of a material customer/offer change under Stages 4–5. No channel result authorises promises, contact, data sharing, spend or sales commitments by itself.

## 6. Delivery, capacity, retention and expansion

Adopted contract and source-ID context: [2026-09-10-stage-07-delivery-and-retention-model.md](research-logs/2026-09-10-stage-07-delivery-and-retention-model.md).

### 2. All fourteen delivery and retention concerns

Each concern has an operational representation, evidence, a decision consequence and a failure/repair boundary. Apply it where relevant; a one-off exchange need not acquire a subscription renewal process. An omitted concern requires an explicit applicability reason, not an invented zero.

| ID | Required concern | Representation and evidence | Decision, failure and bounded repair |
|---|---|---|---|
| DR01 | fulfilment / delivery process | Link the accepted offer to actual customer and operator steps, dependencies, handoffs, work items, acceptance events and exception routes. Record touch time, waiting, backlog and completed acceptable work separately. R01, R04. | Compare sold work with work the system can finish at the required quality. A signed order is not fulfilment. Repair the failed handoff or limiting step; retain working steps unless their dependencies require wider change. |
| DR02 | onboarding | Define prerequisites, permissions, setup, necessary customer participation, first useful outcome and assistance. Observe starts, abandonment, blocked cases and completed journeys by offer/cohort, with the responsible handoff and observation cutoff. R02–R03. | A registration or completed checklist is not demonstrated value. Remove the evidenced setup or access barrier, not a necessary safety or consent step. Do not make customer effort invisible by transferring it to unpaid support. |
| DR03 | time-to-value | State the start event, first value event, elapsed interval, observation cutoff and cases not yet reaching value. Separate active effort, calendar waiting and later sustained benefit. R01–R03. | Report the distribution and unresolved cases, not only the fastest or completed journeys. A shorter form can still worsen time to a useful result. Repair the observed delay or dependency before promising a faster outcome. |
| DR04 | quality control | Define acceptance criteria tied to the promise; checks before release, outcome checks, defect severity, detection point, rework and customer recovery. Include prevention, appraisal and failure costs without counting one cost twice. R04, R07. | Throughput means acceptable outputs, not merely closed tickets. A stable process can still miss requirements. Correct the owning cause and verify unaffected requirements; an internal check is not certification or proof of customer outcomes. |
| DR05 | capacity | For each actually shared resource, record availability, skills, existing commitments, expected work mix, setup, support, rework and variation reserve over the same horizon. R03, R09. | Intake must fit every material resource and due-date constraint. Do not count the founder as independent sales, delivery and support capacity. Relieve the evidenced constraint or bound intake; average utilisation is not a delivery guarantee. |
| DR06 | service levels | Define the measured service indicator, target, operating hours, priority, measurement period, exclusions, dependencies, owner and contractual consequences where any exist. Response, resolution, availability and outcome quality remain separate. R05. | Match the promise to demonstrated capability and resources. Do not copy another business's target or mistake an internal objective for an agreed remedy. Missing feasibility or specialist review blocks the affected promise, not necessarily the whole offer. |
| DR07 | support | Describe demand types, available channels, accessibility needs, arrival profile, handling work, escalation, resolution and returned product/process feedback. Include useful assistance and failure-generated contacts. R03, R06. | Cost and staff requirements include unresolved and repeated contacts. Fewer contacts do not prove better service when access was obstructed. Repair the cause or support handoff while preserving necessary assistance and customer access. |
| DR08 | retention | Identify the original eligible cohort, customer/account/user unit, elapsed period and retained state: payment, use, delivered outcome or active relationship. Record cancellations, reactivation and missing observations distinctly. R11, R13–R15. | Continued billing cannot alone validate continuing value. Diagnose value, fit, payment failure and measurement separately; a churn-risk prediction does not establish that an intervention will help. Retain an effective acquisition channel unless its customer mix is implicated. |
| DR09 | repeat purchase | Define a genuinely subsequent purchase, original eligible cohort, observation window, refunds and expected purchase cadence. Separate repeat customers, repeat transactions and purchase frequency, with canonical order identities and exclusions. R12. | In a noncontractual business, no recent purchase is not automatically permanent churn. Compare equally observed cohorts; do not shorten the repeat interval just to claim success. Repair the evidenced relevance, delivery or timing issue. |
| DR10 | renewal | Identify contracts or entitlements actually due, the renewal decision, term, price, service obligation, approval and collected amount. Show due, renewed, declined, overdue and unresolved populations. R11, R14. | Renewal is not new acquisition, and a renewal invoice is not cash. Preserve voluntary exit and existing terms. Examine value and comprehension before discounts; future renewal demand remains a hypothesis until observed. |
| DR11 | expansion | Link optional additional quantity, scope, usage or complementary services to a new customer need. Record accepted incremental entitlement, charge, delivery/support burden, sales cost and later use. the offer/pricing and money modules (3–4); R08, R11. | Separate expansion, price increases, renewal and new customers. Do not remove an existing necessity to manufacture an upsell. Evaluate incremental contribution and capacity; preserve the working core exchange when the add-on fails. |
| DR12 | referral | Connect genuine delivered value to a voluntary introduction or recommendation, permitted incentive, qualified new customer, reward, sales effort and retained outcome. Reuse the acquisition/sales module (5) attribution and consent boundaries and [Stage 3 referral research](research-logs/2026-09-10-stage-03-professional-practice-map.md#p12). | A recommendation is not an incremental sale or permission to contact someone. Reward, attribution, delivery and acquisition costs must reconcile once. Repair an incentive or fit problem without erasing valid organic referrals. |
| DR13 | refunds / cancellations | Preserve request, eligibility/entitlement supplied by the responsible reviewer, decision, processing, settlement, service termination and dispute events. Link original order/cohort, reason, amounts, fees and recovery work. R19–R20; the offer/pricing and money modules (3–4) terms. | Request, approval and settled refund are different states. Do not present delayed processing as retention or deny valid rights to protect a metric. Correct the affected process and fund obligations; statutory and contractual conclusions stay with specialists. |
| DR14 | failure demand | Attribute avoidable repeat contact or rework to an evidenced failure of the end-to-end service. Keep value-creating support, unknown causes, duplicates and measurement gaps separate. R06, R04. | Inspect actual demand and upstream conditions before adding staff or automating symptoms. Do not classify every contact as waste, suppress complaints or mandate organisation-wide redesign. Choose the smallest change that addresses the evidenced system cause. |

### 3. Delivery-capacity model

#### 3.1 Minimum delivery record

One table in the dossier is sufficient for a small case. Record the offer/version and customer promise; unit of acceptable delivery; existing obligations and due dates; entry conditions; customer/operator/supplier responsibilities; required steps and handoffs; source-located observed work and quality; assumptions and ranges; resource availability; exception/recovery route; and the owner and next decision. References into an authorised operational system can supply details without copying a customer database into the repository.

For each material step retain: input and prerequisite; responsible resource; actual work including setup and rework; waiting/dependency; output and acceptance; failure signal; recovery owner; and evidence/window. A resource may be a person with specific competence, supplier slot, inventory pool, machine, infrastructure quota or partner service. Do not sum unlike resources into a universal capacity number.

Observe at least enough of the actual journey to identify the current decision's uncertainty. A process diagram is not evidence that the process runs. A one-time demonstration establishes only that demonstration; repeatability, variation and production-scale promises need appropriate further evidence. Current-state and proposed-state records stay distinct. R01 motivates end-to-end flow, R04 the quality-cost distinctions and R07 the difference between stable performance and meeting specification.

#### 3.2 Resource accounting and bounds

For a declared horizon and resource r, use this transparent scenario identity:

```text
required_r = existing_r + shared_r + setup_r + sum_j(quantity_j * work_rj)
headroom_r = available_r - protected_reserve_r - required_r
```

`existing_r` includes backlog and ongoing service obligations. `shared_r` includes separately budgeted sales, administration and support. `work_rj` includes the incremental onboarding, delivery, expected rework and ongoing work created by each additional unit in the horizon. Every activity is allocated once: do not put the same support allowance in both shared work and unit work. Availability excludes known absence or uncommitted volunteer time. The protected reserve is an explicit scenario input justified by variation and consequences, not an arbitrary universal utilisation target.

For one homogeneous unit, positive unit work and no changing batch/setup effects, a simple upper bound for each resource is the floor of its remaining work allowance divided by unit work. The smallest nonnegative bound across required resources limits that scenario. A negative starting headroom identifies an existing overload; reporting zero additional capacity must not conceal it. Zero incremental work means that particular resource supplies no quantity bound, not that the business has infinite capacity. Missing resources or unknown unit work block a positive capacity conclusion.

This is a **necessary resource check, not proof of schedulability or service levels**. Respect due dates, precedence, calendar coverage, simultaneous peaks, batch size, supplier lead time and indivisible tasks. A month's available hours can still fail a two-day deadline. Compare expected and credible high-work/low-availability scenarios. Rework may grow with load; preserve that uncertainty instead of assuming a constant historical average at any scale.

Keep the simple conservation check:

```text
closing backlog = opening backlog + accepted incoming work - completed work - cancelled work
```

Units and cutoff must match; completed acceptable work and rejected/reworked items must reconcile. A negative result is a data-definition error, not spare capacity. Rising backlog can identify a mismatch but not prove which cause is responsible. Avoid inferring cycle time by dividing a transient queue by an unrelated throughput average. No queueing distribution or calibrated forecast is assumed by this design.

When resources are genuinely scarce, compare feasible alternatives and opportunity costs. Contribution per limiting-resource unit can be informative under the stated mix and constraints; it is not sufficient where several resources bind, demand is limited, quality differs or contractual commitments take precedence. R09's throughput-accounting material-cost convention is not substituted for service labour and usage costs. Recheck the constraint after a repair rather than continuing to optimise a resource that no longer binds.

#### 3.3 Quality, service and recovery

Separate quality of the output, reliability of the process and the customer's achieved progress. Define observable acceptance and severity appropriate to the consequence; no generic pass percentage overrides a critical defect. Make prevention/appraisal expenditure visible alongside internal rework and external recovery. Improvement benefits remain hypotheses until measured; a cheaper inspection process can increase failures downstream.

A service-level record distinguishes indicator, target and agreed consequences, drawing on R05 without imposing an engineering-only vocabulary on every business. Specify response versus resolution, business versus elapsed hours, priority and customer/supplier dependencies. Ensure the resource plan supports the actual promised coverage. Legal/commercial reviewers own enforceability and remedies; operational owners confirm feasibility. Do not advertise an internal target as a guaranteed result.

Trace failed delivery into support, rework, refunds and retained value. A support workaround may contain immediate harm while a cause is investigated, but it is not evidence that the underlying process is repaired. Necessary recovery for existing customers continues while new intake is paused. Material threats to safety, customer rights or service integrity block optimisation of the affected action.

### 4. Retention/expansion model

#### 4.1 Cohort and event contract

Reuse the customer/value module (2) evidence identities and the acquisition/sales module (5) cohort definitions. A retention record contains cohort entry event/date, unit and eligibility, offer/price version, first-value event, full follow-up window, observed payment/use/outcome states, renewal eligibility, cancellation/refund/dispute events, expansion and reactivation, source coverage, costs and unresolved outcomes. Do not mix accounts and users or turn an unobserved outcome into a negative one.

Differentiate:

- **Point retention:** members of the starting cohort in the defined state at the cutoff. A returned customer can count if the definition allows it.
- **Continuous survival:** members without the specified exit event since entry. Re-entry does not erase an earlier exit.
- **Renewal rate:** renewals among a stated due-and-observed population, with unresolved cases shown rather than silently removed.
- **Repeat-purchase incidence:** original customers with a qualifying further purchase within an equal follow-up horizon. This does not identify permanent departure in a noncontractual setting.

These denominators answer different questions. Report actual counts with rates. A zero eligible denominator is not defined; it is not perfect retention. For immature cohorts either use a common observed horizon or a justified statistical model with its assumptions and uncertainty. Do not simply extrapolate the mature cohort's result to a new population or classify all open observations as churn.

For an operational customer-count bridge, show opening active, first-time active, reactivated and exits under a consistent event-count rule. For point cohort retention use set membership so repeated churn/re-entry cannot create impossible counts. State whether payment failure, pause, expiry or a temporary discount changes the commercial state. A vendor's active-subscriber or churn definition can differ from the business's value or contractual definition; R11 is a concrete example, not a canonical default.

#### 4.2 Revenue retention without acquisition or double counting

For the same starting cohort and comparable recurring entitlement basis, define B as opening recurring amount, L as loss from exited starting customers, Q as contraction, and E as expansion of the retained starting customers:

```text
gross revenue retention = (B - L - Q) / B
net revenue retention   = (B - L - Q + E) / B
```

Require B > 0, disjoint losses and nonnegative components. Identify canonical line changes before applying the formula. New-customer amounts are outside both numerators. Show reactivation as a separate bridge item; this base calculation excludes reactivation uplift and must not be relabelled as a different provider's metric. When a previously exited member returns, disclose its treatment and reconcile the closing balance explicitly. Separate currency effects and material price-only increases from expansion due to additional value or usage. Constant-currency analysis uses a declared conversion basis, not invented exchange rates.

Gross retention excludes expansion; net retention can exceed 100% while customers are leaving. Neither measures contribution, available cash or customer welfare. Monthly recurring revenue is a normalised recurring billing measure, not automatically recognised revenue, lifetime value or collected cash. A year's prepayment does not become twelve independent observed renewals. The formulas here are defined arithmetic over the stated components; R11's worked example was checked rather than copied uncritically (research §4).

#### 4.3 Continuing value and intervention

Review first and sustained value, customer burden, outcomes, complaints and exit reasons alongside payment. An automatic renewal can be contractual and still provide weak evidence of active preference. Conversely, low measured use can reflect instrumentation or the episodic nature of value; do not declare dissatisfaction without evidence. R14 supports examining billing inattention in its studied setting, not asserting that any particular customer forgot.

A retention action starts from a specific value, fit, payment or support problem. Record the expected mechanism, eligible population, customer choice, action cost, possible harm and required evidence. Predicted churn and response to an intervention are different questions (R15). Do not offer blanket discounts merely because a model labels people high risk. Module 8 defines the complete experiment and learning contracts; these delivery and retention records supply their operational and economic inputs.

Expansion must preserve accepted entitlements, have a genuine additional purpose and pass incremental delivery, support, sales, cash and consent checks. An upsell's higher revenue can be offset by service effort or cannibalisation. Keep new sale, renewal, expansion, cross-sell and price change as analytical tags on canonical transactions, not separate amounts to sum blindly. Referral rewards and partner fees follow the same cost identity rule and the acquisition/sales module (5)'s existing attribution/permission constraints.

Cancellation, service termination, refund and dispute are distinct events. Respect supplied rights and approval boundaries. No cancellation barrier, hidden renewal or withheld support is accepted as an improvement in retention. Record customer recovery and evidence of the underlying cause, then repair the responsible layer without rewriting a sound offer or channel unless the evidence implicates it.

## 7. Economics, cash and independent growth gates

Adopted contract and source-ID context: [2026-09-10-stage-07-unit-economics-and-cash-contract.md](research-logs/2026-09-10-stage-07-unit-economics-and-cash-contract.md).

### 1. Ownership, evidence and compatibility

Business Building defines the decision, units, assumptions, comparison and required interpretation. Deterministic calculation tools execute the arithmetic; operational/accounting systems supply source records; qualified professionals determine applicable accounting, legal and tax treatment. An agent may organise and calculate a supplied scenario within its brief, but cannot invent missing records, choose an accounting policy on behalf of a client, or treat a model result as authority to spend, charge, borrow or hire.

Keep the [the customer/value module (2) evidence contract](research-logs/2026-09-10-stage-04-business-customer-and-value-model.md) and [the acquisition/sales module (5) acquisition contract](research-logs/2026-09-10-stage-06-demand-lead-and-sales-architecture.md). Source, assumption, measurement, interpretation and decision remain separate. Every material external fact needs appropriate current verification; a historical source register is not an evergreen market-data feed. A scenario can be useful with labelled assumptions, but critical unknowns block a substantiated growth claim.

#### 1.1 Preserve the the offer/pricing and money modules (3–4) commercial definitions

The accepted [offer/pricing architecture](research-logs/2026-09-10-stage-05-offer-and-pricing-architecture.md) defines `G` as gross commercial consideration for the business's own exchange, `D` as discounts, `F` as reducing refunds/credits, `N = G - D - F`, `K` as the declared directly attributable cost scope and `C = N - K` as direct contribution. Preserve those exact meanings. `C - A - H` is a residual after declared acquisition and other costs, not automatically net profit. Adjustments, labour and commissions must not be deducted twice.

**N is not automatically recognised revenue, and direct costs are not necessarily all variable costs.** A comparison can allocate committed labour to an engagement even when that labour does not create a new cash outflow. Equally, a future capacity step can turn an apparently fixed resource into an incremental commitment. Record the decision horizon and alternatives, not only the accounting label. R08 supports relevant-cost distinctions; R10's revenue-recognition overview demonstrates why delivery and payment events must not be collapsed. Neither source supplies a treatment decision for a particular customer contract here.

#### 1.2 Cost and revenue bridges

Retain one canonical identity for each commercial event, adjustment, cost and obligation. The same item can appear in different **views**, but within one total it appears once. Each material cost record contains the amount or calculation, currency, period, source/assumption, purpose, unit/cohort attribution, behaviour over the decision horizon, cash timing and allocation basis. Mark costs excluded from a view. Do not create an accounting ledger in this repository.

Use separate, explicitly reconciled views:

| View | Meaning and reconciliation |
|---|---|
| Commercial exchange | the offer/pricing and money modules (3–4) G, D, F, N and declared K/C for the stated transaction or obligation horizon. These amounts can precede or follow recognised revenue and cash. |
| Accounting gross margin | Supplied recognised net revenue R and matched cost of sales S under the applicable accounting policy: gross profit R - S, margin (R - S) / R when R > 0. Record policy, period and classification. Business synthesis does not certify it. |
| Variable-cost contribution | For a declared aligned revenue basis B and included variable costs V: B - V. If B is recognised revenue, call it a period contribution; if B is commercial N, identify that horizon instead. Show acquisition inclusion separately. Do not silently relabel the offer/pricing and money modules (3–4) K as V. |
| Decision-relevant change | Difference between feasible alternatives in future receipts, avoidable costs, additional fixed commitments and opportunity consequences. Sunk or unchanged allocated costs do not become new cash outflows merely because a cost report contains them. |
| Whole-business sustainability | Include the resources and fixed obligations needed to continue, even when a short-run incremental decision is positive. Reconcile total cash compensation, facilities, maintenance and other material costs; missing categories prevent a net-profit conclusion. |
| Cash | Actual or forecast usable collections and payments on dates, plus verified funding. Recognition, non-cash allocation and opportunity costs are not themselves cash movements. |

A bridge identifies the difference in recognition timing, discounts/refunds, cost classification/allocation, included acquisition/shared costs and cash dates. Do not add results from these views: they are alternative descriptions of the same underlying business, not independent income streams. If the bridge is unavailable, report the views as non-comparable and request the missing data rather than picking the most favourable margin.

For a constrained employee, compare the complete alternative cash/contribution consequences. Do not both deduct an unchanged salary as incremental expenditure and charge the full foregone margin of displaced work. Conversely, removing salary from an incremental-cash view does not create free long-term labour or extra hours. The delivery model records the real shared resource constraint.

### 2. Metric contract: all twelve required economic concerns

Every metric carries: name/version and decision; formula or event rule; unit; numerator/denominator; population/cohort and attribution; period and elapsed observation age; currency/conversion; revenue and cost basis; included/excluded components; source/assumption; realised versus forecast status; calculation method/rounding; limitations; owner and review trigger. These fields may link to shared definitions instead of duplicating them. Undefined, unavailable and not applicable are distinct from zero.

| ID | Required metric concern | Definition and required evidence | Interpretation, failure and repair |
|---|---|---|---|
| UE01 | revenue per customer / transaction | For an aligned scope, divide the declared own-revenue basis by the defined distinct customer or transaction count. Label commercial N, recognised R, recurring run rate and collections separately. Preserve refunds, discounts, tax/pass-through treatment and mixed currencies. | A customer average is not a transaction average or cash per sale. More than one invoice can belong to one customer. Repair unit, period or party attribution before diagnosing pricing; never call marketplace gross volume own revenue without the appropriate basis. |
| UE02 | gross margin | Use (R - S) / R for positive supplied recognised net revenue R and matching cost of sales S. Disclose accounting basis and cost classification, including material fulfilment, hosting or labour treatment. R10; the bridge above. | A direct-commercial or variable-cost residual is not necessarily accounting gross margin. Positive gross profit can coexist with losses after acquisition/fixed costs or negative cash. Request professional treatment where classification is unresolved. |
| UE03 | contribution margin | Preserve the offer/pricing and money modules (3–4) direct contribution C/N when N > 0. Where variable-cost contribution is needed, separately define (B - V)/B and reconcile V against K and A. Include volume-dependent costs and capacity-step effects in the actual decision. R08–R09. | Do not improve the percentage by changing exclusions or counting fixed allocations as avoidable cash. Negative or zero revenue makes these margin percentages not meaningful; retain absolute amounts and causes. |
| UE04 | cost to serve | Declare attributable onboarding, delivery, infrastructure/materials, support, rework, remedies and service-management costs for the customer/transaction/cohort and horizon. Show direct, allocated and incremental views as needed. R03–R04, R08. | A low marginal software cost does not prove low support or human cost. Average cost can hide heavy-use or high-failure cohorts. Repair the implicated workload, scope, classification or population rather than assuming every customer costs the mean. |
| UE05 | customer acquisition cost | Reuse the acquisition/sales module (5) A divided by matched new paid customers where the count is positive. Identify media, production, sales/partner effort, tools, commissions, allocation, unsuccessful/pending work and lag. Cash-only CAC is a separate view. | Zero customers means the ratio is not defined, not zero acquisition cost. Renewal/expansion and free signups are not new paid customers. A labelled attribution is not a causal incremental estimate. Incomplete scope or time windows block acceptance of a CAC claim. |
| UE06 | payback period | State acquisition outflow/cost basis, start event, per-customer or cohort unit and recovery basis. Locate the first observed or forecast date when cumulative contribution or net service cash covers that acquisition amount; identify which basis is used. | Booking value is not cash recovery. If the horizon ends before recovery, say not reached within that horizon. Repeated later refunds/costs can reverse first recovery; do not equate first crossing with permanent cash safety. |
| UE07 | retention / churn | Use the delivery companion's point, continuous-survival or due-renewal cohort definitions. State exit event, reactivation, voluntary/involuntary classification, window, missing observations and counts, with the exact source-event and eligibility rules. R11, R13–R15. | A provider's rolling churn denominator is not necessarily a starting-cohort exit probability. No constant-hazard or unlimited-life forecast follows from one window. Reconcile the event/population before recommending retention spend. |
| UE08 | repeat purchase | Report original customers with a qualifying subsequent retained purchase / eligible original customers over equal follow-up, alongside repeat transaction count and frequency. State refund, same-order, reactivation and cutoff rules. R12. | No purchase yet is not established permanent churn in a noncontractual model. Do not pool immature customers with fully observed ones and call the result a comparable rate. Keep latent departure and observed repeat behaviour distinct. |
| UE09 | lifetime value assumptions | State whether the number means revenue, gross profit, direct contribution, variable contribution or discounted cash; define entry population, horizon, retention/repeat model, margin/cost evolution, expansion, discounting and evidence. Use realised-to-date separately from a forecast. R11–R14. | A revenue dashboard LTV does not pay acquisition or service costs. Unobserved retention, heterogeneity and changing economics can invalidate simple extrapolation. Use finite scenarios or unknown rather than a confident lifetime multiplier without support. |
| UE10 | refund / chargeback rate | Define request versus issued versus settled refund; amount-based versus count-based rate; original payment/order cohort versus event-date activity; duplicates, partial refunds, dispute outcomes and cutoff. Preserve actual fees and recovery timing. R19–R20. | A dispute can arrive after the sale cohort closes. Do not subtract a refunded/disputed principal twice or erase an event because a dispute was won. Repair identity/window handling before attributing a changed rate to customer quality. |
| UE11 | sales cost | Include prospecting/qualification, calls, proposals, specialist reviews, concessions administration and commissions across won/lost/pending work. Record time valuation, cash cost, allocation and role capacity. Reuse the acquisition/sales module (5) A. | Sales cost per win can hide unfinished or unsuccessful work. A commission already in A is not added again to K. Separate acquisition, renewal and expansion effort and compare like windows. |
| UE12 | support cost | Account for demand type, handling/resolution/rework effort, channels, tools, escalations, fixed coverage and incremental load. Attribute to appropriate cohorts while reconciling shared staffing and failure costs. R03–R04, R06. | Cost per closed ticket alone can reward premature closure or obstructed access. Include unresolved work and quality. Avoid subtracting a salary both through cost allocation and as an extra cash expense in the same view. |

No universal margin, LTV/CAC ratio, payback limit, retention percentage or acceptable dispute rate is introduced. Any real threshold needs the owner's objective, evidence, model context, obligations and appropriate specialist constraints. Existing provider reports are evidence with definitions, not the repository's authoritative business truth.

### 3. LTV, CAC and payback acceptance

#### 3.1 Finite, explicit customer-value scenarios

Prefer a directly observed cohort contribution-to-date where sufficient. To forecast, choose a finite horizon justified by the decision and evidence. One permitted scenario representation is:

```text
forecast contribution value over T periods
  = sum_t(expected cohort contribution in period t / (1 + discount_rate)^t)
    / original acquisition cohort size
```

The expected cohort contribution includes the chosen revenue/cost basis, retention or repeat behaviour, refunds, customer mix, expansion and support. State time-zero convention and whether costs occur before or after delivery/collection. Costs that survive churn, such as committed coverage or exit remedies, cannot disappear just because revenue stops. Acquisition is excluded from this value by default and shown once as a separate deduction for the acquisition decision. A source using an after-acquisition definition must be labelled and reconciled, not charged CAC again.

This is arithmetic over explicit assumptions, not a universal customer-behaviour model. Retention probability, purchase frequency, average order value and cost may interact; multiplying independent averages can be misleading. Account for joint scenarios when dependence matters. Record observed coverage, censored cases, selection, population changes and forecast uncertainty. A short cohort does not supply evidence for an indefinite tail. Discount rate and currency are supplied scenario choices, not investment or financing advice.

For an intentionally simple constant-contribution illustration, assume contribution m occurs immediately in period zero, the customer leaves with probability c after each period, all future contribution ceases at departure, and per-period discount rate r is nonnegative. Then:

```text
finite value(T) = sum for t = 0..T-1 of m * ((1-c)/(1+r))^t
```

Only if the stationarity and horizon assumptions are justified and the ratio is below one does the infinite geometric sum exist: `m*(1+r)/(r+c)`. At r=0 and c>0 this is m/c. When c=0 and r=0 there is no finite infinite-horizon value; the finite sum is still m*T. A revenue-based ARPU cannot be substituted for m without changing the result's meaning. A rolling churn ratio with entrants in the denominator cannot automatically be substituted for c. Invalid probabilities, missing horizon or inconsistent period units are rejected rather than repaired with made-up defaults.

The project does not make the infinite formula the default, calibrate a survival model, or assert a realistic discount rate here. R12–R13 justify distinguishing behavioural models and their settings; the displayed equations follow from the stated scenario and are checked deterministically. More complex modelling belongs in an appropriate existing calculation/research tool with auditable assumptions, not a custom universal LTV engine.

#### 3.2 Comparable acquisition and payback

Before accepting LTV/CAC, identify numerator and denominator cost bases, acquisition cohort and time window, currency, maturity, allocation and missing costs. A customer-value forecast and historical blended CAC can be compared only with the transfer limitation visible. Average past CAC and retention do not demonstrate the marginal economics of a larger future campaign. A positive ratio never overrides current capacity, customer rights or cash dates.

For cash payback, use acquisition outflow plus dated customer receipts minus the cash costs and refunds necessary for that cohort's service under the stated scope. Show other obligations and funding in the business cash model rather than disguising them as customer receipts. A first recovery date is one result; minimum subsequent balance and remaining obligation exposure are separate. An annual receipt that covers acquisition today may leave tomorrow's fulfilment unfunded.

### 4. Cash-risk model: all eleven concerns

Use a dated cash calendar supported by source records and explicit scenarios, not a profit total relabelled cash. The time horizon must encompass the commitment it informs and its material collection, delivery, renewal and refund consequences. A rolling near-term view can coexist with a longer obligation view; truncating a prepaid service at collection is not sufficient.

| ID | Required cash concern | Required representation and evidence | Risk, decision and bounded repair |
|---|---|---|---|
| CA01 | customer prepayment | Record actual cleared receipt, restrictions, customer/offer, remaining service and refund obligations, and permitted use. Pair early collections with future cost/capacity scenarios and a source-located schedule of outstanding obligations. R10, R17, R19. | Prepayment improves timing, not necessarily contribution or free cash. Do not spend all proceeds on acquisition without funding existing promises. Review pace, reserves or approved terms before assuming more sales solve the gap. |
| CA02 | receivables | Separate quote, contract, invoice, due date, disputed/overdue amount and actual collection. Forecast clearing dates with supported assumptions, delay/default scenarios and collection effort, including the payer and evidence of any revised agreement. R16–R17. | An invoice is not money available for payroll. Repair collection, billing accuracy, timing or approved credit terms; do not change a validated value proposition because the payer is late. |
| CA03 | supplier terms | Record committed orders, deposits, credit conditions, due dates, currency, minimum quantities, early-payment effects and supplier capacity/reliability. Identify source agreements, cancellation conditions, fulfilment dependencies and the owner authorised to renegotiate. R16–R17. | Never assume unused or interest-free supplier credit exists. Delayed payment can change availability, price or terms. Compare feasible agreed alternatives; the agent cannot unilaterally postpone an obligation. |
| CA04 | inventory | Track opening stock, purchases, lead times, landed cash costs, usable/sold/returned/lost stock and replenishment commitments. Align sales and recovery assumptions with actual stock and fulfilment. R16, R17. | Purchasing inventory uses cash before or independently of its expense as cost of sales. In a direct cash schedule, do not deduct both the supplier payment and an additional inventory-change adjustment for the same outflow. |
| CA05 | payroll | Use approved gross compensation, employee deductions, net pay, employer costs and remittance/benefit dates. Record hiring start, notice/commitment and actual availability separately, alongside the approved payroll source and period. R17, R21. | Net pay plus withheld amounts remitted is not paid in addition to gross pay: reconcile the components once. Employer charges and benefits can be extra. No salary, tax rate or worker classification is guessed. |
| CA06 | refund exposure | Link actual and potential remedies to eligible cohorts, request/settlement lags, dispute fees, recoverable stock, remaining service and usable funds. Use mutually coherent base and downside cases. R19–R20. | A pending processor balance cannot necessarily fund an immediate refund. A reserve is a cash restriction or planning floor, not itself a second expense when the refund is later paid. Do not assume refunds and continued full service occur together unless the obligation actually requires both. |
| CA07 | advertising spend timing | Reuse the acquisition/sales module (5) cost scope but record cash charging, deposits/credits, billing thresholds where relevant, payment dates and conversion/collection lags. Reconcile campaign billing with actual cash charges and remaining card payables. R17; accepted the acquisition/sales module (5). | Attributed revenue may arrive later or never. Card payment postponement is a dated payable, not cancelled spend or guaranteed free finance. Bound growth by verified funding and obligations, not a headline return ratio. |
| CA08 | tax obligations | Obtain applicable jurisdiction/entity/activity, basis, amount or approved estimate, tax periods, due and clearing dates, withheld/collected amounts and reviewer. R21–R22 are examples of jurisdiction-specific schedules, not defaults. | Unknown tax is not zero. Do not choose rates, eligibility, exemptions or filing treatment; request qualified inputs and assess sensitivity. A tax-related cash gap cannot be solved by ignoring or silently deferring payment. |
| CA09 | working capital | Distinguish formal current assets less current liabilities from the selected operating measure, often inventory plus trade receivables less trade payables. State inclusions, measurement dates and changes. R16. | A healthy ratio does not prove available cash or appropriately valued stock. Avoid counting customer/counterparty funds as unrestricted assets. Repair the actual stock, collection or obligation timing; reconcile any indirect bridge to the direct calendar. |
| CA10 | cash conversion | Where meaningful, calculate inventory, receivable and payable days with matched average balances, period flows and day basis. Cash conversion cycle is inventory days + receivable days - payable days. R16. | A negative cycle can coexist with poor margins and future obligations. Do not force inventory days into a pure service model, use incompatible denominators or infer clearing dates from an annual average alone. |
| CA11 | runway | Show the first date usable cash breaches the required floor in the dated scenario. A cash/net-burn ratio is only a labelled approximation when burn is positive, comparable and sufficiently stable. R17–R18. | Zero/negative average burn does not establish infinite safety; seasonal payments or refund obligations can create a near-term breach. Report minimum cash, breach date, funding gap and assumptions instead of relying on an average. |

#### 4.1 Direct cash calculation and controls

Start from reconciled opening cash. Identify restricted/customer/partner amounts separately and declare whether the main schedule is total bank cash or usable business cash. Do not count a transfer of counterparty funds as business revenue. Remove restricted amounts once in a usable-cash view; when a restricted obligation settles, reduce the corresponding restricted balance as well so the same obligation does not drain usable cash twice.

For ordered dates/events under one consistent basis:

```text
closing_cash_t = opening_cash_t + receipts_t + authorised_funding_t - payments_t
opening_cash_next = closing_cash_t
headroom_t = usable_cash_t - required_floor_t
funding_gap = max(0, -min_t(headroom_t))
```

Separate customer collections, tax/pass-through receipts and financing. Financing availability, draw dates, fees, covenants, repayment and authority require evidence. A possible investment or unused credit limit is not actual cash. Do not infer suitable borrowing or approval from a positive forecast.

Order materially different dates within a month. When same-day ordering is uncertain and liquidity is tight, examine the adverse order rather than netting away an intra-day risk. A positive month-end balance can hide inability to pay earlier. Missing dates, inconsistent signs, duplicate event IDs or mismatched currencies fail validation; do not silently coerce them into favourable values.

Keep direct and indirect cash methods separate. The direct calendar uses actual/forecast receipts and payments. An indirect reconciliation starts from a defined profit basis and adjusts non-cash items and working capital. Do not deduct an inventory purchase, then deduct the same cost again through cost of sales and the inventory movement. A specialist or existing accounting tool provides the accounting bridge where needed; the skills compare its reconciled results, not rebuild the ledger.

Compare a baseline supported by current obligations with downside cases relevant to the commitment: slower receipts, weaker retention, higher usage/support, supplier delays, refunds/chargebacks, reduced availability or a capacity step. Preserve joint consistency. For example, a cancelled service may require a refund and cessation of some future work, while sunk work and other obligations remain. Do not add mutually exclusive worst cases and call the result an expected forecast, or omit a plausible coupled failure because single-variable sensitivities look safe.

#### 4.2 Cash conversion and runway details

For period length d and aligned positive denominators, use inventory days = average inventory / cost of sales * d; receivable days = average trade receivables / credit sales * d; payable days = average trade payables / credit purchases * d. The balances and flows must use compatible currency and tax bases. A cost-of-sales proxy for credit purchases or closing-balance proxy for average stock is disclosed, not silently treated as observed equivalence. R16's exam assumptions are not assumptions for a live business.

Zero flow can make a ratio undefined even when the balance is meaningful. A genuinely inventory-free business can state inventory days not applicable, with the reasoning for any zero component used in a simplified cycle. Large seasonal swings, mixed cash/credit sales and long work in progress can make average-day measures poor forecasts of dated payments. The cash calendar remains the decision basis.

A stationary runway approximation divides opening usable cash above a declared floor by positive comparable periodic net burn. State period, excluded one-off payments and forecast limitations. If burn is zero or negative, the ratio is not a useful finite runway estimate; examine the dated obligations and possible downside instead. Growth can consume working capital faster than it earns cash even with positive unit contribution. No generic number of months is an approval threshold.

### 5. Deterministic calculation handoff

The smallest useful calculation handoff has these fields, whether implemented by a spreadsheet, calculator, existing accounting system or temporary verification script:

| ID | Handoff field | Contract |
|---|---|---|
| HC01 | decision and scope | State the business decision, accepted versions, calculation view, alternatives, horizon and material obligations. |
| HC02 | inputs and provenance | Provide source-located observations and separately labelled assumptions; units, currency, cohort, dates, exclusions and access boundary are explicit. |
| HC03 | definitions and formulas | Supply metric versions, cost/adjustment identities, revenue recognition boundary, allocation, timing convention and formula. No unexplained dashboard number is sufficient. |
| HC04 | calculation method | Identify tool/version or reproducible method, input representation, rounding policy and prerequisites. Use decimal money arithmetic or verified spreadsheet formulas; retain unrounded intermediate values where appropriate. |
| HC05 | validation and reconciliation | Check signs, ranges, uniqueness, units, matching periods, totals, balance bridges, zero denominators and boundary cases before interpreting results. |
| HC06 | outputs and scenarios | Return absolute amounts, denominators, ratios where defined, minimum dated cash/headroom, capacity consequences, base/downside results and error states. |
| HC07 | professional and authority boundary | Identify treatment requiring accounting/tax/legal input, unresolved facts and exact permitted action. Calculation success cannot grant commercial approval. |
| HC08 | evidence and review | Preserve the executed input/output identities, run result, limitations, owner, decision and trigger for recalculation. Do not claim a script was executed merely because it exists. |

Choose a simple calculator for a bounded verified expression, a transparent spreadsheet for linked scenarios, or an established operational/accounting tool for actual records and policy-driven reporting. Specification 03 defines the chosen execution boundary and actual calculation-receipt requirements; no custom accounting engine or business runtime is required. Sensitive raw business data stays in its authorised location; public examples are synthetic or explicitly approved/redacted.

### 6. Independent growth gates and repair routing

A recommendation to increase revenue-producing commitments must state the amount, timing, existing obligations and decision owner. Apply every relevant gate below; no weighted score can offset a blocking failure. Unknown material facts produce **BLOCKED**, adverse evidence **FAIL**, adequate bounded support **PASS**; **NOT APPLICABLE** needs a reason grounded in the business mechanism. These are evaluation results, not autonomous execution states.

| ID | Gate | Required evidence and consequence |
|---|---|---|
| GG01 | evidence and definition integrity | Customer, offer, cohort, cost and time-window inputs are traceable and compatible. Undefined CAC or unsupported LTV blocks the conclusion; repair records/definitions before changing the business. |
| GG02 | deliverable value and quality | The accepted promise has relevant delivery/outcome evidence, feasible dependencies and appropriate quality/recovery controls. Unsupported benefits or unsafe service block the affected commitment. |
| GG03 | operational capacity | Existing plus proposed sales, onboarding, delivery and support work fits each resource and material due-date/service-level constraint under justified scenarios. Bound intake or repair the responsible constraint; don't invent extra staff. |
| GG04 | economics and sustainability | Contribution and wider resource funding are coherent on explicit bases; marginal scale effects and excluded costs are visible. Negative contribution cannot be labelled profitable growth. A deliberately funded test is separately authorised and labelled, not a waiver. |
| GG05 | retention, expansion and downstream quality | The business's dependence on repeat value is evidenced or bounded as an explicit test. Billing, new acquisition and expansion cannot hide cohort decay, refunds or excessive cost to serve. One-off models justify which repeat assumptions are not needed. |
| GG06 | cash and obligation coverage | Dated usable cash covers existing and proposed obligations and the declared floor over an adequate horizon and relevant downside. Missing tax/funding data or a negative headroom blocks safe-scale claims even when margins are positive. |
| GG07 | customer rights, professional constraints and authority | Truthful terms, accepted entitlements, relevant specialist constraints and the responsible owner's permission remain intact. Conversion, a model pass or tool access cannot authorise spend, outreach, changed cancellation terms or a new contract. |

A whole-gate exemption is allowed only for GG05 when no repeat, renewal or expansion dependency is used in the proposed decision. Other gates may contain inapplicable submeasures, but still require their own supported conclusion. Record the result of each relevant gate, evidence, uncertainty, affected layer, retained decisions and permitted next step. A gate can permit a specifically bounded test only when its own actual resource, risk and authority requirements are satisfied; speculative lifetime profit does not fund an experiment. Recalculate affected gates after a repair. Broader redesign is justified only when the evidence shows the dependencies cannot be repaired locally.


## 8. Assumptions, experiments and learning

Adopted contract and source-ID context: [2026-09-10-stage-08-assumptions-experiments-and-learning.md](research-logs/2026-09-10-stage-08-assumptions-experiments-and-learning.md).

### 2. Assumption register

#### 2.1 Minimal record and separate ratings

Each material assumption has a stable ID and version, an explicit bounded assertion, relevant customer/role/context and time horizon, linked accepted decisions and dependencies, supporting/challenging evidence, current uncertainty, consequence if wrong, owner, and the next discriminating evidence or review trigger. An existing the customer/value module (2) claim can supply the assertion; do not copy it into several inconsistent registers.

Write an assertion narrowly enough to challenge. “People want convenience” is not adequate; an identified payer choosing a specified exchange in a particular situation is more useful. Separate evidence that the problem occurs, that the proposed mechanism addresses it, that the buyer will pay, and that delivery remains viable. One observed payment cannot validate all four.

**Uncertainty** describes the claim's evidential position: unresolved; partly informed with material gaps; supported within the observed scope; or challenged by relevant evidence. Include source relevance, age, independence, selection and contrary observations. These are not probabilities. A numeric estimate requires an explicit suitable model and data, not confidence invented by an agent. Supported within scope is not permanently or universally true.

**Consequence** describes what being wrong would do to the named decision: for example, a reversible wording correction, wasted but bounded discovery expenditure, failure of the current commercial commitment, or harm/rights/cash/quality exposure. Record the actual affected obligation and magnitude or range when supplied. Missing consequence information remains unknown. Do not multiply ordinal labels into a risk score or average an unacceptable harm against promising revenue.

Prioritise by first respecting safety, rights and authority; then identifying claims material to the pending decision; then comparing unresolved dependencies, what evidence could discriminate, and the effort/exposure of obtaining it. A highly uncertain trivial claim need not precede a partly informed claim that could invalidate the commitment. A consequential assumption can justify pausing a commitment even when no cheap adequate test exists. Record the ordering rationale and unresolved ties rather than inventing a quantitative value-of-information model.

#### 2.2 All ten specified assumption classes

These are coverage classes, not ten tests that every business must run. An actual assertion may span classes; preserve its separate dependencies rather than counting the same observation as independent proof twice.

| ID | Assumption class | Bounded question and usable evidence | What could challenge it; inference limit |
|---|---|---|---|
| AS01 | customer exists | Identify a reachable-in-principle population with the stated circumstances, role and eligibility. Distinguish verified records or direct accounts from an owner-declared segment or generated persona. | Repeated inability to find qualifying cases may challenge the segment or recruitment method, not prove universal absence. A large market statistic does not establish suitable local customers. |
| AS02 | problem matters | Establish recent circumstances, consequences, competing priorities and actual workarounds through relevant observations and neutral accounts. Include non-adopters and contrary cases where they bear on the claim. | Customers may recognise the problem yet prefer the status quo or have more urgent needs. Polite agreement or frequency in a selected interview sample does not establish population demand. |
| AS03 | customer can be reached | Identify a permissible channel and observe actual suitable exposure or voluntary response under a stated resource cap. Reuse the acquisition/sales module (5)'s separate contact, permission, fit and acquisition definitions. | Failed delivery, irrelevant placement or a restricted channel can block access without disproving the customer need. Search volume, a purchased list or tool access alone does not establish reachability or permission. |
| AS04 | offer is understood | Test whether relevant actors can explain the real outcome, scope, total price, exclusions and next step in their own terms, using a truthful concept or existing offer. | A misunderstood condition challenges presentation or expectations. Good comprehension does not establish that the exchange is desirable, affordable, deliverable or accepted by the actual budget holder. |
| AS05 | customer will pay | Observe a specified payer's authorised choice at the actual price, scope and terms; distinguish stated intention, quote acceptance, deposit, payment and later refund. | Rejection can implicate fit, value, proof, price, authority or timing. Free interest, a discounted purchase or a user without budget authority cannot establish full-price demand in another context. |
| AS06 | channel is economical | Reconcile actual attributed acquisition/sales effort with suitable new customers and downstream contribution over a matched horizon. Keep marginal scale, cash-only and full-cost assumptions explicit. | More leads or lower cost per lead can hide worse customer fit, costly sales work or losses. Attribution is not causal incrementality, and observed average CAC is not proof about the next growth tranche. |
| AS07 | delivery works | Observe a bounded end-to-end delivery with actual dependencies, acceptable quality, customer participation, rework and shared resource use. Distinguish a demonstration from repeated performance. | A missed handoff, infeasible deadline or overloaded resource challenges delivery at that scope. A sale or a technically completed output is not proof of a reliably delivered promise. |
| AS08 | customer receives promised value | Link the customer's actual progress to a defined baseline/alternative and the proposed mechanism, retaining timing, effort, side effects and competing explanations. | Completed onboarding, use or satisfaction alone may not establish the promised outcome. Attribute causal benefit only with adequate identification; a credible customer account can still reveal a specific broken promise. |
| AS09 | customer stays / repeats | Observe an eligible cohort over an appropriate repeat/renewal horizon with payment, use, outcomes, cancellation and reactivation semantics explicit. Preserve customer choice and immature cases. | Expansion or new acquisition can conceal departures, and automatic collection can differ from active preference. No repeat yet is not necessarily permanent churn in a noncontractual business. |
| AS10 | economics remain viable at scale | Compare proposed incremental volume with cost, price, retention, service variation, resource constraints, cash dates and wider sustainable funding. Use observed limits and clearly labelled scenarios. | Saturation, heavier usage, capacity steps or delayed collections may invalidate extrapolation. A profitable small pilot or positive lifetime ratio does not by itself justify increased commitments. |

Unknown current facts become research inputs. An observation changing the population or offer scope creates a new claim version and downstream review under the customer/value module (2); it does not rewrite old evidence as support for a new segment. Preserve invalidated claims and reasons as history rather than deleting the failures.

### 3. Experiment contract

#### 3.1 All nine required fields

An experiment record has an ID/version, accountable owner, linked decision and accepted baseline versions, creation/freeze time, permitted operations, and the nine fields below. Freeze the plan before observing the result used to evaluate it. Material amendments retain the old version, when and why they changed, and what data were already visible. Internal versioned records are sufficient; this design does not require publishing confidential plans to an external registry. R01 supports distinguishing planned and exploratory analysis.

| ID | Required field | Minimum useful contract | Invalid shortcut and control |
|---|---|---|---|
| EX01 | assumption | Link the exact assertion/version, context, uncertainty, consequence and decision dependency. Identify which link is being tested and which related assumptions the test will not resolve. | A broad ambition or an entire business model is not one measurable assumption. Split claims when one observation would otherwise be misrepresented as validating several untested links. |
| EX02 | hypothesis | State the predicted observation under the proposed mechanism, its comparator or baseline where needed, plausible rival explanation and the scope of any descriptive or causal inference. | “This will work” cannot discriminate. An exploratory study may generate hypotheses, but must name the question and possible decision implications without pretending it confirms a prediction invented afterwards. |
| EX03 | cheapest valid test | Compare adequate candidate methods against the actual decision, evidence needed, fidelity, resources, risk and existing data. Select the least burdensome sufficient option and explain why cheaper alternatives are inadequate. | Do not use a popularity poll to prove paid retention, or impose a randomised trial when a documented delivery defect already resolves the decision. No adequate affordable test means bound or defer the commitment, not weaken validity. |
| EX04 | target population | Specify eligibility, observed versus intended actors, recruitment/access, exclusions, unit of assignment and analysis where relevant, and the population to which results may apply. | Friendly users, visitors and authorised buyers differ. Repeated sessions or contacts are not automatically independent participants; privacy restrictions cannot be bypassed to join records or increase sample size. |
| EX05 | success / failure signal | Define observable events, measures, denominators, practical acceptance or rejection criteria and competing outcomes, including incomplete or inconclusive evidence. Retain downstream value and adverse signals alongside the primary result. | Downloads, calls or an arbitrary significance threshold cannot substitute for the decision's outcome. Specify what would challenge the claim and distinguish a failed business hypothesis from an invalid measurement process. |
| EX06 | guardrails | State allowed exposure, spend, work/capacity, cash, quality, rights, truthfulness, data use and participant safeguards, together with monitoring, stop triggers, owner and recovery obligations. | A favourable primary metric cannot override harm or an unfunded promise. A missing critical guardrail or approval blocks launch; breaching one stops the affected exposure and preserves evidence rather than hiding adverse results. |
| EX07 | duration / sample requirements where relevant | Set the necessary observation/maturation horizon, recruitment/exposure unit, information or precision need, maximum resource duration and stopping/analysis plan. Justify statistical sample design when making statistical claims. | A fixed week, activity quota or small convenient sample is not universally sufficient. Insufficient independent exposure or slow outcomes can make a result inconclusive even after the budget is exhausted. |
| EX08 | confounders | Identify material alternative explanations, mix and time effects, concurrent changes, selection, missingness, interference and instrumentation risks. State prevention, checks and residual identification limits. | A before/after difference is not automatically caused by the change. Multiple changes may test a coherent bundle, but cannot identify each component's effect without an appropriate design. |
| EX09 | decision rule | Before results, map meaningful outcome regions, invalid evidence, inconclusive findings and guardrail stops to bounded next decisions, required approvals and preserved baseline choices. | If every possible outcome produces the same success claim, the test is not useful validation. An action rule may retain a baseline under uncertainty; it must not recast that operational decision as proof of no effect. |

The contract does not authorise execution. The owner approves the named external actions and budget; operators and existing systems perform assignment, communication, data collection or delivery. The evidence returned includes the actual version used, deviations, exposure and stop events. Missing mandatory access, rights or human input blocks the real task; during this bootstrap any such required user decision stops the sequence under its execution contract.

#### 3.2 Selecting an adequate method

| Method candidate | Suitable narrow question and minimum evidence | What it cannot establish by itself |
|---|---|---|
| Existing-record or calculation audit | Resolve a wrong denominator, duplicate cost, missing event, breached promise or cash date with traceable records and deterministic reconciliation. | A corrected number does not demonstrate a new causal intervention, market demand or future scalability. No new experiment is required merely to fix proven arithmetic. |
| Neutral interview or observed workflow | Explore recent circumstances, roles, alternatives, burden and mechanisms; record recruitment and contrary accounts. R02. | Hypothetical intention, selected-sample frequency and enthusiasm are not population prevalence, payment or causal lift. |
| Truthful concept/comprehension or usability test | Examine understanding of actual scope/terms or an explicitly described prototype, with the relevant role attempting the needed task. | An attractive mock-up or successful task does not prove deliverable production economics or paid retention. Missing functionality is disclosed. |
| Honest interest, quote or purchase test | Distinguish interest from an actual authorised payer choice at specified terms. A presale explicitly states availability, obligations and uncertainty. | A fake checkout or hidden nonexistence is not accepted. One paid choice does not prove premium demand, a different segment or repeat behaviour. |
| Bounded manual service or delivery trial | Observe real work, first value, defects and resource use at a limited authorised scope; include customer and supplier participation. | A one-off concierge success does not prove automated, repeated or scaled delivery. All promises and recovery obligations still apply. |
| Randomised comparison where appropriate | Estimate the stated intervention effect with valid allocation, comparable observation, correct analysis unit, suitable measures and an explicit inference plan. R03–R06. | Randomisation does not guarantee representative recruitment, legal acceptability, absent spillovers, a good metric or viable net economics. |
| Non-randomised comparison or modelled scenario | Compare observed cohorts, historical alternatives or declared economic/capacity assumptions when the decision can tolerate stated identification and forecasting limits. | A correlation, forecast or scenario is not an observed causal effect. An untestable identifying assumption remains visible rather than becoming a confidence claim. |

Choose the evidence needed first and then minimise unnecessary effort. Opportunity theory can suggest a distinctive hypothesis even when feedback is difficult to obtain; do not reject it solely because a cheap proxy cannot test it. Conversely, novelty does not exempt it from an adequate bounded commitment. This retains the Stage 3 comparison between theory-guided search and experiment discipline without claiming a fresh empirical validation of that debate.

#### 3.3 Timing, inference and validity

For a quantitative effect claim, specify the outcome or estimand, practical decision threshold, population, assignment/analysis unit, comparator, variability or baseline assumptions, suitable error/precision or power requirements, multiplicity treatment and observation horizon. A calculation tool or qualified analyst supplies the appropriate design and inference. R03's single-proportion normal-approximation guidance is not copied as a universal two-arm, clustered or retention sample calculator.

Use a predefined fixed-horizon analysis or an appropriate explicitly specified sequential procedure; repeatedly inspecting ordinary fixed-horizon significance results and stopping at a favourable one is not the same thing. R05 supports the existence of valid continuous-monitoring methods, not permission to use any stopping rule. Safety, cash and rights monitoring continues regardless of the statistical plan. A safety stop may leave the primary effect unestimated or biased; record that rather than pretending a full planned run occurred.

Check allocation, exposure, event identity, missingness, duplicates, delayed data, cohort maturity and consistent definitions before interpretation. A statistically diagnosed sample-ratio mismatch is a symptom requiring investigation, not proof of one particular defect; ordinary chance imbalance alone is not an automatic mismatch diagnosis. R06–R07 motivate integrity checks. Do not remove inconvenient groups or condition on treatment-affected outcomes merely to restore an attractive comparison. Material unresolved integrity failures prevent the affected causal conclusion, not honest reporting of the raw observation or urgent recovery work.

Keep effect magnitude, uncertainty, practical relevance and downstream economics distinct. Failure to cross a statistical threshold is not proof of equivalence; a precise tiny improvement can still be commercially insufficient. R04 supports interpretation in context rather than a single-number decision. Equivalence or non-inferiority requires its own prespecified margin and suitable analysis. Exploratory segments and new hypotheses are useful, but must be labelled; data used to discover them is not independent confirmation. No default probability that a hypothesis is true is inferred from a p-value.

If Bayesian or other specialised inference is chosen, document its model, prior or other assumptions, decision loss/threshold and stopping validity as applicable. No statistical vendor, universal framework or experimentation runtime is mandatory. Conditional methods need specialist or tool verification appropriate to the consequence, and calculations cannot make biased inputs representative.

#### 3.4 Interpretive result versus next decision

Use a result description that carries both scope and limitations:

- **Supports within tested scope:** the valid observation meets the prespecified relevant signal; untested dependencies remain unknown.
- **Challenges the stated claim:** valid contrary evidence conflicts with the bounded prediction; identify the actual claim challenged rather than declaring the whole business false.
- **Inconclusive:** valid data do not discriminate sufficiently, observations are immature, or important competing explanations remain.
- **Not interpretable for the intended inference:** the design, data, identity, population or material protocol deviation prevents that conclusion; preserve any narrower legitimate observation.
- **Stopped by a guardrail:** cease the affected exposure and recover as authorised; separately state what, if anything, the partial evidence can support.

These labels describe findings, not five automatic actions. The next decision can retain a supported baseline, request missing evidence, propose a different bounded test, reject the proposed change, correct a specific layer, stop commitments or propose a justified model change. The result and action need a reasoned link. For example, budget exhaustion can justify not continuing a test while the hypothesis remains inconclusive. Successful comprehension can justify testing a paid exchange, not an immediate acquisition scale-up.

Before implementing a favourable change, recheck the relevant the delivery/economics modules (6–7) GG01–GG07 gates, accepted terms and action authority. Scope remains bounded to the tested population and mechanism unless independent evidence supports transfer. A document status or a statistical result cannot silently approve a new segment, recurring charge, staffing commitment or platform-wide rollout.

### 4. Learning record

Every completed, stopped or uninterpretable test produces a linked record, not only successful tests. Retain the plan/version as it existed before the relevant observations, actual operations/exposure and deviations. Source records stay in their authorised location; public repository fixtures are synthetic or explicitly approved and redacted. Do not publish private customer accounts to make the record look auditable.

| ID | Required field | Record to preserve | Decision-integrity boundary |
|---|---|---|---|
| LR01 | assumption | Exact claim/version, scope, uncertainty, consequence and affected decision before the test, including supported and challenging prior evidence. | Do not rewrite the original assumption to match the observed result or substitute a weaker question after learning which outcome is favourable. |
| LR02 | test | Frozen contract/version, method, actual dates, population, resources, conditions, execution evidence, stopping event and deviations from plan. | A written plan is not an executed test. Report what actually happened, including failed recruitment, technical interruption or withheld approval. |
| LR03 | observed evidence | Traceable records or attributed accounts, counts/denominators, units, source/collection dates, cutoff, missing cases, adverse events and permitted-use limits. | Keep synthetic and real observations separate. No unseen event becomes zero, no duplicate becomes a new participant and no source quote becomes a local customer result. |
| LR04 | result | Reproducible measures or qualitative findings and the applicable interpretive state, using the stated method and uncertainty boundaries. Include failed checks and contrary observations. | Distinguish an invalid measurement from a challenged business hypothesis. Do not present a raw rate or activity count as proof of a broad effect. |
| LR05 | interpretation | Explain which claim is supported, challenged or still unresolved, plausible rival causes, scope of generalisation and how plan deviations affect confidence. | Conclusions may be weaker than initially intended. A causal story, improved confidence or unchanged result label is not evidence that uncertainty was resolved. |
| LR06 | decision | Name the bounded action or deliberate no-change decision, owner, approvals, reason, accepted versions preserved and economic/operational constraints consumed. | Approval does not upgrade the evidence. Rejecting further expenditure is not proof of no demand, and a positive signal is not blanket permission to scale. |
| LR07 | what remains unknown | List unresolved dependencies, immature outcomes, identification limits, missing roles/data and assumptions about transfer or scale that the test did not address. | Do not delete inconvenient gaps to produce a completed narrative. An unknown can block the next commitment even when the tested narrow claim is supported. |
| LR08 | next experiment / commitment | State the next decision, needed evidence, smallest adequate test or approved commitment, limits, responsible owner and review/stop trigger; include no further action where justified. | Avoid an endless test queue detached from a decision. The next action cannot silently exceed the prior permission, budget, population or accepted customer obligations. |

Record the actual change in decision-relevant knowledge: a claim narrowed, an alternative rejected, a mechanism found wanting, a measurement problem exposed or an explicit uncertainty retained. Do not create a composite learning-speed score from calls, experiments or documents. Counts may describe workload; they do not measure the truth or value of learning.

Version changes are append-only in the logical record: preserve superseded plans and conclusions, link the correcting entry and explain the discrepancy. Storage can remain ordinary documents and existing systems. A correction to erroneous data must propagate to affected interpretations/decisions, while keeping unaffected accepted choices intact. The diagnosis and repair companion defines that routing.

## 9. Constraint diagnosis, preservation and repair

Adopted contract and source-ID context: [2026-09-10-stage-08-constraint-diagnosis-and-repair.md](research-logs/2026-09-10-stage-08-constraint-diagnosis-and-repair.md).

### 1. What a constraint finding means

A binding constraint limits the next feasible improvement toward the accountable owner's objective within a stated horizon and obligations. It is not simply the smallest percentage, the busiest team, the largest raw cost or the latest complaint. A weak-looking metric can be irrelevant to that decision; several limitations can bind together. Keep the objective, unit and time window explicit before comparing signals.

Reuse the [the customer/value module (2) business/claim/decision map](research-logs/2026-09-10-stage-04-business-customer-and-value-model.md), [the offer/pricing and money modules (3–4) offer and pricing](research-logs/2026-09-10-stage-05-offer-and-pricing-architecture.md), [the acquisition/sales module (5) diagnosis](research-logs/2026-09-10-stage-06-demand-lead-and-sales-architecture.md#8-diagnostic-model-and-smallest-responsible-repair) and [the delivery/economics modules (6–7) delivery/cash/economics](research-logs/2026-09-10-stage-07-unit-economics-and-cash-contract.md). Do not replace these with a second taxonomy of commercial truth. The table below routes observations to those owners.

A diagnosis record contains the decision/objective and baseline versions; symptom with event, population and period; source evidence and integrity limits; candidate explanations and their discriminating observations; the supported or provisional constraint; scope and consequence; proposed correction or further test; protected accepted choices; owner/approval and review trigger. It can be one ordinary table row with links. A customer record, model-generated cause or five-question conversation alone is not causal proof.

### 2. Constraint taxonomy

CT01–CT13 preserve all thirteen candidate constraints in original §5 in their original order. CT14–CT15 are project-selected measurement/design routes needed to prevent invalid evidence from being misdiagnosed as business failure. Fifteen routes are a design choice, not a new bootstrap quota, universal ontology or fifteen skills. A case can implicate several routes with reasons.

| ID | Constraint or repair route | Evidence and important rival explanation | Smallest responsible correction and preserved boundary |
|---|---|---|---|
| CT01 | demand | Relevant customers show insufficient need or willingness to pursue the exchange under the observed conditions. First check intended versus observed population, reach, offer comprehension and timing. | Revisit the specific need/segment/value assumption only when evidence implicates it. An inaccessible channel or poor explanation is not enough to abandon an otherwise supported customer problem. |
| CT02 | lead quality | Responses are poorly matched to need, eligibility, intent or buying authority. Inspect source mix, incentives, actual role evidence and versioned qualification criteria. | Correct targeting, expectation-setting, incentives or the missing qualification evidence. Preserve an offer that works for suitable customers; unknown budget is not proof of inability to buy. |
| CT03 | conversion | Suitable informed buyers fail to complete a legitimate next step. Inspect technical errors, missing ownership, process complexity, approval delays and genuine no-decision cases. | Repair the identified path or handoff, or retain deferred status. Do not reprice or rewrite the whole product for a payment defect, and do not pressure every refusal into a sale. |
| CT04 | price | At the actual scope and terms, buyer choice or contribution evidence implicates the pricing level, unit, package or payment structure. Separate message, value and collection problems. | Compare bounded price/scope/term alternatives through the offer/pricing and money modules (3–4) while preserving the supported exchange. No fabricated anchor, concealed renewal or universal premium/discount rule substitutes for local evidence. |
| CT05 | retention | An eligible mature cohort fails the defined continued-value, renewal or repeat expectation. Inspect use/outcomes, acquisition mix, onboarding, payment failures and observation maturity separately. | Fix the supported value, fit, onboarding or billing cause. Preserve appropriate customer exit and a functioning channel unless its acquired population is responsible; expansion cannot erase departing customers. |
| CT06 | delivery capacity | Existing plus proposed work exceeds a material resource, dependency or due-date limit. Inspect shared sales/support time, variation, backlog, setup and rework rather than counting nominal hours. | Bound new intake, reschedule where authorised or correct the limiting process/resource. Preserve existing customer obligations and quality; extra sales do not create missing skilled capacity or committed supplier time. |
| CT07 | gross margin | A declared recognised-revenue/cost-of-sales view fails the decision's margin requirement. Check accounting basis, discounts, refunds, cost identities, mix and timing before blaming an offer. | Repair the implicated price, cost or delivery assumption and obtain treatment clarification where necessary. Do not rename direct contribution accounting gross margin or omit costs to pass a target. |
| CT08 | cash | Usable cash does not cover dated obligations or the required floor. Reconcile collections, restrictions, payroll, tax, refunds, supplier dates and authorised funding over the full commitment horizon. | Correct collection or payment timing, reduce proposed commitments or request an approved feasible funding decision. A positive profit or payback ratio cannot override the actual earlier cash gap. |
| CT09 | sales capacity | Required qualification, proposal, negotiation or approval work exceeds available appropriately skilled resources. Include lost and pending opportunities, specialist involvement and shared delivery responsibilities. | Reduce or prioritise intake, fix the failing handoff, or propose an authorised capacity change. Preserve a supported message/offer and do not invent unlimited founder or partner availability. |
| CT10 | fulfilment quality | Actual delivered outputs miss the accepted promise or create material defects, recovery work or customer harm. Distinguish stable process output, inspection completion and achieved customer value. | Contain the affected failure, honour existing recovery obligations and fix its evidenced owner. Do not sell more, suppress complaints or downgrade acceptance criteria to make completion figures improve. |
| CT11 | onboarding | Suitable customers cannot reach the first useful outcome because prerequisites, access, setup, comprehension or assistance fail. Check whether the event measured is actually value, not mere registration. | Repair the failing setup step or support handoff with appropriate design/technical ownership. Preserve needed safety/consent checks and valid product/value choices unless the observed failure implicates them. |
| CT12 | product value | Relevant customers do not achieve the intended progress despite adequate understanding and delivery of the nominal output. Examine the mechanism, alternative and actual burden or adverse effects. | Revisit the implicated value proposition or production requirement and design a discriminating test. Cosmetic messaging or more bonuses cannot repair absent benefit; allow broader change when the fundamental assumption fails. |
| CT13 | trust | Suitable buyers lack credible, understandable proof or face inconsistent claims, unclear terms or broken promises. Distinguish actual risk from merely low attention or a confusing sales path. | Correct unsupported claims, missing substantiation or inconsistent obligations. Seek appropriate research/legal/production review; never manufacture testimonials, guarantees or urgency to overcome a real evidence gap. |
| CT14 | measurement / evidence integrity | Event identity, denominator, cohort, costs, allocation, missing data, source access or observation cutoff makes the apparent result unreliable for its intended claim. | Repair or qualify the data and reissue affected analysis; preserve actual observations and accepted business choices. A logging failure is not automatically evidence of poor customer value or a failed experiment hypothesis. |
| CT15 | experiment design / inference | Test scope, population, fidelity, confounding, information, stopping or post-result changes prevent the planned inference. A valid but imprecise result may instead be simply inconclusive. | Retain the plan and observations, label the limit and choose a justified redesign or no further test. Do not invent causality, relabel exploratory findings as prespecified success or rewrite the business solely because a test was inadequate. |

Legal/ethical restrictions, customer rights, safety and missing authority are **cross-cutting gates**, not low-scoring commercial dimensions. They can block an action in any route regardless of the apparent bottleneck. Module 10 defines the complete specialist handoff, under the professional boundary in specification 01. Compliance is not inferred from a higher conversion rate or a model's approval label.

### 3. Diagnosis procedure

First specify the next decision, target outcome, accepted baseline, resource/obligation horizon and customer population. Reconcile the observation's meaning before choosing a cause: compare event definitions, source access, denominators, elapsed follow-up, offer versions, customer mix, costs and cash dates. A red metric whose definition changed may require a measurement correction rather than an operational intervention.

Next enumerate plausible explanations capable of producing the symptom and the evidence that would distinguish them. Include an unaffected baseline or no-change explanation. Compare observations from the actual business path; do not deduce cause merely because a table places one stage before another. A qualitative account can reveal a specific failure, but frequency or generality remains a separate question.

For each serious candidate, ask what would improve if that limitation were relieved, what else would then bind, and what dependencies or existing rights would be affected. Use the the delivery/economics modules (6–7) resource and economic/cash scenarios with their assumptions, not a universal bottleneck score. Feasible improvement can be limited by several gates; no forced single root cause is required. If evidence cannot distinguish candidates, record a working hypothesis or inconclusive diagnosis and choose the smallest adequate test from the experiment model.

Finally decide among no change, containment, local correction, a bounded test, or an explicitly justified coordinated model change. If immediate harm, broken obligations or cash exposure is evidenced, authorised containment may need to precede complete causal explanation. That urgent action does not prove the suspected cause; preserve the uncertainty and review it after containment. A metric fluctuation alone does not justify emergency authority or a wholesale pivot.

### 4. Repair-routing contract

Each proposed repair is attached to a diagnosis and accepted decision versions. These eight fields make preservation and verification operational without building a universal change engine.

| ID | Repair field | Required content and constraint |
|---|---|---|
| RR01 | responsible layer and evidence | Name the supported or provisional CT route, exact symptom/claim, source evidence, competing explanations and certainty limits. Unsupported cause labels cannot authorise broad change. |
| RR02 | smallest sufficient change | State the bounded proposed change and compare no change or an adequate smaller alternative. If several coupled layers must change, explain why a local repair cannot satisfy the objective. |
| RR03 | preserved decisions and obligations | Identify accepted customer, value, offer, price, channel, delivery and terms that remain unchanged, plus rights/obligations that cannot be withdrawn. Preserve source versions and original evidence scope. |
| RR04 | dependency and impact review | List only genuinely affected downstream claims, calculations, assets, processes and specialist constraints, with retain/review/revise/block dispositions. Review is not automatic regeneration or loss of accepted evidence. |
| RR05 | approval and execution owner | Identify the accountable approver, qualified reviewer where needed, operator, permitted operation and authority evidence. A proposal is not permission to mutate CRM, billing, advertisements, contracts or customer records. |
| RR06 | bounded resources and reversibility | State exposure, timing, costs, capacity, cash and recovery/rollback where feasible. An irreversible commitment needs proportionate evidence and approval; do not describe it as a harmless test. |
| RR07 | verification and decision rule | Define the observation that would show the proposed correction worked, relevant guardrails, comparison/uncertainty and what to do if it fails or remains inconclusive. Avoid changing the acceptance rule after results. |
| RR08 | learning and regression handoff | Preserve actual before/after evidence, deviations, result, decision, unresolved causes and follow-up. Send escaped reasoning defects to later benchmark design with a reproducible case and expected failure/repair, not a false claim of an implemented regression suite. |

A local failure does not permit changing everything that is convenient to regenerate. For a proved checkout error, retain the customer/offer/price while routing the technical repair to its owner. For negative contribution caused by a known high-support cohort, investigate fit, support or scope before redesigning unrelated brand assets. For a cash gap, test dates and commitments before treating the market thesis as false.

Preservation is not immobility. If evidence rejects a fundamental target/value assumption or reveals a dependency that cannot be repaired locally, propose the smallest coherent bundle of changes with explicit new hypotheses and impact review. A bundle can be tested as a bundle; a positive combined effect does not identify every component's individual effect. Never preserve an unsafe or deceptive choice merely because someone previously approved it.

## 10. Specialist issue and legal-constraint handoffs

Adopted contract and source-ID context: [2026-09-10-stage-09-ethical-and-legal-handoffs.md](research-logs/2026-09-10-stage-09-ethical-and-legal-handoffs.md).

### 2. Seven-step handoff loop

| ID | Step | Required operation and retained evidence |
|---|---|---|
| HF01 | identify issue | Name the affected action, representation or obligation and all relevant LH routes below. Explain the observed trigger, not just a generic risk label; contain an evidenced harm through authorised procedures when necessary. |
| HF02 | preserve facts | Retain exact text, accepted versions, relevant dates, customer/party roles, source locators and contradictory facts. Separate observation from assumption. Preserve evidence lawfully in its authorised location, not by copying sensitive records into public GitHub. |
| HF03 | state business intention | Specify what the business proposes to change, the desired benefit, alternatives, affected people, timing, cost and responsible owner. A larger conversion estimate is context, not a justification for bypassing constraints. |
| HF04 | surface assumptions | Identify unknown applicability, status, permissions, terms, evidence and jurisdiction. State what each missing fact could change. Do not turn a likely exemption, generated consent record or hoped-for review into a fact. |
| HF05 | route legal question | Prepare a bounded question and necessary evidence for Legal Skills, counsel or the relevant specialist; transmit it only when that communication is authorised. Name the requested finding and decision deadline. Route overlapping privacy, consumer, employment, tax and regulated questions to their proper owners. |
| HF06 | consume resulting legal constraint | Record the attributed conclusion, factual assumptions, jurisdiction, effective dates, scope, source and review triggers. Check that it applies to this action/version. Unanswered, conflicting, expired or materially conditional findings remain unresolved. |
| HF07 | adjust offer / channel / process | Propose the smallest sufficient compliant correction, identify preserved decisions, recompute affected economics/cash and obtain action approval. Operators execute; verify the implemented wording and behaviour, return evidence and reopen the issue if the constraint is not actually met. |

### 3. Issue packet and returned constraint

A packet can be one linked document. Include issue ID/version and state; exact decision and intended external effect; relevant customer, payer, entity and operator roles; jurisdictions and reasons they may apply; action/contract/observation dates; evidence locators and access restrictions; exact claims, terms and current behaviour; assumptions and contrary evidence; applicable existing policies/findings; the bounded questions and requested reviewers; interim protection; owner, response deadline and blocked dependency. Use approved redacted extracts only where necessary. This record does not itself establish legal privilege or permission to disclose client material.

A returned finding identifies its author and remit, question answered, reviewed factual/version boundary, applicable jurisdiction, sources and their legal status, effective or transitional dates, conclusion and limitations, required/prohibited actions, unresolved conditions and review trigger. Owner approval identifies a separate action, scope and budget. Where formal regulatory approval is required, preserve evidence of the actual authorised approver and relevant permission; ordinary sign-off is not an equivalent.

Resolve with separate results: **PASS** means the bounded business review has adequate evidence, applicable constraints and required authority; it does not certify legality or automatically execute anything. **FAIL** means the proposed conduct contradicts a known constraint or the project’s truthfulness boundary. **BLOCKED** means a material fact, applicable finding or required permission is unresolved. **NOT APPLICABLE** is allowed for a particular route only with a recorded reason; it cannot exempt the whole action from ethical review. A draft may remain draft without pretending these results already exist.

For a conditional finding, enumerate the conditions and require evidence for each before relying on it. Silence is not approval. A conflict goes back to the appropriate reviewers with both findings intact, not to the commercially more convenient opinion. A changed claim, purpose, customer group, territory, law or material data flow triggers applicability review even when the marketing name is unchanged. A new source publication does not automatically invalidate every accepted decision; review the affected dependencies.

A known harmful or deceptive practice is contained before optional optimisation or completion of diagnosis. Preserve legitimate customer rights and existing promises during repair. Do not erase refund entitlements, suppress complaints or invent emergency authority. Urgent facts can justify an authorised containment request without claiming to have established the entire legal or causal analysis.

### 4. Complete handoff catalogue

All twenty original §16 topics are retained below in their original order. They are routing concerns, not twenty mandatory legal opinions for every business. A single issue can use several routes; reuse the shared packet and do not count the same evidence twice. Source identifiers resolve in the research companion and support the stated research distinctions, not a local legal clearance.

#### LH01 — advertising substantiation

**Trigger and facts:** Launching a measurable performance, quality or superiority claim. Preserve the exact words, medium, audience, product/version, implied claim, source studies, method, dates and contrary findings; a book’s assertion is not local customer evidence.

**Question and owner:** Advertising counsel or Legal Skills: what substantiation and qualifications are required for this exact claim and audience, and does the supplied evidence cover the inference? Research specialists may assess the underlying measurement.

**Returned constraint and smallest repair:** Obtain the permitted wording, evidential limits and required disclosure. Remove or narrow an unsupported claim before publication; preserve a useful offer and route missing proof to research. A footnote cannot rescue a contradictory headline.

**Research basis:** [R01](research-logs/2026-09-10-stage-09-research-and-sources.md#r01), [R02](research-logs/2026-09-10-stage-09-research-and-sources.md#r02).

#### LH02 — comparative claims

**Trigger and facts:** Naming or implying a competitor or alternative in price, feature or outcome comparisons. Preserve the dated comparable offer, unit, fees, conditions, availability, test method, selection rule and relevant trade mark or presentation context.

**Question and owner:** Advertising and, where relevant, competition/IP counsel: is the comparison like-for-like, verifiable and appropriately presented; which claims, names and qualifications are permissible? Do not infer current competitor terms from memory.

**Returned constraint and smallest repair:** Return the comparison’s scope, evidence and presentation constraints. Correct the comparison or omit it while retaining independently supported benefits. Do not translate a limited result into a universal best-in-market claim.

**Research basis:** [R01](research-logs/2026-09-10-stage-09-research-and-sources.md#r01), [R02](research-logs/2026-09-10-stage-09-research-and-sources.md#r02), [R09](research-logs/2026-09-10-stage-09-research-and-sources.md#r09), [R17](research-logs/2026-09-10-stage-09-research-and-sources.md#r17).

#### LH03 — guarantees

**Trigger and facts:** Adding a result promise, warranty or money-back assurance. Capture the actual promise, eligibility, duration, exclusions, remedy, request path, responsible entity, evidence of capability and funds, and existing customer rights.

**Question and owner:** Consumer/commercial counsel: what additional obligation is created, which terms or exclusions are acceptable and how does the promise interact with existing rights? Operations verifies fulfilment; finance supplies exposure, not legality.

**Returned constraint and smallest repair:** Receive a defined obligation and remedy boundary, then reconcile wording, service process and cash exposure. Block unsupported new guarantees. Honour existing obligations through the responsible operator; an economic shortfall is not permission to erase them.

**Research basis:** [R02](research-logs/2026-09-10-stage-09-research-and-sources.md#r02), [R06](research-logs/2026-09-10-stage-09-research-and-sources.md#r06), [R08](research-logs/2026-09-10-stage-09-research-and-sources.md#r08).

#### LH04 — scarcity / urgency

**Trigger and facts:** Creating a deadline, stock count or capacity claim. Preserve its real cause, evidence, start/end, affected offer, inventory or staffing constraint, refresh behaviour and what happens when availability ends.

**Question and owner:** Advertising/consumer reviewer: does the presentation truthfully describe the limitation without creating a misleading pressure mechanism? A genuine limit can still be presented misleadingly.

**Returned constraint and smallest repair:** Return approved scope and any qualification. Remove fabricated scarcity and ensure real expiry behaviour matches the statement. Preserve the underlying product and price rather than invent a new deadline after every failed sale.

**Research basis:** [R01](research-logs/2026-09-10-stage-09-research-and-sources.md#r01), [R02](research-logs/2026-09-10-stage-09-research-and-sources.md#r02).

#### LH05 — testimonials / endorsements

**Trigger and facts:** Publishing reviews, endorsements, ratings or success stories. Capture authenticity and provenance, permission, incentives, editing, representativeness, moderation rules and the objective claims embedded in the statement; minimise personal information.

**Question and owner:** Advertising/consumer counsel and privacy reviewer where needed: what verification, disclosure, permission and publisher controls are required? Distinguish genuine opinion from evidence supporting an objective product claim.

**Returned constraint and smallest repair:** Use genuine, permitted material with required disclosure and fair handling of reviews. Reject invented people and outcomes; do not conceal a paid relationship or remove contrary reviews solely to improve conversion. Preserve authorised truthful material.

**Research basis:** [R02](research-logs/2026-09-10-stage-09-research-and-sources.md#r02), [R03](research-logs/2026-09-10-stage-09-research-and-sources.md#r03), [R14](research-logs/2026-09-10-stage-09-research-and-sources.md#r14).

#### LH06 — email / SMS outreach

**Trigger and facts:** Contacting people by email or SMS. Preserve sender, subscriber type, location, purpose, solicited status, source and wording of consent, relationship and exception facts, suppression state, identity and unsubscribe path.

**Question and owner:** Privacy/direct-marketing reviewer: which communication and personal-data rules apply; is consent or a specific exception available on these facts, and what records, notices and opt-out handling are required?

**Returned constraint and smallest repair:** Return the authorised audience/purpose and conditions. Exclude unverified or suppressed contacts; repair targeting and consent records, not by assuming every public address is permission. Preserve a legitimate requested message or properly reviewed corporate campaign.

**Research basis:** [R04](research-logs/2026-09-10-stage-09-research-and-sources.md#r04).

#### LH07 — privacy / tracking

**Trigger and facts:** Introducing cookies, SDKs, pixels, identifiers, profiling or data sharing. Capture actual device access, purposes, parties, data flows, retention, transfers, user controls and personal/sensitive-data involvement, not merely the vendor’s product label.

**Question and owner:** Privacy counsel or qualified reviewer: what consent, exception, lawful basis, notices, contracts, assessments and user controls are required for each purpose and transfer? Determine whether a cited exception’s conditions actually hold.

**Returned constraint and smallest repair:** Receive purpose-specific constraints and configuration acceptance evidence. Suspend unreviewed tracking, or choose a lower-data method where sufficient. Do not call advertising tracking essential for revenue or treat all analytics as automatically exempt.

**Research basis:** [R04](research-logs/2026-09-10-stage-09-research-and-sources.md#r04), [R05](research-logs/2026-09-10-stage-09-research-and-sources.md#r05), [R15](research-logs/2026-09-10-stage-09-research-and-sources.md#r15).

#### LH08 — subscription terms

**Trigger and facts:** Drafting a recurring offer or changing existing terms. Preserve total price, billing cadence versus commitment, trial conditions, service entitlement, variation, cancellation, customer type, purchase channel and accepted historical version.

**Question and owner:** Consumer/commercial counsel: are formation, transparency, fairness, notice and variation requirements met, and which current or future regime covers these contracts? The business objective is not a reason to suppress a material term.

**Returned constraint and smallest repair:** Return acceptable wording, customer information and change procedure. Reconcile sales, checkout, billing and support. Preserve existing entitlements pending a valid change; a signed clause or visible link is not automatic clearance.

**Research basis:** [R06](research-logs/2026-09-10-stage-09-research-and-sources.md#r06), [R07](research-logs/2026-09-10-stage-09-research-and-sources.md#r07), [R09](research-logs/2026-09-10-stage-09-research-and-sources.md#r09), [R10](research-logs/2026-09-10-stage-09-research-and-sources.md#r10), [R11](research-logs/2026-09-10-stage-09-research-and-sources.md#r11).

#### LH09 — automatic renewal

**Trigger and facts:** Renewing or converting a trial into paid service. Capture agreement date, renewal event, amount, term, information and reminder records, cancellation route, platform role and any applicable transitional treatment.

**Question and owner:** Consumer counsel: what current notice, consent, reminder, cooling-off or transition requirements cover this cohort and event date? Check commenced rules separately from policy announcements.

**Returned constraint and smallest repair:** Implement the returned renewal conditions through approved operators. Block concealed conversion or a silent new commitment; retain voluntarily chosen recurring value. Do not treat a future commencement announcement as an operative rule; obtain current applicability evidence for the actual event date.

**Research basis:** [R06](research-logs/2026-09-10-stage-09-research-and-sources.md#r06), [R07](research-logs/2026-09-10-stage-09-research-and-sources.md#r07), [R10](research-logs/2026-09-10-stage-09-research-and-sources.md#r10), [R11](research-logs/2026-09-10-stage-09-research-and-sources.md#r11).

#### LH10 — cancellation

**Trigger and facts:** Changing the exit journey or delaying a cancellation request. Preserve real steps, authentication needs, availability, notices, fees, request/effective dates, access consequences and billing behaviour; test the journey, not only its help text.

**Question and owner:** Consumer/commercial counsel, with UX and security input: which exit routes and consequences are required, and is the proposed friction justified rather than obstructive? Avoid inventing a universal number-of-clicks legal rule.

**Returned constraint and smallest repair:** Return exit and confirmation conditions. Remove coercive hurdles while preserving proportionate security; verify request receipt, effective cancellation and subsequent billing separately. Existing complaints and entitlements remain actionable, not erased by redesign.

**Research basis:** [R06](research-logs/2026-09-10-stage-09-research-and-sources.md#r06), [R07](research-logs/2026-09-10-stage-09-research-and-sources.md#r07), [R10](research-logs/2026-09-10-stage-09-research-and-sources.md#r10), [R11](research-logs/2026-09-10-stage-09-research-and-sources.md#r11).

#### LH11 — refunds

**Trigger and facts:** Offering, refusing, processing or funding refunds. Capture product/supply type, jurisdiction, sales channel, dates, reason, accepted terms, statutory versus additional remedy, amount, payment state and supporting evidence.

**Question and owner:** Consumer/commercial counsel decides entitlement and applicable conditions; the payment operator resolves settlement; finance models available funds. Ask about deadlines, permitted deductions and rights without presuming all purchases share one rule.

**Returned constraint and smallest repair:** Return remedy and timing constraints, then reconcile approval, submission, settlement and customer communication. Honour established rights; do not replace cash with credit or deny a valid remedy solely to protect margin. Record disputed facts without inventing entitlement.

**Research basis:** [R07](research-logs/2026-09-10-stage-09-research-and-sources.md#r07), [R08](research-logs/2026-09-10-stage-09-research-and-sources.md#r08), [R06](research-logs/2026-09-10-stage-09-research-and-sources.md#r06).

#### LH12 — pricing presentation

**Trigger and facts:** Presenting a headline, discount, unit or periodic price. Capture all unavoidable charges, tax inputs, minimum term, optional extras, reference-price history, currency and any genuinely uncalculable customer-dependent amount.

**Question and owner:** Consumer/advertising reviewer and tax specialist where necessary: what total or prominent calculation and qualifications are required, and is the comparison price substantiated? Do not make an independent tax classification to improve the headline.

**Returned constraint and smallest repair:** Return an accurate presentation contract. Correct the affected display and downstream totals; preserve the underlying approved price where feasible. Instalments cannot hide total commitment, and future policy proposals do not excuse deceptive presentation today.

**Research basis:** [R01](research-logs/2026-09-10-stage-09-research-and-sources.md#r01), [R02](research-logs/2026-09-10-stage-09-research-and-sources.md#r02), [R09](research-logs/2026-09-10-stage-09-research-and-sources.md#r09), [R11](research-logs/2026-09-10-stage-09-research-and-sources.md#r11).

#### LH13 — financing / credit

**Trigger and facts:** Adding instalments, deferred payment, lending, broking or credit referrals. Capture creditor, supplier and intermediary roles, agreement date, charges, term, borrower and location, permission evidence and referral incentives.

**Question and owner:** Consumer-credit counsel or appropriate regulated specialist: does this arrangement enter a regulated perimeter or exception; what permissions, promotion, affordability, disclosure and redress requirements apply?

**Returned constraint and smallest repair:** Return a fact-specific route and permission requirements. Hold an unreviewed credit feature without blocking the ordinary non-credit purchase option. Neither interest-free wording nor an old BNPL article proves exemption; verify the actual provider and activity.

**Research basis:** [R12](research-logs/2026-09-10-stage-09-research-and-sources.md#r12), [R13](research-logs/2026-09-10-stage-09-research-and-sources.md#r13).

#### LH14 — financial promotions

**Trigger and facts:** Publishing an invitation or inducement relating to investments, credit or other potentially controlled activities. Preserve exact content, context, destination, audience, product, speaker, remuneration, links and proposed approval or exemption route.

**Question and owner:** Financial-regulatory counsel identifies perimeter and route; an appropriately authorised approver is used where required. Ask which permissions, audience restrictions, risk information and ongoing controls apply.

**Returned constraint and smallest repair:** Retain attributed findings and actual approval evidence for the exact version. Do not treat general legal review, an owner’s sign-off or a disclaimer as regulated approval. Block the affected promotion, not unrelated factual company information.

**Research basis:** [R13](research-logs/2026-09-10-stage-09-research-and-sources.md#r13).

#### LH15 — earnings / investment claims

**Trigger and facts:** Claiming income, savings, returns or ROI, including through testimonials. Preserve gross/net basis, costs, time horizon, population, selection, outcome distribution, losses, causal assumptions and whether an example is hypothetical.

**Question and owner:** Advertising/consumer or financial-regulatory reviewer: what support and presentation are required, and does the claim also trigger a regulated promotion? Distinguish business-course earnings, operational savings and investment returns.

**Returned constraint and smallest repair:** Narrow or remove unsupported promises; label genuine scenarios without implying observed results. Keep substantiation and typicality limits visible. A favourable calculation proves arithmetic only; it does not establish achievable earnings or make a testimonial representative.

**Research basis:** [R02](research-logs/2026-09-10-stage-09-research-and-sources.md#r02), [R13](research-logs/2026-09-10-stage-09-research-and-sources.md#r13), [R14](research-logs/2026-09-10-stage-09-research-and-sources.md#r14).

#### LH16 — children / vulnerable users

**Trigger and facts:** A service may be accessed by children or affect people in vulnerable circumstances. Capture actual access context, foreseeable effects, interaction design, data use and support needs using the least sensitive evidence sufficient.

**Question and owner:** Children’s-privacy, consumer or relevant sector specialist: what safeguarding, best-interests, accessibility, consent and support constraints apply? Examine actual service use; a declared adult target or user checkbox cannot answer every question.

**Returned constraint and smallest repair:** Return protective design and data limits, then verify the journey with appropriate specialist input. Reject exploitation of distress or susceptibility. Do not exclude all vulnerable customers or infer personal traits merely to make targeting easier.

**Research basis:** [R01](research-logs/2026-09-10-stage-09-research-and-sources.md#r01), [R15](research-logs/2026-09-10-stage-09-research-and-sources.md#r15), [R16](research-logs/2026-09-10-stage-09-research-and-sources.md#r16).

#### LH17 — competition / unfair commercial practices

**Trigger and facts:** A partnership, marketplace, pricing discussion or conduct could restrict competition or unfairly pressure consumers. Preserve proposed agreements, information exchanged, parties, timing, market context and commercial incentives; restrict access to sensitive material.

**Question and owner:** Competition counsel reviews coordination, information exchange and market conduct; consumer counsel handles unfair practice questions. Ask about the exact arrangement rather than treating collaboration, market share or industry custom as a safe harbour.

**Returned constraint and smallest repair:** Suspend the questionable exchange or restriction while reviewing it. Preserve independently set prices and legitimate collaboration. Do not circulate competitor-specific future plans to improve forecasts, or assume a small business cannot raise competition issues.

**Research basis:** [R01](research-logs/2026-09-10-stage-09-research-and-sources.md#r01), [R17](research-logs/2026-09-10-stage-09-research-and-sources.md#r17).

#### LH18 — employment / contractor matters

**Trigger and facts:** Designing staffing, contractor engagement or incentive terms. Capture actual control, substitution, integration, work pattern, payment, place of work, contract and relevant jurisdictions, not just the desired classification.

**Question and owner:** Employment counsel reviews rights and obligations; tax specialists separately review employment status for tax and payroll. Ask which missing facts determine each result and which proposed terms are permissible.

**Returned constraint and smallest repair:** Return distinct attributed findings and associated operating costs. Correct the engagement or staffing scenario through approval. Do not label someone self-employed to remove protections, or present a tax-tool outcome as a complete employment-rights decision.

**Research basis:** [R18](research-logs/2026-09-10-stage-09-research-and-sources.md#r18), [R19](research-logs/2026-09-10-stage-09-research-and-sources.md#r19).

#### LH19 — tax

**Trigger and facts:** A price, revenue model, staffing plan or cash forecast depends on tax treatment. Capture entity and transaction jurisdictions, supply type, registrations, customer status, dates, records and professional inputs without exposing identifiers publicly.

**Question and owner:** Qualified tax/accounting advisers determine registration, treatment, reporting and payment obligations. Business Building asks the bounded question and consumes approved amounts and dates; it does not optimise a tax position itself.

**Returned constraint and smallest repair:** Return dated inputs, calculation owner and review trigger. Update the affected price or cash scenario deterministically. Unknown tax is not zero; a claimed exemption or changed income label must not be adopted without support.

**Research basis:** [R19](research-logs/2026-09-10-stage-09-research-and-sources.md#r19), [R20](research-logs/2026-09-10-stage-09-research-and-sources.md#r20).

#### LH20 — regulated sectors

**Trigger and facts:** The actual product, service, claim or operational activity may enter a regulated sector. Capture intended purpose, users, territory, functionality, claims, licences, provider roles and deployment changes; include services built from general-purpose components.

**Question and owner:** Appropriate sector counsel and technical/regulatory experts: which classification, authorisation, evidence, safety, conduct or reporting requirements apply to the specific activity? Finance and medical examples are not an exhaustive sector catalogue.

**Returned constraint and smallest repair:** Hold the affected launch or claim until the necessary findings exist. Preserve legitimate lower-risk functionality without disguising the true intended use. A general-purpose model, open-source licence or app-store acceptance does not confer regulatory clearance.

**Research basis:** [R12](research-logs/2026-09-10-stage-09-research-and-sources.md#r12), [R13](research-logs/2026-09-10-stage-09-research-and-sources.md#r13), [R21](research-logs/2026-09-10-stage-09-research-and-sources.md#r21).

## 11. Handoff completion and consistency

Every outgoing brief carries the relevant accepted versions, exact question/action, source/assumption distinctions, constraints, owner, permitted operation and required return evidence. Technical binding and uncertain-effect handling follow H01–H08 in specification 03. A research brief is not completed research, an offer brief is not a delivered product, and a prepared specialist packet is not a sent message or professional finding.

Before accepting a returned result, inspect identity, actual execution state, source semantics, periods/units, completeness, conflicting evidence and limits. Reconcile duplicate transactions/costs and cash restrictions once. Link the result to the claim and original test, update the learning record, review implicated dependencies and retain unaffected choices. A changed tool or pack is not itself evidence for a business pivot. Material missing facts block only the conclusion or commitment that needs them; retain legitimate narrower findings.

Workflow acceptance requires a traceable next decision without invented facts, correct and executed calculations where used, complete relevant records, independent GG01–GG07 findings for growth, current applicable constraints and exact action authority. Specification 04 defines how actual responses are graded, including legitimate alternative decisions, a correct stop and inconclusive evidence.

---

Specification 02 · Contract version 1.0 · 12 September 2026
