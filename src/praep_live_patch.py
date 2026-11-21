#!/usr/bin/env python3
"""Präpositionen-Block live (2026-11-21d): src/praep_neu.js in index.html (Grammatik > Präpositionen & Fall > Theorie). Idempotent."""
import os,re
root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
p=os.path.join(root,"index.html");s=open(p,encoding="utf-8").read()
if "[praep-neu]" in s: print("already patched");raise SystemExit
js=open(os.path.join(root,"src","praep_neu.js"),encoding="utf-8").read()
a="return{render:open};})();";assert s.count(a)==1
s=s.replace(a,"return{render:open,U:{seg,hero,table,ART,CC,CAP,G,mix}};})();")
b="/* ---------- Sehen · Fälle: Artikel, Präpositionen, Roller ---------- */";assert s.count(b)==1
s=s.replace(b,js+b)
s=re.sub(r'<meta name="app-version" content="[^"]+">','<meta name="app-version" content="2026-11-21d">',s,count=1)
open(p,"w",encoding="utf-8").write(s);print("ok")
