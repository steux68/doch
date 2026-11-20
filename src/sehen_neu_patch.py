#!/usr/bin/env python3
"""Sehen neu (2026-11-21): puts src/sehen_neu.js and src/sehen_neu.css into index.html.
Old renderSehen is kept as renderSehenOld (fallback). Idempotent."""
import re,sys,os
root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
p=os.path.join(root,"index.html");s=open(p,encoding="utf-8").read()
js=open(os.path.join(root,"src","sehen_neu.js"),encoding="utf-8").read()
css=open(os.path.join(root,"src","sehen_neu.css"),encoding="utf-8").read()
if "[sehen-neu]" in s:
    # refresh: drop previous blocks first
    s=re.sub(r"/\* ---------- Sehen neu \(2026-11-21\).*?function renderSehen\(\)\{if\(SV\.tab===\"k\"&&SV\.kp&&SV\.kp!==\"s\"\)return renderSehenX\(\);return SNEW\.render\(\);\}\n","",s,flags=re.S)
    s=re.sub(r"/\* ---- Sehen neu \[sehen-neu\] ---- \*/.*?\.snw\{[^}]*\}\n","",s,flags=re.S)
else:
    old='function renderSehen(){if(SV.tab==="k"&&SV.kp&&SV.kp!=="s")return renderSehenX();const th='
    assert s.count(old)==1
    s=s.replace(old,'function renderSehenOld(){if(SV.tab==="k"&&SV.kp&&SV.kp!=="s")return renderSehenX();const th=')
a='/* ---------- Sehen · Fälle: Artikel, Präpositionen, Roller ---------- */'
assert s.count(a)==1
s=s.replace(a,js+a)
b='.svln{position:absolute;left:0;top:0;width:100%;height:100%;pointer-events:none;overflow:visible}\n'
assert s.count(b)==1
s=s.replace(b,b+css)
m=re.search(r'<meta name="app-version" content="([^"]+)">',s)
open(p,"w",encoding="utf-8").write(s)
print("ok, version",m.group(1))
