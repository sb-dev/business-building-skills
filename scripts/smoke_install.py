#!/usr/bin/env python3
"""Copy each core skill into a clean temp project and validate local references.
This tests source-independent skill packaging without requiring network or a specific agent CLI.
"""
from pathlib import Path
import re, shutil, tempfile, sys
ROOT=Path(__file__).resolve().parents[1]
errors=[]
with tempfile.TemporaryDirectory() as td:
    dest=Path(td)/'consumer'/'skills'; dest.mkdir(parents=True)
    for name in ['business-build','business-grow','business-evaluate','business-pack-author']:
        src=ROOT/'skills'/name; out=dest/name; shutil.copytree(src,out)
        skill=out/'SKILL.md'
        if not skill.exists(): errors.append(f'{name}: SKILL.md missing')
        text=skill.read_text()
        if f'name: {name}' not in text: errors.append(f'{name}: name mismatch')
        for rel in re.findall(r'`((?:references|commands|scripts)/[^`]+)`', text):
            if not (out/rel).exists(): errors.append(f'{name}: unresolved local path {rel}')
if errors:
    print('\n'.join(f'ERROR: {e}' for e in errors)); sys.exit(1)
print('clean skill-copy smoke test passed')
