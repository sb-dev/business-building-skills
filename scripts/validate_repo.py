#!/usr/bin/env python3
from pathlib import Path
import re, sys
ROOT=Path(__file__).resolve().parents[1]
errors=[]
for name in ['business-build','business-grow','business-evaluate','business-pack-author']:
    p=ROOT/'skills'/name/'SKILL.md'
    if not p.exists(): errors.append(f'missing {p.relative_to(ROOT)}'); continue
    t=p.read_text()
    if not t.startswith('---\n') or f'name: {name}' not in t: errors.append(f'invalid frontmatter: {name}')
for n in range(1,7):
    if not list((ROOT/'docs').glob(f'{n:02d}-*.md')): errors.append(f'missing canonical spec {n:02d}')
lic=(ROOT/'LICENSE').read_text() if (ROOT/'LICENSE').exists() else ''
if 'END OF TERMS AND CONDITIONS' not in lic: errors.append('LICENSE is not the full Apache-2.0 text')
pack=ROOT/'extension-packs'/'professional-services'/'PACK.md'
if not pack.exists() or '## Showcase exact prompt' not in pack.read_text(): errors.append('professional-services pack/showcase missing')
if errors:
    print('\n'.join(f'ERROR: {e}' for e in errors)); sys.exit(1)
print('repository validation passed')
