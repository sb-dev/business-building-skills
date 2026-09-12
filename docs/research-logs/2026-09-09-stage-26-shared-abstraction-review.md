# Stage 26 — Shared-Abstraction Review

**Version:** 1.0 · **Date:** 9 September 2026 · **Status:** Bootstrap abstraction review complete

## 1. Rule

Promote only when at least two independent Production Skills domains demonstrate substantially the same reusable concept and centralisation is simpler than independent implementations. Similar names are not enough.

## 2. Candidates

| Candidate | Business Building evidence | Cross-domain evidence inspected | Decision |
|---|---|---|---|
| Extension Pack precedence | Pack facts/approved decisions must outrank defaults | Already canonical in Production Skills Project Contract | **Already family-owned; reuse** |
| Progressive example 5×3 model | Stage 15 | Already canonical family contract | **Already family-owned; reuse** |
| Installable skill self-containment | Stage 11/24 | Already canonical family contract | **Already family-owned; reuse** |
| Evidence-backed cross-domain handoff | Stage 9/20 | Family cross-domain spec already defines producing/consuming/minimum info/authority | **Use family handoff abstraction; keep business evidence fields domain-owned** |
| Assumption → evidence → decision record | Central to business experiments | Related research/UX/software patterns likely, but no second-domain schema inspected deeply enough here | **Observe; do not centralise** |
| Constraint diagnosis → smallest repair | Central to business evaluation | Production Skills family uses diagnosis/repair concepts across domains, but domain failure taxonomies differ | **Cross-domain candidate; do not create universal schema/runtime** |
| Preservation / mutation scope | Accepted business decisions and targeted repair | Strong analogous family production principle | **Candidate for minimal family wording, not a shared state engine** |
| Validity/confidence metadata | Business evidence requires scope/method/limits | Deep Research likely shares provenance/confidence needs | **Candidate; needs direct cross-domain comparison before extraction** |
| Human approval / authority record | External commercial commitments | Other production domains have approval concepts but semantics vary | **Keep domain-owned; family may retain generic authority notion** |
| Universal experiment contract | Business experiments | UI/UX/software experiments differ in population, causal method and artefacts | **Reject universal contract now** |
| Universal artefact/business graph | Not needed | Family spec explicitly rejects default universal graph | **Reject** |
| Universal provider router | Not needed | Family spec rejects default central provider router | **Reject** |
| Universal business-quality score | Explicitly rejected | Family evaluation is domain-specific | **Reject** |

## 3. Proposed future extraction evidence

For the three live candidates—assumption/evidence/decision, preservation/mutation scope, and validity/confidence—future work should compare at least Deep Research, UI/UX and Software Engineering implementations. Extract only the minimal invariant if it reduces duplication without erasing domain semantics.

A likely useful invariant is descriptive rather than executable:

```text
claim/decision identity
source or prior state
scope/conditions
confidence/validity
allowed authority/mutation
supersession/lineage
```

Do not implement this as a central database, graph, workflow DSL or universal JSON envelope until repeated implementations demonstrate that such machinery is necessary.

## 4. Bootstrap conclusion

Business Building Skills remains an independent domain repository. The family already owns the abstractions that are sufficiently proven: project packaging, progressive examples, Extension Packs, installation/evaluation separation and generic cross-domain handoffs. The novel business semantics remain local.

No change to the central Production Skills repository is justified by this stage alone.

## 5. Exit

All shared-abstraction candidates are either reused, retained for later evidence or explicitly rejected. The bootstrap process is complete through Stage 26, with known evidence/maturity gaps preserved rather than hidden.

*Stage 26 · Version 1.0 · 9 September 2026.*
