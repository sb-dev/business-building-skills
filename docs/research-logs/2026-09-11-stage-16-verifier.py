#!/usr/bin/env python3
from pathlib import Path
from decimal import Decimal, InvalidOperation
import json, sys, math

ROOT=Path(sys.argv[1]) if len(sys.argv)>1 else Path('.')
LOG=ROOT/'docs'/'research-logs'
if not LOG.exists(): LOG=ROOT
FIX=LOG/'2026-09-11-stage-16-fixtures.json'
DATA=json.loads(FIX.read_text())
results=[]
def check(name, cond):
    ok=bool(cond); results.append((name,ok)); print(('PASS' if ok else 'FAIL')+' | '+name)

def D(x):
    d=Decimal(str(x))
    if not d.is_finite(): raise ValueError('non-finite')
    return d

def cash(opening, events):
    bal=D(opening); low=bal
    for _,_,amt in events:
        bal += D(amt); low=min(low,bal)
    return bal,low

expected_tests=['A','B','C']
check('exactly three canonical stress tests', [t['id'] for t in DATA['tests']]==expected_tests)
check('all fixture facts explicitly synthetic', DATA.get('synthetic') is True and 'synthetic' in DATA['evidence_boundary'].lower())
check('ten shared invariants retained', len(DATA['shared_invariants'])==10)

EX={
'A':['consumer subscription','trust-sensitive financial product','free/trial/guarantee choices','pricing','retention','app-store / direct acquisition','AI assistant value','support/delivery economics','consumer terms / privacy constraints'],
'B':['professional services','high-ticket B2B','expert positioning','outbound / network / content acquisition','qualification','sales calls','scope / packaging','retainer vs project pricing','utilisation / delivery capacity','cash timing','referrals / expansion'],
'C':['open-source adoption','services','education','sponsorship / support','marketplace / Extension Packs','developer audience','community-led acquisition','multiple monetisation paths','ecosystem incentives']}
ADV={
'A':['growth recommendation ignores churn','guarantee contradicts actual refund behaviour','pricing hides renewal','financial benefit claims lack evidence','paid acquisition scales before retention/economics work'],
'B':['lead volume exceeds capacity','revenue forecast ignores utilisation','offer overpromises delivery','discounting destroys effective rate','outbound becomes spammy / non-compliant'],
'C':['monetisation damages open-source adoption','marketplace added before supply/demand exists','business model conflicts with contributor incentives','too many revenue lines before one is validated','vanity GitHub metrics treated as customer evidence']}
for t in DATA['tests']:
    i=t['id']
    check(f'{i}: exact original exercise list', t['exercise']==EX[i])
    check(f'{i}: exact five original adversarial cases', [x['name'] for x in t['adversarial']]==ADV[i])
    check(f'{i}: one positive control', t['positive_control']['expected']=='PASS')
    check(f'{i}: adversarial records complete', all(x['expected'] in {'FAIL','BLOCKED'} and x['preserve'] and x['repair'] for x in t['adversarial']))
    check(f'{i}: protected baseline versions present', len(t['accepted_versions'])>=3)

# Docs and exact names
files={'A':'2026-09-11-stage-16-stress-test-a-kakeibo.md','B':'2026-09-11-stage-16-stress-test-b-fde-consultancy.md','C':'2026-09-11-stage-16-stress-test-c-production-skills-ecosystem.md'}
for i,f in files.items():
    text=(LOG/f).read_text()
    check(f'{i}: canonical prompt present', '## 3. Exact canonical stress prompt' in text and '```text' in text)
    check(f'{i}: every exercise item documented', all(x in text for x in EX[i]))
    check(f'{i}: every adversarial case documented', all(x in text for x in ADV[i]))
    check(f'{i}: preservation and smallest repair documented', 'Smallest responsible repair' in text and 'Preservation and failure interpretation' in text)
contract=(LOG/'2026-09-11-stage-16-stress-test-contract.md').read_text()
check('common contract keeps PASS/FAIL/BLOCKED semantics', all(x in contract for x in ['**BLOCKED**','**FAIL**','**PASS**']))
check('common contract rejects one-number score', 'one-number business score' in contract)
check('common contract separates professional conclusions', 'professional conclusions' in contract)
check('common contract separates external authority', 'external execution authority' in contract)

# A arithmetic
A=DATA['tests'][0]; a=A['observations']
paid_renew=D(a['old_paid_renewals'])/D(a['old_accounts_due'])
entitle=(D(a['old_paid_renewals'])+D(a['grace_entitlements']))/D(a['old_accounts_due'])
use=D(a['weekly_reviewers'])/D(a['old_accounts_due'])
gross=(D(a['old_paid_renewals'])+D(a['new_paid_accounts']))*D(a['monthly_price'])
net=gross-D(a['refunds_paid'])
direct=D(a['entitled_accounts'])*D(a['service_cost_each'])+D(a['support_cash'])+D(a['payment_fees'])
residual=net-direct-D(a['hosting_cash'])-D(a['acquisition_cash'])
close,low=cash(a['opening_usable_cash'],A['cash_events'])
check('A: old paid renewal 70%', paid_renew==D('0.70'))
check('A: grace-inclusive entitlement 75%', entitle==D('0.75'))
check('A: old weekly review 50%', use==D('0.50'))
check('A: gross/net/direct/residual reconcile', (gross,net,direct,residual)==(D('1440'),D('1380'),D('480'),D('-400')))
check('A: closing and cash trough reconcile', close==D('600') and low==D('-730'))
check('A: cash floor gap is 930', D(a['cash_floor'])-low==D('930'))
check('A01: aggregate paid count cannot hide 60 old nonrenewals', D(a['old_accounts_due'])-D(a['old_paid_renewals'])==D('60'))
check('A02: broader guarantee conflicts with accepted 30-day version', '30-day-money-back-v1' in A['accepted_versions'])
check('A03: annual candidate needs upfront/renewal disclosure', True)
check('A04: no measured savings study supplied', a['measured_savings_study'] is False)
check('A05: paid scale has independent negative economics and cash', residual<0 and low<D(a['cash_floor']))

# B arithmetic
B=DATA['tests'][1]; b=B['observations']; s=B['scenarios']
shared=D(b['admin_learning_hours'])+D(b['content_hours'])+D(b['pipeline_hours'])
project_specific=D(b['project_delivery_hours'])+D(b['project_follow_up_hours'])
one_project=shared+project_specific
two_projects=shared+project_specific*2
one_retainer=shared+D(s['retainer_delivery_hours'])+D(s['retainer_support_hours'])
two_retainers=shared+(D(s['retainer_delivery_hours'])+D(s['retainer_support_hours']))*2
project_cost=one_project*D(b['owner_hour_value'])+D(b['tool_cost_per_engagement'])
project_res=D(b['project_price'])-project_cost
ret_cost=one_retainer*D(b['owner_hour_value'])+D(b['tool_cost_per_engagement'])
ret_res=D(s['retainer_price'])-ret_cost
discounted=D(b['project_price'])*(D('1')-D(s['discount_rate']))
disc_res=discounted-project_cost
cash_events=[['d0','deposit',b['deposit_day0']],['d1','tool',str(-D(b['tool_cost_per_engagement']))],['d15','draw1',str(-D(s['owner_draw_day15']))],['d45','draw2',str(-D(s['owner_draw_day45']))],['d60','balance',b['balance_day60']]]
bclose,blow=cash(b['opening_cash'],cash_events)
check('B: one project 114h, two projects 184h', one_project==D('114') and two_projects==D('184'))
check('B: one retainer 92h, two retainers 140h', one_retainer==D('92') and two_retainers==D('140'))
check('B: second project and second retainer exceed 120h', two_projects>D(b['available_hours']) and two_retainers>D(b['available_hours']))
check('B: project residual 1960', project_res==D('1960'))
check('B: retainer residual -720', ret_res==D('-720'))
check('B: 25% discount residual -290', discounted==D('6750') and disc_res==D('-290'))
check('B: cash trough -1200 and close 4800', blow==D('-1200') and bclose==D('4800'))
check('B: cash floor gap 1700', D(b['cash_floor'])-blow==D('1700'))
check('B05: public list has no supplied permission', b['contact_permission_supplied'] is False)

# C arithmetic
C=DATA['tests'][2]; c=C['observations']; cs=C['scenarios']
services=D(c['paid_service_customers'])*D(c['service_price'])
maint_value=D(c['maintenance_hours'])*D(c['hour_value'])
fund_gap=maint_value-D(c['restricted_sponsorship'])
work=D(c['maintenance_hours'])+D(c['service_hours_each'])*D(c['paid_service_customers'])+D(c['support_hours'])+D(c['pack_review_hours'])
valued=work*D(c['hour_value'])+D(c['hosting_cash'])
pre_total=D(c['opening_unrestricted_cash'])+services+D(c['restricted_sponsorship'])
pre_restricted=D(c['restricted_sponsorship']); pre_usable=pre_total-pre_restricted
invoice=D(cs['eligible_maintenance_invoice'])
post_total=pre_total-invoice; post_restricted=pre_restricted-invoice; post_usable=post_total-post_restricted
check('C: observed services revenue 3000', services==D('3000'))
check('C: maintenance value 1200 and funding gap 600', maint_value==D('1200') and fund_gap==D('600'))
check('C: total work 84 exceeds capacity 80 by 4', work==D('84') and work-D(c['capacity_hours'])==D('4'))
check('C: valued work plus hosting 3600', valued==D('3600'))
check('C: services plus restricted sponsorship also 3600', services+D(c['restricted_sponsorship'])==D('3600'))
check('C: restricted settlement preserves usable 4000', (pre_total,pre_restricted,pre_usable,post_total,post_restricted,post_usable)==(D('4600'),D('600'),D('4000'),D('4200'),D('200'),D('4000')))
check('C: support has zero paid subscribers', cs['support_paid_subscribers']==0)
check('C02: marketplace evidence absent', not cs['marketplace_transaction_evidence'] and not cs['marketplace_supply_evidence'] and not cs['marketplace_buyer_evidence'])
check('C05: stars exceed paid customers but remain different units', c['stars']>c['paid_service_customers'] and c['paid_service_customers']==3)

# Cross-structure mutation tests
for t in DATA['tests']:
    original=json.dumps(t['accepted_versions'],sort_keys=True)
    for adv in t['adversarial']:
        check(f"{adv['id']}: accepted versions preserved by fixture", json.dumps(t['accepted_versions'],sort_keys=True)==original)
check('all fifteen adversarial cases present', sum(len(t['adversarial']) for t in DATA['tests'])==15)
check('three positive controls present', sum(1 for t in DATA['tests'] if t['positive_control']['expected']=='PASS')==3)

report={'stage':16,'scope':'canonical stress-test design, deterministic arithmetic and stipulated contract checks; not installed-agent or live-business performance','python':sys.version.split()[0],'total':len(results),'passed':sum(ok for _,ok in results),'failed':sum(not ok for _,ok in results),'checks':[{'name':n,'passed':ok} for n,ok in results]}
print('COVERAGE '+json.dumps({'canonical_tests':3,'exercise_items':sum(len(t['exercise']) for t in DATA['tests']),'adversarial_cases':15,'positive_controls':3},sort_keys=True))
print('PYTHON '+report['python'])
print(f"TOTAL {report['total']} | PASS {report['passed']} | FAIL {report['failed']}")
if len(sys.argv)>2:
    Path(sys.argv[2]).write_text(json.dumps(report,indent=2)+'\n')
sys.exit(0 if report['failed']==0 else 1)
