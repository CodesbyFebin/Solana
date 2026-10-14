#!/usr/bin/env python3
import json,pathlib,re
root=pathlib.Path(__file__).resolve().parents[1]
c=json.loads((root/'catalog/repos.json').read_text())
all_items=[r for group in c['groups'].values() for r in group]
assert len(all_items)==47,(len(all_items),'expected 47')
names=[r['repo'] for r in all_items]
assert len(set(names))==len(names),'duplicate repo'
assert all(re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+',n) for n in names)
assert all(r['url']=='https://github.com/'+r['repo'] for r in all_items)
print('PASS: 47 unique Solana source references in',len(c['groups']),'groups')
