# Business Building Skills — Bootstrap Execution Contract

**Repository:** `sb-dev/business-building-skills`  
**Working branch:** `feat/bootstrap-4`  
**Governing bootstrap:** `docs/research-logs/2026-09-08-business-building-skills-new-project-bootstrap-process.md`  
**Operator command:** `/bootstrap`

This contract defines execution mechanics only. The bootstrap specification remains authoritative for substantive requirements, business-building evidence rules, and exit criteria.

## Branch basis and accepted state

`feat/bootstrap-4` is based directly on `main` at `4e70762beabb76ed93600a383b3871772a1b73db`.

Do not inherit accepted stage completion from `feat/bootstrap`, `feat/bootstrap-2`, `feat/bootstrap-3`, or any other feature branch. Reconstruct progress only from repository state and committed outputs on `feat/bootstrap-4`.

## Local supplied books

User-supplied book PDFs belong under:

```text
books/**/*.pdf
```

`/bootstrap` inventories them automatically. The user does not need to pass book paths in the command or repeat them between runs.

Treat discovered PDFs as user-supplied sources under the governing bootstrap's corpus rules. Record bibliographic metadata, access state, selection decisions and reading coverage in research logs, but keep the PDFs themselves local and uncommitted.

Do not:

- commit, rename, move, delete or modify supplied PDFs;
- publish absolute machine paths;
- upload supplied PDFs to Firecrawl or another external service without explicit user approval;
- silently exclude, replace or demote supplied books when the bootstrap requires permission;
- silently reopen an accepted corpus merely because a new PDF later appears under `books/`.

If a direct-extraction stage requires a selected book that is not locally accessible, stop with the exact missing source requirement rather than substituting summaries or model memory.

## Default authorisation

Invoking `/bootstrap` authorises execution from the next incomplete stage through the final bootstrap stage unless the user explicitly narrows the scope.

The user does not need to restate the current stage, book paths, execution instructions, or a stage range on each run.

## Stage execution

For every remaining stage:

```text
read complete stage
→ read accepted dependencies
→ extract requirements and exit criteria
→ perform substantive work
→ persist required outputs
→ verify actual outputs
→ repair failures
→ commit only that stage
→ push commit
→ verify remote commit
→ continue automatically
```

`/bootstrap` uses these internal support skills as applicable:

```text
bootstrap-stage-execution
bootstrap-research
direct-source-extraction
```

Domain-specific business-building evidence rules come directly from the governing bootstrap specification and accepted prior-stage outputs.

## Evidence rules

Do not:

- substitute a summary for required substantive research;
- substitute a bibliography, publisher description, secondary summary, or model memory for required direct-source examination;
- describe expected execution when actual execution is required;
- invent customer evidence, market evidence, pricing evidence, conversion data, unit economics, experiment results, benchmarks, installations, searches or tool runs;
- weaken a bootstrap exit criterion because the work is difficult;
- batch independently defined stages into one commit.

Preserve the bootstrap's distinction between assumption, observed evidence, metric, interpretation and decision. Revenue claims, growth claims and commercial tactics must remain grounded in real evidence and the legal/ethical boundaries defined by the bootstrap.

## Repair before escalation

A failed search, dead URL, failed command, test failure, extraction problem, implementation defect, or verification failure is not by itself a blocker. Use the smallest responsible repair or an allowed alternative path and continue.

## Stop only for genuine user decisions

Stop when progress actually depends on the user, including:

- explicit permission or approval required by the bootstrap;
- supplied-source exclusion, substitution, removal or demotion requiring approval;
- materially different valid interpretations that change project scope or accepted behaviour;
- unavailable mandatory evidence or capability that cannot be repaired or substituted within the bootstrap rules;
- a contradiction that would require reopening accepted prior work without authority;
- unrelated local changes would have to be discarded or overwritten.

## Verification

Before completing each stage, re-read the original requirements, inspect actual outputs, run required checks, repair mandatory failures, and persist enough evidence to justify completion.

## Commit and remote rule

Use one commit per completed stage and include the stage identifier in the commit message. Push every completed stage commit to `origin/feat/bootstrap-4`, verify the remote branch points to that commit, then continue automatically.

## Context rule

Reconstruct every stage from:

```text
governing bootstrap specification
+
accepted prior-stage outputs on feat/bootstrap-4
+
this execution contract
+
local supplied-source inventory under books/
```

## Final audit

After the final stage, audit the resulting repository against the bootstrap's global acceptance requirements. Do not claim maturity, publication readiness, benchmark success, installation success, or completion without the required evidence.
