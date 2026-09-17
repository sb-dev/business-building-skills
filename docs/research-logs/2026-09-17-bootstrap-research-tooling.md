# Bootstrap Research and Execution Tooling

**Status:** Family-candidate prototype  
**Date:** 17 September 2026  
**Branch:** `feat/bootstrap-4`

## Purpose

This branch adds a single `/bootstrap` operator command and three internal support skills for executing the Business Building bootstrap without repeating stage prompts or duplicating the domain methodology.

The governing Business Building bootstrap remains authoritative for domain scope, evidence rules, stage requirements, outputs, and exit criteria.

## Operator surface

Use only:

```text
/bootstrap
```

The command reconstructs accepted progress from `feat/bootstrap-4`, finds the next incomplete stage, executes and verifies it, commits and pushes it separately, and continues automatically until the bootstrap is complete or a genuine user decision is required.

## Internal support skills

```text
.claude/skills/bootstrap-stage-execution/SKILL.md
.claude/skills/bootstrap-research/SKILL.md
.claude/skills/direct-source-extraction/SKILL.md
```

These are implementation details used by `/bootstrap`, not normal operator commands.

`bootstrap-research` uses Claude Code `WebSearch` and `WebFetch` first and escalates to Firecrawl only when a concrete retrieval problem justifies search+scrape, scrape, map, crawl, interact, parse, or developer-index retrieval.

`direct-source-extraction` handles meaningful examination and reconciliation when the bootstrap requires direct reading of books or other supplied sources.

`bootstrap-stage-execution` owns the repeated stage loop: read, execute, persist, verify, repair, commit, push, verify remote, return to `/bootstrap`.

## Business-building evidence discipline

The reusable research mechanics defer to the governing bootstrap for domain rules. In particular, Business Building research must keep assumptions separate from observations and decisions, prefer professional/empirical evidence over business folklore, avoid invented customer or market evidence, expose economic assumptions, and preserve legal/ethical handoffs defined by the bootstrap.

## Firecrawl

Firecrawl is an escalation path, not the default provider. Do not run `firecrawl setup defaults` and do not add a separate generic deep-research workflow. Large Firecrawl outputs belong under `.firecrawl/` and should be inspected incrementally.

## Branch-state rule

`feat/bootstrap-4` is based directly on `main`. No stage-completion state is inherited from earlier feature branches. Repository state and committed outputs on this branch are authoritative.

## Target architecture

These four skills are co-located here for validation. The reusable mechanics remain candidates for later extraction to central Production Skills tooling; Business Building-specific production intelligence remains in this project's bootstrap and eventual product skills.
