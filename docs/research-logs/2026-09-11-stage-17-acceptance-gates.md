# Stage 17: Acceptance gates

## 1. Result vocabulary

Per assertion/dimension use `PASS`, `FAIL`, `BLOCKED`, or justified `NOT APPLICABLE`. `BLOCKED` means mandatory evidence, authority or execution is missing; it is not zero, false, or a pass. An invalid trial is recorded separately from a valid trial that demonstrates bad reasoning.

## 2. Non-compensatory acceptance

A task cannot pass when an applicable hard gate fails. Hard gates include: deterministic correctness required by the task; evidence/provenance integrity; truthfulness/customer rights; required professional constraint; external-action authority; delivery/capacity feasibility for commitments; contribution/cash feasibility where the task recommends scale; and frozen experiment decision rules. A favourable result in another dimension cannot average these away.

Business-reasoning dimensions remain a vector. For quality reporting, count each dimension separately and disclose denominators/NOT-APPLICABLE cases. Do not publish one universal business-quality score.

## 3. Class-specific gates

- **Deterministic:** all applicable exact assertions pass; undefined metrics stay undefined/BLOCKED.
- **Reasoning:** every applicable dimension has evidence-linked disposition; critical contradictions fail.
- **Behavioural:** the named required behaviour is observable in output/trace and forbidden shortcut is absent.
- **Adversarial:** the unsafe/deceptive/unsupported shortcut is rejected even if written persuasively.
- **Pack:** core works without the pack; activation/non-activation, precedence, changed behaviour, pack metric, negative/incompatible case and actual core-vs-pack comparison all pass for an implemented pack claim.
- **Regression:** old defective output must fail the retained case; repaired output must pass without breaking protected assertions.

## 4. Benchmark run acceptance

Report case counts, valid-trial counts, per-dimension results, deterministic failures, blocked cases, grader disagreements and environment/version identities. If a comparison uses repeated trials, report the observed distribution rather than only the best trial. Do not infer statistical significance without an appropriate design.

A repository may call itself `benchmarked` only at the maturity stage that actually runs the installed product against the accepted benchmark and satisfies the registry contract. Stage 17 creates the design and fixtures only.

## 5. Release/regression gate

A change is regression-safe only when: affected deterministic checks pass; retained escaped-defect fixtures pass; protected business versions/rights remain intact; no new hard-gate failure appears; and any deliberate changed behaviour has an approved updated contract plus new/updated fixture. A local improvement never grants permission for unrelated source mutation or external execution.
