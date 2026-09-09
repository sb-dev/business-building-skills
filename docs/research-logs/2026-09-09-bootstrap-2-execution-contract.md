Execute the bootstrap process below. Treat EACH STAGE AS A SEPARATE, COMPLETE TASK, exactly as though it were the only task I had asked you to perform.

Bootstrap specification: https://github.com/sb-dev/business-building-skills/blob/main/docs/research-logs/2026-09-08-business-building-skills-new-project-bootstrap-process.md

Repository: `sb-dev/business-building-skills`

Working branch: `feat/bootstrap-2`

Starting point: `main` — the clean bootstrap workspace. Do not reuse work from `feat/bootstrap` or any artefact produced by the failed bootstrap attempt unless I explicitly instruct you to do so.

Stages authorised: Stages 1–26, executed strictly sequentially. Stage 0 already exists as the bootstrap workspace.

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
- has been committed to `feat/bootstrap-2`;
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

Do not use `feat/bootstrap` as an implementation source, shortcut, template or authority. This is a clean execution from `main`.

You may independently rediscover the same good decisions if the evidence leads there, but do not copy the failed bootstrap forward simply because work already exists.

If ANY question requires my input, STOP THE ENTIRE PROCESS AND ASK ME.

This includes:

- ambiguous requirements;
- conflicting requirements;
- uncertainty about what the specification requires;
- uncertainty about the approved baseline;
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

Use only `feat/bootstrap-2` throughout this bootstrap unless I explicitly change the branch strategy.

## 3. Before starting EACH stage

At the beginning of every stage:

1. Re-read the ORIGINAL bootstrap specification from `main`.
2. Read the complete section for the current stage.
3. Read any global principles, acceptance gates and cross-references that constrain that stage.
4. Read the accepted outputs of earlier stages from `feat/bootstrap-2`.
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

Give the current stage the same care, research depth, analysis, implementation effort and verification you would give it if no other bootstrap stages existed.

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

Do not weaken a validator or acceptance criterion to make the work pass.

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

## 7. Commit the completed stage

Only after every mandatory current-stage requirement is `PASS`:

1. Persist the complete stage outputs.
2. Persist its verification/conformance evidence.
3. Update the bootstrap progress record accurately.
4. Review the staged changes for unrelated files.
5. Commit only the current stage's work to `feat/bootstrap-2`.
6. Verify the remote branch points to the new commit.
7. Verify the intended files exist at that commit.

Commit messages must remain stage-scoped.

Example:

```text
docs: complete stage 4 business customer and value model
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

Stages 1–26 are authorised, but authorisation does NOT make them one task.

The execution model is:

```text
STAGE 1 IS THE ONLY TASK
→ finish it completely
→ verify it completely
→ commit it completely

THEN

STAGE 2 IS THE ONLY TASK
→ finish it completely
→ verify it completely
→ commit it completely

THEN

STAGE 3 IS THE ONLY TASK

...
```

Continue this exact pattern through Stage 26.

Do not think:

```text
“I need to finish 26 stages.”
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
original bootstrap specification on main
+
accepted earlier stage outputs on feat/bootstrap-2
```

If context becomes too large, STOP at the current verified stage boundary rather than compressing or skipping work.

It is better to complete fewer stages correctly than to reach Stage 26 incorrectly.

If interrupted during a stage:

- do not claim completion;
- preserve accurate partial work only if useful;
- identify the last fully verified commit;
- resume the SAME stage later.

## 10. Final bootstrap audit

After Stage 26 has individually passed and been committed, perform an additional end-to-end conformance audit.

Re-read the ORIGINAL bootstrap specification from `main`.

Build a complete matrix covering Stage 0 through Stage 26 and all global acceptance gates.

For every stage verify:

```text
required research log exists
required deliverables exist
exact counts pass
exit criteria pass
commit exists
later stages did not contradict it improperly
```

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

Repair the owning stage and rerun affected downstream checks.

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

## 12. Governing execution sequence

For EVERY stage:

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

Follow the actual specification literally and verify that you did so.