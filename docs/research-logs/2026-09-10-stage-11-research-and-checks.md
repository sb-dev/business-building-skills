# Stage 11: Research and tool-substitution checks

**Date:** 10 September 2026  
**Branch:** `feat/bootstrap-2`  
**Authority:** [Original §18](2026-09-08-business-building-skills-new-project-bootstrap-process.md).  
**Companions:** [Execution-layer decision](2026-09-10-stage-11-execution-layer.md), [conformance and executable checks](2026-09-10-stage-11-conformance.md).

## 1. Inputs and research boundary

The verified starting point is Stage 10 receipt `92fdd644decb6e469e5cf2ac3874d01919bd9330`, root `1517229364f39556de3c7a53b2c5d9b3d80ebd4e`. Its parent is the existing Stage 10 content commit `348e1471926881b5da13002c1d8a0fdc8a30a1f9`. The original bootstrap on main was reread fully; its identity remains `a0ac1b6c78a0cde8ccd9aca6fda6c5b0880c516d`. The uploaded execution contract was available in full. No failed-branch artefacts or unverified Stage 9 drafts were used.

Stage 10's four reports were inspected during receipt verification, including all candidate records, the ownership and reuse decisions, and persisted execution evidence. Those source reads and 57-check executions are historical accepted inputs, not new Stage 11 executions. Fresh accepted-input reads at the starting head covered Stage 1 professional/execution boundaries, Stage 7 HC01–HC08 and GG01–GG07, and Stage 9's complete shared handoff/constraint packet. The model retains the referenced Stage 4 dossier and Stage 8 experiment/learning contracts rather than replacing their terminology.

The choice is project design under these accepted contracts. Targeted primary-source research below checks operational distinctions that matter to portability. It is not a new exhaustive vendor landscape, price comparison, legal audit, account test or evaluation of an entire SDK. All five selected sources were accessed on 10 September 2026. Only the stated passages were used; no linked PDF, source code, credential, customer data or restricted third-party skill was republished.

## 2. Additional primary-source register

### R01 — Stripe API v1 idempotent requests

Source: https://docs.stripe.com/api/idempotent_requests

Read the live page's key handling, saved responses, parameter checks and execution-start qualifications. Its stored-result behaviour can repeat a failure response, and key retention limits matter. This supports keeping retries with the actual operation rather than adopting a universal success-or-retry rule. No payment API request was executed. Documentation examples are not local credentials or approved actions.

### R02 — Stripe API v2 overview

Source: https://docs.stripe.com/api-v2-overview

Read the namespace comparison and idempotency section. It describes re-execution of failed work under specified replay conditions and an account/API/time scope different from v1. The project therefore requires version-specific retry evidence; the same provider name is not enough. This is a comparison of documented contracts, not an observed replay benchmark or approval to migrate an integration.

### R03 — Google Sheets CellData

Source: https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/cells

Read CellData's entered, effective and formatted value definitions. A formula input and its calculated result are separate fields; formatted display is another representation. The design requires a calculated-result receipt tied to the relevant inputs. No spreadsheet was created, uploaded or recalculated, and the synthetic receipt checks below are not a Google Sheets integration test.

### R04 — MCP Tools specification, version 2025-11-25

Source: https://modelcontextprotocol.io/specification/2025-11-25/server/tools

Read user-interaction, tool annotations, structured results, error handling and security sections. Tool execution errors can appear within a result; annotations have a trust boundary; server-produced structured data is not a model's generated structured output. These distinctions motivate result inspection and explicit action scope. This is a named version, not a claim it is the latest protocol, and MCP is not selected as a mandatory runtime.

### R05 — Python Decimal documentation

Source: https://docs.python.org/3/library/decimal.html

Read construction, finite-value checks and arithmetic contexts, including precision, rounding and localcontext. Decimal construction from a float can preserve its binary approximation; arithmetic remains subject to context. Use explicit numeric strings and a declared context for the bounded fixture. The fetched documentation identifies Python 3.14.7; the actual local interpreter is recorded separately. No newer-version-only API or general exactness guarantee is assumed.

The source register supports specific operational distinctions. The entire architecture, eight annotations and test conventions are independently authored project decisions. Vendor documentation does not prove local capability, evidence validity, legal permission or commercial effectiveness.

## 3. Substitution design and fixed expectations

All exports, monetary events, approvals and responses below are **original synthetic fixtures**, not real vendor schemas or customer observations. The checker performs local transformations and comparisons only. Its miniature functions are disposable design checks, not a proposed connector SDK, ledger, access-control system, retry engine or universal business evaluator.

| Case | Fixed facts and expected disposition |
|---|---|
| S01 | Export A has two major-unit rows: gross 120 and 80, discount 10 and 0, refund 0 and 20, direct cost 90 and 60. Export B encodes the same events in integer minor units and different field names. Separate Decimal and integer calculation paths must agree: N=170, K=150, C=20 GBP. Accepted customer/offer/price/experiment versions remain unchanged; other growth gates are still unassessed. |
| S02 | Change currency, unit, period, time zone, cohort, metric or cost basis in B. The fixture must request a semantic bridge rather than falsely assert equivalent evidence. A difference is not automatically evidence of business failure. |
| S03 | Duplicate event identity, absent amount, malformed/non-finite input, excessive precision for this particular minor-unit fixture, or Boolean-as-money must not be silently accepted. This fixture's two-decimal convention is not a universal currency rule. |
| S04 | A stipulated valid approval covers only reading report-1 in sandbox at offer version o-v1 for analysis. Sending, broader target, live environment, changed version/purpose, absent or expired approval must fail the exact-scope comparison. These are not real permissions. |
| S05 | Tool-returned prose asks for broader sending. It is data, not authority: the read grant cannot become a send grant. This checks explicit-field separation, not general prompt-injection resistance of an installed model. |
| S06 | Timeout remains unknown effect; protocol and tool-result errors remain errors requiring reconciliation; accepted means pending; confirmed remains provider confirmation, not proof of a business outcome. Missing result meaning yields unverified, not success. |
| S07 | An automatic retry requires stipulated evidence of same operation/scope/payload, documented window, current authority and documented safe replay. Remove any one: no automatic retry. Source-specific policy supplies those facts; the fixture does not infer them or call a provider. |
| S08 | A calculated value must match its input version, have no returned errors and a verified method. A stale cache, formula-only file, returned error or unknown method cannot support a fresh-calculation claim. No real workbook is evaluated. |
| S09 | The common workflow remains frame→inspect→assumptions→request→validate→interpret→decide→learn for both export formats. Equivalent results preserve the accepted baseline. This is an executable local contract demonstration, not a live migration or installed-agent benchmark. |

The no-change comparison is deliberate: a valid data-format substitution needs a different field mapping, not a new offer or growth strategy. An incompatible source needs a bridge or additional evidence, not forced numerical agreement. A new tool may be adequate for reading but unsuitable or unauthorised for an effectful action. These are separate decisions.

## 4. Semantic review

The assistant reviewed every BD and EX ownership row against §18 and retained all eleven items in each original list. Arithmetic remains external even when the agent authors a formula. The host may reason about economics without posting a ledger; it may design an experiment without allocating live users; it may draft outreach without sending it. Existing tools' analytical abilities remain reusable, not denied to justify native code.

The workflow does not require a particular SaaS account or adapter framework. Existing-source exports are acceptable only when adequate for the decision. Missing information is not converted into zero; rights, current specialist constraints and action authority still block the affected operation. Portability permits a changed result when actual facts or meanings differ, while protecting unaffected accepted choices.

S01–S09 are reviewed against those distinctions. The monetary example yields positive direct contribution but leaves acquisition, capacity, cash and other relevant growth gates unknown. Therefore it cannot authorise scale. Error and approval fixtures verify the declared control-flow boundary, not classification of every possible provider response. Real integration and installed-agent acceptance remain later-stage obligations.

## 5. Execution results

Actual results and the exact reproducible checker are retained in the conformance companion. Overall stage completion additionally requires the scoped commit and verified remote receipt. No unperformed operation is counted as a test pass.
