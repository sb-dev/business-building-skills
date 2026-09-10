# Stage 8: Research and decision-loop checks

**Date:** 10 September 2026  
**Branch:** `feat/bootstrap-2`  
**Authority:** [Original bootstrap §15](2026-09-08-business-building-skills-new-project-bootstrap-process.md); [execution contract](2026-09-09-bootstrap-2-execution-contract.md).  
**Outputs:** [Assumptions, experiments and learning](2026-09-10-stage-08-assumptions-experiments-and-learning.md), [constraint diagnosis and repair](2026-09-10-stage-08-constraint-diagnosis-and-repair.md), [conformance](2026-09-10-stage-08-conformance.md).

## 1. Actual inputs and method

Stage 8 began after Stage 7's content and receipt were remotely verified. The accepted parent is `157f001ec3f35465f0d09868cae2f202d2778e40`, tree `73cd7632625a7cfb477871aa4eda228189df7fe8`, thirty files. The current progress blob at that boundary is `bd9247e55d66db8f1cae09874a23c514ff9855bd`. The original specification was reread from main in complete source ranges 1–525, 526–1050, 1051–1575, 1576–2200 and 2201–2400; its blob remained `a0ac1b6c78a0cde8ccd9aca6fda6c5b0880c516d`. The complete stage-specific acceptance checklist was extracted before substantive authoring and is retained in conformance.

Relevant accepted inputs reread include Stage 2's C01–C22 taxonomy; Stage 3's evidence hierarchy, P25–P27 practice cards and methodological source records S33–S40; Stage 4's evidence, claim, decision and change-impact model; Stage 6's diagnostic separation of message, offer, execution and downstream economics; and Stage 7's explicit economic, capacity, cash and authority gates. Source findings reported in those earlier records remain attributed historical research. This stage does not claim to have reopened the five books, reproduced earlier trials or reread the full papers whose earlier reading was recorded.

Additional methodological research used the primary pages below to verify distinctions about neutral inquiry, planned versus exploratory analysis, sampling and blocking, result interpretation, continuous monitoring and data integrity. This is a bounded design review, not a systematic literature review or empirical validation of the complete skills product. No new external-source quota is imposed by §15. No PDF was used as newly inspected source material in this stage; HTML methods and publication abstracts have their scopes stated explicitly.

The GitHub API supplies repository reads and stage-scoped writes. Local files support document/arithmetic checks, not a claimed Git checkout or clean consumer installation. Only `feat/bootstrap-2` is used; no failed-attempt branch, live campaign, customer contact or business-system mutation is part of this work.

## 2. Methodological source register

Accessed **10 September 2026**. Each finding below is limited to the material actually read. The model is the project's application of the original contract and these distinctions, not a workflow claimed verbatim from a source. No source examples or extended quotations are republished.

<a id="r01"></a>
### R01 — Center for Open Science: Preregistration

**Source:** https://www.cos.io/initiatives/prereg  
**Scope:** Live HTML explanation of prespecification, planned/exploratory work, transparent changes and held-out data.  
**Finding:** A plan recorded before the relevant results makes later deviations and hypothesis generation visible.  
**Limit and application:** No external registration was submitted and no registry is a product dependency. The project uses versioned pre-result contracts; exploratory findings remain valuable without being labelled independent confirmation from the same data.

<a id="r02"></a>
### R02 — Government Digital Service: Using in-depth interviews

**Source:** https://www.gov.uk/service-manual/user-research/using-in-depth-interviews  
**Scope:** Live HTML planning, recruitment, consent, neutral questioning, real examples and secure records guidance.  
**Finding:** Interviews can investigate actual circumstances and needs through relevant participants' accounts.  
**Limit and application:** Guidance is not evidence that an interview establishes population prevalence or willingness to pay. No universal interview count, session length, customer truth or conversion effect is adopted; actual source accounts retain role and sampling context.

<a id="r03"></a>
### R03 — NIST/SEMATECH: Sample sizes and randomised blocks

**Sources:** https://www.itl.nist.gov/div898/handbook/prc/section2/prc242.htm and https://www.itl.nist.gov/div898/handbook/pri/section3/pri332.htm  
**Scope:** Read HTML discussion of the single-proportion normal-approximation sample calculation and the nuisance-factor/blocking design. Source worked-case quantities are not used as fixtures.  
**Finding:** Information requirements depend on the effect/question and analysis design; controlling known nuisance variation is distinct from the treatment of interest.  
**Limit and application:** No single-proportion formula is repurposed as a two-arm, clustered or retention calculator. Blocking does not establish external representativeness or remove every confound. Appropriate statistical calculation remains with a suitable tool or analyst.

<a id="r04"></a>
### R04 — American Statistical Association: Interpretation beyond a threshold

**Source:** https://magazine.amstat.org/blog/2016/04/01/pres-apr16/  
**Publication:** 1 April 2016, official ASA discussion of its statement on p-values.  
**Scope:** Read the original interview on effect magnitude, uncertainty, assumptions and transparent analysis. The related ASA release was inspected for context; the journal DOI route, https://doi.org/10.1080/00031305.2016.1154108, returned 403, so a full journal-statement read is not claimed here. Reader comments were not evidence.  
**Finding:** One numerical threshold cannot replace interpretation of the study and its assumptions.  
**Limit and application:** The project does not claim the statement bans significance testing or proves commercial equivalence. Practical relevance, uncertainty and business constraints remain separate from statistical labels.

<a id="r05"></a>
### R05 — Johari, Koomen, Pekelis and Walsh: Always Valid Inference

**Source:** https://pubsonline.informs.org/doi/abs/10.1287/opre.2021.2135  
**Publication:** Online 10 August 2021; Operations Research 70(3), 1806–1821, May–June 2022.  
**Scope:** Publisher abstract and bibliographic metadata only; no full proof, implementation or performance replication.  
**Finding:** Valid inference under continuous monitoring is a distinct methodological problem, with purpose-designed sequential procedures.  
**Limit and application:** No proprietary platform or arbitrary peeking rule is selected. The experiment contract specifies fixed-horizon or a suitable sequential plan, while safety monitoring remains active independently.

<a id="r06"></a>
### R06 — Microsoft Research: Diagnosing Sample Ratio Mismatch

**Source:** https://www.microsoft.com/en-us/research/publication/diagnosing-sample-ratio-mismatch-in-online-controlled-experiments-a-taxonomy-and-rules-of-thumb-for-practitioners/  
**Publication:** July 2019, KDD publication record.  
**Scope:** Institutional abstract, not the full paper's taxonomy or individual cases.  
**Finding:** A detected mismatch between expected and observed allocation can signal different data-quality problems and needs diagnosis before a trustworthy conclusion.  
**Limit and application:** A small ordinary chance imbalance is not automatically a defect, and the symptom does not identify its cause. No universal SRM cutoff or complete statistical diagnostic is implemented by the bootstrap fixtures.

<a id="r07"></a>
### R07 — Microsoft Research: Data Quality for Trustworthy A/B Testing

**Source:** https://www.microsoft.com/en-us/research/articles/data-quality-fundamental-building-blocks-for-trustworthy-a-b-testing-analysis/  
**Publication:** 9 November 2021.  
**Scope:** Read HTML narrative on missingness, duplicates, assignment units, delays and consistent treatment information; no image-derived measurement used.  
**Finding:** Integrity problems can affect the meaning and reliability of an experiment's reported result.  
**Limit and application:** This is provider practice, not a universal data platform specification or proof that all proposed checks suffice. The project retains decision-relevant integrity questions without adopting its branded metric framework or rebuilding analytics infrastructure.

## 3. Resolutions and rejected shortcuts

| Comparison | Resolution | Boundary retained |
|---|---|---|
| Uncertainty versus consequence | Separate evidential position from the effect of being wrong and explain priority in the pending decision. | No opaque multiplied risk score or fabricated probability. |
| Cheapest activity versus cheapest adequate evidence | Compare the existing-data audit, inquiry, concept, paid-choice, delivery and comparison options against the claim. | A cheap interest survey cannot validate paid retention; a large trial is not needed to establish a proved calculation defect. |
| Planned test versus exploration | Preserve a frozen version and actual deviations; label new hypotheses and seek independent evidence when confirming them. R01. | No post-result rewrite that turns failure into prespecified success. |
| Hypothesis result versus action | A result can support a narrow claim while cash, capacity or authority blocks the proposed commitment. | No statistical or qualitative success overrides Stage 7 gates or customer rights. |
| Valid inconclusive versus invalid inference | Keep insufficient discrimination or immature outcomes separate from evidence that cannot answer the intended question. | Neither is automatically proof of a failed business or of no effect. |
| Local symptom versus binding constraint | Use the objective, horizon, rival explanations and actual resource/economic dependencies. | The lowest conversion percentage or busiest resource is not a universal diagnosis rule. |
| Preservation versus justified change | Retain accepted choices unless implicated; permit the smallest coherent multi-layer change when fundamental evidence warrants it. | No routine full-business rewrite, and no preservation of unsafe or deceptive choices merely because they were approved. |
| Observation versus busy work | Record what changed in the decision's knowledge and what remains unresolved. | Calls, documents, test counts and activity are not themselves validated learning. |

No current-stage user-owned decision is unresolved. Actual customer populations, allowed exposure, budget, statistical model choice and jurisdiction-specific constraints remain future-task inputs. Their absence in a synthetic design check is not silently filled with invented real-world facts.

## 4. Complete synthetic loop: a bounded service-delivery decision

**Everything in this section is synthetic**, including people, observations, costs, permissions and dates. These are original design fixtures, not actual client research, primary progressive examples or installed-skill outputs.

### Assumption and decision before the test

An imagined service has accepted customer/value/offer versions `customer-v1`, `value-v1` and `offer-v1`. The proposed sale is 120 currency units per engagement. Direct delivery labour is valued at 30 per hour and another direct cost is 10 per engagement. Acquisition cost is excluded and explicitly unknown for a future growth decision; no profit or CAC claim is made. The owner is considering additional commitments but first needs delivery-work evidence.

Assumption `A-SERVICE-v1`, class AS07: each of three specified pilot engagements can deliver the accepted output at the agreed quality using at most three active work-hours. Uncertainty is unresolved; consequence is that more work could invalidate the current price/capacity expectation. This dependency informs AS10 but is not an assertion that three pilots prove scale economics. Customer need and wider repeat behaviour are not being tested.

### Frozen experiment record

| Field | Synthetic contract `T-SERVICE-v1` |
|---|---|
| assumption | A-SERVICE-v1 and its work/cost dependency, leaving demand and retention unresolved. |
| hypothesis | All three defined pilot engagements finish acceptably with no more than three active work-hours each. A rival is that necessary quality review takes materially longer. |
| cheapest valid test | Observe three bounded manual deliveries with recorded work and output checks. Interviews cannot reveal actual backstage time; a new acquisition campaign would add cost without first resolving fulfilment. No suitable historical delivery records exist in the fixture. |
| target population | Three named fictional eligible pilot engagements at the existing scope; no population-level demand, mean-time or causal generalisation is intended. |
| success / failure signal | Each output meets the unchanged quality criteria and each engagement uses at most three hours. One counterexample challenges the stated all-three work prediction; missing records leave the test uninterpretable or incomplete. |
| guardrails | Synthetic approval covers these three pilots only, a two-week window, at most fifteen total active hours and 500 direct-cost units, with ordinary rights/quality controls and recovery for existing promises. The internal three-hour hypothesis is not a customer-facing guarantee. |
| duration / sample requirements where relevant | All three deliveries must reach the agreed completion check within the window. Three is the scope of this bounded case, not a statistically sufficient sample for the market or a universal pilot count. |
| confounders | Hold accepted scope/quality definitions fixed; record case complexity, waiting, rework and customer inputs. No baseline comparison establishes a causal time-saving effect. |
| decision rule | If the exact quality/work prediction holds, review further operational/economic evidence before proposing a limited next commitment. If it is challenged, do not scale the current work assumption and investigate the responsible step. If data are missing, retain uncertainty and repair measurement. A guardrail breach stops the affected work. |

### Observations, learning and repair

All three fictional outputs meet their existing quality criteria. Recorded active work is 4, 4.5 and 3.5 hours: twelve hours total. Direct cost is 130, 145 and 115; total commercial consideration is 360, declared direct cost 390 and direct contribution -30. The fifteen-hour and 500-unit guardrails are not breached, but the all-three three-hour hypothesis is challenged. Those amounts are independently checked in the companion verifier.

| Learning field | Synthetic record `L-SERVICE-v1` |
|---|---|
| assumption | Preserve A-SERVICE-v1, its unresolved prior work estimate and commercial consequence. |
| test | Preserve T-SERVICE-v1, three completed pilot records, unchanged scope/quality and actual total work/cost. No causal time-saving experiment was run. |
| observed evidence | Source IDs `service-1`, `service-2`, `service-3` hold the stated work and acceptable output events. They are explicitly synthetic and cannot enter a real evidence register as customers. |
| result | The bounded work prediction is challenged; direct contribution on the declared basis totals -30 despite acceptable outputs. Guardrails remained within limits. |
| interpretation | The current work assumption cannot justify the proposed increase. The evidence does not refute the customer problem or prove why review work took longer. A large-market average or permanent unviability is not inferred. |
| decision | Hold additional commitments under that assumption. Preserve customer-v1, value-v1 and offer-v1; honour existing pilot promises. Route investigation to delivery work/cost, not a wholesale customer or brand rewrite. |
| what remains unknown | Which necessary tasks account for the extra work, whether a safe process change helps, variable complexity, future acquisition/support costs, repeated value and larger-volume capacity. |
| next experiment / commitment | Inspect task-level work first. Only if that evidence supports a specific process correction, propose a new bounded contract with unchanged acceptance criteria and fresh resource/authority checks. No new spending or price change is automatically approved. |

The constraint finding is a provisional delivery-work/economic limitation, routed through CT06 with the Stage 7 cost contract. It is not falsely labelled an accounting gross-margin result under CT07. The repair preserves accepted customer/value/offer versions, identifies the extra-work hypothesis and verifies any subsequent correction before revised intake. If genuine fixed-scope delivery requirements make a local correction insufficient, scope or price changes require evidence and an explicit approved new version rather than hidden quality reduction.

## 5. Decision-rule, integrity and preservation fixtures

These are additional **synthetic** checks. Intervals below are supplied artificial inputs solely to exercise a decision rule; they were not estimated from real data and have no claimed confidence coverage. Valid inference, population and maturation flags in the fixture are stipulated facts for control-flow testing, not statistical tests of actual observations. The verifier is a temporary test program, not a production decision engine.

| ID | Fixed case and expected result |
|---|---|
| S01 | The complete service loop above must compute twelve work-hours, 390 direct cost and -30 contribution, challenge the work prediction without a resource stop, and preserve the three accepted versions. |
| S02 | For a predeclared worthwhile-effect threshold 0.02, artificial bounds [0.03,0.05] support that threshold, [-0.01,0.01] challenge it, and [0.00,0.04] are inconclusive. The upper boundary [0.00,0.02] remains inconclusive; [0.02,0.03] meets the specified support rule. These are project fixture conventions, not a universal inference method. |
| S03 | Even the supportive S02 result cannot permit the proposed change when its cash, capacity or action-authority input is blocked. The evidence result stays supportive within scope; the action is blocked separately. |
| S04 | The favourable interval with a different population, missing data-integrity clearance or a changed frozen contract is not interpretable for the intended inference. Preserve the actual observation, not a success label. |
| S05 | The same interval before the required follow-up matures is inconclusive and cannot be presented as the completed planned result. Safety monitoring is not postponed while waiting. |
| S06 | A breached truthfulness/participant-safety guardrail stops the affected exposure even when the primary result is favourable. This is not permission to infer a clean completed-run effect. |
| S07 | Missing, unordered or non-finite interval inputs cannot create a supported claim. Missing evidence remains incomplete; malformed numeric data is explicitly rejected rather than coerced to zero. |
| S08 | A decision plan whose meaningful result regions all map to the same declared success/commitment fails the minimum decision-changing check. This structural check is necessary but not sufficient; semantic review must also verify that outcomes genuinely discriminate. |
| S09 | The least expensive candidate is an inadequate interest survey at cost 5; adequate delivery observation costs 90; an adequate larger study costs 300. Select 90 among the explicitly adequate feasible candidates. When none is adequate/feasible, return no selection rather than weakening the claim. |
| S10 | A proposed CT14 measurement repair changing only the defective measurement version preserves customer/value/offer/price/channel/delivery. A proposal that also silently replaces the offer fails preservation; a justified, explicitly affected offer change still requires separate approval. |
| S11 | Wrong denominator arithmetic, an incomplete repeat window and a genuine price mismatch receive measurement, observation or commercial review respectively, not automatic full-business pivots. Qualitative review confirms the route; no universal root-cause classifier is asserted. |

## 6. Verification and stage boundary

The final complete run returned 51 PASS, 0 FAIL, exit 0. The initial phrase-matching failure, subsequent semantic corrections and two added guardrail/plan checks are recorded in conformance, together with the exact executed checker and named outcomes. No expected result or required field was weakened. The direct review covered every named class/field and all eleven synthetic probes. The service fixture calculated twelve hours, 390 direct cost and -30 contribution; all remained synthetic, not observed business results. A rerun after recording the complete evidence matched the full output byte-for-byte and exited 0. Coverage means ten assumption classes, nine experiment fields, eight learning fields and all five model responsibilities; it does not mean ten real experiments were run. The selected fifteen routing entries and eight repair fields are justified project design, not invented specification quotas.

Stage 9 receives bounded questions about claims, participant information, data/consent, terms, guardrails, rights and professional constraints. No legal conclusions, installed-agent results, primary-example coverage or later-stage maturity follow from these model checks. Overall completion requires the actual stage-scoped commit and verified remote receipt.
