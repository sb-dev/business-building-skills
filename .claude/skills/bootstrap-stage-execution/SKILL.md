---
name: bootstrap-stage-execution
description: Internal execution discipline for staged Production Skills bootstraps. Used by /bootstrap to execute one stage completely, verify it, repair failures, commit it, and continue safely.
allowed-tools:
  - Read
  - Grep
  - Glob
  - Skill
  - Bash
---

# Bootstrap Stage Execution

This skill standardises execution mechanics. It does not define domain work. The governing bootstrap specification remains authoritative.

## Stage loop

For the current stage:

1. Read the complete stage in the governing bootstrap specification.
2. Read accepted prior-stage outputs that the stage depends on.
3. Derive a compact checklist covering required inputs, substantive work, outputs, exact counts/distributions, required execution/tests/evaluation, and exit criteria.
4. Perform the complete substantive work.
5. Persist the stage's durable outputs.
6. Re-read the stage requirements and verify the actual outputs against them.
7. Diagnose and repair every mandatory failure, then re-run affected verification.
8. Commit only the completed stage.
9. Push and verify the remote branch points to the intended commit and files.
10. Return control to `/bootstrap`, which determines and starts the next incomplete stage.

## Evidence rule

Never substitute:

```text
plan for execution
summary for required research
bibliography for direct-source examination
script for required script execution
prompt for required generated output
file existence for substantive validation
single favourable run for a required benchmark/comparison
model memory for required source evidence
```

Never invent research findings, customer evidence, market observations, experiment results, metrics, benchmark results, installation results, tool executions, or repository state. Synthetic fixtures must remain explicitly synthetic.

## Verification and repair

Verification must check substance, not filenames alone.

If a mandatory requirement fails:

```text
diagnose
→ repair the owning scope
→ re-run affected verification
→ continue
```

Do not weaken acceptance criteria, skip required work, or rewrite validators to make incomplete work pass.

An exhaustive conformance table is optional unless the bootstrap, execution contract, or stage risk requires one.

## Blockers

Stop only when progress genuinely depends on a user decision, including required approval, supplied-source substitution, material scope ambiguity, unavailable mandatory evidence/capability with no allowed alternative, or reopening accepted work without authority.

Failed tests, poor searches, dead URLs, tool failures, implementation defects, extraction problems, and verification failures are execution problems to repair, not user-decision blockers.

## Commit discipline

Use one commit per completed stage and include the stage identifier, for example:

```text
stage 3: research professional business practice
stage 14 P3: extract specialised corpus
stage 23 P6: implement extension pack
```

Do not batch independent stages into one commit.

## Context

Reconstruct stage context from:

```text
governing bootstrap specification
+
accepted prior-stage repository outputs
+
current bootstrap execution contract under docs/research-logs/
```

Do not depend on conversation memory for accepted state.
