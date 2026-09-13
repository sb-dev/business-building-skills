# Benchmark source and run protocol

[cases.json](cases.json) registers all fifteen accepted primary cases at three per level, with source identities and distinct prompt, facts and oracle paths. Paths in this manifest resolve from the repository root. The [examples](../examples/README.md) supply complete subject inputs. `oracles/` contains evaluator-only expected responsibilities, findings, negative controls, preservation requirements and dimensions. Do not expose it to the subject.

The [evaluation contracts](oracles/evaluation-contracts.json) preserve all ten deterministic categories, sixteen reasoning dimensions, ten behavioural dimensions, fourteen added adversaries, three canonical stress structures, seven pack evaluation obligations, nine pack profiles (eight independent packs plus advisory mode), fourteen case-contract fields and seven regression steps from the accepted corpus. Authored positive/negative controls are calibration material, not captured agent output. A pack profile does not establish an implemented pack.

## Run and assess

1. Freeze the case ID/version, exact prompt and facts hashes, actual core revision/distribution, pack condition or core-only, host/model identity as exposed, allowed tools and output directory. Use a fresh subject context; do not supply this document or oracle contents as answers.
2. Use the host's actual supported loading mechanism and capture discovery and resource access when claiming an installed run. Source-only checks cannot stand in for that execution.
3. Retain the entire response, produced artefacts, tool calls/results, errors and incomplete attempts. A retry has a separate attempt ID and reason. Keep source and output hashes and actual runtime metadata; unavailable metadata stays unknown.
4. Give a separate evaluator the frozen subject inputs, captured response/trace and matching oracle. Grade the relevant dimensions as PASS, FAIL, BLOCKED or justified NOT APPLICABLE, with actual evidence locators. Arithmetic requires executed results. Assess meaning, including adequate alternatives; keyword matching is not business reasoning evaluation.
5. Preserve the business decision and its growth-gate findings separately from response conformance. A correctly blocked cash-dependent expansion can be a conforming answer. Do not average dimensions into a business score.

No installed runs are present at this scaffold revision. Record actual attempts only when executed; never create placeholder output files or fill expected results into a run receipt. Stage 22 owns the installed first vertical, Stage 23 the full progressive/pack execution, and Stage 24 the distinct clean/selective installation verification. These stages do not reduce the accepted case set.

Run `python tests/validate_repository.py` and `python -m unittest discover -s tests -p 'test_*.py' -v` from the repository root for the implemented deterministic checks. The complete [testing specification](../docs/04-testing-and-benchmark-spec.md) owns semantic, stress, adversarial, pack and regression acceptance. Later run reports must identify their actual evidence and compatible revisions before supporting a product or maturity claim.
