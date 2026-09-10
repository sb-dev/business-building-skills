#!/usr/bin/env python3
"""Stage 14 design/fixture checks. No host, installed pack or external API is run."""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
import sys
from datetime import date
from decimal import Decimal, InvalidOperation, localcontext
from pathlib import Path
from urllib.parse import urlsplit

PREFIX = '2026-09-10-stage-14-'
NAMES = ['saas-business', 'consumer-mobile-subscription', 'professional-services',
         'consulting-business', 'ecommerce-business', 'marketplace-business',
         'creator-digital-product', 'open-source-commercialisation', 'local-service-business']
DIMENSIONS = ['customer / buyer structure', 'offer grammar', 'pricing unit', 'money model',
              'channel priorities', 'sales path', 'delivery model', 'retention model',
              'unit economics', 'capacity constraints', 'cash behaviour', 'core metrics',
              'experiment types', 'quality criteria']
STEPS = ['inspect catalogue', 'prove existing pack is insufficient', 'research business-model practice',
         'define changed core behaviour', 'define economics and constraints', 'build showcase',
         'include exact prompt', 'create positive / negative evals', 'compare core vs core+pack',
         'validate', 'catalogue']
COMMANDS = {*(f'B{i:02}' for i in range(1, 11)), *(f'G{i:02}' for i in range(1, 9)),
            *(f'E{i:02}' for i in range(1, 8)), *(f'P{i:02}' for i in range(1, 8))}
MECHANISM = dict(zip((f'PK{i:02}' for i in range(1, 10)), [
    'hosted_recurring_service', 'store_mediated_mobile_access', 'bounded_human_service',
    'client_dependent_advice', 'physical_goods_flow', 'distinct_sides_matching',
    'digital_rights_and_access', 'open_source_ecosystem', 'geographic_delivery_constraint']))
BASELINE_PATHS = {
    '2026-09-08-business-building-skills-new-project-bootstrap-process.md',
    '2026-09-09-bootstrap-2-execution-contract.md',
    '2026-09-10-stage-13-pack-command-contracts.md',
}


def number(value: str) -> Decimal:
    if not isinstance(value, str):
        raise ValueError('Money and measured quantities require explicit decimal strings')
    try:
        result = Decimal(value)
    except InvalidOperation as exc:
        raise ValueError('Invalid decimal') from exc
    if not result.is_finite():
        raise ValueError('Non-finite decimal')
    return result


def share(numerator: int, denominator: int):
    if type(numerator) is not int or type(denominator) is not int:
        raise ValueError('A count requires an integer, not a boolean or float')
    if numerator < 0 or denominator < 0 or numerator > denominator:
        raise ValueError('Not a share of the stated eligible population')
    return None if denominator == 0 else str(Decimal(numerator) / Decimal(denominator))


def identity(value) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def core_report(case: dict) -> dict:
    """Common calculations; missing cash data never becomes a cash-feasibility pass."""
    ids = [r['id'] for r in case['costs']]
    if len(ids) != len(set(ids)):
        raise ValueError('Duplicate cost identity')
    costs = [number(r['amount']) for r in case['costs']]
    if any(v < 0 for v in costs):
        raise ValueError('Fixture costs use positive outlays; credits need an explicit bridge')
    net = number(case['gross']) - number(case['discount']) - number(case['refund'])
    total_cost = sum(costs, Decimal(0))
    cash = None
    events = case['cash_events']
    if events:
        event_ids = [r['id'] for r in events]
        dates = [date.fromisoformat(r['date']) for r in events]
        if len(event_ids) != len(set(event_ids)) or dates != sorted(dates):
            raise ValueError('Duplicate cash event or unsorted cash calendar')
        balance = number(case['opening_usable_cash'])
        balances = [balance]
        for r in events:
            balance += number(r['amount'])
            balances.append(balance)
        cash = {'minimum': str(min(balances)), 'closing': str(balance)}
    resources = case['resources']
    resource_ids = [r['id'] for r in resources]
    if len(resource_ids) != len(set(resource_ids)):
        raise ValueError('Duplicate resource')
    headroom = {}
    for r in resources:
        amounts = [number(r[k]) for k in ('available', 'shared', 'required')]
        if any(v < 0 for v in amounts):
            raise ValueError('Negative resource input')
        headroom[r['id']] = str(amounts[0] - amounts[1] - amounts[2])
    return {'net': str(net), 'direct_cost': str(total_cost), 'contribution': str(net-total_cost),
            'cash': cash, 'resource_headroom': headroom, 'scale': 'BLOCKED',
            'scale_reason': case['growth_gate_evidence'], 'external_actions': [],
            'accepted_identity': identity(case['accepted'])}


def specialised_report(case: dict) -> dict:
    """Explicit per-fixture projections, not an implemented pack or NLP classifier."""
    f, k = case['facts'], case['id']
    if k == 'S01':
        if len(f['account_net']) != len(f['account_cost']):
            raise ValueError('Unmatched account inputs')
        consumed, billable, invoiced = (f[x] for x in ('consumed_units', 'billable_units', 'invoiced_units'))
        if any(type(v) is not int for v in (consumed, billable, invoiced)) or not 0 <= invoiced <= billable <= consumed:
            raise ValueError('Incompatible usage counts')
        return {'account_contributions': [str(number(n)-number(c)) for n,c in zip(f['account_net'],f['account_cost'])],
                'billable_not_invoiced': billable-invoiced, 'consumed_not_billable': consumed-billable}
    if k == 'S02':
        return {key+'_share': share(f[key], f['eligible']) for key in ('paid','entitled','meaningful_use')}
    if k == 'S03':
        hours = sum((number(x) for x in f['delivery_hours']), Decimal(0)) + number(f['nonbillable_hours'])
        if hours <= 0:
            raise ValueError('Missing positive full-work denominator')
        return {'total_hours':str(hours), 'net_consideration_per_total_hour':str(number(case['gross'])/hours)}
    if k == 'S04':
        if type(f['report_delivered']) is not bool or type(f['client_acceptance']) is not bool:
            raise ValueError('Stipulated acceptance facts require booleans')
        return {'report_delivered':f['report_delivered'], 'acceptance_met':f['client_acceptance'],
                'adoption':f['adoption'], 'realised_impact':f['realised_impact'],
                'milestone_supported':f['client_acceptance'] if f['milestone_requires_acceptance'] else None}
    if k == 'S05':
        ending = f['received_units'] - f['sold_units'] + f['recoverable_returns']
        if ending != f['ending_physical'] or not 0 <= f['committed'] <= ending:
            raise ValueError('Incompatible stock states')
        return {'physical':ending, 'available':ending-f['committed'], 'committed':f['committed'],
                'gross_sold_received_share':share(f['sold_units'],f['received_units'])}
    if k == 'S06':
        bank, sellers, reserve = (number(f[x]) for x in ('bank_after_operations','seller_funds','refund_reserve'))
        return {'matched_request_share':share(f['matched_requests'],f['eligible_requests']),
                'transaction_value':f['transaction_value'], 'own_consideration':case['gross'],
                'usable_before':str(bank-sellers-reserve),
                'usable_after_seller_settlement':str((bank-sellers)-reserve),
                'usable_after_reserved_refund':str(bank-sellers-reserve)}
    if k == 'S07':
        return {'access_removal':'FAIL' if f['existing_access_promised'] and f['proposed_access_removal'] else 'NOT APPLICABLE',
                'future_update_cost_is_scenario':f['future_update_cost_is_scenario']}
    if k == 'S08':
        return {'maintenance_funding_gap':str(max(Decimal(0),number(f['monthly_maintenance_need'])-number(f['secured_recurring_maintenance_funding']))),
                'adopters':f['adopters'],'contributors':f['contributors'],'payers':f['payers'],'stars':f['stars'],
                'existing_open_source_rights':f['existing_open_source_rights']}
    if k == 'S09':
        hands=f['visits']*f['service_minutes']; full=f['visits']*(f['service_minutes']+f['travel_minutes']+f['setup_minutes'])
        return {'hands_on_minutes':hands,'full_minutes':full,'other_minutes':full-hands,
                'full_cycle_labour_cost':str(Decimal(full)*number(f['labour_per_minute']))}
    raise ValueError('Unrecognised design fixture')


def activation(pack: str, facts: dict, selected, compatible) -> str:
    if pack not in MECHANISM:
        return 'FAIL'
    fact=facts.get(MECHANISM[pack])
    if fact is False:
        return 'NOT APPLICABLE'
    if fact is not True or selected is not True or compatible is not True:
        return 'BLOCKED'
    return 'PASS'


def choose_default(key, pack_value, explicit, accepted, constraint=None, core_value=None):
    """Checks stipulations, not law. Does not alter input records or grant permission."""
    if key in {'external_actions','waive_core_gates','fabricate_evidence'}:
        return {'status':'FAIL','value':None,'origin':'forbidden override'}
    if constraint is not None and constraint.get('reviewed_current_applicable') is not True:
        return {'status':'BLOCKED','value':None,'origin':'unresolved constraint'}
    for origin, record in [('explicit', explicit),('accepted', accepted)]:
        if key in record:
            value=record[key]
            if constraint is not None and value not in constraint['allowed_values']:
                return {'status':'BLOCKED','value':value,'origin':origin+' conflicts with constraint'}
            if origin=='explicit' and key in accepted and accepted[key]!=value:
                return {'status':'BLOCKED','value':value,'origin':'accepted decision needs impact review'}
            return {'status':'PASS','value':value,'origin':origin}
    value, origin=(pack_value,'pack default') if pack_value is not None else (core_value,'core default')
    if constraint is not None and value not in constraint['allowed_values']:
        return {'status':'FAIL','value':value,'origin':'default conflicts with constraint'}
    return {'status':'PASS','value':value,'origin':origin}


def qualification(packet: dict) -> str:
    """Admission-rule probe on reviewed stipulations, not automated business assessment."""
    if packet.get('label_only') is True or packet.get('replaces_execution') is True:
        return 'FAIL'
    if packet.get('adequate_existing_option') is True:
        return 'NOT APPLICABLE'  # No new pack is needed; the original task remains valid.
    if packet.get('mechanism_evidence_reviewed') is not True or packet.get('comparison_reviewed') is not True:
        return 'BLOCKED'
    effects=packet.get('effects', [])
    if not effects or any(e.get('command') not in COMMANDS or not e.get('delta') for e in effects):
        return 'FAIL'
    required={'facts','accepted_decisions','truthfulness','rights','core_gates','external_authority'}
    if not required <= set(packet.get('preserved', [])):
        return 'FAIL'
    if not packet.get('positive_case') or not packet.get('negative_case') or not packet.get('source_locators'):
        return 'BLOCKED'
    return 'PASS'


def raises(call):
    try:
        call()
    except (ValueError, KeyError, TypeError):
        return True
    return False


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('workspace',type=Path)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    log=args.workspace/'docs/research-logs'
    names=['pack-model.md','candidate-catalogue.md','pack-authoring.md','research-and-sources.md','design-probes.md']
    texts={name:(log/(PREFIX+name)).read_text(encoding='utf-8') for name in names}
    results=[]
    def check(name, ok):
        results.append({'name':name,'passed':bool(ok)})
        print(('PASS' if ok else 'FAIL')+' | '+name)
    model,catalogue,author,sources,probes=(texts[n] for n in names)
    records=re.split(r'^### PK',catalogue,flags=re.M)[1:]
    parsed_names=re.findall(r'^### PK\d{2} — `([^`]+)`',catalogue,re.M)
    check('nine original candidate names in order',parsed_names==NAMES)
    check('eight retained candidates and one explicit advisory merge',catalogue.count('**Design disposition:** RETAIN AS DESIGN CANDIDATE')==8 and catalogue.count('**Design disposition:** MERGE INTO PROFESSIONAL-SERVICES ADVISORY MODE')==1)
    check('every candidate remains unimplemented',catalogue.count('**Implementation status:** NOT IMPLEMENTED.')==9)
    drows=lambda text:re.findall(r'^\| D\d{2} \| ([^|]+) \|',text,re.M)
    check('fourteen model dimensions in original order',[x.strip() for x in drows(model)]==DIMENSIONS)
    for i,record in enumerate(records,1):
        check(f'PK{i:02}: all fourteen dimension treatments',[x.strip() for x in drows(record)]==DIMENSIONS)
        check(f'PK{i:02}: fit, non-fit, comparison and discriminating case',all(x in record for x in ['**Fit:**','**Non-activation:**','**Core/catalogue comparison:**',f'design case S{i:02}']))
        effects=re.findall(r'^\| (PK\d{2}-E\d) \| ([^|]+) \| ([^|]+) \|$',record,re.M)
        check(f'PK{i:02}: three traced effects and valid command owners',len(effects)==3 and all(set(re.findall(r'[BGEP]\d{2}',cmd))<=COMMANDS and bool(re.findall(r'[BGEP]\d{2}',cmd)) and behavior.strip() for _,cmd,behavior in effects))
    check('eleven authoring steps in original order',[s.strip() for s in re.findall(r'^\| A\d{2} \| ([^|]+) \|',author,re.M)]==STEPS)
    check('all P01-P07 command responsibilities retained',all(f'P{i:02}' in author for i in range(1,8)))
    check('four original label-only controls',all(f'| {x} |' in model for x in ['AI startup','finance company','fitness business','London business']))
    check('precedence separates mandatory core invariants from defaults',all(s in model for s in ['Verified legal/regulatory constraints','Approved business decisions','Selected pack defaults','Core defaults','Core mandatory evidence']))
    check('selection, hybrid scopes and withdrawal are explicit',all(s in model for s in ['explicit selection','last-loaded-wins','Withdrawal','shared']))
    check('no official pack protocol or installed claim',all(s in model for s in ['not an official business-pack protocol','not an installed pack set']))
    source_ids=set(re.findall(r'^### (R\d{2}) —',sources,re.M))
    check('seventeen scoped selected source records',source_ids=={f'R{i:02}' for i in range(1,18)})
    used=set(re.findall(r'\bR\d{2}\b',catalogue))
    check('candidate sources resolve to actual register',used<=source_ids)
    check('source discrepancy and failed retrieval limits explicit',all(s in sources for s in ['inverts the fraction','not read','no readable live body']))
    urls=re.findall(r'^Source: (\S+)',sources,re.M)
    check('source URLs have explicit https hosts',len(urls)==17 and all(urlsplit(u).scheme=='https' and urlsplit(u).netloc for u in urls))
    targets=[t.split('#')[0] for text in texts.values() for t in re.findall(r'\]\(([^)]+)\)',text) if not t.startswith(('http:','https:','#'))]
    future_here={PREFIX+'conformance.md',PREFIX+'verifier.py'}
    check('document links resolve to local outputs or read baseline paths',all((log/t).is_file() or t in BASELINE_PATHS or t in future_here for t in targets))
    check('templates distinguished from concrete execution',all(s in author for s in ['copyable template','both required conditions','unrun arm','not a completed primary example']))
    payload=re.search(r'<!-- FIXTURES BEGIN -->\s*```json\s*(.*?)\s*```\s*<!-- FIXTURES END -->',probes,re.S)
    if payload is None:
        raise ValueError('Missing fixed fixture block')
    fixtures=json.loads(payload[1]); check('nine original fixed cases, all synthetic',[f['id'] for f in fixtures]==[f'S{i:02}' for i in range(1,10)] and all(f['synthetic'] is True for f in fixtures))
    check('nine concrete exact tasks in prompts',[f['prompt'] for f in fixtures]==re.findall(r'### S\d{2} — PK\d{2}\s*```text\s*(.*?)\s*```',probes,re.S))
    check('comparison scope excludes installed-agent superiority',all(s in probes for s in ['deterministic design projection','does not test whether an LLM','does not claim superiority']))
    expected_contribution=['40','710','200','400','280','20','10','0','180']; pairs={}
    with localcontext() as ctx:
        ctx.prec=28
        for f,expected in zip(fixtures,expected_contribution):
            before=identity(f); base=core_report(f); pack={'common':core_report(f),'specialised':specialised_report(f)}
            check(f["id"]+': identical common core report in both conditions',base==pack['common'])
            check(f["id"]+': input and accepted versions unchanged',identity(f)==before and base['accepted_identity']==identity(f['accepted']))
            check(f["id"]+': expected contribution; no scale or external authority',number(base['contribution'])==number(expected) and base['scale']=='BLOCKED' and base['external_actions']==[])
            pairs[f['id']]={'input_identity':before,'core_only':base,'core_plus_candidate':pack}
        s=lambda k:pairs[k]['core_plus_candidate']['specialised']
        b=lambda k:pairs[k]['core_only']
        check('S01: account and usage bridges',s('S01')=={'account_contributions':['70','-30'],'billable_not_invoiced':1000,'consumed_not_billable':3000})
        check('S02: distinct renewal, entitlement and use',s('S02')=={'paid_share':'0.9','entitled_share':'0.95','meaningful_use_share':'0.6'})
        check('S02: cash timing retained',b('S02')['cash']=={'minimum':'-80','closing':'710'})
        check('S03: full work denominator and finite capacity',number(s('S03')['total_hours'])==24 and number(s('S03')['net_consideration_per_total_hour'])==number('1000')/24 and b('S03')['resource_headroom']=={'consultant':'-2'})
        check('S04: delivery is not acceptance, adoption or impact',s('S04')['report_delivered'] is True and s('S04')['acceptance_met'] is False and s('S04')['adoption'] is None and s('S04')['realised_impact'] is None and s('S04')['milestone_supported'] is False)
        check('S05: physical, committed and available reconcile',s('S05')['physical']==10 and s('S05')['committed']==2 and s('S05')['available']==8)
        check('S05: positive contribution and closing do not erase cash trough',b('S05')['cash']=={'minimum':'-620','closing':'180'})
        check('S06: source inversion rejected by eligible-request share',s('S06')['matched_request_share']=='0.4' and Decimal(10)/4!=Decimal('0.4'))
        check('S06: restricted funds settle without double deduction',s('S06')['usable_before']==s('S06')['usable_after_seller_settlement']==s('S06')['usable_after_reserved_refund']=='100' and b('S06')['cash']['closing']=='100')
        check('S07: access obligation and scenario label preserved',s('S07')['access_removal']=='FAIL' and s('S07')['future_update_cost_is_scenario'] is True and b('S07')['cash']=={'minimum':'50','closing':'360'})
        check('S08: funding gap and actor counts remain distinct',s('S08')['maintenance_funding_gap']=='500' and [s('S08')[x] for x in ['adopters','contributors','payers','stars']]==[1000,20,3,5000])
        check('S09: complete visit time and cost, not a route guarantee',s('S09')=={'hands_on_minutes':225,'full_minutes':400,'other_minutes':175,'full_cycle_labour_cost':'120.00'} and b('S09')['resource_headroom']=={'operator-day':'-40'})
        check('missing cash schedule remains unknown',b('S01')['cash'] is None and b('S04')['cash'] is None)
        check('share rejects inverted or invalid populations',raises(lambda:share(10,4)) and raises(lambda:share(True,10)) and raises(lambda:share(-1,10)))
        check('zero eligible population is undefined, not zero success',share(0,0) is None)
        check('non-finite and binary-float financial inputs rejected',all(raises(lambda x=x:number(x)) for x in ['NaN','Infinity','bad',1.1]))
        duplicate=copy.deepcopy(fixtures[0]); duplicate['costs'].append(copy.deepcopy(duplicate['costs'][0]))
        check('duplicated cost identity rejected',raises(lambda:core_report(duplicate)))
        missing=copy.deepcopy(fixtures[0]); del missing['facts']['billable_units']
        check('missing specialised input does not become zero',raises(lambda:specialised_report(missing)))
        bad_cash=copy.deepcopy(fixtures[4]); bad_cash['cash_events'].reverse()
        check('reversed cash calendar rejected',raises(lambda:core_report(bad_cash)))
        for pk,fact in MECHANISM.items():
            check(pk+': applicable selected compatible control',activation(pk,{fact:True},True,True)=='PASS')
            check(pk+': non-fit, unknown and unselected do not activate',activation(pk,{fact:False},True,True)=='NOT APPLICABLE' and activation(pk,{},True,True)=='BLOCKED' and activation(pk,{fact:True},False,True)=='BLOCKED')
            check(pk+': string true and incompatible version do not activate',activation(pk,{fact:'true'},True,True)=='BLOCKED' and activation(pk,{fact:True},True,False)=='BLOCKED')
        check('unknown pack fails selector validation',activation('PK99',{},True,True)=='FAIL')
        for label in ['AI startup','finance company','fitness business','London business']:
            check('label alone never supplies mechanism: '+label,all(activation(pk,{'label':label},True,True)=='BLOCKED' for pk in MECHANISM))
        admission={'label_only':False,'replaces_execution':False,'adequate_existing_option':False,
                   'mechanism_evidence_reviewed':True,'comparison_reviewed':True,
                   'effects':[{'command':'B06','delta':'include travel and setup in visit capacity'}],
                   'preserved':['facts','accepted_decisions','truthfulness','rights','core_gates','external_authority'],
                   'positive_case':'S09','negative_case':'location-label-only','source_locators':['R16','Stage 7 capacity contract']}
        check('qualification: complete reviewed design packet is admitted',qualification(admission)=='PASS')
        check('qualification: adequate existing option avoids a new pack',qualification({**admission,'adequate_existing_option':True})=='NOT APPLICABLE')
        check('qualification: label and replacement execution rejected',qualification({**admission,'label_only':True})=='FAIL' and qualification({**admission,'replaces_execution':True})=='FAIL')
        check('qualification: absent or no-effect contract rejected',qualification({**admission,'effects':[]})=='FAIL' and qualification({**admission,'effects':[{'command':'B06','delta':''}]})=='FAIL')
        check('qualification: unrecognised command cannot be hidden in a pack',qualification({**admission,'effects':[{'command':'send-email','delta':'send'}]})=='FAIL')
        for invariant in admission['preserved']:
            check('qualification: cannot drop '+invariant,qualification({**admission,'preserved':[x for x in admission['preserved'] if x!=invariant]})=='FAIL')
        for key in ['mechanism_evidence_reviewed','comparison_reviewed','positive_case','negative_case','source_locators']:
            check('qualification: missing '+key+' blocks admission',qualification({k:v for k,v in admission.items() if k!=key})=='BLOCKED')
        check('qualification: string review flag is not evidence',qualification({**admission,'comparison_reviewed':'true'})=='BLOCKED')
        accepted={'price':'80'}; before=identity(accepted)
        r=choose_default('price','100',{},accepted)
        check('accepted decision outranks pack default without mutation',r=={'status':'PASS','value':'80','origin':'accepted'} and identity(accepted)==before)
        check('explicit one-time fact outranks subscription preference',choose_default('unit','subscription',{'unit':'one-time'}, {})['value']=='one-time')
        check('zero or false higher-priority value is not ignored',choose_default('price','100',{}, {'price':0})['value']==0 and choose_default('renew',True,{'renew':False},{})['value'] is False)
        check('new fact versus accepted decision triggers review',choose_default('price','100',{'price':'90'},accepted)['status']=='BLOCKED')
        constraint={'reviewed_current_applicable':True,'allowed_values':['one-time']}
        check('top-level conflict remains explicit rather than rewritten',choose_default('unit','subscription',{'unit':'subscription'}, {},constraint)['status']=='BLOCKED')
        check('known constraint rejects contrary lower default',choose_default('unit','subscription',{}, {},constraint)['status']=='FAIL')
        check('unverified constraint is not treated as permission',choose_default('unit','one-time',{}, {},{**constraint,'reviewed_current_applicable':'true'})['status']=='BLOCKED')
        check('open pack default and fallback core default remain labelled',choose_default('unit','one-time',{}, {})['origin']=='pack default' and choose_default('unit',None,{}, {},core_value='open')['origin']=='core default')
        check('core safeguards and external effects cannot be overridden',all(choose_default(k,True,{}, {})['status']=='FAIL' for k in ['external_actions','waive_core_gates','fabricate_evidence']))
    report={'stage':14,'scope':'local structural, arithmetic and stipulated design-contract checks; not installed-pack performance',
            'python':sys.version.split()[0], 'checks':results,'total':len(results),'passed':sum(r['passed'] for r in results),
            'failed':sum(not r['passed'] for r in results),'coverage':{'candidates':len(parsed_names),'independent_candidates':8,'merged_modes':1,'dimension_treatments':sum(len(drows(r)) for r in records),'core_effects':27,'authoring_steps':len(STEPS),'paired_design_cases':len(pairs)},'paired_design_outputs':pairs,
            'inputs_sha256':{PREFIX+n:hashlib.sha256((log/(PREFIX+n)).read_bytes()).hexdigest() for n in names}}
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('COVERAGE '+json.dumps(report['coverage'],sort_keys=True))
    print('PYTHON '+report['python'])
    print(f"TOTAL {report['total']} | PASS {report['passed']} | FAIL {report['failed']}")
    return 0 if report['failed']==0 else 1


if __name__=='__main__':
    sys.exit(main())
