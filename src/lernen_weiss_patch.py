#!/usr/bin/env python3
"""DOCH: Lernen-Karten ohne grosse Leerflaeche: Karte oben, Erklaerung direkt darunter, Rest unten. Idempotent."""
import re, sys
p="index.html"; s=open(p,encoding="utf-8").read()
if 'id="lernen-weiss-css"' in s: sys.exit("already patched")
css='''<style id="lernen-weiss-css">
.app[data-mode="learn"] #stagew{flex:0 0 auto!important}
.app[data-mode="learn"] #stage{min-height:0!important;flex:0 0 auto!important;justify-content:flex-start!important;padding-top:8px!important;padding-bottom:8px!important}
.app[data-mode="learn"] #panel{margin-bottom:auto!important}
</style>
'''
i=s.rfind('</style>'); assert i>0
j=s.index('\n',i)+1
s=s[:j]+css+s[j:]
m=re.search(r'name="app-version" content="(\d{4}-\d\d-\d\d)([a-z]?)"',s)
new=m.group(1)+chr(ord(m.group(2) or "`")+1)
s=s.replace(m.group(0),'name="app-version" content="%s"'%new)
open(p,"w",encoding="utf-8").write(s); print("OK",new)
