#!/usr/bin/env python3
"""Teil 11: letzter Rest (Zungenbrecher h)."""
import re
p="index.html"; s=open(p,encoding="utf-8").read()
o="Breathe out softly for h. Do not drop it and do not press it."
if o not in s: raise SystemExit("already patched")
s=s.replace(o,"Atme für h weich aus. Lass es nicht weg und presse es nicht.")
s,c=re.subn(r'(<meta name="app-version" content="2026-11-24)([a-z])(")',lambda m:m.group(1)+chr(ord(m.group(2))+1)+m.group(3),s,count=1); assert c==1
open(p,"w",encoding="utf-8").write(s)
