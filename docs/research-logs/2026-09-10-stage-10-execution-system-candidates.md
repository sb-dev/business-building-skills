# Stage 10: Execution-system candidates

**Date:** 10 September 2026  
**Branch:** `feat/bootstrap-2`  
**Authority:** [Original bootstrap §17](2026-09-08-business-building-skills-new-project-bootstrap-process.md).  
**Companions:** [Landscape, method and TC01–TC13](2026-09-10-stage-10-capability-landscape.md), [reuse decisions and boundaries](2026-09-10-stage-10-reuse-decisions-and-boundaries.md), [conformance](2026-09-10-stage-10-conformance.md).

These are the remaining 13 entries in the same 26-candidate assessment. All source material was accessed on 10 September 2026 at the scope stated. The 15 fields retain the original specification labels. USE is conditional reuse of the named execution responsibility, not an installed system, permission to act or a compulsory provider choice. Licence scope, source facts, project analysis and actual execution remain distinct under the landscape’s method.

<a id="tc14"></a>

### TC14 — PostHog product analytics and experiments

**Category references:** LC12, LC13, LC19, LC20, LC21. See the exact original names in the coverage matrix.

| Field | Assessment |
|---|---|
| name | PostHog product analytics and experiments |
| source | [Analytics](https://posthog.com/docs/product-analytics), [experiments](https://posthog.com/docs/experiments), [licence](https://github.com/PostHog/posthog/blob/master/LICENSE). Product and experiment overview text plus root licence read (847d9d3def03458035447bdae131e1981e2a63da); no event dataset, SDK or statistical engine executed. |
| licence | Root licence is MIT Expat outside separately licensed enterprise and third-party portions. Hosted service terms and enterprise rights are separate; do not describe the whole product as unrestricted MIT. |
| maturity | Documented integrated product with funnel, retention, path and experiment features. Public availability does not establish our instrumentation, causal validity or operational performance. |
| installation / access model | Approved project with event capture and appropriate API/SDK access. Hosting and plan choice require their own assessment; no self-hosted or cloud account was provisioned. |
| production responsibility | Capture/query product events and run existing experiment machinery; use its inspection and validity reports instead of rebuilding these execution functions. |
| deterministic vs generative role | Deterministic reporting and statistical inference with optional AI-assisted interpretation. Generated anomaly explanations remain hypotheses rather than established root causes. |
| data requirements | Event definitions, stable analysis units, cohorts, exposure/assignment, observation horizon and privacy controls; revenue/cost inputs require explicit provenance. |
| provider coupling | PostHog event/person/group semantics, query system, SDK behaviour and plan features; preserve definitions when moving reports between systems. |
| composability | Useful return-evidence provider for Stage 6–8. Join data only where permitted and do not silently treat users, accounts and paying customers as one unit. |
| quality suitability | Existing anomaly and experiment-validity capabilities are meaningful overlap. Their presence still does not authorise scale or prove customer value and cash feasibility. |
| maintenance | Current product documentation and licence inspected; no full feature or version compatibility audit. Revalidate selected capabilities and capture behaviour before production. |
| privacy / legal constraints | Autocapture and replay can expose sensitive information; minimise and restrict capture, identity joins, retention and access under Stage 9. |
| USE / ADAPT / REFERENCE / REJECT | USE — optional existing analytics/experimentation system where suitable; not a compulsory migration or a new native analytics engine. |
| gaps | Cross-system unit economics, dated obligations and evidence-qualified commercial repair remain unproved by the inspected product overviews; do not claim PostHog lacks all analysis or judgement. |

<a id="tc15"></a>

### TC15 — GrowthBook feature flags and experimentation

**Category references:** LC13, LC20. See the exact original names in the coverage matrix.

| Field | Assessment |
|---|---|
| name | GrowthBook feature flags and experimentation |
| source | [Overview](https://docs.growthbook.io/overview), [using GrowthBook](https://docs.growthbook.io/using), [licence](https://github.com/growthbook/growthbook/blob/main/LICENSE). Warehouse-native/SDK and analysis workflow plus licence read, blob 0a17616ab12bebe8061d8c101597ed590dbe2c5e. No SDK, SQL query or inference run executed. |
| licence | MIT Expat for the non-enterprise portions; named enterprise directories and third-party components have separate terms. Hosted accounts and enterprise features are not automatically licensed by the root MIT text. |
| maturity | Documented experimentation system with SDK and analysis workflows. No project-specific assignment, power or rollout-quality evidence was produced. |
| installation / access model | Cloud or a separately validated self-hosted setup, SDK/flags and an authorised data source. Do not assume every installation includes the same enterprise features. |
| production responsibility | Own flag assignment and experiment measurement where the configured design is appropriate; reuse existing A/B infrastructure. |
| deterministic vs generative role | Deterministic assignment/query execution and statistical inference; neither provides an automatic causal conclusion when design assumptions fail. |
| data requirements | Experiment plan, assignment unit, exposure logs, metric SQL, comparison window, exclusions and authorised data-source credentials. |
| provider coupling | Flag and SDK semantics plus warehouse queries and statistical settings. Warehouse-native architecture can retain source data ownership, but still requires access review. |
| composability | Return the actual plan/settings, data checks and results into Stage 8. Keep the business decision and independent Stage 7 gates outside rollout status. |
| quality suitability | Suitable alternative to an integrated event-platform experiment when data already lives in a warehouse. More machinery is not justified for a simple observed delivery defect. |
| maintenance | Current usage and licence pages inspected. No claim about the latest SDK version, account features or a completed clean install. |
| privacy / legal constraints | Experiment exposure and data queries require approval and purpose restrictions. Flag access is not permission to expose every user or override guardrails. |
| USE / ADAPT / REFERENCE / REJECT | USE — appropriate existing experimentation option; do not build a universal experiment runtime. |
| gaps | Hypothesis choice, adequacy of the test, interpretation limits and acceptable commercial commitment still require explicit business ownership. |

<a id="tc16"></a>

### TC16 — Mailchimp Marketing API

**Category references:** LC07, LC10, LC15. See the exact original names in the coverage matrix.

| Field | Assessment |
|---|---|
| name | Mailchimp Marketing API |
| source | [Fundamentals](https://mailchimp.com/developer/marketing/docs/fundamentals/). Audience/campaign, authentication, roles, API version and limit sections read; no audience imported or message sent. |
| licence | Commercial hosted service with plan and developer terms. Source samples or an OpenAPI schema do not grant a licence to contact recipients or redistribute audience data. |
| maturity | Documented v3 marketing API and operational resources. Delivery and campaign reporting are not measured incremental business effect. |
| installation / access model | Approved account, plan and API key or OAuth as appropriate. Choose least necessary role rather than automatically adopting an admin recommendation. |
| production responsibility | Manage approved audiences and campaign delivery and provide relevant event reports. Keep the actual sending system outside this skills repository. |
| deterministic vs generative role | Deterministic operations and provider reports; audience selection and message interpretation require separate evidence and review. |
| data requirements | Recipient identity, relationship/permission, suppression state, message version, intended purpose and appropriate campaign/event definitions. |
| provider coupling | Audience, tags, segments, data-centre endpoints and API authentication semantics are provider-specific; do not create a parallel cross-project customer database. |
| composability | Receive an approved brief, execute through the owner and return delivery/response evidence. Duplicate audiences or touches must not inflate new-customer counts. |
| quality suitability | Suitable established delivery option for appropriate campaigns. An API success or email open does not prove consent, intent or profitable acquisition. |
| maintenance | Current fundamentals label v3 and older versions differently. Inspect selected endpoints, limits and role state before real use; no deliverability test conducted. |
| privacy / legal constraints | Protect tokens; honour opt-outs and Stage 9 purpose constraints. A saved address or public contact detail is not blanket permission. |
| USE / ADAPT / REFERENCE / REJECT | USE — an existing approved email platform, not a reason to implement a native sender or force every business onto Mailchimp. |
| gaps | Fit, incremental effect, truthful claims and the downstream economic decision remain separate from audience/campaign execution. |

<a id="tc17"></a>

### TC17 — Customer.io messaging and data APIs

**Category references:** LC07, LC15, LC16. See the exact original names in the coverage matrix.

| Field | Assessment |
|---|---|
| name | Customer.io messaging and data APIs |
| source | [API guide](https://docs.customer.io/integrations/api/customerio-apis/), updated 1 September 2026. Actual content at the end of the navigation-heavy page read: Pipelines/Track/App APIs and reporting webhooks. No workflow or profile mutated. |
| licence | Commercial hosted service under provider terms. API documentation access is not a redistribution licence for customer data or service implementation. |
| maturity | Documented event-driven messaging platform with multiple API roles. No claim that a workflow improves retention for the user’s business. |
| installation / access model | Authorised workspace and API-specific credentials. Current guidance favours Pipelines for new ingress; App API has distinct send/query responsibilities. |
| production responsibility | Handle approved event-based messaging and return message events. Retention strategy and customer rights remain outside an automation trigger. |
| deterministic vs generative role | Data ingress, workflow execution and reports, with optional AI features distinct from the inspected API contract. |
| data requirements | Profiles, event identities/timestamps, permitted attributes, message definitions and suppression/consent facts appropriate to the exact purpose. |
| provider coupling | Provider semantic events and workspace/identity models; some ingestion events can trigger destructive or suppressing operations, so method names alone do not indicate safety. |
| composability | Use explicit operation semantics in handoffs and reconcile returned events. A POST is not necessarily a harmless append or an immediate validated result. |
| quality suitability | Suitable when event-based journeys justify the integration. Message opens, workflow counts and automated retention offers are not achieved customer value. |
| maintenance | Current dated API guidance inspected, including the focus on newer ingress APIs. No migration, rate-limit or delivery test performed. |
| privacy / legal constraints | Keep purpose, suppression and data-out destinations controlled. Do not infer broad messaging or deletion authority from an API key. |
| USE / ADAPT / REFERENCE / REJECT | USE — optional existing lifecycle-message execution when needed; not an autonomous retention engine owned by the business skill. |
| gaps | Whether an intervention benefits an appropriate customer economically and respects exit rights needs evidence beyond trigger execution. |

<a id="tc18"></a>

### TC18 — Zendesk Support / Ticketing API

**Category references:** LC16. See the exact original names in the coverage matrix.

| Field | Assessment |
|---|---|
| name | Zendesk Support / Ticketing API |
| source | [Ticketing introduction](https://developer.zendesk.com/api-reference/ticketing/introduction/). Ticket/workflow scope, linked authentication, pagination and ticket-creation idempotency explanation read. Initial generic route failed; corrected official route worked. No ticket operation executed. |
| licence | Commercial hosted support service with developer terms. Public API examples and schema do not licence reuse of customer conversations or the platform itself. |
| maturity | Documented support system with operational ticket workflows. No measured support-quality or resolution-time performance established here. |
| installation / access model | Approved Zendesk account and current permitted authentication/role. Read/export can be sufficient for analysis; ticket writes require separate approval. |
| production responsibility | Own support tickets, relevant user/organisation state and authorised workflows; return evidence of actual issues and resolution. |
| deterministic vs generative role | Deterministic records and operations. Summaries or predicted reasons remain separate from the original customer account and real outcome. |
| data requirements | Ticket identity, timestamps, issue type, severity, status meaning, customer cohort and permitted conversation content. |
| provider coupling | Provider status, workflow and idempotency semantics; finite retry windows do not imply global exactly-once delivery. |
| composability | Feed support observations into Stage 4/7 without copying an entire help desk into the repository. Preserve duplicates and reopened issues explicitly. |
| quality suitability | Suitable support source and operator. Ticket closure is not necessarily customer resolution; support volume mixes useful requests and failure demand. |
| maintenance | Current introduction includes operation-specific retry semantics; validate the chosen operation before relying on retries. No support SLA or integration audit claimed. |
| privacy / legal constraints | Conversations can be sensitive. Minimise extracts, control access and do not publish customer identifiers to demonstrate evidence traceability. |
| USE / ADAPT / REFERENCE / REJECT | USE — preserve a suitable existing support system and operator; no native help-desk implementation. |
| gaps | Cause, business consequence, service improvement and retention interpretation require evidence beyond ticket counts or status alone. |

<a id="tc19"></a>

### TC19 — Xero Accounting API through official OpenAPI descriptions

**Category references:** LC05, LC17. See the exact original names in the coverage matrix.

| Field | Assessment |
|---|---|
| name | Xero Accounting API through official OpenAPI descriptions |
| source | [Official OpenAPI README](https://github.com/XeroAPI/Xero-OpenAPI/blob/master/README.md), blob 0f4acdc6463e4424f210a0220ba377603fef73ab. Full README/licence statement inspected after the developer overview returned only a JavaScript shell. No accounting schema body, ledger or SDK run claimed. |
| licence | Official OpenAPI descriptions carry MIT terms; Xero hosted accounting/API access remains governed by its service and developer agreement. These are not interchangeable permissions. |
| maturity | Provider-maintained API descriptions identified as in-release and used by SDKs. This is not evidence of correct client books or an independent accounting audit. |
| installation / access model | Authorised organisation and OAuth 2.0 integration using the current official descriptions and appropriate scopes, verified before implementation. |
| production responsibility | Keep accounting records and professional treatment in the accounting system; export approved figures or perform specifically authorised operations. |
| deterministic vs generative role | Deterministic record/API functions; a generated accounting explanation or schema does not settle tax or recognition policy. |
| data requirements | Organisation, account mappings, periods, transaction identities and qualified treatment. Cash dates and recognition dates must remain distinct. |
| provider coupling | Xero accounting objects, tenant/access model and region-specific payroll descriptions; do not imply one global payroll/tax implementation. |
| composability | Consume reviewed reports through Stage 7’s calculation contract. No duplicate ledger or automatic posting merely because a business scenario exists. |
| quality suitability | Suitable accounting-system candidate, but the inspected README does not establish every endpoint’s correctness or a complete integration. |
| maintenance | The repository describes versioning and API-diff checks. Monitor actual selected schema/version changes; the existence of checks is not a claimed run in this bootstrap. |
| privacy / legal constraints | Least-privilege financial access and appropriate professional approval are required. No actual tax result, client posting or private financial disclosure occurred. |
| USE / ADAPT / REFERENCE / REJECT | USE — optional established accounting owner; selection is conditional on a real business’s existing system and needs. |
| gaps | Commercial assumptions, marginal cost bridges and the decision to grow remain outside a ledger/API description; no custom accounting platform is justified. |

<a id="tc20"></a>

### TC20 — Stripe payments, Billing and billing analytics

**Category references:** LC04, LC05, LC06, LC17. See the exact original names in the coverage matrix.

| Field | Assessment |
|---|---|
| name | Stripe payments, Billing and billing analytics |
| source | [API overview](https://docs.stripe.com/api), [Billing analytics](https://docs.stripe.com/billing/subscriptions/analytics). REST/sandbox/version boundary and configurable metrics/export sections read. No account, key, charge, subscription or refund executed. |
| licence | Hosted payment/billing service under applicable service terms; separately licensed clients or skills would need their own checks. No right to process payments follows from public documentation. |
| maturity | Documented transactional and reporting platform. A sandbox or vendor benchmark is not proof of actual collections, satisfaction or local unit economics. |
| installation / access model | Approved account and correct live or sandbox credentials; API version and operation-specific behaviour must be verified. No credentials were requested or used here. |
| production responsibility | Own payment/billing execution and its event states; provide invoice, collection, adjustment and configured subscription reports. |
| deterministic vs generative role | Deterministic transaction state and computed analytics. Configurable metrics and benchmarks are provider-defined, not universal financial truth. |
| data requirements | Canonical transaction/customer IDs, prices/terms, currency, event dates, adjustments and the exact active-subscriber/discount metric configuration. |
| provider coupling | API version, payment states, metric settings and settlement context. Retain source definitions before deriving N, C, CAC or LTV under Stage 7. |
| composability | Use exports or authorised reads as evidence; distinguish billing, recognition and usable cash. Reconcile duplicate events rather than count every notification as a sale. |
| quality suitability | Suitable execution and evidence provider. Its configured active-subscriber boundary can differ between start-of-period and first-payment events. |
| maintenance | Current API and analytics text read; no chosen SDK or account-version validation. Dated settings and exports are required before comparing periods. |
| privacy / legal constraints | Payment data, customer rights, recurring terms and refunds require scoped authority. A test result cannot authorise a live charge. |
| USE / ADAPT / REFERENCE / REJECT | USE — existing payment/billing infrastructure, not a native processor or universal pricing optimiser. |
| gaps | Cost-to-serve, fulfilled value, voluntary retention and full cash obligations are not supplied by billing metrics alone. Do not import an unexplained lifetime ratio. |

<a id="tc21"></a>

### TC21 — Google Sheets and Sheets API

**Category references:** LC05, LC06, LC18, LC22. See the exact original names in the coverage matrix.

| Field | Assessment |
|---|---|
| name | Google Sheets and Sheets API |
| source | [Concepts](https://developers.google.com/workspace/sheets/api/guides/concepts), [CellData reference](https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/cells#CellData). Spreadsheet/range operations and distinction between entered and effective values inspected; no spreadsheet created or recalculated. |
| licence | Hosted spreadsheet service/API terms govern use. Documentation CC BY 4.0 and sample Apache-2.0 notices do not grant access to private sheets. |
| maturity | Documented spreadsheet and API environment. Correct formulas, audited assumptions and financial treatment are still separate acceptance questions. |
| installation / access model | Authorised spreadsheet/account and appropriate API access or human-operated workbook; use actual document IDs and explicit read/write boundaries. |
| production responsibility | Own transparent linked calculations and scenario presentation when a spreadsheet is appropriate, rather than have an LLM perform arithmetic in prose. |
| deterministic vs generative role | Spreadsheet formula evaluation is deterministic under its inputs/settings; formula generation and business interpretation remain reviewable generative work. |
| data requirements | Input sources, named units/periods, formulas, ranges, precision/rounding policy and expected reconciliations; preserve both definitions and results. |
| provider coupling | Sheets formula support, locale/time settings, API ranges and collaborative changes. Do not assume Excel or another engine evaluates every formula identically. |
| composability | Return executed values, errors and input/output versions under Stage 7 HC01–HC08. A written formula is not proof of a recalculated cell. |
| quality suitability | Suitable when linked scenarios need human inspection; a simple calculation may need less machinery. No forecast is validated just because its cells recalculate. |
| maintenance | Concept guide was updated 22 July 2026; selected API behaviour and effective-value fields were checked, not a complete workbook compatibility test. |
| privacy / legal constraints | Client financial sheets require controlled sharing and least-privilege editing. No automatic upload of private records to a public or shared workbook. |
| USE / ADAPT / REFERENCE / REJECT | USE — conditional spreadsheet calculation owner, not a mandatory cloud dependency for every installed skill. |
| gaps | Input truth, accounting policy, observation uncertainty and justified commitment remain outside spreadsheet arithmetic. |

<a id="tc22"></a>

### TC22 — openpyxl spreadsheet file library

**Category references:** LC05, LC18. See the exact original names in the coverage matrix.

| Field | Assessment |
|---|---|
| name | openpyxl spreadsheet file library |
| source | [Official documentation](https://openpyxl.readthedocs.io/en/stable/), [formula handling](https://openpyxl.readthedocs.io/en/stable/simple_formulae.html). Introduction, licence, security warning and formula limits read; not installed or executed for a workbook here. |
| licence | MIT/Expat identified in official documentation. Preserve required notices for distributed software; local dependencies and files have their own rights. |
| maturity | Established documented file library, but the retrieved stable page identifies an older 3.1.3 build. That page is not asserted to be the latest release. |
| installation / access model | Install a compatible pinned Python package when file authoring is needed. Do not equate available import or written formula with a calculation engine. |
| production responsibility | Read/write supported spreadsheet file structures and formulas; actual formula evaluation must be performed elsewhere. |
| deterministic vs generative role | Deterministic file manipulation; the official formula page explicitly says it does not evaluate formulas. Cached data is not a fresh calculation. |
| data requirements | Authorised workbook bytes, supported features, formula definitions and separate expected/recalculated values where required. |
| provider coupling | OOXML feature support and Python/library version; macros, special formulas and round trips need explicit compatibility checks rather than assumptions. |
| composability | Useful file layer alongside a suitable spreadsheet/calculation owner. It is not a replacement for accounting software or full Excel/Sheets semantics. |
| quality suitability | Good narrowly scoped library. Reject the proposal to use it alone as proof of financial-model recalculation. |
| maintenance | Check package releases and supported Python version at installation; inspected docs describe volunteer maintenance and security limits, not a guaranteed SLA. |
| privacy / legal constraints | Treat untrusted workbook content as untrusted input; apply XML safety and data-access controls. Do not run macros or external content by inference. |
| USE / ADAPT / REFERENCE / REJECT | USE — for file authoring/inspection only; explicitly not as the sole formula evaluator. |
| gaps | The missing evaluation capability should be supplied by an existing appropriate tool, not hidden behind a success code or reinvented as an accounting engine. |

<a id="tc23"></a>

### TC23 — statsmodels statistical and time-series library

**Category references:** LC05, LC13, LC22. See the exact original names in the coverage matrix.

| Field | Assessment |
|---|---|
| name | statsmodels statistical and time-series library |
| source | [Time-series catalogue](https://www.statsmodels.org/stable/tsa.html), [testing/stability](https://www.statsmodels.org/stable/about.html), [licence](https://github.com/statsmodels/statsmodels/blob/main/LICENSE.txt), blob 47cd54eec489af242da0e1a9fe00f1ed15cf2e69. Catalogue and limitations read; no model fitted or forecast benchmark run. |
| licence | BSD-3-Clause terms identified in the repository licence, including notice and non-endorsement conditions. No library code is copied into this research. |
| maturity | Documented statistical library with explicit testing and numerical/API caveats. Its existence is not proof that a selected model fits a new business. |
| installation / access model | Pinned compatible Python package and an approved analysis environment; select the actual model only after the statistical question and data are specified. |
| production responsibility | Perform suitable estimation, diagnostics and forecasting calculations; do not implement a new generic inference package. |
| deterministic vs generative role | Deterministic statistical computation conditional on model/data/settings; any generated model choice or causal interpretation is a separate judgement. |
| data requirements | Time-indexed data, missingness, exposure, regressors, training/evaluation split, horizon, assumptions and comparison baseline. |
| provider coupling | Python numerical dependencies, model API and selected method assumptions; portability requires recording versions and analysis settings. |
| composability | Return fit diagnostics, uncertainty, limitations and out-of-sample comparison where appropriate into Stage 8 learning and Stage 7 scenarios. |
| quality suitability | Useful when a justified quantitative model is needed. A good historical fit does not establish causal effects, stationary demand or safe future growth. |
| maintenance | Current documentation describes deprecation practices and warns of untested edge cases. No blanket bug-free or API-stability guarantee is adopted. |
| privacy / legal constraints | Use permitted data and protect sensitive histories; a forecast must not be misrepresented as an investment recommendation or customer guarantee. |
| USE / ADAPT / REFERENCE / REJECT | USE — optional established statistical implementation under a qualified analysis plan, not a required forecast for every business. |
| gaps | Test adequacy, model assumptions, practical relevance and the authorised business response are not decided by calling a library method. |

<a id="tc24"></a>

### TC24 — Cloudflare Workers static assets; existing Pages comparison

**Category references:** LC14. See the exact original names in the coverage matrix.

| Field | Assessment |
|---|---|
| name | Cloudflare Workers static assets; existing Pages comparison |
| source | [Pages getting started](https://developers.cloudflare.com/pages/get-started/), updated 21 August 2026; [Workers static assets](https://developers.cloudflare.com/workers/static-assets/), updated 3 July 2026. Setup direction and asset/deployment behaviour inspected; no site deployed. |
| licence | Hosted platform/service terms govern deployment. Any open-source CLI or framework has separate component terms; this assessment does not copy platform implementation. |
| maturity | Documented hosting platforms. Current Pages guidance recommends Workers for new projects; that is a provider direction, not proof all existing Pages sites should migrate. |
| installation / access model | Approved Cloudflare account/project and current supported deployment route; distinguish local build, preview and user-facing publication. |
| production responsibility | Host the approved landing-page asset through existing infrastructure. Product/creative engineering owns its implementation; Business Building supplies the truthful brief. |
| deterministic vs generative role | Deterministic build/hosting operations, with any generated page content kept separate from approved claims and actual customer evidence. |
| data requirements | Approved assets, build configuration, domain, environment, secrets, form/tracking constraints and intended publication scope. |
| provider coupling | Worker bindings/routing, build configuration and platform behaviour; static assets can be portable while dynamic integrations increase coupling. |
| composability | Use a verified deployment identity and actual served-page checks as returned evidence. Hosting success is not evidence of demand or conversion. |
| quality suitability | Current new-project candidate, with existing Pages retained where it already meets the task. Avoid an unnecessary migration merely because guidance changed. |
| maintenance | Dated official setup direction and static-asset guidance inspected; validate chosen runtime/CLI before implementation and do not assume historical commands remain best. |
| privacy / legal constraints | Publication authority, claims, tracking and form-data handling remain Stage 9 constraints. A preview URL may still expose confidential content. |
| USE / ADAPT / REFERENCE / REJECT | USE — existing suitable hosting; prefer evaluating Workers for a new Cloudflare project, not automatically creating or migrating one. |
| gaps | Value, copy substantiation, experiment validity and commercial success remain outside deployment infrastructure. |

<a id="tc25"></a>

### TC25 — Vercel deployments

**Category references:** LC14. See the exact original names in the coverage matrix.

| Field | Assessment |
|---|---|
| name | Vercel deployments |
| source | [Deployment documentation](https://vercel.com/docs/deployments). Git/CLI/API methods, preview/production and verification guidance read; no account access, build or publication executed. |
| licence | Commercial hosted platform under its service/plan terms; framework or CLI licences are distinct. No redistribution of provider implementation is proposed. |
| maturity | Documented deployment platform with environment separation. No latency, cost, availability or conversion benchmark was performed. |
| installation / access model | Approved account/project with Git, CLI or REST access as appropriate. Verify the exact environment before any operation that publishes a live site. |
| production responsibility | Build and host approved landing-page implementations and return deployment identity and served behaviour. |
| deterministic vs generative role | Deterministic build/deploy state; AI-generated code or copy is not automatically reviewed, safe or commercially validated. |
| data requirements | Approved code/assets, build settings, domain, environment, secrets and publication permission; verify forms, claims and measurement configuration. |
| provider coupling | Platform deployment, environment and optional runtime features; use ordinary portable assets where sufficient rather than require proprietary coupling. |
| composability | Research/creative/software owners prepare the page; operator publishes only as approved and returns actual URL/version/error evidence. |
| quality suitability | Appropriate alternative where it matches the current stack. An example command containing --prod must not be run merely to inspect a draft. |
| maintenance | Current deployment guide inspected, including verification and environment distinctions; no latest CLI or end-to-end install compatibility test claimed. |
| privacy / legal constraints | Public/preview exposure, repository integration and secrets require control. Deployment credentials do not confer approval for customer-facing claims. |
| USE / ADAPT / REFERENCE / REJECT | USE — an optional existing hosting operator; compare with the incumbent or Cloudflare rather than impose two hosting systems. |
| gaps | Offer validity, audience fit and causal conversion evaluation are not solved by a successful build or generated preview URL. |

<a id="tc26"></a>

### TC26 — Python standard-library Decimal for bounded calculations

**Category references:** LC05, LC06, LC18. See the exact original names in the coverage matrix.

| Field | Assessment |
|---|---|
| name | Python standard-library Decimal for bounded calculations |
| source | [Decimal documentation](https://docs.python.org/3/library/decimal.html). Number construction, finite values, context, rounding and traps inspected; only stable basic operations are proposed, not newer-version-only APIs. [Python licence](https://docs.python.org/3/license.html) main PSF terms and incorporated-software distinction inspected; no exhaustive bundled-component audit. |
| licence | Python distribution uses its published PSF and component licensing; use the installed interpreter rather than copy implementation source. No vendor account or hosted-service agreement is required for local arithmetic. |
| maturity | Standard-library numerical facility. Arithmetic determinism is narrower than a validated business model or a complete spreadsheet engine. |
| installation / access model | Existing compatible Python interpreter; declare the actual runtime and decimal context when executing a bounded calculation. No additional SaaS account is necessary. |
| production responsibility | Compute inspectable expressions and small scenario reconciliations from explicit inputs, not ledger state, tax policy or a universal financial DSL. |
| deterministic vs generative role | Deterministic decimal arithmetic with explicit precision/rounding and exceptional-value handling; no generative numerical answer is accepted without execution. |
| data requirements | Source-located numeric strings, units, signs, periods, denominator rules and assumptions; values copied from binary floats can retain approximation. |
| provider coupling | Low provider coupling but runtime/context/rounding still matter. Do not call every decimal operation exact irrespective of precision or division. |
| composability | Can supply Stage 7 calculation evidence to an ordinary document or file writer; link input/output and actual execution rather than build a new engine. |
| quality suitability | Small adequate baseline for simple arithmetic. It does not evaluate arbitrary workbook formulas or decide whether costs and demand assumptions are valid. |
| maintenance | Current official docs inspected; the executed environment version is recorded in any actual check. Avoid asserting the docs version equals the installed runtime. |
| privacy / legal constraints | Keep calculation inputs in their authorised location; local execution does not justify disclosure of private financial records. |
| USE / ADAPT / REFERENCE / REJECT | USE — small deterministic calculation option, not a mandatory framework or substitute for an established accounting/spreadsheet system. |
| gaps | Accounting treatment, complete costs, statistical forecasting and commitments need their own evidence; a correct decimal result cannot supply them. |

