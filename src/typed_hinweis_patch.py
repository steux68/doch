#!/usr/bin/env python3
"""Tipp-Feld im Spiel: klarer Hinweis statt "Lücke schreiben …" (Steuart, 13 Nov 2026). Zählt app-version hoch.
Aufruf im Repo-Hauptordner: python3 src/typed_hinweis_patch.py"""
import re, sys
p = "index.html"
s = open(p, encoding="utf-8").read()
old = 'placeholder="Lücke schreiben …"'
if s.count(old) != 1:
    sys.exit("already patched oder Anker nicht gefunden")
s = s.replace(old, 'placeholder="Was gehört in die Lücke?"', 1)
m = re.search(r'name="app-version" content="(\d{4}-\d\d-\d\d)([a-z]?)"', s)
if m:
    nxt = chr(ord(m.group(2) or "`") + 1)
    s = s.replace(m.group(0), 'name="app-version" content="%s%s"' % (m.group(1), nxt), 1)
open(p, "w", encoding="utf-8").write(s)
print("OK")
