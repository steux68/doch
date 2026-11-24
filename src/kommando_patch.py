#!/usr/bin/env python3
"""DOCH Startseite Grammatik: Kommandoleiste oben (Level + Heute/Weitermachen/Fehler), darunter Zeiten/Faelle;
Fortschritt = gepunktete Linie mit rotem Punkt an der Stelle. Idempotent."""
import re, sys
p="index.html"; s=open(p,encoding="utf-8").read()
if 'id="kommando-css"' in s: sys.exit("already patched")
D='repeating-linear-gradient(to right,#b8b8b8 0 1px,transparent 1px 3px)'
css='''<style id="kommando-css">
#p-home .lvsel{order:1!important;margin:8px 0 0!important}
#p-home .rcb{order:2!important;margin:0 0 8px!important}
#p-home #sehb{order:3!important;margin:0 0 12px!important}
#p-home #groups{order:4!important}
.tt .pk{height:1px!important;background:%s!important;margin:0 4px!important;position:relative!important;overflow:visible!important}
.tt .pk i{display:block!important;position:absolute!important;left:0!important;top:0!important;height:0!important;background:none!important;max-width:100%%!important}
.tt .pk i::after{content:"";position:absolute;right:-4px;top:-4px;width:8px;height:8px;border-radius:50%%;background:#e30613}
.gl .tt.dim .pk i::after{background:#c9cbc6}
</style>
''' % D
i=s.rfind('</style>'); assert i>0
j=s.index('\n',i)+1
s=s[:j]+css+s[j:]
m=re.search(r'name="app-version" content="(\d{4}-\d\d-\d\d)([a-z]?)"',s)
new=m.group(1)+chr(ord(m.group(2) or "`")+1)
s=s.replace(m.group(0),'name="app-version" content="%s"'%new)
open(p,"w",encoding="utf-8").write(s); print("OK",new)
