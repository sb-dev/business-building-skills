#!/usr/bin/env python3
"""Verify Stage 20 review integrity and accessed-source identities, not integration behaviour."""
from pathlib import Path
from collections import Counter
from datetime import datetime, timezone
from urllib.parse import urlsplit, unquote
import argparse
import hashlib
import json
import platform
import re
import sys

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent.parent
P='2026-09-13-stage-20-'
ap=argparse.ArgumentParser(description=__doc__)
ap.add_argument('--source-root',type=Path,required=True,help='Cache of the 21 pinned source files at <repository>/<path>; fetch from review-inputs.json URLs.')
args=ap.parse_args()
inputs_path=HERE/(P+'review-inputs.json')
x=json.loads(inputs_path.read_text())
review_path=HERE/(P+'cross-project-review.md')
review=review_path.read_text()
out=HERE/(P+'executed-checks.json')
checks=[]
def check(name,ok,evidence): checks.append({'check':name,'result':'PASS' if ok else 'FAIL','evidence':evidence})
def blob(data): return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
def slug(t): return re.sub(r'[^\w\- ]','',t.lower()).replace(' ','-')
def anchors(text):
 seen=Counter(); found=set(); fenced=False
 for line in text.splitlines():
  if re.match(r'^\s*```',line):fenced=not fenced;continue
  if fenced:continue
  m=re.match(r'^#{1,6}\s+(.*?)\s*#*$',line)
  if m:
   s=slug(m[1]);n=seen[s];seen[s]+=1;found.add(s+(f'-{n}' if n else ''))
 return found

spec=HERE/'2026-09-08-business-building-skills-new-project-bootstrap-process.md'
original=spec.read_text().split('# 27. Stage 20 — Cross-Project Review\n',1)[1].split('\n# 28.',1)[0]
required=['Deep Research Skills','Legal Skills','UI/UX Design Skills','Software Engineering Skills','Production Skills family','Pactwright']
check('Original comparison subjects',all(n in original for n in required),required)
check('Six exact comparison subjects',{c['project'] for c in x['comparisons']}==set(required) and len(x['comparisons'])==6,[c['project'] for c in x['comparisons']])
check('Four suggested concept families',len(x['abstraction_candidates'])==4 and [a['id'] for a in x['abstraction_candidates']]==['A01','A02','A03','A04'],[a['name'] for a in x['abstraction_candidates']])
check('Six bounded reviews and opportunities',len(x['handoff_reviews'])==6 and all(f'I{i:02d} —' in review for i in range(1,7)),[h['id'] for h in x['handoff_reviews']])
check('Twenty-one accessed sources',len(x['sources'])==21 and len({s['id'] for s in x['sources']})==21,len(x['sources']))
source_ids={s['id'] for s in x['sources']}
source_urls={s['url'] for s in x['sources']}
check('Sources cover all six named repositories',{s['repo'] for s in x['sources']}=={c['repo'] for c in x['comparisons']},sorted({s['repo'] for s in x['sources']}))
for s in x['sources']:
 p=args.source_root/s['repo']/s['path']
 check('Accessed source '+s['id'],p.is_file() and blob(p.read_bytes())==s['sha'] and hashlib.sha256(p.read_bytes()).hexdigest()==s['sha256'],{'repository':s['repo'],'head':s['head'],'path':s['path'],'blob':s['sha'],'read_scope':s['read_scope']})
 check('Pinned source URL '+s['id'],s['url']==f"https://github.com/sb-dev/{s['repo']}/blob/{s['head']}/{s['path']}" and re.fullmatch('[0-9a-f]{40}',s['head']) is not None,s['url'])
for c in x['comparisons']:
 check('Complete comparison '+c['id'],all(c.get(k) for k in ['project','repo','sources','business_owns','other_owns','handoff','return','limit','decision']) and set(c['sources'])<=source_ids and f"### {c['id']} — {c['project']}" in review,c['project'])
for a in x['abstraction_candidates']:
 check('Complete candidate '+a['id'],all(a.get(k) for k in ['name','sources','common_need','variations','decision','production_evidence']) and set(a['sources'])<=source_ids and f"### {a['id']} — {a['name']}" in review,a['decision'])
for h in x['handoff_reviews']:
 check('Recorded bounded review '+h['id'],all(h.get(k) for k in ['comparison','kind','input','adequate_return','reject','preserved','result']) and h['result']=='PASS' and f"#### {h['id']} — {h['comparison']}" in review,h['kind'])

reg=json.loads((args.source_root/'production-skills/registry/projects/business-building-skills.json').read_text())
check('Actual registry state retained',reg['status']=='proposed' and reg['pactwright']=='planned',reg)
parser=(args.source_root/'pactwright/src/pack/manifest.ts').read_text()
check('Format difference grounded in actual parser','PACK_MANIFEST_FILE = "pack.yml"' in parser and '`${skill}.md`' in parser and '`PACK.md`' in review,'Direct source inspection; no parser invocation or compatibility pass claimed.')
schema=(args.source_root/'pactwright/src/graph/schema.ts').read_text()
check('Actual Pactwright core node ownership','["intent", "decision", "contract", "brief", "evidence"]' in schema,'Node schema inspected; no business node types added.')
check('No production implementation in Stage 20',all(not (ROOT/p).exists() for p in ['skills','examples','benchmarks','tests','tools','extension-packs','integrations','.github']),'Current stage adds only review/evidence/progress files.')
snapshot=HERE/'2026-09-13-bootstrap-3-progress-through-stage-19.md'
for f in x['baseline']['files']:
 p=snapshot if f['path']=='docs/research-logs/bootstrap-3-progress.md' else ROOT/f['path']
 check('Preserve '+f['path'],p.is_file() and blob(p.read_bytes())==f['sha'],{'expected_blob':f['sha'],'path':str(p.relative_to(ROOT))})
case_data=json.loads((HERE/'2026-09-12-stage-17-case-contracts.json').read_text())
check('Accepted example distribution preserved',Counter(c['level'] for c in case_data['primary_cases'])==Counter({1:3,2:3,3:3,4:3,5:3}),'15 accepted examples; original corpus preserved by byte identity.')
check('All six canonical owners retained',len(list((ROOT/'docs').glob('0[1-6]-*.md')))==6,'All six full canonical identities also checked against predecessor.')
allowed={str((HERE/(P+n)).relative_to(ROOT)) for n in ['cross-project-review.md','review-inputs.json','verifier.py','executed-checks.json']}
allowed.add(str(snapshot.relative_to(ROOT)))
inherited={f['path'] for f in x['baseline']['files']}
actual={str(p.relative_to(ROOT)) for p in ROOT.rglob('*') if p.is_file()}
check('Only stage-scoped additions',actual-inherited<=allowed and allowed-{str(out.relative_to(ROOT))}<=actual,sorted(actual-inherited))
check('Balanced review Markdown fences',len(re.findall(r'^\s*```',review,re.M))%2==0,'Pairing only; meaning reviewed directly.')
deferred=[];links=0
for label,target in re.findall(r'(?<!!)\[([^\]]+)\]\(([^)]+)\)',review):
 u=urlsplit(target);links+=1
 if u.scheme:
  check('Inspected external link '+label,target in source_urls,target)
 else:
  p=(review_path.parent/unquote(u.path)).resolve() if u.path else review_path
  if p==out: deferred.append((label,target));continue
  check('Local link '+label,p.is_relative_to(ROOT) and p.is_file(),target)
  if u.fragment and p.is_file():check('Local anchor '+label,unquote(u.fragment) in anchors(p.read_text()),target)
check('No unresolved mandatory conformance row',not re.search(r'\| (FAIL|BLOCKED) \|\s*$',review,re.M),'Recorded substantive conformance; no automated semantic-quality claim.')

result={'stage':20,'kind':'Executed source/documentation integrity verification','executed_at':datetime.now(timezone.utc).isoformat(),'python':platform.python_version(),'baseline_head':x['baseline']['head'],'source_count':21,'comparison_count':6,'abstraction_count':4,'handoff_review_count':6,'links_checked':links,'checks':checks,'publication_inputs':{str(p.relative_to(ROOT)):{'blob':blob(p.read_bytes()),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in [review_path,inputs_path,Path(__file__),snapshot,HERE/'bootstrap-3-progress.md']},'limits':['Source inspection and authored semantic review, not installed cross-project behaviour','No external law/provider/market claims reverified','No live business evidence, registry promotion or shared implementation']}
def emit():
 counts=Counter(c['result'] for c in checks);result['results']={'PASS':counts['PASS'],'FAIL':counts['FAIL']};result['exit_code']=int(bool(counts['FAIL']))
 out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
emit()
for label,target in deferred:check('Emitted result link '+label,out.is_file() and json.loads(out.read_text())['stage']==20,target)
emit()
print(json.dumps({k:result[k] for k in ['results','exit_code','source_count','comparison_count','abstraction_count','links_checked']}))
if result['exit_code']:print(json.dumps([c for c in checks if c['result']=='FAIL']))
sys.exit(result['exit_code'])
