Execute the bootstrap process below. Treat EACH STAGE AS A SEPARATE, COMPLETE TASK, exactly as though it were the only task I had asked you to perform.

Bootstrap specification: https://github.com/sb-dev/business-building-skills/blob/feat/bootstrap-3/docs/research-logs/2026-09-08-business-building-skills-new-project-bootstrap-process.md

Repository: `sb-dev/business-building-skills`

Working branch: `feat/bootstrap-3`

Starting point: commit `fbaed771716f30994eb30cf6678fad7d4d22e2c1` on `feat/bootstrap-3` — the verified Stage 15 completion receipt. Stages 1–15 are accepted as COMPLETE at this boundary. Stages 16–26 have not started.

Accepted progress record: `docs/research-logs/bootstrap-2-progress.md` at the starting commit above. Earlier Stage 1–15 research logs, conformance evidence, verifier outputs and completion receipts on this branch are authoritative prior-stage inputs.

Stages authorised: Stages 16–26, executed strictly sequentially. Stage 0 is the existing bootstrap workspace. Stages 1–15 must not be redone, rewritten or silently modified while completing Stages 16–26. If a later requirement exposes a genuine contradiction or defect in an accepted earlier stage that would require changing Stage 1–15 work, STOP THE PROCESS AND ASK ME before making that change.

Do not use `feat/bootstrap` or any rejected/failed bootstrap attempt as an implementation source, shortcut, template or authority. Do not replace accepted `feat/bootstrap-3` outputs with work from another branch.

## 1. Non-negotiable execution rule

Authorisation to complete multiple stages means repeating the full execution and verification process for each stage. It does NOT mean batching the stages, summarising their intent, reducing their depth or replacing required outputs with representative samples.

Your unit of work is ONE STAGE.

Treat the current stage exactly as if it were the ONLY task I had asked you to perform.

Do not consider the existence of later stages when deciding how much research, analysis, implementation or verification the current stage deserves.

Do not start the next stage until the current stage:

- has every mandatory requirement satisfied;
- has every required activity actually performed;
- has every required deliverable present and complete;
- satisfies every exact count, distribution, structure and content requirement;
- has passed its specified exit criteria;
- has its verification evidence recorded;
- has been committed to `feat/bootstrap-3`;
- has the remote commit verified.

A stage is not complete merely because:

- a research log exists;
- a file has the expected name;
- the intended implementation is described;
- some representative subset was produced;
- a validator exists but was not executed;
- later work could theoretically finish it;
- a commit was created.

Never substitute:

```text
representative
partial
illustrative
provisional implementation
future target
planned
designed
```

for a requirement that the stage says must actually exist or be completed.

If a stage requires 15 items, produce and verify 15 items.

If a stage requires six specifications, produce and verify six specifications.

If a stage requires execution, execute it.

If a stage requires a measured comparison, do not replace it with a description of the expected result.

## 2. Authority and questions

The governing bootstrap specification is the acceptance contract.

Do not rewrite, weaken, reinterpret, waive or silently defer one of its requirements merely because satisfying it makes the stage larger.

The accepted Stage 1–15 outputs on `feat/bootstrap-3` are the prior-stage authority for continuation. Do not regenerate them from conversation memory and do not copy alternative versions from other branches.

If ANY question requires my input, STOP THE ENTIRE PROCESS AND ASK ME.

This includes:

- ambiguous requirements;
- conflicting requirements;
- uncertainty about what the specification requires;
- uncertainty about the approved baseline;
- uncertainty about whether an earlier accepted decision may be changed;
- missing source material required to satisfy the stage;
- an unavailable tool required to satisfy or verify the stage;
- a failed prerequisite;
- an unresolved requirement from an earlier stage;
- a proposed deferral;
- a proposed substitution;
- a proposed scope reduction;
- a proposed exception;
- a decision that belongs to me;
- an external action requiring authority I have not explicitly provided.

Do not answer such questions on my behalf.

Do not make a “reasonable assumption” and continue when my decision is required.

Do not continue with a different stage while waiting for the answer.

The rule is:

```text
QUESTION REQUIRES USER INPUT
→ STOP
→ ASK
→ DO NOT CONTINUE UNTIL ANSWERED
```

Use only `feat/bootstrap-3` throughout this continuation unless I explicitly change the branch strategy.

## 3. Before starting EACH stage

At the beginning of every stage:

1. Re-read the ORIGINAL bootstrap specification from `feat/bootstrap-3` at `docs/research-logs/2026-09-08-business-building-skills-new-project-bootstrap-process.md`.
2. Read the complete section for the current stage.
3. Read any global principles, acceptance gates and cross-references that constrain that stage.
4. Read the accepted outputs of earlier stages from `feat/bootstrap-3`, beginning from the verified Stage 15 boundary at `fbaed771716f30994eb30cf6678fad7d4d22e2c1` and following the durable repository evidence rather than conversation memory.
5. Verify that all prerequisites actually exist and passed their previous exit criteria.

Then extract a stage-specific acceptance checklist.

The checklist must explicitly capture:

```text
stage purpose
required inputs
prerequisites
questions to resolve
required research
required activities
required comparisons
required candidate discovery
required analysis
required decisions
required deliverables
required contents of each deliverable
exact counts
exact distribution requirements
exact naming requirements
exact structural requirements
required prompts
required examples
required tests
required execution
required measurements
required verification
research-log output
exit criteria
things explicitly deferred to later stages
```

For every checklist item, cite or identify the corresponding requirement in the bootstrap specification.

Before doing substantive work, state:

```text
Stage: <number and title>

Completion requires:
- ...
- ...
- ...
```

Do not begin work belonging to a later stage.

## 4. Execute the current stage fully

Give this stage the same depth, care, research and verification you would give it if there were no other stages remaining.

Do not optimise for reaching Stage 26.

Do not shorten the work because many stages remain.

Do not convert exact requirements into weaker approximations.

Examples:

```text
“5 levels × 3 primary examples = 15”
means exactly 15 primary examples,
distributed exactly 3 per level.

It does NOT mean:
5 representative examples,
15 example ideas,
or one implemented example plus 14 future targets.
```

```text
“Generate six canonical specifications”
means six actual complete specification files.

It does NOT mean:
five files and one planned document,
or a README link to a missing sixth file.
```

```text
“Validate clean external installation”
means actually perform the required clean external installation verification.

It does NOT mean:
write an installation script,
inspect source structure,
or state that CI can run it later.
```

```text
“Compare core vs core + pack”
means perform the comparison required by the stage and record the actual result.

It does NOT mean:
describe what the expected difference should be.
```

Perform required discovery and selection processes literally.

If the specification says:

```text
generate candidate pool
→ build coverage matrix
→ remove redundancy
→ select final examples
```

then perform all four activities and persist their evidence.

Do not jump directly to a plausible-looking final selection.

Do not invent:

- source evidence;
- customer evidence;
- book contents;
- benchmark executions;
- agent outputs;
- measurements;
- command results;
- installation results;
- test passes;
- empirical findings.

Synthetic fixtures must always remain explicitly synthetic.

If evidence needed for a mandatory requirement is unavailable and cannot legitimately be obtained, STOP and ask me rather than weakening the stage.

For the remaining Business Building Skills stages specifically, preserve the accepted boundaries already established in Stages 1–15:

```text
customer evidence ≠ generated persona
revenue ≠ contribution ≠ cash
lead volume ≠ lead quality
design/evaluation evidence ≠ executed business outcome
approval ≠ validation
source-book claim ≠ independent professional evidence
pack design ≠ implemented pack
specified behaviour ≠ executed benchmark result
```

Do not silently reopen these distinctions simply because a later implementation would be easier without them.

## 5. Verification before completion

After doing the work, re-read the ORIGINAL current-stage section from the bootstrap specification.

Do not verify against your own research log or your interpretation of what the stage was supposed to mean.

Verify against the governing specification.

Inspect the ACTUAL repository contents.

Produce a conformance table:

| Requirement | Specification reference | Deliverable / evidence | Verification performed | Result |
|---|---|---|---|---|
| ... | ... | ... | ... | PASS / FAIL / BLOCKED |

Use only:

```text
PASS
FAIL
BLOCKED
NOT APPLICABLE
```

`NOT APPLICABLE` requires an explicit justification grounded in the bootstrap specification.

For exact requirements, perform explicit checks.

Examples:

```text
Required examples: 15
Actual examples: count repository entries
Distribution required: 3 / 3 / 3 / 3 / 3
Actual distribution: verify every level
Exact prompts required: 15
Actual prompts: inspect all 15
Result: PASS only if all checks pass
```

```text
Canonical specs required: 6
Actual canonical specs: list docs/
Required responsibilities: verify each file contents
Links: verify every documentation link resolves
Result: PASS only if all six exist and satisfy their contract
```

Verification must include substance, not just filenames.

Check where applicable:

- exact item counts;
- distribution across categories/levels;
- completeness;
- internal consistency;
- links;
- references;
- required prompts;
- required metadata;
- required tests;
- actual test results;
- actual command execution;
- actual installation behaviour;
- actual benchmark/evaluation output;
- preservation of earlier accepted decisions;
- contradiction with earlier stages;
- maturity/completion claims;
- prohibited premature implementation;
- source/evidence provenance.

For later implementation/validation stages, verification must compare the repository with the accepted Stage 15 primary example set and other accepted Stage 1–15 outputs rather than inventing a smaller “representative” target.

Do not weaken a validator or acceptance criterion to make incomplete work pass.

If anything is `FAIL`:

```text
repair it
→ verify again
```

If anything is `BLOCKED` and requires my input:

```text
STOP
→ ASK ME
```

Do not begin the next stage.

## 6. Research-log requirements

Each stage's durable research log must record enough information for a future conversation to understand and verify the stage without relying on chat history.

Where relevant include:

```text
stage goal
inputs inspected
sources actually accessed
source limitations
research performed
candidate pool
comparisons
analysis
decisions
rejected alternatives
exact outputs
verification
conformance table
unresolved questions
explicitly deferred work
exit assessment
inputs for the next stage
```

Do not claim a stage is complete in its research log until all mandatory stage requirements pass.

Do not write phrases such as:

```text
representative implementation
remaining examples can be added later
target coverage remains
future work will complete
execution pending
```

and then mark the stage complete if the governing specification requires those things in the current stage.

Where a stage is design-only, clearly distinguish complete design from later implementation. Where a stage requires implementation or execution, design evidence alone cannot satisfy it.

## 7. Commit the completed stage

Only after every mandatory current-stage requirement is `PASS`:

1. Persist the complete stage outputs.
2. Persist its verification/conformance evidence.
3. Update the bootstrap progress record accurately for `feat/bootstrap-3`.
4. Review the staged changes for unrelated files.
5. Commit only the current stage's work to `feat/bootstrap-3`.
6. Verify the remote branch points to the new commit.
7. Verify the intended files exist at that commit.

Commit messages must remain stage-scoped.

Example:

```text
docs: complete stage 16 canonical business stress tests
```

or:

```text
feat: complete stage 23 progressive coverage and extension packs
```

Do not combine several stages into one commit.

Do not place unfinished next-stage work in the current commit.

After the remote commit is verified, report:

```text
Stage:
Status: COMPLETE

Deliverables:
- ...

Verification:
- ...

Commit:
<full SHA>

Remaining blockers:
none
```

Only then may the next authorised stage begin.

## 8. Stage progression

Stages 16–26 are authorised, but authorisation does NOT make them one task.

The execution model is:

```text
STAGE 16 IS THE ONLY TASK
→ finish it completely
→ verify it completely
→ commit it completely

THEN

STAGE 17 IS THE ONLY TASK
→ finish it completely
→ verify it completely
→ commit it completely

THEN

STAGE 18 IS THE ONLY TASK

...
```

Continue this exact pattern through Stage 26.

Do not think:

```text
“I need to finish Stages 16–26.”
```

Think only:

```text
“I need to complete the current stage perfectly.”
```

The existence of a later stage must never be used to justify incomplete work in the current stage.

## 9. Context and interruption safety

The repository is the authoritative bootstrap state.

Do not rely on long conversation memory for previous stage decisions.

At the start of every new stage, reconstruct the required context from:

```text
bootstrap specification on feat/bootstrap-3
+
accepted Stage 1–15 outputs already present on feat/bootstrap-3
+
accepted Stage 16+ outputs committed earlier in this continuation
```

The Stage 15 completion boundary is commit `fbaed771716f30994eb30cf6678fad7d4d22e2c1`. Do not replace that boundary with a different branch's history.

If context becomes too large, STOP at the current verified stage boundary rather than compressing or skipping work.

It is better to complete fewer stages correctly than to reach Stage 26 incorrectly.

If interrupted during a stage:

- do not claim completion;
- preserve accurate partial work only if useful;
- identify the last fully verified commit;
- resume the SAME stage later.

## 10. Final bootstrap audit

After Stage 26 has individually passed and been committed, perform an additional end-to-end conformance audit.

Re-read the ORIGINAL bootstrap specification from `feat/bootstrap-3`.

Build a complete matrix covering Stage 0 through Stage 26 and all global acceptance gates.

For every stage verify:

```text
required research log exists
required deliverables exist
exact counts pass
exit criteria pass
completion receipt / accepted evidence exists
later stages did not contradict it improperly
```

For Stages 1–15, use the existing accepted completion receipts and immutable/durable evidence rather than re-performing the stages. Verify that later work did not invalidate their accepted outputs. If the final audit would require changing an accepted Stage 1–15 output, STOP and ask me before doing so.

Also verify global requirements including:

- source integrity;
- customer/value evidence discipline;
- offer/pricing requirements;
- acquisition/sales requirements;
- economics and operations;
- experimentation;
- diagnosis and repair;
- Extension Packs;
- 15 primary progressive examples;
- exact prompts;
- six canonical specifications;
- canonical stress tests;
- benchmark architecture;
- installation;
- repository integrity;
- README consistency;
- maturity claims.

If the final audit reveals a failure, the bootstrap is NOT COMPLETE.

Repair the owning Stage 16–26 work and rerun affected downstream checks. For an accepted Stage 1–15 defect requiring modification, STOP and ask me first.

Do not raise or mark a PR ready until the final conformance audit has zero unresolved mandatory failures.

## 11. PR and maturity rules

Do not:

- merge to `main`;
- mark a PR ready;
- promote registry maturity;
- publish a release;
- claim `working`;
- claim `benchmarked`;
- claim `mature`;

unless the corresponding evidence and bootstrap criteria actually exist and I have authorised the action where required.

A large number of files, commits or research logs is not evidence of maturity.

Maturity follows demonstrated acceptance criteria only.

Do not treat implementation presence as executed validation. Do not treat a deterministic structural check as a semantic Agent Skills benchmark. Do not treat a synthetic business fixture as live commercial validation.

## 12. Governing execution sequence

For EVERY remaining stage:

```text
READ THE ORIGINAL STAGE SPECIFICATION
        ↓
EXTRACT EVERY REQUIREMENT
        ↓
VERIFY PREREQUISITES
        ↓
STATE THE ACCEPTANCE CHECKLIST
        ↓
PERFORM THE REQUIRED RESEARCH / DESIGN / IMPLEMENTATION
        ↓
CREATE EVERY REQUIRED DELIVERABLE
        ↓
RE-READ THE ORIGINAL SPECIFICATION
        ↓
VERIFY ACTUAL OUTPUT AGAINST EVERY REQUIREMENT
        ↓
FAIL? → REPAIR
BLOCKED / USER DECISION? → STOP AND ASK
        ↓
ALL PASS
        ↓
PERSIST CONFORMANCE EVIDENCE
        ↓
COMMIT ONLY THIS STAGE
        ↓
VERIFY REMOTE COMMIT
        ↓
REPORT COMPLETION
        ↓
ONLY THEN START THE NEXT STAGE
```

The most important rule is:

# COMPLETE EACH STAGE AS IF IT WERE THE ONLY TASK I ASKED YOU TO DO.

Do not optimise for the whole bootstrap.

Do not preserve merely the “general intent”.

Follow the actual Business Building Skills bootstrap specification literally and verify that you did so.