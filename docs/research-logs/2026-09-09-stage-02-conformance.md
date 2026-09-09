# Stage 2: Acceptance and conformance

**Date:** 9 September 2026  
**Stage:** 2, Extract and Reconcile the Five-Book Capability Corpus  
**Branch:** `feat/bootstrap-2`  
**Completion:** Remote completion is recorded separately in [bootstrap progress](bootstrap-2-progress.md). This record does not preclaim a future commit.

## 1. Acceptance checklist extracted before substantive source analysis

Authority: [original bootstrap specification v1.1](2026-09-08-business-building-skills-new-project-bootstrap-process.md), especially §9, constrained by §§1–5, 7–8 and 34–36. The entire original specification was reread from `main`. Its blob remained `a0ac1b6c78a0cde8ccd9aca6fda6c5b0880c516d`. The [execution contract](2026-09-09-bootstrap-2-execution-contract.md) adds stage isolation, direct verification, commit and remote-read requirements.

| Checklist field | Stage 2 requirement | Specification reference |
|---|---|---|
| stage purpose | Turn the five books into a capability evidence base, not a book-shaped architecture. | §9 purpose and exit; §3 |
| required inputs | All five identified books, the original process, execution contract and accepted Stage 1 domain/boundary outputs. | §§1, 8–9; execution §3 |
| prerequisites | Five accessible sources; verified Stage 1 completion; correct branch and baseline; usable commit/verification tools. | §9; execution §§2–3, 7 |
| questions to resolve | What the sources actually say; what overlaps, conflicts or lacks validation; what belongs in the domain. | §9; §§3–5 |
| required research | Examine the five source texts and relevant figures, retaining locators and limitations. | §9 per-book capture; §34 source integrity |
| required activities | Extract every per-book field; construct the capability matrix; compare overlap and tension; synthesise the taxonomy. | §9 |
| required comparisons | Explicitly analyse the four named tensions and additional material conflicts found in the corpus. | §9 tension list |
| required candidate discovery | Discover capability candidates from the source ideas, testing the provisional map rather than assuming it is final. | §§3–4, 9 |
| required analysis | Separate source assertions, assumptions, illustrative examples, metrics and the project's interpretations. | §§3, 5, 9 |
| required decisions | Record retain/merge/adapt/reject/research dispositions with reasons; do not choose aggression by default. | §9 matrix and conflict instruction |
| required deliverables | Five-book extraction, source-to-capability matrix, overlap matrix, conflict log and provisional capability taxonomy. | §9 |
| required contents of each deliverable | Eleven fields per book; meaningful matrix inputs, outputs, risks, evidence and statuses; traced comparisons and taxonomy. | §9 lists and candidate fields |
| exact counts | Five books × eleven prescribed capture fields = 55 field instances. Verify all four named tension pairs. | §9 enumerations |
| exact distribution requirements | Every book must have all eleven fields. No fixed quota of capability rows per book is prescribed. | §9 |
| exact naming requirements | Keep the five source titles identifiable; preserve repository/branch names. No Stage 2 filenames are prescribed. | §§1, 7, 9; execution §2 |
| exact structural requirements | Durable research logs; capability-shaped synthesis; no premature production scaffold. | §§3, 7, 9, 28 |
| required prompts | None for Stage 2. Exact primary-example prompts belong to Stage 15. | §§9, 22 |
| required examples | Capture source examples as abstract patterns only, not copied stories, scripts or proprietary examples. | §§3, 9 |
| required tests | Source/field/reference/count/link checks and substantive review against the original section. | execution §5; §9 exit |
| required execution | Actually access sources, analyse them, persist complete outputs, run checks, commit this stage and verify remotely. | §9; execution §§4–7 |
| required measurements | Count field coverage and outputs; verify any arithmetic used in the analysis. No live commercial experiment is prescribed. | §§5, 9; execution §5 |
| required verification | Reread original §9; inspect actual output, source support, consistency, scope and remote file identities. | execution §§5–7 |
| research-log output | Preserve source access/limits, extraction, matrices, conflicts, decisions, taxonomy, unresolved claims and conformance. | §9 output; execution §6 |
| exit criteria | Source books are evidence for independently expressed capabilities; all current requirements pass and commit is remotely verified. | §9 exit; execution §§1, 7 |
| things explicitly deferred to later stages | Broader empirical/professional research: Stage 3; detailed domain models: 4–9; tool choice: 10–11; skills/packs/examples/evals: 12–17; canonical specs: 18; implementation/install: 21–24. These assignments do not defer Stage 2 extraction. | §§10–31 |

## 2. Prerequisite verification

The remote branch was read at `b7905ae3657813001f487106ff8f5d8d6a538067`. Its seven-file tree matches the Stage 1 receipt: original specification, two READMEs, execution contract, Stage 1 charter, conformance and progress. The charter and its conformance were reread at that commit. The receipt identifies content commit `1e17881096fbfa5ad470805a6ad8c2fa12da77b3` and reports the accepted Stage 1 exit. No Stage 2 output existed there. Neither `feat/bootstrap` nor its artefacts were consulted.

The uploaded execution contract has SHA-256 `3927a0190242a7e8b2add790e9030a55ddaf61fadf139dae2ee58a22fb9a0d85`, matching the retained contract. All five uploaded PDFs open without encryption; their page counts and hashes are recorded in the corpus log. A GitHub `create_blob` call with the already-existing README content returned its unchanged blob `c2311bac2170cec37102ade6da92c1b2c7a803cd`, establishing usable write access without changing a branch or creating a test commit. Commit creation and ref verification are assessed again at publication, not inferred from that probe.

The earlier missing-source and write-tool blockers are resolved for resuming this stage. No new external business action, spending, release, merge or maturity promotion is authorised by this research.

## 3. Direct conformance review against original §9

After drafting the outputs, original Stage 2 was fetched again from `main`, lines 550–620, covering its complete section and the start of Stage 3. The source blob remained `a0ac1b6c78a0cde8ccd9aca6fda6c5b0880c516d`. The eleven field labels, ten suggested matrix fields, four named tensions, required outputs and exit were checked against that original, not a replacement summary.

Semantic review was performed by the assistant. It is not an independent business, legal or statistical audit. Presence checks below supplement, rather than establish, the substantive assessments.

| Requirement | Specification reference | Deliverable / evidence | Verification performed | Result |
|---|---|---|---|---|
| All five source books accessed | §§1, 9 | Corpus §1 source register and reading scope | Opened all five PDFs; checked edition pages, native text, file hashes and relevant sections | PASS |
| Offers: all eleven fields | §9 per-book list | Corpus §2; O01–O11 | Reviewed market, offer, delivery, pricing, proof, guarantees, metrics, caveats, overlaps and validation questions with page locators | PASS |
| Leads: all eleven fields | §9 per-book list | Corpus §3; L01–L12 | Reviewed definitions, magnets, channels, paid/delegated costs, referrals, effort, downstream quality and conflicting cautions | PASS |
| Money Models: all eleven fields | §9 per-book list | Corpus §4; M01–M16 | Reviewed offer families, cash, scope, credit/refunds, continuity, staged construction and transparency/tactic tensions | PASS |
| Personal MBA: all eleven fields | §9 per-book list | Corpus §5; P01–P16 | Reviewed business/people/systems breadth, customer evidence, pricing, finance, sufficiency and measurement limitations | PASS |
| Lean Startup: all eleven fields | §9 per-book list | Corpus §6; R01–R14 | Reviewed uncertainty, hypotheses, tests, metrics, pivots, growth, batches, repair, sandbox and methodological limits | PASS |
| Complete source-to-capability matrix | §9 matrix | Matrix, 69 entries | Every entry has all ten specified dimensions plus a unique ID; source statements and project implications are distinguished | PASS |
| Discovery tests the seed hypothesis | §§3–4, 9 | Matrix and taxonomy §2 | Consolidated source concepts by responsibility; mapped all 21 original seed clusters without imposing a skill count | PASS |
| Overlap matrix | §9 output | Reconciliation §3 | Verified 22 capability rows by five sources, matching candidate IDs, and all ten source-pair comparisons | PASS |
| Four named tensions | §9 comparison list | T01–T04 | Read both source positions and their caveats; checked explicit conditional resolution and independent-validation needs | PASS |
| Material additional conflicts | §9 capture/analysis | T05–T18 | Preserved price, LTV, cash, remedy, truthfulness, permission, workload, test and repair disagreements rather than silently harmonising them | PASS |
| Do not prefer aggression automatically | §9 final instruction; §5 | Conflict log, dispositions and rejected alternatives | Growth obligation, concealed material terms and implied acceptance rejected; commercially useful options retain evidence and capacity conditions | PASS |
| Provisional capability taxonomy | §9 output/exit | C01–C22 | Every responsibility has an artefact, evaluation implication, source support and bounded case seed; none is selected as an installed skill | PASS |
| Capability-shaped source transformation | §3 | Matrix, taxonomy and seed mapping | Source labels remain provenance; duplicate responsibilities merge across books; no five-book skill architecture exists | PASS |
| Abstract patterns, not copied examples | §§3, 9 | Five abstract-pattern fields | Reviewed for independent expression; no original stories, scripts, proprietary bundles, PDFs or source images are published | PASS |
| Figures and arithmetic checked | §§5, 9; execution §5 | V01–V07 | Visually inspected six rendered pages; recalculated identified equations and durations with deterministic arithmetic | PASS |
| Source support versus external truth | §5; §34 source integrity | Corpus method; definitions; U01–U18 | Author reports, project analysis and outside-validation questions are separate; no customer evidence or efficacy result invented | PASS |
| Preserve Stage 1 and global boundaries | §§2, 5, 8, 35 | All outputs; taxonomy C22; conflict resolutions | Retained owner authority, specialist/execution boundaries, independent use, non-goals and separate quality dimensions | PASS |
| Durable research record | §9 output; execution §6 | Four new dated logs and progress update | Sources, limits, analyses, dispositions, outputs, checks, unresolved external claims and Stage 3 handoff recorded | PASS |
| Exact required coverage | §9 enumerations | Executed checks below | Five by eleven fields; four original comparisons; complete fields in every matrix row | PASS |
| Stage 2 exit | §9 exit | Corpus, matrix and reconciliation together | Books function as traceable candidate evidence for domain responsibilities, not the architecture itself | PASS |
| Current-stage isolation | §§7, 9; execution §§4, 7 | Five-path staging manifest | Only four Stage 2 research logs and the existing progress record change; no later-stage implementation is included | PASS |
| Current external research | §10 assigns Stage 3 | U01–U18 are research questions | Stage 2 requires extraction and unresolved-validation claims, not execution of Stage 3's independent research | NOT APPLICABLE |
| Fifteen primary examples and exact prompts now | §22 assigns Stage 15 | No primary examples claimed | Stage 2 captures source examples only as abstract patterns; taxonomy case seeds are not implemented examples | NOT APPLICABLE |
| Six canonical specifications now | §25 assigns Stage 18 | No canonical files created | Stage 2's five output categories are research artefacts, not six later specification files | NOT APPLICABLE |
| Product benchmarks, installation or maturity now | §§24, 29–34 | No product execution claimed | This is source-extraction acceptance, not implemented skill, pack comparison, clean installation or maturity evidence | NOT APPLICABLE |

## 4. Actual verification results and limitations

The first local checker run stopped with an `IndexError`: its register selector also matched the separate source-coverage table. The selector was restricted to the Source register section. No content acceptance criterion was removed. The complete run then passed. The original-seed check was strengthened to compare all 21 labels in order, and the binary/path check was renamed so that it did not pretend a filename inspection could prove absence of copied text. The final complete run passed again.

Executed command:

```text
python /mnt/data/stage02-private/verify_stage02.py /mnt/data/stage02-output /mnt/data
```

The checker below is retained to avoid depending on a session-local script. Extract its Python code block and run it against an output directory containing the five staged paths and a separate directory containing the five supplied PDFs. A future full repository checkout should copy these five paths into an isolated verification directory before running the staging allowlist check. The five original PDF inputs remain private and are not bundled with this repository.

**Actual final result: 31 checks, 31 PASS, 0 FAIL; process exit 0.** The discovered source arithmetic errors are accurately represented as errors; a pass is not a claim that the books' original arithmetic or commercial claims passed validation.

| Checked output | Required or discovered basis | Actual result |
|---|---|---|
| Book/field distribution | Required: five books, eleven fields each | 11 / 11 / 11 / 11 / 11; 55 populated fields |
| Candidate rows | No fixed row quota in §9; all candidate fields populated | 69 unique entries: O 11, L 12, M 16, P 16, R 14 |
| Taxonomy and source overlap | Actual consolidated responsibilities, not a prescribed skill count | 22 definitions; all supported; 22 × 5 source matrix consistent |
| Pairwise comparisons | All unique pairs of five supplied sources | 10 pairs |
| Seed coverage | All original §4 clusters | 21 ordered labels mapped |
| Tensions | Four named comparisons plus material discoveries | All four explicit; 18 records total |
| Validation questions | Claims requiring broader validation per book | 18 consolidated questions plus five book-specific fields |
| Numerical checks | Narrow source arithmetic, not business efficacy | O multiplication/cash distinction; L funnel; M term/credit; P allowance recomputed |
| Source locators and document links | Actual source-page bounds and target-tree files | No out-of-bounds source locator or unresolved relative document link |
| Staged paths | Four new logs plus one existing progress file | Exactly five allowed Markdown paths; no production directories or binary assets |

An additional exact-sequence scan compared the three substantive reports with all five extracted source texts. It found **zero matching 14-word sequences** after lowercasing and tokenisation. This is only a copying-risk aid, not a legal clearance or proof of independent expression. The semantic review separately checked that original stories, scripts and proprietary examples were not reproduced. Source titles, short terminology and bibliographic locators are deliberately preserved.

The Stage 1 progress record was reconstructed locally from the fetched content and its Git blob was checked as `22c0ad6b45e903d529624e0ae30fa0fdc1e4c51a` before editing. Its Stage 1 completion receipt is retained unchanged. Remote preservation of the other six baseline files, the actual new tree and the stage commit is checked after staging; those results belong in the completion receipt, not a claim made before publication.

## 5. Reproducible content checker

```python
"""Stage 2 structural/arithmetic audit; not a substitute for source review.
Usage: python verify_stage02.py OUTPUT_ROOT PDF_DIRECTORY
OUTPUT_ROOT contains docs/research-logs. PDFs are private inputs, never outputs.
"""
from pathlib import Path
from decimal import Decimal
import sys, re, hashlib, itertools
import fitz

root = Path(sys.argv[1]).resolve()
pdfs = Path(sys.argv[2]).resolve()
logs = root / 'docs/research-logs'
names = {
 'corpus': '2026-09-09-stage-02-five-book-capability-corpus.md',
 'matrix': '2026-09-09-stage-02-source-to-capability-matrix.md',
 'recon': '2026-09-09-stage-02-reconciliation-and-taxonomy.md',
 'audit': '2026-09-09-stage-02-conformance.md',
 'progress': 'bootstrap-2-progress.md',
}
base_names = {
 'README.md', '2026-09-08-business-building-skills-new-project-bootstrap-process.md',
 '2026-09-09-bootstrap-2-execution-contract.md',
 '2026-09-09-stage-01-domain-and-professional-boundary.md',
 '2026-09-09-stage-01-conformance.md',
}
texts = {k: (logs / n).read_text() for k,n in names.items()}
results = []
def check(name, value, detail):
    results.append((name, bool(value), str(detail)))

def table_rows(text, pattern):
    answer=[]
    for line in text.splitlines():
        if not line.startswith('|'): continue
        cells=[s.strip() for s in line.strip().strip('|').split('|')]
        if re.fullmatch(pattern, cells[0]): answer.append(cells)
    return answer

fields = ['business problem addressed','core concepts','workflow implications',
 'decision heuristics','metrics','assumptions','examples as abstract patterns only',
 'failure modes','areas of overlap','areas of tension','claims requiring broader validation']
sections = re.split(r'^## [2-6]\. [OLMPR]: .*$', texts['corpus'], flags=re.M)[1:]
if sections: sections[-1]=sections[-1].split('\n## 7.')[0]
check('Five source dossiers',len(sections)==5,len(sections))
check('Eleven prescribed fields in every dossier',all(re.findall(r'^### (.+)$',s,re.M)==fields for s in sections),[len(re.findall(r'^### ',s,re.M)) for s in sections])
check('55 nonempty field bodies',sum(len(re.findall(r'^### ',s,re.M)) for s in sections)==55 and all(len(part.split())>=20 for s in sections for part in re.split(r'^### .+$',s,flags=re.M)[1:]),55)
register=table_rows(texts['corpus'].split('### Source register')[1].split('### Coverage and material inspected')[0],r'[OLMPR]')
check('Exact source register IDs',[r[0] for r in register]==list('OLMPR'),[r[0] for r in register])
source_ok=[]
page_counts={}
for r in register:
    key=r[0]; path=pdfs/r[2].strip('`'); expected=int(r[3]); digest=r[4].strip('`')
    with fitz.open(path) as doc:
        valid=not doc.is_encrypted and len(doc)==expected
        page_counts[key]=len(doc)
    source_ok.append(valid and hashlib.sha256(path.read_bytes()).hexdigest()==digest)
check('Five PDF identities, page counts and readability',len(source_ok)==5 and all(source_ok),page_counts)
rows=table_rows(texts['matrix'],r'[OLMPR]\d{2}')
ids=[r[0] for r in rows]
check('Unique candidate IDs',len(ids)==len(set(ids)) and len(ids)>0,len(ids))
check('All ten matrix fields plus ID',all(len(r)==11 and all(r) for r in rows),len(rows))
check('All five sources represented',set(i[0] for i in ids)==set('OLMPR'),{b:sum(i.startswith(b) for i in ids) for b in 'OLMPR'})
check('Allowed candidate dispositions',all(r[-1] in {'retain','merge','adapt','reject','research'} for r in rows),sorted(set(r[-1] for r in rows)))
check('Each candidate has source locators',all(re.search(r'[OLMPR]:\d+',r[1]) for r in rows),len(rows))
caps=table_rows(texts['recon'],r'C\d{2}')
tax=[r for r in caps if len(r)==6 and not re.fullmatch(r'(?:[OLMPR]\d{2}(?:, )?)*|—',r[1])]
overlap=[r for r in caps if r not in tax]
expected_caps=[f'C{i:02}' for i in range(1,23)]
check('22 unique capability definitions',[r[0] for r in tax]==expected_caps,len(tax))
check('Taxonomy responsibility, artefact, check and case seed',all(len(r)==6 and all(r) for r in tax),len(tax))
check('Candidate capability references resolve',all(r[3] in expected_caps for r in rows),len(rows))
check('Every capability has primary source support',set(r[3] for r in rows)==set(expected_caps),len(set(r[3] for r in rows)))
check('22 by five-source overlap matrix',[r[0] for r in overlap]==expected_caps and all(len(r)==6 for r in overlap),len(overlap))
check('Overlap cells match source candidates',all(r[1:]==[', '.join(x[0] for x in rows if x[0][0]==b and x[3]==r[0]) or '—' for b in 'OLMPR'] for r in overlap),len(overlap))
pairs=table_rows(texts['recon'],r'[OLMPR] \+ [OLMPR]')
check('All ten source pairs compared',set(r[0] for r in pairs)=={' + '.join(p) for p in itertools.combinations('OLMPR',2)},len(pairs))
seed_section=texts['recon'].split('### Disposition of the original §4 capability hypothesis')[1].split('\nC09 makes')[0]
seeds=[l for l in seed_section.splitlines() if l.startswith('| ')][1:]
original_seeds=['opportunity framing','customer / problem understanding','value proposition','offer construction','pricing','monetisation','lead generation','channel strategy','sales path','conversion','delivery','retention','expansion','referral','unit economics','cash / capacity','assumption mapping','experiment design','learning','constraint diagnosis','business-system evaluation']
check('All 21 original seed clusters mapped',[line.split('|')[1].strip() for line in seeds]==original_seeds,len(seeds))
tensions=table_rows(texts['recon'],r'T\d{2}')
check('18 substantive tension records',len(tensions)==18 and len({r[0] for r in tensions})==18 and all(len(r)==4 and all(r) for r in tensions),len(tensions))
required=['aggressive value/offer optimisation vs experiment-before-commitment','lead volume vs lead quality / capacity','revenue expansion vs retention / customer value / cash risk','broad business heuristics vs context-specific evidence']
check('All four original tension pairs',all(term in tensions[i][1] for i,term in enumerate(required)),4)
queue=table_rows(texts['recon'],r'U\d{2}')
check('18 explicit broader-validation questions',len(queue)==18 and all(len(r)==4 and all(r) for r in queue),len(queue))
bad=[]
for text in texts.values():
    for match in re.finditer(r'\b([OLMPR]):(\d+(?:[–-]\d+)?(?:,\d+(?:[–-]\d+)?)*)',text):
        book, numbers=match.groups()
        for part in numbers.split(','):
            bounds=[int(x) for x in re.split('[–-]',part)]
            if not all(1<=x<=page_counts[book] for x in bounds) or bounds!=sorted(bounds): bad.append(match.group())
check('Source locators within actual PDF bounds',not bad,bad)
D=Decimal
check('O47 explanatory multiplication',D('2.5')*D('2.5')*4==25,'25; source explanatory value 22.4 is inconsistent')
check('O47 displayed cash ratio and rounding',D(112000)/5000==D('22.4') and 28*3997==111916,'22.4 ratio; 111916 exact receipts')
check('L182 lead and hourly arithmetic',100*D('.20')*D('.25')==5 and D(5)/4==D('1.25'),'5 leads; 1.25/hour; source states 4 and 1')
check('M158 term and M159 credit divisor',3+12==15 and 600/12==50,'15 total months; separate credit 50/month')
check('P211-213 acquisition allowance',D(2000)-500-1000-D('.15')*2000==200,'200')
links=[]
for key,text in texts.items():
    # Only Markdown file links, not examples inside this checker.
    for target in re.findall(r'\]\(([^)]+\.md)(?:#[^)]*)?\)',text):
        if '://' not in target and not (logs/target).exists() and target not in base_names: links.append((key,target))
check('Relative document links resolve in target tree',not links,links)
actual={str(p.relative_to(root)) for p in root.rglob('*') if p.is_file()}
allowed={'docs/research-logs/'+n for n in names.values()}
check('Current-stage staging file allowlist',actual==allowed,sorted(actual))
check('No binary assets or production paths staged',all(p.endswith('.md') and p.startswith('docs/research-logs/') for p in actual),len(actual))
check('No unresolved placeholders in deliverables',all('<!-- OVERLAP_TABLE -->' not in texts[k] and 'TODO' not in texts[k] for k in ['corpus','matrix','recon']),3)
for name,ok,detail in results:
    print(f'{"PASS" if ok else "FAIL"} | {name} | {detail}')
print(f'TOTAL {len(results)}; PASS {sum(ok for _,ok,_ in results)}; FAIL {sum(not ok for _,ok,_ in results)}')
if not all(ok for _,ok,_ in results): raise SystemExit(1)
```

## 6. Commit boundary and exit assessment

The content satisfies original Stage 2: all five source dossiers are complete across the eleven fields; the candidate matrix, overlap matrix, conflict log and provisional taxonomy exist; distinctions and tensions are explicit; source evidence has not been represented as independent validation. No required user decision remains. Source arithmetic defects and unresolved empirical claims are findings, not hidden omissions.

Before creating the stage commit, inspect the staged remote tree and compare its new blobs with the reviewed local payloads. Preserve every earlier file except the accurately updated progress record. Then create the Stage 2-only commit, update only `feat/bootstrap-2` without force, and read back the ref, commit and complete intended tree. Record the resulting immutable content commit in a separate receipt update. Until those operations succeed, this document does not declare Stage 2 COMPLETE.

No Stage 3 research, production scaffold, installed skill, release, registry change, PR or merge is part of this commit. The broader-validation queue and accepted source corpus are inputs for a fresh, standalone Stage 3 task, not a substitute for it.
