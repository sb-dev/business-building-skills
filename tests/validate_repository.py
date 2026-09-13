#!/usr/bin/env python3
"""Validate source packaging; no host or semantic evaluation is implied."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import platform
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
CORPUS = 'docs/research-logs/2026-09-12-stage-17-case-contracts.json'
SPEC = 'docs/03-business-building-skills-repository-and-contracts-spec.md'
FIELDS = ['inputs', 'evidence required', 'assumptions allowed', 'output',
          'allowed mutations', 'forbidden behaviour', 'metrics/evidence',
          'failure states', 'legal/ethical boundaries']
MODES = {'G02': ['lead-magnet', 'outreach', 'content-loop'],
         'E02': ['opportunity', 'offer', 'pricing', 'money-model', 'channel', 'funnel', 'retention'],
         'E03': ['economics', 'cash', 'both']}


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def blob(data):
    return hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()


def facts_from_prompt(prompt):
    """Extract the one declared facts object without interpreting the answer."""
    if prompt.count('Facts (JSON):') != 1:
        raise ValueError('Prompt must contain one declared facts object')
    data = prompt.split('Facts (JSON):', 1)[1].lstrip()
    facts, end = json.JSONDecoder().raw_decode(data)
    if not isinstance(facts, dict) or facts.get('synthetic') is not True:
        raise ValueError('Expected explicitly synthetic fixture facts')
    if not data[end:].lstrip().startswith('Task:'):
        raise ValueError('Missing task or material inserted between facts and task')
    return facts


def subject_matches(prompt, facts, accepted):
    return (prompt == accepted['exact_prompt']
            and sha256(prompt.encode()) == accepted['prompt_sha256']
            and facts == facts_from_prompt(prompt))


def anchors(text):
    result, seen = set(), Counter()
    for heading in re.findall(r'^#{1,6} (.+)$', re.sub(r'```.*?```', '', text, flags=re.S), re.M):
        plain = re.sub(r'\[([^]]+)\]\([^)]*\)', r'\1', heading)
        slug = re.sub(r'[^\w\- ]', '', plain.lower()).replace(' ', '-')
        suffix = f'-{seen[slug]}' if seen[slug] else ''
        result.add(slug + suffix)
        seen[slug] += 1
    return result


def validate(root):
    checks = []
    observed = {}

    def check(name, valid, detail='', blocked=False):
        checks.append({'check': name, 'result': 'PASS' if valid else ('BLOCKED' if blocked else 'FAIL'), 'detail': detail})

    def read(relative):
        p = root / relative
        resolved = p.resolve()
        if not resolved.is_relative_to(root) or p.is_symlink():
            raise ValueError(f'Unsafe source path: {relative}')
        data = p.read_bytes()
        observed[relative] = sha256(data)
        return data

    def parsed(relative):
        return json.loads(read(relative))

    for p in ['README.md', 'CONTRIBUTING.md', 'CHANGELOG.md', '.github/workflows/validate.yml']:
        check('required file: ' + p, bool(read(p).strip()))
    for p in ['skills', 'examples', 'benchmarks', 'tests', '.github']:
        check('immediate content: ' + p, any(x.is_file() and x.stat().st_size for x in (root / p).rglob('*')))
    for p in ['tools', 'extension-packs', 'integrations']:
        check('optional directory not prematurely created: ' + p, not (root / p).exists(), 'No implemented need at Stage 21')
    check('project licence terms present', (root / 'LICENSE').is_file() and bool((root / 'LICENSE').read_text().strip()),
          'Owner authorisation must also be established in Stage 21 conformance; a filename alone grants no authority.', blocked=True)

    source = parsed(CORPUS)
    canonical = read(SPEC).decode()
    registry = parsed('benchmarks/cases.json')
    check('case source identity', registry['source'] == {'path': CORPUS, 'blob': blob(read(CORPUS))})
    cases = registry['primary_cases']
    check('exact 15 primary identities', [x['id'] for x in cases] == [f'E{i:02d}' for i in range(1, 16)])
    check('exact 3/3/3/3/3 distribution', Counter(x['level'] for x in cases) == {i: 3 for i in range(1, 6)})
    accepted = {x['id']: x for x in source['primary_cases']}
    for case in cases:
        ident = case['id']
        prior = accepted[ident]
        prompt = read(case['prompt']).decode()
        facts = parsed(case['facts'])
        oracle = parsed(case['oracle'])
        check(ident + ' exact full prompt and matching facts', subject_matches(prompt, facts, prior))
        check(ident + ' manifest input identities', sha256(prompt.encode()) == case['prompt_sha256'] and sha256(read(case['facts'])) == case['facts_sha256'])
        check(ident + ' level and source provenance', prior['level'] == case['level'] and blob(read(prior['source_path'])) == prior['source_blob'])
        check(ident + ' actual example location', case['prompt'] == f'examples/level-{case["level"]:02d}/{ident}/prompt.txt' and case['facts'] == f'examples/level-{case["level"]:02d}/{ident}/input.json')
        expected = {k: v for k, v in prior.items() if k != 'exact_prompt'}
        expected.update(material_kind='AUTHORED_EVALUATION_CONTRACT_NOT_AGENT_OUTPUT', installed_run_state='NOT_RUN')
        check(ident + ' complete separate oracle', oracle == expected and case['oracle'] == f'benchmarks/oracles/{ident}.json')
        check(ident + ' truthful synthetic/run state', case['synthetic'] is True and facts['synthetic'] is True and case['installed_run_state'] == 'NOT_RUN' and facts['case_version'] == case['version'])
    actual_prompts = {x.relative_to(root).as_posix() for x in (root / 'examples').rglob('prompt.txt')}
    check('no missing or extra primary prompt', actual_prompts == {x['prompt'] for x in cases})
    contracts = parsed('benchmarks/oracles/evaluation-contracts.json')
    expected_counts = {'deterministic': 10, 'reasoning': 16, 'behaviour': 10, 'adversaries': 14,
                       'pack_dimensions': 7, 'pack_profiles': 9, 'regression': 7, 'case_contract': 14, 'stress_cases': 3}
    for key, count in expected_counts.items():
        check('complete evaluation corpus: ' + key, contracts[key] == source[key] and len(contracts[key]) == count)

    inventory = parsed('skills/catalogue.json')['skills']
    expected_skills = {'business-build': (6, 10), 'business-grow': (7, 8),
                       'business-evaluate': (8, 7), 'business-pack-author': (9, 7)}
    check('four exact independent contract inventories', [x['name'] for x in inventory] == list(expected_skills))
    all_ids = []
    for entry in inventory:
        name = entry['name']
        section, count = expected_skills[name]
        doc = parsed('skills/' + entry['contract'])
        check(name + ' source identity', doc['source'] == {'path': SPEC, 'blob': blob(read(SPEC)), 'section': section})
        check(name + ' exact description', doc['description'] == re.search(r'^' + name + r': (.*)$', canonical, re.M).group(1))
        check(name + ' not advertised as installed', entry['implementation_state'] == doc['implementation_state'] == 'NOT_IMPLEMENTED' and not (root / 'skills' / name / 'SKILL.md').exists())
        expected = []
        block = canonical.split(f'## {section}. ', 1)[1].split(f'## {section+1}. ', 1)[0]
        for match in re.finditer(r'^### ([BGEP]\d{2}) — `([^`]+)`\n(.*?)(?=^### |\Z)', block, re.M | re.S):
            ident, selector, body = match.groups()
            rows = dict(re.findall(r'^\| ([^|\n]+?) \| (.*?) \|$', body, re.M))
            expected.append({'id': ident, 'selector': selector, 'modes': MODES.get(ident, []), 'contract': {f: rows[f] for f in FIELDS}})
        check(name + ' complete accepted commands and nine fields', doc['commands'] == expected and len(doc['commands']) == entry['command_count'] == count)
        all_ids.extend(x['id'] for x in doc['commands'])
    check('32 unique logical selectors', len(all_ids) == len(set(all_ids)) == 32)

    public = [Path(x) for x in ['README.md', 'CONTRIBUTING.md', 'CHANGELOG.md', 'skills/README.md', 'examples/README.md', 'benchmarks/README.md', 'tests/README.md']]
    link_count = 0
    for relative in public:
        text = re.sub(r'```.*?```', '', read(relative.as_posix()).decode(), flags=re.S)
        for target in re.findall(r'\[[^]\n]+\]\(([^)\s]+)\)', text):
            u = urlsplit(target)
            if u.scheme or u.netloc:
                continue
            p = (root / relative.parent / unquote(u.path)).resolve() if u.path else (root / relative).resolve()
            valid = p.is_relative_to(root) and p.exists()
            if valid and u.fragment:
                valid = p.is_file() and unquote(u.fragment) in anchors(p.read_text())
            check(f'local link: {relative} -> {target}', valid)
            link_count += 1
    check('checks preserve every read source', all(sha256((root / path).read_bytes()) == before for path, before in observed.items()))
    results = Counter(x['result'] for x in checks)
    return {'scope': 'Stage 21 deterministic scaffold validation; no installed or semantic claim', 'python': platform.python_version(),
            'counts': {k: results[k] for k in ('PASS', 'FAIL', 'BLOCKED')}, 'local_links': link_count,
            'source_files_read': len(observed), 'source_hashes': observed, 'checks': checks}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--report', type=Path)
    args = parser.parse_args()
    if args.report and args.report.resolve().is_relative_to(ROOT):
        parser.error('Report must be outside the validated repository')
    try:
        result = validate(ROOT)
    except (OSError, ValueError, KeyError, TypeError, AttributeError) as exc:
        result = {'scope': 'Stage 21 deterministic scaffold validation', 'counts': {'PASS': 0, 'FAIL': 1, 'BLOCKED': 0}, 'error': str(exc)}
    rendered = json.dumps(result, indent=2, ensure_ascii=False) + '\n'
    if args.report:
        with args.report.open('x') as out:
            out.write(rendered)
    print(rendered, end='')
    return 1 if result['counts']['FAIL'] else 2 if result['counts']['BLOCKED'] else 0


if __name__ == '__main__':
    sys.exit(main())
