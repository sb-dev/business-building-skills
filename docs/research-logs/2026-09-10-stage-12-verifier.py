#!/usr/bin/env python3
"""Stage 12 traceability checks only; no vendor calls or installed-agent assessment."""
import copy
import json
import re
import sys
from pathlib import Path
root = Path(sys.argv[1]); logs = root / 'docs/research-logs'
gap = (logs/'2026-09-10-stage-12-gap-analysis.md').read_text()
guard = (logs/'2026-09-10-stage-12-guardrails.md').read_text()
conf = (logs/'2026-09-10-stage-12-conformance.md').read_text()
required = ['book-to-capability synthesis','customer evidence discipline','offer/economics consistency','pricing reasoning','lead-quality evaluation','channel/business-model fit','retention-aware acquisition','delivery-capacity checks','cash-aware growth','assumption/observation separation','experiment quality','constraint diagnosis','smallest-change behaviour','truthfulness / consumer safeguards','cross-domain business handoffs']
deferred = ['universal business ontology','universal CRM','custom ad platform','custom payment system','custom analytics platform','custom accounting engine','universal growth graph','autonomous outbound-spam engine','persistent cross-project customer database','one universal business score','universal experiment platform','universal pricing optimiser','multi-agent virtual executive team']
results=[]
def check(name, condition):
 ok=bool(condition); results.append((name,ok)); print(('PASS' if ok else 'FAIL')+' | '+name)
def table(text,prefix):
 return [[c.strip() for c in line.strip().strip('|').split('|')] for line in text.splitlines() if re.match(r'^\| '+prefix+r'\d{2} \|',line)]
gs=table(gap,'G'); ns=table(gap,'NC'); rs=table(gap,'RU'); ds=table(guard,'D')
check('all fifteen original gap areas in order', [r[1].split(';')[0] for r in gs[:15]]==required)
check('additional pack concern explicitly justified', len(gs)==16 and gs[-1][0]=='G16' and 'additional, explicitly justified' in gap and '§§20–21,30' in gap)
check('only specified coverage states used', all(r[2] in {'covered','partially covered','missing'} for r in gs))
check('no quota forces invented missing capability', 'No row is classified **missing**' in gap)
check('every classification has evidence and residual', all(len(r)==5 and len(r[3].split())>=16 and len(r[4].split())>=18 for r in gs))
check('all thirteen exclusions in original order', [r[1] for r in ds]==deferred)
check('each exclusion has reason and smaller alternative', all(len(r)==4 and len(r[2].split())>=12 and len(r[3].split())>=14 for r in ds))
check('spam and universal-score rejection not future permission', 'Reject the spam objective' in guard and 'Reject as the quality/approval mechanism' in guard)
check('eight bounded native responsibilities', [r[0] for r in ns]==[f'NC{i:02d}' for i in range(1,9)])
check('seven reused responsibility groups', [r[0] for r in rs]==[f'RU{i:02d}' for i in range(1,8)])
G={r[0]:r for r in gs}
check('every native gap resolves to a residual', all(re.findall(r'G\d{2}',r[2]) and all(i in G and G[i][2] in {'partially covered','missing'} for i in re.findall(r'G\d{2}',r[2])) for r in ns))
check('every residual has a native owner', all(set(re.findall(r'NC\d{2}',r[4])) and set(re.findall(r'NC\d{2}',r[4])) <= {n[0] for n in ns} for r in gs if r[2]!='covered'))
check('covered corpus does not justify a new native extractor', all('G01' not in r[2] for r in ns))
check('native output and non-ownership are explicit', all(len(r)==5 and len(r[3].split())>=15 and len(r[4].split())>=8 for r in ns))
check('reused groups name scope and connection', all(len(r)==3 and 'NC' in r[2] and len(r[2].split())>=25 for r in rs))
cs=set()
for row in gs[1:15]: cs.update(re.findall(r'C\d{2}',row[1]))
check('functional gaps trace every C01-C22 capability', cs=={f'C{i:02d}' for i in range(1,23)})
tc=set(re.findall(r'TC\d{2}',gap+guard))
check('named candidate references within assessed TC01-TC26', tc <= {f'TC{i:02d}' for i in range(1,27)})
check('coverage distinguished from installed maturity', 'Research-model coverage and installed-product coverage are separate' in gap)
check('reuse can retire native work', 'shrink or remove the native responsibility' in gap)
check('skill count is not predetermined by shortlist', 'not eight skills' in gap and 'Stage 13 must compare coherent groupings' in gap) # semantic review checks the actual grouping boundary.
check('all eleven recorded comparison cases exist', len(table(guard,'P'))+len(table(guard,'S'))==11)
check('synthetic and source comparisons separated', '**synthetic**' in guard and 'not an installed-agent or client benchmark' in guard)
known={'2026-09-08-business-building-skills-new-project-bootstrap-process.md','2026-09-09-bootstrap-2-execution-contract.md','2026-09-09-stage-02-reconciliation-and-taxonomy.md','2026-09-10-stage-10-capability-landscape.md','2026-09-10-stage-10-execution-system-candidates.md','2026-09-10-stage-10-reuse-decisions-and-boundaries.md','2026-09-10-stage-11-execution-layer.md'}
links=re.findall(r'\]\(([^)]+)\)',gap+guard+conf)
check('document targets resolve to actual local or read baseline files',all((logs/x.split('#')[0]).is_file() or x.split('#')[0] in known for x in links if not x.startswith(('https://','#'))))
pre=conf.split('## 2.')[0]
check('all twenty-five pre-work checklist fields retained',len([x for x in pre.splitlines() if x.startswith('| ')])-1==25)

# Explicit synthetic admission packets, not a classifier of raw natural-language proposals.
# Here evidence and meaningful-difference booleans are stipulated outcomes of human review.
def admissible(proposal):
 ids=proposal.get('gaps',[])
 return (bool(ids) and len(ids)==len(set(ids)) and all(i in G and G[i][2] in {'partially covered','missing'} for i in ids) and proposal.get('evidence_reviewed') is True and proposal.get('meaningful_residual') is True and proposal.get('reuses_execution') is True and bool(proposal.get('excluded_ownership')))
p={'gaps':['G03','G04'],'evidence_reviewed':True,'meaningful_residual':True,'reuses_execution':True,'excluded_ownership':['billing','arithmetic']}
check('A01: bounded evidence-reviewed native packet admitted',admissible(p))
for name,change in [('unmapped gap',{'gaps':['G99']}),('covered-only gap',{'gaps':['G01']}),('duplicate gap',{'gaps':['G03','G03']}),('missing evidence',{'evidence_reviewed':False}),('no meaningful residual',{'meaningful_residual':False}),('owns replacement execution',{'reuses_execution':False}),('missing ownership boundary',{'excluded_ownership':[]})]:
 q=copy.deepcopy(p);q.update(change);check('A02: reject '+name,not admissible(q))
check('A03: no gap silently defaults to approval',not admissible({}))
check('A04: string true is not verified evidence',not admissible({**p,'evidence_reviewed':'true'}))
print('COVERAGE '+json.dumps({'required_gap_areas':15,'additional_areas':len(gs)-15,'native_responsibilities':len(ns),'reused_groups':len(rs),'deferred_or_rejected_ideas':len(ds),'coverage_states':{s:sum(r[2]==s for r in gs) for s in ['covered','partially covered','missing']}},sort_keys=True))
print(f'TOTAL {len(results)} | PASS {sum(ok for _,ok in results)} | FAIL {sum(not ok for _,ok in results)}')
sys.exit(0 if all(ok for _,ok in results) else 1)
