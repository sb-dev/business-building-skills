# Business Building Skills — New Project Bootstrap Process

**Status:** Bootstrap specification  
**Version:** 1.2  
**Date:** 11 September 2026

## 1. Purpose

This process defines how `business-building-skills` moves from a project idea to a **specified, scaffolded, benchmarked, installable open-source Agent Skills repository** for evidence-driven business building.

The project should help AI agents turn an opportunity, product, service or existing business into a coherent system spanning:

```text
customer / problem
→ value
→ offer
→ pricing / monetisation
→ acquisition
→ sales / conversion
→ delivery
→ retention / expansion / referral
→ unit economics / cash
→ experimentation
→ evidence
→ diagnosis
→ smallest sufficient correction
```

The project is not a collection of summaries or prompts for five business books. The books are an initial evidence corpus from which reusable capabilities are extracted, challenged, reconciled and independently expressed.

The initial source corpus is:

1. *$100M Offers: How to Make Offers So Good People Feel Stupid Saying No*
2. *$100M Leads: How to Get Strangers To Want To Buy Your Stuff*
3. *$100M Money Models: How To Make Money*
4. *The Personal MBA: Master the Art of Business*
5. *The Lean Startup: How Today's Entrepreneurs Use Continuous Innovation to Create Radically Successful Businesses*

The target thesis is:

> Business-building intelligence lies in turning uncertain customer and economic assumptions into coherent business choices, testing the riskiest assumptions cheaply, creating compelling but truthful value propositions, building repeatable demand and monetisation systems, and improving the current constraint without unnecessary change.

This thesis must be validated through broader professional and empirical business research. The five books are starting inputs, not unquestionable doctrine.

---

## 2. Production Skills Family Position and Boundaries

`business-building-skills` is a **Production Skills family project**. It applies the family architecture to the production discipline of creating, validating and evolving viable businesses.

Its family role is:

```text
Business Building Skills
→ owns reusable business-building production intelligence

Other Production Skills
→ produce the software, research, legal analysis, design, media, worlds,
  audio and other domain artefacts used to create and deliver value

Pactwright
→ may govern authorised delivery work, Contracts and Evidence
```

Business Building Skills may compose with:

```text
Deep Research Skills
Legal Skills
UI/UX Design Skills
Software Engineering Skills
Narrative / Video / Audio Production Skills
other Production Skills
```

while remaining independently installable and useful without Pactwright or any other Production Skills project.

The central `production-skills` repository owns only family-level contracts, registry/maturity, bootstrap rules and abstractions proven across multiple domains. `business-building-skills` owns its business workflow, artefacts, commands, Extension Packs, examples, benchmarks and domain research.

Apply the normal family extraction rule: promote shared abstractions only after multiple independent Production Skills domains demonstrate substantially the same need.

---

## 3. Book-Derived Knowledge Rule

The repository must encode **capabilities**, not books.

Do not create this architecture:

```text
skills/
├── 100m-offers/
├── 100m-leads/
├── 100m-money-models/
├── personal-mba/
└── lean-startup/
```

Instead extract:

```text
source idea
→ business capability
→ production responsibility
→ command / workflow
→ evaluation criterion
→ benchmark case
```

A principle appearing in several books should become one coherent capability rather than duplicated skills.

A book-specific idea that does not survive broader research should remain a cited research finding, not a core rule.

### Copyright-safe extraction

The repository may use ideas, methods, high-level frameworks and independently expressed synthesis.

It must not reproduce substantial copyrighted text, chapter structure, proprietary examples or long passages.

Use the source books as:

```text
evidence
comparison material
historical/business-practice context
candidate framework sources
```

not as text corpora to republish.

Where a book uses branded terminology, research whether the underlying concept has a broader professional equivalent and prefer domain-neutral language in the reusable skill unless the branded term materially improves precision.

---

## 4. Initial Source-to-Capability Hypothesis

The following map is provisional and must be tested.

| Source | Primary capability families to extract |
|---|---|
| `$100M Offers` | offer design, value construction, pricing, packaging, risk reduction, offer economics |
| `$100M Leads` | demand creation, lead generation, channel choice, outreach, lead magnets, acquisition systems |
| `$100M Money Models` | monetisation architecture, revenue expansion, transaction structure, cash generation, economic sequencing |
| `The Personal MBA` | value creation, marketing, sales, finance, operations, systems thinking, general business vocabulary |
| `The Lean Startup` | assumptions, experiments, validated learning, iteration, evidence-driven commitment |

The combined repository should reconcile overlaps rather than preserve five parallel models.

Potential cross-book capability clusters include:

```text
opportunity framing
customer / problem understanding
value proposition
offer construction
pricing
monetisation
lead generation
channel strategy
sales path
conversion
delivery
retention
expansion
referral
unit economics
cash / capacity
assumption mapping
experiment design
learning
constraint diagnosis
business-system evaluation
```

---

## 5. Governing Principles

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

---

# 6. Bootstrap Flow

```text
PROJECT IDEA
    ↓
0. Create Bootstrap Workspace Repository
    ↓
1. Define Business-Building Domain and Professional Boundary
    ↓
2. Extract and Reconcile the Five-Book Capability Corpus
    ↓
3. Research Broader Professional and Empirical Business Practice
    ↓
4. Define Business-System, Customer and Value Model
    ↓
5. Define Offer, Pricing and Monetisation Architecture
    ↓
6. Define Demand, Lead Generation, Sales and Conversion Architecture
    ↓
7. Define Delivery, Retention, Expansion, Unit Economics and Cash Model
    ↓
8. Define Assumption, Experiment, Learning and Constraint-Diagnosis Model
    ↓
9. Define Ethical, Consumer-Protection and Legal Handoffs
    ↓
10. Research Existing Agent Skills, Tools and Business Systems
    ↓
11. Choose Execution Layer
    ↓
12. Gap Analysis + Over-Engineering Guardrails
    ↓
13. Design Core Skills and Commands
    ↓
14. Design Extension Packs and Pack Authoring
    ↓
15. Design Five Progressive Example Levels
    ↓
16. Design Canonical Business Stress Tests
    ↓
17. Design Evals, Benchmarks and Regression Fixtures
    ↓
18. Generate Six Canonical Specifications
    ↓
19. Design Public README and Public Claims Contract
    ↓
20. Cross-Project Review
    ↓
21. Scaffold Production Repository and Preserve Public README
    ↓
22. Implement and Prove Core Vertical
    ↓
23. Expand Progressive Coverage and Extension Packs
    ↓
24. Validate Installation and Repository Integrity
    ↓
25. Optional Pactwright Integration + Registry Promotion
    ↓
26. Review Shared-Abstraction Candidates
    ↓
MATURE BUSINESS BUILDING SKILLS PROJECT
```

The Stage 0 repository is the durable bootstrap workspace, not the production scaffold created at Stage 21.

---

# 7. Stage 0 — Create Bootstrap Workspace Repository

Create `sb-dev/business-building-skills` before substantive bootstrap research begins.

Initial structure:

```text
business-building-skills/
├── README.md
└── docs/
    └── research-logs/
        ├── README.md
        └── 2026-09-08-business-building-skills-new-project-bootstrap-process.md
```

The root README should contain only:

```text
project name
provisional one-line purpose
bootstrap status
```

The research-log README should explain that this directory is the durable record of bootstrap evidence and decisions.

Do not create yet:

```text
skills/
examples/
benchmarks/
extension-packs/
tools/
tests/
integrations/
.github/
package metadata
production CI
```

unless bootstrap research itself genuinely requires them.

Repository existence does not imply `scaffolded` maturity.

**Exit:** later stages can continue primarily from repository research logs rather than long conversation context.

---

# 8. Stage 1 — Define Business-Building Domain and Professional Boundary

Resolve:

```text
owned business outcomes
intended users
business lifecycle coverage
greenfield vs existing-business work
consumer vs B2B applicability
business strategy vs tactical execution
financial-analysis depth
marketing / sales boundaries
operations boundaries
legal / tax / regulated-activity boundaries
human approval points
non-goals
```

Candidate owned outcomes:

```text
opportunity framing
customer/problem model
value proposition
offer
pricing
money model
acquisition system
sales path
delivery/economic model
business experiments
constraint diagnosis
business-model review
```

Explicitly distinguish Business Building Skills from:

```text
market/deep research
legal advice
accounting / tax
investment advice
financial planning
software/product implementation
brand/creative production
sales CRM execution
paid-ad platform operation
Pactwright lifecycle governance
```

**Research-log output:** domain charter, responsibility map, user model, quality dimensions, human/legal handoffs and non-goals.

**Exit:** the project can explain what “building a business” means without referring to any one book.

---

# 9. Stage 2 — Extract and Reconcile the Five-Book Capability Corpus

## Purpose

Turn the five books into a structured capability evidence base without making the repository book-shaped.

For each book capture:

```text
business problem addressed
core concepts
workflow implications
decision heuristics
metrics
assumptions
examples as abstract patterns only
failure modes
areas of overlap
areas of tension
claims requiring broader validation
```

Create a source-to-capability matrix.

Candidate fields:

| Field | Meaning |
|---|---|
| Source | Book |
| Concept | Independently paraphrased idea |
| Capability | Reusable business responsibility |
| Lifecycle stage | Where it applies |
| Inputs | Facts/evidence needed |
| Output | Decision/artefact |
| Metric/evidence | How it can be checked |
| Risks | Failure or misuse modes |
| Overlap | Other sources supporting similar need |
| Status | retain / merge / adapt / reject / research |

Explicitly compare tensions such as:

```text
aggressive value/offer optimisation
vs
experiment-before-commitment

lead volume
vs
lead quality / capacity

revenue expansion
vs
retention / customer value / cash risk

broad business heuristics
vs
context-specific evidence
```

Do not resolve disagreement by choosing the most commercially aggressive option automatically.

**Research-log output:** five-book extraction, overlap matrix, conflict log and provisional capability taxonomy.

**Exit:** the books have become evidence for capabilities rather than the architecture itself.

---

# 10. Stage 3 — Research Broader Professional and Empirical Business Practice

Use the book-derived taxonomy to guide, not limit, broader research.

Research at least:

```text
customer discovery
market research
positioning
value proposition design
pricing
revenue models
B2B sales
consumer conversion
demand generation
performance marketing
content / organic acquisition
referrals / partnerships
sales operations
customer success / retention
unit economics
management accounting
cash flow / working capital
operations / capacity
service design
subscription businesses
marketplaces
SaaS
ecommerce
professional services
experimentation / A/B testing
product-market fit concepts
business-model innovation
```

Prefer durable professional practice and empirical evidence over social-media business folklore.

For each practice capture:

```text
decision it supports
inputs
cheap evidence
working artefacts
metrics
commitment points
failure modes
repair actions
business-model dependencies
```

Research criticisms and failure conditions of the initial book frameworks.

**Research-log output:** professional-practice map, terminology map, evidence hierarchy, failure taxonomy and unresolved claims.

**Exit:** core principles can be justified independently from the five books.

---

# 11. Stage 4 — Define Business-System, Customer and Value Model

Define the smallest useful representation of a business system.

Candidate model:

```text
target customer
problem / desired progress
alternative / status quo
value proposition
offer
acquisition channel
sales / conversion path
price / revenue mechanism
delivery mechanism
cost structure
retention / repeat / expansion
referral / advocacy
operational constraints
cash timing
key assumptions
```

Do not create a universal ontology of business.

### Customer evidence

Separate:

```text
declared target customer
observed customer
buyer
user
economic decision-maker
influencer
```

where relevant.

Capture evidence such as:

```text
interviews
sales calls
support issues
search / demand evidence
usage data
conversion data
retention data
competitive alternatives
willingness-to-pay evidence
```

### Value model

Distinguish:

```text
functional value
economic value
emotional value
social/status value
risk reduction
time reduction
effort reduction
uncertainty reduction
```

without assuming every offer needs all dimensions.

**Exit:** later offer and growth work can trace decisions back to customer/value evidence.

---

# 12. Stage 5 — Define Offer, Pricing and Monetisation Architecture

## Offer model

Research reusable offer components:

```text
customer
outcome
scope
mechanism
deliverables
time-to-value
price
payment structure
risk reversal
guarantee / refund terms
bonuses / added components
proof / credibility
constraints / exclusions
urgency / scarcity only where truthful
```

A good offer must be deliverable at the promised quality and economics.

### Pricing

Research:

```text
cost-informed boundaries
value-based pricing
competitor/reference pricing
willingness-to-pay
tiering
packaging
usage pricing
subscription
one-time purchase
service retainers
performance-linked structures where lawful/appropriate
freemium / free-to-paid
discounting
payment timing
```

Do not optimise conversion by hiding material price or renewal terms.

### Monetisation architecture

Research:

```text
initial transaction
recurring revenue
upsell
cross-sell
expansion
renewal
usage
services
licensing
marketplace take rate
advertising
affiliate / referral revenue
open-source commercialisation
```

For each model define:

```text
value exchange
payer
pricing unit
gross revenue
direct costs
margin
cash timing
retention dependency
capacity dependency
risk
```

**Research-log output:** offer model, pricing decision framework, money-model taxonomy and failure modes.

**Exit:** the repository can distinguish a compelling offer from an economically weak or legally risky one.

---

# 13. Stage 6 — Define Demand, Lead Generation, Sales and Conversion Architecture

Model demand generation as a system rather than a list of tactics.

Candidate stages:

```text
target audience
→ awareness / reach
→ response / engagement
→ lead / prospect
→ qualification
→ sales conversation / conversion path
→ customer
```

Research channel classes:

```text
direct outreach
content
community
search
paid media
partnerships
affiliates
referrals
events
marketplaces
platform distribution
product-led acquisition
existing audience
```

Do not assume all businesses should use all channels.

### Lead quality

Track:

```text
volume
fit
intent
qualification
conversion
acquisition cost
sales effort
time-to-close
retention / downstream quality
```

### Sales path

Research:

```text
self-serve
sales-assisted
consultative
enterprise
inbound
outbound
marketplace-mediated
partner-led
```

Separate marketing-message quality from offer quality and sales execution.

**Research-log output:** acquisition/channel model, lead-quality model, sales-path model and channel selection evidence.

**Exit:** the project can diagnose whether a growth problem is reach, qualification, offer, conversion or downstream economics.

---

# 14. Stage 7 — Define Delivery, Retention, Expansion, Unit Economics and Cash Model

A sold offer is not a viable business until it can be delivered repeatedly.

Research:

```text
fulfilment / delivery process
onboarding
time-to-value
quality control
capacity
service levels
support
retention
repeat purchase
renewal
expansion
referral
refunds / cancellations
failure demand
```

### Unit economics

Research context-appropriate metrics such as:

```text
revenue per customer / transaction
gross margin
contribution margin
cost to serve
customer acquisition cost
payback period
retention / churn
repeat purchase
lifetime value assumptions
refund / chargeback rate
sales cost
support cost
```

Do not accept LTV or CAC figures without exposing assumptions and time windows.

### Cash model

Research:

```text
customer prepayment
receivables
supplier terms
inventory
payroll
refund exposure
advertising spend timing
tax obligations
working capital
cash conversion
runway
```

The project is not an accounting system; it should know when deterministic spreadsheets/accounting tools must own calculations.

**Research-log output:** delivery-capacity model, retention/expansion model, unit-economics contract and cash-risk model.

**Exit:** revenue growth cannot be recommended without checking whether the business can fulfil it economically and operationally.

---

# 15. Stage 8 — Define Assumption, Experiment, Learning and Constraint-Diagnosis Model

## Assumption model

Classify material assumptions such as:

```text
customer exists
problem matters
customer can be reached
offer is understood
customer will pay
channel is economical
delivery works
customer receives promised value
customer stays / repeats
economics remain viable at scale
```

Rate uncertainty and consequence separately rather than creating one opaque risk score.

### Experiment design

Define:

```text
assumption
hypothesis
cheapest valid test
target population
success / failure signal
guardrails
duration / sample requirements where relevant
confounders
decision rule
```

An experiment should be capable of changing the decision. If every outcome would be interpreted as success, it is not useful validation.

### Learning record

Preserve:

```text
assumption
test
observed evidence
result
interpretation
decision
what remains unknown
next experiment / commitment
```

### Constraint diagnosis

Use business evidence to identify the current binding constraint rather than optimising every metric simultaneously.

**Research-log output:** assumption register, experiment contract, learning record, constraint taxonomy and repair-routing model.

**Exit:** the system can move from uncertainty to evidence without treating activity as learning.

---

# 16. Stage 9 — Define Ethical, Consumer-Protection and Legal Handoffs

Business optimisation must remain inside truthful and lawful boundaries.

Research and define handoffs for:

```text
advertising substantiation
comparative claims
guarantees
scarcity / urgency
testimonials / endorsements
email / SMS outreach
privacy / tracking
subscription terms
automatic renewal
cancellation
refunds
pricing presentation
financing / credit
financial promotions
earnings / investment claims
children / vulnerable users
competition / unfair commercial practices
employment / contractor matters
tax
regulated sectors
```

Business Building Skills should:

```text
identify issue
preserve facts
state business intention
surface assumptions
route legal question
consume resulting legal constraint
adjust offer / channel / process
```

Legal Skills should own legal research and conclusions.

Build adversarial evaluation for:

```text
false scarcity
fabricated social proof
unsupported ROI claims
hidden renewal
misleading free trial
spam
dark-pattern cancellation
fake guarantees
```

**Exit:** stronger conversion is never treated as evidence that a tactic is acceptable.

---

# 17. Stage 10 — Research Existing Agent Skills, Tools and Business Systems

Research current reusable capabilities before designing native skills.

Categories:

```text
business strategy Agent Skills
market research
competitive research
pricing
financial modelling
unit economics
growth marketing
SEO / content
paid acquisition
sales / outreach
CRM
analytics
experimentation
landing pages
email automation
customer support / success
accounting / finance tools
spreadsheet modelling
survey/interview tooling
conversion analytics
attribution
forecasting
```

For each candidate record:

```text
name
source
licence
maturity
installation / access model
production responsibility
deterministic vs generative role
data requirements
provider coupling
composability
quality suitability
maintenance
privacy / legal constraints
USE / ADAPT / REFERENCE / REJECT
gaps
```

Existing systems should execute:

```text
CRM operations
email delivery
ad buying
analytics
accounting
payments
spreadsheets
A/B infrastructure
landing-page hosting
survey collection
```

where they already solve those execution problems well.

**Research-log output:** capability landscape, reuse decisions and provider/tool boundaries.

**Exit:** native skills are justified by missing business judgement, not by a desire to rebuild SaaS tools.

---

# 18. Stage 11 — Choose Execution Layer

Business Building Skills should own decisions such as:

```text
business framing
customer/problem reasoning
offer design
pricing / monetisation reasoning
channel strategy
sales-path design
experiment design
metric interpretation
constraint diagnosis
unit-economics reasoning
smallest-sufficient correction
```

Deterministic/external systems should own:

```text
arithmetic
spreadsheet calculation
CRM state
email sending
ad execution
web analytics
billing
accounting
survey collection
A/B assignment
data warehousing
```

when available.

Do not create a universal CRM, analytics platform, marketing automation platform or accounting system.

**Exit:** changing execution tools does not require redesigning the business-building workflow.

---

# 19. Stage 12 — Gap Analysis and Over-Engineering Guardrails

Classify capabilities:

```text
covered
partially covered
missing
```

Test particularly for gaps in:

```text
book-to-capability synthesis
customer evidence discipline
offer/economics consistency
pricing reasoning
lead-quality evaluation
channel/business-model fit
retention-aware acquisition
delivery-capacity checks
cash-aware growth
assumption/observation separation
experiment quality
constraint diagnosis
smallest-change behaviour
truthfulness / consumer safeguards
cross-domain business handoffs
```

Defer unless proven necessary:

```text
universal business ontology
universal CRM
custom ad platform
custom payment system
custom analytics platform
custom accounting engine
universal growth graph
autonomous outbound-spam engine
persistent cross-project customer database
one universal business score
universal experiment platform
universal pricing optimiser
multi-agent virtual executive team
```

**Research-log output:** gap matrix, native capability shortlist, reused capability shortlist and deferred ideas.

**Exit:** every proposed native skill responsibility maps to an evidenced gap.

---

# 20. Stage 13 — Design Core Skills and Commands

Do not begin from a fixed number of skills.

## Lean hypothesis

```text
business-build
business-grow
business-evaluate
business-pack-author
```

Possible responsibility split:

### `business-build`

```text
frame-opportunity
define-customer
define-problem
map-value
design-offer
design-pricing
design-money-model
model-unit-economics
model-delivery
identify-assumptions
design-experiment
```

### `business-grow`

```text
define-demand
select-channel
design-lead-magnet
design-outreach
design-content-loop
design-referral-loop
design-sales-path
improve-conversion
design-retention
design-expansion
scale-channel
```

### `business-evaluate`

```text
audit-customer-evidence
evaluate-opportunity
evaluate-offer
evaluate-pricing
evaluate-money-model
evaluate-channel
evaluate-funnel
evaluate-unit-economics
evaluate-cash-risk
evaluate-retention
evaluate-experiment
audit-claims
diagnose-business-constraint
recommend-smallest-change
```

### `business-pack-author`

```text
inspect-catalogue
research-business-model
define-specialisation
define-core-effects
build-showcase
build-evals
compare-core-vs-pack
validate-pack
```

## Alternative hypothesis

Research whether a separate `business-model` or `business-experiment` skill has enough independent installation value.

Do not split skills merely to mirror the five source books or common executive job titles.

For every command define:

```text
inputs
evidence required
assumptions allowed
output
allowed mutations
forbidden behaviour
metrics/evidence
failure states
legal/ethical boundaries
```

**Research-log output:** skill architecture, command contracts and rejected alternatives.

**Exit:** the smallest coherent skill set can run the business-building loop end to end.

---

# 21. Stage 14 — Design Extension Packs and Pack Authoring

Extension Packs should represent coherent reusable **business-model production grammars**.

Strong candidates to research:

```text
saas-business
consumer-mobile-subscription
professional-services
consulting-business
ecommerce-business
marketplace-business
creator-digital-product
open-source-commercialisation
local-service-business
```

A valid pack may change:

```text
customer / buyer structure
offer grammar
pricing unit
money model
channel priorities
sales path
delivery model
retention model
unit economics
capacity constraints
cash behaviour
core metrics
experiment types
quality criteria
```

A pack must not be merely:

```text
"AI startup"
"finance company"
"fitness business"
"London business"
```

unless the specialisation materially changes reusable business-building behaviour.

### Precedence

```text
verified legal / regulatory constraints
+ explicit project facts and instructions
→ approved business decisions
→ selected Business Extension Pack
→ core Business Building defaults
```

### Pack authoring

```text
inspect catalogue
→ prove existing pack is insufficient
→ research business-model practice
→ define changed core behaviour
→ define economics and constraints
→ build showcase
→ include exact prompt
→ create positive / negative evals
→ compare core vs core+pack
→ validate
→ catalogue
```

**Research-log output:** pack model, candidate catalogue, qualification rules and pack-authoring contract.

**Exit:** packs represent reusable business models, not industry tags.

---

# 22. Stage 15 — Design Five Progressive Example Levels

Target:

```text
5 levels × 3 primary examples = 15 primary examples
```

Choose examples through capability coverage.

## Level 1 — Validate one bounded business decision

Candidate classes:

```text
choose between two pricing structures
evaluate one acquisition channel hypothesis
calculate whether one offer can support its delivery cost
```

## Level 2 — Build one coherent commercial component

Candidate classes:

```text
offer + price for a bounded service
lead magnet + qualification + sales path
retention / renewal redesign for a subscription
```

## Level 3 — Design one complete small business model

Candidate classes:

```text
solo professional service
small SaaS product
small ecommerce / digital-product business
```

## Level 4 — Diagnose and repair an existing business

Candidate classes:

```text
high lead volume / poor conversion
profitable sales / delivery-capacity failure
growing revenue / cash-flow failure
```

## Level 5 — Full business-building thesis

Candidate classes:

```text
Kakeibo consumer subscription business
one-person Forward Deployment Engineer consultancy
Production Skills open-source commercial ecosystem
```

The complete 15 should cover:

```text
B2B / B2C
subscription / transaction / services
self-serve / sales-assisted
paid / organic / outbound / referral acquisition
low / high ticket
short / long sales cycle
digital / human delivery
retention-dependent / one-off
cash-light / working-capital-sensitive
offer design
pricing
money model
lead generation
sales
delivery
retention
unit economics
experimentation
legal/ethical boundaries
constraint diagnosis
```

Every primary example must include its exact copyable prompt.

**Research-log output:** candidate pool, coverage matrix, selected 15 and rationale.

**Exit:** the examples demonstrate a business-building system rather than fifteen marketing exercises.

---

# 23. Stage 16 — Design Canonical Business Stress Tests

Use three deliberately different business structures.

## Stress Test A — Kakeibo

Exercise:

```text
consumer subscription
trust-sensitive financial product
free/trial/guarantee choices
pricing
retention
app-store / direct acquisition
AI assistant value
support/delivery economics
consumer terms / privacy constraints
```

Adversarial cases:

```text
growth recommendation ignores churn
guarantee contradicts actual refund behaviour
pricing hides renewal
financial benefit claims lack evidence
paid acquisition scales before retention/economics work
```

## Stress Test B — One-person FDE consultancy

Exercise:

```text
professional services
high-ticket B2B
expert positioning
outbound / network / content acquisition
qualification
sales calls
scope / packaging
retainer vs project pricing
utilisation / delivery capacity
cash timing
referrals / expansion
```

Adversarial cases:

```text
lead volume exceeds capacity
revenue forecast ignores utilisation
offer overpromises delivery
discounting destroys effective rate
outbound becomes spammy / non-compliant
```

## Stress Test C — Production Skills commercial ecosystem

Exercise:

```text
open-source adoption
services
education
sponsorship / support
marketplace / Extension Packs
developer audience
community-led acquisition
multiple monetisation paths
ecosystem incentives
```

Adversarial cases:

```text
monetisation damages open-source adoption
marketplace added before supply/demand exists
business model conflicts with contributor incentives
too many revenue lines before one is validated
vanity GitHub metrics treated as customer evidence
```

**Exit:** the architecture survives consumer SaaS, high-ticket services and open-source ecosystem models without becoming tailored to one.

---

# 24. Stage 17 — Design Evals, Benchmarks and Regression Fixtures

Evaluation must separate correctness from commercial judgement.

## Deterministic validation

Check where possible:

```text
required artefact fields
arithmetic
unit-economics formulas
cash-flow calculations
funnel consistency
experiment decision rules
metric definitions
pack structure
prompt completeness
installation integrity
```

Use spreadsheets/calculators for arithmetic rather than trusting prose calculations.

## Business reasoning evaluation

Keep dimensions separate:

```text
customer evidence
problem importance
value coherence
offer strength
truthfulness
pricing logic
monetisation coherence
channel fit
lead quality
sales-path fit
delivery feasibility
retention logic
unit economics
cash robustness
experiment quality
constraint diagnosis
```

## Behavioural evaluation

Test whether the agent:

```text
distinguishes facts from assumptions
asks research/tooling to verify external claims when needed
chooses cheap experiments before large commitments
does not invent market size / conversion / CAC data
checks delivery and economics before scaling
uses downstream quality when judging acquisition
diagnoses the current constraint
preserves validated decisions
recommends the smallest responsible change
flags legal/ethical concerns
```

## Adversarial evaluation

Include:

```text
false scarcity
fake urgency
invented testimonials
unsupported guarantee
unsupported earnings / ROI claim
hidden renewal
spam outreach
vanity metrics
CAC without downstream quality
LTV without retention evidence
growth despite negative contribution margin
experiment with no falsifiable decision rule
scaling before delivery capacity
pricing test that changes several variables at once
```

## Preservation and repair

A local failure should not trigger unnecessary redesign.

Example:

```text
channel fails
→ replace/retest channel

not
→ rewrite customer + offer + price + delivery + brand
```

unless evidence shows those layers are responsible.

## Extension Pack evaluation

Every implemented pack must test:

```text
activation
non-activation
precedence
changed business behaviour
pack-specific metrics
negative / incompatible cases
core vs core+pack difference
```

## Regression loop

```text
escaped business-reasoning defect
→ diagnose owning layer
→ create smallest reproducible case
→ add benchmark
→ prove old behaviour fails
→ prove repaired behaviour passes
→ retain permanently
```

**Research-log output:** benchmark taxonomy, case contracts, acceptance gates and regression policy.

**Exit:** the benchmark can detect bad business reasoning even when the prose sounds persuasive.

---

# 25. Stage 18 — Generate Six Canonical Specifications

Generate:

```text
docs/
├── 01-business-building-skills-system-spec.md
├── 02-business-building-skills-workflows-and-artifacts-spec.md
├── 03-business-building-skills-repository-and-contracts-spec.md
├── 04-testing-and-benchmark-spec.md
├── 05-business-building-customisation-packs-spec.md
└── 06-business-building-extension-pack-catalogue.md
```

## 01 — System

Owns:

```text
mission
scope
book-evidence relationship
principles
business-system architecture
core skills
execution boundary
legal/ethical boundary
build order
acceptance
```

## 02 — Workflows and Artifacts

Owns:

```text
customer/value model
offer/pricing
money model
acquisition
sales
delivery
retention/expansion
unit economics
cash
assumptions
experiments
learning
constraint diagnosis
preservation / repair
handoffs
```

## 03 — Repository and Contracts

Owns:

```text
repository layout
SKILL.md contracts
command contracts
references
scripts
tool integration
self-containment
installation
CI
technical acceptance
```

## 04 — Testing and Benchmark

Owns:

```text
deterministic checks
business reasoning rubrics
adversarial cases
progressive examples
stress tests
pack evaluation
regressions
installation
release gates
```

## 05 — Customisation / Extension Packs

Owns:

```text
pack model
business-model dimensions
activation
precedence
core effects
metrics
pack-aware evaluation
packaging
pack authoring
```

## 06 — Extension Pack Catalogue

Owns:

```text
curated initial packs
business-model profiles
selection rationale
showcases
exact prompts
pack-specific evals
maturity
```

Generate these specs from persisted research logs, not conversation memory.

**Exit:** implementation can proceed without inventing the business architecture in code.

---

# 26. Stage 19 — Design Public README and Public Claims Contract

Stage 19 designs the complete **target public product surface**. It must not turn the root README into a bootstrap diary, implementation plan, maturity report or verification log.

Use the current Production Skills public README process and family template as the governing pattern, adapted to Business Building rather than copied mechanically from another domain.

The target README structure is:

```text
# Business Building Skills
positioning and business-building capabilities
evidence / experiment / commitment control
truthful-growth and legal/ethical boundary
installation
strong Level 1 quick start with complete prompt inline
5 × 3 Learn by Building
project structure grows with the business work
substantive core-skill sections
Extension Packs
execution tools and cross-domain handoffs
evaluation / benchmark entry points
canonical stress tests
source-book lineage
documentation
boundary
contributing
licence
```

A positioning direction to test:

> Turn business ideas into evidence-backed offers, acquisition systems and viable economic models.

The README should make clear that the project is **derived from** the initial books but does not reproduce them or require users to adopt every framework they contain.

## Public-surface separation

After the target public README is designed, keep these surfaces distinct:

```text
README.md
→ public product and onboarding surface
→ explains what Business Building Skills does and how to use it


docs/research-logs/
→ bootstrap execution history
→ stage status
→ verification and maturity evidence
→ unresolved implementation/publication gates
```

Do not insert internal process language into the target README merely because later bootstrap stages have not executed.

The public README must not contain user-facing bootstrap bookkeeping such as:

```text
Stage 19 / Stage 21 / Stage N
feat/bootstrap or feat/bootstrap-2
bootstrap progress
production scaffold status
maturity promotion steps
completion commit SHAs
validator check counts
"not-run" suite bookkeeping
"this will be implemented in Stage N"
```

A real product limitation may be documented when a user needs to know it, but express the limitation in product terms rather than bootstrap-stage terms.

## Quick start and public examples

The Level 1 quick start must contain its **complete copyable prompt inline**. A link to a research log is not a quick start.

The Learn by Building progression must expose exactly five levels with three complementary primary examples per level. Once the public example surface exists, README navigation must use stable paths such as:

```text
examples/level-1-<example>/README.md
examples/level-2-<example>/README.md
```

Research logs remain the evidence for selection/design reasoning, not the primary user onboarding path.

## Skills

Every core skill needs a substantive public section explaining:

```text
what it owns
when to use it
what business decision or production problem it resolves
important evidence, preservation or legal/ethical boundaries
```

A compact table may supplement these sections but must not replace them.

## Required Stage 19 outputs

Produce three separate artefacts:

1. **Complete target README** — the exact intended public product surface.
2. **Business Building README contract** — required section order, domain control model, skills, 5 × 3 progression, public example-path rules and permitted deviations from the family template.
3. **Public claims ledger** — internal mapping from important public claims to the later evidence gate that must support them before final publication.

Example claims ledger:

| Public claim | Evidence owner / gate |
|---|---|
| canonical installation works | clean external installation validation |
| Level 1 quick start produces the promised business artefacts | proven core vertical |
| an Extension Pack changes the stated business behaviour | pack differential evaluation |
| benchmark result | executed benchmark report |
| provider/host support | tested compatibility evidence |

The claims ledger is an internal bootstrap artefact. Do not paste stage/evidence bookkeeping into the README.

During bootstrap, the target README describes the intended public product. Do not distort it to mirror intermediate stage completion. Final publication later reconciles every claim against implementation and evaluation evidence: keep supported claims, narrow partially supported claims, finish required missing evidence or remove unsupported non-essential claims.

**Research-log output:** complete target README, Business Building README contract and public claims ledger.

**Exit:** a user can understand and try the intended project without reading the internal bootstrap, and later scaffold work has an explicit preservation contract rather than permission to redesign the README.

---

# 27. Stage 20 — Cross-Project Review

Compare the independently derived architecture with:

```text
Deep Research Skills
Legal Skills
UI/UX Design Skills
Software Engineering Skills
Production Skills family
Pactwright
```

Likely boundaries:

```text
Deep Research
→ gathers and synthesises external market/customer evidence

Business Building
→ turns evidence into business choices and experiments

Legal
→ determines legal constraints

Production Skills
→ produce the product / content / artefacts

Pactwright
→ can govern authorised execution
```

Record repeated abstractions without centralising them prematurely.

Potential candidates include:

```text
assumption / evidence / decision handoff
experiment contract
constraint diagnosis
validity / confidence metadata
```

As part of this review, verify the Stage 19 README contract against current Production Skills public patterns. Confirm that the public README remains product-facing, that bootstrap/maturity evidence stays in research logs, that the claims ledger remains internal and that substantive skill/example navigation is preserved.

**Exit:** integration opportunities are recorded without turning this project into a universal business operating system, and no cross-project convention has reintroduced bootstrap mechanics into the public README.

---

# 28. Stage 21 — Scaffold Production Repository and Preserve Public README

Only now expand the Stage 0 workspace.

Likely baseline:

```text
business-building-skills/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── CHANGELOG.md
├── docs/
│   ├── 01-business-building-skills-system-spec.md
│   ├── 02-business-building-skills-workflows-and-artifacts-spec.md
│   ├── 03-business-building-skills-repository-and-contracts-spec.md
│   ├── 04-testing-and-benchmark-spec.md
│   ├── 05-business-building-customisation-packs-spec.md
│   ├── 06-business-building-extension-pack-catalogue.md
│   └── research-logs/
├── skills/
├── examples/
├── benchmarks/
├── tests/
├── tools/                 # only if justified
├── extension-packs/       # once implemented
├── integrations/          # optional
└── .github/
```

Do not create:

```text
CRM
customer database
analytics warehouse
marketing automation platform
accounting engine
```

inside this repository.

## README handoff is preservation, not redesign

Adopt the accepted Stage 19 target README and Stage 20 review findings. Stage 21 may make only mechanical publication changes required by the real repository, such as:

```text
rebase links from the Stage 19 design location to repository-root paths
replace intentional repository-name placeholders
link the selected repository licence
point to public example paths created by the scaffold
correct a factual repository path introduced by scaffolding
```

Stage 21 must not independently:

```text
change the product positioning
replace or remove the Level 1 quick-start prompt
change the five-level × three-example progression
collapse substantive skill sections into a responsibility table
introduce bootstrap-stage or maturity prose
rewrite product limitations around current bootstrap status
replace public example navigation with research-log links
```

If a substantive public-content problem is discovered, record it and reopen the owning README-design decision rather than silently redesigning the README inside scaffold work.

## Public example surface

Create usable public example navigation for all 15 primary examples. Public example files may initially contain the accepted prompt and production problem without pretending their outputs have already been executed. Later execution stages add actual outputs/evidence to the same stable public surface.

The root README should link to `examples/...` rather than requiring users to navigate bootstrap research logs.

## Deterministic README conformance

Add repository checks that fail when the public README violates its accepted contract. At minimum verify:

```text
required canonical sections and domain-approved order
complete inline Level 1 quick-start prompt
five progressive levels
exactly three primary examples per level
all primary example links resolve to public example surfaces
substantive section for every core skill
installation / Extension Packs / execution / benchmark / docs / boundary / contributing / licence surfaces
local links resolve
no internal bootstrap mechanics leak into the public product copy
```

The leakage check should reject obvious process text such as stage-number references, `feat/bootstrap`, `feat/bootstrap-2`, completion SHAs, scaffold/maturity narration and `not-run` bookkeeping in the public README.

These deterministic checks validate public structure and leakage only. They do not prove business quality or evidence for the public claims ledger.

Preserve `docs/research-logs/` as the authoritative place for bootstrap status, maturity evidence, validation receipts and unfulfilled later-stage work.

**Exit:** every production directory has a justified immediate purpose, the scaffold adopts the accepted public README without redesigning it around current bootstrap state, public examples are navigable through `examples/`, and deterministic checks protect the README contract.

---

# 29. Stage 22 — Implement and Prove Core Vertical

Implement the minimum skills/commands required for one realistic bounded business problem.

A strong first vertical:

```text
business idea
→ customer/problem assumptions
→ offer hypothesis
→ price / basic economics
→ riskiest assumption
→ cheap experiment
→ evidence
→ evaluation
→ bounded change
```

Do not begin with a large acquisition automation system.

A professional-services or small digital-product fixture is preferable because economics and delivery can be tested cheaply.

**Exit:** installed skills can move one business decision from assumption to evidence-backed action.

---

# 30. Stage 23 — Expand Progressive Coverage and Extension Packs

Expand gradually to the selected 15 examples and representative packs.

For every implemented pack prove:

```text
core works without pack
core + pack changes intended business-building behaviour
explicit project facts and approved business decisions outrank pack defaults
legal constraints outrank optimisation
pack evaluation recognises valid specialisation
pack authoring can create/revise a valid pack
```

**Exit:** the project demonstrates multiple viable business models rather than one favoured playbook.

---

# 31. Stage 24 — Validate Installation and Repository Integrity

Validate:

```text
repository contracts
skill self-containment
command discovery
selective installation
clean consumer-project installation
skill-local references/scripts/assets
tool prerequisites
benchmark entry points
example reproducibility
no undocumented source-checkout dependencies
```

Clean external installation must be distinct from source-repository tests.

**Exit:** the repository behaves as an installable Agent Skills product.

---

# 32. Stage 25 — Optional Pactwright Integration + Registry Promotion

Business Building Skills remains independently installable as required by the Production Skills family contract.

If Pactwright integration is useful, define thin compatibility bindings. Cross-domain composition with other Production Skills is a normal family capability, not evidence that this project sits outside the family.

Potential composition:

```text
Business Building Skills
→ business requirement / experiment / commercial constraint

Pactwright
→ authorised implementation Contract

Production Skills
→ product / marketing / research / legal / media execution

evidence
→ Business Building Skills evaluation
```

Business Building Skills should not own Pactwright lifecycle state.

Production Skills should not own business-model truth.

Register the project in the Production Skills registry from bootstrap as `proposed`. Promote maturity only through demonstrated evidence:

```text
proposed
→ researching
→ specified
→ scaffolded
→ working
→ benchmarked
→ mature
```

Creating the Stage 0 workspace does not by itself justify promotion beyond `proposed`.

**Exit:** Pactwright compatibility and cross-project composition work without runtime dependence, and registry status reflects demonstrated maturity.

---

# 33. Stage 26 — Review Shared-Abstraction Candidates

After implementation evidence exists, review abstractions that may generalise.

Potential candidates:

```text
assumption register
evidence-backed decision
experiment contract
constraint diagnosis
smallest-sufficient correction
```

Apply the same extraction discipline:

> Share abstractions only after multiple independent projects need substantially the same concept.

Do not create:

```text
universal business graph
universal experimentation runtime
central decision engine
universal business evaluator
```

without repeated production evidence.

---

# 34. Business-Building Acceptance Gates

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

---

# 35. Initial Non-Goals

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

---

# 36. Success Criterion

This bootstrap succeeds if later sessions can execute each stage from persisted research logs without redesigning `business-building-skills` from first principles.

The resulting project should make business-building work:

```text
more evidence-driven
more customer-grounded
more coherent across offer, acquisition and monetisation
more explicit about economics and cash
more disciplined about experiments
more resistant to vanity metrics
more truthful in growth tactics
more precise about current constraints
more capable of preserving validated decisions
more efficient to diagnose and repair
```

while translating the useful ideas from the five initial books into independently expressed, reusable business capabilities rather than five book-specific prompt collections.