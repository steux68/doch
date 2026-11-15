#!/usr/bin/env python3
"""Spiel/Test im dasein-design-Popup-Stil (Steuart, 15 Nov 2026): weiße Karte, feine gepunktete Linien,
helles Grün/Rot, W/E-Kompasspfeile ohne abgeschnittenes Label. Nach spiel_popup_patch.py ausführen."""
import re, sys
p = "index.html"
s = open(p, encoding="utf-8").read()
if "/* spiel-elegant */" in s: sys.exit("already patched")
if "/* spiel-popup */" not in s: sys.exit("zuerst spiel_popup_patch.py ausführen")
A = '.app[data-mode="game"] '
CSS = """
/* spiel-elegant */
%(A)s#gqpop{background:#fff;border:1px dotted #b9b9b5;padding:46px 12px 8px}
%(A)s#stagew,%(A)s#panel{font-family:Carlito,Calibri,sans-serif}
%(A)s#gnav button svg,%(A)s #gnav svg{overflow:visible}
%(A)s#gnav .rg{fill:none;stroke:#3a3c37;stroke-width:.7}
%(A)s#gnav .dt{fill:#4d4f4a;stroke:#1a1a1a;stroke-width:.5;stroke-linejoin:round}
%(A)s#gnav text{fill:#3a3c37;font:700 6.4px Carlito,Calibri,sans-serif;text-anchor:middle;dominant-baseline:central}
%(A)s#gnav .tr{display:none}
%(A)s#gnav button{width:34px;height:34px}
%(A)s#gnav button svg{width:30px;height:30px}
%(A)s#gnav{top:6px;left:14px;right:14px;height:34px}
%(A)s#panel .card.df .top{top:0;left:56px;right:56px;height:46px;font-size:14px;letter-spacing:.06em;text-transform:none;color:#555}
%(A)s#panel .card.df .top *{font-size:14px;letter-spacing:.06em}
%(A)s#panel #tx{font-weight:400!important;color:#222!important}
%(A)s#panel .gap{border-bottom:1px dotted #555!important}
%(A)s#panel #ans,%(A)s#panel .opt{border:1px dotted #999!important;background:#fff!important}
%(A)s#panel #ans:focus{outline:0;border:1px solid #777!important}
%(A)s#panel #chk{background:#fff3a8!important;border:1px dotted #b9a64a!important;font-weight:400!important}
%(A)s#panel #ans.ok,%(A)s#panel .opt.ok{border:1px solid #9ccf84!important;background:#eef8e8!important}
%(A)s#panel #ans.bad,%(A)s#panel .opt.bad{border:1px solid #eba5a9!important;background:#fdeeee!important}
%(A)s#panel #res .nr.bad,%(A)s#panel #res .nr.bad *{color:#b3262f!important;font-weight:400!important}
%(A)s#panel #res .nr.ok,%(A)s#panel #res .nr.ok *{color:#3a7a1f!important;font-weight:400!important}
%(A)s#panel #res .nr b{font-weight:700!important}
%(A)s#panel #ct{display:none}
%(A)s#panel #pcn{margin-left:10px;color:#555}
%(A)s#panel #pcn b{color:#e30613;font-weight:400}
""" % {"A": A}
i = s.rindex("</style>"); s = s[:i] + CSS + s[i:]
m = re.search(r'name="app-version" content="(\d{4}-\d\d-\d\d)([a-z]?)"', s)
if m:
    n = chr(ord(m.group(2) or "`") + 1)
    s = s.replace(m.group(0), 'name="app-version" content="%s%s"' % (m.group(1), n))
JS = """<script id="elegant-js">setInterval(function(){var c=document.getElementById("ct"),t=c&&c.parentNode;if(!t)return;var m=/(\\d+)\\s*\\/\\s*(\\d+)/.exec(c.textContent);if(!m)return;var h="<b>"+("0"+m[1]).slice(-2)+"</b> / "+m[2],s=t.querySelector("#pcn");if(!s){s=document.createElement("span");s.id="pcn";t.appendChild(s);}if(s.innerHTML!==h)s.innerHTML=h;},150);</script>
"""
j = s.rindex("</script>") + len("</script>"); s = s[:j] + "\n" + JS + s[j:]
open(p, "w", encoding="utf-8").write(s); print("OK")
