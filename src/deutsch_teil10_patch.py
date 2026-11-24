#!/usr/bin/env python3
"""DOCH: 'Lernen auf Deutsch' Teil 10 - Erklärungen zu falschen Antworten (window.WX, 1352 Einträge). Eigene Formulierung."""
import sys,re,json
sys.path.insert(0,"src/data")
from b1 import B as B1
from b2 import B as B2
from b3 import B as B3
from b4 import B as B4
p="index.html"; s=open(p,encoding="utf-8").read()
i=s.find("window.WX={"); j=s.find("};",i)
assert i>0 and j>i
d=json.loads(s[i+10:j+1])
T=B1+B2+B3+B4
assert len(T)==len(d)==1352
if d[next(iter(d))]==T[0]: sys.exit("already patched")
new={k:T[n] for n,k in enumerate(d)}
s=s[:i+10]+json.dumps(new,ensure_ascii=False,separators=(",",":"))+s[j+1:]
s,c=re.subn(r'(<meta name="app-version" content="2026-11-24)([a-z])(")',lambda m:m.group(1)+chr(ord(m.group(2))+1)+m.group(3),s,count=1)
assert c==1
open(p,"w",encoding="utf-8").write(s); print("ok")
