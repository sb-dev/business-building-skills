#!/usr/bin/env python3
"""Stage 21 preservation/scope evidence. Run only against this stage's work."""
from collections import Counter
import hashlib
import json
from pathlib import Path
import platform

ROOT = Path(__file__).resolve().parents[2]
LOG = 'docs/research-logs/'
checks = []


def blob(path):
    data = path.read_bytes()
    return hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()


def check(name, valid, detail):
    checks.append({'check': name, 'result': 'PASS' if valid else 'FAIL', 'detail': detail})


inputs = json.loads((ROOT / (LOG + '2026-09-13-stage-21-inputs.json')).read_text())
prior = {x['path']: x['sha'] for x in inputs['inherited_files']}
allowed = {'README.md', LOG + 'bootstrap-3-progress.md'}
for path, sha in prior.items():
    if path not in allowed:
        check('preserved: ' + path, blob(ROOT / path) == sha, sha)
for source, snapshot in [('README.md', '2026-09-13-stage-21-inherited-root-readme.md'), (LOG + 'bootstrap-3-progress.md', '2026-09-13-bootstrap-3-progress-through-stage-20.md')]:
    check('exact prior snapshot: ' + source, blob(ROOT / (LOG + snapshot)) == prior[source], prior[source])
actual_specs = sorted(p.name for p in (ROOT / 'docs').glob('0[1-6]-*.md'))
expected_specs = sorted(Path(p).name for p in prior if p.startswith('docs/0'))
check('six exact canonical names', len(actual_specs) == 6 and actual_specs == expected_specs, actual_specs)
examples = (ROOT / 'examples/README.md').read_text()
check('five rendered three-case Markdown tables', len(__import__('re').findall(r'\|---\|---\|---\|\n(?:\| E\d\d[^\n]*\n){3}', examples)) == 5, 'No blank lines split table header and rows')
check('no empty marker files', not any(p.is_file() and p.stat().st_size == 0 for p in ROOT.rglob('*')), 'Every created path has real contents')
workflow = (ROOT / '.github/workflows/validate.yml').read_text()
check('scoped CI inspected', all(x in workflow for x in ['contents: read', 'persist-credentials: false', "python-version: '3.12.14'", 'python tests/validate_repository.py', "python -m unittest discover -s tests -p 'test_*.py' -v"]) and not any(x in workflow for x in ['pull_request_target:', 'write-all', 'secrets.', 'workflow_run:']), 'Static configuration inspection, not an executed remote workflow')
check('exact inspected action identities', all(x in workflow for x in ['actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1', 'actions/setup-python@5fda3b95a4ea91299a34e894583c3862153e4b97']), inputs['action_sources'])
readme = (ROOT / 'README.md').read_text()
draft = (ROOT / (LOG + '2026-09-13-stage-19-public-readme.md')).read_text()
headings = lambda t: __import__('re').findall(r'^#{1,2} (.*)$', t, __import__('re').M)
check('full Stage 19 public topic sequence retained', headings(readme) == headings(draft), headings(readme))
progress = (ROOT / (LOG + 'bootstrap-3-progress.md')).read_text()
old_progress = (ROOT / (LOG + '2026-09-13-bootstrap-3-progress-through-stage-20.md')).read_text()
check('prior completion evidence retained in live progress', old_progress[old_progress.index('## Stage 16 completion receipt'):] in progress, 'Prior completion sections remain exact; current index and Stage 21 record reflect the prepared work')
check('authorised MIT licence and exact recorded text', inputs['licence_authority']['status'] == 'PASS' and inputs['licence_authority']['user_reply'] == 'MIT' and inputs['licence_authority']['grant_created'] and hashlib.sha256((ROOT / 'LICENSE').read_bytes()).hexdigest() == inputs['licence_authority']['license_sha256'], 'Explicit user licence choice; complete standard text inspected against the Open Source Initiative MIT source')
counts = Counter(x['result'] for x in checks)
print(json.dumps({'scope': 'Stage 21 preservation, actual-file review and authorised MIT licence', 'python': platform.python_version(), 'starting_head': inputs['starting_head'], 'counts': dict(counts), 'checks': checks}, indent=2))
raise SystemExit(1 if counts['FAIL'] else 0)
