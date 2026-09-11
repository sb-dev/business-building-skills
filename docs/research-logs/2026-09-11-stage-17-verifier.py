#!/usr/bin/env python3
from pathlib import Path
from decimal import Decimal
import json, sys
ROOT=Path(sys.argv[1]) if len(sys.argv)>1 else Path('.')
LOG=ROOT/'docs'/'research-logs'
if not LOG.exists(): LOG=ROOT
res=[]
def ck(n,c):
    ok=bool(c); res.append((n,ok)); print(('PASS' if ok else 'FAIL')+' | '+n)
def load(n): return json.loads((LOG/n).read_text())
D=load('2026-09-11-stage-17-deterministic-fixtures.json')
B=load('2026-09-11-stage-17-behavioural-fixtures.json')
A=load('2026-09-11-stage-17-adversarial-fixtures.json')
P=load('2026-09-11-stage-17-pack-fixtures.json')
R=load('2026-09-11-stage-17-regression-fixtures.json')
DET=[('D01', 'required artefact fields'), ('D02', 'arithmetic'), ('D03', 'unit-economics formulas'), ('D04', 'cash-flow calculations'), ('D05', 'funnel consistency'), ('D06', 'experiment decision rules'), ('D07', 'metric definitions'), ('D08', 'pack structure'), ('D09', 'prompt completeness'), ('D10', 'installation integrity')]
REASON=['customer evidence', 'problem importance', 'value coherence', 'offer strength', 'truthfulness', 'pricing logic', 'monetisation coherence', 'channel fit', 'lead quality', 'sales-path fit', 'delivery feasibility', 'retention logic', 'unit economics', 'cash robustness', 'experiment quality', 'constraint diagnosis']
BEH=[('B01', 'distinguishes facts from assumptions'), ('B02', 'asks research/tooling to verify external claims when needed'), ('B03', 'chooses cheap experiments before large commitments'), ('B04', 'does not invent market size / conversion / CAC data'), ('B05', 'checks delivery and economics before scaling'), ('B06', 'uses downstream quality when judging acquisition'), ('B07', 'diagnoses the current constraint'), ('B08', 'preserves validated decisions'), ('B09', 'recommends the smallest responsible change'), ('B10', 'flags legal/ethical concerns')]
ADV=[('A01', 'false scarcity'), ('A02', 'fake urgency'), ('A03', 'invented testimonials'), ('A04', 'unsupported guarantee'), ('A05', 'unsupported earnings / ROI claim'), ('A06', 'hidden renewal'), ('A07', 'spam outreach'), ('A08', 'vanity metrics'), ('A09', 'CAC without downstream quality'), ('A10', 'LTV without retention evidence'), ('A11', 'growth despite negative contribution margin'), ('A12', 'experiment with no falsifiable decision rule'), ('A13', 'scaling before delivery capacity'), ('A14', 'pricing test that changes several variables at once')]
PACK=[('P01', 'activation'), ('P02', 'non-activation'), ('P03', 'precedence'), ('P04', 'changed business behaviour'), ('P05', 'pack-specific metrics'), ('P06', 'negative / incompatible cases'), ('P07', 'core vs core+pack difference')]
ck('exact ten deterministic concerns',[x['requirement'] for x in D]==[x[1] for x in DET])
ck('exact ten behavioural concerns',[x['requirement'] for x in B]==[x[1] for x in BEH])
ck('exact fourteen adversarial concerns',[x['requirement'] for x in A]==[x[1] for x in ADV])
ck('exact seven pack concerns',[x['requirement'] for x in P]==[x[1] for x in PACK])
ck('exact 43 fixture cases',len(D)+len(B)+len(A)+len(P)+len(R)==43)
ck('unique fixture ids',len({x['id'] for group in [D,B,A,P,R] for x in group})==43)
covered=set(d for x in B+A for d in x.get('dimensions',[]))
ck('all sixteen reasoning dimensions covered',set(REASON)<=covered)
ck('all fixtures labelled synthetic',all(x.get('synthetic') is True for g in [D,B,A,P,R] for x in g))
# Deterministic reference graders
f={x['id']:x['fixture'] for x in D}
ck('D01 required fields',all(k in f['D01']['record'] for k in f['D01']['required']))
ck('D02 arithmetic',sum(Decimal(x) for x in f['D02']['values'])==Decimal(f['D02']['expected_sum']))
rev=Decimal(f['D03']['revenue']); cost=Decimal(f['D03']['direct_cost']); c=rev-cost
ck('D03 contribution',c==Decimal(f['D03']['expected_contribution']) and c/rev==Decimal(f['D03']['expected_margin']))
bal=Decimal(f['D04']['opening']); low=bal
for x in f['D04']['events']: bal+=Decimal(x); low=min(low,bal)
ck('D04 cash close and minimum',bal==Decimal(f['D04']['expected_close']) and low==Decimal(f['D04']['expected_low']))
ck('D05 funnel valid and invalid detected',all(a>=b for a,b in zip(f['D05']['stages'],f['D05']['stages'][1:])) and not all(a>=b for a,b in zip(f['D05']['invalid_stages'],f['D05']['invalid_stages'][1:])))
obs=f['D06']['observed_success']; dec='success' if obs>=f['D06']['success_min'] else ('failure' if obs<=f['D06']['failure_max'] else 'inconclusive')
ck('D06 frozen experiment rule',dec==f['D06']['expected_decision'] and f['D06']['failure_max']<f['D06']['inconclusive']<f['D06']['success_min'])
ck('D07 metric and zero denominator',Decimal(f['D07']['numerator'])/Decimal(f['D07']['denominator'])==Decimal(f['D07']['expected']) and f['D07']['zero_denominator_status']=='BLOCKED')
ck('D08 pack required structure',set(f['D08']['required'])<=set(f['D08']['record_fields']))
ck('D09 prompt completeness',all(t in f['D09']['prompt'] for t in f['D09']['required_terms']))
ck('D10 missing installation evidence blocks',f['D10']['installation_evidence'] is None and f['D10']['expected_status']=='BLOCKED')
ck('behaviour fixtures define required and forbidden behaviour',all(x['required_behaviour'] and x['forbidden_behaviour'] and x['expected_if_required_behaviour_missing']=='FAIL' for x in B))
ck('adversarial fixtures are hard failures',all(x['expected']=='FAIL' and x['hard_gate'] and x['repair'] for x in A))
ck('pack fixtures have negative controls',all(x['expected']=='PASS' and x['evidence'] and x['negative_control'] for x in P))
# preservation + regression
r1=next(x for x in R if x['id']=='R01'); rg=next(x for x in R if x['id']=='RG01')
ck('R01 broad rewrite fails',set(r1['bad_repair'])!=set(r1['expected_repair']) and r1['expected_bad']=='FAIL')
ck('R01 local channel repair passes',r1['expected_repair']==['channel'] and r1['expected_good']=='PASS')
ck('RG01 old output reproduces defect',set(rg['old_output']['changes'])==set(r1['bad_repair']) and rg['old_expected']=='FAIL')
ck('RG01 repaired output passes smallest case',rg['repaired_output']['changes']==['channel'] and rg['repaired_expected']=='PASS')
ck('RG01 retained permanently',rg['benchmark_added'] and 'permanent' in rg['retention'])
# Docs and original-list presence
docs=['2026-09-11-stage-17-benchmark-taxonomy.md','2026-09-11-stage-17-case-contracts.md','2026-09-11-stage-17-acceptance-gates.md','2026-09-11-stage-17-regression-policy.md','2026-09-11-stage-17-research-and-sources.md']
texts='\n'.join((LOG/d).read_text() for d in docs)
for _,x in DET+BEH+ADV+PACK: ck('documented: '+x,x in texts)
for x in REASON: ck('reasoning dimension documented: '+x,x in texts)
ck('six regression steps explicit',all(x in texts for x in ['escaped business-reasoning defect','diagnose owning layer','create smallest reproducible case','add benchmark','prove old behaviour fails','prove repaired behaviour passes','retain permanently']))
ck('no universal score acceptance','No single weighted score' in texts or 'no universal business-quality score' in texts)
report={'stage':17,'scope':'benchmark/fixture design integrity and reference-grader execution; not installed-agent performance','python':sys.version.split()[0],'total':len(res),'passed':sum(ok for _,ok in res),'failed':sum(not ok for _,ok in res),'coverage':{'deterministic':len(D),'reasoning_dimensions':len(REASON),'behavioural':len(B),'adversarial':len(A),'pack':len(P),'preservation_regression':len(R),'fixtures':len(D)+len(B)+len(A)+len(P)+len(R)},'checks':[{'name':n,'passed':ok} for n,ok in res]}
print('COVERAGE '+json.dumps(report['coverage'],sort_keys=True)); print('PYTHON '+report['python']); print(f"TOTAL {report['total']} | PASS {report['passed']} | FAIL {report['failed']}")
if len(sys.argv)>2: Path(sys.argv[2]).write_text(json.dumps(report,indent=2)+'\n')
sys.exit(0 if report['failed']==0 else 1)
