from pathlib import Path
import json, re, hashlib, sys
root=Path(__file__).resolve().parents[1]
errors=[]

def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def need(path, terms):
    p=root/path
    if not p.exists():
        errors.append(f'missing:{path}')
        return
    t=p.read_text(errors='replace')
    for term in terms:
        if term not in t:
            errors.append(f'{path}:missing:{term}')

# Required product/document population.
need('index.html',['Content Approval Queue','Needs review','Waiting','Approved','Rejected','Synthetic data','No external systems connected'])
need('app.js',['rationale','history','next','status','owner','empty','keydown'])
required=[
 'README.md','START_HERE.md','docs/METHODOLOGY.md','docs/LIMITATIONS.md','docs/PRIVACY.md',
 'docs/SECURITY.md','docs/ACCESSIBILITY.md','docs/RECOVERY.md','docs/RIGHTS_AND_USE.md',
 'docs/RELEASE_NOTES.md','docs/VERIFICATION_SUMMARY.md','LINKEDIN_POST.md','CAROUSEL.md',
 'CAROUSEL_ACCESSIBILITY.md','PUBLIC_MANIFEST.json','SHA256SUMS.txt',
 'evidence/PRODUCER_ASSURANCE_v1.0.1.md',
 'evidence/UBUILDOS_LINKEDIN_PUBLIC_CAMPAIGN_POST_STANDARD_v1.3.0_BYTE_LOCK.md',
 'tests/mutation_tests.py','RECOVERY_FROM_v1.0.0.md','PUBLICATION_GATE.md']
for f in required:
    if not (root/f).is_file(): errors.append('missing:'+f)

# Fail-closed integrity indexes.
manifest_path=root/'PUBLIC_MANIFEST.json'; sums_path=root/'SHA256SUMS.txt'
manifest=None
if manifest_path.is_file():
    try: manifest=json.loads(manifest_path.read_text())
    except Exception as e: errors.append('manifest malformed:'+str(e))
if manifest is not None:
    files=manifest.get('files')
    if not isinstance(files,list):
        errors.append('manifest files missing/list-invalid')
        files=[]
    paths=[x.get('path') for x in files if isinstance(x,dict)]
    if len(paths)!=len(set(paths)): errors.append('manifest duplicate path')
    derived={'PUBLIC_MANIFEST.json','SHA256SUMS.txt'}
    actual=sorted(str(p.relative_to(root)) for p in root.rglob('*') if p.is_file() and str(p.relative_to(root)) not in derived)
    listed=sorted(p for p in paths if isinstance(p,str))
    if actual!=listed:
        errors.append('manifest population mismatch')
    if manifest.get('population_count')!=len(actual):
        errors.append('manifest population_count mismatch')
    for rec in files:
        if not isinstance(rec,dict):
            errors.append('manifest record malformed'); continue
        rel=rec.get('path'); p=root/rel if isinstance(rel,str) else None
        if not p or not p.is_file():
            errors.append('manifest missing member:'+str(rel)); continue
        if rec.get('bytes')!=p.stat().st_size: errors.append('manifest byte mismatch:'+rel)
        if rec.get('sha256')!=digest(p): errors.append('manifest hash mismatch:'+rel)

# SHA256SUMS must cover exactly the same governed population with same hashes.
if sums_path.is_file():
    sums={}
    for lineno,line in enumerate(sums_path.read_text().splitlines(),1):
        if not line.strip(): continue
        m=re.fullmatch(r'([0-9a-f]{64})  (.+)',line)
        if not m:
            errors.append(f'sums malformed line:{lineno}'); continue
        h,rel=m.groups()
        if rel in sums: errors.append('sums duplicate path:'+rel)
        sums[rel]=h
    derived={'PUBLIC_MANIFEST.json','SHA256SUMS.txt'}
    actual=sorted(str(p.relative_to(root)) for p in root.rglob('*') if p.is_file() and str(p.relative_to(root)) not in derived)
    if sorted(sums)!=actual: errors.append('sums population mismatch')
    for rel,h in sums.items():
        p=root/rel
        if not p.is_file(): errors.append('sums missing member:'+rel)
        elif digest(p)!=h: errors.append('sums hash mismatch:'+rel)
    if manifest is not None and isinstance(manifest.get('files'),list):
        mh={r.get('path'):r.get('sha256') for r in manifest['files'] if isinstance(r,dict)}
        if sums!=mh: errors.append('manifest/sums disagreement')

# bounded/no-overclaim checks
alltxt='\n'.join(p.read_text(errors='replace') for p in root.rglob('*') if p.is_file() and p.suffix in {'.md','.html','.js','.css'})
for bad in ['FRESH_IQA_PASS','OWNER_ACCEPTED','VERIFIED_TERMINAL_DONE','production-ready','guaranteed results']:
    if bad in alltxt: errors.append('premature/unsupported claim:'+bad)

# no external runtime deps/network
runtime=(root/'index.html').read_text(errors='replace')+(root/'app.js').read_text(errors='replace')
for bad in ['fetch(','XMLHttpRequest','https://cdn','<script src="http']:
    if bad in runtime: errors.append('external dependency:'+bad)

# LinkedIn v1.3.0 Day 5+ mandatory mechanics.
need('PUBLICATION_GATE.md',['Do not publish','Fresh Independent QA PASS','owner/publication authorization'])
post=(root/'LINKEDIN_POST.md').read_text(errors='replace') if (root/'LINKEDIN_POST.md').is_file() else ''
required_post=[
 'Day 10 of building in public:',
 'So I built Content Approval Queue around one simple question:',
 'A capable developer could recreate parts of this quickly. That isn\'t the claim.',
 'The screen may be simple. The test is the whole path around it.',
 'What Day 10 proves',
 'What it does NOT prove',
 'The live review exposed another lesson:',
 'Inspect the product. Challenge the workflow.',
 'Live build:',
 'https://braiz-works.github.io/ubuildos-completion-receipt-011/',
 'Public repository:',
 'https://github.com/BRAIZ-Works/ubuildos-completion-receipt-011',
 'Day 10/30.',
 'One approval bottleneck.',
 'One inspectable workflow.',
 'One verified release.',
 '#BuildInPublic #AI #ArtificialIntelligence #ProductDevelopment #SoftwareEngineering #Automation #AIAgents #SaaS #Startup #Founder #UBuildOS'
]
for term in required_post:
    if term not in post: errors.append('linkedin missing:'+term)
# Exactly one deliberately narrow quoted question; primary CTA itself is not a question.
questions=re.findall(r'[^\n]*\?[^\n]*',post)
if len(questions)!=1: errors.append(f'linkedin question count={len(questions)}')
if questions and not questions[0].strip().startswith('"Can one small queue'):
    errors.append('linkedin narrow question mismatch')
# required sections each before CTA and links/signature in canonical order
order=[
 'Day 10 of building in public:',
 'So I built Content Approval Queue around one simple question:',
 'A capable developer could recreate parts of this quickly. That isn\'t the claim.',
 'What Day 10 proves', 'What it does NOT prove',
 'The live review exposed another lesson:',
 'Inspect the product. Challenge the workflow.', 'Live build:', 'Public repository:', 'Day 10/30.'
]
pos=[]
for term in order:
    i=post.find(term); pos.append(i)
if any(i<0 for i in pos) or pos!=sorted(pos): errors.append('linkedin canonical order')

# carousel parity
acc=(root/'CAROUSEL_ACCESSIBILITY.md').read_text(errors='replace'); car=(root/'CAROUSEL.md').read_text(errors='replace')
if len(re.findall(r'^## \d',car,re.M))!=6: errors.append('carousel page count')
if len(re.findall(r'^\d\.',acc,re.M))!=6: errors.append('carousel accessibility page count')

# data/state presence
js=(root/'app.js').read_text(errors='replace')
for st in ['Needs review','Waiting','Approved','Rejected']:
    if st not in js: errors.append('missing state:'+st)

print(json.dumps({'status':'PASS' if not errors else 'FAIL','errors':errors},indent=2))
sys.exit(1 if errors else 0)
