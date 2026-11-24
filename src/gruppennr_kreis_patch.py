#!/usr/bin/env python3
"""DOCH Start: Gruppennummern rund: geschlossen grau (#777), offen schwarz (#1a1a1a), Zahl weiss."""
import re
p="index.html"; s=open(p,encoding="utf-8").read()
if 'id="gruppennr-css"' in s: raise SystemExit("already patched")
css='<style id="gruppennr-css">.grp:not(.open) .grh .no{background:#777!important;color:#fff!important;border-radius:50%!important}.grp.open .grh .no{border-radius:50%!important;background:#1a1a1a!important;color:#fff!important}</style>'
s=s.rstrip("\n")+"\n"+css+"\n"
s,c=re.subn(r'(<meta name="app-version" content="2026-11-24)([a-z])(")',lambda m:m.group(1)+chr(ord(m.group(2))+1)+m.group(3),s,count=1); assert c==1
open(p,"w",encoding="utf-8").write(s); print("ok")
