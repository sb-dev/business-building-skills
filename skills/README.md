# Skill contract inventory

This directory packages the accepted command responsibilities for implementation and checks. The JSON files are source contracts consumed by repository validation; they are not an Agent Skills host interface. No installable `SKILL.md` entry exists in this scaffold.

| Independent unit | Complete contract | Logical selectors |
|---|---|---:|
| business-build | [contract](business-build/contract.json) | 10 |
| business-grow | [contract](business-grow/contract.json) | 8 |
| business-evaluate | [contract](business-evaluate/contract.json) | 7 |
| business-pack-author | [contract](business-pack-author/contract.json) | 7 |

The [machine-readable catalogue](catalogue.json) records current implementation state. Each selector retains all nine accepted responsibility fields and any explicit modes. The [canonical repository contract](../docs/03-business-building-skills-repository-and-contracts-spec.md) owns the exact descriptions, mutation boundaries, local reference requirements, independence and installation procedure.

Stage 22 implements and executes the first bounded vertical. Future installation units require a real entry and directly reachable command, core-rule, business-record and pack references. Do not turn these inventory files into a universal command runtime or claim that copying them installs a skill. Core operation remains independent of packs, siblings, external providers and Pactwright.
