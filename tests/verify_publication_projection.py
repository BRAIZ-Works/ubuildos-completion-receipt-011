from pathlib import Path
import json, re, sys

root=Path(__file__).resolve().parents[1]
errors=[]

def text(rel):
    p=root/rel
    if not p.is_file():
        errors.append("missing:"+rel)
        return ""
    return p.read_text(errors="replace")

expected="6790b56bfb1f1d5a7165e9fb49160a3ef033b69cbaa52670cc6f1a3426986bb9"
repo_url="https://github.com/BRAIZ-Works/ubuildos-completion-receipt-011"
live_url="https://braiz-works.github.io/ubuildos-completion-receipt-011/"
linkedin_url="https://lnkd.in/p/et2P9BM7"

required_docs=[
    "README.md","START_HERE.md","LIFECYCLE_STATUS.md","PUBLICATION_GATE.md",
    "docs/METHODOLOGY.md","docs/DATA_MODEL.md","docs/TEST_AND_EVIDENCE.md",
    "docs/LIMITATIONS.md","docs/PRIVACY.md","docs/SECURITY.md",
    "docs/ACCESSIBILITY.md","docs/RECOVERY.md","docs/RIGHTS_AND_USE.md",
    "docs/RELEASE_NOTES.md","docs/VERIFICATION_SUMMARY.md",
    "docs/TERMINAL_CLOSEOUT.md","docs/LESSONS_AND_HANDOFF.md"
]
for rel in required_docs:
    text(rel)

readme=text("README.md")
life=text("LIFECYCLE_STATUS.md")
post=text("LINKEDIN_POST.md")
release=text("docs/RELEASE_NOTES.md")
verify=text("docs/VERIFICATION_SUMMARY.md")
closeout=text("docs/TERMINAL_CLOSEOUT.md")

try:
    ident=json.loads((root/"evidence/FROZEN_SUBJECT_IDENTITY.json").read_text())
except Exception as e:
    errors.append("identity malformed:"+str(e))
    ident={}

if ident.get("sha256")!=expected:
    errors.append("wrong frozen subject hash")
if ident.get("fresh_iqa")!="PASS":
    errors.append("fresh IQA not PASS")
if ident.get("owner_accepted") is not True or ident.get("frozen") is not True:
    errors.append("accept/freeze missing")

for term in ["v1.0.1","Fresh Independent IQA PASS",expected,repo_url,live_url,"v1.0.4"]:
    if term not in readme:
        errors.append("README missing:"+term)

for stale in ["PRE-IQA candidate","not independently reviewed","publication/deployment and live readback remain separate external-effect steps"]:
    if stale in readme:
        errors.append("stale README language:"+stale)

for term in ["v1.0.4","terminal-closeout","VERIFIED_TERMINAL_DONE / CLOSED"]:
    if term not in life+release+verify+closeout:
        errors.append("terminal projection status missing:"+term)

if linkedin_url not in life+closeout:
    errors.append("linkedin live URL missing from closeout")

required_post=[
    "Inspect the product. Challenge the workflow.",
    "Live build:","Public repository:","Day 10/30.","One verified release."
]
for term in required_post:
    if term not in post:
        errors.append("linkedin missing:"+term)
if len(re.findall(r"[^\n]*\?[^\n]*",post))!=1:
    errors.append("linkedin question count")

runtime=text("index.html")+text("app.js")
for bad in ["fetch(","XMLHttpRequest","https://cdn","<script src=\"http"]:
    if bad in runtime:
        errors.append("external runtime dependency:"+bad)

for rel in required_docs:
    body=text(rel)
    for stale in ["TODO","TBD","PLACEHOLDER"]:
        if stale in body:
            errors.append(rel+" contains "+stale)

print(json.dumps({"status":"PASS" if not errors else "FAIL","errors":errors},indent=2))
sys.exit(1 if errors else 0)
