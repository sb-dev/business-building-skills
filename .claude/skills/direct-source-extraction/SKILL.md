---
name: direct-source-extraction
description: Internal direct-source examination and reconciliation procedure used when a bootstrap stage requires meaningful reading of supplied books, papers, standards, documents, or other source material. It automatically uses local PDFs under books/ when they are part of the required corpus.
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
---

# Direct Source Extraction

Use this skill when the governing bootstrap requires direct examination rather than source discovery alone.

## Local book source convention

Use `books/**/*.pdf` as the default location for user-supplied book PDFs.

Before extraction:

1. inventory all PDFs under `books/` recursively;
2. match the selected corpus to local files using document metadata and accepted source records, not filename similarity alone;
3. record only repository-relative identifiers such as `books/book.pdf` in durable logs;
4. never commit, rename, move, delete or modify supplied PDFs;
5. never upload a supplied PDF to Firecrawl or another external service without explicit user approval;
6. prefer Claude/local PDF reading or local text extraction before any external parsing service.

If a required selected source cannot be matched to an accessible local file and the bootstrap requires direct reading, record the exact missing source as a blocker rather than substituting summaries or model memory.

New PDFs discovered after a corpus-selection stage has already been accepted do not silently change the accepted corpus. Treat them as supplementary inputs unless the governing process requires reconsideration or the user explicitly asks to reopen selection.

## Access before extraction

For each required source record:

```text
title / identifier
author
edition / version / publication year where relevant
provided or selected origin
repository-relative local source identifier
access state
intended contribution
material actually examined
reading limitations
```

Useful access states include:

```text
full text available
relevant excerpts available
secondary material only
unavailable
```

Access is not reading. A file, table of contents, abstract, review, summary, or publisher description does not count as direct examination.

## Examination record

For each material finding capture:

| Field | Required content |
| --- | --- |
| Source location | Source, edition/version, chapter/section/page or stable location actually examined |
| Problem / concept | Independently expressed principle, method, claim, model, or heuristic |
| Applicability | Context, assumptions, prerequisites, scope, and limitations |
| Production effect | Decision, workflow, artefact, behaviour, or responsibility affected |
| Evaluation | Evidence, metrics, checks, or acceptance implications |
| Failure / misuse | Failure conditions, misuse risks, and repair implications |
| Relationships | Support, overlap, tension, contradiction, or dependency with other sources |
| Disposition | Retain, merge, adapt, qualify, reject, or research further |

Use the project's domain terminology rather than forcing a universal domain model.

## Reconcile the corpus

Analyse across sources:

```text
reinforcing findings
overlapping methods
competing assumptions
context-dependent alternatives
contradictions
important topics absent from the corpus
claims requiring broader professional / empirical / current-practice challenge
```

Repeated claims do not automatically constitute independent corroboration. Do not force every selected source to contribute a core rule.

## Publication boundary

Persist independently expressed synthesis and concise traceability, not substantial copied text, reconstructed chapters, proprietary examples, supplied books, private absolute paths, or private source material.

## Completion

A direct-source stage is complete only when required sources have been meaningfully examined for their intended contributions, reading coverage is honest, material findings are traceable, limitations/conflicts are explicit, and unresolved claims are handed to later challenge research.
