#!/usr/bin/env python3
"""Spiel/Test als fester Popup-Rahmen im Galerie-Stil (Steuart, 14 Nov 2026). Nach spiel_kompakt_patch.py ausführen.
Feste Zeilen: Kopf 44 (Pfeile + Thema) | Hinweis | Satz (2 Zeilen) | Eingabe oder Auswahl | Feedback | Fußzeile.
Nur drei Schriftgrößen (11/15/20), Farben: Gelb = Prüfen, Rot = falsch, Grün = richtig. Zählt app-version hoch.
Aufruf im Repo-Hauptordner: python3 src/spiel_popup_patch.py"""
import re, sys
p = "index.html"
s = open(p, encoding="utf-8").read()
if "/* spiel-popup */" in s:
    sys.exit("already patched")
if "/* spiel-kompakt */" not in s:
    sys.exit("zuerst spiel_kompakt_patch.py ausführen")

CSS = r"""
/* spiel-popup */
#gqpop{display:contents}
.app[data-mode="game"] #gqpop{display:block;position:relative;margin:8px 10px 0;padding:44px 12px 6px;background:rgba(243,243,241,.96);border:.5px solid #bbb}
.app[data-mode="game"] #stagew,.app[data-mode="game"] #panel{background:none;margin:0;padding:0;border:0}
.app[data-mode="game"] #panel{position:static;margin-top:0}
.app[data-mode="game"] #panel .card,.app[data-mode="game"] #panel .card.df{position:static;background:none;border:0;padding:0;margin:0;min-height:0}
/* Kopf: Thema mittig, Pfeile an festen Ecken */
.app[data-mode="game"] #panel .card.df .top{position:absolute;top:0;left:50px;right:50px;height:44px;margin:0;padding:0;border:0;background:none;display:flex;align-items:center;justify-content:center;text-align:center;font-size:11px;font-weight:400;letter-spacing:.08em;text-transform:uppercase;color:#777;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.app[data-mode="game"] #panel .card.df .top *{font-size:11px}
.app[data-mode="game"] #gnav{position:absolute;top:8px;left:12px;right:12px;height:28px;margin:0;padding:0;z-index:2;display:flex;justify-content:space-between;grid-area:auto;pointer-events:none}
.app[data-mode="game"] #gnav button{pointer-events:auto;width:28px;height:28px;min-height:0;padding:0;margin:0;background:none;border:0}
.app[data-mode="game"] #gnav button svg{width:28px;height:28px}
.app[data-mode="game"] #gnav button span{display:none}
.app[data-mode="game"] #gnav button[disabled],.app[data-mode="game"] #gnav button.off{opacity:.25}
/* Hinweis (Stage): eine ruhige Zeile */
.app[data-mode="game"] #stagew{padding:0}
.app[data-mode="game"] .stage{height:auto!important;min-height:26px;max-height:78px;overflow:hidden;background:none!important;padding:0!important;margin:0 0 4px!important;text-align:center}
.app[data-mode="game"] .stage .pict.hide{display:none}
.app[data-mode="game"] .stage:has(>.pict.hide){display:none}
.app[data-mode="game"] .stage .pict .case{display:none}
.app[data-mode="game"] .stage .pict,.app[data-mode="game"] .stage .pict *{font-size:15px!important;font-weight:400!important;letter-spacing:0!important;text-transform:none!important;line-height:1.35!important;margin:0!important}
.app[data-mode="game"] .stage .en{font-size:15px!important;font-weight:400!important;color:#666!important;margin:0 0 6px!important;line-height:1.35!important}
.app[data-mode="game"] .stage .nw{font-size:20px!important;font-weight:500!important;color:#222}
/* Satz */
.app[data-mode="game"] #panel #tx{font-size:20px!important;font-weight:500!important;line-height:1.35!important;color:#222!important;text-align:center;margin:0 0 10px!important;padding:0!important;min-height:54px;display:flex;align-items:center;justify-content:center;flex-wrap:wrap;gap:0 .3em;letter-spacing:0!important;text-transform:none!important}
.app[data-mode="game"] #panel #tx *{font-size:inherit!important;color:inherit!important;font-weight:inherit!important}
.app[data-mode="game"] #panel .gap{display:inline-block;min-width:52px;border-bottom:2px solid #222;text-align:center}
/* Eingabe, Auswahl */
.app[data-mode="game"] #panel .answer{display:flex;gap:8px;margin:0;padding:0;height:44px}
.app[data-mode="game"] #panel #ans{flex:1;min-width:0;height:44px;box-sizing:border-box;font-size:17px;border:1px dotted #999;background:#fff;color:#222;padding:0 12px;text-decoration:none!important}
.app[data-mode="game"] #panel #ans.bad{border:1px solid #e30613;background:#fff;color:#222}
.app[data-mode="game"] #panel #ans.ok{border:1px solid #3f8f1f;background:#fff;color:#222}
.app[data-mode="game"] #panel #chk{height:44px;padding:0 16px;font-size:15px;font-weight:500;background:#ffd400;color:#222;border:0;border-radius:0}
.app[data-mode="game"] #panel #chk:disabled{opacity:.35}
.app[data-mode="game"] #panel .opts{min-height:94px;margin:0}
.app[data-mode="game"] #panel .opt{height:44px;box-sizing:border-box;font-size:17px;font-weight:400;padding:0 12px;margin:0 0 6px;text-align:left;border:1px dotted #999;background:#fff;color:#222;letter-spacing:0;text-transform:none}
.app[data-mode="game"] #panel .opt.ok{border:1px solid #3f8f1f;background:#fff}
.app[data-mode="game"] #panel .opt.bad{border:1px solid #e30613;background:#fff}
/* Feedback: feste Zeile, rot/grün */
.app[data-mode="game"] #panel #res{min-height:44px;margin:8px 0 0;font-size:15px;line-height:1.35}
.app[data-mode="game"] #panel #res .nr{margin:0;font-size:15px;font-weight:500;letter-spacing:0;text-transform:none}
.app[data-mode="game"] #panel #res .nr.bad,.app[data-mode="game"] #panel #res .nr.bad *{color:#e30613}
.app[data-mode="game"] #panel #res .nr.ok,.app[data-mode="game"] #panel #res .nr.ok *{color:#3f8f1f}
.app[data-mode="game"] #panel #gt,.app[data-mode="game"] #panel #nf{margin:0;font-size:13px;line-height:1.35;color:#666;font-weight:400;letter-spacing:0;text-transform:none}
.app[data-mode="game"] #panel #nf:empty{display:none}
/* Fußzeile klein und ruhig */
.app[data-mode="game"] #panel .btns{display:flex;justify-content:space-between;gap:12px;margin:2px 0 0;padding:0}
.app[data-mode="game"] #panel .btns button{font-size:12px;letter-spacing:.04em;font-weight:400;color:#777;background:none;border:0;padding:4px 0;min-height:0;text-transform:none}
.app[data-mode="game"] #panel .btns button.on{color:#777}
.app[data-mode="game"] #panel #bW{display:none}
.app.kbo #gqpop{margin-top:4px}
.app.kbo #panel .btns{display:none}
"""
i = s.rindex("</style>")
s = s[:i] + CSS + s[i:]

JS = r"""<script id="popup-js">(function(){const sw=document.getElementById("stagew"),pn=document.getElementById("panel");if(!sw||!pn||document.getElementById("gqpop"))return;const q=document.createElement("div");q.id="gqpop";sw.parentNode.insertBefore(q,sw);q.append(sw,pn);
const g=i=>document.getElementById(i);
let wired=false;
function sync(){const bW=g("bW"),gE=g("gnE"),pE=g("popE");if(!bW||!gE||!pE)return;
if(!wired){wired=true;const oc=gE.onclick;gE.onclick=function(e){return g("popE").hidden?g("bW").click():oc&&oc.call(gE,e);};}
if(!pE.hidden)return;const ready=bW.classList.contains("primary");if(gE.hidden)gE.hidden=false;if(gE.disabled===ready)gE.disabled=!ready;}
setInterval(sync,120);})();</script>
"""
j = s.rindex("</script>") + len("</script>")
s = s[:j] + "\n" + JS + s[j:]

m = re.search(r'name="app-version" content="(\d{4}-\d\d-\d\d)([a-z]?)"', s)
if m:
    nxt = chr(ord(m.group(2) or "`") + 1)
    s = s.replace(m.group(0), 'name="app-version" content="%s%s"' % (m.group(1), nxt), 1)
open(p, "w", encoding="utf-8").write(s)
print("OK")
