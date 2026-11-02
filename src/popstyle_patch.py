# DOCH!: Lernkarten im Look der PASSAGE-Popups: runde W/E-Pfeile auf der Buehne statt Zurueck/Weiter,
# roter Grossbuchstaben-Titel, Karte/Stufe als gepunktete Zeile. Idempotent. 02.11.2026
import re,sys
s=open('index.html',encoding='utf-8').read()
WSVG='<svg class="ar" width="28" height="28" viewBox="-12 -12 24 24" aria-hidden="true"><circle class="tr" r="9.5"/><path class="rg" d="M-7.88 -5.31A9.5 9.5 0 1 1 -7.88 5.31"/><path class="dt" transform="rotate(180)" d="M5.4 0L-4.6 -4.9L-2.2 0L-4.6 4.9Z"/><text x="-9.50" y="0">W</text></svg>'
ESVG='<svg class="ar" width="28" height="28" viewBox="-12 -12 24 24" aria-hidden="true"><circle class="tr" r="9.5"/><path class="rg" d="M7.88 5.31A9.5 9.5 0 1 1 7.88 -5.31"/><path class="dt" transform="rotate(0)" d="M5.4 0L-4.6 -4.9L-2.2 0L-4.6 4.9Z"/><text x="9.50" y="0">E</text></svg>'
if 'id="popA"' not in s:
    a='<div class="stage" id="stage"></div>'
    assert s.count(a)==1
    s=s.replace(a,'<div class="stagew" id="stagew">'+a+'<button type="button" class="tlar pw" id="popA" aria-label="Zurück" hidden>'+WSVG+'</button><button type="button" class="tlar pe" id="popE" aria-label="Weiter" hidden>'+ESVG+'</button></div>',1)
    css='''
/* Popup-Look (PASSAGE) */
.stagew{position:relative;display:flex;flex-direction:column;flex:1 1 auto;min-height:0}
.stagew>.stage{flex:1 1 auto}
.tlar{position:absolute;top:10px;margin-top:0;width:42px;height:42px;min-height:0;border:0!important;padding:0;border-radius:50%!important;background:rgba(255,255,255,.82)!important;display:flex;align-items:center;justify-content:center;z-index:20;-webkit-tap-highlight-color:transparent}
.tlar.pw{left:6px}.tlar.pe{right:6px}.tlar[hidden]{display:none!important}.tlar:disabled{opacity:.28}
.ar{overflow:visible}.ar .rg{fill:none;stroke:#3a3c37;stroke-width:1px}.ar .dt{fill:#4d4f4a;stroke:#1a1a1a;stroke-width:1px;stroke-linejoin:round}
.ar text{fill:#3a3c37;font:700 6.4px Carlito,Calibri,sans-serif;text-anchor:middle;dominant-baseline:central}.ar .tr{display:none}
#btns1 .popgone{display:none}
#panel .card.df #tx{color:#e30613;text-transform:uppercase;font-weight:700;font-size:1.35rem;line-height:1.15;letter-spacing:.01em}
#panel .card.df #gt{font-size:.98rem;line-height:1.45;color:#222}
#panel .card.df{display:flex;flex-direction:column}
#panel .card.df .top{order:9;margin-top:10px;padding-top:6px;border-top:1px dotted #b8b8b8;font-size:12px;color:#888}
#panel .card.df .top .badge{background:none;padding:0;font-size:12px;font-weight:400;color:#111}
'''
    i=s.index('</style>',s.index('.badge{font-weight:700'))
    s=s[:i]+css+s[i:]
    js='''<script id="pop-js">/* Pfeile steuern die vorhandenen Knoepfe Zurueck/Weiter */
(function(){const $=id=>document.getElementById(id),r=$("btns1");if(!r)return;
function sync(){const z=$("bZ"),w=$("bW"),st=$("stage"),on=w&&st&&!st.hidden&&st.offsetParent!==null&&/^Weiter/.test(w.textContent);
 [z,w].forEach(b=>{if(b)b.classList.toggle("popgone",!!on)});
 $("popA").hidden=!(on&&z);$("popE").hidden=!on;if(on){if(z)$("popA").disabled=z.disabled;$("popE").disabled=w.disabled;}}
$("popA").onclick=()=>{const z=$("bZ");if(z)z.click();};
$("popE").onclick=()=>{const w=$("bW");if(w)w.click();};
new MutationObserver(sync).observe(r,{childList:true,subtree:true,attributes:true});
new MutationObserver(sync).observe($("stage"),{attributes:true,childList:true});sync();})();
</script>
'''
    k='<script id="upd-js">'
    assert s.count(k)==1
    s=s.replace(k,js+k,1)
if '--noversion' not in sys.argv:
    s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda mm:mm.group(1)+'2026-11-02a'+mm.group(3),s,count=1)
open('index.html','w',encoding='utf-8').write(s)
