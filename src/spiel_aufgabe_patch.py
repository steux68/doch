#!/usr/bin/env python3
"""Spiel/Test: Aufgabenzeile 'Ergänze: …' über dem Eingabefeld + Karte 94 % weiß (Steuart, 15 Nov 2026). Nach spiel_elegant_patch.py."""
import re, sys
p = "index.html"
s = open(p, encoding="utf-8").read()
if "/* spiel-aufgabe */" in s: sys.exit("already patched")
if "/* spiel-elegant */" not in s: sys.exit("zuerst spiel_elegant_patch.py ausführen")
A = '.app[data-mode="game"] '
CSS = """
/* spiel-aufgabe */
%(A)s#gqpop{background:rgba(255,255,255,.94)!important}
%(A)s#panel #task{font-size:13px;line-height:1.3;color:#777;text-align:center;margin:-4px 0 8px;letter-spacing:.02em}
%(A)s#panel #task b{font-weight:400;color:#222}
""" % {"A": A}
i = s.rindex("</style>"); s = s[:i] + CSS + s[i:]
JS = """<script id="aufgabe-js">(function(){var M={art:"Artikel",prep:"Präposition",vprep:"Präposition",rel:"Relativpronomen",praes:"Verb in der richtigen Form",modal:"Modalverb in der richtigen Form"};
setInterval(function(){var a=document.getElementById("ans");if(!a)return;var w=a.closest(".answer")||a.parentNode,t=document.getElementById("task");var q;try{q=MC.list[MC.i];}catch(e){}var k=q&&q.t,txt=k&&M[k];if(!txt)txt="fehlendes Wort";var h="Ergänze: <b>"+txt+"</b>";if(!t){t=document.createElement("div");t.id="task";w.parentNode.insertBefore(t,w);}if(t.innerHTML!==h)t.innerHTML=h;},150);})();</script>
"""
j = s.rindex("</script>") + len("</script>"); s = s[:j] + "\n" + JS + s[j:]
m = re.search(r'name="app-version" content="(\d{4}-\d\d-\d\d)([a-z]?)"', s)
if m:
    s = s.replace(m.group(0), 'name="app-version" content="%s%s"' % (m.group(1), chr(ord(m.group(2) or "`") + 1)))
open(p, "w", encoding="utf-8").write(s); print("OK")
