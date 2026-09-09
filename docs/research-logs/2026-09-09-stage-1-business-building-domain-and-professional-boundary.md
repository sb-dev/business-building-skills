# Stage 1 — Business-Building Domain and Professional Boundary

**Project:** `business-building-skills`  
**Bootstrap stage:** 1 — Define Business-Building Domain and Professional Boundary  
**Status:** Stage complete; boundary decisions remain subject to evidence from later bootstrap stages  
**Date:** 9 September 2026

---

## 1. Purpose

This research log defines what `business-building-skills` means by **building a business**, what outcomes the project owns, which users it serves, which parts of the business lifecycle it covers, and where responsibility must pass to adjacent Production Skills, specialist tools or qualified humans.

The objective is to establish a domain boundary before the project extracts capabilities from the five-book source corpus or researches broader professional practice.

The project must be broad enough to reason about a complete business system, but narrow enough to avoid becoming a universal business automation platform.

---

## 2. Domain Charter

`business-building-skills` provides reusable production intelligence for **forming, validating, operating, diagnosing and evolving a coherent business system**.

It helps an AI agent turn uncertain commercial assumptions into explicit business choices, evidence, experiments, operating models and corrective actions across:

```text
customer / problem
→ value proposition
→ offer
→ pricing / monetisation
→ acquisition
→ sales / conversion
→ delivery
→ retention / expansion / referral
→ unit economics / cash
→ experiment / evidence
→ diagnosis
→ smallest sufficient correction
```

The project owns the **integration logic between these parts**.

It does not need to execute every specialist activity itself. It should know when a business decision requires market research, legal review, financial accounting, software implementation, creative production, CRM execution, paid-media operation or another specialist capability and should hand off accordingly.

A useful short boundary is:

> Business Building Skills owns business-system decisions and learning loops. Specialist skills and tools own specialist execution and regulated judgement inside those decisions.

---

## 3. What the Project Owns

The project owns reusable reasoning, workflows, artefacts, diagnostics and evaluation concerned with the viability and coherence of a business.

### 3.1 Opportunity framing

Own:

- expressing the opportunity as a falsifiable business hypothesis;
- identifying the customer, buyer, user and beneficiary where they differ;
- describing the problem, desired progress or unmet demand;
- identifying the status quo and alternatives;
- recording important assumptions and uncertainties;
- deciding what must be learned before significant commitment.

Do not own primary market research execution when deeper external investigation is required. That should compose with Deep Research Skills or specialist research tooling.

### 3.2 Customer and problem model

Own:

- the declared target customer;
- the commercial problem or desired outcome;
- buying context and relevant constraints;
- distinction between observed evidence and assumed customer behaviour;
- implications for offer, channel, sales path and delivery.

Do not pretend that AI-generated personas are customer evidence.

### 3.3 Value proposition and offer

Own:

- defining the outcome the business promises to help create;
- connecting customer evidence to a credible value proposition;
- offer structure, packaging and scope;
- price presentation as a business-model choice;
- risk allocation and legitimate risk reduction;
- proof requirements and trust requirements;
- identifying where claims require substantiation or legal review.

Do not own deceptive persuasion, fabricated proof, false scarcity, dark patterns or unsupported claims.

### 3.4 Pricing and monetisation

Own:

- pricing hypotheses;
- pricing structure;
- transaction model;
- subscription, one-off, usage, service, marketplace, licensing or hybrid revenue logic;
- expansion and repeat-purchase mechanisms;
- implications for margin, cash timing, retention and customer value;
- experiments that can reduce pricing or monetisation uncertainty.

Do not own formal valuation, securities analysis, investment recommendations, statutory accounting or tax advice.

### 3.5 Acquisition and demand system

Own:

- acquisition strategy at the business-system level;
- candidate channel selection;
- channel-to-customer fit;
- lead-quality definition;
- demand-generation hypotheses;
- acquisition economics;
- sequencing cheap demand tests before expensive scale;
- diagnosing whether the problem is traffic quantity, traffic quality, message, offer or channel.

Do not own direct operation of advertising platforms, bulk outbound infrastructure, CRM administration or consent-sensitive messaging systems unless a later specialist execution surface is explicitly justified.

### 3.6 Sales and conversion path

Own:

- the commercial path from qualified interest to purchase;
- self-serve versus assisted sales choices;
- sales-stage assumptions;
- conversion bottleneck diagnosis;
- trust, proof and objection requirements;
- commercial handoffs;
- measurement of progression through the path.

Do not become a sales-engagement platform, CRM, dialler, email sequencer or autonomous negotiation system.

### 3.7 Delivery and operating model

Own:

- how value is delivered at a business-model level;
- relationship between promise, fulfilment cost and capacity;
- manual versus automated delivery choices;
- capacity constraints relevant to growth;
- fulfilment bottlenecks that undermine economics or customer value;
- operational implications of offer or pricing changes.

Do not own detailed software architecture, service design implementation, supply-chain execution, workforce scheduling or other specialist operating disciplines when those require dedicated expertise.

### 3.8 Retention, expansion and referral

Own:

- whether the business depends on repeat value delivery;
- retention and repeat-purchase hypotheses;
- expansion mechanisms;
- referral and advocacy loops;
- relationship between retention and acquisition economics;
- diagnosis of churn or weak repeat behaviour at the business-system level.

Do not treat retention tactics as a substitute for actual customer value.

### 3.9 Unit economics and cash model

Own enough financial reasoning to determine whether the business model is commercially coherent.

This includes, where relevant:

```text
revenue per customer / transaction
variable cost
contribution margin
customer acquisition cost
payback
refunds / returns
retention / churn
repeat purchase
customer lifetime economics
capacity cost
working-capital effects
payment timing
cash conversion
```

The project should be able to detect cases such as:

```text
revenue growth with negative contribution margin
profitable sales with unaffordable acquisition payback
healthy margin with cash-timing failure
strong first purchase with destructive churn
high demand with fulfilment capacity failure
```

It does not own bookkeeping, statutory accounts, audited financial statements, tax calculations, payroll, treasury execution, formal corporate finance or investment advice.

### 3.10 Experiment and learning system

Own:

- assumption mapping;
- prioritisation of risky assumptions;
- experiment selection;
- cheapest adequate test;
- measurable success and failure conditions;
- evidence recording;
- separation of observation from interpretation;
- confidence updates;
- decision after evidence;
- preservation of validated decisions.

The project should favour learning per unit of cost and commitment rather than activity volume.

### 3.11 Constraint diagnosis and business-model review

Own cross-system diagnosis.

Given poor performance, the project should determine the smallest plausible responsible layer before recommending broad change.

Examples:

```text
weak qualified demand
→ customer / channel / acquisition

qualified demand but weak conversion
→ offer / trust / sales path

strong conversion but poor margin
→ price / cost / fulfilment

healthy acquisition but weak retention
→ delivered value / onboarding / retention

healthy economics but cash stress
→ payment timing / working capital / growth pace

healthy demand and economics but service failure
→ delivery capacity / operations
```

This diagnostic responsibility is central to the project.

---

## 4. Intended Users

### 4.1 Primary users

The project is primarily designed for people or AI agents helping them build and improve real businesses, including:

```text
founders
solo business builders
small business owners
operators
early business teams
product / venture builders
consultants and agencies working on business models
innovation teams testing new commercial propositions
```

The repository should remain usable by a single capable operator rather than assuming a large specialist organisation.

### 4.2 Secondary users

It may also support:

- product managers validating a new commercial proposition;
- internal venture teams;
- existing companies launching a new offer, segment or revenue model;
- domain specialists who need a coherent business-system view around their work;
- AI delivery systems composing Business Building Skills with other Production Skills.

### 4.3 AI-agent role

The AI agent is a **business-building copilot and production agent**, not the ultimate commercial authority.

It may:

- analyse evidence;
- generate alternatives;
- expose assumptions;
- calculate business-model implications;
- design experiments;
- diagnose likely constraints;
- produce working business artefacts;
- recommend specialist handoffs.

It must not silently commit the business to material financial, legal, reputational or customer-facing obligations where human approval is required.

---

## 5. Lifecycle Coverage

Business Building Skills covers both **greenfield business formation** and **existing-business improvement**.

### 5.1 Greenfield path

A representative greenfield path is:

```text
opportunity
→ explicit assumptions
→ customer / problem evidence
→ value proposition
→ offer hypothesis
→ pricing / monetisation hypothesis
→ cheap demand test
→ sales-path test
→ manual or low-cost delivery test
→ economics evidence
→ retention / repeat evidence where relevant
→ repeatable business system
→ measured expansion
```

The project should resist premature commitment to a complete product, brand system, acquisition stack or operating organisation while the business model remains unvalidated.

### 5.2 Existing-business path

A representative existing-business path is:

```text
observed business problem
→ current-system model
→ evidence by layer
→ binding constraint hypothesis
→ smallest responsible intervention
→ experiment / controlled change
→ measured result
→ preserve or revert
→ next constraint
```

Existing validated decisions should be treated as assets. A failed campaign should not automatically trigger a pricing redesign; a delivery-capacity problem should not automatically trigger a new target customer.

### 5.3 Growth and scaling

The project covers growth where growth changes or stresses the business system, including:

- channel expansion;
- higher acquisition spend;
- sales-capacity expansion;
- pricing or packaging changes;
- new customer segments;
- retention and expansion systems;
- fulfilment capacity;
- working capital;
- cash payback;
- operating constraints.

It does not automatically own enterprise transformation, organisational design, M&A, international tax structure or capital-markets strategy.

---

## 6. B2C and B2B Applicability

The core model should support both consumer and business markets.

The shared business-system responsibilities remain broadly similar:

```text
customer / buyer
value
commercial offer
acquisition
conversion
revenue
fulfilment
retention / repeat
unit economics
cash
learning
```

However, workflows and metrics may differ materially.

### B2C examples of variation

- short buying cycle;
- higher transaction volume;
- performance marketing;
- ecommerce conversion;
- refunds and returns;
- subscriptions;
- consumer-protection obligations.

### B2B examples of variation

- buyer, user and approver may differ;
- long sales cycles;
- qualification;
- account-level economics;
- procurement and security review;
- pilots;
- implementation effort;
- contract renewal and expansion.

The core architecture should not hard-code either B2C funnel conventions or enterprise-sales conventions as universal.

Extension Packs may later specialise behaviours for business models such as SaaS, ecommerce, professional services, marketplaces or subscription businesses once the pack architecture is designed.

---

## 7. Strategy Versus Tactical Execution

Business Building Skills spans strategy and tactics, but with a precise rule:

> It owns tactics when they are necessary to test, operate or repair a business hypothesis; it does not need to become the specialist execution system for every tactic.

For example:

| Business question | Business Building Skills | Specialist execution |
|---|---|---|
| Which customer segment should we test? | Own | Deep research may supply evidence |
| Which acquisition channel is most plausible? | Own | Ad / outreach tooling executes campaign |
| What landing-page claim should be tested? | Own business hypothesis and evidence requirement | UI/UX, copy or creative skills produce final artefact |
| Should we introduce a subscription? | Own | Legal, billing and software systems implement it |
| Why is conversion falling? | Own cross-system diagnosis | Specialist skills repair the responsible layer |
| Should we increase price? | Own commercial hypothesis and experiment design | Billing / commerce system applies approved change |

This protects the project from collapsing into a loose collection of marketing, finance and operations utilities.

---

## 8. Financial-Analysis Depth

The project needs a **managerial and business-model financial layer**, not a full accounting profession implementation.

### It should be able to reason about

```text
revenue model
price and volume
contribution margin
unit economics
acquisition cost
payback
retention economics
refund / return effects
delivery cost
capacity economics
cash timing
working capital at a decision level
scenario comparisons
break-even conditions
commercial sensitivity
```

### It should not claim authority over

```text
statutory accounting
audit
GAAP / IFRS compliance
tax returns
tax optimisation
payroll accounting
regulated financial advice
investment suitability
securities recommendations
formal business valuation
capital adequacy
regulated lending decisions
```

Where the distinction matters, output should state whether a figure is:

```text
observed accounting data
management estimate
business-model assumption
scenario
forecast
calculated business metric
```

rather than presenting all numbers as equivalent facts.

---

## 9. Marketing and Sales Boundary

Marketing and sales are inside the business system but do not consume the entire project.

### Business Building Skills owns

- target market and customer hypothesis;
- positioning implications at a commercial level;
- value proposition;
- offer logic;
- acquisition-channel choice;
- lead-quality model;
- sales-path design;
- conversion hypotheses;
- acquisition economics;
- campaign or outreach experiments as business tests;
- diagnosis across customer, channel, message, offer and sales path.

### Specialist capabilities own or may own

- finished brand identity;
- visual design;
- long-form copy production where specialised production skill is useful;
- media production;
- advertising creative production;
- ad-platform configuration and bidding;
- CRM administration;
- email-delivery infrastructure;
- sales diallers;
- contact enrichment;
- automated prospecting;
- consent and suppression-list implementation;
- sales-call execution.

Business Building Skills may generate requirements or test briefs for these surfaces and evaluate their effect on the business system.

---

## 10. Operations Boundary

Operations matter when they affect whether the commercial promise can be delivered profitably, reliably and at the required capacity.

The project therefore owns business-level operating questions such as:

```text
Can this offer be fulfilled at the promised quality?
What is the delivery bottleneck?
What variable cost is created by this offer?
Can capacity support the proposed acquisition rate?
Should delivery remain manual while uncertainty is high?
Does automation improve economics enough to justify commitment?
Does growth create working-capital stress?
```

It should not attempt to replace specialist operational disciplines such as:

```text
manufacturing engineering
warehouse management
supply-chain optimisation
workforce-management systems
software architecture
site reliability engineering
clinical operations
regulated quality systems
```

unless future evidence supports a specific Business Building extension that remains within the family boundary.

---

## 11. Responsibility Map and Handoffs

| Area | Business Building Skills responsibility | Handoff target |
|---|---|---|
| Opportunity | Frame commercial hypothesis, assumptions, evidence needs | Deep Research Skills for external research |
| Customer / problem | Define model, evidence requirements, implications | Deep Research Skills / UI-UX research where deeper research is needed |
| Value proposition | Own business proposition and commercial coherence | Narrative / brand / UI-UX skills for specialist expression |
| Offer | Own structure, economics, risk and proof requirements | Legal Skills for terms/claims; creative skills for production |
| Pricing | Own pricing hypothesis and commercial model | Accounting/tax/legal specialists where implications require them |
| Monetisation | Own revenue mechanism and economic implications | Software Engineering for implementation; Legal Skills for contract/regulatory issues |
| Acquisition | Own channel strategy, test design and economics | Ad, outreach, content or media execution tools |
| Sales | Own path, qualification logic and conversion diagnosis | CRM / sales tooling and human sellers |
| Delivery | Own business-level fulfilment and capacity model | Domain operations / Software Engineering / service design |
| Retention | Own retention economics and business diagnosis | Product, customer-success, UI/UX or service specialists |
| Unit economics | Own managerial business-model analysis | Accounting / finance specialists for formal reporting or regulated analysis |
| Cash | Own decision-level timing and working-capital implications | Accountant / treasury / tax specialist where formal expertise is required |
| Experiments | Own business hypothesis, test design and learning decision | Research, product, engineering or marketing tools execute specific test |
| Legal risk | Identify issue, stop unsafe optimisation, prepare handoff context | Legal Skills / qualified counsel |
| Tax | Identify tax dependency as a decision constraint | Qualified tax professional / specialist tax tooling |
| Regulated activity | Detect possible regulated boundary and require escalation | Qualified professional / authorised organisation |
| Lifecycle governance | Produce business decisions/evidence usable by governance | Pactwright if the consuming project uses it |

---

## 12. Legal, Tax and Regulated-Activity Boundary

Business Building Skills must treat legal and regulatory constraints as inputs to business design without presenting itself as the final legal authority.

### It may

- identify that a proposed offer, claim, price presentation or sales method creates legal risk;
- identify jurisdiction-sensitive assumptions;
- refuse to optimise around deception or unlawful conduct;
- produce facts, commercial intent and questions for legal review;
- preserve approved legal constraints in subsequent business decisions;
- require legal approval before a risky change is treated as deployable.

### It must not

- fabricate legal certainty;
- present jurisdiction-specific legal conclusions as universally valid;
- replace qualified advice where professional judgement is required;
- recommend evasion of tax, consumer, marketing, privacy, financial or employment obligations;
- convert a commercial preference into a legal interpretation.

Likely escalation surfaces include:

```text
advertising and substantiation
consumer protection
pricing presentation
subscriptions and cancellation
refunds / guarantees
privacy and direct marketing
email / SMS consent
testimonials / endorsements
earnings or ROI claims
competition / antitrust
financial promotions
regulated financial activity
health claims
children / vulnerable consumers
employment / contractor classification
intellectual property
cross-border trade
tax
```

Stage 9 will define these handoffs in greater detail.

---

## 13. Human Approval Points

The project should distinguish between **analysis that may be automated** and **commitments that require accountable approval**.

Human approval is required before an AI agent independently causes or authorises material changes such as:

```text
publishing a new customer-facing claim
committing to a guarantee or refund obligation
material price change
new subscription or renewal terms
significant paid-media spend
bulk outbound / direct marketing activation
contractual commitment
regulated or jurisdiction-sensitive commercial activity
material inventory / hiring / capital commitment
borrowing or financing commitment
business-model change with significant customer impact
collection or use of sensitive / regulated customer data
```

Human approval should also be available as an explicit checkpoint when evidence is ambiguous but the decision is irreversible or expensive.

The project may later define lower-risk actions that can be executed automatically under pre-approved limits, but automation authority must be explicit rather than assumed.

---

## 14. Quality Model

Business quality is multidimensional. The project should evaluate the business system by separate dimensions rather than one synthetic score.

Candidate quality dimensions for later refinement are:

| Dimension | Core question |
|---|---|
| Customer evidence | Is the customer/problem model supported by real evidence? |
| Problem importance | Is the problem or desired progress commercially meaningful? |
| Value clarity | Is the value proposition understandable and relevant? |
| Offer strength | Does the offer make value, scope, proof and risk allocation credible? |
| Differentiation | Is there a defensible reason to choose this business over alternatives or the status quo? |
| Trust / proof | Are claims supported by adequate evidence and credible proof? |
| Pricing fit | Does pricing align customer value, willingness to pay and business economics? |
| Monetisation coherence | Does the revenue mechanism fit customer behaviour and delivery model? |
| Acquisition quality | Does acquisition attract the right prospects economically? |
| Conversion quality | Can qualified demand progress to purchase without misleading pressure? |
| Delivery quality | Can the promised value actually be delivered? |
| Retention / repeat value | Does continued customer behaviour indicate continuing value where relevant? |
| Unit economics | Does the business generate acceptable economics per relevant unit? |
| Cash robustness | Can obligations be met given cash timing and growth pace? |
| Capacity robustness | Can the operating model handle intended demand? |
| Experiment quality | Do tests reduce meaningful uncertainty? |
| Learning velocity | Does evidence cause timely, traceable decisions? |
| Preservation | Are validated decisions protected from unrelated churn? |
| Legal / ethical robustness | Are commercial choices truthful and compatible with required constraints? |

Later stages may merge, rename or specialise these dimensions when broader professional evidence is available.

---

## 15. Working Artefacts Implied by the Boundary

Stage 1 does not design the final artefact model, but the domain boundary already implies likely working artefacts such as:

```text
business hypothesis
customer / buyer model
problem / desired-progress statement
assumption register
value proposition
offer brief
pricing hypothesis
monetisation model
acquisition hypothesis
sales-path model
delivery / capacity model
unit-economics model
cash-timing model
experiment brief
evidence record
business-system diagnosis
constraint hypothesis
corrective-action decision
business-model review
```

These are provisional inputs to later workflow design, not a final repository structure.

---

## 16. Explicit Non-Goals

`business-building-skills` is not intended to become:

```text
a generic entrepreneurship textbook
a reproduction of the five source books
a universal business ontology
a business-plan generator as its primary product
a pitch-deck generator
a CRM
a sales-engagement platform
an ad-buying platform
an email-marketing platform
an accounting package
a bookkeeping system
a tax engine
an investment adviser
a securities-analysis system
a legal-advice engine
a payroll system
a treasury platform
a generic project-management system
a software-development framework
a brand or creative-production framework
a universal market-research engine
a universal autonomous-company agent
a replacement for qualified human judgement in regulated domains
```

It may compose with systems that perform those functions.

---

## 17. Boundary Tests

The following tests should be used in later stages when deciding whether a capability belongs in the core project.

### Test A — Does it change or evaluate the business system?

If a capability determines customer, value, offer, revenue, acquisition, conversion, delivery, retention, economics, cash, experiment or business constraint, it is likely in scope.

If it merely performs specialist implementation after those decisions are made, it is more likely a handoff.

### Test B — Is the knowledge reusable across business types?

Core skills should encode durable business-building intelligence.

A highly specific SaaS, ecommerce, marketplace or professional-services method may belong in an Extension Pack rather than core.

### Test C — Does it require regulated professional judgement?

If yes, Business Building Skills may identify the issue and structure the decision, but final authority belongs to the relevant qualified professional or specialist system.

### Test D — Can a specialist Production Skill execute it better?

If yes, Business Building Skills should produce a clear brief, constraints and acceptance criteria rather than duplicate the specialist domain.

### Test E — Is it a tactic without a business decision?

If the capability is only "send emails", "run ads", "make a logo", "build a landing page" or "implement billing", it is not sufficient reason for core ownership.

The project owns why, when, for whom, under what economics, what evidence and how success changes the business decision.

---

## 18. Decisions Made in Stage 1

1. **The domain is business-system production, not business-content generation.**
2. **The project covers both new businesses and existing-business diagnosis/evolution.**
3. **Core applicability must span B2C and B2B without hard-coding either model.**
4. **Business Building Skills owns cross-functional commercial integration, not every specialist execution layer.**
5. **Managerial financial reasoning is in scope; statutory accounting, tax and investment advice are out of scope.**
6. **Marketing and sales are in scope as business systems; CRM, ad-tech and outbound infrastructure are not core responsibilities.**
7. **Operations are in scope where delivery, cost, capacity or cash constrain the business; specialist operational implementation remains a handoff.**
8. **Experiment design, evidence handling and constraint diagnosis are first-class core responsibilities.**
9. **Human approval is mandatory for material legal, financial, reputational or customer-facing commitments unless an explicit pre-authorised execution policy later says otherwise.**
10. **Legal, tax and regulated concerns are surfaced and routed, not silently solved as if universal professional advice.**
11. **Business quality remains multidimensional; no single universal business score is assumed.**
12. **The project must preserve validated business decisions and prefer the smallest responsible correction.**

---

## 19. What Remains Provisional

Stage 1 establishes the boundary, not the final production model.

The following remain deliberately provisional:

```text
final capability taxonomy
final skill decomposition
final command set
exact artefact schemas
business-model-specific Extension Packs
formal evidence hierarchy
metric definitions and thresholds
financial calculation contracts
legal-handoff contract
execution-layer selection
example catalogue
benchmark cases
```

They must be resolved from later bootstrap evidence rather than inferred from this charter alone.

---

## 20. Inputs to Stage 2

Stage 2 should use this domain charter to extract and reconcile the five-book source corpus.

The extraction should ask of every candidate book concept:

```text
Which owned business outcome does this support?
What business decision does it improve?
What evidence does it require?
What artefact or workflow does it imply?
Does it duplicate another source?
Does it conflict with another source?
Is it core, business-model-specific, specialist execution or out of scope?
Does it create a legal / ethical / professional handoff?
What claim requires broader validation in Stage 3?
```

The books should therefore be mapped into this business-building domain rather than allowed to redefine the domain around their chapter structures or branded terminology.

---

## 21. Stage 1 Exit Assessment

The Stage 1 exit criterion is satisfied.

The project can now explain "building a business" independently from any one source book:

> Build and improve a coherent system that identifies a customer need, creates and communicates credible value, converts demand into economically viable transactions, fulfils the promise, retains or expands value where relevant, manages cash and capacity constraints, tests uncertainty cheaply, and changes the smallest responsible layer when evidence shows the system is failing.

This definition is sufficiently concrete to constrain Stage 2 capability extraction while remaining open to revision from broader professional and empirical research in Stage 3.
