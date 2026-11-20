# 20.11.2026: Test-Kopie stack4.html (index.html bleibt unveraendert).
# Schalter wie in dasein-design/PASSAGE: "Studieren (Schalter) Staunen" mit pulsierendem Ring; jede Haelfte hat ihre eigene Startseite
# (Karte mit nur den eigenen drei Pins); der Wechsel springt nicht mehr zum ersten Balken; Eintraege/Cross-Pins entfallen.
import sys
s = open('index.html', encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (a[:70], s.count(a)); s = s.replace(a, b)
# 1. Pins der anderen Haelfte gar nicht erst laden (vor dem Hauptskript)
EARLY = '''<script>(function(){var m="d";try{m=sessionStorage.getItem("dochMode")==="s"?"s":"d";}catch(e){}
(m==="s"?["home","test","links"]:["quotes","rede","hist"]).forEach(function(k){var p=document.querySelector('#tstage .pin[data-k="'+k+'"]');if(p&&p.parentNode)p.parentNode.removeChild(p);});})();</script>
'''
rep('</footer>\n</div>\n\n<script>\n/* ---------- data: Satzbau', '</footer>\n</div>\n\n' + EARLY + '<script>\n/* ---------- data: Satzbau')
# 2. kein Sprung zum ersten Balken mehr nach dem Wechsel
rep('function go(m){try{sessionStorage.setItem("dochMode",m);sessionStorage.setItem("dochSwitched","1");}catch(e){}location.reload();}',
    'function go(m){try{sessionStorage.setItem("dochMode",m);}catch(e){}location.reload();}')
# 3. Eintragslisten raus (der Schalter oben und der Balken unten sind die zwei Wege)
i = s.index('enter($("p-wow"),"s"'); j = s.index('\n', s.index('enter($("p-study"),"d"', i)) + 1
s = s[:i] + s[j:]
CSS = '''<style id="stack4-css">
#dsw{display:none!important}
#dsw4{flex:none;display:flex;align-items:center;gap:6px;margin-left:auto;padding:0;border:0;background:none;font:inherit;font-size:11.5px;letter-spacing:.3px;color:#8a8a86;cursor:pointer;position:relative;white-space:nowrap}
#dsw4[data-m="d"] .t1,#dsw4[data-m="s"] .t2{font-weight:700;color:#222}
#dsw4 .pill{position:relative;flex:none;width:34px;height:18px;box-sizing:border-box;border:1.5px solid #222;border-radius:9px;background:#fff}
#dsw4 .knob{position:absolute;top:1px;left:1px;width:13px;height:13px;box-sizing:border-box;border-radius:50%;background:#cdff3e;border:1.5px solid #222;transition:left .25s}
#dsw4[data-m="s"] .knob{left:16px}
#dsw4 .knob::after{content:"";position:absolute;inset:-7px;border:1.5px solid rgba(227,6,19,.5);border-radius:50%;animation:dsRing 2.4s ease-out infinite;pointer-events:none}
@keyframes dsRing{0%{transform:scale(.55);opacity:.95}100%{transform:scale(1.7);opacity:0}}
@media (prefers-reduced-motion:reduce){#dsw4 .knob::after{animation:none;opacity:.5}}
#dsw4::before{content:"";position:absolute;left:-8px;right:-4px;top:-14px;bottom:-14px}
.home h1.logo{min-width:0}.home h1.logo svg{max-width:100%;height:auto;max-height:47px}
</style>
'''
JS = '''<script id="stack4-js">(function(){
const $=id=>document.getElementById(id);
function go2(m){try{sessionStorage.setItem("dochMode",m);}catch(e){}location.reload();}
const old=$("dsw");if(old){const t=document.createElement("button");t.type="button";t.id="dsw4";t.dataset.m=DMODE;t.setAttribute("role","switch");t.setAttribute("aria-checked",String(DMODE==="s"));t.setAttribute("aria-label","Studieren oder Staunen");
 t.innerHTML='<span class="t1">Studieren</span><span class="pill"><i class="knob"></i></span><span class="t2">Staunen</span>';
 t.onclick=()=>go2(DMODE==="s"?"d":"s");old.parentNode.insertBefore(t,old);}
const lb=document.querySelectorAll("#hscroll>.hb")[3];if(lb){const b=lb.querySelector("b");if(b)b.textContent=DMODE==="s"?"\\u2190 Studieren":"Staunen \\u2192";}
function row(sec,label,m){if(!sec)return;const w=document.createElement("div");w.className="endblk enter";const b=document.createElement("button");b.type="button";b.className="enterrow";b.innerHTML="<b>"+label+"</b><small>\\u2192</small>";b.onclick=()=>go2(m);w.appendChild(b);sec.appendChild(w);}
row($("p-wow"),"Staunen öffnen","s");row($("p-study"),"Studieren öffnen","d");
})();</script>
'''
rep('<script id="info-link-js">', CSS + JS + '<script id="info-link-js">')
open('stack4.html', 'w', encoding='utf-8').write(s)
print('ok -> stack4.html')
