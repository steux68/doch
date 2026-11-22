#!/usr/bin/env python3
"""2026-11-22i Sehen: Bildung, Gebrauch, Signale, Achtung immer alle offen (kein '+'). Idempotent."""
import os, re, sys
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
p = os.path.join(root, "index.html")
s = open(p, encoding="utf-8").read()
if 'id="acc-offen-css"' in s:
    print("already patched"); sys.exit()
old = """(st.r==r[0]?esc(r[2]):'<span style="color:#aaa">+</span>')"""
assert s.count(old) == 1, s.count(old)
s = s.replace(old, "esc(r[2])")
css = ('<style id="acc-offen-css">'
       '.sn .svr{height:auto;min-height:28px;white-space:normal;align-items:flex-start;padding:7px 2px;line-height:1.3;cursor:default}'
       '.sn .svr span:first-child{padding-top:1px}'
       '.sn .svr span:last-child{flex:1 1 auto;min-width:0}'
       '</style>\n')
s = s.rstrip("\n") + "\n" + css
s = re.sub(r'<meta name="app-version" content="[^"]+">', '<meta name="app-version" content="2026-11-22i">', s, count=1)
open(p, "w", encoding="utf-8").write(s); print("ok")
