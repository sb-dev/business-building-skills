# Stage 10 — Existing Agent Skills, Tools and Business Systems

**Version:** 1.0  
**Date:** 9 September 2026  
**Status:** Landscape research complete for architecture selection  
**Branch:** `feat/bootstrap`

## 1. Decision

Native Business Building Skills should own **business judgement, evidence contracts, experiment design, cross-system diagnosis and bounded change**. Existing systems already provide CRM state, billing, analytics, forms, campaign execution, experiments, scheduling, messaging and accounting surfaces. Rebuilding those systems would increase scope without improving the missing business judgement.

The landscape is intentionally representative, not an exhaustive vendor directory. Product plans, APIs and licences can change; reverify them before implementation or commercial redistribution.

## 2. Reuse matrix

| Candidate | Role / access / licence signal | Decision | Boundary and gap |
|---|---|---|---|
| `astDeniss/business-skills` | Public Agent Skills repository; 69 operational playbooks spanning sales, marketing, SEO, ads, analytics, success and operations; install/read SKILL.md model | **REFERENCE** | Useful decomposition comparison, but broader function playbooks are not the evidence/decision architecture this project needs; do not copy text or assume licence from a search result |
| HubSpot CRM | Hosted CRM for contacts, deals, tasks, email/meeting and related customer activity | **USE/REFERENCE** | Good execution/state surface; provider-coupled, personal data and plan limits; does not own our qualification/evidence semantics |
| Twenty | Open-source extensible CRM; contacts/deals/tasks/notes | **USE/REFERENCE** | Potential self-hosted CRM option; verify current licence/deployment/security before adopting; no need to fork it |
| Pipedrive | Hosted deal/pipeline CRM with leads/deals and sales reporting | **USE/REFERENCE** | Concrete sales-state executor; vendor definitions remain external |
| Stripe Billing | Hosted subscriptions, invoices, usage billing, quotes, portal and analytics | **USE** when consumer project already uses Stripe | Billing state and payment execution; Stripe metric definitions are configurable/vendor-specific and not business truth |
| PostHog | Product/web analytics, feature flags, experiments, surveys and data tooling; public source repository | **USE/REFERENCE** | Strong digital-product execution; verify current deployment/licence/data terms; not appropriate for every service business |
| Google Analytics | Event/key-event analytics | **USE/REFERENCE** | Existing web measurement; definitions and privacy setup are project responsibilities |
| Plausible | Open-source/privacy-oriented web analytics with cloud/self-host options | **USE/REFERENCE** | Simpler aggregate web analytics; verify current licence/data requirements before self-hosting/integration |
| Metabase | Open-source BI/query/visualisation layer; cloud/self-host; current repository mixes AGPL open-source and commercial editions | **USE/REFERENCE** | Useful over existing databases; licence boundaries matter; not a data warehouse or business-decision engine |
| Google Ads Experiments | Hosted control/treatment campaign experimentation | **USE** for applicable Google Ads tests | Owns campaign assignment/execution; does not establish cross-channel or whole-business causality |
| Typeform | Hosted forms/surveys with Create/Responses/Webhooks APIs and MCP surface | **USE/REFERENCE** | Collection infrastructure; provider/data-plan coupling; survey response is not market validation by itself |
| Formbricks | Open-source forms/surveys with self-hosting option | **USE/REFERENCE** | Alternative collection surface; verify current licence/security/hosting before implementation |
| Google Forms | Hosted forms with spreadsheet response integration | **USE** for simple authorised collection | Low setup; not a research-method engine; consumer data/Workspace controls remain project concerns |
| Cal.com | Scheduling platform with open-source/open-core repository and APIs | **USE/REFERENCE** | Scheduling executor, not sales qualification; licence split requires care for redistribution/self-hosting |
| Mailchimp / Brevo | Hosted email/SMS marketing automation | **USE** only after permission/marketing review | Delivery and automation, not authority to contact; provider terms and personal-data handling apply |
| QuickBooks / Xero ecosystem | Hosted accounting/invoicing and forecasting ecosystem | **USE** for authoritative bookkeeping/accounting inputs where the project uses them | Do not rebuild accounting; calculations imported into business analysis need source/date/basis |
| Spreadsheets / CSV | Deterministic arithmetic and portable tabular interchange | **USE** | Preferred baseline for unit economics/cash fixtures; formulas and units must be explicit |
| Existing search/research tools | External market/company/current-fact retrieval | **USE** | Business Building defines the question/evidence need; Deep Research or web tooling performs deeper retrieval |
| Legal Skills / qualified counsel | Legal research and professional handoff | **USE/COMPOSE** | Optional family dependency; professional authority remains outside this repository |

## 3. Production-role decisions

### Native responsibilities

```text
frame business decision
separate fact / assumption / synthetic fixture
model customer, value, offer and economic dependencies
define channel/sales hypotheses
select evidence appropriate to the question
specify experiment and decision rule
interpret metrics with their definitions and limitations
diagnose likely binding constraint
preserve supported decisions
recommend smallest sufficient correction
prepare professional handoffs
```

### Existing systems should execute

```text
CRM record mutation and pipeline state
email/SMS delivery
paid-ad buying and platform experiments
web/product event collection
subscription billing and payments
survey/form collection
scheduling
accounting/bookkeeping
BI querying/visualisation
spreadsheet arithmetic
```

An integration can be useful later, but a command must still work by producing a clear human/tool handoff when the provider is absent. No core workflow should require one vendor account.

## 4. Data, privacy and provider coupling

Provider systems may contain personal, confidential or regulated information. A skill should request only fields necessary for the decision and avoid copying raw CRM/customer datasets into repository examples or logs. Project-specific retention, access and jurisdiction rules travel with the data.

Metric names are not portable facts. Stripe MRR, CRM deal stages, Google Analytics key events and ad-platform conversions each depend on configured semantics. Import the definition, period and source with the number.

External execution credentials do not confer permission. Stage 9's authority and legal handoff rules remain in force even when an API can technically perform the action.

## 5. Native gap conclusion

Existing tools are strong at **state and execution** and some repositories provide operational playbooks. The evidenced gap is a small installable layer that connects business evidence to coherent decisions across offer, acquisition, delivery, economics, experiments and repair while remaining provider-independent.

That gap justifies native Agent Skills. It does not justify a new CRM, analytics store, ad platform, billing engine, accounting package, form service or generic integration bus.

## 6. Sources checked

Accessed 9 September 2026. Product marketing claims were used only to identify available surfaces, not to establish business effectiveness.

- GitHub, [`astDeniss/business-skills`](https://github.com/astDeniss/business-skills), public repository README.
- HubSpot, [Free CRM](https://www.hubspot.com/products/crm), current feature description.
- Twenty, [What is Twenty](https://docs.twenty.com/user-guide/getting-started/capabilities/what-is-twenty), current docs.
- Pipedrive, [Deals](https://support.pipedrive.com/en/article/deals-what-they-are-and-how-to-add-them), current docs.
- Stripe, [Billing](https://docs.stripe.com/billing) and [Analytics](https://docs.stripe.com/billing/subscriptions/analytics), current docs.
- PostHog, [`PostHog/posthog`](https://github.com/PostHog/posthog), public repository README.
- Google, [Analytics events](https://developers.google.com/analytics/devguides/collection/ga4/events) and [Ads experiments](https://developers.google.com/google-ads/api/docs/experiments/overview), current docs.
- Plausible, [`plausible/analytics`](https://github.com/plausible/analytics), public repository README.
- Metabase, [documentation](https://www.metabase.com/docs/latest/) and [`metabase/metabase`](https://github.com/metabase/metabase), including current licence notice.
- Typeform, [Developer Platform](https://www.typeform.com/developers/), current API/MCP description.
- Formbricks, [Open Source Form Builder](https://formbricks.com/open-source-form-builder), current product description.
- Google, [Forms help](https://support.google.com/docs/answer/6281888), current docs.
- Cal.com, [documentation](https://cal.com/docs/availability) and public repository licence description checked via GitHub search.
- Mailchimp, [Automation](https://mailchimp.com/help/automation/); Brevo, [platform overview](https://help.brevo.com/hc/en-us/articles/33456241984914-Overview-of-the-Brevo-platform).
- QuickBooks UK, [Invoicing](https://quickbooks.intuit.com/uk/invoicing/); Xero UK app ecosystem cash-flow collection checked for execution landscape.

## 7. Exit

Native skills are justified by missing provider-independent business judgement, not by a desire to reproduce existing SaaS tools. Stage 11 can now choose a thin execution boundary that keeps providers replaceable.

*Stage 10 · Version 1.0 · 9 September 2026.*
