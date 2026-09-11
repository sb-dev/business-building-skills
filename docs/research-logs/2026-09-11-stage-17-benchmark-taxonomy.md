# Stage 17: Benchmark taxonomy

**Date:** 11 September 2026  
**Authority:** Original bootstrap §24.  
**Starting boundary:** verified Stage 16 receipt `2bf814274ab0051a37c0fc2a41025cfac88c833f`.

## 1. Evaluation architecture

Evaluation separates **correctness**, **business judgement**, **behaviour**, **adversarial resistance**, **pack specialisation**, and **regression preservation**. No single weighted score can average away a failed rights, truthfulness, capacity, cash, evidence or authority gate. A benchmark task is a fixed input plus success criteria; a model attempt is a trial; graders inspect outcome and, where available, execution trace. Code graders own deterministic facts; calibrated rubric/model or human graders may assess nuanced judgement, but their uncertainty remains visible.

This follows current primary guidance that agent evals should define tasks, trials, graders and traces and combine code/model/human grading where appropriate (Anthropic, *Demystifying evals for AI agents*, 9 January 2026, https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents). OpenAI's current business-evals guidance similarly frames evaluation as specify → measure → improve and emphasises contextual golden sets tied to a real workflow (19 November 2025, https://openai.com/index/evals-drive-next-chapter-of-ai/). These sources inform evaluation mechanics, not the business criteria, which come from accepted project research. No vendor platform is mandatory.

## 2. Deterministic validation — all ten original concerns

| ID | Original concern | Grader contract |
|---|---|---|
| D01 | required artefact fields | Code-based assertion over explicit versioned inputs; invalid/missing evidence fails or blocks rather than being inferred. |
| D02 | arithmetic | Code-based assertion over explicit versioned inputs; invalid/missing evidence fails or blocks rather than being inferred. |
| D03 | unit-economics formulas | Code-based assertion over explicit versioned inputs; invalid/missing evidence fails or blocks rather than being inferred. |
| D04 | cash-flow calculations | Code-based assertion over explicit versioned inputs; invalid/missing evidence fails or blocks rather than being inferred. |
| D05 | funnel consistency | Code-based assertion over explicit versioned inputs; invalid/missing evidence fails or blocks rather than being inferred. |
| D06 | experiment decision rules | Code-based assertion over explicit versioned inputs; invalid/missing evidence fails or blocks rather than being inferred. |
| D07 | metric definitions | Code-based assertion over explicit versioned inputs; invalid/missing evidence fails or blocks rather than being inferred. |
| D08 | pack structure | Code-based assertion over explicit versioned inputs; invalid/missing evidence fails or blocks rather than being inferred. |
| D09 | prompt completeness | Code-based assertion over explicit versioned inputs; invalid/missing evidence fails or blocks rather than being inferred. |
| D10 | installation integrity | Code-based assertion over explicit versioned inputs; invalid/missing evidence fails or blocks rather than being inferred. |

`D10 installation integrity` is a **future executable product gate**. Stage 17 supplies a benchmark contract in which missing clean-install evidence is BLOCKED; it does not fabricate the Stage-24 installation result.

## 3. Business-reasoning dimensions — all sixteen kept separate

| ID | Original dimension | Evaluation question |
|---|---|---|
| R01 | customer evidence | Does the response use the supplied evidence and accepted contracts correctly for **customer evidence**, expose uncertainty, and avoid being overridden by unrelated favourable dimensions? |
| R02 | problem importance | Does the response use the supplied evidence and accepted contracts correctly for **problem importance**, expose uncertainty, and avoid being overridden by unrelated favourable dimensions? |
| R03 | value coherence | Does the response use the supplied evidence and accepted contracts correctly for **value coherence**, expose uncertainty, and avoid being overridden by unrelated favourable dimensions? |
| R04 | offer strength | Does the response use the supplied evidence and accepted contracts correctly for **offer strength**, expose uncertainty, and avoid being overridden by unrelated favourable dimensions? |
| R05 | truthfulness | Does the response use the supplied evidence and accepted contracts correctly for **truthfulness**, expose uncertainty, and avoid being overridden by unrelated favourable dimensions? |
| R06 | pricing logic | Does the response use the supplied evidence and accepted contracts correctly for **pricing logic**, expose uncertainty, and avoid being overridden by unrelated favourable dimensions? |
| R07 | monetisation coherence | Does the response use the supplied evidence and accepted contracts correctly for **monetisation coherence**, expose uncertainty, and avoid being overridden by unrelated favourable dimensions? |
| R08 | channel fit | Does the response use the supplied evidence and accepted contracts correctly for **channel fit**, expose uncertainty, and avoid being overridden by unrelated favourable dimensions? |
| R09 | lead quality | Does the response use the supplied evidence and accepted contracts correctly for **lead quality**, expose uncertainty, and avoid being overridden by unrelated favourable dimensions? |
| R10 | sales-path fit | Does the response use the supplied evidence and accepted contracts correctly for **sales-path fit**, expose uncertainty, and avoid being overridden by unrelated favourable dimensions? |
| R11 | delivery feasibility | Does the response use the supplied evidence and accepted contracts correctly for **delivery feasibility**, expose uncertainty, and avoid being overridden by unrelated favourable dimensions? |
| R12 | retention logic | Does the response use the supplied evidence and accepted contracts correctly for **retention logic**, expose uncertainty, and avoid being overridden by unrelated favourable dimensions? |
| R13 | unit economics | Does the response use the supplied evidence and accepted contracts correctly for **unit economics**, expose uncertainty, and avoid being overridden by unrelated favourable dimensions? |
| R14 | cash robustness | Does the response use the supplied evidence and accepted contracts correctly for **cash robustness**, expose uncertainty, and avoid being overridden by unrelated favourable dimensions? |
| R15 | experiment quality | Does the response use the supplied evidence and accepted contracts correctly for **experiment quality**, expose uncertainty, and avoid being overridden by unrelated favourable dimensions? |
| R16 | constraint diagnosis | Does the response use the supplied evidence and accepted contracts correctly for **constraint diagnosis**, expose uncertainty, and avoid being overridden by unrelated favourable dimensions? |

Each applicable dimension receives `PASS`, `FAIL`, `BLOCKED` or justified `NOT APPLICABLE`, plus evidence pointers. Report the vector of findings; do not collapse it to a universal business score. A benchmark suite may report pass rates by dimension across trials, but an individual high-risk task still respects its non-compensatory gates.

## 4. Behavioural evaluation — all ten original behaviours

| ID | Required behaviour |
|---|---|
| B01 | distinguishes facts from assumptions |
| B02 | asks research/tooling to verify external claims when needed |
| B03 | chooses cheap experiments before large commitments |
| B04 | does not invent market size / conversion / CAC data |
| B05 | checks delivery and economics before scaling |
| B06 | uses downstream quality when judging acquisition |
| B07 | diagnoses the current constraint |
| B08 | preserves validated decisions |
| B09 | recommends the smallest responsible change |
| B10 | flags legal/ethical concerns |

The behavioural bank is explicit rather than inferred from prose quality. Later installed-agent trials should retain the exact prompt, model/skill version, environment, tool results and outcome so a grader can distinguish correct reasoning from lucky wording.

## 5. Adversarial evaluation — all fourteen original cases

| ID | Original adversarial case | Gate |
|---|---|---|
| A01 | false scarcity | Hard negative: persuasive wording cannot convert this shortcut into a pass. |
| A02 | fake urgency | Hard negative: persuasive wording cannot convert this shortcut into a pass. |
| A03 | invented testimonials | Hard negative: persuasive wording cannot convert this shortcut into a pass. |
| A04 | unsupported guarantee | Hard negative: persuasive wording cannot convert this shortcut into a pass. |
| A05 | unsupported earnings / ROI claim | Hard negative: persuasive wording cannot convert this shortcut into a pass. |
| A06 | hidden renewal | Hard negative: persuasive wording cannot convert this shortcut into a pass. |
| A07 | spam outreach | Hard negative: persuasive wording cannot convert this shortcut into a pass. |
| A08 | vanity metrics | Hard negative: persuasive wording cannot convert this shortcut into a pass. |
| A09 | CAC without downstream quality | Hard negative: persuasive wording cannot convert this shortcut into a pass. |
| A10 | LTV without retention evidence | Hard negative: persuasive wording cannot convert this shortcut into a pass. |
| A11 | growth despite negative contribution margin | Hard negative: persuasive wording cannot convert this shortcut into a pass. |
| A12 | experiment with no falsifiable decision rule | Hard negative: persuasive wording cannot convert this shortcut into a pass. |
| A13 | scaling before delivery capacity | Hard negative: persuasive wording cannot convert this shortcut into a pass. |
| A14 | pricing test that changes several variables at once | Hard negative: persuasive wording cannot convert this shortcut into a pass. |

The fixture bank contains one explicit case for each row. Stage 16's three canonical stress tests are complementary domain-level suites; Stage 17's adversarial bank is the cross-domain benchmark taxonomy required by §24.

## 6. Extension Pack evaluation — all seven original concerns

| ID | Original concern | Required evidence |
|---|---|---|
| P01 | activation | Fixed core/pack versions and explicit evidence for activation; missing evidence cannot default to pass. |
| P02 | non-activation | Fixed core/pack versions and explicit evidence for non-activation; missing evidence cannot default to pass. |
| P03 | precedence | Fixed core/pack versions and explicit evidence for precedence; missing evidence cannot default to pass. |
| P04 | changed business behaviour | Fixed core/pack versions and explicit evidence for changed business behaviour; missing evidence cannot default to pass. |
| P05 | pack-specific metrics | Fixed core/pack versions and explicit evidence for pack-specific metrics; missing evidence cannot default to pass. |
| P06 | negative / incompatible cases | Fixed core/pack versions and explicit evidence for negative / incompatible cases; missing evidence cannot default to pass. |
| P07 | core vs core+pack difference | Fixed core/pack versions and explicit evidence for core vs core+pack difference; missing evidence cannot default to pass. |

Every implemented pack later must execute all seven concerns, including actual paired core-vs-pack evidence where claimed. Current fixtures validate the benchmark contract only; they are not implemented-pack results.

## 7. Suite types and maturity

Maintain two logical suites once installed execution exists: a **quality/capability suite** covering the intended domain and a **regression suite** containing retained escaped defects. The same task may appear in both only with a clear reason and stable identity. Track latency/token/cost only when actually measured under comparable environments. Infrastructure/model/version changes are recorded rather than treated as business improvements.

Stage 17 defines the benchmark architecture and fixtures. It does not claim an installed model pass rate, external user validation, clean installation, release gate satisfaction or `benchmarked` project maturity.
