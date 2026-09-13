#!/usr/bin/env python3
"""Stage 19 documentation checks and actual E01 arithmetic; never an agent benchmark."""
from pathlib import Path
from collections import Counter
from decimal import Decimal
from fractions import Fraction
from datetime import datetime, timezone
import hashlib
import json
import platform
import re
import sys
from urllib.parse import unquote, urlsplit

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
PREFIX = '2026-09-13-stage-19-'
inputs = json.loads((HERE/(PREFIX+'verification-inputs.json')).read_text())
draft_path = HERE/(PREFIX+'public-readme.md')
draft = draft_path.read_text()
log_path = HERE/(PREFIX+'readme-design.md')
design_log = log_path.read_text()
spec_path = HERE/'2026-09-08-business-building-skills-new-project-bootstrap-process.md'
spec = spec_path.read_text()
original_stage = spec.split('# 26. Stage 19 — Design Public README\n', 1)[1].split('\n# 27.',1)[0]
checks = []

def check(name, condition, evidence):
    checks.append({'check':name,'result':'PASS' if condition else 'FAIL','evidence':evidence})

def git_blob(data):
    return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()

def sha256(text):
    return hashlib.sha256(text.encode()).hexdigest()

def slug(text):
    return re.sub(r'[^\w\- ]','',text.lower()).replace(' ','-')

def anchors(text):
    seen=Counter(); result=set(); fenced=False
    for line in text.splitlines():
        if re.match(r'^\s*```', line):
            fenced=not fenced
            continue
        if fenced: continue
        match=re.match(r'^#{1,6}\s+(.*?)\s*#*$',line)
        if match:
            base=slug(match[1]); n=seen[base]; seen[base]+=1
            result.add(base+(f'-{n}' if n else ''))
    return result

check('Original bootstrap identity',git_blob(spec_path.read_bytes())==inputs['original_spec_blob'],inputs['original_spec_blob'])
check('Original Stage 19 literal target',all(x in original_stage for x in ['5 × 3 Learn by Building','installation','quick start','licence','without reading the internal bootstrap']), 'Full original §26 read; design cannot replace later installed execution.')
check('Exact H1',draft.splitlines()[0]=='# Business Building Skills',draft.splitlines()[0])
actual_h2=re.findall(r'^## (.+)$',draft,re.M)
check('All requested topics in original order',actual_h2==inputs['required_h2'],{'actual_h2':actual_h2,'count':len(actual_h2),'opening_positioning':True})
check('Positioning tested, with current state immediately visible',draft.startswith('# Business Building Skills\n\nTurn business ideas and existing businesses') and '**Design preview:**' in draft.split('## ',1)[0], 'Opening wording plus design limitations; substantive choice reviewed in log §3.')

corpus=json.loads((HERE/'2026-09-12-stage-17-case-contracts.json').read_text())['primary_cases']
canonical=(ROOT/'docs/04-testing-and-benchmark-spec.md').read_text()
learn=draft.split('## Learn by Building',1)[1].split('\n## Project structure',1)[0]
rows=re.findall(r'^\| \[(E\d{2}) · (.*?)\]\((.*?)\) \| (.*?) \|$',learn,re.M)
check('Exactly fifteen primary example links',[r[0] for r in rows]==[f'E{i:02d}' for i in range(1,16)], [r[0] for r in rows])
distribution=[]
for level in range(1,6):
    block=learn.split(f'### Level {level} — ',1)[1].split('\n### Level ',1)[0]
    distribution.append(len(re.findall(r'^\| \[E\d{2} · ',block,re.M)))
check('Exact level distribution',distribution==[3]*5,distribution)
for c in corpus:
    row=next((r for r in rows if r[0]==c['id']),None)
    expected_anchor=slug(c['id']+' — '+c['title'])
    section=canonical.split('### '+c['id']+' — '+c['title']+'\n',1)[1].split('\n### ',1)[0]
    prompt=re.search(r'#### Exact copyable prompt\n\n```text\n(.*?)\n```',section,re.S)[1]
    check(c['id']+' exact prompt and preserved case',sha256(prompt)==c['prompt_sha256'] and prompt==c['exact_prompt'],{'prompt_sha256':sha256(prompt),'source_blob':c['source_blob']})
    check(c['id']+' correct title and direct canonical link',row is not None and row[1]==c['title'] and row[2]=='../04-testing-and-benchmark-spec.md#'+expected_anchor and expected_anchor in anchors(canonical),{'link':row[2] if row else None,'level':c['level']})
quick=draft.split('## Quick start\n',1)[1].split('\n## Learn by Building',1)[0]
prompt=re.search(r'```text\n(.*?)\n```',quick,re.S)[1]
check('Self-contained quick-start prompt byte fidelity',prompt==corpus[0]['exact_prompt'],{'sha256':sha256(prompt),'expected':corpus[0]['prompt_sha256']})
facts_text=prompt.split('Facts (JSON):\n',1)[1].split('\n\nTask:',1)[0]
facts=json.loads(facts_text)
check('Quick-start inputs are synthetic and protected',facts['synthetic'] is True and facts['accepted_versions']=={'customer':'small-agency-v1','offer':'one-report-v1'},facts['accepted_versions'])

obs=facts['observations']; scenarios=facts['scenarios']; D=Decimal
calculation=[]
for hours in obs['past_job_hours']:
    h=D(hours); cost=h*D(obs['labour_value_per_hour'])+D(obs['other_direct_cost_per_job'])
    fixed=D(scenarios['fixed_fee']); hourly=h*D(scenarios['hourly_price'])
    calculation.append({'hours':hours,'valued_labour':str(h*D(obs['labour_value_per_hour'])),'other_direct_cost':obs['other_direct_cost_per_job'],'fixed_consideration':str(fixed),'fixed_contribution':str(fixed-cost),'hourly_consideration':str(hourly),'hourly_contribution':str(hourly-cost)})
    expected_row=f'| {hours} hours | £{fixed} | '+(f'-£{abs(fixed-cost)}' if fixed-cost<0 else f'£{fixed-cost}')+f' | £{hourly} | £{hourly-cost} |'
    check('Quick-start displayed arithmetic at '+hours+' hours',expected_row in quick,calculation[-1])
boundary=(Fraction(scenarios['fixed_fee'])-Fraction(obs['other_direct_cost_per_job']))/Fraction(obs['labour_value_per_hour'])
check('Fixed-fee boundary exact arithmetic',boundary==Fraction(11,3) and '`11/3` hours' in quick,{'hours_fraction':str(boundary),'formula':'(fixed_fee-other_direct_cost)/labour_value_per_hour'})

core=draft.split('## Core skills\n',1)[1].split('\n## Extension Packs',1)[0]
skills=re.findall(r'^\| `(business-[^`]+)` \|',core,re.M)
check('Four independent skills',skills==['business-build','business-grow','business-evaluate','business-pack-author'],skills)
contracts=(ROOT/'docs/03-business-building-skills-repository-and-contracts-spec.md').read_text()
selectors=re.findall(r'^### [BGEP]\d{2} — `([^`]+)`',contracts,re.M)
check('Named command count matches canonical contracts',len(selectors)==32 and 'all 32 selectors' in core,{'canonical_count':len(selectors)})
named=[]
for line in core.splitlines():
    if re.match(r'^\| `business-',line):
        named.extend(re.findall(r'`([^`]+)`',line)[1:])
check('Every advertised example selector exists',all(s in selectors for s in named),named)
packs=draft.split('## Extension Packs\n',1)[1].split('\n## Execution tools',1)[0]
pack_names=re.findall(r'^\| `([^`]+)` \|',packs,re.M)
expected_packs=['saas-business','consumer-mobile-subscription','professional-services','ecommerce-business','marketplace-business','creator-digital-product','open-source-commercialisation','local-service-business']
check('Eight independent pack candidates and advisory mode',pack_names==expected_packs and 'advisory mode' in packs and 'not a ninth installation' in packs,pack_names)
check('Pack implementation status explicit','all **not implemented**' in packs and not (ROOT/'extension-packs').exists(),'Catalogue designs are not installable packs.')
stress=draft.split('## Canonical stress tests\n',1)[1].split('\n## Source-book lineage',1)[0]
check('Three canonical stress structures',len(re.findall(r'^\| \[',stress,re.M))==3 and all(x in stress for x in ['Kakeibo','FDE consultancy','Production Skills commercial ecosystem']), 'Exactly three direct links to the accepted stress designs.')
books=draft.split('## Source-book lineage\n',1)[1].split('\n## Documentation',1)[0]
book_rows=re.findall(r'^\| (?:Alex Hormozi|Josh Kaufman|Eric Ries), .*$',books,re.M)
check('Five attributed book sources',len(book_rows)==5,book_rows)
docs=draft.split('## Documentation\n',1)[1].split('\n## Boundary',1)[0]
check('Six canonical documentation links',len(re.findall(r'^\| \[0[1-6] · ',docs,re.M))==6,'01–06; exact local target paths checked below.')
check('No missing installer or licence advertised',not (ROOT/'skills').exists() and not (ROOT/'LICENSE').exists() and 'There is no installable release' in draft and 'No project licence has been selected' in draft,'Current tree agrees; actual host installation and licence authorisation belong to their later owning work.')
check('Production root README preserved',git_blob((ROOT/'README.md').read_bytes())==next(f['sha'] for f in inputs['baseline']['files'] if f['path']=='README.md'),'Original §28 production scaffold is not begun.')

link_count=0
for source in [draft_path,log_path]:
    text=source.read_text()
    check('Balanced Markdown fences '+source.name,len(re.findall(r'^\s*```',text,re.M))%2==0,'Fence pairing; content meaning reviewed separately.')
    for label,target in re.findall(r'(?<!!)\[([^\]]+)\]\(([^)]+)\)',text):
        url=urlsplit(target)
        if url.scheme or url.netloc:
            check('External link is an inspected GitHub source '+label,url.scheme=='https' and url.netloc=='github.com' and url.path.startswith('/sb-dev/business-building-skills/'),'No external product compatibility assertion is made.')
            continue
        resolved=(source.parent/unquote(url.path)).resolve() if url.path else source
        link_count+=1
        check('Local link '+source.name+' / '+label,resolved.is_relative_to(ROOT) and resolved.is_file(),target)
        if url.fragment and resolved.is_file():
            check('Local anchor '+label,unquote(url.fragment) in anchors(resolved.read_text()),target)
check('README does not require an internal bootstrap link',all('research-logs/' not in target and 'bootstrap' not in target for _,target in re.findall(r'(?<!!)\[([^\]]+)\]\(([^)]+)\)',draft)),'README links directly to canonical documentation; quick start has no external input dependency.')

snapshot=HERE/'2026-09-13-bootstrap-3-progress-through-stage-18.md'
for f in inputs['baseline']['files']:
    p=snapshot if f['path']=='docs/research-logs/bootstrap-3-progress.md' else ROOT/f['path']
    check('Preserve '+f['path'],p.is_file() and git_blob(p.read_bytes())==f['sha'],{'expected_blob':f['sha'],'verified_at':str(p.relative_to(ROOT))})
allowed={str((HERE/(PREFIX+n)).relative_to(ROOT)) for n in ['public-readme.md','readme-design.md','verification-inputs.json','verifier.py','executed-checks.json']}
allowed.add(str(snapshot.relative_to(ROOT)))
inherited={f['path'] for f in inputs['baseline']['files']}
actual={str(p.relative_to(ROOT)) for p in ROOT.rglob('*') if p.is_file()}
check('Only current-stage additions',actual-inherited<=allowed and allowed-{'docs/research-logs/'+PREFIX+'executed-checks.json'}<=actual,{'additions':sorted(actual-inherited),'allowed':sorted(allowed)})
check('Research-log conformance has no unresolved failure',not re.search(r'\| (?:FAIL|BLOCKED) \|\s*$',design_log,re.M),'Direct substantive review and outcome limits are recorded in the research log, not inferred from keywords.')

result_counts=Counter(c['result'] for c in checks)
result={
    'stage':19,'kind':'Executed documentation integrity checks and deterministic synthetic E01 arithmetic',
    'executed_at':datetime.now(timezone.utc).isoformat(),'python':platform.python_version(),
    'baseline_head':inputs['baseline']['head'],'results':dict(result_counts),'exit_code':int(result_counts['FAIL']>0),
    'local_links_checked':link_count,'primary_distribution':distribution,
    'calculation':{'source':'E01 exact prompt copied in the public README design','method':'Python decimal.Decimal and fractions.Fraction','currency':'GBP','rows':calculation,'fixed_zero_contribution_hours':str(boundary),'limits':'Synthetic consideration and contribution after valued labour/direct costs; not a cash forecast, net profit or willingness-to-pay evidence.'},
    'publication_inputs':{str(p.relative_to(ROOT)):{'blob':git_blob(p.read_bytes()),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in [draft_path,log_path,HERE/(PREFIX+'verification-inputs.json'),Path(__file__),snapshot,HERE/'bootstrap-3-progress.md']},
    'checks':checks,
    'limits':['No installed Agent Skills execution','No independent reader study','No live customer experiment','No measured core/pack performance','No clean external installation','Remote commit checks are recorded separately after publication']
}
(HERE/(PREFIX+'executed-checks.json')).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'results':dict(result_counts),'exit_code':result['exit_code'],'links':link_count,'calculation':result['calculation'],'failures':[c for c in checks if c['result']=='FAIL']},ensure_ascii=False))
sys.exit(result['exit_code'])
