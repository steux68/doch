#!/usr/bin/env python3
"""Sehen: keine Doppellinien, Raten ohne Vorab-Farbe, Tabelle weiter nach oben (2026-11-23c). Marker [sehen-raten]. Idempotent."""
import sys
P="index.html"
s=open(P,encoding="utf-8").read()
if "[sehen-raten]" in s:
    print("schon angewendet"); sys.exit(0)
def rep(a,b):
    global s
    assert s.count(a)==1,("Treffer != 1:",s.count(a),a[:80])
    s=s.replace(a,b)
# Tabelle direkt unter die Auswahl, Beschriftung nur "Antippen"
rep("""h+=acc(x)+'<div class="snc" style="display:block;padding:8px 8px 0">Artikel · antippen</div>'+table(c,g);return h;}""",
    """h+='<div class="snc snant">Antippen</div>'+table(c,g)+acc(x);return h;}""")
rep("app-version\" content=\"2026-11-23b\"","app-version\" content=\"2026-11-23c\"")
css="""/* [sehen-raten] */
.sn .snctl{background:var(--dfv) left top/1px 100% no-repeat}
.sn .snant{display:block;padding:6px 8px 0}
.snt{margin:2px 0 6px}
.sn .snrat.on{background-color:transparent;font-weight:700;color:#111}
.sn .snhw .np[style*="#ededeb"]:empty{background:none}
"""
rep("/* [sehen-verben] */\n</style>","/* [sehen-verben] */\n"+css+"</style>")
open(P,"w",encoding="utf-8").write(s)
print("ok")
