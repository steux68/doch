#!/usr/bin/env python3
"""Titelleiste halbtransparent über dem scrollenden Inhalt + Ergebnis-Karten (Lückentext/Text prüfen) im Popup-Stil (Steuart, 15 Nov 2026). Nach text_popup_patch.py."""
import re, sys
p = "index.html"
s = open(p, encoding="utf-8").read()
if "/* text-popup2 */" in s: sys.exit("already patched")
if "/* text-popup */" not in s: sys.exit("zuerst text_popup_patch.py")
T = '.app[data-mode="theo"] '
CSS = """
/* text-popup2 */
%(T)s#lres .tc,%(T)s#wres .tc{background:rgba(255,255,255,.94);border:1px dotted #b9b9b5;margin:8px 10px;padding:12px 12px 10px}
%(T)s#lres .tc>h3,%(T)s#wres .tc>h3{font-size:14px!important;font-weight:400!important;letter-spacing:.06em!important;text-transform:none!important;color:#555!important;text-align:center;margin:0 0 10px!important}
%(T)s#lres .tc>p:not(.tline),%(T)s#wres .tc>p:not(.tline){color:#3a7a1f!important;font-weight:400!important}
#topic .titlebar{position:relative;z-index:3;background:rgba(255,255,255,.92)!important}
%(T)s#topic .theo{margin-top:-44px;padding-top:50px}
""" % {"T": T}
i = s.rindex("</style>"); s = s[:i] + CSS + s[i:]
m = re.search(r'name="app-version" content="(\d{4}-\d\d-\d\d)([a-z]?)"', s)
if m: s = s.replace(m.group(0), 'name="app-version" content="%s%s"' % (m.group(1), chr(ord(m.group(2) or "`") + 1)))
open(p, "w", encoding="utf-8").write(s); print("OK")
