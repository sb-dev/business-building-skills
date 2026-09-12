# Business Building Skills — System Specification

**Contract version:** 1.0 · 12 September 2026  
**State:** Complete canonical specification; implementation and installed validation are separate gates.  
**Authority:** [Bootstrap §25](research-logs/2026-09-08-business-building-skills-new-project-bootstrap-process.md#25-stage-18--generate-six-canonical-specifications), accepted research through Stage 17 at `ff97f73866012b296bc4a142e0de6258a7906c94`.  
**Specification set:** [01](01-business-building-skills-system-spec.md) · [02](02-business-building-skills-workflows-and-artifacts-spec.md) · [03](03-business-building-skills-repository-and-contracts-spec.md) · [04](04-testing-and-benchmark-spec.md) · [05](05-business-building-customisation-packs-spec.md) · [06](06-business-building-extension-pack-catalogue.md)

Owns mission, scope, source-book treatment, governing principles, architecture, skill boundaries, execution and professional boundaries, build order and system acceptance. The other five specifications implement these obligations without becoming alternative owners of business truth.

“Must” states a requirement; “may” permits a bounded option. Examples and authored controls remain synthetic. A specification, complete record or passing calculation does not establish customer validation, installed behaviour, professional clearance or permission for an external action. Earlier research dates, source IDs and stage references record provenance; the ownership table in specification 01 identifies the current normative document. Where an incorporated record names an earlier stage, implement its completed contract in this specification set, not a missing future design.

## 1. Mission and scope

Turn uncertain customer and economic assumptions into coherent, evidence-backed business choices, test the riskiest dependencies at adequate cost, and improve the current constraint while preserving supported decisions. The result is a bounded decision and its business artefacts, not a guarantee of revenue, market fit or business success.

Support greenfield opportunities and existing businesses, consumer and B2B exchanges, solo operators and teams. Begin from the accountable owner's actual objective; a sufficient sustainable business is not required to maximise growth. Distinguish the skill operator, business owner, specialist reviewer and execution operator from the target business's customers, users and payers. For existing work inspect accepted versions and outstanding promises before proposing changes. For greenfield work preserve unknowns and hypotheses.

The lifecycle connects customer/problem, alternatives/value, offer, pricing and monetisation, acquisition/qualification, sales, delivery/onboarding, retention/expansion/referral, economics/cash, assumptions, experiments, learning and diagnosis/repair. Evidence, customer rights, economics and capacity constrain every step; they are not postponed until after a sale.

## 2. Document ownership and conflict handling

| Specification | Owns | Uses from other specifications |
|---|---|---|
| 01 System | Discipline, invariants, skills, professional boundary, build order and overall acceptance | Detailed records, distribution and evaluation evidence |
| 02 Workflows and Artifacts | Business record meanings, decision procedures, calculations, growth gates and handoffs | Skill mutation contracts in 03; evaluation method in 04 |
| 03 Repository and Contracts | Actual distribution design, SKILL.md and all 32 command contracts, local resources, installation and CI | Domain meanings in 02; test gates in 04; pack contents in 05 |
| 04 Testing and Benchmark | Cases, rubrics, real run evidence, regressions and product/release gates | Record semantics in 02, technical contracts in 03, effects in 05–06 |
| 05 Customisation / Extension Packs | Qualification, selection, precedence, effect contracts, authoring and packaging content | Core command names in 03; evaluation execution in 04; candidates in 06 |
| 06 Extension Pack Catalogue | The eight independent candidates, advisory mode, complete profiles, concrete prompts and effect-specific evaluations | Pack contract in 05 and actual evidence gates in 04 |

A local file, pack default or operator dashboard cannot override a mandatory domain invariant. Resolve a document defect at its owning specification and trace every affected command, fixture and installed resource. During this bootstrap, a contradiction requiring a change to accepted Stages 1–15 needs the user's decision under the continuation contract. Do not silently alter those sources. After a compatible correction, version the changed contract and rerun affected checks; retain unaffected accepted decisions and evidence.

## 3. Book-evidence relationship

The five books supply an initial capability corpus, not five skills or a compulsory business doctrine. Their exact supplied editions and input identities are recorded below. The original PDFs and extracted copyrighted text are not distributed. This stage consumes the persisted extraction and independent research; it does not claim to have reopened those PDFs.

| ID | Source and supplied edition | Supplied filename | PDF pages | SHA-256 |
|---|---|---|---:|---|
| O | Alex Hormozi, *$100M Offers: How to Make Offers So Good People Feel Stupid Saying No*, 2021 | `100_million_offer_-_Alex_Hormozi.pdf` | 206 | `296801add91e0e578bf4d65f9829eea743868d99667f05cc56b2319c675a2b42` |
| L | Alex Hormozi, *$100M Leads: How to Get Strangers To Want To Buy Your Stuff*, 2023 | `100m_leads_-_Alex_Hormozi.pdf` | 391 | `e69667ec6bffe4806e3f5907394803cd3d36f3485b0ca201378b4879f7b9450e` |
| M | Alex Hormozi, *$100M Money Models: How To Make Money*, 2025 | `100M_Money_Models_How_To_Make_Money_-_Alex_Hormozi.pdf` | 188 | `86eb74efb95c35db341b0d92a9d835f1ec48650980bd82835624deb261fc5333` |
| P | Josh Kaufman, *The Personal MBA: Master the Art of Business*, revised tenth-anniversary edition, 2020 | `The_Personal_MBA_-_Josh_Kaufman.pdf` | 496 | `1a41fd73ef09bd44a931dbcbf985c9c42d0fa274ccc7b6ed246cfbad0a2f7e2b` |
| R | Eric Ries, *The Lean Startup: How Today's Entrepreneurs Use Continuous Innovation to Create Radically Successful Businesses*, first edition, 2011 | `The_Lean_Startup__How_Todays_Entrepreneur_-_Eric_Ries.pdf` | 247 | `aaf5c67cf1f268fcbc16d59fdeecabebda12e98ba5e16316c4bd88174e85bb80` |

The trace is source idea → reusable capability → production responsibility → command/workflow → evaluation criterion → case. Preserve attribution and reading limits. Independently express methods; do not republish substantial passages, chapter structures, proprietary examples or branded terminology merely for familiarity. Several books sharing an author or lineage are not independent replications. Arithmetic can establish a calculation without proving the forecast or method's commercial efficacy.

Reconcile competing recommendations using customer context, independent professional/empirical evidence, actual constraints and the decision consequence. Offer ambition cannot replace adequate experiments; lead volume cannot outrank qualified downstream value; added revenue cannot excuse lost rights, weak retention or unfunded obligations. Neither premium-first nor discount-first is a universal rule. A short recovery target supplies no automatic credit facility. Preserve a target while evidence supports it, and allow a justified coordinated change when evidence implicates the fundamental dependency.

The source matrix and conflict log remain the complete lineage record: [source-to-capability matrix](research-logs/2026-09-09-stage-02-source-to-capability-matrix.md), [reconciliation](research-logs/2026-09-09-stage-02-reconciliation-and-taxonomy.md), [independent evidence hierarchy](research-logs/2026-09-10-stage-03-evidence-and-terminology.md).

## 4. Capability architecture

| ID | Capability | Production responsibility and workflow implication | Decision artefact | Evaluation criterion |
|---|---|---|---|---|
| C01 | Opportunity and market framing | Distinguish a customer/market hypothesis from an operating fact and discovery from execution. | Bounded opportunity with conditions and unknowns | Material market assumptions and alternatives are visible; no universal opportunity score |
| C02 | Customer and problem evidence | Establish whose problem matters, who buys/uses and what was actually observed. | Customer/problem account with provenance | Declared segment, observed customer and unsuitable prospect remain distinct |
| C03 | Value and alternatives | Relate desired progress, confidence, effort and delay to actual alternatives. | Value hypothesis and obstacle map | Claims trace to evidence or remain hypotheses; perception is not delivered value |
| C04 | Offer construction and obligations | Connect scope, components, deliverability, proof and remedies. | Coherent offer hypothesis | Every promise and added component has purpose, cost, scope and approval needs |
| C05 | Pricing and packaging | Compare price structure and real options under customer and economic constraints. | Price/packaging options | Total price and material terms are explicit; willingness to pay is not invented |
| C06 | Revenue and offer sequencing | Explain who pays, for what, when and why an additional offer belongs. | Revenue-sequence hypothesis | Each step creates value and has economic justification; four offer types are not mandatory |
| C07 | Channel fit and bounded growth | Choose reach mechanisms appropriate to the audience and assess incremental expansion. | Channel hypothesis and scale/repair decision | Downstream economics, cash and capacity constrain volume |
| C08 | Engagement and qualification | Distinguish contact, interest, suitability and progression through a commercial path. | Qualification and engagement model | A useful magnet or contactable lead is not automatically a customer or permission |
| C09 | Truthful communication and proof | Turn approved commercial facts into clear message requirements and flag unsupported claims. | Substantiated message/proof brief | No fabricated scarcity, anchors, testimonials or late material disclosure |
| C10 | Sales path and conversion | Match buyer needs, alternatives, scope and acceptance to an appropriate buying process. | Commercial-path diagnosis or option brief | Suitable informed agreement is distinct from a forced yes; execution authority is external |
| C11 | Delivery, capacity and quality | Connect promises to repeatable work, human limits, costs and learning time. | Delivery/capacity assessment | Actual fulfilment, workload and quality can support proposed demand |
| C12 | Retention, repeat and renewal | Separate continued value and voluntary repeat purchase from continued billing. | Retention/renewal hypothesis | Matched cohorts, value delivery and exit behaviour are visible |
| C13 | Expansion and complements | Offer additional scope only for a genuine customer need with explicit acceptance. | Incremental-value expansion proposal | Additional contribution, obligations and customer choice are assessed |
| C14 | Referrals and partnerships | Connect delivered value, incentives, partner fit and propagation mechanisms. | Referral/partner hypothesis | Suitable incremental customers, costs and counterparties are identified |
| C15 | Unit economics and metric meaning | Define costs, margins, lifetime value and acquisition cost before interpreting them. | Reproducible economics assessment | Units, period, cost basis and assumptions agree; arithmetic passes |
| C16 | Cash timing and exposure | Assess when usable cash arrives relative to commitments, refunds and future delivery. | Cash/payback scenario | Commitments and receivables are not cash; nominal profitability cannot override a cash gap |
| C17 | Assumption identification | Surface the conditions on which value, demand, delivery and economics depend. | Decision-relevant assumption questions | Observation, belief, consequence and uncertainty stay separate |
| C18 | Experiment design | Start from a decision, choose adequate evidence, then minimise necessary effort. | Bounded experiment proposal | Results can change the decision; test fidelity, truthfulness and interpretation limits are explicit |
| C19 | Measurement and learning | Connect exposure and observations to interpretable, auditable learning. | Learning/evidence record | Denominators, cohorts, uncertainty and source records support the conclusion |
| C20 | Constraint diagnosis and repair | Locate the responsible failure layer and choose no change, local correction or justified pivot. | Bounded change rationale | Evidence implicates changed decisions; unaffected accepted decisions are preserved |
| C21 | Business-system review and resilience | Judge coherence against actual owner objectives and plausible failure conditions. | Multidimensional business review | No single score or growth target replaces value, economics, cash and constraints |
| C22 | Human and specialist handoffs | Keep recommendations distinct from authorised execution and professional conclusions. | Bounded handoff with questions, facts and return evidence | Owner authority, operator roles and legal/accounting boundaries remain explicit |

Use one ordinary business dossier with fifteen linked concerns, not a universal graph or customer database. A small case keeps records inline; split only when ownership or review benefits. Stable local IDs refer to claims, observations, decisions, calculations and obligations. Preserve unit, period, source and authority across handoffs. A material target change triggers downstream review; review does not regenerate every artefact.

## 5. Governing principles

### Evidence before scale

Do not scale acquisition, hiring, inventory, infrastructure or paid media while critical assumptions remain untested or unit economics are structurally unknown.

### Customer reality before offer optimisation

Do not optimise copy, bonuses, guarantees or urgency around a problem the target customer does not materially care about.

### Offer strength is not permission to mislead

An offer may reduce buyer risk, improve clarity and increase perceived value, but must not depend on:

```text
false scarcity
fabricated urgency
unsupported guarantees
misleading comparisons
invented testimonials
hidden material terms
deceptive price anchoring
dark patterns
spam or consent violations
```

Truthfulness and enforceable obligations are part of business quality.

### Business model before isolated tactic

A lead tactic, pricing trick or landing-page improvement is useful only inside a coherent system:

```text
customer
→ value
→ acquisition
→ conversion
→ delivery
→ economics
→ retention / referral
```

### Cheapest adequate experiment

Use the cheapest experiment capable of reducing the current uncertainty.

Examples:

```text
customer interviews before paid acquisition
manual service before automation
landing-page interest test before full build
concierge delivery before platform build
small price test before pricing-system redesign
single-channel test before multichannel expansion
manual sales call before complex sales automation
```

Experiments must be honest about what exists and must not deceive participants about material facts.

### Assumption, observation and conclusion remain separate

Preserve:

```text
assumption
observed evidence
metric
interpretation
decision
confidence
```

Do not convert a plausible hypothesis into a fact because an AI generated it.

### Revenue is not economics

Evaluate revenue together with relevant costs, margins, churn/retention, refunds, delivery capacity, working capital, acquisition cost, payback and cash timing.

### Growth is constrained by the weakest binding system

A business may be constrained by:

```text
demand
lead quality
conversion
price
retention
delivery capacity
gross margin
cash
sales capacity
fulfilment quality
onboarding
product value
trust
```

Diagnose the current constraint before redesigning the entire business.

### Acquisition quality matters more than raw lead volume

Measure whether acquired prospects fit the target customer and progress through the intended commercial path.

### Retention changes acquisition economics

Customer acquisition and monetisation cannot be evaluated independently of continued value delivery where the business depends on repeat purchase, subscription, expansion or referral.

### Cash timing is a first-class constraint

A profitable model can still fail if cash arrives after obligations become due.

Research working capital, payment terms, refunds, inventory, fulfilment timing and customer acquisition payback where relevant.

### Preserve validated business decisions

An accepted target segment, proven channel, working offer, profitable pricing structure or validated onboarding step should not be casually rewritten when a different layer fails.

### Correct the smallest responsible layer

Examples:

```text
low qualified traffic
→ acquisition / channel

high traffic but weak conversion
→ offer / trust / sales path

strong conversion but weak contribution margin
→ price / cost / fulfilment model

good first purchase but poor retention
→ delivered value / onboarding / retention system

good economics but capacity failure
→ operations / delivery system

good demand and margin but cash crisis
→ payment timing / working capital / growth pace

experiment inconclusive
→ experiment design / measurement
```

### Business quality is multidimensional

Do not collapse business quality into one score.

Keep dimensions such as:

```text
customer evidence
problem importance
offer strength
differentiation
trust / credibility
pricing fit
acquisition efficiency
conversion quality
retention / expansion
delivery quality
unit economics
cash robustness
operational capacity
legal / ethical risk
experiment quality
learning velocity
```

separate where useful.

### Legal and ethical constraints are production inputs

Business Building Skills should identify issues and route them to Legal Skills or qualified counsel where needed.

Relevant surfaces include:

```text
consumer protection
advertising claims
privacy / direct marketing
email / SMS consent
subscription cancellation
refund promises
guarantees
competition law
financial promotions
earnings / ROI claims
testimonials / endorsements
pricing presentation
automatic renewal
children / vulnerable users
employment / contractor classification
tax and regulated activity
```

The business workflow should never optimise around illegal or deceptive behaviour.

## 6. Four core skills

| Skill | Primary responsibility and NC trace | Use when | Do not activate merely because |
|---|---|---|---|
| `business-build` | Construct or revise bounded business choices; NC01, NC02, NC04, NC05, with NC07 safeguards. | The task asks for opportunity/customer/value/offer/pricing/delivery/economic models, assumptions, an experiment plan or a learning record. | An existing artefact needs assessment only, a live campaign needs sending, or software needs implementation. |
| `business-grow` | Improve qualified demand, sales, retained value and bounded scale; NC03, constrained by NC04/NC07. | The task concerns an accepted or explicitly hypothetical commercial system's channels, sales path, retention, expansion or scale decision. | Raw lead volume rose, a user asks to send messages, or the customer/offer baseline may be silently replaced. |
| `business-evaluate` | Assess evidence, coherence and constraints without changing the subject; NC04, NC06, NC07 and review of NC01–NC05 outputs. | The task asks for an audit, judgement, diagnosis or smallest-change recommendation on supplied business evidence or artefacts. | The reviewer wants to repair the source automatically, generate favourable proof, or confer legal approval. |
| `business-pack-author` | Research, qualify, author and validate reusable business-model specialisations; NC08 with NC07 safeguards. | The task explicitly concerns a reusable pack, its changed core behaviour, showcase, evaluations or catalogue entry. | The project belongs to an industry/location, or an ordinary business task could be completed with existing core behaviour. |

The selected logical command distribution is **10 build / 8 grow / 7 evaluate / 7 pack-author = 32**. Specification 03 defines every command's nine fields and explicit modes. Logical selectors are requests, not executable or universal slash commands. Route by the requested output. A focused experiment or model task can use business-build without reconstructing the entire business; evaluation remains a separate read-only subject assessment. Mixed work keeps each mutation boundary distinct.

Each skill performs its own relevant evidence, rights, arithmetic, economics, cash and capacity self-checks. No sibling evaluator or pack is required to make a skill responsible. Composition exchanges artefacts; it does not transfer approval or create an autonomous executive team. Separate business-model and business-experiment packages were examined and rejected as overlapping the selected focused paths; reopen only for demonstrated independent installation needs.

## 7. Execution boundary

Document-led reasoning is the chosen execution layer. Business Building owns commercial choices and interpretation; existing systems or authorised operators own arithmetic, spreadsheet recalculation, CRM state, email, advertising, analytics, billing, accounting, survey collection, A/B assignment and warehouses. Choose an adequate incumbent system or read-only export for the actual task. No compulsory SaaS stack, cloud account, MCP server or Pactwright runtime is required.

Use a deterministic calculator for calculations; the accepted conditional choice for small exact money scenarios is an available Python Decimal implementation. A workbook needs an actual calculation engine, not just a library that writes formulas. Statistical inference requires a suitable verified design and established method. Tool absence may block the affected evidence claim; it cannot justify invented observations. Specification 03 defines exact H01–H08 binding, result and retry responsibilities.

Other Production Skills can create research, software, design, content or other delivery artefacts. Business Building supplies a bounded question, commercial requirement or experiment and consumes attributable returned evidence. Pactwright may govern authorised delivery Contracts and Evidence, but does not own business truth; Business Building does not own its lifecycle state. The central Production Skills repository owns family contracts, registry/maturity and abstractions demonstrated across independent domains. Cross-project compatibility is reviewed in Stage 20 and tested only where implemented.

## 8. Legal and ethical boundary

Judge truthfulness, applicable professional constraints and action authority separately. Known false scarcity, fabricated urgency, invented testimonials, unsupported outcome claims, fake guarantees, hidden prices or renewals, obstructed cancellation and spam fail the affected proposal. Improved conversion cannot offset them. A disclaimer cannot cure a contradicted headline or actual refund refusal. Preserve legitimate existing rights during repair.

Business Building identifies issues and prepares the HF01–HF07 packet in specification 02. Legal Skills or qualified reviewers own legal research and conclusions; accounting/tax and regulated specialists keep their own remit. Retain reviewed facts, jurisdiction, source status, effective date, conditions and review trigger. A historical research finding or provider policy is not current global clearance. Verify material applicability before relying on it; unresolved required findings block the affected commitment. A valid existing reviewed policy can cover routine work without an invented new opinion on every repetition.

Drafting, reading and local calculation within the user's authorised task can proceed. Sending, spending, charging, publishing, changing customer records/terms, hiring or making other external commitments requires its actual authority. Existing valid authority remains usable; a command name, credential, generated consent record, installed skill or approval of a draft does not enlarge it. Preserve source data in its authorised custody and publish only original synthetic or specifically approved/redacted evidence.

## 9. Build order and maturity

| Stage | Required result before advancing |
|---|---|
| 18 | Six complete canonical specs from accepted logs, conformance and remotely verified scoped commit/receipt |
| 19 | Complete public README design with honest installation/implementation status and all fifteen examples |
| 20 | Actual cross-project comparison and bounded integration opportunities; no premature shared runtime |
| 21 | Justified production scaffold; licence and contribution policy have actual authority; no empty speculative platforms |
| 22 | Installed skills complete one bounded idea-to-evidence-to-repair vertical with captured outputs and actual calculations |
| 23 | Implement and demonstrate all fifteen selected examples and representative packs; every implemented pack has actual paired and create/revise evidence |
| 24 | Source and distinct clean external/selective installation, command discovery, local resources and reproduction actually pass |
| 25 | Optional thin Pactwright composition remains independent; any authorised registry change matches demonstrated evidence |
| 26 | Shared abstractions reviewed only against repeated independent production needs; retain local mechanisms when evidence is insufficient |
| Final audit | All Stages 0–26 and global gates checked together; zero unresolved mandatory failures before PR readiness |

The maturity sequence is proposed → researching → specified → scaffolded → working → benchmarked → mature. These words require their actual evidence and any required publication authority. This specification set does not promote a registry, publish a release, raise a ready PR, or establish working/benchmarked/mature product behaviour. Individual stages are completed sequentially under the execution contract.

## 10. System acceptance

Before maturity, demonstrate:

### Source integrity

- the five books are traceable as source evidence;
- skills are capability-shaped rather than book-shaped;
- copyrighted text/examples are not substantially reproduced;
- conflicting book recommendations are resolved through broader research and context.

### Customer and value

- customer/problem claims distinguish evidence from assumption;
- external market facts are verified where material;
- value propositions connect to actual customer evidence;
- target-customer changes trigger appropriate downstream review.

### Offer and pricing

- offers are deliverable;
- pricing and payment structures are explicit;
- guarantees/refunds match actual capability and terms;
- scarcity/urgency is truthful;
- economic consequences are considered;
- stronger conversion does not excuse misleading design.

### Acquisition and sales

- lead quality is separate from lead volume;
- channel selection reflects customer/business model;
- acquisition is judged using downstream conversion/retention/economics;
- spam/deceptive tactics fail evaluation;
- sales path and delivery capacity are compatible.

### Economics and operations

- revenue is not treated as profit;
- unit-economics assumptions are visible;
- LTV/CAC claims expose time-window and retention assumptions;
- delivery capacity is considered;
- cash timing can block otherwise profitable scaling.

### Experimentation

- assumptions are explicit;
- experiments can falsify the hypothesis;
- success criteria exist before interpretation;
- tests are cheaper than the commitment they inform where practical;
- evidence changes decisions;
- inconclusive results remain inconclusive.

### Diagnosis and repair

- the current constraint is identified before broad redesign;
- validated business components are preserved;
- smallest sufficient changes are preferred;
- known failures become regression fixtures.

### Extension Packs

- core works without packs;
- packs materially change business-model behaviour;
- business-model-specific metrics are evaluated;
- core-vs-pack differences are measured;
- pack-authoring capability exists.

### Product behaviour

- 15 primary progressive examples exist with exact prompts;
- six canonical specs exist;
- README matches actual implementation;
- canonical stress tests cover consumer subscription, professional services and open-source ecosystem models;
- local and clean external installation pass.

All triggered mandatory gates must pass for the particular claim. A correctly blocked commercial proposal can be an adequate skill response; specification 04 separates response conformance from business approval. A favourable dimension cannot compensate for an unresolved cash, rights, capacity or evidence gate.

## 11. Non-goals

Until evidence proves otherwise, `business-building-skills` is not:

- a replacement for the five source books;
- a business-book summarisation repository;
- a universal entrepreneurship doctrine;
- a CRM;
- a marketing automation platform;
- an ad-buying platform;
- an accounting package;
- a payment processor;
- a sales-dialler or spam system;
- an investment-advice system;
- a tax-advice system;
- a legal-advice system;
- a market-data vendor;
- a universal business ontology;
- a one-number startup score;
- an autonomous executive team;

Domain and architecture provenance: [2026-09-09-stage-01-domain-and-professional-boundary.md](research-logs/2026-09-09-stage-01-domain-and-professional-boundary.md), [2026-09-10-stage-11-execution-layer.md](research-logs/2026-09-10-stage-11-execution-layer.md), [2026-09-10-stage-12-gap-analysis.md](research-logs/2026-09-10-stage-12-gap-analysis.md), [2026-09-10-stage-12-guardrails.md](research-logs/2026-09-10-stage-12-guardrails.md), [2026-09-10-stage-13-skill-architecture.md](research-logs/2026-09-10-stage-13-skill-architecture.md).

---

Specification 01 · Contract version 1.0 · 12 September 2026
