#!/usr/bin/env python3
"""Ergänzen-Modus (Tippen) nicht bei Wortstellungs-Fragen (Steuart, 13 Nov 2026): Wenn alle Antworten dieselben
Wörter in anderer Reihenfolge sind (z. B. "meiner Mutter einen Ring" / "einen Ring meiner Mutter"), gibt es nichts
zu tippen, das man nicht schon sieht; dann bleibt es bei der Auswahl. Zählt app-version hoch.
Aufruf im Repo-Hauptordner: python3 src/typed_wortstellung_patch.py"""
import re, sys
p = "index.html"
s = open(p, encoding="utf-8").read()
if "const sameWords=" in s:
    sys.exit("already patched")
old = 'const canType=q=>store.typ&&q.s.includes("___")&&q.k!=="c"&&q.o[q.c].length<=24;'
new = ('const sameWords=q=>{const k=o=>o.split(/\\s+/).sort().join(" ");return q.o.every(x=>k(x)===k(q.o[0]));};\n'
       'const canType=q=>store.typ&&q.s.includes("___")&&q.k!=="c"&&q.o[q.c].length<=24&&!sameWords(q);')
if s.count(old) != 1:
    sys.exit("Anker nicht gefunden")
s = s.replace(old, new, 1)
m = re.search(r'name="app-version" content="(\d{4}-\d\d-\d\d)([a-z]?)"', s)
if m:
    nxt = chr(ord(m.group(2) or "`") + 1)
    s = s.replace(m.group(0), 'name="app-version" content="%s%s"' % (m.group(1), nxt), 1)
open(p, "w", encoding="utf-8").write(s)
print("OK")
