---
name: bootstrap-research
description: Internal evidence-first research procedure used by /bootstrap when a stage requires external research, current verification, professional-practice challenge, capability-landscape research, or other source-based investigation.
allowed-tools:
  - WebSearch
  - WebFetch
  - Read
  - Grep
  - Glob
  - Skill
  - Bash(firecrawl *)
  - Bash(npx firecrawl-cli *)
---

# Bootstrap Research

This skill defines reusable research mechanics. The project bootstrap defines what must be proved and what evidence is appropriate for the domain.

## Research loop

1. Read the current stage and relevant governing principles in the bootstrap specification.
2. Convert material requirements and exit criteria into distinct evidence questions.
3. Search each important question from more than one angle when one query is unlikely to establish adequate coverage.
4. Prefer primary, authoritative, official, empirical, first-party, or professional sources appropriate to the claim and domain.
5. Inspect the source itself. Search snippets, model memory, summaries, and generated prose are discovery aids, not evidence.
6. Capture enough provenance to trace material findings to inspected sources.
7. Look for counterexamples, contrary evidence, missing responsibilities, temporal changes, scope limits, and implementation constraints.
8. Run targeted follow-up searches for material gaps rather than broad repetitive searches.
9. Keep unresolved or weakly supported claims explicit.
10. Persist detailed findings and stop only when the stage's evidence requirements and exit criteria are satisfied or remaining uncertainty is explicitly bounded.

## Native-first retrieval

Use Claude Code's native web tools first:

| Need | Default |
| --- | --- |
| Discover current sources | `WebSearch` |
| Read a straightforward web source | `WebFetch` |
| Inspect local supplied material | `Read`, `Grep`, `Glob` |
| Challenge coverage | another targeted `WebSearch` |

Escalate to Firecrawl only for a concrete retrieval problem:

| Problem | Escalation |
| --- | --- |
| Need several full search results together | `firecrawl search ... --scrape` |
| Native fetch cannot extract a known page | `firecrawl scrape` |
| Need to discover a site's structure | `firecrawl map` |
| Need a bounded multi-page corpus | `firecrawl crawl` |
| Dynamic interaction/forms/pagination required | `firecrawl interact` |
| Difficult local document needs clean extraction and external processing is allowed | `firecrawl parse` |
| Tooling research needs docs, READMEs, issues, or merged PRs | Firecrawl developer-index capability |

Do not run `firecrawl setup defaults`; native Claude web search remains the normal first path.

Store large Firecrawl results under `.firecrawl/` and inspect them incrementally.

## Evidence record

For each material finding capture, as applicable:

```text
research question
claim / proposition / practice
source type
source title
stable URL or identifier
publication / effective / update date
retrieved-at date
section / paragraph / page / stable location
scope / applicability
limitations / contrary evidence
evidential standing
project implication
```

Use domain-specific fields required by the governing bootstrap.

## Business-building evidence

Respect the bootstrap's separation of assumption, observation, metric, interpretation and decision. Do not turn plausible market, customer, conversion, pricing, CAC, LTV, retention, unit-economics, or growth claims into facts without evidence. Prefer durable professional practice and empirical evidence over business folklore, and verify change-sensitive platform, market, legal, or tooling claims against current sources.

## Direct-source stages

When a stage explicitly requires direct examination of supplied books, papers, standards, files, or other source material, invoke `direct-source-extraction`. Source access is not source examination.

## Cost and context discipline

Use the cheapest adequate operation:

```text
WebSearch before Firecrawl search
WebFetch before Firecrawl scrape
scrape before site-wide operations
map before broad crawl
local Read before external document parsing
```

Do not add providers merely for redundant coverage. Cross-provider verification is justified only when a material gap, contradiction, or discovery risk remains.
