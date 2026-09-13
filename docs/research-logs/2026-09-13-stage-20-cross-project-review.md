# Stage 20: Cross-project review

**Date:** 13 September 2026  
**Stage:** 20 — Cross-Project Review  
**Branch and starting head:** `feat/bootstrap-3` at `e42a44fee5ca6291348b317a0d3edbd762b49198`  
**Authority:** [Original bootstrap §27](2026-09-08-business-building-skills-new-project-bootstrap-process.md#27-stage-20--cross-project-review), global §§2,5,34–35 and [execution contract](2026-09-12-bootstrap-3-execution-contract.md).

## 1. Goal, prerequisite and scope

Compare the independently derived business architecture with all six named projects. Record compatible ownership and useful integration opportunities, exposing differences in terminology, maturity and loading conventions. Record repeated concepts without implementing shared infrastructure or rewriting the accepted business architecture.

Stage 19’s completion receipt was freshly verified: branch/head `e42a44fee5ca6291348b317a0d3edbd762b49198`, parent `7527bfbd53c5cf07e7d23e14e48c621d83bfd610`, tree `a21376d277b4f02b9718a7e820340c9d5f208eef`, one commit ahead and only the progress file changed. The complete fetched progress blob is `5ea320b2d9318d353252eef548e7e95b33f48229`. All 118 local predecessor files match the remote tree. Earlier accepted outputs and the Stage 19 public draft remain authoritative.

The original business bootstrap was reread in full, then the complete Stage 20 section and relevant globals. Accepted specifications 01 §§6–9, 02 §10, 03 §§10–11 and the earlier progress/README design supplied the current boundaries. All six canonical specification identities and earlier case/pack contracts are preserved by the baseline manifest. No earlier-stage verifier is rerun or earlier-stage decision reopened.

The user explicitly directed continuation after each completed stage unless a genuine blocker requires their input. Earlier session-stop notes remain historical evidence, not an instruction to stop this continuation. Stage 21 will begin after this stage’s content and remote receipt pass.

## 2. Acceptance checklist

| Category | Requirement and source |
|---|---|
| Purpose | Actual cross-project architecture review; original §27 |
| Inputs | Original specification, accepted six canonical specs, Stage 19 receipt/draft and actual sources of the six named projects; §27 and contract §3 |
| Prerequisites | Stage 19 fully verified; accepted Stages 1–19 preserved; contract §§1–3,7 |
| Questions | Resolve source scope, ownership overlaps, evidence/approval meanings and compatibility differences; §27 exit |
| Research | Access actual repositories and read relevant source contracts at identified revisions; §27 “Compare” and contract §§3–4 |
| Activities | Compare responsibilities, handoffs, returned evidence, authority, independence, maturity and candidate abstractions; §27; global §2 |
| Comparisons | Exactly the six named projects: Deep Research, Legal, UI/UX, Software Engineering, Production Skills family and Pactwright; §27 literal list |
| Candidate discovery | Inspect recurrence of all four suggested abstraction families and meaningful variations; §27; no new business/pack/example selection required |
| Analysis | Separate business choices from research/legal/UX/engineering/lifecycle truth; expose practical integration gaps; §27 and §§5,34 |
| Decisions | Preserve business architecture, use explicit bounded artefact handoffs, keep shared implementation local and optional; §§2,27,33 |
| Deliverables | Complete review, source/access evidence, comparison/candidate records, verification/conformance and accurate progress/remote receipt; contract §§5–7 |
| Contents | Six complete comparisons, concrete integration opportunities, four abstraction candidates with variations/rejected over-generalisations, sources/limits and next-stage inputs; §27 and contract §6 |
| Counts/distribution | Six named comparison subjects; all four suggested concepts examined. Original 15 examples and eight independent pack candidates plus advisory mode remain intact; §§22,27 and accepted outputs |
| Names/structure | Preserve owning project/skill/artefact names; avoid equating different “Contract”, “Evidence” or “Pack” meanings; §27/global §2 |
| Prompts/examples | No new primary prompt count in §27. Six bounded handoff reviews make the comparison concrete; accepted E01–E15 are not replaced |
| Tests/execution | Actually inspect sources and perform substantive handoff/compatibility review; execute file/source/link/count/preservation verification; contract §5 |
| Measurements | Record actual versions, file identities, check results and observed source limitations. No installed or commercial measurements required or invented; contract §§4–6 |
| Verification | Reread the original §27 after drafting; check each required comparison, concept, boundary, links and actual file scope; contract §5 |
| Research log | Goal, accessed sources/limits, comparisons, analysis, decisions, rejected alternatives, outputs, conformance, questions and handoff; contract §6 |
| Exit | Integration opportunities recorded without creating a universal business operating system; §27 |
| Later work | Production scaffold §28, installed business proof/coverage §§29–30, clean install §31, optional actual Pactwright compatibility/registry §32 and production-evidenced extraction §33 |

## 3. Source selection and limits

Use the default published branch of each named repository and pin its actual head. This gives a consistent public-contract comparison and does not import unfinished feature-branch work as a business implementation template. A default-branch limitation is recorded rather than hidden. This review does not claim that other branches lack work. The business repository remains on `feat/bootstrap-3`; no other repository is modified.

| Project | Inspected `main` commit | Observed source scope |
|---|---|---|
| Deep Research Skills | `80b209968b366662c01a8ded5ecb6c30bb6beb0b` | Three-file bootstrap workspace; declared architecture only. |
| Legal Skills | `b15f3134552ea763d434783d655aea44c0e01925` | Three-file bootstrap workspace; declared architecture only. |
| UI/UX Design Skills | `db888866787542311e9e29e15ed92362f5f283e5` | Canonical specs, actual SKILL.md and command references; README explicitly retains semantic/clean-install gates. |
| Software Engineering Skills | `684986785ceafbc031419d6fc7287dbfe0578dba` | Three-file bootstrap workspace; declared architecture only. |
| Production Skills family | `20979e0c68ac4b37433374df7fe10ceb2e7ee69a` | Canonical family contracts and actual proposed registry entry. |
| Pactwright | `207ac08507f9687be9eca105915bbd3db1e1dd4b` | Current README, historical architecture, actual manifest parser and core node schema; no runtime invocation. |

All 21 selected files were fetched in full through the GitHub connector, matched to the pinned repository trees and checked by Git blob identity. Reading was focused on the stated sections; fetching a full file is not a claim to have read every linked reference. The source register identifies exact scopes. Source files are comparison inputs, not vendored runtime dependencies. Underlying book, legal-authority and third-party provider links inside those documents were not reopened and are not presented as freshly verified claims.

| Source | Actual file and immutable revision | Material inspected |
|---|---|---|
| S01 | [deep-research-skills/README.md](https://github.com/sb-dev/deep-research-skills/blob/80b209968b366662c01a8ded5ecb6c30bb6beb0b/README.md) | Complete README; bootstrap state. |
| S02 | [deep-research-skills/docs/research-logs/2026-09-07-deep-research-skills-new-project-bootstrap-process.md](https://github.com/sb-dev/deep-research-skills/blob/80b209968b366662c01a8ded5ecb6c30bb6beb0b/docs/research-logs/2026-09-07-deep-research-skills-new-project-bootstrap-process.md) | Purpose and governing principles; question/evidence/claim/provenance model (§9); workflow/artifacts (§11); effort and stopping (§12). Seed citations are attributed source content, not reverified legal/provider facts. |
| S03 | [legal-skills/README.md](https://github.com/sb-dev/legal-skills/blob/b15f3134552ea763d434783d655aea44c0e01925/README.md) | Complete README; bootstrap state. |
| S04 | [legal-skills/docs/research-logs/2026-09-08-legal-skills-new-project-bootstrap-process.md](https://github.com/sb-dev/legal-skills/blob/b15f3134552ea763d434783d655aea44c0e01925/docs/research-logs/2026-09-08-legal-skills-new-project-bootstrap-process.md) | Purpose, boundary and principles; jurisdiction/authority/time (§11), matter records (§12), change traceability (§14), uncertainty/escalation (§15), confidentiality (§16). Underlying legal authorities were not newly accessed or adopted as live advice. |
| S05 | [software-engineering-skills/README.md](https://github.com/sb-dev/software-engineering-skills/blob/684986785ceafbc031419d6fc7287dbfe0578dba/README.md) | Complete README; bootstrap state. |
| S06 | [software-engineering-skills/docs/research-logs/2026-09-07-software-engineering-skills-new-project-bootstrap-process.md](https://github.com/sb-dev/software-engineering-skills/blob/684986785ceafbc031419d6fc7287dbfe0578dba/docs/research-logs/2026-09-07-software-engineering-skills-new-project-bootstrap-process.md) | Thesis/principles (§§4–5), change/contract model (§12), workflow (§13), risk/verification (§14), optional Pactwright boundary (§28). No execution of this bootstrap. |
| S07 | [ui-ux-design-skills/README.md](https://github.com/sb-dev/ui-ux-design-skills/blob/db888866787542311e9e29e15ed92362f5f283e5/README.md) | Opening capabilities, approval, installation advertisement and quick start; tools/checks/documentation/boundary/status/licence. Advertised installer was not run. |
| S08 | [ui-ux-design-skills/docs/01-ui-ux-design-skills-system-spec.md](https://github.com/sb-dev/ui-ux-design-skills/blob/db888866787542311e9e29e15ed92362f5f283e5/docs/01-ui-ux-design-skills-system-spec.md) | Purpose/goals/non-goals/principles; uiux-handoff responsibility, independent skills and family boundary (§19). |
| S09 | [ui-ux-design-skills/docs/02-ui-ux-design-skills-workflows-and-artifacts-spec.md](https://github.com/sb-dev/ui-ux-design-skills/blob/db888866787542311e9e29e15ed92362f5f283e5/docs/02-ui-ux-design-skills-workflows-and-artifacts-spec.md) | Evidence/confidence/conflicts (§§7–9), interaction hypotheses (§14), fidelity/approval/preservation (§§22–24), evaluation/diagnosis (§§31–34), handoff/traceability (§§39–43), consumer-state boundary (§46). |
| S10 | [ui-ux-design-skills/skills/uiux-handoff/SKILL.md](https://github.com/sb-dev/ui-ux-design-skills/blob/db888866787542311e9e29e15ed92362f5f283e5/skills/uiux-handoff/SKILL.md) | Complete actual uiux-handoff SKILL.md; activation, commands, artefacts, external execution and ownership. No installed execution. |
| S11 | [production-skills/README.md](https://github.com/sb-dev/production-skills/blob/20979e0c68ac4b37433374df7fe10ceb2e7ee69a/README.md) | Complete README, including family-owned/consumer-owned state and explicit non-retroactive bootstrap migration. |
| S12 | [production-skills/docs/specs/01-production-skills-family-system.md](https://github.com/sb-dev/production-skills/blob/20979e0c68ac4b37433374df7fe10ceb2e7ee69a/docs/specs/01-production-skills-family-system.md) | Architecture, ownership, principles, terminology, maturity, anti-goals and change rule (§§3–9). |
| S13 | [production-skills/docs/specs/02-production-skills-project-contract.md](https://github.com/sb-dev/production-skills/blob/20979e0c68ac4b37433374df7fe10ceb2e7ee69a/docs/specs/02-production-skills-project-contract.md) | Required responsibilities; production baseline; skill/command/resource/tool/pack/standalone/binding contracts (§§8–14); working/benchmarked/mature and compatibility gates (§§16–20). |
| S14 | [production-skills/docs/specs/04-cross-domain-orchestration-and-integration.md](https://github.com/sb-dev/production-skills/blob/20979e0c68ac4b37433374df7fe10ceb2e7ee69a/docs/specs/04-cross-domain-orchestration-and-integration.md) | Complete canonical cross-domain integration specification. |
| S15 | [production-skills/registry/projects/business-building-skills.json](https://github.com/sb-dev/production-skills/blob/20979e0c68ac4b37433374df7fe10ceb2e7ee69a/registry/projects/business-building-skills.json) | Complete actual business-building registry record; proposed status and planned Pactwright compatibility. |
| S16 | [pactwright/README.md](https://github.com/sb-dev/pactwright/blob/207ac08507f9687be9eca105915bbd3db1e1dd4b/README.md) | Complete current README. CLI and release statements are documented interfaces/claims, not new install/release evidence. |
| S17 | [pactwright/docs/research-logs/2026-08-11-pactwright-system-architecture.md](https://github.com/sb-dev/pactwright/blob/207ac08507f9687be9eca105915bbd3db1e1dd4b/docs/research-logs/2026-08-11-pactwright-system-architecture.md) | Purpose/system model (§§1–2), architectural boundaries (§4), state model (§6), invariants/governing rules (§§11–12). Historical architecture is distinguished from inspected runtime code. |
| S18 | [pactwright/docs/research-logs/2026-08-11-pactwright-delivery-graph-and-lifecycle-engineering-spec.md](https://github.com/sb-dev/pactwright/blob/207ac08507f9687be9eca105915bbd3db1e1dd4b/docs/research-logs/2026-08-11-pactwright-delivery-graph-and-lifecycle-engineering-spec.md) | Stable semantics (§2), decision/contract/brief (§§8–10), delivery Evidence (§12), supersession (§15). |
| S19 | [pactwright/packages/standard/skills/contract-writing.md](https://github.com/sb-dev/pactwright/blob/207ac08507f9687be9eca105915bbd3db1e1dd4b/packages/standard/skills/contract-writing.md) | Complete default agent-pack contract-writing resource. |
| S20 | [pactwright/src/pack/manifest.ts](https://github.com/sb-dev/pactwright/blob/207ac08507f9687be9eca105915bbd3db1e1dd4b/src/pack/manifest.ts) | Complete actual TypeScript pack manifest parser, pack.yml identity and flat skill-path resolution. Read, not executed. |
| S21 | [pactwright/src/graph/schema.ts](https://github.com/sb-dev/pactwright/blob/207ac08507f9687be9eca105915bbd3db1e1dd4b/src/graph/schema.ts) | Complete actual TypeScript core node schema and decision outcomes. Read, not executed. |

## 4. Six complete architecture comparisons

### CP01 — Deep Research Skills

Source basis: [S01](https://github.com/sb-dev/deep-research-skills/blob/80b209968b366662c01a8ded5ecb6c30bb6beb0b/README.md), [S02](https://github.com/sb-dev/deep-research-skills/blob/80b209968b366662c01a8ded5ecb6c30bb6beb0b/docs/research-logs/2026-09-07-deep-research-skills-new-project-bootstrap-process.md).

| Responsibility | Comparison finding |
|---|---|
| Business/consumer ownership | Commercial question, customer/value decision, experiment and economic consequence. |
| Other project ownership | Question-driven source acquisition, provenance, contradiction analysis, synthesis and claim audit. |
| Outbound information | Decision/use, population, claim, required freshness, known facts and unknowns, source restrictions, effort ceiling and requested evidence. |
| Returned information | Attributable source/evidence/claim links, underlying-source independence, contrary evidence, dates and uncertainty; not invented local customers. |
| Observed limit | Default main contains only three bootstrap files. Compare declared architecture; do not claim installed capability. |
| Decision | Compose through a bounded research brief and evidence return; keep the business decision with Business Building. |

### CP02 — Legal Skills

Source basis: [S03](https://github.com/sb-dev/legal-skills/blob/b15f3134552ea763d434783d655aea44c0e01925/README.md), [S04](https://github.com/sb-dev/legal-skills/blob/b15f3134552ea763d434783d655aea44c0e01925/docs/research-logs/2026-09-08-legal-skills-new-project-bootstrap-process.md).

| Responsibility | Comparison finding |
|---|---|
| Business/consumer ownership | Commercial intention, actual terms/behaviour, economics, customer obligations and authorised business response. |
| Other project ownership | Legal scoping, authoritative research, applicability, legal drafting/review and professional escalation. |
| Outbound information | HF01–HF07 issue packet: exact versions, actors, jurisdictions, dates, conduct, data-use limits, contradictions and precise legal question. |
| Returned information | Author/remit, reviewed facts, authority/status, jurisdiction, effective/valid-as-of dates, conditions, required/prohibited acts and re-review trigger. |
| Observed limit | Default main contains only bootstrap intent. This review makes no current substantive-law finding or professional clearance. |
| Decision | Consume attributed, applicable constraints; unresolved jurisdiction/authority blocks the affected commitment, not honest draft work. |

### CP03 — UI/UX Design Skills

Source basis: [S07](https://github.com/sb-dev/ui-ux-design-skills/blob/db888866787542311e9e29e15ed92362f5f283e5/README.md), [S08](https://github.com/sb-dev/ui-ux-design-skills/blob/db888866787542311e9e29e15ed92362f5f283e5/docs/01-ui-ux-design-skills-system-spec.md), [S09](https://github.com/sb-dev/ui-ux-design-skills/blob/db888866787542311e9e29e15ed92362f5f283e5/docs/02-ui-ux-design-skills-workflows-and-artifacts-spec.md), [S10](https://github.com/sb-dev/ui-ux-design-skills/blob/db888866787542311e9e29e15ed92362f5f283e5/skills/uiux-handoff/SKILL.md).

| Responsibility | Comparison finding |
|---|---|
| Business/consumer ownership | Customer/value hypothesis, offer and terms, commercial experiment, money/capacity constraints and scale decision. |
| Other project ownership | Interaction requirements, hypotheses, lowest useful fidelity, accessibility, states, UX validation and engineering handoff. |
| Outbound information | Accepted offer/price/rights, target task, evidence and unknowns, experiment question, no-change constraints and any applicable legal finding. |
| Returned information | Interaction contract, states/recovery/accessibility, measured task outcomes and limits, hypothesis state, accepted design version and unresolved implementation risk. |
| Observed limit | Actual SKILL.md and command references exist; README says semantic benchmark and clean installation remain gates. No installation was performed here. |
| Decision | Use UX to resolve interaction uncertainty; retain its confidence vocabulary without upgrading it to paid demand, retention or commercial approval. |

### CP04 — Software Engineering Skills

Source basis: [S05](https://github.com/sb-dev/software-engineering-skills/blob/684986785ceafbc031419d6fc7287dbfe0578dba/README.md), [S06](https://github.com/sb-dev/software-engineering-skills/blob/684986785ceafbc031419d6fc7287dbfe0578dba/docs/research-logs/2026-09-07-software-engineering-skills-new-project-bootstrap-process.md).

| Responsibility | Comparison finding |
|---|---|
| Business/consumer ownership | Business outcome in scope, accepted commercial facts/obligations, decision rule and permitted commitment. |
| Other project ownership | Repository inspection, affected technical contracts, code change, appropriate verification, failure diagnosis and implementation repair. |
| Outbound information | Bounded behaviour, exact inputs/outputs, invariants, privacy/rights/quality constraints, acceptance examples and change authority; UX contract if relevant. |
| Returned information | Actual revision/diff, tests and results, remaining limitations, operational assumptions and any business-relevant behaviour change. |
| Observed limit | Default main has three bootstrap files. Engineering intent is not an implemented/validated skill product. |
| Decision | Keep architecture and tools in engineering; a passing test proves only tested behaviour, not demand, delivered customer value or permission to deploy. |

### CP05 — Production Skills family

Source basis: [S11](https://github.com/sb-dev/production-skills/blob/20979e0c68ac4b37433374df7fe10ceb2e7ee69a/README.md), [S12](https://github.com/sb-dev/production-skills/blob/20979e0c68ac4b37433374df7fe10ceb2e7ee69a/docs/specs/01-production-skills-family-system.md), [S13](https://github.com/sb-dev/production-skills/blob/20979e0c68ac4b37433374df7fe10ceb2e7ee69a/docs/specs/02-production-skills-project-contract.md), [S14](https://github.com/sb-dev/production-skills/blob/20979e0c68ac4b37433374df7fe10ceb2e7ee69a/docs/specs/04-cross-domain-orchestration-and-integration.md), [S15](https://github.com/sb-dev/production-skills/blob/20979e0c68ac4b37433374df7fe10ceb2e7ee69a/registry/projects/business-building-skills.json).

| Responsibility | Comparison finding |
|---|---|
| Business/consumer ownership | Reusable business semantics, skills/packs/cases/benchmarks and domain evidence. Consuming business owns its actual records and choices. |
| Other project ownership | Family principles, packaging/evaluation/composition contracts, registry/maturity and evidence-qualified shared abstractions. |
| Outbound information | Stable project identity, revision, scoped capabilities, actual gate evidence and optional compatibility status; no customer state or private project knowledge. |
| Returned information | Structural conformance and registry metadata; no central commercial-quality score. |
| Observed limit | Observed registry status remains proposed, Pactwright planned; no registry mutation or maturity promotion in Stage 20. |
| Decision | Preserve independent distribution and domain-owned evaluation. New bootstrap recipes do not retroactively reopen accepted Stages 1–15. |

### CP06 — Pactwright

Source basis: [S14](https://github.com/sb-dev/production-skills/blob/20979e0c68ac4b37433374df7fe10ceb2e7ee69a/docs/specs/04-cross-domain-orchestration-and-integration.md), [S16](https://github.com/sb-dev/pactwright/blob/207ac08507f9687be9eca105915bbd3db1e1dd4b/README.md), [S17](https://github.com/sb-dev/pactwright/blob/207ac08507f9687be9eca105915bbd3db1e1dd4b/docs/research-logs/2026-08-11-pactwright-system-architecture.md), [S18](https://github.com/sb-dev/pactwright/blob/207ac08507f9687be9eca105915bbd3db1e1dd4b/docs/research-logs/2026-08-11-pactwright-delivery-graph-and-lifecycle-engineering-spec.md), [S19](https://github.com/sb-dev/pactwright/blob/207ac08507f9687be9eca105915bbd3db1e1dd4b/packages/standard/skills/contract-writing.md), [S20](https://github.com/sb-dev/pactwright/blob/207ac08507f9687be9eca105915bbd3db1e1dd4b/src/pack/manifest.ts), [S21](https://github.com/sb-dev/pactwright/blob/207ac08507f9687be9eca105915bbd3db1e1dd4b/src/graph/schema.ts).

| Responsibility | Comparison finding |
|---|---|
| Business/consumer ownership | Business meaning, assumptions, evidence interpretation, commercial constraints and smallest-change proposal. |
| Other project ownership | Delivery lifecycle authority, typed canonical nodes, authorised decisions/contracts/briefs and delivery Evidence; optional extensions own their additional state. |
| Outbound information | A proposed bounded deliverable and acceptance conditions with preserved versions, scope/non-scope, limits and actual owner authority; through the consuming project’s configured agent pack. |
| Returned information | Delivered outputs, verification/results, deviations and residual risks tied to actual revision; post-delivery observations separate. |
| Observed limit | Inspected runtime uses `pack.yml` and `skills/<name>.md`; no inference that `PACK.md` or `integrations/pactwright.yml` is automatically loaded. No integration executed. |
| Decision | Keep optional explicit binding and existing lifecycle. Business review cannot directly create/mutate graph nodes or turn delivery Evidence into commercial validation. |

The comparisons preserve the original likely boundaries. Overlap in “research”, “experiment”, “evaluate” and “repair” is intentional at different owning layers. A business question can need external research, interaction design and engineering without transferring its commercial decision to any of them. A specialist finding can constrain that decision without becoming permission for execution.

## 5. Concrete integration opportunities and semantics

| Opportunity | Bounded handoff and return | Acceptance and preserved boundary |
|---|---|---|
| I01 — Evidence for a channel or pricing assumption | Business supplies its decision, actual population/context, claim and evidence gap; research returns source-specific support, contradictions, freshness and limits | Source methods and population must fit the claim. Generic published CAC, search traffic or stated interest cannot become local acquired-customer evidence. Use core analysis when supplied facts already suffice. |
| I02 — Offer/renewal/cancellation review | Business sends exact proposed terms and current behaviour through an authorised legal issue packet; Legal returns matter-specific constraints; Business/UX/engineering consume their relevant obligations | Preserve reviewed versions, jurisdiction, effective dates and conditions. Missing applicability stays unresolved. Clear wording cannot cure behaviour that breaches a known constraint. |
| I03 — Quote, onboarding or cancellation comprehension | Business supplies accepted value/offer/price/rights and the uncertainty; UX designs the cheapest adequate task/interaction test and returns scoped evidence and a behavioural handoff | Preserve price and rights during UX refinement. Task completion, accessibility or comprehension are assessed in their own scope; payment, retention and commercial viability require their own evidence. |
| I04 — Bounded product or measurement change | A business experiment or diagnosed defect supplies exact intended behaviour and metrics; engineering inspects the current system, implements the scoped change and returns actual verification | Preserve denominators, cohort/window and event meaning across instrumentation changes. Code tests establish tested behaviour. Customer evidence is collected separately under the actual experiment/permission contract. |
| I05 — Family discovery and maturity | Expose project identity, immutable revision, scoped capabilities and actual evidence; consult the registry as a discovery/status record | Structural conformance does not grade business quality. Current observed registry remains proposed; no migration, dependency or promotion is induced by this review. |
| I06 — Optional governed delivery | The consuming project converts an authorised bounded business deliverable into its Pactwright Contract/Brief and selected agent-pack execution; returned Evidence records actual delivery and verification | Core Delivery ends at Evidence. Deployment, publication, use and business outcome remain separate. Business skills do not write graph state, invent lifecycle stages or bypass configured gates. |

### 5.1 Practical incompatibilities resolved by explicit boundaries

**Pack format:** source S20 actually declares `pack.yml`, a capability-to-agent map and `skills/<name>.md`. Business distribution uses independent `skills/<name>/SKILL.md`; a Business Extension Pack uses `PACK.md` and domain-specific effects. These are different objects. A family `integrations/pactwright.yml` can describe compatibility, but the inspected parser does not establish an automatic loader for that file or a business pack. Stage 25 must use an actual supported binding and test it if integration is implemented. Do not add one in this review or turn business selectors into lifecycle stages.

**Approval and evidence:** Business’s decision/permission and evidence classification, UX’s approval and `VALIDATED_IN_CONTEXT`, Legal’s applicable conclusion, and Pactwright’s `proceed` decision/delivery Evidence have different predicates. Keep the producer’s original state and explain the receiving claim. Do not convert them to one boolean. Business conformance PASS can coexist with an unapproved or cash-blocked business action.

**Time and identity:** retain event, collection, publication, effective and valid-as-of meanings as relevant. A new commit/hash identifies bytes, not current law, fresh customer evidence or business truth. A business cohort/window and cost basis remain attached to calculations. Incompatible metric/event definitions require reconciliation before comparison; unchanged headings do not establish equivalence.

**Project state:** reusable records and instructions belong to the skill owner; actual business, UX, legal and engineering evidence stays with the consuming project and its authorised data sources. Pactwright/Project Intelligence, when selected, keeps its own canonical ownership. No second customer database, manual parallel graph or central business state store is introduced.

**Family evolution:** the current family README explicitly preserves existing domain bootstrap books, history and maturity unless the owner adopts a migration. Its newer Seed → Five → Challenge recipe therefore does not silently invalidate accepted business Stages 1–15. No contradiction requiring alteration of those accepted outputs was found.

### 5.2 Bounded handoff reviews actually performed

The following are authored semantic reviews against the inspected contracts. They are not installed-agent outputs, API round trips, user studies, legal opinions or live business results. Their PASS means the proposed translation preserves the source/consumer boundary. It does not mean a business proposal or runtime integration passed.

#### H01 — CP01

**Method:** Authored synthetic handoff review, not a research run.

**Input:** A research report attributes the same acquisition-cost claim to three articles that repeat one underlying source. Local paid-customer data is absent.

**Adequate return:** Retain all locators but identify one underlying evidence source; preserve claim scope/dates and missing local cohort data. Business Building can propose a test, not report verified local CAC.

**Rejected translation:** Count three independent validations or import the advertised number as the business’s observed CAC.

**Preserved:** Accepted customer/offer and actual evidence states. **Review result:** PASS.

#### H02 — CP02

**Method:** Authored synthetic handoff review, not legal research or advice.

**Input:** A cancellation proposal has exact current terms and observed UI behaviour, but applicable jurisdiction and reviewer finding are unknown.

**Adequate return:** Prepare the bounded issue packet, preserve rights and facts, request applicability/conditions through an authorised reviewer. Keep the dependent legal commitment unresolved.

**Rejected translation:** Infer the jurisdiction from the business-model pack or call the proposal legally approved because copy is clear.

**Preserved:** Existing refund/cancellation obligations; no message sent or terms changed. **Review result:** PASS.

#### H03 — CP03

**Method:** Authored synthetic vocabulary/ownership review, not a UX trial.

**Input:** UX marks a cancellation interaction VALIDATED_IN_CONTEXT for observed task completion in a stated small study. The business has no subsequent paid-renewal evidence.

**Adequate return:** Retain the scoped task observation and confidence label, study limits and accepted terms. Paid renewal and satisfaction remain separate unresolved claims.

**Rejected translation:** Map the UX label to business PASS for retention or permission to scale paid acquisition.

**Preserved:** Price, renewal/refund terms, audience and accepted interaction scope. **Review result:** PASS.

#### H04 — CP04

**Method:** Authored synthetic delivery review, not a software execution.

**Input:** Engineering reports a tested calculation fix at a named revision; unit tests pass on synthetic input. The customer experiment has not run.

**Adequate return:** Record the implementation and exact tested numerical behaviour. Recalculate affected business scenarios with actual inputs when available; keep demand and experiment outcome unknown.

**Rejected translation:** Treat the synthetic test pass as observed demand, new revenue or authorisation to deploy/charge.

**Preserved:** Metric definitions, input evidence states, unrelated code and commercial decisions. **Review result:** PASS.

#### H05 — CP05

**Method:** Actual registry/source inspection with an authored adverse interpretation.

**Input:** The pinned family registry records business-building-skills as proposed with Pactwright planned; local documents and design checks exist.

**Adequate return:** Retain the actual registered status and separate current design evidence. Later promotion requires its own gates and authority.

**Rejected translation:** Overwrite the registry to mature because the structural files and links pass.

**Preserved:** Family registry and all other repositories remain unchanged. **Review result:** PASS.

#### H06 — CP06

**Method:** Authored synthetic semantic/format review, not Pactwright execution.

**Input:** A Pactwright Evidence record says a prototype was delivered and verified. A Business Extension Pack has PACK.md; the inspected agent-pack parser requires pack.yml and flat skill resources.

**Adequate return:** Keep prototype delivery distinct from exposure/customer outcome; keep the business pack outside the agent-pack loader. An optional binding must be explicitly implemented and tested at compatible versions.

**Rejected translation:** Mark the business experiment successful from delivery Evidence or claim that copying PACK.md installs a Pactwright agent pack.

**Preserved:** Core node/lifecycle semantics, original business evidence and standalone skill distribution. **Review result:** PASS.

## 6. Repeated abstraction candidates

All four suggested candidates were compared. Recurrence is architectural/source evidence at this stage. Business Building has no installed production run yet, so none qualifies here for a new shared implementation. Existing family principles remain usable without promoting a new schema or engine.

### A01 — Assumption / evidence / decision handoff

Source witnesses: [S02](https://github.com/sb-dev/deep-research-skills/blob/80b209968b366662c01a8ded5ecb6c30bb6beb0b/docs/research-logs/2026-09-07-deep-research-skills-new-project-bootstrap-process.md), [S04](https://github.com/sb-dev/legal-skills/blob/b15f3134552ea763d434783d655aea44c0e01925/docs/research-logs/2026-09-08-legal-skills-new-project-bootstrap-process.md), [S09](https://github.com/sb-dev/ui-ux-design-skills/blob/db888866787542311e9e29e15ed92362f5f283e5/docs/02-ui-ux-design-skills-workflows-and-artifacts-spec.md), [S14](https://github.com/sb-dev/production-skills/blob/20979e0c68ac4b37433374df7fe10ceb2e7ee69a/docs/specs/04-cross-domain-orchestration-and-integration.md), [S17](https://github.com/sb-dev/pactwright/blob/207ac08507f9687be9eca105915bbd3db1e1dd4b/docs/research-logs/2026-08-11-pactwright-system-architecture.md).

- Common need: Preserve the meaning, provenance, uncertainty and authority of information at an ownership transition.
- Meaningful variations: Research source/claim distinctions; legal authority/applicability; UX mechanism/hypothesis; business observation/interpretation/commitment; Pactwright canonical delivery records.
- Evidence limit: Architecture and source-contract recurrence observed; no independent implemented Business Building handoff run yet.
- Decision: Use existing documented handoffs. Candidate only; no common database, schema migration or runtime.

### A02 — Experiment contract

Source witnesses: [S02](https://github.com/sb-dev/deep-research-skills/blob/80b209968b366662c01a8ded5ecb6c30bb6beb0b/docs/research-logs/2026-09-07-deep-research-skills-new-project-bootstrap-process.md), [S06](https://github.com/sb-dev/software-engineering-skills/blob/684986785ceafbc031419d6fc7287dbfe0578dba/docs/research-logs/2026-09-07-software-engineering-skills-new-project-bootstrap-process.md), [S09](https://github.com/sb-dev/ui-ux-design-skills/blob/db888866787542311e9e29e15ed92362f5f283e5/docs/02-ui-ux-design-skills-workflows-and-artifacts-spec.md), [S18](https://github.com/sb-dev/pactwright/blob/207ac08507f9687be9eca105915bbd3db1e1dd4b/docs/research-logs/2026-08-11-pactwright-delivery-graph-and-lifecycle-engineering-spec.md).

- Common need: Choose a bounded question, adequate method, comparison and predeclared decision-changing evidence.
- Meaningful variations: Research may resolve uncertainty without intervention; UX tests an interaction/human outcome; software verifies behaviour; business needs actual customer/economic evidence. Pactwright Contract records agreed delivery, not experimental validity.
- Evidence limit: Repeated design needs, including existing UX/source contracts; no measured cross-domain equivalence established.
- Decision: Retain domain records and terminology. Link dependent tests; do not create one experiment platform or treat every test pass as market validation.

### A03 — Constraint diagnosis and smallest sufficient correction

Source witnesses: [S02](https://github.com/sb-dev/deep-research-skills/blob/80b209968b366662c01a8ded5ecb6c30bb6beb0b/docs/research-logs/2026-09-07-deep-research-skills-new-project-bootstrap-process.md), [S04](https://github.com/sb-dev/legal-skills/blob/b15f3134552ea763d434783d655aea44c0e01925/docs/research-logs/2026-09-08-legal-skills-new-project-bootstrap-process.md), [S06](https://github.com/sb-dev/software-engineering-skills/blob/684986785ceafbc031419d6fc7287dbfe0578dba/docs/research-logs/2026-09-07-software-engineering-skills-new-project-bootstrap-process.md), [S08](https://github.com/sb-dev/ui-ux-design-skills/blob/db888866787542311e9e29e15ed92362f5f283e5/docs/01-ui-ux-design-skills-system-spec.md), [S09](https://github.com/sb-dev/ui-ux-design-skills/blob/db888866787542311e9e29e15ed92362f5f283e5/docs/02-ui-ux-design-skills-workflows-and-artifacts-spec.md), [S12](https://github.com/sb-dev/production-skills/blob/20979e0c68ac4b37433374df7fe10ceb2e7ee69a/docs/specs/01-production-skills-family-system.md), [S18](https://github.com/sb-dev/pactwright/blob/207ac08507f9687be9eca105915bbd3db1e1dd4b/docs/research-logs/2026-08-11-pactwright-delivery-graph-and-lifecycle-engineering-spec.md).

- Common need: Locate the owning failure layer, preserve sound work and review only true dependencies.
- Meaningful variations: Research claim/source; legal fact/authority/clause; UX requirement/flow/state; engineering requirement/interface/code/test; business channel/price/delivery/cash. Pactwright scope changes return through its lifecycle.
- Evidence limit: Strong architectural recurrence; owning-domain runtime/business repair evidence still needed for new shared implementation.
- Decision: Share the already accepted principle; retain domain repair units and authority. No central diagnosis engine or cross-project automatic rewrite.

### A04 — Validity / confidence metadata

Source witnesses: [S02](https://github.com/sb-dev/deep-research-skills/blob/80b209968b366662c01a8ded5ecb6c30bb6beb0b/docs/research-logs/2026-09-07-deep-research-skills-new-project-bootstrap-process.md), [S04](https://github.com/sb-dev/legal-skills/blob/b15f3134552ea763d434783d655aea44c0e01925/docs/research-logs/2026-09-08-legal-skills-new-project-bootstrap-process.md), [S09](https://github.com/sb-dev/ui-ux-design-skills/blob/db888866787542311e9e29e15ed92362f5f283e5/docs/02-ui-ux-design-skills-workflows-and-artifacts-spec.md), [S17](https://github.com/sb-dev/pactwright/blob/207ac08507f9687be9eca105915bbd3db1e1dd4b/docs/research-logs/2026-08-11-pactwright-system-architecture.md), [S21](https://github.com/sb-dev/pactwright/blob/207ac08507f9687be9eca105915bbd3db1e1dd4b/src/graph/schema.ts).

- Common need: Prevent evidence from becoming stronger, more current or more broadly applicable during translation.
- Meaningful variations: Event/publication/retrieval dates; legal commencement and valid-as-of; UX VALIDATED_IN_CONTEXT; business cohort/window/cost basis; graph byte revision and delivery completion. None is a universal confidence number.
- Evidence limit: Source-level semantic differences observed; insufficient evidence for a universal validity engine.
- Decision: Preserve original field meanings and add explicit context in the receiving record. No scalar score or enum conversion that invents confidence.

Rejected alternatives are concrete: one cross-domain evidence enum would lose legal and UX meanings; one experiment runtime would confuse research, engineering tests and customer experiments; one universal evaluator would replace separate commercial, legal, UX and technical criteria; one shared pack interpreter would misread incompatible formats; mandatory Pactwright would break independent use. A project-specific integration document is sufficient. Stage 26 may reconsider implementation candidates only after multiple independent production needs are demonstrated.

## 7. Conformance and verification

After writing this review, the original complete §27 was reread. Direct inspection checked the actual six comparison sections, all four candidate analyses, six integration opportunities, six bounded reviews, exact source identities, links, baseline and changed paths. Integrity checks support the substantive review; they do not grade source truth or installed behaviour.

| Requirement | Specification reference | Deliverable / evidence | Verification performed | Result |
|---|---|---|---|---|
| Actual six-project comparison | Original §27 named list | CP01–CP06 and 21 accessed files | Each source contract read at pinned main revision; responsibilities, handoff, return, maturity and decision inspected | PASS |
| Deep Research gathers/synthesises evidence | §27 likely boundaries; §5 | CP01, I01, H01 | Research provenance/contradiction/uncertainty preserved; business facts not invented | PASS |
| Legal determines applicable constraints | §27; accepted HF01–HF07 | CP02, I02, H02 | Exact matter facts, jurisdiction/dates, scope and specialist return preserved; no legal clearance inferred | PASS |
| UI/UX owns interaction and handoff | §27 named comparison; global §2 | CP03, I03, H03 | Actual skill and canonical confidence/hypothesis/approval contracts reviewed; commercial inference kept separate | PASS |
| Software Engineering owns software changes | §27 named comparison; global §2 | CP04, I04, H04 | Inspection, technical contracts, actual test evidence and bounded repair compared; implementation not business outcome | PASS |
| Family owns only family responsibilities | §27; global §2 | CP05, I05, H05, actual registry | Registry remains proposed; consumer/domain state local; no silent migration or central quality score | PASS |
| Pactwright governs authorised delivery | §27; global §2 | CP06, I06, H06; actual source code | Five core node types and pack parser inspected; delivery Evidence and business validation distinct; no assumed pack loader | PASS |
| Four suggested repeated concepts examined | §27 candidate list | A01–A04 | Common need, source witnesses, meaningful variation, evidence limit and explicit decision for every candidate | PASS |
| No premature centralisation | §27 exit; §§2,33,35 | Decisions and actual tree | No shared runtime/schema/graph/evaluator/installer, integration implementation or new platform added | PASS |
| Accepted work preserved | Contract §§2–5 | 118-file baseline and Stage 19 snapshot | All earlier content identities unchanged; previous progress preserved byte-for-byte | PASS |
| Verification and durable evidence | Contract §§5–6 | Review inputs, verifier and actual JSON | Source/link/count/preservation checks executed; substantive findings retained separately | PASS |
| Installed cross-project execution or measured commercial effects | §27 vs §§29–32 | Explicit claim limits throughout | Current stage requires review and opportunities; actual implementations/tests belong to their named later stages | NOT APPLICABLE |

The first local attempt to persist the fetched comparison cache hit an operating-system argument-length limit. The files were then written individually and every fetched byte identity checked. No source was dropped and no partial access was described as a full read. This was a recovered local write error, not missing access or a user blocker.

Final publication-input verification returned **264 PASS, 0 FAIL, exit 0 on Python 3.12.14**, covering 21 accessed sources, six comparisons, four candidate concepts, 72 links and all 118 predecessor identities. The executed JSON records actual results, input identities and limits. To reproduce the source review check, retrieve the 21 pinned files listed in review-inputs.json into an external cache at `<repository>/<path>`, then run `python docs/research-logs/2026-09-13-stage-20-verifier.py --source-root <cache-directory>`. This explicit research cache is not an installed-skill dependency. Final commit/ref/parent/tree/change-scope and immutable remote-content verification is performed only after local conformance and is recorded in the progress receipt. No earlier-stage verifier output is regenerated.

## 8. Outputs, exit and next stage

- [Cross-project review](2026-09-13-stage-20-cross-project-review.md): complete source-informed analysis, decisions and conformance.
- [Review inputs](2026-09-13-stage-20-review-inputs.json): 118 predecessor identities, 21 exact accessed sources, six full comparison records, four candidates and six bounded semantic reviews.
- [Verifier](2026-09-13-stage-20-verifier.py) and [executed checks](2026-09-13-stage-20-executed-checks.json): actual integrity/identity results.
- [Stage 19 progress snapshot](2026-09-13-bootstrap-3-progress-through-stage-19.md): exact previous live index.
- [Current progress](bootstrap-3-progress.md): current state and separate remote completion receipt.

The original Stage 20 exit is satisfied: concrete integration opportunities and their limits are recorded, while Business Building remains independent and domain-owned. No required source, unresolved contradiction, failed prerequisite or current user decision remains. No Stage 20 requirement is deferred. No external repository, registry, production system or source business record was changed.

After this stage’s remote verification, continue immediately with Stage 21. Its inputs are the six unchanged canonical specifications, the complete Stage 19 README design, these ownership/compatibility decisions and the verified branch. Production paths must serve immediate work, with actual authorised licence/contribution terms; optional integrations and pack directories need actual implementation before they appear. Keep the identified format and evidence-state differences explicit when later integration is implemented.
