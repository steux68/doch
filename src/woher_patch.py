#!/usr/bin/env python3
"""Woher-Formulierung (2026-11-21e): nicht die Frage 'Woher?' ist Dativ, sondern aus/von regieren den Dativ. Idempotent."""
import os,re
root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
p=os.path.join(root,"index.html");s=open(p,encoding="utf-8").read()
if "aus and von always take Dativ" in s: print("already patched");raise SystemExit
a="Woher is always Dativ: aus or von."
assert s.count(a)==1
s=s.replace(a,"aus and von always take Dativ.")
b="<b>Woher</b> kommst du? – Aus Wien."
assert s.count(b)==1
s=s.replace(b,"<b>Woher</b> kommst du? – <b>Aus</b> Wien. (aus, von + Dativ)")
s=re.sub(r'<meta name="app-version" content="[^"]+">','<meta name="app-version" content="2026-11-21e">',s,count=1)
open(p,"w",encoding="utf-8").write(s);print("ok")
