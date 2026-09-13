# Progressive business exercises

All fifteen exercises are synthetic. Every `prompt.txt` is the exact accepted prompt, without an appended answer. Each `input.json` is the unchanged facts object extracted from that same prompt; it supplies no additional hidden facts.

## Reproduce an exercise

1. Choose a case and open its complete prompt. Use a fresh conversation or case workspace.
2. Give the subject only `prompt.txt` and, if useful, its matching `input.json`. Keep benchmark oracles and acceptance notes out of the subject context.
3. Write all outputs to a separate authorised directory. Retain the full response, actual calculation/tool results, errors, timestamps and host identity as exposed. Preserve all supplied accepted versions.
4. After the response is captured, assess it separately using the case oracle and [benchmark protocol](../benchmarks/README.md). No installed run is claimed by packaging a prompt.

The named skill/command selectors describe accepted responsibilities. Installable skill entries are not yet implemented. This exercise can be explored with an assistant that can read the prompt and execute arithmetic; that exploration must not be relabelled as installed product validation. No source checkout is needed to understand the complete prompt.

## Level 1

| Case | Exact prompt | Fixed facts |
|---|---|---|
| E01 · Fixed fee or hourly price | [prompt](level-01/E01/prompt.txt) | [facts](level-01/E01/input.json) |
| E02 · Paid-channel hypothesis against a referral baseline | [prompt](level-01/E02/prompt.txt) | [facts](level-01/E02/input.json) |
| E03 · Digital offer covers copying but not creation | [prompt](level-01/E03/prompt.txt) | [facts](level-01/E03/input.json) |

## Level 2

| Case | Exact prompt | Fixed facts |
|---|---|---|
| E04 · Bounded reporting diagnostic offer | [prompt](level-02/E04/prompt.txt) | [facts](level-02/E04/input.json) |
| E05 · Readiness checklist to qualified sale | [prompt](level-02/E05/prompt.txt) | [facts](level-02/E05/input.json) |
| E06 · Subscription renewal and recovery component | [prompt](level-02/E06/prompt.txt) | [facts](level-02/E06/input.json) |

## Level 3

| Case | Exact prompt | Fixed facts |
|---|---|---|
| E07 · Solo local bicycle service | [prompt](level-03/E07/prompt.txt) | [facts](level-03/E07/input.json) |
| E08 · Small team-reporting SaaS | [prompt](level-03/E08/prompt.txt) | [facts](level-03/E08/input.json) |
| E09 · Small notebook ecommerce business | [prompt](level-03/E09/prompt.txt) | [facts](level-03/E09/input.json) |

## Level 4

| Case | Exact prompt | Fixed facts |
|---|---|---|
| E10 · Lead growth without qualified growth | [prompt](level-04/E10/prompt.txt) | [facts](level-04/E10/input.json) |
| E11 · Profitable service is over capacity | [prompt](level-04/E11/prompt.txt) | [facts](level-04/E11/input.json) |
| E12 · Growing orders with an earlier cash crisis | [prompt](level-04/E12/prompt.txt) | [facts](level-04/E12/input.json) |

## Level 5

| Case | Exact prompt | Fixed facts |
|---|---|---|
| E13 · Kakeibo consumer subscription thesis | [prompt](level-05/E13/prompt.txt) | [facts](level-05/E13/input.json) |
| E14 · One-person FDE consultancy thesis | [prompt](level-05/E14/prompt.txt) | [facts](level-05/E14/input.json) |
| E15 · Production Skills commercial ecosystem thesis | [prompt](level-05/E15/prompt.txt) | [facts](level-05/E15/input.json) |
