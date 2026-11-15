#!/usr/bin/env python3
"""Frage-Karte als schwebendes Popup im Zitate-Look (Schatten, Unschärfe dahinter) + Zitate-Karte etwas höher, damit kein roter Balken nötig ist (Steuart, 15 Nov 2026; Variante ohne Fixierung, weil die untere Theorie-Leiste sonst überdeckt wird). Nach popup_fest_patch.py."""
import re, sys
p = "index.html"
s = open(p, encoding="utf-8").read()
if "/* popup-frage */" in s: sys.exit("already patched")
G = '.app[data-mode="game"] '
CSS = """
/* popup-frage */
.tlpop .tlcard.qv2{height:min(100%%,calc(27svh + 318px))}
%(G)s#gqpop{box-shadow:0 2px 18px rgba(0,0,0,.18);background:rgba(255,255,255,.93)!important;margin:10px 12px 0!important}
""" % {"G": G}
i = s.rindex("</style>"); s = s[:i] + CSS + s[i:]
m = re.search(r'name="app-version" content="(\d{4}-\d\d-\d\d)([a-z]?)"', s)
if m: s = s.replace(m.group(0), 'name="app-version" content="%s%s"' % (m.group(1), chr(ord(m.group(2) or "`") + 1)))
open(p, "w", encoding="utf-8").write(s); print("OK")
