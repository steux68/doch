#!/usr/bin/env python3
"""Legende TEKAMOLO: Verb-Eintrag, einzeilig; Mo wirklich weiss (spaetere Regeln ueberstimmen)."""
import re
p="index.html"; s=open(p,encoding="utf-8").read()
if "legende2-css" in s: raise SystemExit("already patched")
o="""lg:'<span><i class="sw te"></i> Te wann?</span>"""
assert s.count(o)==1
s=s.replace(o,"""lg:'<span><i class="sw" style="background:var(--mkey)"></i> Verb</span><span><i class="sw te"></i> Te wann?</span>""")
css='''<style id="legende2-css">
.app[data-mode="learn"] #lg:has(.sw){width:100%;max-width:none;margin:0;box-sizing:border-box;gap:0 6px;flex-wrap:nowrap;white-space:nowrap;font-size:12px;padding:8px 0}
.app[data-mode="learn"] #lg:has(.sw) span{gap:4px}\n.app[data-mode="learn"] #lg .sw{width:10px!important}
.app #stage .tkm .mo,.app .lg .sw.mo,.app .sw.mo,.app .mo{background-color:#fff!important;
 background-image:repeating-linear-gradient(to right,#b8b8b8 0 1px,transparent 1px 3px),repeating-linear-gradient(to right,#b8b8b8 0 1px,transparent 1px 3px)!important;
 background-size:100% 1px,100% 1px!important;background-position:left top,left bottom!important;background-repeat:no-repeat!important}
</style>
'''
s=s.replace("</head>",css+"</head>")
s,c=re.subn(r'(<meta name="app-version" content="2026-11-24)([a-z])(")',lambda m:m.group(1)+chr(ord(m.group(2))+1)+m.group(3),s,count=1); assert c==1
open(p,"w",encoding="utf-8").write(s)
