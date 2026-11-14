#!/usr/bin/env python3
"""Spiel und Test kompakt und einheitlich (Steuart, 14 Nov 2026).
- Zähler in die Kopfzeile, Zeile "TEKAMOLO 01 / 08" entfällt
- Zurück/Weiter als Pfeile oben auf der Karte (wie im Popup), keine eigene Zeile mehr
- Stage + Frage + Antworten auf einem hellgrauen Kartenhintergrund
- Tastatur offen (Tippfeld aktiv): Tabs, Legende, Bild und Fußtasten klappen weg, die Seite passt in die sichtbare Höhe
  (die Mindesthöhe .app{min-height:600px} war der Grund, warum die Tastatur alles zerquetscht hat)
- Grammarly im Tippfeld abgeschaltet
Aufruf im Repo-Hauptordner: python3 src/spiel_kompakt_patch.py"""
import re, sys
p = "index.html"
s = open(p, encoding="utf-8").read()
if "/* spiel-kompakt */" in s:
    sys.exit("already patched")

CSS = r"""
/* spiel-kompakt */
.titlebar .spacer{text-align:right;font-size:12px;color:#666;font-variant-numeric:tabular-nums;white-space:nowrap;width:auto;min-width:70px}
.app[data-mode="game"] #gbar{display:none}
.app[data-mode="game"] #stagew,.app[data-mode="game"] #panel{background:#f3f3f1;margin:0 10px;padding-left:12px;padding-right:12px}
.app[data-mode="game"] #stagew{padding-top:8px}
.app[data-mode="game"] #panel{margin-top:-8px;padding-bottom:6px;position:relative;flex:0 0 auto!important}
.app[data-mode="game"] .stage{background-color:transparent!important;height:min(var(--sh,150px),120px);min-height:64px}
.app[data-mode="game"] #panel .card{background:transparent;position:relative}
.app[data-mode="game"] #panel .card.df .top{position:absolute;left:0;top:0;margin:0;padding:0;border:0;background:none;font-size:11px}
.app[data-mode="game"] #panel .card.df .top .count{display:none}
.app[data-mode="game"] #panel .card.df #tx{padding:14px 40px 0;text-align:center}
.app[data-mode="game"] #gnav{position:absolute;grid-area:auto;left:12px;right:12px;top:4px;min-height:0;pointer-events:none;z-index:2}
.app[data-mode="game"] #gnav button{pointer-events:auto;min-height:0}
.app[data-mode="game"] #gnav button span{display:none}
.app[data-mode="game"] #gnav .ar{width:30px;height:30px}
.app[data-mode="game"] #panel>.card{margin-top:0}
.app[data-mode="game"] #panel #tx,.app[data-mode="game"] #panel .opts{min-height:0}
.app.kbo{min-height:0!important;height:var(--vvh,100%)!important;padding-block:2px 2px}
.app.kbo .seg,.app.kbo #lg,.app.kbo #panel .btns,.app.kbo #tabar,.app.kbo .abar{display:none!important}
.app.kbo:not(:has(.stage #ans)) #stagew{display:none}
.app.kbo .stage{height:auto!important;min-height:0!important;padding:4px 0!important}
.app.kbo:not(:has(.stage #ans)) #panel{margin-top:0}
.app.kbo #panel .card.df #tx{min-height:0!important}
.app.kbo .titlebar{height:34px}
.app.kbo #panel .card.df #gt{font-size:13px;margin-top:6px}
"""
i = s.rindex("</style>")
s = s[:i] + CSS + s[i:]

JS = r"""<script id="kompakt-js">(function(){
const app=document.querySelector(".app"),vv=window.visualViewport,ct=document.getElementById("ct"),sp=document.querySelector(".titlebar .spacer");
function cnt(){if(!sp)return;if(app.dataset.mode!=="game"||!ct){sp.textContent="";return;}const lv=ct.querySelector(".lv"),r=ct.textContent.replace(lv?lv.textContent:"","").replace(/\s*richtig/,"").trim();sp.textContent=(lv?lv.textContent+" · ":"")+r+" ✓";}
if(ct){new MutationObserver(cnt).observe(ct,{childList:true,characterData:true,subtree:true});}
new MutationObserver(cnt).observe(app,{attributes:true,attributeFilter:["data-mode"]});cnt();
function kb(){const a=document.activeElement,typing=a&&(a.tagName==="INPUT"||a.tagName==="TEXTAREA")&&!a.disabled&&app.dataset.mode==="game";
 const h=vv?vv.height:innerHeight,open=!!typing&&h<innerHeight*.8;
 document.documentElement.style.setProperty("--vvh",Math.round(h)+"px");app.classList.toggle("kbo",open);if(open)scrollTo(0,0);}
if(vv)vv.addEventListener("resize",kb);
addEventListener("focusin",()=>setTimeout(kb,350));addEventListener("focusout",()=>setTimeout(kb,350));
})();</script>
"""
j = s.rindex("</script>") + len("</script>")
s = s[:j] + "\n" + JS + s[j:]

s = s.replace('placeholder="Was gehört in die Lücke?"', 'placeholder="Was fehlt?"')
n = s.count('<input id="ans" type="text"')
s = s.replace('<input id="ans" type="text"', '<input id="ans" data-gramm="false" data-gramm_editor="false" data-enable-grammarly="false" type="text"')

m = re.search(r'name="app-version" content="(\d{4}-\d\d-\d\d)([a-z]?)"', s)
if m:
    nxt = chr(ord(m.group(2) or "`") + 1)
    s = s.replace(m.group(0), 'name="app-version" content="%s%s"' % (m.group(1), nxt), 1)
open(p, "w", encoding="utf-8").write(s)
print("OK – Tippfelder:", n)
