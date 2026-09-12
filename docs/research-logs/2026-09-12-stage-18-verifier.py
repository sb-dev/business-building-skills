#!/usr/bin/env python3
from pathlib import Path
import hashlib, json, re, sys

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"
LOGS = DOCS / "research-logs"

EXPECTED = [
    "01-business-building-skills-system-spec.md",
    "02-business-building-skills-workflows-and-artifacts-spec.md",
    "03-business-building-skills-repository-and-contracts-spec.md",
    "04-testing-and-benchmark-spec.md",
    "05-business-building-customisation-packs-spec.md",
    "06-business-building-extension-pack-catalogue.md",
]

results=[]
def check(name, ok, detail=""):
    results.append({"name":name,"passed":bool(ok),"detail":detail})

def text(name):
    return (DOCS/name).read_text(encoding="utf-8")

def has_all(t, xs): return all(x in t for x in xs)

def ordered(t, xs):
    pos=-1
    for x in xs:
        n=t.find(x, pos+1)
        if n < 0: return False
        pos=n
    return True

# Exact canonical file set.
actual=sorted(p.name for p in DOCS.glob("0[1-6]-*.md"))
check("exactly six prescribed canonical specs", actual==EXPECTED, f"actual={actual}")
for n in EXPECTED:
    p=DOCS/n
    check(f"{n} exists and substantive", p.is_file() and p.stat().st_size>8000, f"bytes={p.stat().st_size if p.exists() else 0}")

T={n:text(n) for n in EXPECTED}

# §25 ownership coverage.
owners={
EXPECTED[0]: ["Mission","Scope and professional boundary","Source-book and evidence relationship","Governing principles","Business-system architecture","Four core skills","Execution boundary","Legal and ethical boundary","Implementation build order","System acceptance"],
EXPECTED[1]: ["Customer and value artefacts","Offer and pricing artefacts","Money-model artefact","Acquisition and channel workflow","Sales workflow","Delivery and capacity artefacts","Retention and expansion artefacts","Unit-economics artefact","Cash artefact","Assumption register","Experiment contract","Learning record","Constraint diagnosis","Preservation and repair record","Legal/professional handoff"],
EXPECTED[2]: ["Target repository layout","SKILL.md contract","Command contract schema","Reference organisation","Scripts and deterministic helpers","Tool integration contract","Independent installation unit","Installation contract","CI contract","Technical acceptance gates"],
EXPECTED[3]: ["Deterministic validation","Business-reasoning rubric","Adversarial evaluation","Progressive examples","Canonical stress tests","Extension Pack evaluation","Regression policy","Installation evaluation","Release gates"],
EXPECTED[4]: ["Pack model","Fourteen business-model dimensions","Activation contract","Precedence","Core effects","Pack-aware metrics","Pack evaluation","Packaging","Pack authoring workflow"],
EXPECTED[5]: ["Catalogue policy","Profile and selection rationale","Cross-catalogue selection guidance","Exact showcase prompt","Pack-specific evaluations","Current maturity","Catalogue maturity and implementation gate"],
}
for n, req in owners.items():
    missing=[x for x in req if x not in T[n]]
    check(f"{n} owns all §25 responsibilities", not missing, f"missing={missing}")

# System invariants.
sysdoc=T[EXPECTED[0]]
check("system preserves four skill architecture", has_all(sysdoc,["`business-build`","`business-grow`","`business-evaluate`","`business-pack-author`","32 logical command contracts"] ))
check("system preserves source-book capability rule", has_all(sysdoc,["capabilities, not books","source idea","evaluation criterion","benchmark case"]))
check("system keeps legal constraint and action authority separate", has_all(sysdoc,["project truthfulness/treatment boundary","applicable specialist constraint","action authority"]))
check("system rejects one-number quality", "Never collapse" in sysdoc or "Never collapse customer evidence" in sysdoc)

# Workflow exact contracts.
w=T[EXPECTED[1]]
check("workflow has all 15 business-map IDs", all(f"B{i:02d}" in w for i in range(1,16)))
check("workflow has offer O01-O14", all(f"O{i:02d}" in w for i in range(1,15)))
check("workflow has commercial arithmetic N/K/C", has_all(w,["N = G - D - F","C = N - K","contribution margin = C / N"]))
check("workflow has 10 assumption classes", has_all(w,["customer exists","problem matters","customer can be reached","offer is understood","customer will pay","channel is economical","delivery works","customer receives promised value","customer stays / repeats","economics remain viable at scale"]))
check("workflow has exact 9 experiment concerns", has_all(w,["1. assumption;","2. hypothesis;","3. cheapest valid test;","4. target population;","5. success/failure signal;","6. guardrails;","7. duration/sample requirements where relevant;","8. confounders;","9. decision rule."]))
check("workflow has full learning record", has_all(w,["observed evidence","what remains unknown","next experiment / commitment"]))
check("workflow has all 15 constraint routes", has_all(w,["demand\nlead quality","conversion","price","retention","delivery capacity","gross margin","cash","sales capacity","fulfilment quality","onboarding","product value","trust","measurement / evidence integrity","experiment design / inference"]))
check("workflow has RR01-RR08", all(f"RR{i:02d}" in w for i in range(1,9)))
check("workflow has H01-H08", all(f"H{i:02d}" in w for i in range(1,9)))

# Repository/command contract exactness.
r=T[EXPECTED[2]]
commands={
"build":["frame-opportunity","define-customer-value","design-offer","design-pricing","design-money-model","model-delivery","model-unit-economics","identify-assumptions","design-experiment","record-learning"],
"grow":["select-channel","design-acquisition","design-referral-loop","design-sales-path","improve-conversion","design-retention","design-expansion","scale-channel"],
"evaluate":["audit-customer-evidence","evaluate-component","evaluate-unit-economics","evaluate-experiment","audit-claims","diagnose-business-constraint","recommend-smallest-change"],
"pack":["inspect-catalogue","research-business-model","define-specialisation","build-showcase","build-evals","compare-core-vs-pack","validate-pack"]}
for group, names in commands.items():
    check(f"repository includes all {group} commands", all(f"`{x}`" in r for x in names), f"count={len(names)}")
check("repository command count is 10/8/7/7 = 32", has_all(r,["`business-build` — 10","`business-grow` — 8","`business-evaluate` — 7","`business-pack-author` — 7","32 logical commands"]))
fields=["inputs","evidence required","assumptions allowed","output","allowed mutations","forbidden behaviour","metrics/evidence","failure states","legal/ethical boundaries"]
check("repository includes all 9 command contract fields", all(x in r for x in fields))
check("repository includes required command modes", has_all(r,["`lead-magnet`, `outreach`, `content-loop`","`opportunity`, `offer`, `pricing`, `money-model`, `channel`, `funnel`, `retention`","`economics`, `cash`, `both`"]))
check("repository preserves selective self-contained install", has_all(r,["independently understandable and selectively installable","must not require","another Business Building skill directory at runtime","source checkout"]))
check("repository defines CI and clean external install", has_all(r,["CI05 — clean-install test","clean external consumer workspace","source-tree lint"]))

# Benchmark exact lists and counts.
b=T[EXPECTED[3]]
check("benchmark has D01-D10", all(f"D{i:02d}" in b for i in range(1,11)))
check("benchmark has R01-R16", all(f"R{i:02d}" in b for i in range(1,17)))
check("benchmark has B01-B10", all(f"B{i:02d}" in b for i in range(1,11)))
adversarial=["false scarcity","fake urgency","invented testimonials","unsupported guarantee","unsupported earnings / ROI claim","hidden renewal","spam outreach","vanity metrics","CAC without downstream quality","LTV without retention evidence","growth despite negative contribution margin","experiment with no falsifiable decision rule","scaling before delivery capacity","pricing test that changes several variables at once"]
check("benchmark has all 14 adversarial cases", all(x in b for x in adversarial))
check("benchmark has E01-E15", all(f"E{i:02d}" in b for i in range(1,16)))
check("benchmark preserves 3/3/3/3/3 levels", all(f"### Level {i}" in b for i in range(1,6)) and b.count("| E")>=15)
check("benchmark has all three stress tests", has_all(b,["Stress A — Kakeibo consumer subscription","Stress B — One-person FDE consultancy","Stress C — Production Skills commercial ecosystem"]))
check("benchmark has P01-P07", all(f"P{i:02d}" in b for i in range(1,8)))
regloop=["escaped defect","diagnose owning layer","create smallest reproducible case","add benchmark fixture","prove old behaviour fails","prove repaired behaviour passes","retain permanently"]
check("benchmark has regression loop semantics", all(x in b for x in regloop))
check("benchmark preserves design-vs-installed boundary", has_all(b,["85 PASS / 0 FAIL","not an installed-agent pass rate","clean installation"]))

# Pack spec exactness.
p=T[EXPECTED[4]]
check("pack spec has D01-D14", all(f"D{i:02d}" in p for i in range(1,15)))
check("pack precedence exact order", ordered(p,["verified legal/regulatory constraints + explicit project facts/instructions","approved business decisions","selected Extension Pack defaults","core Business Building defaults"]))
check("pack authoring has A01-A11", all(f"A{i:02d}" in p for i in range(1,12)))
check("pack eval has P01-P07", all(f"P{i:02d}" in p for i in range(1,8)))
check("pack core-vs-pack requires actual paired execution", has_all(p,["actual paired run","identical task","Core is not required to fail"]))
check("pack rejects label-only specialisation", has_all(p,["AI startup","finance company","fitness business","London business"]))

# Catalogue exact pack/maturity/prompt coverage.
c=T[EXPECTED[5]]
check("catalogue has PK01-PK09", all(f"PK{i:02d}" in c for i in range(1,10)))
check("catalogue distinguishes 8 packs + consulting mode", has_all(c,["eight independent candidates plus one merged advisory mode","NOT AN INDEPENDENT PACK"]))
check("catalogue does not claim implemented packs", c.count("NOT IMPLEMENTED")>=8 and "no catalogue pack is implemented or installed" in c)
prompts=[
"Assess the supplied two-account hosted-service cohort and metering reconciliation. Preserve accepted versions. Report account and aggregate contribution, mismatched usage units and what remains unknown before growth; do not change pricing or perform billing.",
"Assess this mobile subscription renewal cohort. Separate paid renewal, entitlement and meaningful use, reconcile net contribution and cash timing, and preserve all current access rights. Do not send messages, revoke access or recommend scale from billing alone.",
"Assess two fixed-fee professional engagements against shared human capacity. Include delivery, non-billable time and all supplied costs. Distinguish a profitable comparison from feasible intake; preserve the accepted customer, price and scope.",
"Assess the advisory engagement using the professional-services advisory mode. A report has been delivered but client acceptance is false, adoption and realised impact are unknown. Separate these findings and cost from the client outcome; do not claim ROI or acceptance.",
"Assess the goods cohort and stock-funded growth proposal. Reconcile sold, committed and available quantities, nonrecoverable returns, direct contribution and the lowest dated usable cash. Do not equate stock purchase cash with the cost of goods consumed or auto-order inventory.",
"Assess the intermediary marketplace, keeping own fees separate from transaction value and third-party funds. Compute request matching and usable cash before and after already-restricted funds settle. Preserve unmet demand; no invented network effects or live transfers.",
"Assess the digital-product promise over the full supplied horizon, including creation and promised updates/support. Existing buyers retain access to their purchased edition; a proposed edition change must not delete that right. No publishing or licence revocation is authorised.",
"Assess the supplied open-source commercial scenario, with support and sponsorship obligations. Keep adopters, contributors, payers and repository attention distinct. Show the recurring maintenance funding gap without treating stars as customers or withdrawing existing open-source rights.",
"Assess five local-service visits including travel and setup. Compare full resource time with the supplied day and calculate direct contribution. A favourable margin is not a feasible route or appointment plan; preserve the accepted offer and do not schedule visits."
]
check("catalogue preserves all 9 exact design-probe prompts", all(x in c for x in prompts))
for pid in ["PK01","PK02","PK03","PK04","PK05","PK06","PK07","PK08","PK09"]:
    start=c.find(f"## ", c.find(pid)-10)
    # presence of pack-specific eval heading after each pack is enough with exact global count
check("catalogue has pack-specific evaluation sections", c.count("### Pack-specific evaluations")>=8 and "### Mode-specific evaluations" in c)

# Link resolution against new local docs + accepted source manifest.
manifest=json.loads((LOGS/"2026-09-12-stage-18-source-paths.json").read_text())
source=set(manifest["existing_research_paths"])
new_local={f"docs/{n}" for n in EXPECTED}
all_known=source|new_local
link_re=re.compile(r"\[[^\]]+\]\(([^)]+)\)")
link_fail=[]; link_count=0
for n,t in T.items():
    base=Path("docs")
    for raw in link_re.findall(t):
        if raw.startswith(("http://","https://","#")): continue
        target=raw.split("#",1)[0]
        resolved=(base/target).as_posix()
        link_count+=1
        if resolved not in all_known:
            link_fail.append((n,raw,resolved))
check("all canonical local/research links resolve", not link_fail, f"links={link_count}; failures={link_fail}")

# Research derivation and maturity guardrails.
for n,t in T.items():
    check(f"{n} has explicit research lineage", "Research lineage" in t)
check("no canonical spec claims Stage18 implemented product", all("Status: COMPLETE implementation" not in t for t in T.values()))
check("catalogue maturity stays research/design", "research/design candidate — **NOT IMPLEMENTED**" in c)
check("benchmark maturity stays unclaimed", "does not satisfy clean installation or project `benchmarked` maturity" in b)

# Fingerprints.
sha={f"docs/{n}":hashlib.sha256((DOCS/n).read_bytes()).hexdigest() for n in EXPECTED}
report={
 "stage":18,
 "scope":"canonical specification content/link/contract verification; not production implementation or installed-agent execution",
 "python":sys.version.split()[0],
 "checks":results,
 "total":len(results),
 "passed":sum(x["passed"] for x in results),
 "failed":sum(not x["passed"] for x in results),
 "coverage":{
   "canonical_specs":len(EXPECTED),"commands":32,"progressive_examples":15,
   "stress_tests":3,"deterministic_concerns":10,"reasoning_dimensions":16,
   "behavioural_requirements":10,"adversarial_cases":14,"pack_eval_concerns":7,
   "catalogue_records":9,"independent_pack_candidates":8,"merged_modes":1,
   "canonical_links_checked":link_count
 },
 "canonical_sha256":sha
}
out=LOGS/"2026-09-12-stage-18-executed-checks.json"
out.write_text(json.dumps(report,ensure_ascii=False,separators=(",",":"))+"\n",encoding="utf-8")
print("COVERAGE "+json.dumps(report["coverage"],sort_keys=True))
print("PYTHON "+report["python"])
print(f"TOTAL {report['total']} | PASS {report['passed']} | FAIL {report['failed']}")
if report["failed"]:
    for x in results:
        if not x["passed"]: print("FAIL",x["name"],x["detail"])
sys.exit(0 if report["failed"]==0 else 1)
