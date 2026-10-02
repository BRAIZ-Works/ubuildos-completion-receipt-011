from pathlib import Path
import tempfile, shutil, subprocess, json, hashlib
ROOT=Path(__file__).resolve().parents[1]
VERIFY='tests/verify.py'

def run(root):
    p=subprocess.run(['python3',str(root/VERIFY)],cwd=root,text=True,capture_output=True)
    return p.returncode, p.stdout+p.stderr

def regen(root):
    derived={'PUBLIC_MANIFEST.json','SHA256SUMS.txt'}
    files=sorted(p for p in root.rglob('*') if p.is_file() and str(p.relative_to(root)) not in derived)
    rec=[]; lines=[]
    for p in files:
        rel=str(p.relative_to(root)); b=p.read_bytes(); h=hashlib.sha256(b).hexdigest()
        rec.append({'path':rel,'bytes':len(b),'sha256':h}); lines.append(f'{h}  {rel}')
    (root/'PUBLIC_MANIFEST.json').write_text(json.dumps({'schema':'DAY10_PUBLIC_MANIFEST_V1','version':'1.0.1-candidate','population_definition':'all release files except derived integrity indexes PUBLIC_MANIFEST.json and SHA256SUMS.txt','population_count':len(rec),'files':rec},indent=2)+'\n')
    (root/'SHA256SUMS.txt').write_text('\n'.join(lines)+'\n')

cases=[]
def case(name, mutate, regen_indexes=False):
    with tempfile.TemporaryDirectory() as td:
        d=Path(td)/'subject'; shutil.copytree(ROOT,d)
        mutate(d)
        if regen_indexes: regen(d)
        rc,out=run(d); cases.append({'id':name,'rejected':rc!=0,'output':out[-1200:]})

case('M01-missing-manifest',lambda d:(d/'PUBLIC_MANIFEST.json').unlink())
case('M02-missing-sums',lambda d:(d/'SHA256SUMS.txt').unlink())
case('M03-content-byte-drift',lambda d:(d/'README.md').write_text((d/'README.md').read_text()+'\nmutation\n'))
case('M04-extra-member',lambda d:(d/'UNDECLARED.txt').write_text('unsafe extra'))
case('M05-linkedin-cta-removed-self-consistent',lambda d:(d/'LINKEDIN_POST.md').write_text((d/'LINKEDIN_POST.md').read_text().replace('Inspect the product. Challenge the workflow.','Inspect it.')),True)
case('M06-linkedin-hashtags-weakened-self-consistent',lambda d:(d/'LINKEDIN_POST.md').write_text((d/'LINKEDIN_POST.md').read_text().replace('#BuildInPublic #AI #ArtificialIntelligence #ProductDevelopment #SoftwareEngineering #Automation #AIAgents #SaaS #Startup #Founder #UBuildOS','#UBuildOS')),True)
case('M07-linkedin-question-added-self-consistent',lambda d:(d/'LINKEDIN_POST.md').write_text((d/'LINKEDIN_POST.md').read_text()+'\nWould you use this?\n'),True)
case('M08-state-removed-self-consistent',lambda d:(d/'app.js').write_text((d/'app.js').read_text().replace('Rejected','Declined')),True)
failed=[c for c in cases if not c['rejected']]
print(json.dumps({'status':'PASS' if not failed else 'FAIL','detected':len(cases)-len(failed),'total':len(cases),'cases':cases},indent=2))
raise SystemExit(1 if failed else 0)
