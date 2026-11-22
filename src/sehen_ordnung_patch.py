#!/usr/bin/env python3
"""2026-11-22h Sehen: (1) Zeiten/Fälle-Schalter über dem gepunkteten Rahmen (übergeordnete Wahl),
(2) Satz- und Verb-Zeilen wieder sichtbar (kein 'mehr'), (3) Zeitleiste direkt über dem Satz,
(4) gepunktete Verbindungslinie von der gewählten Zeit zum markierten Wort im Satz (nur Zeiten). Idempotent."""
import os, re, sys
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
p = os.path.join(root, "index.html")
s = open(p, encoding="utf-8").read()
if 'id="sehen-ordnung-css"' in s:
    print("already patched"); sys.exit()

def rep(old, new, count=1):
    global s
    assert s.count(old) == count, (old[:80], s.count(old))
    s = s.replace(old, new)

# 1. Schalter bekommt Klasse svtg (neue Seite und Fälle-Unterseiten)
rep("""const top='<div class="svg" style="--n:2"><span role="button" tabindex="0" class="svb svo fr'+(SV.tab==="t"?' on':'')+'" data-tab="t">Zeiten</span>""",
    """const top='<div class="svg svtg" style="--n:2"><span role="button" tabindex="0" class="svb svo fr'+(SV.tab==="t"?' on':'')+'" data-tab="t">Zeiten</span>""")
rep("""let h='<div class="sv" id="sv"><div class="svg" style="--n:2"><span role="button" tabindex="0" class="svb svo fr" data-tab="t">Zeiten</span><span role="button" tabindex="0" class="svb svo fr on" data-tab="k">Fälle</span></div>'+svSub()""",
    """let h='<div class="sv" id="sv"><div class="svg svtg" style="--n:2"><span role="button" tabindex="0" class="svb svo fr" data-tab="t">Zeiten</span><span role="button" tabindex="0" class="svb svo fr on" data-tab="k">Fälle</span></div>'+svSub()""")

# 2. Reihenfolge in der Zeiten-Seite: Person, Satzart, Verb, dann Zeitleiste direkt über dem Satz
old_zh = re.search(r" let h=seg\(PR,st\.p,\"p\"\);\n(?P<bands> h\+='<div class=\"svg svbd\".*?\n)(?P<chips> h\+='<div class=\"svg\" style=\"--n:6\">'\+SVCFG\.t\.chips.*?\n) h\+='<div style=\"height:6px\"></div>';\n(?P<zl> h\+=seg\(\[\"kurz\".*?\n)(?P<v> h\+=seg\(\[\"lernen \(haben\)\".*?\n)", s)
assert old_zh, "zH nicht gefunden"
new_zh = " let h=seg(PR,st.p,\"p\");\n" + old_zh.group("zl") + old_zh.group("v") + old_zh.group("bands") + old_zh.group("chips")
s = s[:old_zh.start()] + new_zh + s[old_zh.end():]

# 3. Verbindungslinie: SVG im Rahmen (nur Zeiten) + Zeichnen nach dem Rendern
rep("""th.innerHTML='<div class="sv sn" id="sv">'+top+(SV.tab==="t"?'<div style="height:6px"></div>'+zH():fH())+'</div>';
 const root=$("sv");svGlue();requestAnimationFrame(svGlue);""",
    """th.innerHTML='<div class="sv sn" id="sv">'+top+(SV.tab==="t"?'<div style="height:6px"></div>'+zH()+'<svg class="svln" aria-hidden="true"><path id="svpath" fill="none" stroke="#b8b8b8" stroke-width="1.2" stroke-linecap="round" stroke-dasharray="0.5 2.5"/></svg>':fH())+'</div>';
 const root=$("sv");svGlue();requestAnimationFrame(svGlue);sehLine();requestAnimationFrame(sehLine);setTimeout(sehLine,250);""")
rep("function svGlue(){", """function sehLine(){const sv=document.getElementById("sv"),pa=document.getElementById("svpath");if(!sv||!pa)return;
  const on=sv.querySelector(".svk.on"),w=sv.querySelector(".sns .g");if(!on||!w){pa.setAttribute("d","");return;}
  const W=sv.getBoundingClientRect(),c=on.getBoundingClientRect(),r=w.getBoundingClientRect();
  const x1=c.left+c.width/2-W.left,y1=c.bottom-W.top+2,x2=r.left+r.width/2-W.left,y2=r.top-W.top-3,ym=y1+Math.min(14,(y2-y1)/2);
  pa.setAttribute("d","M"+x1+" "+y1+" V"+ym+" H"+x2+" V"+y2);}
addEventListener("resize",()=>{try{sehLine()}catch(e){}});
function svGlue(){""")

# 4. 'mehr'-Knopf aus ux_patch abschalten (Zeilen bleiben sichtbar)
rep("function fix(){pend=0;", "function fix(){pend=0;return;")

# 5. CSS
css = '''<style id="sehen-ordnung-css">
#sv:has(>.svtg){margin-top:46px}
#sv>.svtg{position:absolute;left:0;right:0;top:-38px}
#sv>.svtg .svb:not(.on){background:rgba(255,255,255,.82)}
#sv .svln{z-index:2}
</style>
'''
s = s.rstrip("\n") + "\n" + css
s = re.sub(r'<meta name="app-version" content="[^"]+">', '<meta name="app-version" content="2026-11-22h">', s, count=1)
open(p, "w", encoding="utf-8").write(s); print("ok")
