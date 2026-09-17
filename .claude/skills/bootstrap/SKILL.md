---
name: bootstrap
description: Public entry point for resuming and executing the repository bootstrap. Invoke as /bootstrap. It reconstructs progress from repository state, starts at the next incomplete stage, and continues stage by stage until the bootstrap is complete or a genuine user decision is required.
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

No stage number, stage range, or repeated execution prompt is required.

## Default behaviour

Invocation of `/bootstrap` authorises execution of the remaining bootstrap from the next incomplete stage through the final stage, unless the user explicitly narrows the scope.

1. Find the current bootstrap execution contract under `docs/research-logs/`.
2. Read the governing bootstrap specification named by that contract.
3. Verify the current repository and working branch. Preserve existing local changes; never discard or overwrite unrelated work to switch branches.
4. Reconstruct accepted progress from repository state, committed research logs, and stage outputs. Do not use conversation memory as accepted state.
5. Determine the next incomplete stage from the governing bootstrap.
6. Invoke `bootstrap-stage-execution` for that stage.
7. Let stage execution use `bootstrap-research` and `direct-source-extraction` when required.
8. After the stage passes verification, commit it separately, push it to the working branch, and verify the remote commit.
9. Continue immediately with the next incomplete stage.
10. After the final stage, run the bootstrap's final/global acceptance audit.

## Stop condition

Stop only when progress genuinely depends on a user decision, such as:

- explicit approval required by the bootstrap;
- supplied-source replacement, removal, or demotion requiring permission;
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

Do not ask the user to restate the current stage, the remaining range, or the execution procedure when repository state already provides that information.
