#!/usr/bin/env python3
"""Rueckmeldung bei falscher Wahl live (2026-11-21g): uebernimmt den geprueften Block aus falsch.html. Idempotent."""
import os,re
root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
p=os.path.join(root,"index.html");s=open(p,encoding="utf-8").read()
if 'id="wx-js"' in s: print("already patched");raise SystemExit
v=open(os.path.join(root,"falsch.html"),encoding="utf-8").read()
assert v.count('<script id="wx-js">')==1
s=s+v[v.index('<script id="wx-js">'):]
s=re.sub(r'<meta name="app-version" content="[^"]+">','<meta name="app-version" content="2026-11-21g">',s,count=1)
open(p,"w",encoding="utf-8").write(s);print("ok")
