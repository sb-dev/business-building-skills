# Stage 17: Regression and preservation policy

## 1. Preservation rule

A local failure changes the smallest responsible layer. The canonical preservation fixture `R01` states that only channel evidence fails while customer, offer, price and delivery remain supported. Changing all six layers is a benchmark failure; changing/retesting the channel alone is the expected bounded repair. Wider change is allowed only when new evidence implicates dependencies and the case record names them.

## 2. Exact six-step regression loop

Retain the original §24 sequence literally:

1. **escaped business-reasoning defect** — preserve the actual failed output/trace and impact; do not rewrite history;
2. **diagnose owning layer** — distinguish business reasoning, fixture, grader, tool/environment, evidence and permission failures;
3. **create smallest reproducible case** — remove irrelevant context while retaining the trigger, protected decisions and expected failure;
4. **add benchmark** — assign stable ID/version, graders and acceptance criteria before repair claims;
5. **prove old behaviour fails → prove repaired behaviour passes** — execute both against the same case/environment where comparable;
6. **retain permanently** — keep the regression fixture unless a documented contract change makes it obsolete, preserving lineage rather than silently deleting it.

## 3. Synthetic regression demonstration RG01

RG01 is explicitly synthetic, not an escaped production incident. Its old output responds to a channel-only failure by changing customer, offer, price, channel, delivery and brand; the retained expected result is FAIL. The repaired output changes only channel; with all other supplied accepted versions unchanged, the expected result is PASS. The verifier executes this old-fail/repaired-pass reference grader.

This demonstrates the regression machinery without falsely claiming a real deployed agent defect. Once real escapes exist, their raw evidence supersedes synthetic stand-ins for that defect class.

## 4. Changes to fixtures or graders

Never update an expected result merely because a new model or skill fails it. First decide whether the governing business contract changed or the test/grader is wrong. If the contract changes legitimately, version the case, preserve the previous result and document migration. If the implementation is wrong, repair implementation and retain the existing test. If the grader is wrong, add a grader regression and rerun affected trials.

## 5. Pack regressions

A pack-specific escape records both core and core-plus-pack versions, activation facts, precedence, pack-specific metrics and the actual behaviour difference. Repair the pack layer when only pack behaviour is implicated. Do not change core simply to make a broken pack test pass.
