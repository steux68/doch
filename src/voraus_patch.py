#!/usr/bin/env python3
"""Zuerst-Zeile (Voraussetzungen) live (2026-11-21f): uebernimmt die geprueften CSS/JS-Bloecke aus voraus.html. Idempotent."""
import os,re
root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
p=os.path.join(root,"index.html");s=open(p,encoding="utf-8").read()
if 'id="pre-css"' in s: print("already patched");raise SystemExit
v=open(os.path.join(root,"voraus.html"),encoding="utf-8").read()
i=v.index('<style id="pre-css">');blk=v[i:]
assert blk.count('<script id="pre-js">')==1 and v.count('<style id="pre-css">')==1
s=s+blk
s=re.sub(r'<meta name="app-version" content="[^"]+">','<meta name="app-version" content="2026-11-21f">',s,count=1)
open(p,"w",encoding="utf-8").write(s);print("ok")
