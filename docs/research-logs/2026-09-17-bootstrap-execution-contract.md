# Business Building Skills — Bootstrap Execution Contract

**Repository:** `sb-dev/business-building-skills`  
**Working branch:** `feat/bootstrap-4`  
**Governing bootstrap:** `docs/research-logs/2026-09-08-business-building-skills-new-project-bootstrap-process.md`  
**Operator command:** `/bootstrap`

This contract defines execution mechanics only. The bootstrap specification remains authoritative for substantive requirements, business-building evidence rules, and exit criteria.

## Branch basis and accepted state

`feat/bootstrap-4` is based directly on `main` at `4e70762beabb76ed93600a383b3871772a1b73db`.

Do not inherit accepted stage completion from `feat/bootstrap`, `feat/bootstrap-2`, `feat/bootstrap-3`, or any other feature branch. Reconstruct progress only from repository state and committed outputs on `feat/bootstrap-4`.

At branch creation, `main` contains the governing bootstrap specification and research-log README but no substantive Stage 1+ execution logs. `/bootstrap` must verify the next incomplete stage from repository state rather than rely on this note alone.

## Default authorisation

Invoking `/bootstrap` authorises execution from the next incomplete stage through the final bootstrap stage.

The user does not need to restate the current stage, repeat execution instructions, or provide a stage range on each run. An explicit user instruction may narrow or stop that range.

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

`/bootstrap` is the public entry point. It uses these internal support skills as applicable:

```text
bootstrap-stage-execution
bootstrap-research
direct-source-extraction
```

Domain-specific business-building rules come directly from the governing bootstrap specification and accepted prior-stage outputs.

## Evidence rules

Do not:

- substitute a summary for required substantive research;
- substitute a bibliography, publisher description, secondary summary, or model memory for required direct-source examination;
- invent market size, customer demand, conversion, pricing, CAC, LTV, retention, unit economics, cash-flow, experiment, or business-performance evidence;
- describe expected execution when actual execution is required;
- claim tests, benchmarks, installations, comparisons, searches, experiments, or tool runs that did not occur;
- weaken a bootstrap exit criterion because the work is difficult;
- silently replace, remove, or demote a user-provided source where permission is required;
- batch independently defined stages into one commit.

Keep assumptions, observations, metrics, interpretations, and decisions distinct as required by the bootstrap.

## Repair before escalation

A failed search, dead URL, failed command, test failure, extraction problem, implementation defect, or verification failure is not by itself a blocker.

Use the smallest responsible repair or an allowed alternative path and continue.

## Stop only for genuine user decisions

Stop when progress actually depends on the user, including:

- explicit permission or approval required by the bootstrap;
- supplied-source substitution/removal/demotion requiring approval;
- materially different valid interpretations that change project scope or accepted behaviour;
- unavailable mandatory evidence or capability that cannot be repaired or substituted within the bootstrap rules;
- a contradiction that would require reopening accepted prior work without authority;
- unrelated local changes would have to be discarded or overwritten.

Do not stop merely because work is difficult, a first attempt failed, or verification found defects.

## Verification

Before completing each stage:

1. re-read the original stage requirements and exit criteria;
2. inspect the actual repository outputs;
3. run required tests, calculations, experiments, comparisons, or installation checks;
4. verify deterministic calculations with appropriate tools where the bootstrap requires them;
5. repair every mandatory failure;
6. persist enough verification evidence to justify completion.

An exhaustive conformance table is optional unless the stage, bootstrap, or risk level requires one.

## Commit and remote rule

Use one commit per completed stage and include the stage identifier in the commit message, for example:

```text
stage 3: research broader business practice
stage 14 P3: extract specialised corpus
stage 23 P6: implement extension pack
```

Push every completed stage commit to `origin/feat/bootstrap-4`, verify the remote branch points to that commit, then continue automatically.

## Context rule

Reconstruct every stage from:

```text
governing bootstrap specification
+
accepted prior-stage outputs on feat/bootstrap-4
+
this execution contract
```

Do not rely on conversation memory for accepted state.

## Final audit

After the final stage, audit the resulting repository against the bootstrap's global acceptance requirements. Do not claim maturity, publication readiness, benchmark success, installation success, or completion without the required evidence.
