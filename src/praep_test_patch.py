#!/usr/bin/env python3
"""Testfassung: index.html + Präpositionen-Block -> praep2.html (index.html bleibt unverändert)."""
import os
root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
s=open(os.path.join(root,"index.html"),encoding="utf-8").read()
js=open(os.path.join(root,"src","praep_neu.js"),encoding="utf-8").read()
a="return{render:open};})();"
assert s.count(a)==1
s=s.replace(a,"return{render:open,U:{seg,hero,table,ART,CC,CAP,G,mix}};})();")
b="/* ---------- Sehen · Fälle: Artikel, Präpositionen, Roller ---------- */"
assert s.count(b)==1
s=s.replace(b,js+b)
s=s.replace('<meta name="app-version" content="','<meta name="app-version" content="TEST-praep2-',1)
open(os.path.join(root,"praep2.html"),"w",encoding="utf-8").write(s)
print("praep2.html written")
