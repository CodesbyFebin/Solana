#!/usr/bin/env python3
"""Opt-in shallow source snapshotter; never run cloned code automatically."""
import argparse, json, pathlib, subprocess
root=pathlib.Path(__file__).resolve().parents[1]
catalog=json.loads((root/'catalog/repos.json').read_text())['groups']
p=argparse.ArgumentParser();p.add_argument('--groups',nargs='+',choices=sorted(catalog),required=True)
a=p.parse_args()
for group in a.groups:
 for item in catalog[group]:
  full=item['repo']; dest=root/'vendor'/group/full.replace('/','__')
  if dest.exists(): print('SKIP',full);continue
  dest.parent.mkdir(parents=True,exist_ok=True)
  print('CLONE',full,flush=True)
  subprocess.run(['git','clone','--depth=1','--no-tags',item['clone_url'],str(dest)],check=True)
  print('SHA',subprocess.check_output(['git','-C',str(dest),'rev-parse','HEAD'],text=True).strip())
