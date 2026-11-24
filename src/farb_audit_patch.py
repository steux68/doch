#!/usr/bin/env python3
"""DOCH: Farb-Audit 24 Nov - Genitiv/Ka dunkler (#a98ae0), TEKAMOLO Mo #c8c8c8 (CVD-Abstand)."""
import re
p="index.html"; s=open(p,encoding="utf-8").read()
a=s.count("#c4a6ee"); b=s.count("#d4d4d4")
if a==0 and b==0: raise SystemExit("already patched")
s=s.replace("#c4a6ee","#a98ae0").replace("#d4d4d4","#c8c8c8")
s,c=re.subn(r'(<meta name="app-version" content="2026-11-24)([a-z])(")',lambda m:m.group(1)+chr(ord(m.group(2))+1)+m.group(3),s,count=1); assert c==1
open(p,"w",encoding="utf-8").write(s); print("ok",a,b)
