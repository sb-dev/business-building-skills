# Repository verification

These checks exercise source packaging and fixed deterministic cases. They are not an installed agent runtime, semantic benchmark, professional clearance or commercial outcome.

Use Python 3.12 and its standard library. Python 3.12.14 is the pinned CI interpreter and the actual local version used for Stage 21. Reading or drafting business records does not require Python.

```sh
python tests/validate_repository.py
python -m unittest discover -s tests -p 'test_*.py' -v
```

The validator derives the repository root from its own location, verifies the source contract inventories and all packaged primary inputs/oracles, and checks local documentation targets. It prints a JSON report to stdout. Use `--report /absolute/new-report.json` to also save the report; the target must not exist and must be outside the validated repository, so source inputs and historical receipts are preserved. Exit 0 means these checks pass, 1 means a failure, and 2 means a required scaffold item is blocked. Missing project licence terms are reported explicitly; file presence alone does not prove owner authorisation, which the stage conformance record must establish.

Unit tests execute every E01 workload and the E12 baseline, conditional-deposit and reduced-order cash schedules against independent exact expected values. They also challenge unsupported/missing/non-finite numbers, zero denominators, incomplete prompts and oracle contamination. Calculation results are fixtures only; no production accounting engine is introduced.

The [workflow](../.github/workflows/validate.yml) runs these commands with `contents: read` and no retained checkout credentials. Its action revisions were inspected at immutable source identities: checkout v7.0.1 and setup-python v7.0.0 both use Node 24 and document a minimum Actions runner of 2.327.1. Hosted Ubuntu 24.04 is the declared target; an actual remote run is still required before claiming that environment passed. No service accounts, package dependencies, customer data or commercial side effects are needed.

Historical bootstrap verifiers retain their original inputs and receipts. Do not rerun them against a changing progress file to manufacture current results. The [Stage 21 conformance record](../docs/research-logs/2026-09-13-stage-21-production-scaffold.md) records the actual scope and remaining blocker.
