#!/usr/bin/env python3
"""Popup-Kopf: Zähler mittig zwischen den Pfeilen, Thema darunter in kleiner Schrift – nichts wird mehr von den Pfeilen verdeckt (Steuart, 15 Nov 2026)."""
import re, sys
p = "index.html"
s = open(p, encoding="utf-8").read()
if "/* spiel-kopf */" in s: sys.exit("already patched")
if "/* spiel-aufgabe */" not in s: sys.exit("zuerst spiel_aufgabe_patch.py")
A = '.app[data-mode="game"] '
CSS = """
/* spiel-kopf */
%(A)s#gqpop{padding-top:60px!important}
%(A)s#panel .card.df .top{flex-direction:column!important;justify-content:flex-start!important;gap:0!important;height:54px!important;padding-top:7px!important;left:52px!important;right:52px!important;white-space:normal!important;text-overflow:clip!important}
%(A)s#panel #pcn{order:-1;margin:0!important;font-size:14px!important;line-height:22px}
%(A)s#panel #bd{font-size:11px!important;letter-spacing:.04em!important;line-height:15px;max-width:100%%;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;color:#777}
""" % {"A": A}
i = s.rindex("</style>"); s = s[:i] + CSS + s[i:]
m = re.search(r'name="app-version" content="(\d{4}-\d\d-\d\d)([a-z]?)"', s)
if m: s = s.replace(m.group(0), 'name="app-version" content="%s%s"' % (m.group(1), chr(ord(m.group(2) or "`") + 1)))
open(p, "w", encoding="utf-8").write(s); print("OK")
