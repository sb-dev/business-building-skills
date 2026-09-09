# Stage 1: Business-building domain and professional boundary

**Date:** 9 September 2026  
**Branch:** `feat/bootstrap-2`  
**Record type:** Domain design and requirement-by-requirement analysis, not empirical business validation  
**Acceptance:** See [conformance evidence](2026-09-09-stage-01-conformance.md) and [bootstrap progress](bootstrap-2-progress.md). A content pass is not a remotely verified stage completion.

## 1. Authority, inputs and provenance

The acceptance contract is [Bootstrap specification v1.1](2026-09-08-business-building-skills-new-project-bootstrap-process.md), read from `main`, particularly §8 (Stage 1), §§1–5 (purpose, family position, knowledge rule and principles), §7 (workspace), §§34–36 (acceptance, non-goals and success). Later-stage sections were read to identify ownership and prevent premature work, not to execute them.

The baseline is commit `010e9abeb2dc73dd17c37d1f8ed6f72d9097c545`, root tree `59369c4eb3802c8e2a45a152d548e9ffd9ca632f`. The governing specification blob is `a0ac1b6c78a0cde8ccd9aca6fda6c5b0880c516d`. GitHub reads confirmed exactly three baseline files: root `README.md`, `docs/research-logs/README.md`, and the governing specification. Both READMEs were read. The first identifies a bootstrap workspace, not a production product; the second makes research logs the durable evidence and decision store. No earlier accepted Stage 1–26 outputs exist on this clean baseline.

The [execution contract](2026-09-09-bootstrap-2-execution-contract.md) is the user's attached instruction file, preserved verbatim. Its SHA-256 is `3927a0190242a7e8b2add790e9030a55ddaf61fadf139dae2ee58a22fb9a0d85`. `feat/bootstrap-2` was created at the baseline and its remote ref was read back before substantive work. The implementation and artefacts on `feat/bootstrap` and all other feature branches were not read or reused. A branch-name listing was used only to establish whether the authorised branch already existed.

Sources actually accessed for this stage are the governing specification, both baseline READMEs, GitHub branch/tree/commit metadata and the attached execution contract. No book, customer dataset, market study or external professional source is asserted to have been examined. Decisions below are domain-design resolutions derived from the acceptance contract. They are not findings about customer demand or evidence that a business method works.

A local `git clone` attempt failed with `Could not resolve host: github.com` (exit 128). No local checkout or installation is claimed. The connected GitHub API remains the route for repository inspection, Git tree construction, commit creation and remote verification. Local staging files support content checks only. Stage 1 does not require clean external installation; Stage 24 does and must assess its own tools when reached.

## 2. Stage-specific acceptance checklist

References in this record are to the original bootstrap specification unless prefixed `Execution contract`.

| Checklist field | Stage 1 requirement and treatment | Specification reference |
|---|---|---|
| Stage purpose | Define business-building ownership and professional boundaries independently of any one book. | §8 purpose and exit; §1 |
| Required inputs | Original `main` specification, global constraints, Stage 0 READMEs, clean baseline and execution instructions. | §§1–8, 34–36; Execution contract §3 |
| Prerequisites | Workspace exists; required three files can be read; authorised branch starts exactly at `main`; no prior accepted stages are required. | §7; Execution contract §§2–3 |
| Questions to resolve | Resolve every item in the 12-line `Resolve` list, without treating scope decisions as observed customer facts. | §8 `Resolve` |
| Required research | Inspect the domain contract and applicable principles; no external source quota or book extraction is prescribed in Stage 1. Broader empirical research belongs to Stage 3. | §§8–10 |
| Required activities | Assess candidate outcomes, resolve scope, distinguish neighbouring work, define handoffs, quality and exclusions. | §8 |
| Required comparisons | Explicitly distinguish all ten named neighbouring responsibilities; compare greenfield/existing and consumer/B2B applicability. | §8 |
| Required candidate discovery | Assess all 12 supplied candidate outcomes; Stage 1 requires no independently generated candidate pool or final skill selection. | §8 candidate outcomes; §20 assigns skill design to Stage 13 |
| Required analysis | Trace the complete business lifecycle, decision versus execution ownership, finance depth, authority and professional risk. | §§1–2, 5, 8 |
| Required decisions | Decide owned outcomes, user roles, coverage, professional boundaries, approval points and non-goals. | §8 |
| Required deliverables | Domain charter, responsibility map, user model, quality dimensions, human/legal handoffs and non-goals, in this durable research log. | §8 research-log output |
| Required contents | Each of the six outputs must resolve its responsibility in substance; the twelve scope resolutions must be explicit. | §8; Execution contract §§5–6 |
| Exact counts | Verify the 12 source scope items, 12 candidate dispositions, 10 named distinctions and 6 output categories are covered. These are enumeration checks, not invented quotas for skills. | §8 |
| Exact distribution | No levels or category distribution is prescribed for Stage 1. The five-level example distribution belongs to Stage 15. | §§8, 22 |
| Exact naming | No Stage 1 filename is prescribed; use a descriptive dated research log. Repository and branch names remain exact. | §§7–8; Execution contract §2 |
| Exact structure | Keep outputs under `docs/research-logs/`; preserve the three baseline files and do not create the production scaffold. | §7; §28 assigns scaffolding to Stage 21 |
| Required prompts | None in Stage 1; exact example prompts belong to Stage 15. | §§8, 22 |
| Required examples | None to select or implement in Stage 1; do not substitute hypothetical scenarios for empirical evidence. | §§8, 22–24, 29–30 |
| Required tests | Direct semantic conformance review and explicit completeness checks; no product benchmark execution is required here. | §8 exit; Execution contract §5 |
| Required execution | Actually read prerequisites, write outputs, execute checks, inspect the staged Git tree, commit this stage and verify the remote result. No live business action is authorised by domain design. | §8; Execution contract §§3–7 |
| Required measurements | Enumerated coverage, actual file presence and unchanged baseline hashes; no commercial-performance measurement is prescribed here. | §8; Execution contract §5 |
| Required verification | Re-read original §8; check content, consistency, traceability, links, authority, non-goals and absence of premature work. | §§5, 7–8, 34–36; Execution contract §5 |
| Research-log output | Preserve inputs, limitations, resolutions, alternatives, conformance, unresolved questions, exit assessment and next-stage inputs. | §8; Execution contract §6 |
| Exit criteria | Explain what building a business means without referring to one book, with all current requirements satisfied and a remotely verified commit. | §8 exit; Execution contract §7 |
| Explicitly later work | Book extraction (Stage 2), empirical research (3), detailed models (4–9), tools (10–11), architecture/packs/examples/evals (12–17), canonical specs (18), public README (19), cross-project review (20), scaffold/implementation/installation (21–24), integration/maturity and shared extraction (25–26). | §§9–33 |

## 3. Domain charter

### Mission and owned result

Business Building Skills owns the reasoning that connects customer needs, a deliverable value proposition, commercial choices, acquisition and sales, delivery, retention, economics and cash into an explicit business model. It turns uncertainties into testable assumptions, uses observed evidence to evaluate choices, identifies the current binding constraint and proposes the smallest responsible correction while preserving validated decisions.

“Building a business” means making and revising those connected choices so that value can be delivered repeatedly under the business's economic, operational, human, legal and ethical constraints. A persuasive offer, a finished product, a busy acquisition channel or growing revenue alone is not an accepted demonstration of that outcome. This definition does not depend on book terminology. It expresses the target discipline, not a guarantee of business success. (§§1, 5, 8, 36.)

The family owns reusable business judgement and business artefacts, not every activity needed to operate a company. It must remain independently installable and useful without Pactwright or another family project. Where specialist projects exist, it exchanges evidence, requirements and constraints with them. Where they are unavailable, it provides a handoff for a human or appropriate external tool rather than inventing a dependency or claiming the specialist work is complete. (§2.)

### Complete lifecycle coverage

Coverage includes opportunity framing; customer/problem and alternative; value; offer; pricing and monetisation; acquisition and qualification; sales/conversion; delivery and onboarding; retention, repeat purchase, expansion and referral; economics, capacity and cash; experimentation and evidence; diagnosis, review and bounded repair. Economics, evidence and constraints apply throughout, not merely after sale. This is a responsibility boundary, not the detailed business-system schema assigned to Stage 4. (§§1, 4–5, 8, 11.)

| ID | Scope question from §8 | Resolution |
|---|---|---|
| R01 | owned business outcomes | Own the twelve outcomes in §4 below as decision artefacts, evidence assessments and bounded recommendations. Do not promise revenue, profitability, growth or market fit as guaranteed results. |
| R02 | intended users | Serve people accountable for business decisions and agents assisting them; distinguish business owner, functional contributor, specialist reviewer and execution operator in §5. These are intended roles, not validated personas. |
| R03 | business lifecycle coverage | Cover the full lifecycle above, including post-sale value, retention, cash, experimentation and repair. Do not equate business building with launch or marketing. |
| R04 | greenfield vs existing-business work | Greenfield work starts with explicit unknowns and inexpensive valid tests. Existing-business work starts with observed performance, existing obligations and accepted decisions, then locates the responsible constraint before changing anything. Neither mode permits fabricated evidence. |
| R05 | consumer vs B2B applicability | Support both. For consumer work distinguish user, payer, purchase and renewal where relevant. For B2B distinguish user, buyer, economic decision-maker and procurement/approval roles where relevant. Do not assume identical channels, sales cycles, delivery or retention economics; detailed models belong to Stage 4 and later packs. |
| R06 | business strategy vs tactical execution | Own choices about segment, value, offer, business model, channel, sales path and experiments, plus bounded recommendations and briefs. A recommendation to send, publish, spend, charge or change a live system is not authorisation to do it. |
| R07 | financial-analysis depth | Own managerial business-model reasoning: price/cost assumptions, unit and contribution economics, retention-dependent acquisition analysis, capacity, scenarios and cash timing. Deterministic tools own arithmetic; accounting/tax professionals own accounting treatment, filings and tax conclusions; investment and personal financial advice are excluded. |
| R08 | marketing / sales boundaries | Own channel fit, qualification criteria, commercial message requirements, sales-path design and evidence-based diagnosis. Research gathers external evidence; creative teams produce final assets; authorised operators and tools execute outreach, ads and CRM changes. Do not optimise lead count without downstream quality. |
| R09 | operations boundaries | Own delivery feasibility, capacity and cost assumptions, service promises, onboarding/retention requirements and identification of operational constraints. Operators own fulfilment, staffing, procurement, support transactions and operational systems of record. |
| R10 | legal / tax / regulated-activity boundaries | Identify risk surfaces, preserve facts and questions, route to Legal Skills or qualified advisers and consume resulting constraints. Do not determine legality, tax treatment, regulatory permissions or suitability of financial products. Unresolved material constraints block the affected recommendation or commitment. |
| R11 | human approval points | A responsible human approves customer-facing claims and terms, commitments, spending, data use, live-system mutations and changes to accepted business decisions. Specialist clearance and owner approval are distinct; neither substitutes for the other. See §7. |
| R12 | non-goals | Retain the sixteen initial exclusions in §8 below and the specialist execution distinctions in §6. Do not create a universal business operating system, tool platform or autonomous executive authority. |

## 4. Owned outcome responsibility map

All twelve supplied candidates are retained as bounded business responsibilities. Retaining an outcome is not selecting a skill, command, provider, package or implementation. No outcome is owned merely because one of the source books discusses it. (§§3–4, 8.)

| ID | Candidate outcome | Business Building owns | Required grounding and downstream boundary |
|---|---|---|---|
| O01 | opportunity framing | A bounded opportunity and the decision it could justify, including constraints and material unknowns. | Supplied context is distinguished from verified market facts; commission external research rather than inventing demand. |
| O02 | customer/problem model | A declared customer/problem account with evidence strength, alternatives and uncertainties. | Interviews, behaviour or other observations require provenance; customer research execution is separate. |
| O03 | value proposition | The connection between a customer's desired progress and the value the business proposes to deliver. | Claims trace to customer evidence or remain hypotheses; creative wording cannot manufacture proof. |
| O04 | offer | Outcome, scope, deliverables, exclusions, proof needs and commercial obligations as a coherent proposition. | Delivery must be feasible; claims, refund promises and guarantees require the appropriate human/legal checks. |
| O05 | pricing | Pricing-structure options, trade-offs, assumptions and consequences for value, conversion, margins and cash. | Calculations must be reproducible; publishing prices or changing billing requires separate approval and execution. |
| O06 | money model | How value exchange, payer, revenue mechanism and timing connect to cost, retention and delivery. | This is not bookkeeping, payment processing, tax advice or a promise that revenue expansion is beneficial. |
| O07 | acquisition system | Channel choices, qualification, demand-generation logic and evaluation against downstream outcomes. | No fabricated audience/CAC evidence; operators own live outreach, ad accounts and analytics collection. |
| O08 | sales path | The commercial path from a qualified prospect to a suitable purchase, including fit and evidence requirements. | Salespeople and authorised systems own conversations, contacts and CRM mutations; no autonomous commitments. |
| O09 | delivery/economic model | The connection between promised value, fulfilment capacity, costs, retention and cash obligations. | Deterministic systems calculate; accountable operators validate capacity and perform delivery; no accounting certification. |
| O10 | business experiments | A proposed test of a decision-relevant assumption and interpretation of its observed result. | Human approval precedes external effects; collection/assignment tools supply observations; synthetic data never becomes customer evidence. |
| O11 | constraint diagnosis | An evidence-qualified account of the binding failure layer and the smallest justified correction. | Competing explanations and unknowns remain visible; preserve accepted decisions unless evidence implicates them. |
| O12 | business-model review | A coherent review across customer, offer, growth, delivery, retention, economics, cash, evidence and risk. | Separate dimensions rather than a universal score; accountable humans decide commitments and specialists retain their conclusions. |

## 5. User model

This is an intended-use model, not completed user discovery. It admits solo operators and teams without assuming company size determines business-model structure. It does not authorise work on the user's own business, accounts or customers. (§8 intended users and approval points.)

| Intended role | Decisions or contribution | Necessary input | Authority boundary |
|---|---|---|---|
| Founder, owner or accountable business lead | Frame a new venture, choose commercial options, review an existing business and approve changes. | Objectives, constraints, current obligations, available evidence and decision authority. | Owns business risk and commitments; the agent does not acquire this authority by drafting a recommendation. |
| Product, marketing, sales, customer-success or operations contributor | Bring evidence from an owned function, diagnose a bounded problem and propose a correction. | Actual observations, definitions, time windows and dependencies on other functions. | May propose within a role; cross-functional or financial commitments require the designated owner. |
| Consultant or adviser supporting a business | Structure analysis, compare options and prepare an evidence-backed recommendation. | Agreed brief, permitted data access and an identified client decision-maker. | Advisory work is not authority to bind the client or claim unperformed specialist review. |
| AI agent using the installed capabilities | Organise facts and assumptions, request evidence, draft business artefacts and evaluate bounded changes. | User instructions, accepted decisions, evidence and applicable constraints. | Must stop at missing approval, unresolved material facts or specialist questions; must not manufacture customer observations. |
| Specialist reviewer | Supply research, legal, tax/accounting, finance or production findings within the reviewer's remit. | A bounded question and enough source material to answer it. | Specialist conclusions remain attributed; business reasoning does not rewrite them for better conversion. |
| Execution operator | Perform approved campaigns, CRM actions, pricing changes, delivery or measurement through the appropriate systems. | A specific authorised action, constraints and required return evidence. | Execution state and access permissions belong to the operator/tool, not to a business-reasoning artefact. |

The customer of a target business is not automatically the user of these skills. Buyer, user and payer distinctions in a business model must not be confused with the operator, approver or specialist roles above. Where authority or required facts are missing, ask the accountable human; do not infer permission from job titles.

## 6. Professional and execution boundaries

The ten distinctions explicitly required by Stage 1 are resolved below. These are project responsibility allocations under the bootstrap contract, not claims about the current implementation of neighbouring repositories. Formal cross-project comparison belongs to Stage 20. (§§2, 8, 27.)

| ID | Neighbouring responsibility | Business Building may do | Other owner and handoff | Must not do |
|---|---|---|---|---|
| B01 | market/deep research | Frame evidence questions, identify decision-relevant uncertainty and interpret returned evidence in context. | Deep Research Skills or a researcher gathers/verifies external market and customer evidence, with sources and limitations. | Invent market size, customer demand, competitors or interview findings; portray business synthesis as primary research. |
| B02 | legal advice | Identify issues, capture facts and business intention, request review and revise choices within returned constraints. | Legal Skills owns legal research/conclusions; qualified counsel handles advice or approval where needed. | Determine legality or draft a legal conclusion as if professionally reviewed. |
| B03 | accounting / tax | Define business assumptions and request cost, cash and tax inputs needed for commercial analysis. | Accounting systems and accountants own records/treatment; qualified tax advisers own tax conclusions and filings. | Rebuild accounting, certify statements, infer tax obligations or choose tax treatment. |
| B04 | investment advice | Describe the business's operational economics and identify where a question is investment-related. | An appropriately qualified professional owns investment recommendations and regulated questions. | Recommend securities, allocations or financial products; promise investment returns or treat business analysis as investment suitability. |
| B05 | financial planning | Analyse the venture's operating scenarios and cash constraints without presenting them as a person's financial plan. | The business owner and appropriately qualified financial professionals handle personal planning, borrowing/suitability and related regulated questions. | Produce personal retirement, insurance, borrowing or wealth-planning advice under a business-skills label. |
| B06 | software/product implementation | Supply customer/value requirements, acceptance intentions and commercial constraints. | Software Engineering and UI/UX Design Skills, or delivery teams, build/test the product and return delivery evidence. | Treat a business brief as implemented software or dictate an unsupported technical architecture. |
| B07 | brand/creative production | Set audience, offer, proof requirements and truthful commercial-message constraints. | Appropriate design, narrative, video, audio or other production disciplines create and review assets. | Replace creative production, fabricate testimonials or let an attractive asset count as market validation. |
| B08 | sales CRM execution | Define qualification, stages, evidence needs and authorised action requirements. | Sales operators and CRM tools own contact records, pipeline state, calls and authorised changes. | Become a CRM, silently alter records, contact prospects or negotiate binding terms. |
| B09 | paid-ad platform operation | Recommend a channel hypothesis, bounded experiment, stop criteria and approved-spend request. | Authorised marketers and ad platforms own buying, targeting, delivery, spend and measurement configuration. | Launch or scale campaigns, acquire audiences or spend money because a plan exists. |
| B10 | Pactwright lifecycle governance | Provide business requirements, proposed experiments, constraints and evaluation evidence. | Pactwright may govern authorised Contracts, Evidence and lifecycle state where adopted. | Own Pactwright state, require Pactwright at runtime or let lifecycle status determine business-model truth. |

Operations is an additional explicit scope boundary: the skills assess delivery promises and diagnose constraints; they do not fulfil orders, hire staff, procure inventory, run support desks, collect payments or own those systems of record. Revenue/cost/cash calculations belong to deterministic tools whose inputs and outputs can be inspected. No provider or tool has been selected in this stage. (§§5, 8; detailed models/tool choice assigned to §§14, 17–18.)

## 7. Quality dimensions and human/legal handoffs

### Quality dimensions

Retain all sixteen dimensions named in §5 separately. They describe what later decisions and evaluations must examine, not a benchmark executed here or universal numeric thresholds. Evidence provenance, assumptions and uncertainty apply to every dimension. A missing measure must remain unknown rather than receiving an invented favourable score.

| ID | Dimension | Question the business artefact must support | Unacceptable shortcut |
|---|---|---|---|
| Q01 | customer evidence | What was observed, from whom, when, and how relevant is it to this customer claim? | Treating a declared segment or AI-generated persona as observed demand. |
| Q02 | problem importance | What supports the claim that this problem matters relative to alternatives? | Improving an offer around an unexamined problem. |
| Q03 | offer strength | Is the promised outcome clear, supported and deliverable within scope? | Adding bonuses or guarantees while ignoring feasibility. |
| Q04 | differentiation | Which relevant alternative is being compared, and on what evidence? | Unsupported superiority or misleading comparisons. |
| Q05 | trust / credibility | Can proof, claims and material terms be traced and understood? | Fabricated social proof, urgency or hidden obligations. |
| Q06 | pricing fit | Is the pricing structure coherent with value, payer, delivery costs and payment timing? | Treating conversion alone as pricing quality. |
| Q07 | acquisition efficiency | Do prospects fit and produce worthwhile downstream outcomes relative to acquisition and sales effort? | Counting leads without qualification, retention or economics. |
| Q08 | conversion quality | Are appropriate customers buying through a truthful, workable sales path? | Conversion achieved through deceptive friction or concealed terms. |
| Q09 | retention / expansion | Is continued purchase or expansion supported by continued delivered value? | Assuming repeat revenue without retention evidence. |
| Q10 | delivery quality | Can the business fulfil what was sold at the promised quality and time? | Treating a successful sale as evidence of successful delivery. |
| Q11 | unit economics | Are costs, margins, acquisition and retention assumptions, units and periods explicit? | Calling revenue profit or trusting unexplained LTV/CAC. |
| Q12 | cash robustness | Can obligations be met when due under the stated growth and payment assumptions? | Inferring cash sufficiency from an accounting margin. |
| Q13 | operational capacity | Can sales, onboarding, fulfilment and support absorb the proposed demand? | Scaling a channel into an unexamined capacity failure. |
| Q14 | legal / ethical risk | Are relevant issues surfaced, constraints respected and necessary reviews complete? | Treating increased conversion as evidence of acceptability. |
| Q15 | experiment quality | Can an adequately designed, honest test falsify the assumption and change the decision? | Interpreting every result as success. |
| Q16 | learning velocity | Is uncertainty actually reduced and does evidence inform a bounded next decision? | Equating activity count with validated learning. |

The fifteen governing principles in §5 are retained by the charter's full-system scope, the outcome/boundary maps, these dimensions and the approval rules below. In particular, evidence precedes scale; the current constraint precedes redesign; validated choices are preserved; and the smallest responsible correction is preferred. No single dimension overrides truthfulness, legal constraints, deliverability or missing authority.

### Human approval points

Routine organisation of supplied evidence, transparent scenario analysis and drafting recommendations may occur within the user's brief. The following are commitment boundaries, not routine drafting permissions. (§§5, 8.)

| Approval point | Human decision required | Required evidence or clearance before action |
|---|---|---|
| Accept or materially change the business direction | Approve target customer, offer, pricing, business model or changes to previously accepted choices. | Decision rationale, affected dependencies, actual supporting evidence and uncertainty; review downstream effects of a target-customer change. |
| Publish customer-facing claims or commercial terms | Approve promises, prices, discounts, guarantees, refunds, renewals, urgency and comparisons. | Substantiation, delivery/economic feasibility, material terms and legal review when needed. |
| Spend, scale or take on obligations | Approve ad spend, inventory, staffing, contracts, pricing/billing changes or other commitments. | Stated scope, budget/capacity, stop conditions, material assumption checks and cash consequences. |
| Run an external experiment or contact people | Approve the test, participants, outreach and permissible data use. | Honest description of what exists, lawful/ethical constraints, measurement plan and relevant specialist clearance. |
| Access or mutate live business systems | Authorise the specific records, accounts and operations. | Appropriate permissions, permitted purpose and clear requested actions; tool availability is not permission. |
| Rely on a specialist conclusion | Obtain the relevant qualified review and decide the business response. | Attributed conclusion, jurisdiction/context where applicable, limitations and unresolved questions; approval cannot convert unknown legal facts into clearance. |
| Treat a result as accepted business evidence | Approve the interpretation and resulting commitment within the assigned authority. | Actual observations separated from assumptions, metric definitions, caveats and confidence; inconclusive stays inconclusive. |

### Human/legal handoff

At a professional boundary, identify the issue; preserve the relevant facts; state the intended business decision; distinguish assumptions and missing evidence; formulate the bounded question; identify the appropriate reviewer and accountable approver; receive the attributed result and limitations; then revise the affected business choice within the returned constraints. If a required conclusion or authorisation is missing, stop and ask before continuing the affected business task. During this bootstrap, any required user input stops the entire process under the execution contract. Do not convert silence into approval. This defines the boundary; Stage 9 owns researched legal-handoff design and adversarial evaluations. (§§5, 8, 16.)

The legal/tax risk surfaces expressly listed in §5 remain in scope for identification and routing: consumer protection; advertising claims; privacy / direct marketing; email / SMS consent; subscription cancellation; refund promises; guarantees; competition law; financial promotions; earnings / ROI claims; testimonials / endorsements; pricing presentation; automatic renewal; children / vulnerable users; employment / contractor classification; tax and regulated activity. No jurisdiction-specific legal conclusion is made here.

Specialist legal constraints cannot be traded away for revenue or conversion. The same distinction applies to accounting, tax, investment and personal financial-planning boundaries. A business recommendation records the constraint it consumed; it does not claim the specialist's work as its own. If no specialist integration is installed, a human handoff remains valid; missing substantive review does not.

## 8. Non-goals

The initial sixteen non-goals in §35 remain explicit exclusions. The qualifications below describe their boundary; they do not silently make any exclusion an optional feature.

| ID | Exclusion | Boundary |
|---|---|---|
| N01 | a replacement for the five source books | Use independently expressed capabilities; do not republish books or offer the repository as their substitute. |
| N02 | a business-book summarisation repository | Book evidence is an input, not the repository's output architecture. |
| N03 | a universal entrepreneurship doctrine | Context and observed evidence may challenge any source-derived heuristic. |
| N04 | a CRM | CRM state and operations stay in dedicated systems. |
| N05 | a marketing automation platform | Define business intentions and constraints, not an automation platform. |
| N06 | an ad-buying platform | Campaign operation and spend remain external and authorised. |
| N07 | an accounting package | Business reasoning does not own ledgers, accounting treatment or statutory records. |
| N08 | a payment processor | Payment execution and billing systems are external. |
| N09 | a sales-dialler or spam system | No autonomous contact engine or consent-violating growth mechanism. |
| N10 | an investment-advice system | Operational business economics is not investment recommendation or suitability. |
| N11 | a tax-advice system | Surface questions and consume qualified answers; do not determine tax treatment. |
| N12 | a legal-advice system | Identify and route issues; legal conclusions belong to the legal discipline. |
| N13 | a market-data vendor | Use traceable evidence rather than fabricating or maintaining a universal market feed. |
| N14 | a universal business ontology | Define only business representations justified by the workflow in their owning stages. |
| N15 | a one-number startup score | Preserve separate quality dimensions and uncertainty. |
| N16 | an autonomous executive team | Do not replace human business authority with role-named agents. |

Software/product implementation, creative production, personal financial planning, operational fulfilment and Pactwright governance are also outside the owned discipline as resolved in §6. The central Production Skills project retains family contracts, registry/maturity and genuinely shared abstractions. No shared abstraction is extracted here, no other repository is modified, and no maturity promotion follows from this domain charter. (§§2, 8, 32–35.)

## 9. Alternatives considered and rejected

| Alternative | Decision and reason | Source requirement |
|---|---|---|
| Book-shaped skills or five parallel playbooks | Reject. Capability ownership must remain independently expressed and reconcile source overlap. | §§3–4, 8 exit |
| Marketing-first scope focused on offers and leads | Reject. It would omit delivery, retention, economics, cash and learning from business viability. | §§1, 5, 8 |
| Greenfield-only or B2B-only product | Reject. Both lifecycle starting points and both customer settings are explicit scope questions and can be covered without inventing a narrower market. | §8 |
| Full-stack business operating platform | Reject. It would absorb CRM, ads, accounting, payments, production execution and human authority. | §§2, 8, 35 |
| Advisory scope so narrow that it excludes tactics | Reject. Bounded commercial recommendations, briefs and experiments belong to business reasoning; the boundary is authorised execution, not an inability to reason about concrete actions. | §§5, 8 |
| Domain charter as proof of commercial effectiveness | Reject. Contract-derived scope decisions are not empirical findings; broader research has an explicit owning stage. | §§1, 9–10, 34 |
| Immediate formal schemas, commands, packs or production folders | Reject for Stage 1. Those are separately assigned design and implementation tasks, not prerequisites for defining the domain. | §§11–33 |

## 10. Verification, unresolved questions and handoff

Verification is recorded in [Stage 1 conformance](2026-09-09-stage-01-conformance.md). It includes direct review against original §8, enumerated coverage, all six output categories, global-constraint review, provenance checks, relative-link checks and repository-tree checks. Automated presence checks supplement semantic review; they do not establish sound business judgement or legal correctness.

No unresolved user decision is needed to define this domain within the supplied contract. No live business action, external data access, jurisdiction choice, spending, release, PR readiness or registry promotion has been assumed. The failed shell clone is recorded, not reported as a successful checkout. The connected API supplies the repository operations required for this stage.

**Exit explanation:** Business building connects customer evidence, value, offer, price, acquisition, sales, delivery, retention and economic/cash constraints; tests decision-relevant uncertainty; and preserves validated choices while correcting the responsible failure layer. This explanation is independent of any one book. It is a scope resolution, not a tested claim of business success.

**Inputs for Stage 2:** this domain charter, the responsibility/user/quality/handoff maps, the explicit exclusions, the verified acceptance/provenance record and the original source-to-capability hypothesis in the governing specification. Stage 2 must access adequate source material for all five books, distinguish actual source support from interpretation, extract all required fields, compare tensions and record a capability-based synthesis. Stage 1 has not extracted or validated book contents. If mandatory source evidence is unavailable, Stage 2 must stop and ask under the execution contract rather than substitute imagined contents or a representative sample.

Only a verified Stage 1 completion recorded in [bootstrap progress](bootstrap-2-progress.md) permits starting Stage 2. All later work listed in the acceptance checklist remains outside this stage; none is claimed complete.
