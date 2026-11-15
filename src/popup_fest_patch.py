#!/usr/bin/env python3
"""Feste Größe für Frage-Karte und Popups (Zitate/Geschichte), leicht durchscheinend mit Unschärfe dahinter (Steuart, 15 Nov 2026)."""
import re, sys
p = "index.html"
s = open(p, encoding="utf-8").read()
if "/* popup-fest */" in s: sys.exit("already patched")
G = '.app[data-mode="game"] '
CSS = """
/* popup-fest */
%(G)s#gqpop{height:420px;box-sizing:border-box;overflow-y:auto;overflow-x:hidden;scrollbar-width:none;background:rgba(255,255,255,.9)!important;-webkit-backdrop-filter:blur(6px);backdrop-filter:blur(6px)}
%(G)s#gqpop::-webkit-scrollbar{display:none}
%(G)s#panel .btns{position:absolute;left:12px;right:12px;bottom:8px;margin:0;z-index:1}
%(G)s#panel #btns1{right:auto}
%(G)s#panel #btns2{left:auto}
%(G)s#gqpop{padding-bottom:36px!important}
.app.kbo #gqpop{height:min(300px,calc(var(--vvh,400px) - 72px))}
.tlpop .tlcard{height:min(100%%,640px);background:rgba(255,255,255,.93);-webkit-backdrop-filter:blur(6px);backdrop-filter:blur(6px)}
.tlpop .tlcard.qv2{height:min(100%%,calc(27svh + 285px))}
.qv2 .qvimg{width:min(calc(100%% - 24px),27svh)}
.tlpop{background:rgba(255,255,255,.5);-webkit-backdrop-filter:blur(3px);backdrop-filter:blur(3px)}
""" % {"G": G}
i = s.rindex("</style>"); s = s[:i] + CSS + s[i:]
m = re.search(r'name="app-version" content="(\d{4}-\d\d-\d\d)([a-z]?)"', s)
if m: s = s.replace(m.group(0), 'name="app-version" content="%s%s"' % (m.group(1), chr(ord(m.group(2) or "`") + 1)))
open(p, "w", encoding="utf-8").write(s); print("OK")
