# Stage 24 — Installation and Repository Integrity

**Version:** 1.0 · **Date:** 9 September 2026 · **Status:** Structural validation implemented; runtime execution still to be run by CI/local checkout

## Implemented validation

- full Apache-2.0 licence text replaces the Stage 21 temporary notice;
- `scripts/validate_repo.py` checks four skill frontmatters, six canonical specs, licence and first pack showcase;
- `tests/test_repo.py` and `tests/test_economics.py` provide standard-library deterministic tests;
- `scripts/smoke_install.py` copies each core skill into a clean temporary consumer directory and checks local references, independent of the source checkout;
- GitHub Actions workflow runs validator, tests and smoke install on Python 3.12.

No provider SDK, credential or undocumented source checkout is required for these checks.

## Installation claim boundary

The repository follows `skills/<name>/SKILL.md`, which current Skills CLI tooling discovers from Git repositories. The README documents the intended `npx skills add` path. This stage does **not** claim that a networked `npx skills add` command was executed from this environment; the clean-copy smoke test validates the repository's self-containment contract locally, and CI will execute the deterministic suite after the branch is pushed.

Semantic skill quality also remains separate: a copied SKILL.md is installable structure, not proof that an agent produced a passing business decision.

## Integrity gates

Expected commands in a checkout:

```bash
python3 scripts/validate_repo.py
python3 -m unittest discover -s tests -p 'test_*.py'
python3 scripts/smoke_install.py
```

Stage 24 exit is satisfied at the repository-contract level once these run successfully in CI/local checkout. Until execution is observed, status is `implemented validation, execution pending`, not a fabricated pass.

## Remaining gaps

- only representative Level 1–5 example directories are implemented; the full 15-example product set remains Stage 23 expansion work;
- semantic core-vs-pack and canonical stress-test agent runs are not recorded;
- provider integrations are intentionally absent;
- Stage 2 full-book access gaps remain;
- clean networked Skills CLI installation should be added as a release smoke test when available.

*Stage 24 · Version 1.0 · 9 September 2026.*
