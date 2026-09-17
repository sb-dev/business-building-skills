---
name: bootstrap
description: Public entry point for resuming and executing the repository bootstrap. Invoke as /bootstrap. It reconstructs progress from repository state, discovers supplied local book PDFs, starts at the next incomplete stage, and continues stage by stage until the bootstrap is complete or a genuine user decision is required.
allowed-tools:
  - Read
  - Grep
  - Glob
  - Skill
  - Bash
---

# Bootstrap

Use:

```text
/bootstrap
```

No stage number, stage range, book-path arguments, or repeated execution prompt is required.

## Local supplied books

At the start of every run, inspect `books/**/*.pdf` when that directory exists.

Treat every discovered PDF as user-supplied source material for the bootstrap. Do not require the user to restate filenames or paths in the command.

Rules:

- `books/` is local-only and gitignored;
- never commit, move, rename, delete, or rewrite supplied PDFs;
- record repository-relative identifiers such as `books/example.pdf`, never absolute machine paths;
- derive title, author, edition and publication metadata from the document when possible rather than trusting the filename alone;
- do not upload supplied PDFs to Firecrawl or another external service without explicit user approval;
- if a corpus-selection stage is not yet complete, include all discovered PDFs in the supplied-source decision process required by the governing bootstrap;
- if the bootstrap requires an exact corpus size and supplied books must be excluded, replaced or demoted, follow its explicit permission rules before doing so;
- if corpus selection is already accepted, newly discovered PDFs are supplementary inputs and must not silently reopen the accepted corpus unless the governing process requires it or the user asks;
- when a direct-extraction stage requires a selected book, use the local PDF under `books/`; if required direct access is missing, report the exact missing source as a genuine source-access blocker.

The durable research logs store source metadata, selection decisions, reading coverage and findings. The PDFs themselves remain local working material.

## Default behaviour

Invocation of `/bootstrap` authorises execution of the remaining bootstrap from the next incomplete stage through the final stage, unless the user explicitly narrows the scope.

1. Find the current bootstrap execution contract under `docs/research-logs/`.
2. Read the governing bootstrap specification named by that contract.
3. Verify the current repository and working branch. Preserve existing local changes; never discard or overwrite unrelated work to switch branches.
4. Inventory local supplied PDFs under `books/` using the rules above.
5. Reconstruct accepted progress from repository state, committed research logs, and stage outputs. Do not use conversation memory as accepted state.
6. Determine the next incomplete stage from the governing bootstrap.
7. Invoke `bootstrap-stage-execution` for that stage.
8. Let stage execution use `bootstrap-research` and `direct-source-extraction` when required.
9. After the stage passes verification, commit it separately, push it to the working branch, and verify the remote commit.
10. Continue immediately with the next incomplete stage.
11. After the final stage, run the bootstrap's final/global acceptance audit.

## Stop condition

Stop only when progress genuinely depends on a user decision, such as:

- explicit approval required by the bootstrap;
- supplied-source replacement, removal, exclusion or demotion requiring permission;
- materially different valid interpretations that change accepted scope or behaviour;
- mandatory evidence or capability that cannot be repaired or substituted under the governing rules;
- continuing would reopen accepted work without authority;
- local uncommitted work would have to be discarded or overwritten.

A failed search, dead URL, failed command, failed test, extraction problem, implementation defect, or verification failure is not a reason to stop. Diagnose it, repair it, retry, or use an allowed alternative path.

## Operator contract

`/bootstrap` is the public command. The following are internal support skills and should normally be selected by this workflow rather than invoked manually:

```text
bootstrap-stage-execution
bootstrap-research
direct-source-extraction
```

Do not ask the user to restate the current stage, remaining range, book PDF paths, or execution procedure when repository state already provides that information.
