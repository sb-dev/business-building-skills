#!/usr/bin/env python3
"""Verify Stage 16 design coverage, immutable inputs and fixed arithmetic.

This is a bootstrap design verifier, not an Agent Skills benchmark or a
business-reasoning evaluator. The separate conformance records semantic review.
Run from any cwd with Python 3.10+; only the standard library is required.
"""
from pathlib import Path
from decimal import Decimal, InvalidOperation
import hashlib
import json
import platform
import re
import sys

LOG = Path(__file__).resolve().parent
ROOT = LOG.parent.parent
PREFIX = '2026-09-12-stage-16'
OUT = LOG / (PREFIX + '-executed-checks.json')
checks = []

def check(name, condition, detail):
    checks.append({'check': name, 'result': 'PASS' if condition else 'FAIL', 'evidence': detail})

def D(value):
    if isinstance(value, bool) or not isinstance(value, (str, int, Decimal)):
        raise ValueError('Expected explicit decimal string, integer or Decimal')
    try:
        number = Decimal(value)
    except InvalidOperation as exc:
        raise ValueError('Invalid decimal') from exc
    if not number.is_finite():
        raise ValueError('Non-finite input')
    return number

def eq(name, actual, expected):
    check(name, D(actual) == D(expected), {'actual': str(actual), 'expected': str(expected)})

def blob(path):
    b = path.read_bytes()
    return hashlib.sha1(b'blob ' + str(len(b)).encode() + b'\0' + b).hexdigest()

def decode_prompt(prompt):
    return json.loads(re.search(r'Facts \(JSON\):\n(.*?)\n\nTask:', prompt, re.S).group(1))

def cash(opening, events):
    current = D(opening)
    low = current
    calendar = []
    for date, identity, amount in events:
        current += D(amount)
        low = min(low, current)
        calendar.append({'date':date, 'identity':identity, 'balance':str(current)})
    return current, low, calendar

def main():
    # A real running state makes the report path resolvable during link checks.
    # It is always replaced by actual results or an explicit verifier error.
    OUT.write_text(json.dumps({'state':'RUNNING', 'stage':16})+'\n')
    corpus = json.loads((LOG / (PREFIX+'-cases.json')).read_text())
    spec_path = ROOT / corpus['specification']
    spec = spec_path.read_text()
    check('Original specification identity', blob(spec_path) == corpus['specification_blob'], blob(spec_path))
    stage = spec.split('# 23. Stage 16 — Design Canonical Business Stress Tests\n',1)[1].split('# 24. Stage 17',1)[0]
    check('Exactly three canonical designs', [c['id'] for c in corpus['cases']] == ['A','B','C'], [c['id'] for c in corpus['cases']])
    check('Inherited file manifest complete', len(corpus['inherited_files']) == 85 and len({f['path'] for f in corpus['inherited_files']}) == 85, len(corpus['inherited_files']))
    for f in corpus['inherited_files']:
        p = ROOT/f['path']
        actual = blob(p) if p.is_file() else None
        check('Preserved '+f['path'], actual == f['sha'], {'expected':f['sha'],'actual':actual})
    source = (LOG/'2026-09-10-stage-15-level-05.md').read_text()
    source_sections = {m.group(1):m.group(2) for m in re.finditer(r'## (E1[345]) — [^\n]+\n(.*?)(?=\n## |\Z)',source,re.S)}
    commands = set()
    for kind,skill in [('build','business-build'),('grow','business-grow'),('evaluate','business-evaluate'),('pack','business-pack-author')]:
        command_text = (LOG/f'2026-09-10-stage-13-{kind}-command-contracts.md').read_text()
        commands.update(skill+'/'+s for s in re.findall(r'^### [BGEP]\d+ — `([^`]+)`',command_text,re.M))
    check('Accepted canonical command catalogue',len(commands)==32,sorted(commands))
    distributions = []
    all_variants = []
    for c in corpus['cases']:
        segment = stage.split('## Stress Test '+c['id']+' — ',1)[1].split('## Stress Test ',1)[0]
        original_title = segment.split('\n',1)[0]
        blocks = re.findall(r'```text\n(.*?)\n```',segment,re.S)
        original_exercises, original_adversaries = [b.splitlines() for b in blocks]
        check(c['id']+' exact name',c['title']==original_title,original_title)
        check(c['id']+' original exercise coverage',[x['requirement'] for x in c['coverage']]==original_exercises,original_exercises)
        check(c['id']+' original adversarial coverage',[v['requirement'] for v in c['variants']]==original_adversaries,original_adversaries)
        expected_ids=[c['id']+f'{n:02}' for n in range(1,6)]
        check(c['id']+' five unique adversarial IDs',[v['id'] for v in c['variants']]==expected_ids,expected_ids)
        accepted_prompt = re.search(r'### Exact copyable prompt\n\n```text\n(.*?)\n```',source_sections[c['base_example']],re.S).group(1)
        check(c['id']+' exact accepted prompt',c['base_prompt']==accepted_prompt,c['base_example'])
        check(c['id']+' exact accepted facts',c['base_inputs']==decode_prompt(accepted_prompt),c['base_inputs']['case_version'])
        check(c['id']+' protected versions',c['protected_versions']==c['base_inputs']['accepted_versions'],c['protected_versions'])
        check(c['id']+' synthetic boundary',c['synthetic'] is True and c['base_inputs']['synthetic'] is True,c['version'])
        check(c['id']+' prompt SHA256',hashlib.sha256(c['base_prompt'].encode()).hexdigest()==c['base_prompt_sha256'],c['base_prompt_sha256'])
        doc=(ROOT/c['output_path']).read_text()
        check(c['id']+' complete base and stress prompt in document',c['base_prompt'] in doc and c['stress_instruction'] in doc,c['output_path'])
        check(c['id']+' complete shared protocol',corpus['common_protocol'] in doc,c['output_path'])
        for row in c['coverage']:
            check(c['id']+' mapping '+row['requirement'], all(s in commands for s in row['selectors']) and row['expected_evidence'] in doc and row['failure_condition'] in doc and all(x in expected_ids for x in row['adversarial_ids']), row['selectors'])
        for v in c['variants']:
            all_variants.append(v['id'])
            required=['requirement','review_request','failing_candidate','adequate_candidate','smallest_repair']
            check(v['id']+' complete overlay and distinct authored controls',bool(v['fixture_extension']) and all(v[k] in doc and len(v[k])>15 for k in required) and v['failing_candidate'] != v['adequate_candidate'],v['requirement'])
            check(v['id']+' discriminating findings and handoffs',len(v['required_findings'])>=3 and all(f in doc for f in v['required_findings']) and all(h in doc for h in v['handoffs']) and bool(v['growth_gates']),v['growth_gates'])
            check(v['id']+' exact copyable overlay',json.dumps(v['fixture_extension'],indent=2,ensure_ascii=False) in doc,v['fixture_extension'])
        expected_fields=['assumption','hypothesis','cheapest_valid_test','target_population','success_failure_signal','guardrails','duration_sample','confounders','decision_rule']
        check(c['id']+' complete nine-field evidence design',list(c['evidence_test'])==expected_fields and all(v in doc for v in c['evidence_test'].values()),expected_fields)
        check(c['id']+' complete architecture walkthrough',len(c['design_walkthrough'])==4 and all(v in doc for v in c['design_walkthrough']),c['design_walkthrough'])
        check(c['id']+' optional pack design trace',len(c['pack_effects'])==3 and c['optional_pack'] in doc and all(e in doc for e in c['pack_effects']),c['pack_effects'])
        distributions.append((len(c['coverage']),len(c['variants'])))
    check('Exact coverage distribution',distributions==[(9,5),(11,5),(9,5)],distributions)
    check('Fifteen distinct adversarial designs',len(all_variants)==len(set(all_variants))==15,all_variants)
    primaries=[]
    counts=[]
    for n in range(1,6):
        s=(LOG/f'2026-09-10-stage-15-level-{n:02}.md').read_text()
        ids=re.findall(r'^## (E\d{2}) — ',s,re.M)
        primaries+=ids
        counts.append(len(ids))
    check('Fifteen accepted primary examples preserved',primaries==[f'E{n:02}' for n in range(1,16)] and counts==[3]*5,{'ids':primaries,'distribution':counts})

    A,B,C=corpus['cases']
    a=A['base_inputs']['observations']
    gross=D(a['monthly_price'])*(a['old_paid_renewals']+a['new_paid_accounts'])
    net=gross-D(a['refunds_paid'])
    costs=D(a['entitled_accounts_charged_service_cost'])*D(a['service_cost_per_entitled_account'])+D(a['support_cash'])+D(a['payment_fees'])
    contribution=net-costs
    close,low,acalendar=cash(a['opening_usable_cash'],A['base_inputs']['scenarios']['cash_events'])
    am={'paid_renewal_percent':D(a['old_paid_renewals'])/D(a['old_accounts_due'])*100,'entitlement_percent':D(a['old_paid_renewals']+a['grace_entitlements'])/D(a['old_accounts_due'])*100,'review_percent':D(a['old_accounts_completing_weekly_review'])/D(a['old_accounts_due'])*100,'gross':gross,'net':net,'direct_cost':costs,'contribution':contribution,'residual':contribution-D(a['fixed_hosting_cash'])-D(a['acquisition_cash']),'cash_min':low,'cash_close':close,'floor_gap':D(a['cash_floor'])-low,'annual_candidate':D(A['base_inputs']['scenarios']['candidate_annual_price']),'twelve_monthly':D(a['monthly_price'])*12}
    b=B['base_inputs']['observations']; bs=B['base_inputs']['scenarios']
    shared=D(b['monthly_admin_learning_hours'])+D(b['monthly_content_hours'])+D(b['monthly_pipeline_hours'])
    ph=D(b['project_delivery_hours'])+D(b['project_follow_up_hours'])
    rh=D(bs['retainer_reserved_delivery_hours'])+D(bs['retainer_support_hours'])
    bclose,blow,bcalendar=cash(b['opening_usable_cash'],[['day-00','deposit',b['deposit_collected_day_0']],['day-00','tools',-D(b['cash_tool_cost_per_engagement'])],['day-15','draw',-D(bs['owner_draw_day_15'])],['day-45','draw',-D(bs['owner_draw_day_45'])],['day-60','contingent_balance',b['balance_due_day_60']]])
    bm={'one_project_hours':ph+shared,'two_projects_hours':2*ph+shared,'two_projects_overload':2*ph+shared-D(b['available_month_hours']),'one_retainer_hours':rh+shared,'two_retainers_hours':2*rh+shared,'two_retainers_overload':2*rh+shared-D(b['available_month_hours']),'project_residual':D(b['project_price'])-D(b['cash_tool_cost_per_engagement'])-(ph+shared)*D(b['owner_hour_value']),'retainer_residual':D(bs['retainer_price_per_month'])-D(b['cash_tool_cost_per_engagement'])-(rh+shared)*D(b['owner_hour_value']),'cash_min':blow,'cash_close':bclose,'floor_gap':D(b['cash_floor'])-blow}
    c=C['base_inputs']['observations']; cs=C['base_inputs']['scenarios']
    service=D(c['paid_service_customers'])*D(c['service_price'])
    maintenance=D(c['maintenance_hours'])*D(c['hour_value'])
    work=D(c['maintenance_hours'])+D(c['paid_service_customers'])*D(c['service_hours_each'])+D(c['support_hours'])+D(c['pack_review_hours'])
    total=D(c['opening_unrestricted_cash'])+service+D(c['restricted_sponsorship'])
    restricted=D(c['restricted_sponsorship']); invoice=D(cs['eligible_maintenance_invoice'])
    cm={'service_revenue':service,'valued_maintenance':maintenance,'maintenance_funding_gap':maintenance-restricted,'work_hours':work,'overload':work-D(c['maintainer_capacity_hours']),'valued_work':work*D(c['hour_value']),'valued_cost_with_hosting':work*D(c['hour_value'])+D(c['hosting_cash']),'services_plus_restricted_sponsor':service+restricted,'support_revenue':D(cs['support_paid_subscribers'])*D(cs['support_price_per_month']),'cash_total_before_invoice':total,'cash_restricted_before_invoice':restricted,'cash_usable_before_invoice':total-restricted,'cash_total_after_invoice':total-invoice,'cash_restricted_after_invoice':restricted-invoice,'cash_usable_after_invoice':total-invoice-(restricted-invoice)}
    for case,metrics in [(A,am),(B,bm),(C,cm)]:
        check(case['id']+' full reference metric set',set(metrics)==set(case['expected_base_metrics']),sorted(metrics))
        for k,v in metrics.items():
            eq(case['id']+' '+k,v,case['expected_base_metrics'][k])
    a2=A['variants'][1]['fixture_extension']
    eq('A02 eligible request processing percent',D(a2['processed_requests'])/D(a2['eligible_requests'])*100,'20')
    eq('A02 isolated outstanding exposure',D(a2['eligible_requests']-a2['processed_requests'])*D(a2['purchase_amount']),'48')
    a5=A['variants'][4]['fixture_extension']; delta=D(a5['acquisition_cash'])-D(a['acquisition_cash'])
    for k,actual,expected in [('residual',am['residual']-delta,'-1600'),('trough',low-delta,'-1930'),('close',close-delta,'-600'),('floor_gap',D(a['cash_floor'])-(low-delta),'2130')]: eq('A05 '+k,actual,expected)
    b1=B['variants'][0]['fixture_extension']; callhours=D(b1['proposed_additional_discovery_calls'])*D(b1['assumed_hours_each'])
    eq('B01 extra call workload',callhours,'18'); eq('B01 combined workload',bm['one_project_hours']+callhours,'132')
    eq('B01 nominal additional-call ceiling',(D(b['available_month_hours'])-bm['one_project_hours'])//D(b1['assumed_hours_each']),'4')
    eq('B02 hypothetical two-project gross',D(b['project_price'])*2,'18000')
    b4=B['variants'][3]['fixture_extension']; discounted=D(b4['discounted_project_price'])
    eq('B04 discount amount',D(b['project_price'])*(1-D(b4['discount_percent'])/100),discounted)
    eq('B04 full valued residual',discounted-D(b['cash_tool_cost_per_engagement'])-bm['one_project_hours']*D(b['owner_hour_value']),'-1640')
    yield_rate=(discounted-D(b['cash_tool_cost_per_engagement']))/bm['one_project_hours']
    check('B04 effective-rate numerical bound',D('45.614035') < yield_rate < D('45.614036'),str(yield_rate))
    b5=B['variants'][4]['fixture_extension']; eq('B05 unknown-eligibility remainder',B['base_inputs']['scenarios']['outbound_list_size']-b5['stipulated_suppressed_records'],'42')
    c3=C['variants'][2]['fixture_extension']; eq('C03 unsupported volunteered-hours assumption',D(c['contributors'])*D(c3['assumed_volunteer_hours_each']),'48')
    c4=C['variants'][3]['fixture_extension']; additional=sum(D(x) for x in c4['additional_planning_hours'].values())
    eq('C04 additional assumed hours',additional,'38'); eq('C04 workload lower bound',work+additional,'122'); eq('C04 overload lower bound',work+additional-D(c['maintainer_capacity_hours']),'42')
    forecast=D(c4['support_forecast_customers'])*D(c4['support_price'])+D(c4['course_forecast_seats'])*D(c4['course_price'])+D(c4['marketplace_forecast_transactions'])*D(c4['transaction_price'])*D(c4['take_rate'])
    eq('C04 unvalidated incremental commercial forecast',forecast,'1400')
    eq('C04 mixed commercial/funding scenario',service+restricted+forecast,'5000')
    for bad in [True,1.5,'NaN','Infinity','not-a-number']:
        try: D(bad); rejected=False
        except ValueError: rejected=True
        check('Calculator rejects invalid/non-finite '+repr(bad),rejected,repr(bad))
    check('No premature production directories',all(not (ROOT/p).exists() for p in ['skills','examples','benchmarks','tests','tools','extension-packs','integrations','.github']), 'Only bootstrap research workspace')
    docs=[LOG/(PREFIX+'-stress-test-design.md')]+[ROOT/c['output_path'] for c in corpus['cases']]+[LOG/'bootstrap-3-progress.md']
    missing=[]
    for doc in docs:
        if not doc.is_file(): missing.append(str(doc)); continue
        for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)',doc.read_text()):
            if re.match(r'^[a-z]+:',target) or target.startswith('#'): continue
            path=(doc.parent/target.split('#',1)[0]).resolve()
            if not path.is_file(): missing.append(str(path))
    check('All new local documentation links resolve',not missing,missing)
    inputs={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [LOG/(PREFIX+'-cases.json'),Path(__file__)]+docs if p.is_file()}
    results={'stage':16,'scope':'structural/arithmetic/preservation design verification only; semantic design review is recorded separately','python':platform.python_version(),'starting_head':corpus['starting_head'],'inputs_sha256':inputs,'summary':{'PASS':sum(c['result']=='PASS' for c in checks),'FAIL':sum(c['result']=='FAIL' for c in checks)},'cash_calendars':{'A':acalendar,'B':bcalendar},'checks':checks}
    OUT.write_text(json.dumps(results,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps({'stage':16,**results['summary'],'python':results['python'],'output':str(OUT)}))
    return 1 if results['summary']['FAIL'] else 0

if __name__=='__main__':
    try:
        sys.exit(main())
    except Exception as exc:
        OUT.write_text(json.dumps({'stage':16,'state':'ERROR','error':type(exc).__name__+': '+str(exc),'checks':checks},indent=2)+'\n')
        raise
