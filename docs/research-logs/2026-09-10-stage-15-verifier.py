#!/usr/bin/env python3
"""Stage 15 design integrity and original synthetic arithmetic. No network or agent calls."""
from __future__ import annotations
import argparse, copy, hashlib, json, re, sys
from decimal import Decimal, InvalidOperation, localcontext, ROUND_FLOOR
from fractions import Fraction
from pathlib import Path

PREFIX='2026-09-10-stage-15-'
LEVELS=['Validate one bounded business decision','Build one coherent commercial component','Design one complete small business model','Diagnose and repair an existing business','Full business-building thesis']
COVERAGE_LINES=['B2B / B2C','subscription / transaction / services','self-serve / sales-assisted','paid / organic / outbound / referral acquisition','low / high ticket','short / long sales cycle','digital / human delivery','retention-dependent / one-off','cash-light / working-capital-sensitive','offer design','pricing','money model','lead generation','sales','delivery','retention','unit economics','experimentation','legal/ethical boundaries','constraint diagnosis']
ATOMS={'B2B','B2C','subscription','transaction','services','self-serve','sales-assisted','paid acquisition','organic acquisition','outbound acquisition','referral acquisition','low ticket','high ticket','short sales cycle','long sales cycle','digital delivery','human delivery','retention-dependent','one-off','cash-light','working-capital-sensitive','offer design','pricing','money model','lead generation','sales','delivery','retention','unit economics','experimentation','legal/ethical boundaries','constraint diagnosis'}
SELECTED=[1,2,3,7,8,9,13,14,15,19,20,21,25,26,27]
COMMANDS={
'business-build':{'frame-opportunity','define-customer-value','design-offer','design-pricing','design-money-model','model-delivery','model-unit-economics','identify-assumptions','design-experiment','record-learning'},
'business-grow':{'select-channel','design-acquisition','design-referral-loop','design-sales-path','improve-conversion','design-retention','design-expansion','scale-channel'},
'business-evaluate':{'audit-customer-evidence','evaluate-component','evaluate-unit-economics','evaluate-experiment','audit-claims','diagnose-business-constraint','recommend-smallest-change'},
'business-pack-author':{'inspect-catalogue','research-business-model','define-specialisation','build-showcase','build-evals','compare-core-vs-pack','validate-pack'}}
MODES={'design-acquisition':{'lead-magnet','outreach','content-loop'},'evaluate-component':{'opportunity','offer','pricing','money-model','channel','funnel','retention'},'evaluate-unit-economics':{'economics','cash','both'}}
SECTIONS=['Exact copyable prompt','Expected artefacts','Discriminating acceptance','Negative control','Preservation and smallest responsible repair']
KNOWN={'2026-09-08-business-building-skills-new-project-bootstrap-process.md','2026-09-09-bootstrap-2-execution-contract.md'}

def digest(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode()).hexdigest()

def number(value):
    if isinstance(value,bool) or not isinstance(value,(str,int)):
        raise ValueError('Use finite decimal strings or integer counts')
    try: result=Decimal(value)
    except InvalidOperation as exc: raise ValueError('Invalid decimal input') from exc
    if not result.is_finite(): raise ValueError('Non-finite value')
    return result

def fmt(value):
    return format(value.normalize(),'f') if isinstance(value,Decimal) else value

def serial(value):
    if isinstance(value,dict): return {k:serial(v) for k,v in value.items()}
    if isinstance(value,(list,tuple)): return [serial(v) for v in value]
    return fmt(value)

def percent(n,d):
    # Calculated internal Decimals retain precision; raw values keep strict validation.
    def operand(value):
        return number(str(value)) if isinstance(value, Decimal) else number(value)
    n,d=operand(n),operand(d)
    if d<=0: raise ValueError('Undefined denominator')
    return n/d*100

def cash(opening,events,floor):
    balance=number(opening); floor=number(floor); values=[balance]; seen=set(); last=-1
    first=None
    for date,identity,amount in events:
        if not re.fullmatch(r'day-\d{2}',date): raise ValueError('Invalid relative day')
        day=int(date[4:])
        if day<last: raise ValueError('Cash dates are not ordered')
        if not identity or identity in seen: raise ValueError('Duplicate cash identity')
        seen.add(identity);last=day;balance+=number(amount);values.append(balance)
        if first is None and balance<floor:first=date
    return {'closing':balance,'minimum':min(values),'floor_gap':max(Decimal(0),floor-min(values)),'first_breach':first}

def parse_examples(text,level):
    marks=list(re.finditer(r'^## (E\d{2}) — (.+)$',text,re.M)); records=[]
    for i,m in enumerate(marks):
        block=text[m.end():marks[i+1].start() if i+1<len(marks) else len(text)]
        prompts=re.findall(r'^```text\n(.*?)\n```',block,re.S|re.M)
        def field(name):
            hit=re.search(r'^\*\*'+re.escape(name)+r':\*\* (.+)$',block,re.M)
            return hit[1].strip() if hit else ''
        prompt=prompts[0] if len(prompts)==1 else ''
        facts=None
        if 'Facts (JSON):\n' in prompt:
            try:facts,_=json.JSONDecoder().raw_decode(prompt.split('Facts (JSON):\n',1)[1])
            except json.JSONDecodeError:pass
        command_match=re.search(r'Use these logical selectors as needed: (.+)\.\n\nFacts',prompt)
        commands=command_match[1].split(', ') if command_match else []
        records.append({'id':m[1],'title':m[2],'file_level':level,'level':field('Level'),'candidate':field('Candidate'),'coverage':field('Coverage').split('; '),'capabilities':field('Capability trace').split(', '),'prompt':prompt,'prompt_count':len(prompts),'facts':facts,'commands':commands,'block':block})
    return records

def issues(records,pool):
    errors=[]; bycp={c['id']:c for c in pool['candidates']}
    ids=[r['id'] for r in records]
    if ids!=[f'E{i:02d}' for i in range(1,16)]:errors.append('example identity/count/order')
    if [sum(r['level']==str(l) for r in records) for l in range(1,6)]!=[3]*5:errors.append('3/3/3/3/3 distribution')
    for i,r in enumerate(records):
        c=bycp.get(r['candidate']); f=r['facts']
        if i>=15 or r['candidate']!=f'CP{SELECTED[i]:02d}':errors.append('selected candidate mapping')
        if not c or r['title']!=c['title'] or r['level']!=str(c['level']) or r['file_level']!=c['level']:errors.append('title/depth/candidate integrity')
        if not c or r['coverage']!=c['coverage'] or r['capabilities']!=c['capabilities']:errors.append('coverage/capability trace')
        if r['prompt_count']!=1 or len(r['prompt'])<500:errors.append('complete exact prompt')
        if not isinstance(f,dict) or f.get('synthetic') is not True or f.get('case_version')!=r['id']+'-v1' or f.get('currency')!='GBP':errors.append('fixed synthetic input identity')
        if not isinstance(f,dict) or len(f.get('accepted_versions',{}))<2 or not f.get('unknowns'):errors.append('preserved baseline and unknowns')
        if not all('### '+s in r['block'] for s in SECTIONS):errors.append('complete case responsibilities')
        if not r['commands']:errors.append('command selection absent')
        for command in r['commands']:
            m=re.fullmatch(r'([^/]+)/([^\s]+)(?: \[([^]]+)\])?',command)
            if not m or m[2] not in COMMANDS.get(m[1],set()):errors.append('unknown canonical command');continue
            if m[2] in MODES and m[3] not in MODES[m[2]]:errors.append('missing/unknown required mode')
            if m[2] not in MODES and m[3]:errors.append('unrecognised mode')
        if not all(t in r['prompt'] for t in ['Use core behaviour without requiring an Extension Pack','Do not contact people','Keep missing evidence unknown','Task:']):errors.append('evidence and external-effect boundary')
    if set().union(*(set(r['coverage']) for r in records))!=ATOMS:errors.append('all atomic coverage values')
    if set().union(*(set(r['capabilities']) for r in records))!={f'C{i:02d}' for i in range(1,23)}:errors.append('C01–C22 coverage')
    return errors

def calculate(case,f):
    o=f.get('observations',f.get('scenario_inputs',{}));s=f.get('scenarios',{})
    n=lambda key:number(o[key])
    v=lambda key:number(s[key])
    if case=='E01':
        h=list(map(number,o['past_job_hours']));cost=[x*n('labour_value_per_hour')+n('other_direct_cost_per_job') for x in h]
        return {'fixed_contribution':[v('fixed_fee')-c for c in cost],'hourly_consideration':[x*v('hourly_price') for x in h],'hourly_contribution':[x*v('hourly_price')-c for x,c in zip(h,cost)],'fixed_hours_boundary':str(Fraction(v('fixed_fee')-n('other_direct_cost_per_job'))/Fraction(n('labour_value_per_hour')))}
    if case=='E02':
        result={}
        for name in ['paid','referral']:
            q=o[name];spend=number(q.get('media_cash',q.get('reward_cash')))+number(q['sales_cost']);customers=number(q['paid_customers'])
            result[name]={'CAC':spend/customers,'cohort_after_acquisition':customers*n('contribution_per_customer_before_acquisition')-spend,'qualified_pct':percent(q['qualified'],q['responses']),'paid_pct':percent(q['paid_customers'],q['responses'])}
        return result
    if case=='E03':
        gross=n('orders')*n('price');net=gross-n('discounts')-n('refund_amount');k=sum(n(x) for x in ['payment_fees','support_cost','distribution_cost'])
        return {'gross':gross,'net':net,'direct_cost':k,'contribution':net-k,'creation_inclusive_residual':net-k-n('creation_cost')}
    if case=='E04':
        h=v('delivery_hours')+v('discovery_admin_support_hours');k=h*n('labour_value_per_hour')+v('tool_cash')
        if k!=v('delivery_cash_day_14'):raise ValueError('Cost/cash source bridge mismatch')
        return {'hours':h,'direct_cost':k,'standard_contribution':v('fee')-k,'discount_contribution':v('discounted_fee')-k,'nominal_engagement_bound':int(((n('available_month_hours')-n('existing_work_hours'))/h).to_integral_value(rounding=ROUND_FLOOR)),'cash':cash(o['opening_usable_cash'],[['day-00','deposit',s['deposit_day_0']],['day-14','delivery',str(-k)],['day-30','balance',s['balance_day_30']]],o['cash_floor'])}
    if case=='E05':
        seq=[o[k] for k in ['downloads','fit_downloaders','follow_up_permitted','call_requests','calls_attended','qualified_proposals','paid_customers']]
        if any(a<b for a,b in zip(seq,seq[1:])):raise ValueError('Funnel subset mismatch')
        a=n('content_acquisition_cost')+n('sales_hours')*n('sales_hourly_cost');c=n('paid_customers')*(n('price')-n('direct_delivery_cost'))
        return {'sales_cost':n('sales_hours')*n('sales_hourly_cost'),'acquisition_cost':a,'contribution_before_acquisition':c,'after_acquisition':c-a,'permitted_follow_up':o['follow_up_permitted']}
    if case=='E06':
        due=n('renewals_due');paid=n('paid_renewals');grace=n('grace_entitlements')
        if paid+n('voluntary_exits')+n('failed_payments')!=due or grace>n('failed_payments'):raise ValueError('Renewal state mismatch')
        gross=paid*n('price');net=gross-n('cohort_refunds');service=(paid+grace)*n('service_cost_per_entitled_account');k=service+n('cohort_support_cost')+n('cohort_payment_fees')
        return {'paid_renewal_pct':percent(paid,due),'entitlement_pct':percent(paid+grace,due),'meaningful_use_pct':percent(o['meaningful_users_in_starting_cohort'],due),'gross':gross,'net':net,'service_cost':service,'direct_cost':k,'contribution':net-k}
    if case=='E07':
        visit=n('service_hours_per_visit')+n('travel_setup_hours_per_visit');qty=v('monthly_visits');available=v('working_days_per_month')*v('available_hours_per_day');h=qty*visit+v('non_visit_hours_per_month');cashcost=qty*(n('materials_cash_per_visit')+n('travel_cash_per_visit'));receipts=qty*n('price');availablecash=receipts-cashcost-v('monthly_overhead_cash');maxvisits=int(((available-v('non_visit_hours_per_month'))/visit).to_integral_value(rounding=ROUND_FLOOR))
        return {'visit_hours':visit,'month_hours':h,'receipts':receipts,'variable_cash_cost':cashcost,'cash_after_overhead':availablecash,'full_valued_residual':availablecash-h*v('owner_time_value_per_hour'),'whole_visit_bound':maxvisits,'max_visit_cash_after_overhead':maxvisits*(n('price')-n('materials_cash_per_visit')-n('travel_cash_per_visit'))-v('monthly_overhead_cash')}
    if case=='E08':
        accounts=n('light_accounts')+n('heavy_accounts')
        if accounts!=n('accounts_renewed')+n('new_paid_accounts'):raise ValueError('Account identity mismatch')
        revenue=accounts*n('price_per_account');k=n('light_accounts')*n('light_usage_cost')+n('heavy_accounts')*n('heavy_usage_cost')+accounts*(n('support_cost_per_account')+n('payment_fee_per_account'));kd=k+n('heavy_accounts')*(v('heavy_usage_cost_downside')-n('heavy_usage_cost'))
        return {'consideration':revenue,'direct_cost':k,'contribution':revenue-k,'after_fixed_acquisition':revenue-k-n('fixed_platform_cost')-n('acquisition_cost_for_new_accounts'),'heavy_contribution_each':n('price_per_account')-n('heavy_usage_cost')-n('support_cost_per_account')-n('payment_fee_per_account'),'downside_heavy_each':n('price_per_account')-v('heavy_usage_cost_downside')-n('support_cost_per_account')-n('payment_fee_per_account'),'downside_contribution':revenue-kd,'downside_residual':revenue-kd-n('fixed_platform_cost')-n('acquisition_cost_for_new_accounts'),'renewal_pct':percent(o['accounts_renewed'],o['accounts_due_to_renew']),'old_use_pct':percent(o['meaningful_old_accounts'],o['accounts_due_to_renew']),'CAC_fraction':str(Fraction(n('acquisition_cost_for_new_accounts'))/Fraction(n('new_paid_accounts')))}
    if case=='E09':
        gross=n('orders')*n('price');net=gross-n('refund_amount');consumed=n('orders')*n('unit_stock_cost');k=consumed+n('orders')*n('shipping_per_order')+n('payment_fees')+n('refunded_orders')*n('return_handling_per_refund');remaining=(n('units_bought')-n('orders'))*n('unit_stock_cost');cf=cash(o['opening_usable_cash'],s['cash_events'],o['cash_floor'])
        if cf['closing']!=n('opening_usable_cash')+net-k-n('ad_acquisition_cash')-remaining:raise ValueError('Stock/cash reconciliation failed')
        return {'gross':gross,'net':net,'consumed_stock':consumed,'direct_cost':k,'contribution':net-k,'after_acquisition':net-k-n('ad_acquisition_cash'),'remaining_units':int(n('units_bought')-n('orders')),'remaining_stock_cost':remaining,'cash':cf}
    if case=='E10':
        result={}
        for name in ['A','B']:
            q=o[name];a=number(q['ad_cash'])+number(q['sales_hours'])*n('sales_hourly_cost');paid=number(q['paid_customers']);result[name]={'qualified_pct':percent(q['qualified'],q['leads']),'qualified_to_paid_pct':percent(paid,q['qualified']),'all_in_CAC':a/paid,'after_acquisition':paid*n('contribution_per_customer_before_acquisition')-a}
        return result
    if case=='E11':
        result={}
        for label,q in [('current',n('current_accepted_engagements')),('proposed',v('proposed_total_engagements'))]:
            N=q*n('price');K=q*((n('delivery_hours_each')+n('support_hours_each'))*n('labour_value_per_hour')+n('other_direct_cost_each'));A=q*n('sales_hours_each')*n('labour_value_per_hour');H=n('fixed_admin_hours')*n('labour_value_per_hour');hours=q*(n('delivery_hours_each')+n('support_hours_each')+n('sales_hours_each'))+n('fixed_admin_hours');result[label]={'hours':hours,'headroom':n('available_hours')-hours,'N':N,'K':K,'C':N-K,'A':A,'H':H,'residual':N-K-A-H}
        return result
    if case=='E12':
        def model(q,deposit):
            total=q*n('price_per_order');events=[]
            if deposit:events.append(['day-00','deposit',str(q*deposit)])
            events += [['day-00','stock',str(-q*n('stock_cash_per_order_day_0'))],['day-00','advertising',str(-q*n('advertising_cash_per_order_day_0'))],['day-14','payroll',str(-q*n('payroll_cash_per_order_day_14'))],['day-30','tax',str(-n('tax_cash_day_30'))],['day-45','remaining_collection',str(total-q*deposit)]]
            return cash(o['opening_usable_cash'],events,o['cash_floor'])
        return {'base':model(n('accepted_orders'),Decimal(0)),'agreed_deposit_scenario':model(n('accepted_orders'),v('deposit_each_if_agreed_day_0')),'reduced_orders':model(v('reduced_orders'),Decimal(0)),'total_deposit':n('accepted_orders')*v('deposit_each_if_agreed_day_0'),'remaining_collection':n('accepted_orders')*(n('price_per_order')-v('deposit_each_if_agreed_day_0'))}
    if case=='E13':
        paid=n('old_paid_renewals')+n('new_paid_accounts');gross=paid*n('monthly_price');net=gross-n('refunds_paid');k=n('entitled_accounts_charged_service_cost')*n('service_cost_per_entitled_account')+n('support_cash')+n('payment_fees')
        if n('new_store_origin_accounts')+n('new_direct_origin_accounts')!=n('new_paid_accounts'):raise ValueError('Acquisition origin mismatch')
        if paid+n('grace_entitlements')!=n('entitled_accounts_charged_service_cost'):raise ValueError('Entitlement mismatch')
        return {'old_paid_renewal_pct':percent(o['old_paid_renewals'],o['old_accounts_due']),'old_entitlement_pct':percent(n('old_paid_renewals')+n('grace_entitlements'),o['old_accounts_due']),'old_review_pct':percent(o['old_accounts_completing_weekly_review'],o['old_accounts_due']),'gross':gross,'net':net,'direct_cost':k,'contribution':net-k,'residual':net-k-n('fixed_hosting_cash')-n('acquisition_cash'),'cash_scenario':cash(o['opening_usable_cash'],s['cash_events'],o['cash_floor']),'twelve_monthly_payments':n('monthly_price')*12,'proposed_annual_payment':v('candidate_annual_price')}
    if case=='E14':
        shared=n('monthly_admin_learning_hours')+n('monthly_content_hours')+n('monthly_pipeline_hours');project=n('project_delivery_hours')+n('project_follow_up_hours');retainer=v('retainer_reserved_delivery_hours')+v('retainer_support_hours');events=[['day-00','deposit',o['deposit_collected_day_0']],['day-07','tools',str(-n('cash_tool_cost_per_engagement'))],['day-15','owner_draw_1',str(-v('owner_draw_day_15'))],['day-45','owner_draw_2',str(-v('owner_draw_day_45'))],['day-60','balance',o['balance_due_day_60']]]
        return {'one_project_hours':project+shared,'two_project_hours':2*project+shared,'one_retainer_hours':retainer+shared,'two_retainer_hours':2*retainer+shared,'one_project_full_valued_residual':n('project_price')-(project+shared)*n('owner_hour_value')-n('cash_tool_cost_per_engagement'),'one_retainer_full_valued_residual':v('retainer_price_per_month')-(retainer+shared)*n('owner_hour_value')-n('cash_tool_cost_per_engagement'),'cash_scenario':cash(o['opening_usable_cash'],events,o['cash_floor'])}
    if case=='E15':
        revenue=n('paid_service_customers')*n('service_price');maintenance=n('maintenance_hours')*n('hour_value');hours=n('maintenance_hours')+n('paid_service_customers')*n('service_hours_each')+n('support_hours')+n('pack_review_hours');usable=n('opening_unrestricted_cash')+revenue;restricted=n('restricted_sponsorship');total=usable+restricted;invoice=v('eligible_maintenance_invoice')
        if invoice>restricted:raise ValueError('Restricted settlement exceeds supplied reserve')
        return {'service_revenue':revenue,'valued_maintenance':maintenance,'maintenance_gap_after_sponsor':maintenance-restricted,'hours':hours,'capacity_headroom':n('maintainer_capacity_hours')-hours,'valued_cost_plus_hosting':hours*n('hour_value')+n('hosting_cash'),'total_stated_funding':revenue+restricted,'cash_before':{'total':total,'restricted':restricted,'usable':usable},'cash_after_eligible_settlement':{'total':total-invoice,'restricted':restricted-invoice,'usable':total-invoice-(restricted-invoice)},'observed_support_revenue':v('support_paid_subscribers')*v('support_price_per_month')}
    raise ValueError('Unknown fixture')

EXPECTED={
'E01':{'fixed_contribution':['50','20','-40'],'hourly_consideration':['80','120','200'],'hourly_contribution':['10','20','40'],'fixed_hours_boundary':'11/3'},
'E02':{'paid':{'CAC':'150','cohort_after_acquisition':'60','qualified_pct':'10','paid_pct':'2'},'referral':{'CAC':'50','cohort_after_acquisition':'520','qualified_pct':'60','paid_pct':'20'}},
'E03':{'gross':'2400','net':'2310','direct_cost':'500','contribution':'1810','creation_inclusive_residual':'-190'},
'E04':{'hours':'32','direct_cost':'1360','standard_contribution':'440','discount_contribution':'-160','nominal_engagement_bound':1,'cash':{'closing':'940','minimum':'40','floor_gap':'160','first_breach':'day-14'}},
'E05':{'sales_cost':'300','acquisition_cost':'420','contribution_before_acquisition':'400','after_acquisition':'-20','permitted_follow_up':15},
'E06':{'paid_renewal_pct':'80','entitlement_pct':'85','meaningful_use_pct':'60','gross':'960','net':'936','service_cost':'170','direct_cost':'290','contribution':'646'},
'E07':{'visit_hours':'1.5','month_hours':'44','receipts':'2160','variable_cash_cost':'600','cash_after_overhead':'1400','full_valued_residual':'520','whole_visit_bound':26,'max_visit_cash_after_overhead':'1530'},
'E08':{'consideration':'1170','direct_cost':'405','contribution':'765','after_fixed_acquisition':'285','heavy_contribution_each':'3','downside_heavy_each':'-27','downside_contribution':'615','downside_residual':'135','renewal_pct':'80','old_use_pct':'60','CAC_fraction':'150/7'},
'E09':{'gross':'2000','net':'1900','consumed_stock':'800','direct_cost':'1080','contribution':'820','after_acquisition':'620','remaining_units':20,'remaining_stock_cost':'400','cash':{'closing':'920','minimum':'-900','floor_gap':'1000','first_breach':'day-00'}},
'E10':{'A':{'qualified_pct':'20','qualified_to_paid_pct':'20','all_in_CAC':'125','after_acquisition':'600'},'B':{'qualified_pct':'10','qualified_to_paid_pct':'20','all_in_CAC':'256.25','after_acquisition':'-450'}},
'E11':{'current':{'hours':'148','headroom':'-8','N':'12000','K':'5200','C':'6800','A':'320','H':'800','residual':'5680'},'proposed':{'hours':'180','headroom':'-40','N':'15000','K':'6500','C':'8500','A':'400','H':'800','residual':'7300'}},
'E12':{'base':{'closing':'4800','minimum':'-3200','floor_gap':'3700','first_breach':'day-00'},'agreed_deposit_scenario':{'closing':'4800','minimum':'500','floor_gap':'0','first_breach':None},'reduced_orders':{'closing':'3600','minimum':'-400','floor_gap':'900','first_breach':'day-14'},'total_deposit':'3700','remaining_collection':'4300'},
'E13':{'old_paid_renewal_pct':'70','old_entitlement_pct':'75','old_review_pct':'50','gross':'1440','net':'1380','direct_cost':'480','contribution':'900','residual':'-400','cash_scenario':{'closing':'600','minimum':'-730','floor_gap':'930','first_breach':'day-01'},'twelve_monthly_payments':'72','proposed_annual_payment':'60'},
'E14':{'one_project_hours':'114','two_project_hours':'184','one_retainer_hours':'92','two_retainer_hours':'140','one_project_full_valued_residual':'1960','one_retainer_full_valued_residual':'-720','cash_scenario':{'closing':'4800','minimum':'-1200','floor_gap':'1700','first_breach':'day-45'}},
'E15':{'service_revenue':'3000','valued_maintenance':'1200','maintenance_gap_after_sponsor':'600','hours':'84','capacity_headroom':'-4','valued_cost_plus_hosting':'3600','total_stated_funding':'3600','cash_before':{'total':'4600','restricted':'600','usable':'4000'},'cash_after_eligible_settlement':{'total':'4200','restricted':'200','usable':'4000'},'observed_support_revenue':'0'}}

def main():
    parser=argparse.ArgumentParser();parser.add_argument('root',type=Path);parser.add_argument('--output',type=Path);args=parser.parse_args();log=args.root/'docs/research-logs'
    names=['candidate-pool.json','selection-and-coverage.md']+[f'level-{l:02d}.md' for l in range(1,6)]
    texts={n:(log/(PREFIX+n)).read_text(encoding='utf-8') for n in names};pool=json.loads(texts[names[0]]);results=[]
    def check(name,passed,detail=None):
        item={'name':name,'passed':bool(passed)}
        if detail is not None:item['detail']=detail
        results.append(item);print(('PASS' if passed else 'FAIL')+' | '+name)
    candidates=pool['candidates'];records=[]
    check('percentage accepts finite internal Decimal operands',percent(Decimal('85'),100)==Decimal('85'))
    try:
        percent(Decimal('NaN'),100)
    except ValueError:
        check('percentage rejects non-finite internal Decimal operands',True)
    else:
        check('percentage rejects non-finite internal Decimal operands',False)
    check('30 original candidates, six per level',len(candidates)==30 and [sum(c['level']==l for c in candidates) for l in range(1,6)]==[6]*5)
    check('all original level purposes preserved',pool['original_level_titles']==LEVELS)
    check('20 original coverage lines and 32 exact atomic values',list(pool['original_coverage_lines'])==COVERAGE_LINES and {v for a in pool['original_coverage_lines'].values() for v in a}==ATOMS and sum(map(len,pool['original_coverage_lines'].values()))==32)
    check('candidate identities and genuine alternatives retained',[c['id'] for c in candidates]==[f'CP{i:02d}' for i in range(1,31)] and all(c['scope'] and c['discriminating_failure'] and c['capabilities'] and set(c['coverage'])<=ATOMS for c in candidates))
    for level,title in enumerate(LEVELS,1):
        text=texts[f'level-{level:02d}.md'];rs=parse_examples(text,level);records+=rs
        check(f'Level {level}: exact purpose and three primary entries',text.startswith(f'# Stage 15: Level {level} — {title}') and len(rs)==3)
    found=issues(records,pool);check('all 15 complete self-contained contracts, prompts, commands and boundaries',not found,found)
    for r in records:
        check(r['id']+': exact prompt has fixed JSON, preserved versions, unknowns and all case sections',r['prompt_count']==1 and r['facts']['synthetic'] is True and bool(r['facts']['accepted_versions']) and bool(r['facts']['unknowns']) and all('### '+s in r['block'] for s in SECTIONS))
    check('all 32 coverage values have selected primary witnesses',set().union(*(set(r['coverage']) for r in records))==ATOMS)
    check('all C01–C22 responsibilities have selected witnesses',set().union(*(set(r['capabilities']) for r in records))=={f'C{i:02d}' for i in range(1,23)})
    selection=texts['selection-and-coverage.md'];rows=re.findall(r'^\| (CP\d{2}) \| (\d) \| ([^|]+) \| ([^|]+) \| (.+) \|$',selection,re.M)
    check('all 30 candidate dispositions retained with reasons',len(rows)==30 and all(len(reason.strip())>50 for _,_,_,_,reason in rows))
    check('selection rows agree with the fifteen actual entries',[(cp,state.strip()) for cp,_,_,state,_ in rows if state.strip().startswith('E')]==[(r['candidate'],r['id']) for r in records])
    coverage_rows=re.findall(r'^\| ([^|]+) \| ([^|]+) \| (E\d{2}[^|]*) \|$',selection,re.M)
    coverage_rows=[(original.strip(),atom.strip(),ids.strip()) for original,atom,ids in coverage_rows if atom.strip() in ATOMS]
    check('matrix supplies exact per-value evidence pointers',len(coverage_rows)==32 and all(re.findall(r'E\d{2}',ids)==[r['id'] for r in records if atom in r['coverage']] for _,atom,ids in coverage_rows))
    check('physical delivery is not inferred from a web shop', 'digital delivery' not in next(c for c in candidates if c['id']=='CP15')['coverage'] and 'scenario_inputs' in records[8]['facts'])
    check('full models and theses request all fifteen map concerns',all('Cover all fifteen business-map concerns:' in r['prompt'] for r in records if r['file_level'] in (3,5)))
    check('theses add alternatives and sequenced evidence/commitment programmes',all('Add a coherent thesis, rejected strategic alternatives' in r['prompt'] for r in records if r['file_level']==5))
    check('named project data remain explicitly synthetic',all('not' in r['prompt'] and r['facts']['synthetic'] is True for r in records[-3:]))
    allnames={PREFIX+n for n in names}|{PREFIX+'verifier.py',PREFIX+'conformance.md',PREFIX+'executed-checks.json'}|KNOWN
    links=[link.split('#')[0] for text in texts.values() for link in re.findall(r'\]\(([^)]+)\)',text) if not link.startswith(('https://','http://','#'))]
    check('all relative documentation targets resolve to new or inspected earlier files',all(link in allnames for link in links))
    outputs={}
    with localcontext() as ctx:
        ctx.prec=28
        for r in records:
            before=digest(r['facts'])
            try:
                actual=serial(calculate(r['id'],r['facts']));outputs[r['id']]=actual
                check(r['id']+': synthetic arithmetic and declared reconciliation match independent reference',actual==EXPECTED[r['id']],None if actual==EXPECTED[r['id']] else {'actual':actual,'expected':EXPECTED[r['id']]})
            except (ValueError,KeyError,ZeroDivisionError) as exc:
                check(r['id']+': calculation failed',False,str(exc))
            check(r['id']+': input and accepted versions unchanged',digest(r['facts'])==before)
    mutations=[]
    q=copy.deepcopy(records);q.pop();mutations.append(('missing primary example',q))
    q=copy.deepcopy(records);q[0]['id']='E02';mutations.append(('duplicate primary identity',q))
    q=copy.deepcopy(records);q[0]['level']='2';mutations.append(('wrong level distribution',q))
    q=copy.deepcopy(records);q[0]['prompt']='';mutations.append(('empty exact prompt',q))
    q=copy.deepcopy(records);q[0]['facts']['synthetic']=False;mutations.append(('unlabelled synthetic input',q))
    q=copy.deepcopy(records);q[0]['facts']['accepted_versions']={};mutations.append(('missing preservation baseline',q))
    q=copy.deepcopy(records);q[0]['commands']=['business-grow/send-every-email'];mutations.append(('invented command',q))
    q=copy.deepcopy(records);q[0]['commands']=['business-evaluate/evaluate-component [anything]'];mutations.append(('unknown evaluation mode',q))
    q=copy.deepcopy(records)
    for r in q:r['coverage']=[v for v in r['coverage'] if v!='B2C']
    mutations.append(('lost required coverage',q))
    for label,q in mutations:check('Negative mutation rejected: '+label,bool(issues(q,pool)))
    def rejects(fn):
        try:fn()
        except (ValueError,KeyError):return True
        return False
    check('non-finite, boolean, float and malformed numbers rejected',all(rejects(lambda x=x:number(x)) for x in ['NaN','Infinity','bad',True,0.1]))
    check('zero and negative denominators do not become valid rates',rejects(lambda:percent(10,0)) and rejects(lambda:percent(10,-1)))
    check('cash duplicate identities and reversed dates rejected',rejects(lambda:cash('100',[['day-01','x','-10'],['day-02','x','-10']],'0')) and rejects(lambda:cash('100',[['day-02','a','-10'],['day-01','b','-10']],'0')))
    q=copy.deepcopy(records[0]['facts']);del q['scenarios']['fixed_fee'];check('missing mandatory numeric input is not silently zero',rejects(lambda:calculate('E01',q)))
    report={'stage':15,'scope':'Design integrity and original synthetic arithmetic/input-preservation, not installed-agent, customer or professional validation.','python':sys.version.split()[0],'decimal_precision':28,'checks':results,'fixture_outputs':outputs,'coverage':{'candidate_pool':len(candidates),'primary_examples':len(records),'levels':5,'distribution':[sum(r['file_level']==l for r in records) for l in range(1,6)],'exact_prompts':sum(r['prompt_count'] for r in records),'original_coverage_lines':20,'atomic_coverage_values':len(ATOMS),'capabilities':22},'input_sha256':{PREFIX+n:hashlib.sha256((log/(PREFIX+n)).read_bytes()).hexdigest() for n in names},'verifier_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'total':len(results),'passed':sum(r['passed'] for r in results),'failed':sum(not r['passed'] for r in results)}
    if args.output:args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('COVERAGE '+json.dumps(report['coverage'],sort_keys=True));print('PYTHON '+report['python']);print(f"TOTAL {report['total']} | PASS {report['passed']} | FAIL {report['failed']}")
    return 0 if not report['failed'] else 1
if __name__=='__main__':sys.exit(main())
