# Stage 17: Evaluation research and source limits

## Inputs inspected

Original bootstrap §24 and applicable global gates; accepted Stage 15 progressive cases; Stage 16 canonical stress tests; Stage 13 command boundaries; Stage 14 pack evaluation contract; Stage 7 deterministic economics/cash handoff; Stage 8 preservation/repair rules; Stage 9 professional handoffs.

## Fresh evaluation-method sources

### R01 — Anthropic, “Demystifying evals for AI agents” (9 January 2026)
https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents

Read definitions of task/trial/grader/trace, code/model/human grader trade-offs, regression/capability suites and advice to start from concrete requirements/failures. Retained: explicit task contracts, multiple grader types, trace evidence, stable regression cases and repeated trials for nondeterministic systems. Limit: practitioner guidance, not proof that a particular grader or trial count is optimal for this repository; its suggested early task counts are not adopted as a project quota.

### R02 — OpenAI, “How evals drive the next chapter in AI for businesses” (19 November 2025)
https://openai.com/index/evals-drive-next-chapter-of-ai/

Read the specify → measure → improve framing and contextual/golden-set discussion. Retained: define workflow-specific success and failure before measurement and grow a living case set from domain judgement. Limit: broad guidance, not a current product/platform requirement or substitute for the repository's domain acceptance contract.

### R03 — Anthropic, “Quantifying infrastructure noise in agentic coding evals” (5 February 2026)
https://www.anthropic.com/engineering/infrastructure-noise

Read the finding that environment configuration can materially affect agentic benchmark results. Retained: record environment/tool/runtime configuration and avoid attributing every benchmark delta to business reasoning. Limit: coding-agent measurements do not provide a numeric noise estimate for this business benchmark.

## Design decisions

Use deterministic graders wherever correctness is formal; use separate domain dimensions for judgement; treat truthfulness/rights/cash/capacity/authority as non-compensatory gates; retain exact traces/versions for installed trials; and convert real escapes into permanent smallest reproducible regressions. Synthetic bootstrap fixtures define contracts now but are not evidence of deployed agent quality.
