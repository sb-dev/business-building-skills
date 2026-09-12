#!/usr/bin/env python3
"""Verify Stage 17 design contracts and calculate its fixed numeric witnesses.

No installed agent is invoked or semantically graded by this script. The
authored-control calibration is a separately attributed manual review record.
"""
from pathlib import Path
from decimal import Decimal, InvalidOperation
import hashlib,json,platform,re,sys

LOG=Path(__file__).resolve().parent
ROOT=LOG.parent.parent
PREFIX='2026-09-12-stage-17'
OUT=LOG/(PREFIX+'-executed-checks.json')
checks=[]

def check(name,condition,evidence):
    checks.append({'check':name,'result':'PASS' if condition else 'FAIL','evidence':evidence})

def blob(p):
    b=p.read_bytes()
    return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()

def D(x):
    if isinstance(x,bool) or not isinstance(x,(str,int,Decimal)): raise ValueError('Invalid numeric type')
    try: d=Decimal(x)
    except InvalidOperation as exc: raise ValueError('Invalid decimal') from exc
    if not d.is_finite(): raise ValueError('Non-finite number')
    return d

def eq(name,actual,expected):
    check(name,D(actual)==D(expected),{'actual':str(actual),'expected':str(expected)})

def section(text,name):
    return text.split('## '+name+'\n',1)[1].split('\n## ',1)[0]

def main():
    OUT.write_text(json.dumps({'state':'RUNNING','stage':17})+'\n')
    corpus=json.loads((LOG/(PREFIX+'-case-contracts.json')).read_text())
    original=LOG/'2026-09-08-business-building-skills-new-project-bootstrap-process.md'
    check('Original specification identity',blob(original)=='a0ac1b6c78a0cde8ccd9aca6fda6c5b0880c516d',blob(original))
    spec=original.read_text().split('# 24. Stage 17 — Design Evals, Benchmarks and Regression Fixtures\n',1)[1].split('# 25. Stage 18',1)[0]
    rubric=(LOG/(PREFIX+'-rubrics-and-regression.md')).read_text()
    advdoc=(LOG/(PREFIX+'-adversarial-fixtures.md')).read_text()
    design=(LOG/(PREFIX+'-benchmark-design.md')).read_text()
    calibration=(LOG/(PREFIX+'-calibration.md')).read_text()
    lists=[('deterministic','Deterministic validation',10),('reasoning','Business reasoning evaluation',16),('behaviour','Behavioural evaluation',10),('adversaries','Adversarial evaluation',14),('pack_dimensions','Extension Pack evaluation',7),('regression','Regression loop',7)]
    for key,heading,count in lists:
        block=re.search(r'```text\n(.*?)\n```',section(spec,heading),re.S).group(1)
        expected=[line.removeprefix('→ ').strip() for line in block.splitlines()]
        actual=[r['requirement'] for r in corpus[key]]
        check(key+' complete original literal list',actual==expected and len(actual)==count,{'required':expected,'actual':actual})
        check(key+' unique IDs',len({r['id'] for r in corpus[key]})==count,[r['id'] for r in corpus[key]])
        if key!='adversaries':
            for row in corpus[key]:
                check(row['id']+' complete method/anchors/witnesses',all(isinstance(row[k],str) and len(row[k])>20 and row[k] in rubric for k in ['method','positive','negative']) and bool(row['witnesses']),row['requirement'])
    check('Complete inherited manifest',len(corpus['inherited_files'])==93 and len({f['path'] for f in corpus['inherited_files']})==93,93)
    for f in corpus['inherited_files']:
        p=ROOT/f['path']
        if f['path']=='docs/research-logs/bootstrap-3-progress.md': p=LOG/'2026-09-12-bootstrap-3-progress-through-stage-16.md'
        actual=blob(p) if p.is_file() else None
        check('Preserved '+f['path'],actual==f['sha'],{'actual':actual,'expected':f['sha'],'preserved_at':str(p.relative_to(ROOT))})
    known={r['id'] for r in corpus['reasoning']}
    primary_ids=[]; distribution=[0]*5
    for case in corpus['primary_cases']:
        primary_ids.append(case['id']); distribution[case['level']-1]+=1
        src=(ROOT/case['source_path']).read_text()
        body=re.search(r'## '+case['id']+r' — [^\n]+\n(.*?)(?=\n## |\Z)',src,re.S).group(1)
        prompt=re.search(r'### Exact copyable prompt\n\n```text\n(.*?)\n```',body,re.S).group(1)
        check(case['id']+' exact accepted prompt',case['exact_prompt']==prompt and hashlib.sha256(prompt.encode()).hexdigest()==case['prompt_sha256'],case['prompt_sha256'])
        check(case['id']+' source identity',blob(ROOT/case['source_path'])==case['source_blob'],case['source_blob'])
        for field,heading in [('expected_artifacts','Expected artefacts'),('reference_findings','Discriminating acceptance'),('negative_control','Negative control'),('preservation','Preservation and smallest responsible repair')]:
            expected=re.search(r'### '+heading+r'\n\n(.*?)(?=\n### |\Z)',body,re.S).group(1).strip()
            check(case['id']+' complete '+field,case[field]==expected,heading)
        check(case['id']+' scoped reasoning contract',bool(case['reasoning_dimensions']) and set(case['reasoning_dimensions'])<=known and len(case['applicability_rule'])>50,case['reasoning_dimensions'])
    check('Exact complete primary set',primary_ids==[f'E{i:02}' for i in range(1,16)],primary_ids)
    check('Exact primary distribution',distribution==[3,3,3,3,3],distribution)
    st=json.loads((LOG/'2026-09-12-stage-16-cases.json').read_text())
    for c,prior in zip(corpus['stress_cases'],st['cases']):
        check(c['id']+' inherited stress identity',c['id']==prior['id'] and c['version']==prior['version'] and c['base_prompt_sha256']==prior['base_prompt_sha256'] and c['source_path']==prior['output_path'],c['version'])
        check(c['id']+' complete inherited stress coverage',c['exercise_requirements']==[r['requirement'] for r in prior['coverage']] and c['adversarial_ids']==[v['id'] for v in prior['variants']],c['adversarial_ids'])
    check('All three stress structures',len(corpus['stress_cases'])==3,[c['id'] for c in corpus['stress_cases']])
    packtext=(LOG/'2026-09-10-stage-14-design-probes.md').read_text()
    inputs=json.loads(re.search(r'<!-- FIXTURES BEGIN -->\s*```json\n(.*?)\n```',packtext,re.S).group(1))
    catalogue=(LOG/'2026-09-10-stage-14-candidate-catalogue.md').read_text()
    pids=[p['id'] for p in corpus['pack_profiles']]
    check('All retained pack candidates and advisory mode',pids==[f'PK{i:02}' for i in range(1,10)],pids)
    for p in corpus['pack_profiles']:
        original=next(x for x in inputs if x['id']==p['probe'])
        check(p['id']+' exact accepted probe',p['exact_source_fixture']==original,p['probe'])
        check(p['id']+' retained effect identities',p['effects']==[p['id']+f'-E{i}' for i in range(1,4)] and all(e in catalogue for e in p['effects']),p['effects'])
        check(p['id']+' full seven-part evaluation contract',p['required_evaluation_dimensions']==[f'P{i:02}' for i in range(1,8)] and p['metric'] in rubric and p['nonfit'] in rubric,p['required_evaluation_dimensions'])
        check(p['id']+' honest implementation state',p['implementation_state']=='NOT IMPLEMENTED; inherited design candidate',p['implementation_state'])
    check('Advisory mode remains inside professional-services',next(p for p in corpus['pack_profiles'] if p['id']=='PK04')['name']=='professional-services:advisory-mode','PK04 is not a ninth independent pack')
    fields=['identity','subject_input','execution_condition','authority','expected_artifacts','deterministic_oracle','reasoning_oracle','behaviour_oracle','adversarial_controls','business_result','run_evidence','assessment','repair_and_regression','claim_scope']
    check('Complete case and evidence record contract',list(corpus['case_contract'])==fields and all(len(v)>70 for v in corpus['case_contract'].values()),fields)
    pairs=re.findall(r'^\| (AD\d{2}) \| (R\d{2}) [^|]+ \| (FAIL) \| (PASS) \| (.+) \|$',calibration,re.M)
    for a in corpus['adversaries']:
        check(a['id']+' fixed synthetic prompt and facts',a['synthetic'] is True and bool(a['fixture']) and a['exact_prompt'] in advdoc and a['question'] in a['exact_prompt'] and json.dumps(a['fixture'],indent=2,ensure_ascii=False) in a['exact_prompt'],a['requirement'])
        check(a['id']+' concrete separate controls',a['failing_candidate'] in advdoc and a['adequate_candidate'] in advdoc and a['failing_candidate']!=a['adequate_candidate'] and a['failing_candidate'] not in a['exact_prompt'] and a['adequate_candidate'] not in a['exact_prompt'],a['dimensions'])
        check(a['id']+' findings and bounded repair',len(a['required_findings'])>=2 and all(f in advdoc for f in a['required_findings']) and a['smallest_repair'] in advdoc and bool(a['inherited_witnesses']),a['required_findings'])
        got=[p[1] for p in pairs if p[0]==a['id']]
        check(a['id']+' separate attributed calibration dimensions',got==a['dimensions'] and set(got)<=known,got)
    check('All 36 attributed dimension comparisons',len(pairs)==36,len(pairs))
    check('No calibration substituted for installed performance','not an installed-agent run' in calibration and 'not a model success rate' in calibration and 'actual outputs' in rubric,'Explicit evidence boundaries inspected')
    cases={a['id']:a['fixture'] for a in corpus['adversaries']}
    eq('AD04 honoured proportion',D(cases['AD04']['honoured'])/D(cases['AD04']['eligible_requests']),'0.2')
    eq('AD04 eligible dispositions reconcile',cases['AD04']['honoured']+cases['AD04']['refused_despite_eligibility'],cases['AD04']['eligible_requests'])
    eq('AD07 unknown-eligibility remainder',cases['AD07']['contacts']-cases['AD07']['known_opt_outs'],'42')
    eq('AD08 actual support revenue',D(cases['AD08']['paid_support_subscribers'])*D(cases['AD08']['monthly_support_price']),'0')
    for label,expected in [('A',('1','100','-80')),('B',('10','20','50'))]:
        c=cases['AD09']['channel_'+label]
        for metric,actual,want in [('CPL',D(c['acquisition_cost'])/D(c['leads']),expected[0]),('CAC',D(c['acquisition_cost'])/D(c['paid_customers']),expected[1]),('residual',D(c['paid_customers'])*D(c['contribution_per_customer'])-D(c['acquisition_cost']),expected[2])]:eq('AD09 '+label+' '+metric,actual,want)
    eq('AD10 observed finite contribution',D(cases['AD10']['monthly_contribution'])*D(cases['AD10']['observed_months']),'10')
    eq('AD10 unvalidated twelve-month scenario',D(cases['AD10']['monthly_contribution'])*12,'120')
    unit=D(cases['AD11']['price'])-D(cases['AD11']['direct_service_cost'])
    eq('AD11 marginal contribution',unit,'-10');eq('AD11 total marginal contribution',unit*D(cases['AD11']['proposed_new_units']),'-1000')
    eq('AD11 gross sales',D(cases['AD11']['price'])*D(cases['AD11']['proposed_new_units']),'5000')
    add=D(cases['AD13']['proposed_additional_calls'])*D(cases['AD13']['hours_per_call'])
    eq('AD13 added hours',add,'18');eq('AD13 all-in hours',D(cases['AD13']['existing_all_in_workload_hours'])+add,'132')
    eq('AD14 descriptive percentage-point difference',(D(cases['AD14']['observed_conversion_after'])-D(cases['AD14']['observed_conversion_before']))*100,'5')
    for bad in [True,1.2,'NaN','Infinity','']:
        try:D(bad);rejected=False
        except ValueError:rejected=True
        check('Calculator rejects '+repr(bad),rejected,repr(bad))
    documents=[LOG/(PREFIX+suffix) for suffix in ['-benchmark-design.md','-rubrics-and-regression.md','-adversarial-fixtures.md','-calibration.md']]+[LOG/'bootstrap-3-progress.md',LOG/'2026-09-12-bootstrap-3-progress-through-stage-16.md']
    missing=[]
    for p in documents:
        for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)',p.read_text()):
            if re.match(r'^[a-z]+:',target) or target.startswith('#'):continue
            linked=(p.parent/target.split('#',1)[0]).resolve()
            if not linked.is_file():missing.append(str(linked))
    check('All new documentation targets resolve',not missing,missing)
    check('No premature production directories',all(not (ROOT/p).exists() for p in ['skills','examples','benchmarks','tests','tools','extension-packs','integrations','.github']),'Research workspace only')
    hashed=[LOG/(PREFIX+'-case-contracts.json'),Path(__file__)]+documents
    result={'stage':17,'scope':'Design structure, identity, exact coverage and arithmetic; calibration is separately attributed direct review, not installed-agent performance','python':platform.python_version(),'starting_head':corpus['starting_head'],'inputs_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in hashed},'summary':{'PASS':sum(x['result']=='PASS' for x in checks),'FAIL':sum(x['result']=='FAIL' for x in checks)},'checks':checks}
    OUT.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps({'stage':17,**result['summary'],'python':result['python'],'output':str(OUT)}))
    return 1 if result['summary']['FAIL'] else 0

if __name__=='__main__':
    try:sys.exit(main())
    except Exception as exc:
        OUT.write_text(json.dumps({'stage':17,'state':'ERROR','error':type(exc).__name__+': '+str(exc),'checks':checks},indent=2)+'\n')
        raise
