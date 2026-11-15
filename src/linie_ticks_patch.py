#!/usr/bin/env python3
"""DOCH Startseite: Titelleisten-Linie bleibt bei gestapelten Leisten, die oberen Leisten verlieren ihre eigene obere Linie,
Rahmenmarken sitzen genau auf der Linie (vorher 1 px tiefer) und haben dasselbe Strichmuster/Farbe (Steuart, 15 Nov 2026)."""
import re, sys
p = "index.html"
s = open(p, encoding="utf-8").read()
if "/* linie-ticks */" in s: sys.exit("already patched")
for old in ("#home:has(.hbody.tstk) .titlebar::after{border-color:transparent;background-image:none}\n",
            "/* 15 Nov: bars stacked at the top: only the bars' own dotted lines show; no dashed header line or frame ticks under them */\n",
            ".app:has(#home:not([hidden]) .hbody.tstk) .tk.t{visibility:hidden}\n"):
    if old not in s: sys.exit("Anker fehlt: " + old[:50])
    s = s.replace(old, "")
if s.count(".tk.t{top:52px}") != 1: sys.exit("tk.t-Anker")
s = s.replace(".tk.t{top:52px}", ".tk.t{top:51px}")
i = s.index(".home .titlebar::after{")
j = s.index("}", i)
seg = s[i:j].replace("var(--line) 0 4px", "#b8b8b8 0 4px")
s = s[:i] + seg + s[j:]
CSS = """/* linie-ticks */
.hb.stt.hl{background:var(--bl) left bottom/100% 1px no-repeat,var(--hv) right top/1px 100% no-repeat,#fff}
.hb.stt.hr{background:var(--bl) left bottom/100% 1px no-repeat,var(--hv) left top/1px 100% no-repeat,#fff}
.tk{--t:repeating-linear-gradient(to right,#b8b8b8 0 4px,transparent 4px 7px)}
"""
k = s.rindex("</style>"); s = s[:k] + CSS + s[k:]
old = "if(r.top<=R.top+t+.5)tb=Math.max(tb,r.bottom);"
if s.count(old) != 1: sys.exit("JS-Anker")
s = s.replace(old, "const st=r.top<=R.top+t+.5;b.classList.toggle('stt',st);if(st)tb=Math.max(tb,r.bottom);")
n = s.count("transparent 4px 6px"); s = s.replace("transparent 4px 6px", "transparent 4px 7px")
old2 = "if(hl!==null)set(t,hl,11);"
if s.count(old2) != 1: sys.exit("place-Anker")
s = s.replace(old2, "if(hl!==null)set(t,hl-(tbs.length?1:0),11);")
m = re.search(r'name="app-version" content="(\d{4}-\d\d-\d\d)([a-z]?)"', s)
if m: s = s.replace(m.group(0), 'name="app-version" content="%s%s"' % (m.group(1), chr(ord(m.group(2) or "`") + 1)))
open(p, "w", encoding="utf-8").write(s); print("OK", n)
