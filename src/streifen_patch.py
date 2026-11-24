#!/usr/bin/env python3
"""DOCH Startseite: untere Menuestreifen: Staunen-Rueckleiste direkt anschliessend (kein Weissstreifen),
genau eine gepunktete Linie zwischen zwei Streifen (oben je Streifen, unten nur der letzte). Idempotent."""
import re, sys
p="index.html"; s=open(p,encoding="utf-8").read()
if 'id="streifen-css"' in s: sys.exit("already patched")
D='repeating-linear-gradient(to right,rgba(0,0,0,.3) 0 1px,transparent 1px 3px)'
css='''<style id="streifen-css">
html body #hscroll>.hb.hb[data-i]{background-image:none!important}
html body #hscroll>.hb.hb[data-i]::before{content:""!important;position:absolute!important;left:0!important;right:0!important;top:0!important;height:1px!important;z-index:2!important;pointer-events:none!important;background:%s!important}
html body #hscroll>.hb.hb[data-i]::after{content:""!important;position:absolute!important;left:0!important;right:0!important;bottom:0!important;top:auto!important;height:1px!important;z-index:2!important;pointer-events:none!important;background:%s!important}
html body #hscroll>.hb.hb.nb[data-i]::after{display:none!important}
html[data-dmode="s"] #hscroll>.hb.hb[data-i="3"]{margin-top:0!important}
html[data-dmode="s"] #hscroll>.hb.hb[data-i="2"]::after{display:none!important}
</style>
''' % (D,D)
i=s.rfind('</style>'); assert i>0
j=s.index('\n',i)+1
s=s[:j]+css+s[j:]
m=re.search(r'name="app-version" content="(\d{4}-\d\d-\d\d)([a-z]?)"',s)
new=m.group(1)+chr(ord(m.group(2) or "`")+1)
s=s.replace(m.group(0),'name="app-version" content="%s"'%new)
open(p,"w",encoding="utf-8").write(s); print("OK",new)
