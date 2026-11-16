#!/usr/bin/env python3
"""DOCH: Faktenkorrekturen nach Web-Prüfung (16 Nov): sein-Perfekt, Feber, Einkommensteuer."""
import re, sys
p="index.html"; s=open(p,encoding="utf-8").read()
if "AT; DE: haben" in s: sys.exit("already patched")
R=[
 ("(nicht: haben)","(AT; DE: haben)"),("(nicht: habe)","(AT; DE: habe)"),("(nicht: hat)","(AT; DE: hat)"),
 ("In Austria and the south, sitzen, stehen and liegen form the Perfekt with sein. In writing for exams, both forms are understood. Pick one and stay with it.","Duden marks sein as süddeutsch, österreichisch, schweizerisch. The standard form in Germany is haben. Both are understood."),
 ("Feber is also correct but you hear it less.","Feber is dated and now rare; most people say Februar."),
 ("Duden writes Einkommensteuer. You will also see Einkommenssteuer, but the standard form has no extra s.","German and Austrian tax law write Einkommensteuer. In everyday use you will also see Einkommenssteuer, and Swiss law uses it."),
 ("Duden: Einkommensteuer, without a joint.","Tax law in Germany and Austria: Einkommensteuer, without a joint."),
]
for a,b in R:
    if s.count(a)!=1: sys.exit("Anker fehlt: "+a)
    s=s.replace(a,b)
m=re.search(r'name="app-version" content="(\d{4}-\d\d-\d\d)([a-z]?)"',s)
s=s.replace(m.group(0),'name="app-version" content="%s%s"'%(m.group(1),chr(ord(m.group(2) or "`")+1)))
open(p,"w",encoding="utf-8").write(s); print("OK")
