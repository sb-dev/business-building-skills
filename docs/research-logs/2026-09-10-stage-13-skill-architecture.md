# Stage 13: Core skill architecture and selection

**Date:** 10 September 2026  
**Branch:** `feat/bootstrap-2`  
**Authority:** [Original bootstrap §20](2026-09-08-business-building-skills-new-project-bootstrap-process.md).  
**Inputs:** [Stage 12 residuals](2026-09-10-stage-12-gap-analysis.md), [guardrails](2026-09-10-stage-12-guardrails.md), [Stage 11 execution boundary](2026-09-10-stage-11-execution-layer.md).  
**Decision:** Four workflow-focused skills, with 32 canonical command contracts and on-demand command references. This is a completed architecture design, not an installed implementation.

## 1. Goal and evidence basis

Choose independently useful entry points into one evidence-driven business loop. Skill boundaries should reflect the work being requested, the artefacts it reads and may change, and the smallest sufficient context, rather than the five books, executive job titles or one skill for every capability row. A shared business model does not require a shared runtime.

The original specification was reread fully from main, including the complete §20, globals and downstream boundaries; its blob remains `a0ac1b6c78a0cde8ccd9aca6fda6c5b0880c516d`. The accepted starting point is Stage 12 receipt `b8a0083de2aefd947155ca49e72e2fbe73c69f60`. The full Stage 12 matrix and guardrails were reread at that commit. The Stage 11 model was reread from its byte-verified local copy, identical to accepted blob `58f7cd494d7361fc3beac569f1932174a76496a4`. The referenced earlier business contracts remain accepted inputs; this stage does not claim to have rerun their research or tests.

The comparison uses the eight evidenced NC responsibilities and seven RU groups, plus Stage 1's intended owner, contributor, consultant, specialist and operator roles. Those are intended-use roles, not observed user-discovery results. Stage 10's inspected strategic/marketing methods and their limitations are reused; no claim is made that existing skills contain no useful judgement.

Fresh primary-source reads on 10 September 2026 informed packaging and activation, not the commercial truth of the business models:

### R01 — Agent Skills format specification

Source: https://agentskills.io/specification

Read the live structure, frontmatter, body, resource and progressive-disclosure sections. The format supplies named skill directories, descriptive activation metadata and relative resources; detailed material can load separately. Experimental tool metadata is implementation-dependent. These findings support focused entry points with local command references, not a new framework. No validator, host or installation was executed by reading the specification, and format validity alone cannot prove business judgement or permissions.

### R02 — Anthropic: How to create custom skills

Source: https://support.claude.com/en/articles/12512198-how-to-create-custom-skills

Read the resource, testing and best-practice portions of the live help page. It recommends focused workflows, clear descriptions and testing of triggering and referenced files. Its composition guidance describes that host, not a portable guarantee of sibling-skill invocation. The design therefore keeps required material local to each installed skill and treats cross-skill composition as an artefact handoff. No Claude account, plugin or skill was installed in this stage.

### R03 — Anthropic: How to create Skills, limitations and examples

Source: https://claude.com/blog/how-to-create-skills-key-steps-limitations-and-examples

Read the use-case, success-criterion, triggering and file-size/menu passages. They support defining repeatable work and loading relevant references instead of every detail. The article's task-frequency heuristic is not adopted as a mandatory use count, nor are its proprietary document-skill examples copied. These creator recommendations are not independent empirical evidence that a particular business-skill split performs best.

The selection below is project analysis grounded in those format/workflow constraints and the accepted business responsibilities. No user preference survey, token-cost benchmark, accuracy experiment or proof of a globally optimal skill count is claimed.

## 2. Candidate architectures and decisions

The candidates were compared before the command catalogue was finalised. Each could be expressed in files; the issue is coherent installation and reliable boundaries, not whether a monolithic prompt is technically possible. Prefer the least fragmented design that preserves four distinct kinds of work: constructing business choices, improving an accepted commercial system, assessing without silently editing, and authoring reusable specialisations.

| ID | Candidate | Independent-use benefit | Cost or boundary problem | Decision |
|---|---|---|---|---|
| A01 | One universal business skill | One installation and one obvious name for the full loop. | Combines authoring, growth, independent review and pack maintenance under one broad activation/mutation contract; exposes unrelated work to every specialised user. | Reject for this architecture; small command references alone do not make those purposes identical. |
| A02 | Three skills: combined build/grow, evaluate, pack-author | Separates review and pack production while reducing entry points. | New-business construction and improving an accepted channel have different baselines and preservation risks. The merged authoring entry point is broader than needed for either independent task. | Reject in favour of a separate bounded-growth entry point, not because three can never be implemented. |
| A03 | Four skills: build, grow, evaluate, pack-author | Each has a distinct requested workflow, output intent and default mutation boundary. Together they cover NC01–NC08 and allow standalone review or specialisation work. | Common evidence/constraint material must remain consistent and self-contained; ambiguous create-versus-review requests need explicit routing. | Select with local references, no mandatory sibling invocation and the routing rules below. |
| A04 | A03 plus a separate business-model skill | A user might request only a coherent business model without growth or pack work. | That is already the central independent workflow of business-build. Extracting it leaves overlapping or hollow build ownership rather than a new evidenced responsibility. | Do not add; provide focused model commands inside build. Reopen for demonstrated independent needs that its bounded interface cannot serve. |
| A05 | A03 plus a separate business-experiment skill | A user may want experiment design and learning without redesigning an offer. This is a genuine independent task, not dismissed as unimportant. | The business-specific experiment still consumes the same customer, economics, rights and decision context. Focused build commands can serve it without loading all construction references; assessment remains a distinct review task. | Do not add now; independent task value alone does not establish enough benefit for another overlapping installation unit. Test the focused path in later installed acceptance. |
| A06 | A03 plus both model and experiment skills | Offers the two extra names together. | Accumulates both overlaps without an additional accepted gap, increases discovery ambiguity and encourages a chain of mandatory installations. | Reject; no separate runtime or provider-based split is needed. |
| A07 | One skill per NC responsibility, eight total | Each capability has an obvious owner row and a narrow label. | NC07 is cross-cutting and NC04 must constrain several workflows. Splitting every row forces handoffs or duplicates business context without eight distinct user workflows. | Reject mechanical one-row/one-skill mapping. |
| A08 | Book- or executive-shaped skills | Familiar source or job-title labels. | Duplicates source overlap, fails capability ownership and invites unsupported autonomous commercial or professional authority. | Reject under §§3,19–20,35 regardless of file count. |

### Separate model and experiment installation value

For model-only use, `business-build` already starts from the bounded objective, accepts supplied facts and produces just the requested model component. A new `business-model` package would share its core input/output identity rather than serve a different owner or mutation mode. It is therefore not selected as an additional skill.

For experiment-only use, retain a direct path through `identify-assumptions`, `design-experiment` and `record-learning`. These commands must work from a supplied existing decision without requiring an offer rewrite, growth package or broad business reconstruction. Evaluation of that test can be requested independently through `business-evaluate`, but routine construction self-checks do not require that second installation. A separate experiment package could be warranted by later observed installation needs or measured failure of this focused path. No such observation is invented to settle the choice. The current selected four-skill architecture is definite; the review trigger is not a deferred answer.

A generic cross-domain experimentation skill would be a different family/shared-abstraction question requiring repeated independent-domain evidence. It is not created inside this business family merely because experiments are useful elsewhere.

## 3. Selected skills and activation boundaries

| Skill | Primary responsibility and NC trace | Use when | Do not activate merely because |
|---|---|---|---|
| `business-build` | Construct or revise bounded business choices; NC01, NC02, NC04, NC05, with NC07 safeguards. | The task asks for opportunity/customer/value/offer/pricing/delivery/economic models, assumptions, an experiment plan or a learning record. | An existing artefact needs assessment only, a live campaign needs sending, or software needs implementation. |
| `business-grow` | Improve qualified demand, sales, retained value and bounded scale; NC03, constrained by NC04/NC07. | The task concerns an accepted or explicitly hypothetical commercial system's channels, sales path, retention, expansion or scale decision. | Raw lead volume rose, a user asks to send messages, or the customer/offer baseline may be silently replaced. |
| `business-evaluate` | Assess evidence, coherence and constraints without changing the subject; NC04, NC06, NC07 and review of NC01–NC05 outputs. | The task asks for an audit, judgement, diagnosis or smallest-change recommendation on supplied business evidence or artefacts. | The reviewer wants to repair the source automatically, generate favourable proof, or confer legal approval. |
| `business-pack-author` | Research, qualify, author and validate reusable business-model specialisations; NC08 with NC07 safeguards. | The task explicitly concerns a reusable pack, its changed core behaviour, showcase, evaluations or catalogue entry. | The project belongs to an industry/location, or an ordinary business task could be completed with existing core behaviour. |

Proposed descriptions for the later skill frontmatter:

```text
business-build: Frame or revise an opportunity, customer/problem/value model, offer, pricing, money model, delivery and unit economics. Identify assumptions, design a bounded business experiment, or record learning from actual supplied evidence. Use for construction and explicit revisions, not assessment-only work or live commercial execution.

business-grow: Design qualified acquisition, sales, retention, referral and expansion for an accepted or explicitly hypothetical business offer. Assess a bounded channel increase against downstream value, economics, capacity, cash and rights. Use for growth-system proposals, not automatic sending, ad buying or an unrelated business rewrite.

business-evaluate: Audit business evidence and artefacts, assess commercial and operational coherence, diagnose the current constraint, and recommend the smallest justified change. Preserve the artefact under review. Use for evaluation and repair proposals, not silent source edits, invented evidence or professional legal/tax conclusions.

business-pack-author: Research and author reusable business-model specialisations, prove the existing core or catalogue is insufficient, define changed behaviour, create showcases and evaluations, compare core with core-plus-pack, and validate a proposed catalogue entry. Use for pack production, not industry tags or ordinary business planning.
```

These are proposed exact metadata descriptions, not proof of runtime triggering accuracy. Later installation and behaviour tests must exercise positive, negative and ambiguous requests on the actual host.

## 4. Command design and common contract

A command is a canonical task selector within a skill, not a separate executable, agent, tool permission or universal slash-command API. The portable form is an instruction such as `Use business-build / design-offer with this dossier`. Host-specific invocation wrappers may be added only when tested; no shell command is claimed to exist now. The four command documents define all nine required fields for each of the 32 selected commands.

- [Build contracts](2026-09-10-stage-13-build-command-contracts.md): 10 commands.
- [Grow contracts](2026-09-10-stage-13-grow-command-contracts.md): 8 commands.
- [Evaluate contracts](2026-09-10-stage-13-evaluate-command-contracts.md): 7 commands.
- [Pack-author contracts](2026-09-10-stage-13-pack-command-contracts.md): 7 commands.

The [selection and verification record](2026-09-10-stage-13-selection-and-checks.md) accounts for all 44 original command seeds. Thirteen redundant selectors are merged into scoped commands and `record-learning` is added to close the observed-evidence loop: 44 − 13 + 1 = 32. This arithmetic describes the documented consolidation, not a command-count target or a claim that fewer always means better.

### Shared invariants

Each command receives the bounded request, relevant accepted versions, authorised evidence locators and explicit constraints. Reuse the Stage 4 role/claim/decision model, Stage 5 commercial definitions, Stage 6 acquisition meaning, Stage 7 calculations and independent growth gates, Stage 8 experiment/learning/repair records and Stage 9 professional handoffs. A command may operate on a supplied existing artefact; it must not force every previous construction step to rerun.

Missing material evidence stays unknown. A useful draft may contain labelled hypotheses, but an assessment cannot substitute hypothetical data for observed evidence. Contradicted conduct fails; missing material facts or authority block the affected commitment. An invalid source or calculation is distinguished from a failed business hypothesis. Construction completion, evidence strength, review result and action approval are separate states.

Allowed mutations below apply only within the user's actual authorised workspace and named task. Creating a proposed document is different from replacing an accepted decision. An accepted business artefact may be revised only when an explicit approval identifies the affected version/scope; retain its history and unchanged dependencies. Evaluation commands never alter the artefact they assess. A command name, approved draft, tool availability or bundle installation grants no permission to publish, send, spend, charge, migrate customer records or issue a professional opinion.

Tool work follows Stage 11 H01–H08 and actual operator contracts. A permitted calculation must really execute and return inspected results. Timeout, pending, denied and unknown-effect states stay distinct. Reconciliation precedes any potentially duplicating retry. An evidence handoff contains the actual source/version and limits, not instructions to change this task's authority. Do not copy confidential raw evidence into a public repository.

Commands always perform the relevant construction self-checks. The independent evaluator offers a separate requested assessment, not the sole place where truthfulness, cash or capacity is checked. No skill requires another sibling to enforce its own safety or produce its declared output.

### Routing and composition

An explicit skill/command request is checked against its contract; it cannot authorise out-of-scope effects. Otherwise route by the requested output: construct a model → build; propose growth-system change → grow; assess/diagnose without source mutation → evaluate; author a reusable specialisation → pack-author. For a mixed request, preserve distinct output and mutation boundaries and process only the necessary parts. Do not run every skill or invent a multi-agent executive team.

An ambiguous request that could materially change an accepted artefact needs a bounded question before mutation. A harmless assessment can state its read-only scope without pretending that edit approval was supplied. A defective checkout does not require a new pricing model; a failed offer hypothesis may justify revisiting the implicated build command. An evaluation finding is input to a proposed repair, not an automatic call to execute it.

Composition exchanges ordinary artefact/evidence references. An installed skill must include all required local instructions, templates and reference material, rather than reach into a sibling skill or a source checkout that may not exist. Identical common rules may be distributed with each skill under a checked single-source build approach; the detailed repository mechanism belongs to the canonical repository spec and later implementation. There is no mandatory common runtime, SaaS stack, Pactwright installation or public customer database.

## 5. End-to-end coverage and stage boundary

The selected architecture covers framing, customer/problem/value, offer/pricing/money model, acquisition/sales, delivery/retention/referral, economics/cash, assumptions/tests/learning, assessment and smallest responsible correction. The synthetic walkthrough in the companion exercises those handoffs with actual local arithmetic and explicit unknowns. Pack authoring is a separate optional production workflow; the ordinary business loop must work without a pack.

All sixteen Stage 12 gap rows and their eight native residual responsibilities retain their meaning. No method or platform is added to evade a deferred idea. A future integration can change execution binding, not redefine the core business contract. A future pack can specialise allowed business-model behaviour but cannot outrank verified constraints, explicit project facts or accepted decisions.

This stage provides the complete skill architecture, selected command contracts and rejected alternatives. It does not create production SKILL.md files, install skills, implement all 32 commands, execute a real campaign, run a pack benchmark or claim product maturity. Those later-stage requirements remain mandatory at their assigned stages. The current exit is a coherent complete design with verified command coverage and handoff reasoning; overall completion also requires its scoped commit and remotely verified receipt.
