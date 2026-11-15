#!/usr/bin/env python3
"""DOCH Titelseite: das senkrechte Credit (steux) sitzt höher und verdeckt nicht mehr 'Redewendungen'."""
import re, sys
p="index.html"; s=open(p,encoding="utf-8").read()
if "/* credit-hoch */" in s: sys.exit("already patched")
old="f.style.setProperty('--cb',Math.max(60,innerHeight-b+14)+'px');"
if s.count(old)!=1: sys.exit("Anker")
s=s.replace(old,"/* credit-hoch */var up=(on&&t)?72:0;f.style.setProperty('--cb',(Math.max(60,innerHeight-b+14)+up)+'px');")
m=re.search(r'name="app-version" content="(\d{4}-\d\d-\d\d)([a-z]?)"',s)
s=s.replace(m.group(0),'name="app-version" content="%s%s"'%(m.group(1),chr(ord(m.group(2) or "`")+1)))
open(p,"w",encoding="utf-8").write(s); print("OK")
