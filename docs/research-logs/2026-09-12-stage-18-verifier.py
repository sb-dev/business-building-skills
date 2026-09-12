#!/usr/bin/env python3
"""Verify Stage 18 specifications, exact adopted contracts and preservation.

This is documentation/identity verification, not an installed-agent benchmark,
new commercial experiment, actual pack comparison or clean installation test.
"""
from pathlib import Path
import hashlib,json,platform,re,sys,unicodedata

LOG=Path(__file__).resolve().parent
ROOT=LOG.parent.parent
PREFIX='2026-09-12-stage-18'
OUT=LOG/(PREFIX+'-executed-checks.json')
CHECKS=[]

def check(name,condition,evidence):
    CHECKS.append({'check':name,'result':'PASS' if condition else 'FAIL','evidence':evidence})

def blob(path):
    b=path.read_bytes()
    return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()

def sha(text):return hashlib.sha256(text.encode()).hexdigest()

def section(text,heading):
    return text.split(heading+'\n',1)[1].split('\n## ',1)[0]

def anchors(path):
    text=path.read_text();result=set(re.findall(r'<a\s+id="([^"]+)"',text));seen={};code=False
    for line in text.splitlines():
        if line.startswith('```'):code=not code;continue
        if code or not re.match(r'^#{1,6} ',line):continue
        title=re.sub(r'^#{1,6} ','',line).lower()
        title=re.sub(r'<[^>]+>','',title)
        # GitHub removes punctuation/symbols, keeps underscores/hyphens, and
        # converts each space; repeated-heading suffixes retain occurrence.
        title=''.join(c for c in title if c in ' _-' or not unicodedata.category(c).startswith(('P','S','C')))
        slug=title.replace(' ','-');n=seen.get(slug,0);seen[slug]=n+1
        result.add(slug+(f'-{n}' if n else ''))
    return result

def command_blocks(text):
    return {m[1]:m[2].strip() for m in re.finditer(r'^### ([BGEP]\d{2}) — `[^`]+`\n(.*?)(?=^### [BGEP]\d{2} — |^## |\Z)',text,re.M|re.S)}

def main():
    OUT.write_text(json.dumps({'stage':18,'state':'RUNNING'})+'\n')
    manifest=json.loads((LOG/(PREFIX+'-specification-contracts.json')).read_text())
    original=LOG/'2026-09-08-business-building-skills-new-project-bootstrap-process.md'
    check('Original governing specification identity',blob(original)==manifest['original_specification_blob'],blob(original))
    part=original.read_text().split('# 25. Stage 18 — Generate Six Canonical Specifications',1)[1].split('# 26. Stage 19',1)[0]
    required=re.findall(r'(0[1-6]-[a-z-]+\.md)',part)
    paths=manifest['required_files'];texts={p:(ROOT/p).read_text() for p in paths}
    check('Exactly six original canonical filenames',paths==['docs/'+n for n in required] and len(paths)==6,paths)
    check('No substituted extra canonical specification',sorted(p.name for p in (ROOT/'docs').glob('0[1-6]-*.md'))==required,required)
    responsibilities=[]
    for num,title,items in re.findall(r'## (0[1-6]) — ([^\n]+)\n\nOwns:\n\n```text\n(.*?)\n```',part,re.S):
        responsibilities.extend((num,item) for item in items.splitlines())
    actual=[(r['id'].split('-')[1],r['requirement']) for r in manifest['ownership_requirements']]
    check('All 60 literal ownership concerns',actual==responsibilities and len(actual)==60,{'actual':actual,'required':responsibilities})
    for r in manifest['ownership_requirements']:
        check(r['id']+' actual reviewed section',r['section'] in texts[r['path']] and len(r['substantive_review'])>60 and r['result']=='PASS',{'requirement':r['requirement'],'section':r['section'],'direct_review':r['substantive_review']})

    check('Complete 101-file predecessor manifest',len(manifest['inherited_files'])==101 and len({x['path'] for x in manifest['inherited_files']})==101,manifest['starting_head'])
    for f in manifest['inherited_files']:
        p=ROOT/f['path']
        if f['path']=='docs/research-logs/bootstrap-3-progress.md':p=LOG/'2026-09-12-bootstrap-3-progress-through-stage-17.md'
        actual=blob(p) if p.is_file() else None
        check('Preserved '+f['path'],actual==f['sha'],{'actual':actual,'expected':f['sha'],'preserved_path':str(p.relative_to(ROOT))})
    for f in manifest['sources']:
        check('Canonical source identity '+f['path'],blob(ROOT/f['path'])==f['sha'],f['sha'])

    canonical=texts[paths[2]];got=command_blocks(canonical);all_expected={}
    fields=['inputs','evidence required','assumptions allowed','output','allowed mutations','forbidden behaviour','metrics/evidence','failure states','legal/ethical boundaries']
    distribution=[]
    for family,number in [('build',10),('grow',8),('evaluate',7),('pack',7)]:
        p=LOG/f'2026-09-10-stage-13-{family}-command-contracts.md'
        blocks=command_blocks(p.read_text());distribution.append(len(blocks));all_expected.update(blocks)
        check(f'{family} exact command count',len(blocks)==number,number)
        for key,body in blocks.items():
            actual=got.get(key,'')
            for field in fields:
                expected=re.search(r'^\| '+re.escape(field)+r' \| (.+) \|$',body,re.M).group(1)
                m=re.search(r'^\| '+re.escape(field)+r' \| (.+) \|$',actual,re.M)
                check(f'{key} exact {field}',bool(m) and m[1]==expected,{'field':field,'sha256':sha(expected)})
            mode_rows=re.findall(r'^\| `([^`]+)` \| (.+) \|$',body,re.M)
            check(key+' exact mode obligations',mode_rows==re.findall(r'^\| `([^`]+)` \| (.+) \|$',actual,re.M),[x[0] for x in mode_rows])
    check('Exactly 32 canonical command blocks',set(got)==set(all_expected) and len(got)==32,sorted(got))
    check('Command distribution 10/8/7/7',distribution==[10,8,7,7],distribution)
    descriptions=re.search(r'```text\n(business-build:.*?)\n```',canonical,re.S).group(1)
    rows=re.findall(r'^(business-[a-z-]+): (.+)$',descriptions,re.M)
    check('Four exact metadata descriptions with valid lengths',len(rows)==4 and all(1<=len(n)<=64 and re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*',n) and 1<=len(d)<=1024 for n,d in rows),{n:len(d) for n,d in rows})

    domain=texts[paths[1]]
    for prefix,count in [('B',15),('CR',6),('E',9),('V',8),('O',14),('P',14),('D',7),('CH',13),('LQ',9),('SP',8),('DR',14),('UE',12),('CA',11),('HC',8),('GG',7),('AS',10),('EX',9),('LR',8),('CT',15),('RR',8),('HF',7)]:
        actual=re.findall(r'^\| ('+prefix+r'\d{2}) \|',domain,re.M)
        expected=[prefix+f'{i:02}' for i in range(1,count+1)]
        check(prefix+' complete domain table',actual==expected,{'actual':actual,'expected':expected})
    money_fields=['value exchange','payer','pricing unit','gross revenue','direct costs','margin','cash timing','retention dependency','capacity dependency','risk']
    models=re.findall(r'^### M(\d{2}): ([^\n]+)\n(.*?)(?=^### |\Z)',domain,re.M|re.S)
    check('All thirteen money-model cards',len(models)==13,[x[0] for x in models])
    for num,title,body in models:
        check('M'+num+' all ten business fields',all(re.search(r'^\| '+re.escape(f)+r' \| .+ \|$',body,re.M) for f in money_fields),title)
    handoffs=re.findall(r'^#### (LH\d{2}) — [^\n]+\n(.*?)(?=^#### |^## |\Z)',domain,re.M|re.S)
    check('All twenty specialist routes',len(handoffs)==20,[h[0] for h in handoffs])
    for id,body in handoffs:
        check(id+' trigger/question/constraint/repair',all(s in body for s in ['**Trigger and facts:**','**Question and owner:**','**Returned constraint and smallest repair:**','**Research basis:**']),id)
    check('Preparation is separate from sending','transmit it only when that communication is authorised' in domain,'HF05 packet authority')
    h=re.findall(r'^\| (H\d{2}) \|',canonical,re.M)
    check('All eight execution annotations',h==[f'H{i:02}' for i in range(1,9)],h)

    data=json.loads((LOG/'2026-09-12-stage-17-case-contracts.json').read_text());evaluation=texts[paths[3]]
    for key,expected in [('deterministic',10),('reasoning',16),('behaviour',10),('pack_dimensions',7),('regression',7)]:
        check(key+' exact named list retained',len(data[key])==expected and all(x['id']+' — '+x['requirement'] in evaluation for x in data[key]),expected)
        for row in data[key]:
            check(row['id']+' complete method/anchors retained',all(row[k] in evaluation for k in ['method','positive','negative']),row['requirement'])
    ids=[];levels=[0]*5
    for c in data['primary_cases']:
        ids.append(c['id']);levels[c['level']-1]+=1
        block=re.search(r'^### '+c['id']+r' — [^\n]+\n(.*?)(?=^### E\d{2} — |^## |\Z)',evaluation,re.M|re.S).group(1)
        exact=re.search(r'#### Exact copyable prompt\n\n```text\n(.*?)\n```',block,re.S).group(1)
        check(c['id']+' literal full prompt and identity',exact==c['exact_prompt'] and sha(exact)==c['prompt_sha256'],c['prompt_sha256'])
        for key in ['expected_artifacts','reference_findings','negative_control','preservation','applicability_rule']:
            check(c['id']+' full '+key,c[key] in block,sha(c[key]))
    check('All15 exact primaries',ids==[f'E{i:02}' for i in range(1,16)],ids)
    check('Primary distribution3/3/3/3/3',levels==[3,3,3,3,3],levels)
    stress=json.loads((LOG/'2026-09-12-stage-16-cases.json').read_text())
    check('Full stress annex pinned',blob(LOG/'2026-09-12-stage-16-cases.json')=='9dd91fd385401c2ebf03c2c473fc42d70fdf69ab' and '9dd91fd385401c2ebf03c2c473fc42d70fdf69ab' in evaluation,3)
    for c in stress['cases']:
        coverage=[r['requirement'] for r in c['coverage']];variants=[v['id'] for v in c['variants']]
        check('Stress '+c['id']+' complete coverage/instruction',all(r in evaluation for r in coverage) and c['stress_instruction'] in evaluation,coverage)
        check('Stress '+c['id']+' complete adversarial IDs',all(id in evaluation for id in variants),variants)
    check('Stress distribution9/11/9 and5/5/5',[len(c['coverage']) for c in stress['cases']]==[9,11,9] and [len(c['variants']) for c in stress['cases']]==[5,5,5],{'exercise':[len(c['coverage']) for c in stress['cases']],'overlays':[len(c['variants']) for c in stress['cases']]})
    check('Full Stage17 case annex pinned',blob(LOG/'2026-09-12-stage-17-case-contracts.json')=='926a5cf7c0989b6f685cd7c2331bcc66b8d39a05' and '926a5cf7c0989b6f685cd7c2331bcc66b8d39a05' in evaluation,'Complete case contracts, not abbreviated substitutes')
    for c in data['adversaries']:
        check(c['id']+' named pattern/findings/repair',c['requirement'] in evaluation and all(x.replace('|','/') in evaluation for x in c['required_findings']) and c['smallest_repair'].replace('|','/') in evaluation,c['requirement'])

    pack=texts[paths[4]];catalogue=texts[paths[5]]
    dims=re.findall(r'^\| (D\d{2}) \|',pack,re.M)
    check('All fourteen permitted pack dimensions',dims==[f'D{i:02}' for i in range(1,15)],dims)
    author=re.findall(r'^\| (A\d{2}) \|',pack,re.M)
    check('All eleven pack authoring steps',author==[f'A{i:02}' for i in range(1,12)],author)
    profile_blocks=re.findall(r'^### (PK\d{2}) — `([^`]+)`\n(.*?)(?=^### PK\d{2} — |^## |\Z)',catalogue,re.M|re.S)
    check('Nine complete profiles retained',len(profile_blocks)==9,[x[0] for x in profile_blocks])
    original_catalogue=(LOG/'2026-09-10-stage-14-candidate-catalogue.md').read_text()
    for pid,name,body in profile_blocks:
        origin=re.search(r'^### '+pid+r' — `[^`]+`\n(.*?)(?=^### PK\d{2} — |^## |\Z)',original_catalogue,re.M|re.S).group(1)
        fields=re.findall(r'^\| (D\d{2}) \| (.+) \|$',body,re.M)
        check(pid+' all fourteen exact dimension treatments',fields==re.findall(r'^\| (D\d{2}) \| (.+) \|$',origin,re.M) and len(fields)==14,14)
        effects=re.findall(r'^\| (PK\d{2}-E[123]) \| (.+) \|$',body,re.M)
        check(pid+' three exact command effects',effects==re.findall(r'^\| (PK\d{2}-E[123]) \| (.+) \|$',origin,re.M) and len(effects)==3,[x[0] for x in effects])
        check(pid+' complete fit/nonfit/comparison/status',all(x in body for x in ['**Fit:**','**Non-activation:**','**Core/catalogue comparison:**','**Implementation status:** NOT IMPLEMENTED.']),pid)
    check('Exactly eight independent and one advisory disposition',catalogue.count('**Design disposition:** RETAIN AS DESIGN CANDIDATE.')==8 and catalogue.count('**Design disposition:** MERGE INTO PROFESSIONAL-SERVICES ADVISORY MODE.')==1,{'independent':8,'mode':1})
    for p in data['pack_profiles']:
        block=re.search(r'^### '+p['probe']+r' — [^\n]+\n(.*?)(?=^### S\d{2} — |^## |\Z)',catalogue,re.M|re.S).group(1)
        actual=json.loads(re.search(r'#### Complete fixed input\n\n```json\n(.*?)\n```',block,re.S).group(1))
        prompt=re.search(r'#### Exact copyable prompt\n\n```text\n(.*?)\n```',block,re.S).group(1)
        check(p['probe']+' complete unchanged fixed input',actual==p['exact_source_fixture'],sha(json.dumps(actual,sort_keys=True)))
        check(p['probe']+' exact prompt',prompt==p['exact_source_fixture']['prompt'],sha(prompt))
        check(p['probe']+' specific metric/nonfit and comparison procedure',p['metric'] in block and p['nonfit'] in block and '**Evaluation procedure:**' in block and '**Comparison and repair:**' in block,p['effects'])

    documents=[ROOT/p for p in paths]+[LOG/(PREFIX+'-canonical-specifications.md'),LOG/'bootstrap-3-progress.md',LOG/'2026-09-12-bootstrap-3-progress-through-stage-17.md']
    missing=[];invalid_anchors=[];link_count=0;cache={}
    for p in documents:
        text=p.read_text();opened=None
        for line in text.splitlines():
            if line.startswith('```'):opened=None if opened is not None else line
        check(p.name+' balanced Markdown fences',opened is None,opened)
        for index,payload in enumerate(re.findall(r'^```json\n(.*?)\n```',text,re.M|re.S),1):
            try:json.loads(payload);valid=True
            except ValueError:valid=False
            check(p.name+f' valid JSON block {index}',valid,sha(payload))
        for target in re.findall(r'\[[^\]\n]*\]\(([^\s)]+)\)',text):
            if re.match(r'^[a-z]+:',target):continue
            link_count+=1;base,_,anchor=target.partition('#');resolved=(p.parent/base).resolve() if base else p
            if not resolved.is_file():missing.append({'source':p.name,'target':target});continue
            if anchor and resolved.suffix=='.md':
                if resolved not in cache:cache[resolved]=anchors(resolved)
                if anchor not in cache[resolved]:invalid_anchors.append({'source':p.name,'target':target})
    check('Every local documentation path resolves',not missing,{'links':link_count,'missing':missing})
    check('Every local documentation anchor resolves',not invalid_anchors,invalid_anchors)
    check('No premature production directories',all(not (ROOT/p).exists() for p in ['skills','examples','benchmarks','tests','tools','extension-packs','integrations','.github']), 'Specification and research files only')
    check('No production SKILL.md files',not list(ROOT.rglob('SKILL.md')),'Stage18 defines contracts; Stage21+ implements')
    check('No installed maturity claim',all('implementation and installed validation are separate gates' in text for text in texts.values()),'Every spec separates contract from executed product evidence')
    check('No new unresolved reproducibility placeholder in exact tasks',all('<' not in c['exact_prompt'] for c in data['primary_cases']) and all('<' not in p['exact_source_fixture']['prompt'] for p in data['pack_profiles']), 'Authoring templates are explicitly distinct from fixed tasks')
    # Control fixtures for this verifier's parsing properties, not product tests.
    sample='### B01 — `task`\n\n| inputs | present |\n\n## End\n'
    check('Parser does not invent a missing command',set(command_blocks(sample))=={'B01'},'One present, all others absent')
    check('Exact identity detects prompt mutation',sha(data['primary_cases'][0]['exact_prompt']+' changed')!=data['primary_cases'][0]['prompt_sha256'],'Appending a semantic change changes identity')
    publication=documents+[LOG/(PREFIX+'-specification-contracts.json'),Path(__file__)]
    result={'stage':18,'scope':'Canonical documentation conformance, exact inherited contract/fixture fidelity and source preservation; direct substance review is separate. No installed agent, real pack pair or commercial outcome measured.','python':platform.python_version(),'starting_head':manifest['starting_head'],'inputs_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in publication},'summary':{'PASS':sum(x['result']=='PASS' for x in CHECKS),'FAIL':sum(x['result']=='FAIL' for x in CHECKS)},'checks':CHECKS}
    OUT.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps({'stage':18,**result['summary'],'python':result['python'],'output':str(OUT)}))
    for c in CHECKS:
        if c['result']=='FAIL':print(json.dumps(c,ensure_ascii=False))
    return 1 if result['summary']['FAIL'] else 0

if __name__=='__main__':
    try:sys.exit(main())
    except Exception as exc:
        OUT.write_text(json.dumps({'stage':18,'state':'ERROR','error':type(exc).__name__+': '+str(exc),'checks':CHECKS},indent=2)+'\n')
        raise
