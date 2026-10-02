from pathlib import Path
import hashlib, json, re, sys
root=Path(__file__).resolve().parents[1]
errors=[]

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()

def text(rel):
    p=root/rel
    if not p.is_file():
        errors.append('missing:'+rel); return ''
    return p.read_text(errors='replace')

readme=text('README.md')
life=text('LIFECYCLE_STATUS.md')
post=text('LINKEDIN_POST.md')
ident_path=root/'evidence/FROZEN_SUBJECT_IDENTITY.json'
try: ident=json.loads(ident_path.read_text())
except Exception as e: errors.append('identity malformed:'+str(e)); ident={}

expected='6790b56bfb1f1d5a7165e9fb49160a3ef033b69cbaa52670cc6f1a3426986bb9'
if ident.get('sha256')!=expected: errors.append('wrong frozen subject hash')
if ident.get('fresh_iqa')!='PASS': errors.append('fresh IQA not PASS')
if ident.get('owner_accepted') is not True or ident.get('frozen') is not True: errors.append('accept/freeze missing')
for term in ['v1.0.1','Fresh Independent IQA PASS','owner accepted and frozen',expected,
             'https://github.com/BRAIZ-Works/ubuildos-completion-receipt-011',
             'https://braiz-works.github.io/ubuildos-completion-receipt-011/']:
    if term not in readme: errors.append('README missing:'+term)
if 'PRE-IQA candidate' in readme or 'not independently reviewed' in readme: errors.append('stale README candidate language')
for term in ['GitHub publication','GitHub Pages deployment','LinkedIn publication/readback']:
    if term not in life: errors.append('lifecycle boundary missing:'+term)
required_post=['Inspect the product. Challenge the workflow.','Live build:','Public repository:','Day 10/30.','One verified release.']
for term in required_post:
    if term not in post: errors.append('linkedin missing:'+term)
if len(re.findall(r'[^\n]*\?[^\n]*',post))!=1: errors.append('linkedin question count')
# Static app remains offline/bounded.
runtime=text('index.html')+text('app.js')
for bad in ['fetch(','XMLHttpRequest','https://cdn','<script src="http']:
    if bad in runtime: errors.append('external runtime dependency:'+bad)
print(json.dumps({'status':'PASS' if not errors else 'FAIL','errors':errors},indent=2))
sys.exit(1 if errors else 0)
