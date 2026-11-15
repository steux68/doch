#!/usr/bin/env python3
"""Lückentext + Text prüfen im ruhigen Popup-Stil (Steuart, 15 Nov 2026): weiße gepunktete Karten, kleine Überschriften,
helle Farben; bei geöffneter Tastatur Aufgabenkarte ausgeblendet, Text-/Lückenfeld nutzt den Platz."""
import re, sys
p = "index.html"
s = open(p, encoding="utf-8").read()
if "/* text-popup */" in s: sys.exit("already patched")
T = '.app[data-mode="theo"] '
CARDS = ",".join(T + ".tc:has(%s)" % x for x in ("#llv", "#ltx", "#wlv", "#wtx"))
H3 = ",".join(T + ".tc:has(%s)>h3" % x for x in ("#llv", "#ltx", "#wlv", "#wtx"))
CSS = """
/* text-popup */
%(CARDS)s{background:rgba(255,255,255,.94);border:1px dotted #b9b9b5;margin:8px 10px;padding:12px 12px 10px}
%(H3)s{font-size:14px!important;font-weight:400!important;letter-spacing:.06em!important;text-transform:none!important;color:#555!important;text-align:center;margin:0 0 10px!important}
%(T)s#llv button,%(T)s#wlv button{background:#fff;border:1px dotted #b9b9b5;color:#555;font-weight:400;padding:4px 12px}
%(T)s#llv button[aria-pressed="true"],%(T)s#wlv button[aria-pressed="true"]{background:#fff3a8!important;border:1px dotted #b9a64a;color:#222;font-weight:400!important}
%(T)s#ltask,%(T)s#wtask{border:1px dotted #999;background:#fff!important;background-image:none!important;font-size:15px}
%(T)s#wtx{border:1px dotted #999;background:#fff!important;background-image:none!important;min-height:220px}
%(T)s .lg.fld{border-bottom:1px dotted #555;background:#fff!important;background-image:none!important}
%(T)s .lg.ok{background:#eef8e8!important;color:#3a7a1f}
%(T)s .lg.bad{background:#fdeeee!important;color:#b3262f}
%(T)s .lg.near{background:#fff8d0!important}
%(T)s .lbtn button.primary,%(T)s .wrow button.primary{background:#fff3a8!important;border:1px dotted #b9a64a;font-weight:400}
%(T)s .tline,%(T)s .wprompt{font-size:14px;color:#666}
.app.kbt{min-height:0!important;height:var(--vvh,100%%)!important;overflow:hidden}
.app.kbt .tc:has(#wlv),.app.kbt .tc:has(#llv){display:none}
.app.kbt #wtx{min-height:0!important;height:calc(var(--vvh,400px) - 235px)}
.app.kbt .tc:has(#ltx){max-height:calc(var(--vvh,400px) - 70px);overflow:auto}
.app.kbt .titlebar{height:34px}
.app.kbt #tabar,.app.kbt .abar,.app.kbt .tline{display:none!important}
""" % {"CARDS": CARDS, "H3": H3, "T": T}
i = s.rindex("</style>"); s = s[:i] + CSS + s[i:]
JS = """<script id="textkb-js">(function(){var app=document.querySelector(".app"),vv=window.visualViewport;
function kt(){var a=document.activeElement,ok=a&&(a.id==="wtx"||(a.classList&&a.classList.contains("lg")))&&app.dataset.mode==="theo";
var h=vv?vv.height:innerHeight,open=!!ok&&h<innerHeight*.8;document.documentElement.style.setProperty("--vvh",Math.round(h)+"px");app.classList.toggle("kbt",open);if(open){scrollTo(0,0);if(a.scrollIntoView)a.scrollIntoView({block:"center"});}}
if(vv)vv.addEventListener("resize",kt);addEventListener("focusin",function(){setTimeout(kt,350)});addEventListener("focusout",function(){setTimeout(kt,350)});})();</script>
"""
j = s.rindex("</script>") + len("</script>"); s = s[:j] + "\n" + JS + s[j:]
m = re.search(r'name="app-version" content="(\d{4}-\d\d-\d\d)([a-z]?)"', s)
if m: s = s.replace(m.group(0), 'name="app-version" content="%s%s"' % (m.group(1), chr(ord(m.group(2) or "`") + 1)))
open(p, "w", encoding="utf-8").write(s); print("OK")
