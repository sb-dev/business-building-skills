#!/usr/bin/env python3
"""Stage 13 document and original synthetic contract checks. No network or live effects.

The explicit action/result packets are stipulated design cases, not a deployed
security system, natural-language router, inference engine or installed skill.
"""
from __future__ import annotations
import copy
import hashlib
import json
import re
import sys
from decimal import Decimal, localcontext
from pathlib import Path

ROOT=Path(sys.argv[1])
LOG=ROOT/'docs/research-logs'
PREFIX='2026-09-10-stage-13-'
architecture=(LOG/(PREFIX+'skill-architecture.md')).read_text()
selection=(LOG/(PREFIX+'selection-and-checks.md')).read_text()
conformance=(LOG/(PREFIX+'conformance.md')).read_text()
FIELDS=['inputs','evidence required','assumptions allowed','output','allowed mutations','forbidden behaviour','metrics/evidence','failure states','legal/ethical boundaries']
FILES={'business-build':'build-command-contracts','business-grow':'grow-command-contracts','business-evaluate':'evaluate-command-contracts','business-pack-author':'pack-command-contracts'}
EXPECTED={
'business-build':['frame-opportunity','define-customer-value','design-offer','design-pricing','design-money-model','model-delivery','model-unit-economics','identify-assumptions','design-experiment','record-learning'],
'business-grow':['select-channel','design-acquisition','design-referral-loop','design-sales-path','improve-conversion','design-retention','design-expansion','scale-channel'],
'business-evaluate':['audit-customer-evidence','evaluate-component','evaluate-unit-economics','evaluate-experiment','audit-claims','diagnose-business-constraint','recommend-smallest-change'],
'business-pack-author':['inspect-catalogue','research-business-model','define-specialisation','build-showcase','build-evals','compare-core-vs-pack','validate-pack']}
SEEDS={
'business-build':['frame-opportunity','define-customer','define-problem','map-value','design-offer','design-pricing','design-money-model','model-unit-economics','model-delivery','identify-assumptions','design-experiment'],
'business-grow':['define-demand','select-channel','design-lead-magnet','design-outreach','design-content-loop','design-referral-loop','design-sales-path','improve-conversion','design-retention','design-expansion','scale-channel'],
'business-evaluate':['audit-customer-evidence','evaluate-opportunity','evaluate-offer','evaluate-pricing','evaluate-money-model','evaluate-channel','evaluate-funnel','evaluate-unit-economics','evaluate-cash-risk','evaluate-retention','evaluate-experiment','audit-claims','diagnose-business-constraint','recommend-smallest-change'],
'business-pack-author':['inspect-catalogue','research-business-model','define-specialisation','define-core-effects','build-showcase','build-evals','compare-core-vs-pack','validate-pack']}
results=[]
def check(name: str, value: object)->None:
    ok=bool(value); results.append((name,ok)); print(('PASS' if ok else 'FAIL')+' | '+name)

def rows(text: str)->list[list[str]]:
    return [[c.strip() for c in s.strip().strip('|').split('|')] for s in text.splitlines() if s.startswith('| ')]

def contracts(text: str,skill: str)->list[dict]:
    out=[]
    for found in re.finditer(r'^### ([BGEP]\d{2}) — `([^`]+)`\n(.*?)(?=^### |^## |\Z)',text,re.M|re.S):
        id,name,body=found.groups()
        entries=[r for r in rows(body) if r[0] in FIELDS]
        nc=re.search(r'\*\*Native responsibilities:\*\* ([^\n]+)',body)
        seed=re.search(r'\*\*Original §20 seeds:\*\* ([^\n]+)',body)
        modes=[r for r in rows(body) if r[0].startswith('`')]
        out.append({'id':id,'name':name,'skill':skill,'entries':entries,'fields':dict(entries),'nc':re.findall(r'NC\d{2}',nc.group(1) if nc else ''),'seeds':re.findall(r'`([^`]+)`',seed.group(1) if seed else ''),'modes':{r[0].strip('`'):r[1] for r in modes},'body':body})
    return out
all_commands=[]; documents={}
for skill,suffix in FILES.items():
    text=(LOG/(PREFIX+suffix+'.md')).read_text(); documents[skill]=text
    commands=contracts(text,skill); all_commands.extend(commands)
    check(skill+': exact selected commands in order',[c['name'] for c in commands]==EXPECTED[skill])
    check(skill+': nine fields on every command',all([r[0] for r in c['entries']]==FIELDS for c in commands))
    # A completeness alarm; the substantive review in conformance assesses meaning.
    check(skill+': every field has substantive task-specific content',all(len(v.split())>=12 for c in commands for v in c['fields'].values()))
    check(skill+': source seeds accounted for without duplicates',sorted(s for c in commands for s in c['seeds'])==sorted(SEEDS[skill]))
    check(skill+': all command responsibilities map to accepted NC rows',all(c['nc'] and set(c['nc']) <= {f'NC{i:02d}' for i in range(1,9)} for c in commands))
C={c['id']:c for c in all_commands}
check('32 commands and 288 complete fields',len(C)==len(all_commands)==32 and sum(len(c['entries']) for c in all_commands)==288)
check('all eight native responsibilities covered',{n for c in all_commands for n in c['nc']}=={f'NC{i:02d}' for i in range(1,9)})
check('only record-learning adds a command beyond original seeds',[c['name'] for c in all_commands if not c['seeds']]==['record-learning'])
seedrows=[r for r in rows(selection) if r[0].strip('`') in SEEDS]
check('selection table contains all 44 original seeds once',len(seedrows)==44 and {(r[0].strip('`'),r[1].strip('`')) for r in seedrows}=={(skill,s) for skill,ss in SEEDS.items() for s in ss})
check('each seed disposition points to the actual owning command',all(any(c['skill']==r[0].strip('`') and r[1].strip('`') in c['seeds'] and r[2]==c['id']+' `'+c['name']+'`' for c in all_commands) for r in seedrows))
check('13 consolidations plus learning reconcile',sum(len(c['seeds'])-1 for c in all_commands if c['seeds'])==13 and 44-13+1==len(all_commands))
check('three explicit acquisition modes',set(C['G02']['modes'])=={'lead-magnet','outreach','content-loop'})
check('seven explicit component evaluation modes',set(C['E02']['modes'])=={'opportunity','offer','pricing','money-model','channel','funnel','retention'})
check('economics and cash scopes remain distinct',set(C['E03']['modes'])=={'economics','cash','both'} and 'separate' in C['E03']['modes']['both'])
check('mode requirements are substantive',all(len(v.split())>=20 for key in ['G02','E02','E03'] for v in C[key]['modes'].values()))
check('eight architecture candidates compared',[r[0] for r in rows(architecture) if re.fullmatch(r'A\d{2}',r[0])]==[f'A{i:02d}' for i in range(1,9)])
check('model and experiment alternatives explicitly resolved','### Separate model and experiment installation value' in architecture and 'business-model' in architecture and 'business-experiment' in architecture and 'current selected four-skill architecture is definite' in architecture)
metadata=dict(re.findall(r'^(business-(?:build|grow|evaluate|pack-author)): ([^\n]+)$',architecture,re.M))
check('four proposed descriptions satisfy declared format bounds',set(metadata)==set(FILES) and all(re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',k) and len(k)<=64 and 1<=len(v)<=1024 for k,v in metadata.items()))
check('standalone guards and on-demand references explicit','No skill requires another sibling' in architecture and 'required local instructions' in architecture and '32 canonical command contracts' in architecture)
check('logical selectors are not invented host executables','not a separate executable' in architecture and 'no shell command is claimed to exist now' in architecture)
check('all evaluation commands prohibit source mutation',all(any(x in c['fields']['allowed mutations'] for x in ['Do not edit','Never rewrite','Do not overwrite','Do not change','Do not publish','Do not alter','Do not apply']) for c in all_commands if c['skill']=='business-evaluate'))
check('pack actual comparison cannot be replaced by expectations','Actual paired outputs' in C['P06']['fields']['evidence required'] and 'actual required comparison' in C['P07']['fields']['inputs'])
check('catalogue mutation is conditional and excludes publication','Only after all applicable criteria pass' in C['P07']['fields']['allowed mutations'] and 'no external registry promotion' in C['P07']['fields']['allowed mutations'])
check('32 contracts remain a design, not installed implementation','does not create production SKILL.md files' in architecture and all('no installed command' in d for d in documents.values()))
check('three actual research source records with limits',all('### R0'+str(i) in architecture for i in range(1,4)) and 'No validator, host or installation was executed' in architecture)
check('ten independent-use prompts retained',[r[0] for r in rows(selection) if re.fullmatch(r'U\d{2}',r[0])]==[f'U{i:02d}' for i in range(1,11)])
check('ten loop steps and ten negative scope probes retained',[r[0] for r in rows(selection) if re.fullmatch(r'T\d{2}',r[0])]==[f'T{i:02d}' for i in range(1,11)] and [r[0] for r in rows(selection) if re.fullmatch(r'N\d{2}',r[0])]==[f'N{i:02d}' for i in range(1,11)])
check('copyable loop prompt and synthetic limits explicit','### Exact copyable design probe' in selection and '**Every business fact' in selection and 'No real customer was interviewed' in selection)

KNOWN={'2026-09-08-business-building-skills-new-project-bootstrap-process.md','2026-09-09-bootstrap-2-execution-contract.md','2026-09-10-stage-12-gap-analysis.md','2026-09-10-stage-12-guardrails.md','2026-09-10-stage-11-execution-layer.md'}
texts=[architecture,selection,conformance,*documents.values()]
links=[x.split('#')[0] for t in texts for x in re.findall(r'\]\(([^)]+)\)',t) if not x.startswith(('https://','#'))]
check('all document target paths resolve to local or read baseline files',all((LOG/x).is_file() or x in KNOWN for x in links))
pre=conformance.split('## 2.')[0]
check('25 pre-work checklist rows retained',len(rows(pre))-1==25)

fixture=json.loads(re.search(r'```json\n(.*?)\n```',selection,re.S).group(1))
check('loop fixture is explicitly synthetic',fixture['synthetic'] is True)
baseline=copy.deepcopy(fixture['accepted'])
fingerprint=lambda x:hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
initial_identity=fingerprint(baseline)
with localcontext() as ctx:
    ctx.prec=28
    D=Decimal
    hours=[D(h) for h in fixture['pilot_hours']]
    price=D(fixture['price']); rate=D(fixture['labour_per_hour']); other=D(fixture['other_direct_cost'])
    costs=[h*rate+other for h in hours]
    total_hours=sum(hours); total_cost=sum(costs); receipts=len(hours)*price
    contribution=receipts-total_cost
    pilot_trough=D(fixture['pilot_opening_cash'])-total_cost
    pilot_close=pilot_trough+receipts
    work_prediction=all(h<=D(fixture['pilot_hour_prediction']) for h in hours) and all(fixture['pilot_quality'])
    guards=total_hours<=D(fixture['pilot_hour_guardrail']) and total_cost<=D(fixture['pilot_cost_guardrail'])
    def tranche(volume,hours_each):
        v=D(volume); h=D(hours_each)
        work=v*h; cost=v*(h*rate+other); acquisition=D(fixture['next_acquisition_outflow'])
        low=pilot_close-cost-acquisition
        return {'hours':work,'direct_cost':cost,'cash_trough':low,'closing_cash':low+v*price,'capacity_headroom':D(fixture['next_capacity_hours'])-work,'contribution':v*price-cost}
    six_mean=tranche(fixture['proposed_volume'],fixture['mean_hour_scenario'])
    six_high=tranche(fixture['proposed_volume'],fixture['high_hour_scenario'])
    four_high=tranche(fixture['smaller_volume'],fixture['high_hour_scenario'])
check('L01: pilot arithmetic independently reconciles',total_hours==9 and costs==[80,115,150] and total_cost==345 and receipts==600 and contribution==255)
check('L02: work prediction challenged while guardrails hold',not work_prediction and guards and all(fixture['pilot_quality']))
check('L03: pilot cash minimum and closing are distinct',pilot_trough==155 and pilot_close==755)
check('L04: six-unit mean scenario fails capacity and dated cash',six_mean['hours']==18 and six_mean['direct_cost']==690 and six_mean['cash_trough']==-35 and six_mean['closing_cash']==1165 and six_mean['capacity_headroom']==-2)
check('L05: four-hour sensitivity exposes worse six-unit requirements',six_high['hours']==24 and six_high['direct_cost']==900 and six_high['cash_trough']==-245 and six_high['capacity_headroom']==-8)
check('L06: smaller scenario fits stated bounds but is not observed proof',four_high['hours']==16 and four_high['direct_cost']==600 and four_high['cash_trough']==55 and four_high['capacity_headroom']==0 and four_high['closing_cash']==855)
check('L07: original accepted versions preserved',baseline==fixture['accepted'] and fingerprint(baseline)==initial_identity)
check('L08: original frozen prediction not rewritten',fixture['pilot_hour_prediction']=='2' and not all(h<=D('2') for h in hours))

# Stipulated gate outcomes test the declared all-gates requirement, not legal/causal inference.
GATES=tuple('GG'+f'{i:02d}' for i in range(1,8))
def scale_decision(gates):
    if any(v not in {'PASS','FAIL','BLOCKED'} for v in gates.values()):
        raise ValueError('invalid stipulated gate status')
    if any(gates.get(k)=='FAIL' for k in GATES): return 'FAIL'
    if any(gates.get(k)!='PASS' for k in GATES): return 'BLOCKED'
    return 'BOUNDED_PROPOSAL_ONLY'
complete=dict.fromkeys(GATES,'PASS')
check('N04: all-pass stipulated state is proposal, not execution',scale_decision(complete)=='BOUNDED_PROPOSAL_ONLY')
for k in GATES:
    incomplete={a:b for a,b in complete.items() if a!=k}
    check('N04: missing '+k+' blocks scale',scale_decision(incomplete)=='BLOCKED')
check('N04: known failed gate cannot be offset',scale_decision({**complete,'GG06':'FAIL'})=='FAIL')
check('N04: six-unit scenario has independent failure and unknowns',scale_decision({'GG03':'FAIL','GG04':'PASS','GG06':'FAIL'})=='FAIL')
check('N04: smaller cash/capacity success leaves other gates blocked',scale_decision({'GG03':'PASS','GG04':'PASS','GG06':'PASS'})=='BLOCKED')

# Explicit output-action comparisons; no real access-control enforcement is claimed.
def permitted_design_action(command_id,action,approval=False,validated=False):
    if command_id not in C: return False
    if action in {'send','spend','charge','publish','registry-promote','edit-assessed-source'}: return False
    if action=='write-assessment': return C[command_id]['skill']=='business-evaluate'
    if action=='write-draft': return C[command_id]['skill']!='business-evaluate'
    if action=='write-local-catalogue': return command_id=='P07' and approval is True and validated is True
    return False
check('N01: all evaluators allow separate assessment only',all(permitted_design_action(c['id'],'write-assessment') and not permitted_design_action(c['id'],'edit-assessed-source') and not permitted_design_action(c['id'],'write-draft') for c in all_commands if c['skill']=='business-evaluate'))
check('N03: every command denies implicit external effects',all(not permitted_design_action(c['id'],a) for c in all_commands for a in ['send','spend','charge','publish','registry-promote']))
check('N08: valid authorised local catalogue action distinguished',permitted_design_action('P07','write-local-catalogue',True,True))
check('N08: missing approval or validation blocks catalogue action',not permitted_design_action('P07','write-local-catalogue',False,True) and not permitted_design_action('P07','write-local-catalogue',True,False) and not permitted_design_action('P07','write-local-catalogue','true',True))
check('N08: other pack command cannot update catalogue',not permitted_design_action('P01','write-local-catalogue',True,True))
check('N02/N03: unknown commands and modes not accepted',not permitted_design_action('E99','write-assessment') and 'unknown' not in C['E02']['modes'] and '' not in C['G02']['modes'])

def interpreted_test(packet):
    if packet.get('guardrail_breach') is True: return 'STOPPED'
    if packet.get('frozen_plan_unchanged') is not True: return 'NOT_INTERPRETABLE'
    if not packet.get('actual_evidence'): return 'BLOCKED'
    if packet.get('outcome_mature') is not True: return 'INCONCLUSIVE'
    if packet.get('prediction_met') is True: return 'SUPPORTS_TESTED_SCOPE'
    if packet.get('prediction_met') is False: return 'CHALLENGES_PREDICTION'
    return 'INCONCLUSIVE'
packet={'guardrail_breach':False,'frozen_plan_unchanged':True,'actual_evidence':['W1','W2','W3'],'outcome_mature':True,'prediction_met':work_prediction}
check('N05/L09: actual fictional work challenges the retained prediction',interpreted_test(packet)=='CHALLENGES_PREDICTION')
check('N05: absent execution evidence is not a passed learning record',interpreted_test({**packet,'actual_evidence':[]})=='BLOCKED')
check('N06: post-result plan replacement invalidates intended inference',interpreted_test({**packet,'frozen_plan_unchanged':False})=='NOT_INTERPRETABLE')
check('N06: immature outcomes stay inconclusive',interpreted_test({**packet,'outcome_mature':False})=='INCONCLUSIVE')
check('N06: known guardrail stop precedes missing inference inputs',interpreted_test({'guardrail_breach':True})=='STOPPED')

def paired_comparison_record(packet):
    needed=('core_run','pack_run','same_task','same_inputs','versions_recorded','criteria_frozen','results_reviewed')
    return all(packet.get(k) is True for k in needed)
paired={k:True for k in ['core_run','pack_run','same_task','same_inputs','versions_recorded','criteria_frozen','results_reviewed']}
check('N07: complete stipulated paired evidence accepted as record',paired_comparison_record(paired))
for key in paired:
    check('N07: missing '+key+' blocks comparison claim',not paired_comparison_record({k:v for k,v in paired.items() if k!=key}))
check('N07: expected result alone not executed comparison',not paired_comparison_record({'expected_difference':True}))

output={'pilot':{'hours':str(total_hours),'direct_cost':str(total_cost),'consideration':str(receipts),'contribution':str(contribution),'cash_minimum':str(pilot_trough),'cash_closing':str(pilot_close),'work_prediction':work_prediction,'guardrails_hold':guards},'six_mean':{k:str(v) for k,v in six_mean.items()},'six_high':{k:str(v) for k,v in six_high.items()},'four_high':{k:str(v) for k,v in four_high.items()},'accepted_versions_sha256':initial_identity}
print('SYNTHETIC_LOOP '+json.dumps(output,sort_keys=True))
print('COVERAGE '+json.dumps({'skills':len(FILES),'commands':len(C),'fields':sum(len(c['entries']) for c in all_commands),'original_seeds':len(seedrows),'selected_by_skill':{s:len(EXPECTED[s]) for s in FILES}},sort_keys=True))
print('PYTHON '+sys.version.split()[0])
print(f'TOTAL {len(results)} | PASS {sum(ok for _,ok in results)} | FAIL {sum(not ok for _,ok in results)}')
sys.exit(0 if all(ok for _,ok in results) else 1)
