#!/usr/bin/env python3
"""DOCH: Farblegende auch in Lernen zeigen (Themen mit Farbfeldern, z. B. TEKAMOLO); Mo bekommt eine eigene Farbe (weiss mit gepunktetem Rahmen), damit es nicht wie ein Verb aussieht."""
import re
p="index.html"; s=open(p,encoding="utf-8").read()
if 'id="legende-lernen-css"' in s: raise SystemExit("already patched")
css='''<style id="legende-lernen-css">
.app[data-mode="learn"] #lg:has(.sw){display:flex!important;justify-content:center;align-items:center;gap:0 12px;flex-wrap:wrap;white-space:normal;padding:8px 0;min-height:0;font-size:12px;color:var(--fg);
 background:repeating-linear-gradient(to right,#b8b8b8 0 1px,transparent 1px 3px) left bottom/100% 1px no-repeat}
.app[data-mode="learn"] #lg .sw{width:14px;height:10px}
.mo,.lg .sw.mo,.tkm .mo{background:#fff;
 background-image:repeating-linear-gradient(to right,#b8b8b8 0 1px,transparent 1px 3px),repeating-linear-gradient(to right,#b8b8b8 0 1px,transparent 1px 3px);
 background-size:100% 1px,100% 1px;background-position:left top,left bottom;background-repeat:no-repeat}
</style>
'''
assert s.count("</head>")==1
s=s.replace("</head>",css+"</head>")
s,c=re.subn(r'(<meta name="app-version" content="2026-11-24)([a-z])(")',lambda m:m.group(1)+chr(ord(m.group(2))+1)+m.group(3),s,count=1); assert c==1
open(p,"w",encoding="utf-8").write(s)
