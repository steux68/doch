# DOCH!: Popup-Look (wie PASSAGE) fuer Theorie-Popup, Lueckentext, Text pruefen, Geschichte und Zitate.
# Runde W/E-Pfeile, roter Grossbuchstaben-Titel, Text .98rem #222, gepunktete Datenzeile. Idempotent. 02.11.2026
import re,sys
s=open('index.html',encoding='utf-8').read()
WSVG='<svg class="ar" width="28" height="28" viewBox="-12 -12 24 24" aria-hidden="true"><circle class="tr" r="9.5"/><path class="rg" d="M-7.88 -5.31A9.5 9.5 0 1 1 -7.88 5.31"/><path class="dt" transform="rotate(180)" d="M5.4 0L-4.6 -4.9L-2.2 0L-4.6 4.9Z"/><text x="-9.50" y="0">W</text></svg>'
ESVG='<svg class="ar" width="28" height="28" viewBox="-12 -12 24 24" aria-hidden="true"><circle class="tr" r="9.5"/><path class="rg" d="M7.88 5.31A9.5 9.5 0 1 1 7.88 -5.31"/><path class="dt" transform="rotate(0)" d="M5.4 0L-4.6 -4.9L-2.2 0L-4.6 4.9Z"/><text x="9.50" y="0">E</text></svg>'

# 1) Theorie-Popup: Zaehler und runde Pfeile in die untere Leiste (gepunktete Datenzeile)
old_bar='<div class="pbar"><b id="pt"></b><span class="count" id="pc"></span><button id="px" aria-label="Schließen">×</button></div>'
old_nav='<div class="pnav" id="pnav"><button id="pp">← zurück</button><button id="pn">weiter →</button></div>'
if old_bar in s:
    assert s.count(old_bar)==1 and s.count(old_nav)==1
    s=s.replace(old_bar,'<div class="pbar"><b id="pt"></b><button id="px" aria-label="Schließen">×</button></div>',1)
    s=s.replace(old_nav,'<div class="pnav" id="pnav"><button id="pp" class="rnd" aria-label="Zurück">'+WSVG+'</button><span class="count" id="pc"></span><button id="pn" class="rnd" aria-label="Weiter">'+ESVG+'</button></div>',1)

# 2) Zitate: Hinweistext
h='Antippen öffnet die Quelle. Bilder: Wikipedia / Wikimedia Commons.'
if h in s:
    assert s.count(h)==1
    s=s.replace(h,'Antippen öffnet das Zitat, dort steht der Link zur Quelle. Bilder: Wikipedia / Wikimedia Commons.',1)

# 3) CSS
if 'id="popstyle2-css"' not in s:
    css='''<style id="popstyle2-css">
/* Popup-Look 2 (PASSAGE): Theorie-Popup, Geschichte, Zitate, Lueckentext, Text pruefen */
.rnd{width:42px;height:42px;min-height:0;padding:0;border:0!important;border-radius:50%!important;background:rgba(255,255,255,.82)!important;display:flex;align-items:center;justify-content:center;flex:none;-webkit-tap-highlight-color:transparent}
.rnd:disabled{opacity:.28}
#pt,.tlbody h4,#theo:has(#ltx) .tc>h3,#theo:has(#wprompt) .tc>h3{color:#e30613;text-transform:uppercase;font-weight:700;font-size:1.35rem;line-height:1.15;letter-spacing:.01em}
#theo:has(#ltx) .tc>h3,#theo:has(#wprompt) .tc>h3{background:none;padding-bottom:0}
#theo:has(#ltx) .tc>h3 small,#theo:has(#wprompt) .tc>h3 small{text-transform:none;letter-spacing:0;font-size:.8rem;font-weight:400;color:#888}
/* Theorie-Popup */
#pb{color:#222}
#pb p:not([class]){font-size:.98rem;line-height:1.45}
#pb p.tline{font-size:.88rem;color:#555}
.pnav,.qnav{flex:none;display:flex;align-items:center;justify-content:space-between;padding:6px 12px;border-top:1px dotted #b8b8b8}
.pnav .count,.qnav .count{font-size:12px;color:#888;font-variant-numeric:tabular-nums}
/* Geschichte und Zitate: gemeinsame Karte */
.tlbody{color:#222}
.tlbody p{font-size:.98rem;line-height:1.45}
.tlbody p.tline{font-size:.88rem;color:#555}
.tlbody .gs{order:9;margin-top:8px;padding-top:6px;border-top:1px dotted #b8b8b8;font-size:12px;letter-spacing:0;color:#888}
.tlbody .gs b{color:#111;font-weight:400}
.tlbody .qq{font-size:1.1rem;line-height:1.35}
.tlbody .qen2{font-size:.88rem;color:#555}
.qnav{border-top:0;border-bottom:0}
.tlcard .qnav{border-top:1px dotted #b8b8b8}
/* Lueckentext und Text pruefen */
#theo:has(#ltx) .tc p,#theo:has(#wprompt) .tc p{font-size:.98rem;line-height:1.45;color:#222}
#theo:has(#ltx) .tc>.tline,#theo:has(#wprompt) .tc>.tline{margin-top:4px;padding-top:6px;border-top:1px dotted #b8b8b8;font-size:.85rem;color:#555}
#lres .tc>p:not(.tline),#wres .tc>p:not(.tline){color:#1a7f37;font-weight:700}
</style>
'''
    assert s.count('</head>')==1
    s=s.replace('</head>',css+'</head>',1)

# 4) Zitate-Popup (Antippen oeffnet Zitat, Quelle als Link im Popup)
if 'id="qpop-js"' not in s:
    js='''<script id="qpop-js">/* Zitate: Antippen oeffnet ein Popup im Look von Geschichte */
(function(){const $=id=>document.getElementById(id),QO={i:0,open:false},sec0=$("p-quotes");if(!sec0)return;
const E=t=>String(t==null?"":t).replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
const W='__WSVG__',EE='__ESVG__',X='<svg viewBox="-12 -12 24 24" aria-hidden="true"><circle class="rg" r="9.5"/><path class="xx" d="M-3.6 -3.6L3.6 3.6M3.6 -3.6L-3.6 3.6"/></svg>';
const p=document.createElement("div");p.className="tlpop";p.id="qpop";p.hidden=true;p.setAttribute("role","dialog");p.setAttribute("aria-modal","true");p.setAttribute("aria-labelledby","qk");
p.innerHTML='<div class="tlcard"><div class="tltop"><span class="tlk" id="qk">Zitat</span><button type="button" class="tlx" id="qx" aria-label="Schließen">'+X+'</button></div><div class="tlbody" id="qb"></div><div class="qnav"><button type="button" class="rnd" id="qw" aria-label="Zurück">'+W+'</button><span class="count" id="qc"></span><button type="button" class="rnd" id="qe" aria-label="Weiter">'+EE+'</button></div></div>';
document.body.appendChild(p);
const items=()=>Array.prototype.slice.call(document.querySelectorAll("#p-quotes a.qt"));
function show(i){const L=items(),n=L.length;if(!n)return;i=(i%n+n)%n;QO.i=i;const a=L[i],g=(sel)=>{const x=a.querySelector(sel);return x?x.textContent:"";};
 let sec="",el=a.previousElementSibling;while(el){if(el.classList.contains("qsec")){sec=el.textContent;break;}el=el.previousElementSibling;}
 if(!sec){const c=document.querySelector('#qchips button[aria-pressed="true"]');if(c&&c.dataset.f!=="Alle")sec=c.dataset.f;}
 $("qb").innerHTML='<h4>'+E(g(".who"))+'</h4><p class="qq">„'+E(g("q"))+'“</p><p class="qen2">'+E(g(".qen"))+'</p><p class="tline"><a class="wk" href="'+E(a.href)+'" target="_blank" rel="noopener" aria-label="Quelle öffnen: '+E(g(".who"))+'">Quelle ↗</a></p><p class="gs">'+E([sec,g("small")].filter(Boolean).join(" · "))+'</p>';
 $("qc").textContent=(i+1)+" / "+n;$("qb").scrollTop=0;}
function open(i){if(!QO.open){QO.open=true;navPush("qt");p.hidden=false;}show(i);}
function close(){QO.open=false;p.hidden=true;}
function back(){if(navState()==="qt")history.back();else close();}
sec0.addEventListener("click",e=>{const a=e.target.closest&&e.target.closest("a.qt");if(!a)return;e.preventDefault();open(items().indexOf(a));});
$("qx").onclick=back;p.addEventListener("click",e=>{if(e.target===p)back();});
$("qw").onclick=()=>show(QO.i-1);$("qe").onclick=()=>show(QO.i+1);
window.addEventListener("popstate",()=>{if(QO.open)close();});
document.addEventListener("keydown",e=>{if(!QO.open)return;if(e.key==="Escape")back();if(e.key==="ArrowRight")show(QO.i+1);if(e.key==="ArrowLeft")show(QO.i-1);});
let x0=null,y0=0;const tb=$("qb");tb.addEventListener("touchstart",e=>{x0=e.touches[0].clientX;y0=e.touches[0].clientY;},{passive:true});
tb.addEventListener("touchend",e=>{if(x0==null)return;const dx=e.changedTouches[0].clientX-x0,dy=e.changedTouches[0].clientY-y0;x0=null;if(Math.abs(dx)>60&&Math.abs(dx)>Math.abs(dy)*1.5)show(QO.i+(dx<0?1:-1));},{passive:true});})();
</script>
'''.replace('__WSVG__',WSVG).replace('__ESVG__',ESVG)
    k='<script id="upd-js">'
    assert s.count(k)==1
    s=s.replace(k,js+k,1)

if '--noversion' not in sys.argv:
    s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda mm:mm.group(1)+'2026-11-02b'+mm.group(3),s,count=1)
open('index.html','w',encoding='utf-8').write(s)
