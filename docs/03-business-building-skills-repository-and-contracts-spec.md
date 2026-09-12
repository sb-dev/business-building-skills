# Business Building Skills — Repository and Contracts Specification

**Contract version:** 1.0 · 12 September 2026  
**State:** Complete canonical specification; implementation and installed validation are separate gates.  
**Authority:** [Bootstrap §25](research-logs/2026-09-08-business-building-skills-new-project-bootstrap-process.md#25-stage-18--generate-six-canonical-specifications), accepted research through Stage 17 at `ff97f73866012b296bc4a142e0de6258a7906c94`.  
**Specification set:** [01](01-business-building-skills-system-spec.md) · [02](02-business-building-skills-workflows-and-artifacts-spec.md) · [03](03-business-building-skills-repository-and-contracts-spec.md) · [04](04-testing-and-benchmark-spec.md) · [05](05-business-building-customisation-packs-spec.md) · [06](06-business-building-extension-pack-catalogue.md)

Owns repository layout, portable skill and command interfaces, local resources, scripts, tool bindings, installation, CI and technical acceptance. These are complete implementation contracts. No production directory, installer or host execution is claimed to exist at Stage 18.

“Must” states a requirement; “may” permits a bounded option. Examples and authored controls remain synthetic. A specification, complete record or passing calculation does not establish customer validation, installed behaviour, professional clearance or permission for an external action. Earlier research dates, source IDs and stage references record provenance; the ownership table in specification 01 identifies the current normative document. Where an incorporated record names an earlier stage, implement its completed contract in this specification set, not a missing future design.

## 1. Repository layout and ownership

| Path | Purpose and creation gate |
|---|---|
| `README.md` | Public entry designed in Stage 19 and kept consistent with actual implementation |
| `LICENSE`, `CONTRIBUTING.md`, `CHANGELOG.md` | Authorised distribution terms, contribution/verification procedure and accurate change history at Stage 21; do not invent a licence grant |
| `docs/01…06` | These six canonical specifications, with their exact full names |
| `docs/research-logs/` | Durable source, comparison, design, verification and completion history; not a runtime dependency |
| `skills/business-build/` | Independent construction and explicit-revision installation |
| `skills/business-grow/` | Independent bounded-growth installation |
| `skills/business-evaluate/` | Independent assessment installation; does not edit its subject |
| `skills/business-pack-author/` | Independent reusable pack production installation |
| `examples/level-01/` … `examples/level-05/` | Exactly three primary cases per level; fixed prompt/input, actual outputs when run and reproduction instructions |
| `benchmarks/` | Subject inputs separated from oracles, named manifests and captured run/assessment evidence |
| `tests/` | Executable repository, formula, contract and installation checks with actual result evidence |
| `extension-packs/<name>/` | Only implemented packs; required contents are defined in specification 05 |
| `tools/` | Only a justified repository check or distribution helper used immediately; no core business runtime |
| `integrations/` | Only implemented, optional thin bindings with actual compatibility evidence |
| `.github/` | Production CI at Stage 21 onwards; scoped validation rather than commercial operations |

At Stage 18 write only the six specifications and research/progress evidence. Stage 21 creates justified production paths; no empty marker directories stand in for functionality. Never add a CRM, customer database, ad system, payment processor, analytics warehouse or accounting engine. A development checkout is not an installation.

## 2. SKILL.md contracts

Each installation unit contains a root `SKILL.md` with YAML frontmatter and a Markdown body. Required metadata is `name` (1–64 lowercase letters/digits/hyphens, matching the directory, no boundary or consecutive hyphens) and nonempty `description` (up to 1024 characters). Optional compatibility metadata describes actual prerequisites; do not list imaginary runtimes. The upstream `allowed-tools` field is experimental and host-dependent. Resource references resolve from the skill root. These format facts were checked against the [official Agent Skills specification](https://agentskills.io/specification) on 12 September 2026; they establish format, not host execution or business quality.

The following are project requirements. Keep the entry instruction focused and directly link every available command reference; load details only when needed. Include purpose/activation, non-activation and ambiguous-request handling, the command menu, permitted outputs and mutations, evidence/rights invariants, applicable self-checks, pack selection, tool prerequisites, result/error handling and focused examples. Do not require all references to be loaded for a small task. Each entry must state that a selector does not grant external authority.

The exact selected descriptions are:

```text
business-build: Frame or revise an opportunity, customer/problem/value model, offer, pricing, money model, delivery and unit economics. Identify assumptions, design a bounded business experiment, or record learning from actual supplied evidence. Use for construction and explicit revisions, not assessment-only work or live commercial execution.

business-grow: Design qualified acquisition, sales, retention, referral and expansion for an accepted or explicitly hypothetical business offer. Assess a bounded channel increase against downstream value, economics, capacity, cash and rights. Use for growth-system proposals, not automatic sending, ad buying or an unrelated business rewrite.

business-evaluate: Audit business evidence and artefacts, assess commercial and operational coherence, diagnose the current constraint, and recommend the smallest justified change. Preserve the artefact under review. Use for evaluation and repair proposals, not silent source edits, invented evidence or professional legal/tax conclusions.

business-pack-author: Research and author reusable business-model specialisations, prove the existing core or catalogue is insufficient, define changed behaviour, create showcases and evaluations, compare core with core-plus-pack, and validate a proposed catalogue entry. Use for pack production, not industry tags or ordinary business planning.
```

## 3. Skill-local references and self-containment

Use `references/<selector>.md` for each owned command, `references/core-rules.md` for mandatory common evidence/rights/authority rules, and `references/business-records.md` for the complete record meanings needed by that skill. Include `references/packs.md` for selection/precedence and access to an explicitly supplied pack. Every required resource must be reachable directly from SKILL.md. A bibliography may point outward for optional provenance; following it must not be necessary to perform the installed command on supplied facts.

The canonical specs own the editable domain contract. Distribute checked skill-local copies or focused independently expressed implementations of its required rules; do not install symlinks back into `docs/`, a sibling skill or the source repository. The common `core-rules.md` must be byte-identical in all four distributions, with its source/version recorded. Skill-specific record references may differ in coverage, but cannot weaken meaning. Maintain a file manifest with path, content hash, owning canonical section and required/optional classification. The repository verifier compares common copies and coverage; the consumer verifier walks the actual installed dependency closure. This explicit copy-and-check approach needs no new generator framework or shared runtime.

If a required resource is absent, report the missing path and block the affected command; do not fall back to undeclared checkout access. Optional unavailable research or tools leave their factual questions unresolved. Selectively installing only business-evaluate must still support its own arithmetic/evidence/rights/growth review without business-build. Each of the other three has the corresponding standalone obligation.

Templates or small fixed inputs may live in `assets/` only when actually used. No source book PDFs, raw customer databases, credentials or private transcripts belong in distribution. Preserve necessary notices and component rights; the root licence is not assumed to grant rights in third-party content.

## 4. Script and calculation contract

Add a skill-local script only for a demonstrated repeated deterministic need. It must accept explicit input paths/values and an explicit output target, validate types, units, finite numeric values, IDs and required fields, and return errors without inventing defaults. Money uses numeric strings and declared decimal precision/rounding. An undefined ratio is a typed undefined result with its count and reason, not zero. Retain formula/input/output identities and actual run status. Never execute business operations as an arithmetic side effect.

Scripts resolve their own resources from their installed location and business inputs from explicit paths; they cannot assume the process working directory is the repository. Document interpreter/library versions actually required. A read-only dry run, bounded output and no overwrite of accepted source records are the default. Host-provided calculators or an incumbent recalculating spreadsheet remain valid substitutes if HC01–HC08 is satisfied. No Python installation is required merely to read or draft business records.

Repository tests may use available Python and Decimal for fixed fixture calculations. Those tests are not an installed agent runtime or semantic benchmark. A script file's existence, a formula string and a stale spreadsheet cache are never execution receipts.

## 5. Common command interface and routing

Portable request form: `Use business-build / design-offer with this dossier`. A command is a logical task selector. No universal shell, slash-command, RPC or cross-skill invocation API is introduced. A tested host wrapper may map the same request without changing its business or mutation meaning.

Each command has exactly the nine mandatory responsibility fields: inputs; evidence required; assumptions allowed; output; allowed mutations; forbidden behaviour; metrics/evidence; failure states; legal/ethical boundaries. They follow in full. Native NC labels retain their accepted gap-analysis provenance; they are not extra commands. Original seed labels document the accepted consolidation, not additional executable aliases.

Construction, evidence strength, assessment result and action authority remain separate. Operate on supplied existing records without replaying unrelated commands. Drafts may contain labelled hypotheses; missing critical evidence blocks the dependent commitment. Evaluation writes a separate assessment. Any approved revision identifies scope and accepted version, preserves history and reviews affected dependencies. All four skills enforce their own safeguards.

Explicit modes: G02 chooses lead-magnet, outreach or content-loop; E02 chooses exactly one of opportunity, offer, pricing, money-model, channel, funnel or retention; E03 chooses economics, cash or both. Unassessed cash/economics cannot silently pass a scale decision. If a material ambiguity changes authority or subject, obtain the missing choice before mutation; a narrower assessment may state its actual scope.

## 6. business-build — 10 commands

Accepted contract: [2026-09-10-stage-13-build-command-contracts.md](research-logs/2026-09-10-stage-13-build-command-contracts.md). Domain-stage references resolve to specification 02; pack mechanics resolve to 05 and evaluations to 04.

### B01 — `frame-opportunity`

**Native responsibilities:** NC01.  
**Original §20 seeds:** `frame-opportunity`.

| Required field | Contract |
|---|---|
| inputs | The proposed initiative, accountable objective, decision horizon, operating constraints and any accepted direction. Start from supplied context; ask for a missing decision objective rather than inventing the owner’s ambition. |
| evidence required | Source-located facts about the present situation, intended actors and alternatives where available. Material current external claims require verification; absent local demand remains a question, not a fabricated opportunity. |
| assumptions allowed | Clearly labelled opportunity, segment and mechanism hypotheses may frame exploration. Uncertainty and consequence remain separate; assumptions cannot replace commitments, permissions or an asserted market-size fact. |
| output | A bounded opportunity record naming the decision, plausible alternatives including no change, relevant customer/value questions, material dependencies, evidence limits and the smallest useful next enquiry. |
| allowed mutations | Create or revise the named opportunity draft and its linked questions. Do not replace accepted business direction without explicit scope/version approval, or change unrelated customer, pricing or operating records. |
| forbidden behaviour | Treat a fashionable market, book example, generated persona or owner enthusiasm as validated demand; automatically pivot an existing business; or create an executive team to pursue the idea. |
| metrics/evidence | Traceability of each material fact and assumption to its source, actual customer/problem signals where supplied, the consequences of error and the evidence that could change the bounded decision. |
| failure states | BLOCKED when objective or a necessary authority/fact cannot be resolved; FAIL for a proposal relying on known deception or impossible obligations. An untested opportunity may remain an honest draft. |
| legal/ethical boundaries | Identify regulated, financial, data or vulnerable-customer concerns and route them under Stage 9. Framing an opportunity neither establishes legality nor authorises research participation, outreach, expenditure or public claims. |

### B02 — `define-customer-value`

**Native responsibilities:** NC01.  
**Original §20 seeds:** `define-customer`, `define-problem`, `map-value`.

| Required field | Contract |
|---|---|
| inputs | Opportunity or existing business version, intended and observed populations, material buyer/user/payer roles, desired progress, current alternatives and the exact customer, problem or value question being addressed. |
| evidence required | Relevant interviews, actual behaviour, support, sales, usage, competitive alternatives or payment evidence with source, date, population, limitations and contrary observations. An owner-declared target is not an observed customer. |
| assumptions allowed | Unresolved segment, problem-importance, mechanism and value-dimension hypotheses may be recorded separately. Do not infer purchasing authority, representativeness, economic savings or causal benefit from an unrelated proxy. |
| output | A connected customer/problem/value record preserving declared versus observed roles, alternatives, selected relevant value dimensions, supporting/challenging evidence, unknowns and downstream review triggers for a material target change. |
| allowed mutations | Write only the requested customer/problem/value draft and linked claim rows. A material accepted-target change requires explicit approval and affected-decision review; it does not automatically regenerate the offer or channel. |
| forbidden behaviour | Require every value dimension, manufacture testimonials or interview findings, count users as budget owners, or transfer old-segment evidence into a newly named population without an applicable bridge. |
| metrics/evidence | Specific observed events and attributed accounts, population/cohort definition, problem consequences, relevant baseline/outcome indicators and the evidence relationship of each benefit claim; no universal customer-fit score. |
| failure states | BLOCKED for material missing source access or role information needed by the decision; inconsistent populations invalidate the affected inference. Contradictory evidence challenges the precise claim, not automatically the entire business. |
| legal/ethical boundaries | Minimise personal data and preserve permitted-use limits. Do not infer sensitive traits or exploit vulnerability. Route material privacy, claims and professional questions without publishing private customer material or issuing legal conclusions. |

### B03 — `design-offer`

**Native responsibilities:** NC02.  
**Original §20 seeds:** `design-offer`.

| Required field | Contract |
|---|---|
| inputs | Customer/value and alternative records, requested outcome/scope, accepted offer version if any, delivery constraints, available proof, proposed price/payment structure and relevant current obligations or specialist findings. |
| evidence required | Actual capability, capacity, cost and proof sources supporting the promise; customer evidence for relevance; approved or unresolved remedy and term information. A compelling description cannot supply missing fulfilment evidence. |
| assumptions allowed | Explicitly hypothetical benefits or components may support a bounded draft or proposed test. Unsupported outcomes, invented bonus values and assumed refund capability must not appear as established customer-facing claims. |
| output | A complete bounded offer with all relevant Stage 5 components, clear inclusions/exclusions, proof limits, time-to-value, total obligation, remedy feasibility and separate relevance, economics, capacity and rights findings. |
| allowed mutations | Create or revise the named proposed offer. Replace an accepted version only under explicit scoped approval and preserve its history; publishing terms, charging customers or changing other artefacts is not included. |
| forbidden behaviour | Add obligatory bonuses or scarcity merely to complete a sales formula; conceal essential exclusions; weaken promised quality; or treat stronger conversion as permission to make an unsupported guarantee. |
| metrics/evidence | Evidence for customer progress, actual proof coverage, declared N/K/C economics, resource and dated-cash consequences, and consistency between headline, full terms and deliverable scope; no single offer score. |
| failure states | FAIL when the offer contradicts known capability, rights or truthfulness; BLOCKED for a missing material feasibility or professional finding. A labelled test hypothesis is not a passed production offer. |
| legal/ethical boundaries | Route substantiation, comparison, guarantee, refund, price and renewal issues through Stage 9. Existing rights survive revision; approval to draft an offer does not authorise public legal terms or commercial execution. |

### B04 — `design-pricing`

**Native responsibilities:** NC02.  
**Original §20 seeds:** `design-pricing`.

| Required field | Contract |
|---|---|
| inputs | Current offer, payer and pricing unit, owner objective, existing accepted price/terms, relevant alternatives, full declared costs, cash/capacity constraints and the exact level, packaging or payment question. |
| evidence required | Actual price/terms, appropriate willingness-to-pay events, dated competitor/reference evidence where material and reproducible cost/cash inputs. Distinguish a quote, deposit, completed payment, refund and hypothetical survey response. |
| assumptions allowed | Clearly labelled price, demand, usage or retention scenarios with explicit units and ranges are allowed for comparison. They cannot imply observed demand, a universal conversion threshold or automatic permission to reprice. |
| output | A bounded comparison of adequate price/unit/package/payment alternatives, including the unchanged option, with customer evidence, calculation receipts, economic/cash consequences, proof gaps and a justified proposed decision. |
| allowed mutations | Write the pricing proposal and scenario assumptions; any accepted-price revision requires exact approval and version history. Do not modify billing plans, existing subscriptions, published prices or other commercial scope. |
| forbidden behaviour | Use fabricated anchors, hidden mandatory charges or renewal terms; impose a universal premium/discount rule; invent willingness to pay; or omit labour and refund exposure to make the result attractive. |
| metrics/evidence | Actual payer choices, complete payable amounts, explicit price units, contribution and cash by declared scenario, relevant retained-customer consequences and limitations of any price-response inference. |
| failure states | BLOCKED when material cost, rights or payer/term inputs are missing; FAIL for a known misleading or infeasible structure. An undefined denominator or unexecuted formula cannot support an economic pass. |
| legal/ethical boundaries | Keep price presentation, credit/instalment, renewal, competition and tax-treatment questions with the appropriate specialist. An economic comparison is not legal approval, investment advice or authorisation to change customer obligations. |

### B05 — `design-money-model`

**Native responsibilities:** NC02.  
**Original §20 seeds:** `design-money-model`.

| Required field | Contract |
|---|---|
| inputs | Customer/value and offer versions, payer/counterparty roles, current transaction structure, retained-value assumptions, delivery mechanism, relevant cost/capacity/cash constraints and the proposed revenue-model change. |
| evidence required | Source-located transactions, collection/settlement facts, usage or repeat evidence, contractual rights and relevant operating inputs. Platform volume, third-party funds and a pending commission must not be labelled own revenue. |
| assumptions allowed | Explicit hypotheses about a new value exchange, payer, sequence or repeat behaviour may be compared. Do not assume every business needs an upsell, subscription, marketplace or multiple simultaneous revenue lines. |
| output | A coherent selected money-model account stating value exchange, payer, pricing unit, own consideration, direct cost/margin, cash timing, retention/capacity dependencies, risks and justified sequencing or rejection of extras. |
| allowed mutations | Draft or revise the named model and its scenarios. Accepted changes need scoped approval and impact review; no payment, licence grant, marketplace launch, renewal or affiliate relationship is executed. |
| forbidden behaviour | Double-count transactions across revenue labels, call pass-through funds profit, remove promised core value to manufacture an upsell, or add monetisation paths without customer-value and economic justification. |
| metrics/evidence | Canonical transaction and adjustment identities; declared gross/net consideration, direct contribution and collection timing; evidence for incremental value and repeat dependency; consistent cost and currency bases. |
| failure states | FAIL for contradicted rights or structurally incoherent obligations; BLOCKED for material unknown payer, recognition/tax treatment or cash facts. Unvalidated revenue extensions remain hypotheses, not a profitable growth forecast. |
| legal/ethical boundaries | Route licensing, principal/agent, consumer terms, financial promotions, affiliate disclosures and regulated activity as appropriate. Business modelling cannot determine accounting treatment, grant rights or commit another party. |

### B06 — `model-delivery`

**Native responsibilities:** NC04.  
**Original §20 seeds:** `model-delivery`.

| Required field | Contract |
|---|---|
| inputs | Accepted or clearly hypothetical offer, quality/acceptance criteria, actual process and dependencies, available shared resources, backlog, due dates, onboarding/support requirements and existing customer obligations. |
| evidence required | Traceable work, waiting, rework, completion, defect and customer-outcome observations; operator-confirmed resource availability and constraints. A process diagram, sale or demonstration is not repeatable fulfilment evidence. |
| assumptions allowed | Declared work-time, variation or demand scenarios can test feasibility when their uncertainty is explicit. Do not invent staff, supplier availability, customer cooperation or a universal utilisation/service-level target. |
| output | Delivery-capacity model covering flow, onboarding, time-to-value, quality, support, repeat obligations and failure demand, with per-resource headroom, due-date limits, evidence gaps and bounded intake/repair options. |
| allowed mutations | Write the delivery model and proposed adjustments only. Do not reschedule live commitments, procure resources, change customer service levels or lower accepted quality; an approved model revision retains prior obligations. |
| forbidden behaviour | Treat nominal hours as guaranteed schedulability, classify all support as waste, hide backlog/rework, infer value from completion alone, or scale sales into an unexamined resource bottleneck. |
| metrics/evidence | Actual throughput, work and waiting times, backlog conservation, per-resource load/headroom, defects and recovery, customer time-to-value and supported service-level observations; calculation receipts must state units and horizon. |
| failure states | FAIL for evidenced overload, infeasible deadlines or broken quality obligations; BLOCKED for material unavailable resource/delivery facts. A numerical upper bound is not a scheduling guarantee or successful delivery result. |
| legal/ethical boundaries | Honour existing promises and route safety, employment/contractor, data-access and sector issues. Operational owners perform delivery and containment; the skill neither hires people nor issues professional clearance. |

### B07 — `model-unit-economics`

**Native responsibilities:** NC04.  
**Original §20 seeds:** `model-unit-economics`.

| Required field | Contract |
|---|---|
| inputs | Offer and revenue-unit versions, canonical transactions/adjustments, acquisition/direct/shared cost scope, retention horizon, delivery capacity, dated obligations, usable cash and the managerial decision to be modelled. |
| evidence required | Source-located quantities, prices, costs, cohorts, collections, refund exposure and professionally supplied treatment inputs. Calculation must execute through an adequate deterministic tool and return inspectable results under Stage 7 HC01–HC08. |
| assumptions allowed | Labelled base/downside scenarios and finite retention or cost assumptions are allowed. Unknown taxes, funding, costs or collections cannot silently become zero, and a projection cannot become observed lifetime value. |
| output | Reproducible unit-economics and dated-cash model with explicit definitions, formula/input identities, contribution, acquisition/payback and retention assumptions, resource consequences, cash troughs, excluded costs and decision-limiting uncertainty. |
| allowed mutations | Create the named analytical model and scenario inputs in the authorised workspace. Do not post ledger entries, move funds, choose tax treatment or overwrite source evidence; accepted model revisions require scoped approval. |
| forbidden behaviour | Call revenue profit, compare incompatible CAC/LTV bases, count costs twice, treat stale spreadsheet caches as calculation, or label growth safe because ending cash is positive despite an earlier funding gap. |
| metrics/evidence | N, K and C on declared bases; distinct accounting bridges where supplied; CAC denominator/window, finite lifetime assumptions, payback and reversals, minimum dated usable cash/headroom and per-resource capacity checks. |
| failure states | Calculation, reconciliation or identity errors invalidate the affected result; missing critical inputs yield BLOCKED. Negative contribution or inadequate cash defeats a safe-scale claim, while a deliberately funded test remains separately labelled and authorised. |
| legal/ethical boundaries | Accounting, payroll, tax and legal findings remain attributed specialist inputs. No personal financial planning, investment recommendation, borrowing suitability judgement or autonomous commitment follows from a successful calculation. |

### B08 — `identify-assumptions`

**Native responsibilities:** NC05.  
**Original §20 seeds:** `identify-assumptions`.

| Required field | Contract |
|---|---|
| inputs | Pending decision, accepted business versions, customer/value/offer/channel/delivery/economic dependencies, existing evidence and the consequences and reversibility of the proposed commitment. |
| evidence required | Supporting and challenging records for each material dependency, with source scope and uncertainty. Evidence already sufficient for the bounded decision may remove a test need; do not fabricate a mandatory research backlog. |
| assumptions allowed | Explicit bounded assertions are allowed as assumptions, with uncertainty and consequence rated separately and reasoned prioritisation. Numeric confidence requires a justified model/data, not an invented probability or multiplied ordinal risk score. |
| output | A minimal assumption register linked to existing claims, covering applicable Stage 8 classes, owner, evidence state, consequence if wrong, priority rationale and the next discriminating evidence or review trigger. |
| allowed mutations | Create or update the requested register and links without deleting contrary evidence or changing accepted business choices. A corrected assumption retains its prior version and reason; no experiment is launched. |
| forbidden behaviour | Treat source agreement, model confidence or plan completeness as observation; prioritise trivial uncertainty above binding harm or cash; or require ten tests simply because the taxonomy has ten classes. |
| metrics/evidence | Decision relevance, scope and provenance of each assertion; independent uncertainty and consequence descriptions; explicit evidence that would change the next commitment rather than activity or document counts. |
| failure states | BLOCKED when the pending decision or material consequence is unknown and cannot be resolved from inputs. Conflicting evidence remains mixed; a consequential untestable assumption can block commitment without proving it false. |
| legal/ethical boundaries | Identify rights, consent, substantiation, professional or regulated dependencies before commercial optimisation. Missing authority cannot be treated as an assumption to test by exposing customers without approval. |

### B09 — `design-experiment`

**Native responsibilities:** NC05.  
**Original §20 seeds:** `design-experiment`.

| Required field | Contract |
|---|---|
| inputs | Exact assumption/decision versions, target role/population, accepted baseline, known evidence and rivals, feasible resources, outcome horizon and existing ethical/professional constraints. |
| evidence required | Relevant prior observations, instrumentation capability and access, actual cost/exposure limits and the information needed to change the decision. Statistical claims need an appropriate verified design, not a copied universal sample formula. |
| assumptions allowed | A bounded hypothesis and explicitly uncertain effect or mechanism may be tested. Exploratory questions must remain exploratory; provisional design assumptions cannot be presented as customer findings or unprovided launch approval. |
| output | A frozen nine-field Stage 8 experiment contract with adequate-method comparison, actual signals, guardrails, duration/sample rationale, confounders, stopping/analysis plan and distinct success, failure, invalid and inconclusive decision outcomes. |
| allowed mutations | Write or version the experiment plan with amendment history. Do not assign users, send recruitment, spend, fabricate results or silently change a frozen criterion after seeing outcomes; external execution needs separate authorisation. |
| forbidden behaviour | Choose a cheaper invalid proxy, design every outcome as success, conceal nonexistent functionality, peek with an unsupported stopping rule, or confuse a combined treatment effect with each component’s causal effect. |
| metrics/evidence | Named events and denominators, required observation maturity, practical thresholds, appropriate precision/error assumptions, validity checks and independent resource/rights guardrails; no test count is a learning metric. |
| failure states | BLOCKED for missing mandatory permissions, safeguards or an adequate feasible design; FAIL for deceptive or non-discriminating plans. No affordable adequate test permits a bounded stop, not weakened evidence requirements. |
| legal/ethical boundaries | Preserve participant truthfulness, permitted data use and existing customer rights. Qualified review owns specialist design/legal questions. Safety monitoring may stop exposure without establishing a clean completed-run effect. |

### B10 — `record-learning`

**Native responsibilities:** NC05.  
**Original §20 seeds:** none; added to close the required Stage 8 learning loop.

| Required field | Contract |
|---|---|
| inputs | Original assumption and frozen test versions, actual execution/evidence receipts, deviations and stop events, validated measures or findings, relevant review and the owner’s stated or still-pending next decision. |
| evidence required | Actual source records and returned tool/operator results, including negative, missing and adverse observations. Keep synthetic fixtures labelled; a plan, attempted operation or draft narrative cannot count as an executed test. |
| assumptions allowed | Interpretive hypotheses about causes and transfer may remain explicitly uncertain. Do not retrofit the original prediction, infer unobserved outcomes or turn a reasonable operational decision into evidence that the hypothesis is true. |
| output | An eight-field Stage 8 learning record linking assumption, test, observed evidence, result, interpretation, decision, remaining unknowns and next experiment/commitment, with preserved history and affected-decision review. |
| allowed mutations | Append the named learning entry and correction links only. Do not rewrite raw evidence or the frozen plan, erase failed tests, mark unapproved decisions accepted, or execute the proposed next commitment. |
| forbidden behaviour | Report activity as learning, suppress inconclusive results, reuse discovery data as independent confirmation, change thresholds after results or claim an installed-agent/customer outcome from a synthetic design check. |
| metrics/evidence | Observed counts, units, cohort/window, missingness, calculation identity and guardrail events, plus the precise change in decision-relevant knowledge and scope; no universal learning-velocity score. |
| failure states | Incomplete or uninterpretable evidence produces a qualified record, not invented success. BLOCKED applies to a commitment requiring absent evidence/authority; an observed guardrail breach is retained even when other results are invalid. |
| legal/ethical boundaries | Keep evidence in authorised custody and disclose only permitted extracts. Carry forward applicable rights, recovery obligations and specialist constraints; recording a result does not grant new contact, data or spending authority. |

## 7. business-grow — 8 commands

Accepted contract: [2026-09-10-stage-13-grow-command-contracts.md](research-logs/2026-09-10-stage-13-grow-command-contracts.md). Domain-stage references resolve to specification 02; pack mechanics resolve to 05 and evaluations to 04.

### G01 — `select-channel`

**Native responsibilities:** NC03.  
**Original §20 seeds:** `define-demand`, `select-channel`.

| Required field | Contract |
|---|---|
| inputs | Accepted or explicitly hypothetical customer/value/offer, owner growth objective, relevant buying context, existing channel evidence, delivery/economic constraints and the bounded reach or demand question. |
| evidence required | Suitable audience access, actual exposure/response, qualification and downstream outcomes where available; current platform/market facts must be verified when material. A catalogue or search-volume estimate is not local demand. |
| assumptions allowed | Channel, demand and reach hypotheses may be compared under explicit uncertainty. Do not assume permission to contact, full audience accessibility, stable marginal CAC or that every business needs every channel. |
| output | A demand/channel account and selected bounded channel hypothesis, compared with adequate alternatives and no change, including audience fit, sales path, cost/effort, downstream quality, constraints and the next test. |
| allowed mutations | Write the named selection proposal and evidence links only. Preserve a working accepted channel unless implicated; no audience upload, contact purchase, ad launch or customer/offer revision is performed. |
| forbidden behaviour | Pick the largest audience or lowest cost per lead without suitability and retained economics; invent acquisition data; launch all channels; or treat a provider’s access feature as permission. |
| metrics/evidence | Actual reach and suitable progression, fit/intent/qualification, attributed versus incremental cost, sales effort and delay, retained contribution/cash and resource constraints under compatible cohorts and windows. |
| failure states | BLOCKED when material access, evidence or authority is missing; FAIL for incompatible or deceptive acquisition mechanisms. An untested plausible channel remains a proposed test, not a winning acquisition system. |
| legal/ethical boundaries | Apply Stage 9 contact, data, claim, incentive and platform constraints to the actual audience and purpose. Channel strategy neither grants consent nor authorises public messages, spending or regulated promotions. |

### G02 — `design-acquisition`

**Native responsibilities:** NC03.  
**Original §20 seeds:** `design-lead-magnet`, `design-outreach`, `design-content-loop`.

| Required field | Contract |
|---|---|
| inputs | A selected mode of lead-magnet, outreach or content-loop; customer/offer/channel versions; intended response and qualification; truthful proof; cost/capacity limits and the specific asset or sequence needing a brief. |
| evidence required | Evidence of the audience’s actual need and access context, approved claim/term boundaries, existing relevant response/downstream outcomes and mode-specific facts listed below. No generated testimonial or assumed permission is evidence. |
| assumptions allowed | The response mechanism, useful topic or sequence may be a labelled hypothesis. No assumed conversion lift, consent, free-to-paid cross-subsidy, automatically available asset or validated customer list may enter as fact. |
| output | A mode-specific acquisition brief connecting useful value, accurate proposition, voluntary next step, qualification, sales handoff, measurement, cost and rights guardrails. Content production or delivery is separately owned. |
| allowed mutations | Draft or revise the requested brief and planned measurement only. Do not publish assets, send outreach, operate a recurring scheduler, collect personal data or replace accepted offer terms. |
| forbidden behaviour | Hide a sale behind a purported neutral study, use fabricated scarcity/proof, make lead count the sole success criterion, or turn a content-loop plan into autonomous repeated publishing or spam. |
| metrics/evidence | Mode-specific suitable response and qualified progression, content/production and sales effort, actual downstream purchase/value evidence, observation windows and guardrail outcomes; raw views or opens are not sufficient intent evidence. |
| failure states | BLOCKED for missing selected mode, material audience/proof facts or required approval; FAIL for a misleading or harmful mechanism. An approved brief is not an executed campaign or demonstrated acquisition effect. |
| legal/ethical boundaries | Preserve purpose-specific data/contact limits, transparent material terms and truthful participation. Route consent, incentives, substantiation, vulnerable-user and regulated-message questions; external production/sending remains separately authorised. |

**Explicit modes.** Select the applicable mode deliberately; this table adds mode-specific obligations rather than replacing the nine fields.

| Mode | Required behaviour and evidence |
|---|---|
| `lead-magnet` | Specify the genuine standalone value, eligibility, production/delivery cost, requested data, disclosure and a qualification step aligned with the paid exchange. A download is not a qualified customer or proof that free users will pay. |
| `outreach` | Specify actual recipient class, relationship, permissible contact basis, message purpose, proof, bounded cadence, suppression/opt-out handling and buyer-agreed next step. The brief contains no send authority or evasion of limits. |
| `content-loop` | Specify audience questions, evidence/proof inputs, asset brief, distribution hypothesis, production cadence, response and feedback review. The loop is a proposed workflow, not an installed scheduler or permission to publish indefinitely. |

### G03 — `design-referral-loop`

**Native responsibilities:** NC03.  
**Original §20 seeds:** `design-referral-loop`.

| Required field | Contract |
|---|---|
| inputs | Accepted offer and delivered-value evidence, relevant customer or partner population, proposed recommendation mechanism, incentives, eligibility, ownership, acquisition cost and capacity/cash limits. |
| evidence required | Actual appropriate recommendations, introductions and resulting suitable customers where available, plus partner/permission facts and incentive obligations. Friendly statements or hypothetical advocacy do not establish incremental demand. |
| assumptions allowed | A referral motive, reward response or partner fit may be an explicit hypothesis. Do not assume all satisfied customers refer, every introduction is qualified or incentive-funded volume is economical. |
| output | A bounded referral/partner-loop proposal defining value, parties, eligibility, incentive/disclosure, qualifying events, cost/attribution, buyer handoff, downstream measurement and conditions for testing, retaining or rejecting it. |
| allowed mutations | Draft the named referral brief and analytical assumptions. Do not contact partners, enrol customers, pay rewards, share data or bind the business to a partnership without separately authorised execution. |
| forbidden behaviour | Buy fake advocacy, conceal material incentives, count the same sale under several channels, presume access to a customer’s contacts or overlook the work and obligations created by reward-driven volume. |
| metrics/evidence | Defined introduction, qualified lead and paid-customer events; unique transaction attribution; incentive and sales cost; retained contribution, refunds and capacity, with appropriate periods and uncertainty. |
| failure states | FAIL for fabricated proof or conflicting incentives/obligations; BLOCKED for missing material rights, payout or partner facts. A planned loop cannot be counted as actual referrals or earned revenue. |
| legal/ethical boundaries | Route endorsement, competition, data-sharing and contact questions to appropriate reviewers. Genuine customer choice and truthful incentive disclosure remain independent of conversion or revenue, and approved plans do not authorise transfers. |

### G04 — `design-sales-path`

**Native responsibilities:** NC03.  
**Original §20 seeds:** `design-sales-path`.

| Required field | Contract |
|---|---|
| inputs | Customer/buyer roles, accepted offer/terms, channel and qualification context, actual purchasing tasks, ownership and time/capacity constraints, plus the current path or bounded new-path hypothesis. |
| evidence required | Source-located buyer actions, objections, approvals, handoffs and won/lost/open outcomes with cohort age. CRM stage names, seller activity or a signed interest form cannot substitute for actual economic authority and purchase. |
| assumptions allowed | The expected progression or unresolved buying requirements may be hypotheses. Do not assign invented win probabilities, budget authority, guaranteed close dates or a single enterprise process to all customers. |
| output | A suitable self-serve, assisted, consultative, enterprise, inbound/outbound, marketplace or partner path with entry/qualification, buyer tasks, truthful proof, seller ownership, next actions and downstream obligations. |
| allowed mutations | Write or revise the proposed sales-path record. Do not mutate CRM opportunities, negotiate binding terms, schedule contacts or alter accepted offer, pricing or customer commitments through this design command. |
| forbidden behaviour | Force every refusal into an objection to overcome, fabricate urgency, conflate message/offer/execution defects, count seller touches as buyer progress or pressure a user without purchasing authority. |
| metrics/evidence | Qualified progression, actual buyer-agreed actions, close/defer/loss reasons, cohort-aware conversion, sales effort and time-to-close, with delivery capacity and cost consequences retained. |
| failure states | BLOCKED for unresolved material roles, terms or approval requirements; FAIL for coercive or misleading paths. An immature sales cohort remains open/inconclusive rather than proof of failure or success. |
| legal/ethical boundaries | Carry approved claims, full material terms, contact permissions and specialist constraints through every handoff. Sales operators own communication and agreements; this skill does not bind a client or approve regulated activity. |

### G05 — `improve-conversion`

**Native responsibilities:** NC03, NC06.  
**Original §20 seeds:** `improve-conversion`.

| Required field | Contract |
|---|---|
| inputs | A bounded conversion symptom, accepted audience/offer/price/path versions, current objective, observed funnel and evidence about message comprehension, trust, technical function, buyer requirements and downstream economics. |
| evidence required | Compatible event/cohort data, source definitions, buyer or user observations, known defects, and rival explanations such as audience mix or outcome delay. A lower percentage alone does not identify the cause. |
| assumptions allowed | A specific proposed cause and improvement may remain an explicit hypothesis with a discriminating test. No invented lift, universal benchmark, automatic repricing or assumption that all non-buyers are unsuitable is allowed. |
| output | A smallest-sufficient conversion proposal identifying the supported/provisional layer, alternatives, preserved decisions, affected obligations, expected evidence and a bounded experiment or technical/operational handoff. |
| allowed mutations | Draft the targeted proposal and test brief only. A live checkout/content/price change needs its actual owner and approval; do not edit the accepted source artefact merely to improve the displayed conversion. |
| forbidden behaviour | Treat conversion lift as proof of value or acceptability, hide fees or cancellation, reset timers, invent testimonials, or redesign the customer, offer and brand when a local technical defect explains the symptom. |
| metrics/evidence | Actual eligible progression and informed completion, comprehension/error signals, effect size and uncertainty where adequately estimated, downstream contribution/retention and independent quality, cash and rights guardrails. |
| failure states | FAIL for known deceptive or adverse trade-offs; BLOCKED for missing material evidence or authority; inconclusive diagnoses remain qualified. A verified defect can justify a bounded repair without inventing a causal growth estimate. |
| legal/ethical boundaries | Preserve truthful choice, accessibility-relevant requirements, existing terms and applicable specialist findings. Route data, claims and consumer concerns; professional/production owners implement approved changes rather than the optimiser granting itself permission. |

### G06 — `design-retention`

**Native responsibilities:** NC03, NC04.  
**Original §20 seeds:** `design-retention`.

| Required field | Contract |
|---|---|
| inputs | Accepted customer/offer/renewal terms, relevant subscription or repeat mechanism, mature and immature cohorts, actual delivered-value and exit evidence, support/cost/capacity context and the specific retention problem. |
| evidence required | Defined use/outcome, repeat/renewal, payment failure, cancellation, refund and customer accounts with role and observation windows. Continued billing or high expansion does not establish satisfaction or active preference. |
| assumptions allowed | A value, onboarding, billing or fit explanation and bounded retention intervention may remain hypotheses. Do not assume predicted churn implies treatment response, inactivity means permanent exit, or discounts always produce profitable retention. |
| output | A bounded retention/renewal proposal tied to the evidenced cause and continuing value, with lawful customer exit, operational remedy, intervention cost, measured signals, uncertainty and a justified test/no-change decision. |
| allowed mutations | Draft the proposed retention process and analytical assumptions. Do not change renewal/cancellation terms, stop legitimate exits, apply discounts, collect charges or contact customers without the relevant approved execution. |
| forbidden behaviour | Hide cancellation, exploit forgotten billing, count new acquisition as cohort retention, erase departed customers through expansion metrics, or omit continuing support/delivery cost from an apparent retention win. |
| metrics/evidence | Explicit eligible cohort retention, gross/net revenue retention when appropriate, repeat behaviour, value/use, involuntary loss, refunds and intervention contribution/cash under matched periods and units. |
| failure states | FAIL for obstruction or known value/rights conflicts; BLOCKED for material missing cohort, intervention-cost or specialist inputs. Immature follow-up remains inconclusive and cannot support long-term lifetime assumptions. |
| legal/ethical boundaries | Apply actual renewal, cancellation, refund, data and contact constraints from Stage 9. Customer rights remain intact during recovery, and a business review cannot grant billing authority or a legal determination. |

### G07 — `design-expansion`

**Native responsibilities:** NC03, NC04.  
**Original §20 seeds:** `design-expansion`.

| Required field | Contract |
|---|---|
| inputs | Current accepted entitlements and customer roles, evidence of an additional need, proposed upsell/cross-sell/usage or scope change, price/terms, marginal delivery effort and economic/cash constraints. |
| evidence required | Customer-specific or appropriately scoped incremental-value evidence, actual acceptance/payment signals where available and cost/capacity facts. Existing payment alone does not show demand for another component or greater usage. |
| assumptions allowed | The incremental need, acceptance or workload may be an explicit hypothesis. Do not assume expansion is always beneficial, move previously promised value behind a new paywall or invent revenue from unaccepted offers. |
| output | An optional incremental-value expansion proposal with scope, payer, explicit acceptance, marginal cost/capacity/cash, retained-rights analysis and evidence that would support, challenge or bound the change. |
| allowed mutations | Create or revise the proposed expansion record only. Do not upgrade accounts, impose recurring charges, alter current entitlements, change contracts or initiate customer communication through this design command. |
| forbidden behaviour | Manufacture dependency, double-count renewal and expansion, treat higher billing as delivered value, conceal usage exposure or sell additional work that the business cannot fulfil at the promised quality. |
| metrics/evidence | Incremental accepted scope and actual retained contribution, expansion/contraction on the same starting cohort, marginal service/support cost, capacity/headroom, payment timing and customer-value signals. |
| failure states | FAIL for loss of existing rights, unsupported benefit or unfulfillable scope; BLOCKED for material unknown need, price acceptance or costs. A proposed upsell remains unvalidated even when the existing offer is successful. |
| legal/ethical boundaries | Retain informed choice and full material terms; route contract, pricing, renewal, financial-promotion or sector-specific issues. Separate business rationale from the actual authorisation to upgrade, charge or change entitlements. |

### G08 — `scale-channel`

**Native responsibilities:** NC03, NC04, NC07.  
**Original §20 seeds:** `scale-channel`.

| Required field | Contract |
|---|---|
| inputs | Exact proposed volume/spend and timing, accepted channel/offer/customer versions, marginal acquisition evidence, delivery resources, retained economics, usable cash and current action authority. |
| evidence required | Adequate evidence for all relevant Stage 7 GG01–GG07 gates, with matched source/cohort/definition and actual marginal constraints. Historical average CAC, positive revenue or a provider forecast alone is insufficient. |
| assumptions allowed | Transparent bounded downside and marginal-response scenarios may inform a recommendation; untested critical assumptions cannot be converted into a scale pass. A funded experiment must remain distinct from profitable ongoing growth. |
| output | A bounded retain, reduce, test, reject or propose-increase decision, with every independent gate, affected constraints, preserved choices, exact limit, stop/review trigger and required owner/operator approvals. |
| allowed mutations | Write the scale assessment/proposal and explicit assumptions. Do not modify budgets, campaigns, hiring, infrastructure, purchase orders or accepted customer commitments; external execution is a separate authorised operation. |
| forbidden behaviour | Average away a failed rights, cash or capacity gate; invent constant marginal economics; call an acknowledged ad request completed; or use the command name as permission to spend or grow automatically. |
| metrics/evidence | Qualified incremental customer outcomes, full scoped acquisition and service costs, retained contribution, per-resource headroom and dated cash under adequate horizons/downside, plus gate-specific evidence and uncertainty. |
| failure states | Any material unresolved gate yields BLOCKED; a known gate violation yields FAIL for the proposed increase. A justified no-change or reduced-scope proposal is valid; it is not a claim the whole business has failed. |
| legal/ethical boundaries | Verify truthful claims, current applicable constraints and exact action authority independently. No scale result authorises contact, spend, revised terms, regulated promotions or an irreversible obligation outside its approved scope. |

## 8. business-evaluate — 7 commands

Accepted contract: [2026-09-10-stage-13-evaluate-command-contracts.md](research-logs/2026-09-10-stage-13-evaluate-command-contracts.md). Domain-stage references resolve to specification 02; pack mechanics resolve to 05 and evaluations to 04.

### E01 — `audit-customer-evidence`

**Native responsibilities:** NC01, NC07.  
**Original §20 seeds:** `audit-customer-evidence`.

| Required field | Contract |
|---|---|
| inputs | The bounded customer/problem/value claim, intended and observed populations, buyer/user/payer roles, accepted source versions, available evidence locators and the question the assessment must resolve. |
| evidence required | Authorised observations and attributed accounts with recruitment, sample or exposure, collection dates, exclusions and contrary findings. Check whether a record actually supports the exact claim rather than relying on a bibliography or generated persona. |
| assumptions allowed | The assessment may preserve explicitly labelled hypotheses and identify untested mechanisms. It may not invent missing interviews, infer purchasing authority from a title, or extend one population’s evidence to another without justification. |
| output | An assessment-only evidence account with supports, challenges or unresolved findings for each material claim, provenance and relevance limits, required additional evidence, protected versions and a bounded next recommendation. |
| allowed mutations | Create a separate assessment or review record and append corrections to that assessment with history. Do not edit the customer/value dossier, overwrite source observations, approve a new target or mutate any customer record. |
| forbidden behaviour | Upgrade owner beliefs or synthetic examples into customer facts, discard unsuitable or negative cases, count dependent sources as independent validation, or silently replace the assessed claim with a weaker one. |
| metrics/evidence | Traceability, relevance to the stated role/population/context, observation maturity, evidence independence, sampling and missingness limits, and whether the actual decision remains justified. No universal evidence score or invented confidence percentage. |
| failure states | FAIL when an asserted conclusion contradicts its evidence or fabricates proof; BLOCKED when material sources or permissions are absent. Legitimate hypotheses can remain unresolved without falsely declaring the entire business unviable. |
| legal/ethical boundaries | Respect source access and permitted use; use minimal controlled locators rather than publishing personal transcripts. Route privacy, vulnerable-user, claim or regulated questions to the appropriate reviewer; audit status is not legal clearance. |

### E02 — `evaluate-component`

**Native responsibilities:** NC01, NC02, NC03, NC04, NC06, NC07.  
**Original §20 seeds:** `evaluate-opportunity`, `evaluate-offer`, `evaluate-pricing`, `evaluate-money-model`, `evaluate-channel`, `evaluate-funnel`, `evaluate-retention`.

| Required field | Contract |
|---|---|
| inputs | Exactly one declared mode: opportunity, offer, pricing, money-model, channel, funnel or retention; the bounded decision, corresponding accepted artefact/version, owner objective, relevant evidence and preserved dependencies. |
| evidence required | The mode-specific evidence defined below plus common provenance, actual definitions, dates, counter-evidence and relevant economics/rights constraints. An artefact can be assessed as an explicit hypothesis; missing proof cannot be treated as a passed commitment. |
| assumptions allowed | Explicit forecasts or assumptions may be examined as assumptions and tested for consequences. Do not silently complete missing material inputs, infer universal benchmarks, or change the question to fit the information available. |
| output | A mode-labelled assessment with separate quality/evidence findings, supported defects, unresolved questions, responsible layer, preserved decisions and bounded recommendations. Every conclusion links to the actual assessed version and evidence scope. |
| allowed mutations | Write the assessment and proposed review questions only. Never rewrite the assessed opportunity, offer, price, money model, channel, funnel or retention process; changes require a separately requested authoring task and applicable approval. |
| forbidden behaviour | Use a generic persuasive score instead of the mode’s required judgement, average rights/cash blocks into a pass, apply a mode with no identified subject, invent customer results or broaden a local finding into a whole-business pivot. |
| metrics/evidence | Use the mode-specific measures below with clear units, cohort/windows, uncertainty and independent constraints. Compare against the actual objective and unchanged alternative, not an arbitrary universal startup, price or growth target. |
| failure states | Unknown or conflicting mode is an input error; unresolved material dependencies are BLOCKED; contradicted claims or known prohibited conduct are FAIL. An inconclusive evidence result remains separate from a no-change or stop recommendation. |
| legal/ethical boundaries | Consume applicable Stage 9 findings and current action boundaries. A favourable commercial assessment does not authorise publication, contact, billing, spend or professional conclusions; legitimate existing customer obligations remain protected. |

**Explicit modes.** Select the applicable mode deliberately; this table adds mode-specific obligations rather than replacing the nine fields.

| Mode | Required behaviour and evidence |
|---|---|
| `opportunity` | Inspect owner objective, target roles, problem importance, alternatives and evidence of reachable demand together with feasible value/economics dependencies. Assess the bounded opportunity and its next adequate test; no market-size or product-market-fit claim from enthusiasm alone. |
| `offer` | Inspect the exact outcome, scope, mechanism, deliverables, price/payment terms, proof, exclusions and remedies against actual delivery/cost/cash capacity. Optional bonuses or guarantees are not mandatory. Reject unsupported promises without inventing a new offer. |
| `pricing` | Inspect payer, unit, package, total obligation, payment/renewal presentation, actual willingness-to-pay context and relevant cost/value alternatives. Distinguish survey preferences from purchases and price changes from earned revenue; assess a justified bounded option, not an automatic increase. |
| `money-model` | Inspect value exchange, payer, pricing unit, canonical transactions, revenue tags, costs, retention/capacity dependency and collection dates. Reconcile pass-through funds, duplicate revenue and existing entitlements; a new revenue line must have its own value and economic basis. |
| `channel` | Inspect suitable reach, contact purpose/permission, source mix, qualification, actual buyer progression, full acquisition effort and downstream retained economics. Differentiate attribution from incrementality and historical average performance from marginal scale; preserve an effective incumbent where adequate. |
| `funnel` | Inspect event definitions, identities, matched population and maturity, qualification, informed buyer tasks, technical faults and handoffs. Distinguish message, offer and sales execution. Missing or immature events do not prove leakage or a cause for repricing. |
| `retention` | Inspect eligible starting cohorts, use/value, repeat/renewal/payment, cancellation/refund and reactivation semantics with costs and intervention evidence. Separate voluntary value from continued billing; new acquisition and expansion cannot erase exits or prove treatment responsiveness. |

### E03 — `evaluate-unit-economics`

**Native responsibilities:** NC04, NC07.  
**Original §20 seeds:** `evaluate-unit-economics`, `evaluate-cash-risk`.

| Required field | Contract |
|---|---|
| inputs | The specific operating commitment and accepted model/version, scope economics, cash or both, source-located inputs, units/cohorts/windows, cost and revenue definitions, and actual or proposed obligation dates. |
| evidence required | Reproducible HC01–HC08 calculation input/output evidence, canonical cost/adjustment identities, appropriate retention/CAC/LTV assumptions, resource limits and dated usable cash. Critical missing professional treatment or future obligations remain explicit. |
| assumptions allowed | Labelled scenarios and sensitivity assumptions may be reviewed, not asserted as observations. No invented conversion, retention, tax, exchange rate, funding or constant marginal-cost assumptions may produce a scale pass. |
| output | An assessment separating declared commercial contribution, accounting bridges where supplied, acquisition/retention implications, resource feasibility and dated cash findings. State exclusions, invalid calculations, uncertainty and the exact commitment that is supported, rejected or blocked. |
| allowed mutations | Create the assessment and a proposed correction to an input or calculation only. Do not overwrite the source model, select accounting/tax treatment, post ledger entries, move funds or revise accepted prices and payment terms. |
| forbidden behaviour | Call revenue profit, call a partial residual net profit, count the same cost twice, accept LTV/CAC without scope/windows, or let a positive margin or ending balance hide an earlier cash deficit. Never average economic and cash findings. |
| metrics/evidence | Matched N, K, C and declared acquisition/shared costs; denominator validity, retention horizon and payback; per-resource capacity; minimum dated usable cash and headroom against obligations/floor over an adequate horizon and downside. |
| failure states | FAIL for erroneous or contradictory conclusions and known unfunded proposed commitments; BLOCKED for material missing definitions, source access, calculation or specialist inputs. Undefined ratios remain undefined, not zero or infinite safety. |
| legal/ethical boundaries | Accounting systems and qualified professionals own treatment and filings; operational business analysis is not investment or personal financial advice. Preserve refund rights, restrictions on funds and exact owner authority for any later action. |

**Explicit modes.** Select the applicable mode deliberately; this table adds mode-specific obligations rather than replacing the nine fields.

| Mode | Required behaviour and evidence |
|---|---|
| `economics` | Assess the declared unit, consideration, relevant cost and retention/acquisition assumptions. Cash need not receive a numerical verdict when outside the supplied assessment scope, but explicitly unassessed cash must block a safe-scale recommendation that depends on it. |
| `cash` | Assess actual payment dates, usable versus restricted balances, existing/proposed commitments and adequate horizon/downside. Do not infer profit from positive cash; unassessed contribution or capacity cannot silently become passed growth gates. |
| `both` | Return separate economics and cash findings with any bridges and independent blocks. Either adverse or unresolved relevant finding can block the proposed commitment; no combined score offsets one with the other. |

### E04 — `evaluate-experiment`

**Native responsibilities:** NC05, NC07.  
**Original §20 seeds:** `evaluate-experiment`.

| Required field | Contract |
|---|---|
| inputs | A plan-only or completed-test assessment request, exact assumption and frozen contract version where it exists, pending decision, target population, signals, guardrails and available execution/learning records. |
| evidence required | For plan review inspect all nine Stage 8 contract fields and feasible methods. For results inspect actual exposure, assignment/analysis settings, source events, deviations, stopping conditions, maturation, calculations and adverse evidence; a written plan is not an executed test. |
| assumptions allowed | Exploratory findings and declared forecast/model assumptions may be examined with their limits. Do not reconstruct a missing prespecified rule as though it existed, or promote an exploratory hypothesis into independent confirmation. |
| output | An assessment of falsifiability, adequacy, validity, signals and learning/action consequences, with plan versus executed evidence clearly separated. Retain supported, challenged, inconclusive, uninterpretable and guardrail-stop findings within their scope. |
| allowed mutations | Write a separate assessment and proposed design/measurement corrections. Do not change the frozen plan, rewrite observations, assign users, rerun external exposure, amend customer terms or record a test as completed without actual execution evidence. |
| forbidden behaviour | Treat every outcome as success, infer equivalence from non-significance, ignore confounders or multiple changes, peek with an invalid stopping rule, or use a favourable primary signal to override a known guardrail breach. |
| metrics/evidence | Relevant observable outcomes, units and denominators, effect/uncertainty when supported, design/measurement integrity, outcome maturity and whether results could change the actual decision. Activity count is not learning. |
| failure states | An all-success rule or known invalid claim is FAIL; missing material design/execution evidence is BLOCKED; valid but insufficient information is inconclusive. A known breach requires containment even before the intended inference is resolved. |
| legal/ethical boundaries | Respect participant information, permitted data, customer rights and approved exposure/budget. Route statistical or legal questions where necessary; model evaluation neither authorises another test nor supplies professional clearance. |

### E05 — `audit-claims`

**Native responsibilities:** NC07.  
**Original §20 seeds:** `audit-claims`.

| Required field | Contract |
|---|---|
| inputs | The exact proposed or published words and implied representations, medium/audience, offer and product versions, evidence, terms, actual service behaviour and applicable specialist findings or policies. |
| evidence required | Original substantiation, genuine experience and permissions for proof, actual scarcity/urgency facts, complete price/renewal/remedy terms and current reviewed constraints. Compare wording with the real operation rather than accepting a policy document as proof. |
| assumptions allowed | Unverified factual or legal propositions remain explicit questions. No synthetic customer, expected ROI, invented deadline or presumed exemption can be accepted as claim support; legitimate hypotheses must be presented honestly as such. |
| output | An issue-by-issue claim assessment distinguishing project truthfulness, applicable legal constraints and action authority, plus a bounded Stage 9 handoff and smallest-sufficient correction proposal preserving existing obligations. |
| allowed mutations | Create an assessment and proposed wording/behaviour changes separately from the source claim. Do not publish, edit live assets, delete adverse records, issue legal opinions or silently cancel existing customer entitlements. |
| forbidden behaviour | Approve false scarcity, fabricated proof, unsupported returns, hidden renewal, misleading trials, spam, obstructed cancellation or fake guarantees because conversion improved. A disclaimer cannot silently cure a contradicted headline. |
| metrics/evidence | Claim-to-evidence and claim-to-behaviour consistency, qualification visibility, source/currentness scope, satisfied review conditions and independent approval. No conversion, revenue or universal compliance score substitutes for these findings. |
| failure states | FAIL for established fabrication, contradiction or known prohibited conduct; BLOCKED for material missing facts, applicability or review. Genuine bounded claims can pass without requiring a new opinion for every repetition of a valid policy. |
| legal/ethical boundaries | Legal Skills and qualified reviewers own legal research/conclusions; preserve jurisdiction, effective dates, conditions and reviewer remit. Owner permission is separate from specialist constraints and cannot waive rights or professional authority. |

### E06 — `diagnose-business-constraint`

**Native responsibilities:** NC06, NC04, NC07.  
**Original §20 seeds:** `diagnose-business-constraint`.

| Required field | Contract |
|---|---|
| inputs | The owner’s actual objective, bounded next improvement and horizon, accepted business versions, observed symptom, source evidence, resource/economic dependencies and existing commitments. |
| evidence required | Compatible definitions, cohorts, periods and source identities, plausible rival explanations, actual resource/cash/quality limits and observations capable of distinguishing causes. Use existing analytical findings with their limitations, not an arbitrary score ranking. |
| assumptions allowed | A candidate cause may remain a working hypothesis or an inconclusive diagnosis. No missing metric is zero, no smallest conversion rate proves a bottleneck, and no highest activity/resource utilisation establishes causality by itself. |
| output | An evidence-qualified supported or provisional constraint finding with appropriate CT routes, rivals, scope/consequence, what would improve if relieved, possible next constraints, preserved decisions and a bounded repair or discriminating-test recommendation. |
| allowed mutations | Write the diagnosis assessment and proposed next investigation. Do not alter customer, offer, pricing, channel, systems or operations; identifying a possible cause does not authorise a corrective mutation. |
| forbidden behaviour | Optimise every metric simultaneously, force one cause when several constraints bind, infer business failure from a logging defect, or prescribe a whole-business pivot while accepted evidence still supports unaffected layers. |
| metrics/evidence | Evidence integrity, objective relevance, discriminating observations, actual headroom/obligations and conditional improvement under the stated mechanism. Retain separate quality, cash, authority and uncertainty findings rather than one bottleneck score. |
| failure states | BLOCKED or inconclusive when evidence cannot discriminate the candidates; FAIL for unsupported causal certainty or broad repairs. Known harm or an unfunded commitment may require authorised containment without claiming a complete diagnosis. |
| legal/ethical boundaries | Rights, truthfulness and authority constrain every route. Professional/operational owners supply missing treatment or execution facts; a diagnostic label does not make a legal, investment or accounting conclusion. |

### E07 — `recommend-smallest-change`

**Native responsibilities:** NC06, NC07.  
**Original §20 seeds:** `recommend-smallest-change`.

| Required field | Contract |
|---|---|
| inputs | A supported/provisional diagnosis, exact accepted versions and obligations, proposed objective, viable no-change/local/coupled alternatives, available evidence and relevant resource, cash and authority constraints. |
| evidence required | Evidence implicating each proposed changed layer and reasons a smaller correction cannot suffice, with dependency/impact review and expected verification. Retain contrary findings and actual customer entitlements rather than only the preferred plan. |
| assumptions allowed | A proposed repair mechanism may remain an explicit hypothesis requiring a bounded test. A coupled change is allowed only with a reasoned dependency basis; uncertainty does not permit regenerating every convenient artefact. |
| output | A complete RR01–RR08 repair proposal: responsible layer, smallest sufficient change, preserved versions/rights, impact dispositions, owner/approval, resource/reversibility limits, verification rule and learning/regression handoff. |
| allowed mutations | Write the proposal and assessment of alternatives only. Do not apply the repair, replace accepted artefacts, mutate production state or mark another discipline’s implementation complete; separate execution requires its own authority and evidence. |
| forbidden behaviour | Change unimplicated customer/offer/brand/price decisions, lower quality criteria to pass, preserve unsafe/deceptive choices merely because previously approved, or invent rollback rights for irreversible external actions. |
| metrics/evidence | Scope of implicated versus preserved layers, discriminating before/after evidence, relevant guardrails and whether the repair satisfies the actual objective. A smaller textual diff alone is not proof of a sufficient or responsible change. |
| failure states | FAIL for an ungrounded broad change or rights violation; BLOCKED for material missing diagnosis, approval or feasibility. No change, containment, a bounded test or a justified coherent bundle can each be an appropriate proposal. |
| legal/ethical boundaries | Preserve specialist constraints, customer rights and approval boundaries while comparing repairs. Route implementation to the actual owner; financial or legal work remains with the qualified reviewer, not the evaluator. |

## 9. business-pack-author — 7 commands

Accepted contract: [2026-09-10-stage-13-pack-command-contracts.md](research-logs/2026-09-10-stage-13-pack-command-contracts.md). Domain-stage references resolve to specification 02; pack mechanics resolve to 05 and evaluations to 04.

### P01 — `inspect-catalogue`

**Native responsibilities:** NC08.  
**Original §20 seeds:** `inspect-catalogue`.

| Required field | Contract |
|---|---|
| inputs | The requested business-model specialisation and intended use, current accessible catalogue, candidate pack manifests/references, known core version and explicit project facts and constraints. |
| evidence required | Actual catalogue entries, pack content and scope, maturity and compatibility evidence at identified versions. Distinguish an advertised or proposed pack from a built, tested or installed specialisation. |
| assumptions allowed | The user’s proposed specialisation may be a hypothesis; unavailable pack details remain unknown. Do not assume a familiar industry label implies changed business behaviour or that an entry proves its tests passed. |
| output | A catalogue assessment recommending an adequate existing pack, a bounded revision, further evidence or a justified new-pack investigation, with overlap, incompatibility and duplication findings. |
| allowed mutations | Write the inspection report and proposed selection only. Do not install, activate, edit, delete, publish or promote packs or alter the catalogue as a side effect of reading it. |
| forbidden behaviour | Jump directly to a new pack without comparison, count industry/location tags as production grammar, rely on missing content as proof of insufficiency or invent successful activation and benchmark evidence. |
| metrics/evidence | Coverage of requested changed behaviour, compatibility with explicit facts/core version, quality and source scope, overlap and evidence of actual maturity. A larger catalogue is not itself better coverage. |
| failure states | BLOCKED when required catalogue or candidate contents are unavailable; FAIL for claims contradicted by inspected content. A correctly empty catalogue is evidence of no listed candidates, not of a globally absent capability. |
| legal/ethical boundaries | Respect pack and source licence/access limits; do not copy restricted material. Catalogue inspection grants no business or external-tool authority, and legal constraints outrank pack defaults. |

### P02 — `research-business-model`

**Native responsibilities:** NC08, NC07.  
**Original §20 seeds:** `research-business-model`.

| Required field | Contract |
|---|---|
| inputs | A bounded specialisation question, catalogue-insufficiency finding or revision need, core behavioural baseline, business structures to compare and the decisions the proposed pack should improve. |
| evidence required | Appropriate original professional/empirical sources and authorised context, with publication/access scope, contradictions and business-model dependencies. Retain reading limits and distinguish a creator’s workflow from demonstrated causal efficacy. |
| assumptions allowed | Candidate changes may remain labelled hypotheses awaiting evidence and demonstration. Do not infer universal optimal prices, channels, retention thresholds or profitability from a source example, industry tag or familiar playbook. |
| output | A sourced research record connecting business-model differences to proposed core behaviours, economics, capacity/cash, metrics, experiments and evaluation consequences, plus rejected alternatives and unresolved questions. |
| allowed mutations | Create or revise the pack research record with source history. Do not change core rules, author legal conclusions, copy proprietary examples, publish claims or fabricate real business observations. |
| forbidden behaviour | Replicate one book’s chapter structure, elevate branded heuristics to mandatory doctrine, create a specialisation without behavioural differences or conceal source uncertainty to make the pack seem validated. |
| metrics/evidence | Decision relevance, source quality and scope, independence, conflicting findings, explicit behavioural differences and consequences for economic/operational constraints. Research volume does not prove pack quality or customer demand. |
| failure states | BLOCKED for mandatory unavailable sources or unresolved decision-critical facts; FAIL for unsupported universals or copied protected content. A finding that no sufficient specialisation is justified is an acceptable research outcome. |
| legal/ethical boundaries | Identify consumer, privacy, employment, tax or regulated-activity questions and route them under Stage 9. Legal research and conclusions remain specialist-owned; a business-model label never supplies an exemption. |

### P03 — `define-specialisation`

**Native responsibilities:** NC08, NC07.  
**Original §20 seeds:** `define-specialisation`, `define-core-effects`.

| Required field | Contract |
|---|---|
| inputs | The evidenced need and catalogue comparison, source research, core version/contracts, intended business-model profile, explicit project facts and applicable legal/professional constraints. |
| evidence required | Evidence that an existing pack is inadequate and that the proposed distinctions materially change reusable business-building behaviour. Name affected core responsibilities, unchanged controls and the economic or workflow reason for each difference. |
| assumptions allowed | A proposed production grammar and expected benefit may remain hypotheses to be demonstrated. Do not assert that authoring a profile proves improved outcomes, or that an industry/location tag alone justifies a pack. |
| output | A candidate specialisation definition with explicit core effects, activation/non-activation conditions, unchanged invariants, precedence, expected economics/metric/experiment differences, evidence limits and required showcase/evaluation obligations. |
| allowed mutations | Write the candidate pack definition and core-effect proposal only. Do not alter accepted core contracts, apply defaults to a live business, replace project facts, publish a pack or promote maturity without subsequent actual validation and approval. |
| forbidden behaviour | Treat provider-specific implementation as business grammar, override explicit facts/accepted decisions with defaults, weaken rights/cash/quality gates, create a replacement core or declare a no-effect label a valid specialisation. |
| metrics/evidence | Traceable changed responsibilities versus unchanged core, coherence across customer/payer, offer, channel, delivery and economics, meaningful activation boundaries and testable differences that later comparison can observe. |
| failure states | FAIL for no meaningful core effect, incoherent changes or precedence violations; BLOCKED for material missing research, core compatibility or specialist constraints. A candidate remains unvalidated until its showcase and evaluation actually exist and pass. |
| legal/ethical boundaries | Verified legal/regulatory constraints and explicit project facts/instructions, then approved decisions, outrank pack defaults and core defaults. Conflicts cannot be resolved by the commercially convenient choice; qualified findings and action authority remain separate. |

### P04 — `build-showcase`

**Native responsibilities:** NC08, NC05.  
**Original §20 seeds:** `build-showcase`.

| Required field | Contract |
|---|---|
| inputs | A specific candidate pack and core version, intended behavioural difference, scenario/inputs, permitted data and artefact scope, chosen execution method and the exact task the showcase should demonstrate. |
| evidence required | Source-grounded pack rules, an explicit baseline and actual execution evidence when claiming an executed showcase. Synthetic fixtures remain labelled; real customer materials require appropriate authorisation and permitted publication/redaction. |
| assumptions allowed | Fictional business facts may be stipulated in a synthetic demonstration and expected outputs may be labelled as expectations. Neither an authored sample nor an intended result may be described as a measured installed-agent outcome. |
| output | A complete showcase package containing the exact copyable prompt, fixed inputs and versions, baseline and pack configuration, expected behavioural distinctions, actual artefacts/results where executed, source limits and reproducibility steps. |
| allowed mutations | Create showcase files and run only authorised local or separately approved execution within the defined scope. Do not publish content, change customer systems, rewrite a pack’s core effects or assert unperformed execution. |
| forbidden behaviour | Omit the exact prompt, substitute attractive prose for the required behaviour, present synthetic records as actual customer evidence, select only convenient outputs or relabel expected results as observed performance. |
| metrics/evidence | Prompt/input completeness, reproduction of the named task, visibility of the intended core effect, preservation of constraints, actual artifact/operation identities and honest distinction between design demonstration and installed execution. |
| failure states | FAIL for missing required showcase elements or false execution claims; BLOCKED for mandatory unavailable runtime, data or permissions when an executed showcase is required. A failed run remains recorded rather than replaced with a success narrative. |
| legal/ethical boundaries | Respect copyright and personal-data restrictions, keep fictional claims visibly synthetic and preserve applicable professional boundaries. A showcase cannot authorise sales, contact, spend, publication or regulated activity outside its declared approvals. |

### P05 — `build-evals`

**Native responsibilities:** NC08, NC05, NC06, NC07.  
**Original §20 seeds:** `build-evals`.

| Required field | Contract |
|---|---|
| inputs | The candidate pack/core contracts, intended changed behaviour, unchanged core invariants, actual or proposed showcase and the failure modes the evaluation must distinguish. |
| evidence required | Source/core-effect traceability and reviewable case facts. Include positive, negative, non-activation, incompatible and precedence cases, preservation/repair expectations and separate deterministic versus judgement criteria. |
| assumptions allowed | Synthetic case facts and expected dispositions may be explicitly authored for a test design. Do not invent benchmark runs, evaluator agreement, real causal effects or statistical confidence from an unexecuted fixture set. |
| output | A complete evaluation case set with exact inputs/prompts, expected acceptable/unacceptable behaviour, dimension-specific checks, execution/assessment method, evidence requirements and conditions for passing, failing or remaining blocked. |
| allowed mutations | Create or revise evaluation assets within the authorised workspace. Execute only the permitted checks and record their actual results; do not weaken accepted criteria to fit a desired outcome or edit the subject pack as a hidden evaluation step. |
| forbidden behaviour | Test only positive examples, omit incompatible/precedence cases, hide failures behind an average score, count a generated checker as a passing run or call self-assessment independent external validation. |
| metrics/evidence | Activation/non-activation, precedence, meaningful changed behaviour, pack-specific metrics, negative cases, core-versus-pack contrast and preservation/regression coverage. Arithmetic/structure correctness remains separate from business judgement. |
| failure states | FAIL for missing mandatory dimensions, non-discriminating tests or false measurement claims; BLOCKED for required unavailable execution or source evidence. A useful negative result is retained and routed to its owning layer. |
| legal/ethical boundaries | Include truthfulness, consent/data, rights and professional-boundary failures where relevant. No benchmark pass grants external business authority or legal clearance; sensitive inputs remain in their authorised custody. |

### P06 — `compare-core-vs-pack`

**Native responsibilities:** NC08, NC05.  
**Original §20 seeds:** `compare-core-vs-pack`.

| Required field | Contract |
|---|---|
| inputs | Identical bounded task and fixed inputs, exact core and core-plus-pack versions, execution environment/method, relevant evaluation criteria and approved resource/data scope. |
| evidence required | Actual paired outputs and run receipts when reporting an executed comparison, together with settings, deviations, failures and source locations. Written expectations alone are insufficient for a measured core-versus-pack claim. |
| assumptions allowed | Synthetic business data are permitted when labelled and shared consistently across both conditions. Uncontrolled differences, stochastic uncertainty and incomplete runs remain visible; do not fabricate improvement or generalise beyond the tested setting. |
| output | A paired comparison record showing actual shared and changed behaviour by separate criteria, compatible invariants, pack-specific effects, failures, uncertainty, costs where measured and a justified accept/revise/reject or blocked decision. |
| allowed mutations | Run the explicitly authorised local comparison and create its records; request approval/access for any additional external execution. Do not alter the core, pack, prompts or criteria mid-comparison and silently call the runs comparable. |
| forbidden behaviour | Describe what the difference should be instead of executing a required comparison, run only the pack condition, cherry-pick successes, change the task between arms or convert one favourable example into universal pack efficacy. |
| metrics/evidence | The relevant behavioural and deterministic dimensions for both conditions, actual input/configuration/run identity, observed deltas and invariant preservation. Report token/time/cost only when actually measured on compatible bases. |
| failure states | BLOCKED when required paired execution/evidence is missing; FAIL when the pack breaks required invariants or lacks its claimed effect. A valid inconclusive comparison does not demonstrate superiority; its decision remains bounded. |
| legal/ethical boundaries | Use authorised data and runtime access without secret or customer-data leakage. Preserve rights, truthfulness and core precedence; comparison execution cannot contact people, spend money or mutate live accounts without specific authority. |

### P07 — `validate-pack`

**Native responsibilities:** NC08, NC07.  
**Original §20 seeds:** `validate-pack`.

| Required field | Contract |
|---|---|
| inputs | Candidate pack and core versions, catalogue comparison, research/core-effect definition, complete showcase with exact prompt, evaluation assets and actual required comparison/verification evidence. |
| evidence required | All required evidence at consistent versions, including activation/non-activation, precedence, intended changed behaviour, negative/incompatible cases and actual core-versus-pack results. Compatibility and licence checks must address the actual selected components. |
| assumptions allowed | No missing required result may be assumed passed. An explicitly provisional hypothesis may remain in research, but cannot justify validated pack status when its required demonstration or quality gate is unresolved. |
| output | A validation report with separate PASS/FAIL/BLOCKED findings, exact tested versions, unmet obligations, repair owner and permitted catalogue/maturity description. A passing candidate includes a ready-for-authorised-catalogue proposal, not automatic publication. |
| allowed mutations | Write the validation and catalogue-entry proposal. Only after all applicable criteria pass and an explicit instruction permits it, add or revise the local catalogue entry for that exact validated version; no external registry promotion, release or installation follows automatically. |
| forbidden behaviour | Treat catalogue presence or an exact filename as evidence of quality, waive failed precedence, promote an unexecuted comparison, hide unsupported facts in a pack default or silently revise the pack while reporting the original version passed. |
| metrics/evidence | Complete contract, showcase and evaluation coverage; reproducibility, actual paired results, invariant preservation, meaningful specialisation, compatibility, source rights and accuracy of catalogue/maturity claims. |
| failure states | FAIL for a violated criterion or unsupported completion claim; BLOCKED for missing mandatory evidence/authority. Record every failure and rerun affected checks after repair; no validated label or publication until all applicable requirements are satisfied. |
| legal/ethical boundaries | Applicable verified constraints and explicit facts/approved decisions outrank specialisation defaults. Legal, licensing, data and professional matters retain their actual reviewer scope; owner approval is separate and cannot waive unlawful or deceptive behaviour. |

## 10. Tool integration and returned evidence

### 4. Minimal handoff and evidence return

Reuse [Stage 7 HC01–HC08](research-logs/2026-09-10-stage-07-unit-economics-and-cash-contract.md#5-deterministic-calculation-handoff), [Stage 8 experiment/learning records](research-logs/2026-09-10-stage-08-assumptions-experiments-and-learning.md) and [Stage 9 issue/constraint packet](research-logs/2026-09-10-stage-09-ethical-and-legal-handoffs.md). The following execution annotations may be inline in those records. They are not another customer ontology, mandatory database schema or generic RPC runtime.

| ID | Annotation | Minimum necessary information |
|---|---|---|
| H01 | decision and preserved baseline | Decision/question, accepted customer/offer/price/process versions, relevant assumptions and unchanged obligations. |
| H02 | requested evidence or action | Exact operation, target, business purpose, population, time horizon and desired return evidence. Separate a read from a draft, write, send, publish or spend. |
| H03 | source and semantic mapping | Authorised locators and input identity; source fields, currency/unit, time zone/window, cohort, cost/metric definition, exclusions and missingness. Preserve source meaning alongside any justified translation. |
| H04 | task-specific tool binding | Actual operator/tool, API/namespace/version or export format, environment/account, required capability and limits. No endpoint is inferred from a similarly named function. |
| H05 | authority and constraints | Exact approval, purpose/data limits, applicable specialist findings, target/version/environment, resource cap, conditions and expiry/review trigger. Credentials and tool annotations cannot expand this scope. |
| H06 | result and reconciliation | Actual attempt/result identity, provider response/error, observed state, returned values, completeness/cutoff and validation evidence. Distinguish requested, attempted, acknowledged and observed effect. |
| H07 | failure and retry conditions | Operation-specific timeout/error semantics, duplicate detection, idempotency scope/retention, permitted retry, uncertain-effect reconciliation and escalation. No global exactly-once promise. |
| H08 | learning and change impact | Evidence and interpretation separately, decision/unknowns, affected dependencies, preserved versions, responsible owner and next review. A tool change alone cannot authorise a business pivot. |

An adequate read-only export can satisfy H02–H06 without creating a connector. Sensitive data stays in its authorised source; the public repository contains only original synthetic fixtures or explicitly approved minimal redactions. Hashes identify bytes, not truth, representativeness or permission. A schema-valid result still needs semantic and provenance checks. Retrieved documents and tool-returned prose are evidence, not instructions to expand the task or expose data.

#### Action and failure handling

Before an external effect, verify the exact tool action and the current approval against purpose, target, environment, accepted version and constraints. A prior read, successful sandbox calculation, broad job title or available credential is insufficient. A business review PASS and an execution permission are separate findings. Routine actions already expressly covered by a valid approval need no invented repeated approval ceremony; changed scope does.

A transport success can contain a tool execution error. An accepted asynchronous request can still be pending. A timeout after submission leaves the effect unknown unless independent evidence resolves it. Preserve the request identity and reconcile with the system/operator before a retry that might duplicate an irreversible effect. Retry rules must match the actual operation and API version; changing a key after an uncertain charge is not a neutral repair. No automatic compensation, refund, deletion or rollback is authorised just because it might undo an earlier action.

A denial or expired credential blocks that operation, not honest analysis of already available evidence. Repair an ordinary retrieval or format error where possible. Do not classify an incomplete export as an empty population, an absent value as zero, or a failed request as a completed experiment. The business conclusion may remain unknown while technical recovery proceeds. Proven harm or broken obligations require appropriately authorised containment without waiting for optional optimisation.

### 5. Tool substitution without workflow redesign

The invariant workflow is: frame the bounded decision; inspect authorised evidence; state assumptions; request adequate calculation/collection or approved execution; validate returned evidence; interpret within scope; choose a bounded action; record learning and preserve unaffected decisions. Provider names and endpoint schemas are not business stages.

A replacement is acceptable only for the actual required capability and scope. Compare both bindings on input/metric meaning, units, period and observation maturity, state/event identity, completeness, permissions, data custody, calculation/error semantics, cost and operational constraints. Verify the smallest real or synthetic contract appropriate to the current design stage. Before a live integration is accepted later, use actual tool execution and returned records; today's synthetic checks cannot be relabelled that acceptance.

| Change | Required review | Business decision preservation |
|---|---|---|
| Different export shape, equivalent underlying facts | Translate only necessary fields and reconcile identical source/event meanings, totals and cutoffs. | Keep customer, offer, price, experiment and workflow unchanged when equivalence passes. |
| Different currency, denominator, cohort window or accounting basis | Obtain a justified bridge or comparable evidence; expose unavailable conversions rather than guess. | Block the unsupported inference, not automatically redesign the business. A valid bridge may change the result. |
| Different calculation implementation | Match inputs, formulas, rounding, exceptional cases and results within a justified tolerance. | Preserve assumptions and decision rule; do not weaken them to fit the new engine. |
| Different CRM, billing or messaging tool | Check state mapping, authority, outstanding effects, opt-outs, event identity and cutover responsibility. | Do not migrate live data or initiate effects without explicit approval. Historical evidence keeps its original source. |
| Different experiment platform or query source | Reconcile assignment unit, exposure, metric/inference settings and maturation. | Retain the frozen hypothesis; changed design requires a visible version and a qualified comparison. |
| Different host agent or communication protocol | Check installed capabilities, file access, returned evidence and permission controls. | Business contracts remain portable; provider-specific runtime support is separately tested, not assumed. |

A provider change may expose a genuine business flaw. Preservation does not mean force identical conclusions from different facts. Revise the implicated analysis or approved decision through its owner; preserve the rest. No tool vendor, commercial score or protocol status can override [Stage 7 independent growth gates](research-logs/2026-09-10-stage-07-unit-economics-and-cash-contract.md#6-independent-growth-gates-and-repair-routing).

## 11. Installation contract

The portable distribution unit is the complete selected skill directory at a known repository revision. Install into the target host's documented skill root or explicitly load that directory in a supported host; record the actual method, destination, host version/configuration and content manifest. Do not advertise a host-specific install command until it has been performed successfully. Git clone or export obtains source bytes; it does not by itself demonstrate host discovery or activation.

An installation procedure must: select the exact skill names and immutable revision; inspect licence/prerequisites; copy each selected unit with all required local files; verify hashes and dependency closure; invoke the host's actual discovery/loading mechanism; run a fitting bounded request and a non-fitting request; inspect output and attempted tool/resource access; record failure and cleanup. A conflicting existing installation is preserved; use a fresh directory or an explicitly approved replacement with rollback rather than overwrite unrelated work. No sibling, package registry, cloud account or Pactwright is implicitly installed.

For clean consumer acceptance, use a new unrelated project and only the published skill distribution plus documented fixed case inputs and tools. Remove the source checkout and sibling resources from the host's accessible context. Record evidence of that separation and the actual opened paths. Exercise each skill alone, then the requested compositions, with no hidden chat history. Record command discovery, relative resources, calculations, mode errors, missing optional capabilities, and preservation of inputs. Source checks and consumer checks have distinct reports; one cannot stand in for the other.

A pack is an explicitly supplied complete directory, loaded only after the mechanism and selection checks in specification 05. A pack catalogue link does not install it, and a business-pack convention is not an official host autodiscovery guarantee. Test pack installation and removal independently; core must still work with no pack.

## 12. CI and technical acceptance

At production scaffold, define scoped checks with documented entry points. CI executes deterministic repository and calculation checks on the actual changed revision. It has read access and a test-output workspace; it receives no commercial account credentials and performs no sends, payments, campaigns, publication or registry promotion. Do not claim remote CI passed when only the same command ran locally. Required host evaluations can be captured separately when the CI environment cannot run the actual host; a missing mandatory run remains blocked for the corresponding release claim.

| Gate | Required execution/evidence | Failure handling |
|---|---|---|
| Source contracts | Parse four entries, exact 10/8/7/7 command menu, 32 nine-field contracts, modes, common-rule identity and local reference closure | Fail missing/duplicate commands, unresolved required files or weaker distributed rules |
| Domain arithmetic | Execute relevant formulas on fixed data, including zero/missing/non-finite and duplicate identity controls; keep units, periods and cost bases | Repair owning calculation/definition; do not silently coerce values |
| Case registry | Verify 15 primaries at 3/3/3/3/3, full prompts/inputs, three stress structures, 14 added adversaries and complete applicable pack obligations | Keep difficult cases; scoped reruns cannot claim full coverage |
| Source preservation | Compare accepted subject and fixture versions before/after checks; outputs stay separate | Fail unauthorised mutations; preserve attempted run evidence |
| Source installation | Actually load distribution from the repository context and exercise discovery/resources | Record actual host/method and limits |
| Clean/selective installation | Execute the procedure in §11 with source and siblings unavailable | Missing runtime or dependency is BLOCKED, not a passed file listing |
| Business behaviour | Grade actual installed outputs using specification 04, including negative activation, mode selection and preservation | Structural checks cannot replace this gate |
| Release/maturity | Matching current revision, all mandatory deterministic/semantic/installation/pack/regression gates, honest documentation and authority | No automatic merge, release or promotion from CI success alone |

Pin tested tool/host/action versions or immutable identities in receipts where available; state missing metadata. A changing dependency requires an affected compatibility check before repeating its support claim. Select the existing host and minimal verification tools that satisfy these contracts; no bespoke business runtime or universal installer is required. Final technical acceptance is an independently usable product at the documented revision, with reproducible actual evidence rather than planned commands.

---

Specification 03 · Contract version 1.0 · 12 September 2026
