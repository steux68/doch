#!/usr/bin/env python3
"""Frage-Karte frei schwebend (fixiert, oben) über verschwommener Seite; Theorie-Leiste fix am unteren Rand (Steuart, 15 Nov 2026). Nach popup_frage_patch.py."""
import re, sys
p = "index.html"
s = open(p, encoding="utf-8").read()
if "/* popup-frei */" in s: sys.exit("already patched")
G = '.app[data-mode="game"] '
CSS = """
/* popup-frei */
%(G)s#gqpop{position:fixed!important;top:108px;left:50%%;transform:translateX(-50%%);width:min(calc(100%% - 24px),520px);box-sizing:border-box;margin:0!important;z-index:60}
.app[data-mode="game"]::after{content:"";position:fixed;left:0;right:0;bottom:0;top:100px;z-index:55;pointer-events:none;background:rgba(255,255,255,.5);-webkit-backdrop-filter:blur(3px);backdrop-filter:blur(3px)}
%(G)s#tabar{position:fixed;left:0;right:0;bottom:6px;z-index:61}
.app.kbo[data-mode="game"] #gqpop{top:40px}
.app.kbo[data-mode="game"]::after{top:34px}
""" % {"G": G}
i = s.rindex("</style>"); s = s[:i] + CSS + s[i:]
m = re.search(r'name="app-version" content="(\d{4}-\d\d-\d\d)([a-z]?)"', s)
if m: s = s.replace(m.group(0), 'name="app-version" content="%s%s"' % (m.group(1), chr(ord(m.group(2) or "`") + 1)))
open(p, "w", encoding="utf-8").write(s); print("OK")
