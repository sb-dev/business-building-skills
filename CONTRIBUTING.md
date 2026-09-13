# Contributing to Business Building Skills

Start with a concrete business-reasoning defect, a missing evidence distinction or a reusable business mechanism. Identify the responsible canonical specification and the accepted decisions the change must preserve. The [system specification](docs/01-business-building-skills-system-spec.md#2-document-ownership-and-conflict-handling) maps ownership across all six documents.

## Prepare a change

1. State the problem, affected decision and evidence. Cite sources actually accessed, their dates and reading limits. Distinguish an authored control, an executed agent response and a real business outcome.
2. Supply a small synthetic case or material you are authorised to contribute. Include the exact prompt, relevant fixed facts, actual failure evidence when available, expected responsibilities and protected versions. Keep expected answers outside the subject input.
3. Change the responsible layer and review its real dependencies. Preserve the original failure and explain any retry. Keep observations, assumptions, revenue, contribution, cash and external authority distinct.
4. Run the checks below on the proposed revision. Report actual results and limitations. A deterministic pass is not a semantic benchmark or an installation result.
5. Describe why the change is needed, what behaviour changes and what evidence supports it. During the bootstrap, changes remain on `feat/bootstrap-3`, with the stage-scoped conformance and remote verification required by the execution contract. Accepted Stage 1–15 work needs the owner's permission before modification.

## Local verification

Use Python 3.12; this revision is exercised locally with Python 3.12.14. The checks use only the standard library and need no service account or package installation. From the repository root:

```sh
python tests/validate_repository.py
python -m unittest discover -s tests -p 'test_*.py' -v
```

The repository check verifies the four contract inventories, all 32 complete command contracts, modes, all 15 exact prompts and extracted facts, three cases per level, separate oracles, source identities and public documentation links. Missing authorised distribution terms remain a Stage 21 blocker. The calculation tests execute the pricing workloads and dated cash alternatives, including negative/boundary controls. See [tests](tests/README.md) for command results and report handling.

The [CI workflow](.github/workflows/validate.yml) uses the same commands on push and pull request. It has read-only repository permissions, does not persist checkout credentials and uses no commercial credentials. A local run does not establish a remote CI result. Hosted workflow execution will be recorded after the complete stage can be committed.

## Skills, examples and packs

The [skill inventory](skills/README.md) currently contains accepted contracts for implementation, not installable skills. A later installation unit must provide a real `SKILL.md`, complete local resources and actual host/discovery evidence under [specification 03](docs/03-business-building-skills-repository-and-contracts-spec.md). Do not advertise an installation procedure before it has worked on the named host.

Keep all [15 primary cases](examples/README.md) and their exact prompts. Author new regression cases alongside the retained originals. The [benchmark protocol](benchmarks/README.md) separates subject inputs, evaluator material and captured runs. A pack needs a reusable change in business behaviour, its complete required contents and actual core-versus-pack and authoring evidence under [specification 05](docs/05-business-building-customisation-packs-spec.md).

## Contribution rights

Submit only work and data you have authority to contribute. Identify third-party components, citations and applicable notices. Do not include customer databases, credentials, private transcripts, source-book PDFs or substantial copyrighted passages. Independently express source ideas and preserve their attribution and limitations.

Project material is distributed under the [MIT License](LICENSE). This contribution procedure introduces no additional copyright assignment or contributor licence agreement. The project licence does not grant rights in the source books or other third-party material.
