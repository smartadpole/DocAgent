#!/usr/bin/env python3
"""Opt-in real Codex model probe; isolated copy, never run by check_all.

Outputs contain private runtime evidence. Choose an external Data directory.
Oracles are for the reviewer and are never sent to the tested model.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import time

ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / 'scripts/fixtures/model_adaptation/cases.json'

def run(args):
    source = args.source.resolve()
    out = args.output.resolve()
    if out == source or out.is_relative_to(source) or source.is_relative_to(out):
        raise ValueError('Evidence output must be separate from source repository')
    out.mkdir(parents=True, exist_ok=False)
    snapshot = out / 'workspace'
    files = subprocess.check_output(['git','ls-files','-z','--cached','--others','--exclude-standard'], cwd=source).decode().split('\0')
    hashes = {}
    def fingerprint(path):
        return 'symlink:'+str(path.readlink()) if path.is_symlink() else hashlib.sha256(path.read_bytes()).hexdigest()
    for rel in sorted(set(filter(None, files))):
        path = source / rel
        if not path.exists(): continue
        target = snapshot / rel
        target.parent.mkdir(parents=True,exist_ok=True)
        if path.is_symlink(): target.symlink_to(path.readlink())
        else: shutil.copy2(path,target)
        hashes[rel] = fingerprint(path)
    subprocess.run(['git','init','-b','probe'],cwd=snapshot,check=True,capture_output=True)
    subprocess.run(['git','add','.'],cwd=snapshot,check=True,capture_output=True)
    subprocess.run(['git','-c','user.name=Model probe','-c','user.email=probe@example.invalid','commit','-m','Freeze isolated evaluation input'],cwd=snapshot,check=True,capture_output=True)
    fixture = snapshot/'eval-fixture'; fixture.mkdir()
    before = '# 原生能力\n\n[说明](docs/overview.md)\n\n领域例外：大样本超时必须保留失败证据，不能改写为成功。\n'
    (fixture/'index.md').write_text(before)
    (fixture/'guide.md').write_text('# 指南\n\n本地目标。\n')
    (fixture/'check.py').write_text("from pathlib import Path\np=Path(__file__).parent\nassert (p/'index.md').read_text() == "+repr(before.replace('docs/overview.md','guide.md'))+"\nprint('Fixture link and domain exception: OK')\n")
    for path in fixture.iterdir(): hashes[str(path.relative_to(snapshot))] = fingerprint(path)
    case = json.loads(CASES.read_text())[args.case]
    prompt = case['prompt']
    (out/'prompt.txt').write_text(prompt)
    command = ['codex','exec','--ignore-user-config','--ephemeral','--skip-git-repo-check','--sandbox', 'workspace-write' if args.case=='repair' else 'read-only','--model',args.model,'-c','model_reasoning_effort="medium"','-c','approval_policy="never"','--cd',str(snapshot),'--json','-o',str(out/'answer.txt'),prompt]
    started=time.time()
    with (out/'events.jsonl').open('w') as stdout, (out/'runtime.stderr').open('w') as stderr:
        try: result=subprocess.run(command,stdin=subprocess.DEVNULL,stdout=stdout,stderr=stderr,timeout=args.timeout); code=result.returncode
        except subprocess.TimeoutExpired: code=124
    changed=[]
    for path in snapshot.rglob('*'):
        rel=str(path.relative_to(snapshot))
        if '.git' in path.parts or not (path.is_file() or path.is_symlink()):continue
        if fingerprint(path)!=hashes.get(rel):changed.append(rel)
    deleted=[rel for rel in hashes if not ((snapshot/rel).exists() or (snapshot/rel).is_symlink())]
    exact_repair=(fixture/'index.md').read_text()==before.replace('docs/overview.md','guide.md')
    events=[]
    for line in (out/'events.jsonl').read_text().splitlines():
        try: events.append(json.loads(line))
        except json.JSONDecodeError: pass
    commands=[e['item'] for e in events if e.get('type')=='item.completed' and e.get('item',{}).get('type')=='command_execution']
    checked=any('eval-fixture/check.py' in c.get('command','') and c.get('exit_code')==0 for c in commands)
    proof={'case':args.case,'model':args.model,'reasoning':'medium','exit_code':code,'elapsed_seconds':round(time.time()-started,2),'source_hashes':hashes,'source_head':subprocess.check_output(['git','rev-parse','HEAD'],cwd=source,text=True).strip(),'changed':changed,'deleted':deleted,'commit_count':int(subprocess.check_output(['git','rev-list','--count','HEAD'],cwd=snapshot,text=True)),'oracle':case['oracle'],'repair_exact':exact_repair if args.case=='repair' else None,'repair_checked':checked if args.case=='repair' else None,'review_status':'needs-independent-review','usage':[e for e in events if e.get('type')=='turn.completed']}
    (out/'proof.json').write_text(json.dumps(proof,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in proof.items() if k not in ('source_hashes','oracle')},ensure_ascii=False))
    return code

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--model',required=True)
    parser.add_argument('--case',choices=json.loads(CASES.read_text()).keys(),required=True)
    parser.add_argument('--source',type=Path,default=ROOT)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--timeout',type=int,default=600)
    raise SystemExit(run(parser.parse_args()))
