# 20.11.2026: Test-Kopie stack3.html (index.html bleibt unveraendert).
# Mock-up: farbige Flagge links, rechts der Schalter STUDIEREN | STAUNEN (statt der zweiten Flagge);
# Hauptbildschirm = Grammatik, Tests, Hilfsmittel + vierter Balken STAUNEN (zitate · redewendungen · geschichte);
# im Modus STAUNEN = Zitate, Redewendungen, Geschichte + Balken STUDIEREN (grammatik · tests · hilfsmittel).
# Im Mock-up laedt der Wechsel die Seite neu (Modus in sessionStorage); in der echten Version wuerde er ohne Neuladen tauschen.
import sys
s = open('index.html', encoding='utf-8').read()

def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (a[:60], s.count(a)); s = s.replace(a, b)

# 1. Modus festlegen + nur die Abschnitte des Modus als Balken
rep('const SECS=[["home","Grammatik"],["test","Tests"],["links","Hilfsmittel"],["quotes","Zitate"],["rede","Redewendungen"],["hist","Geschichte"]];',
    'const DMODE=(()=>{try{return sessionStorage.getItem("dochMode")==="s"?"s":"d"}catch(e){return"d"}})();document.documentElement.setAttribute("data-dmode",DMODE);\n'
    'const SECS=DMODE==="s"?[["quotes","Zitate"],["rede","Redewendungen"],["hist","Geschichte"],["study","Studieren"]]:[["home","Grammatik"],["test","Tests"],["links","Hilfsmittel"],["wow","Staunen"]];')

# 2. zwei Platzhalter-Abschnitte fuer den vierten Balken
rep('<section class="hp" id="p-hist"></section>',
    '<section class="hp" id="p-hist"></section><section class="hp" id="p-wow"></section><section class="hp" id="p-study"></section>')

# 3. rechte (Umriss-)Flagge raus, Schalter hinein; linke Flagge farbig
SW = ('<span class="dsw" id="dsw" role="group" aria-label="Bereich">'
      '<button type="button" data-m="d" aria-pressed="true">Studieren</button>'
      '<button type="button" data-m="s" aria-pressed="false">Staunen</button></span>')
a = '<button class="markb on" id="markb" aria-label="Zur Titelseite">'
i = s.index(a); j = s.index('</button>', i) + len('</button>')
rep(s[i:j], s[i:j].replace('class="markb on"', 'class="markb"') + SW)
rep('<button class="markb" id="markL" aria-label="Zur Titelseite">', '<button class="markb" id="markL" aria-label="Zur Titelseite" hidden>')

CSS = '''<style id="stack3-css">
/* Schalter oben rechts: STUDIEREN / Flagge / STAUNEN uebereinander */
#dsw{flex:none;display:flex;flex-direction:column;align-items:stretch;width:66px;margin-left:auto;align-self:center;background:#fff;position:relative}
#dsw>button[data-m]{height:11px;padding:0;display:flex;align-items:center;justify-content:center;font-size:8.5px;letter-spacing:.9px;text-transform:uppercase;line-height:1;font-weight:400;color:#222;background:transparent;white-space:nowrap;position:relative}
#dsw>button[data-m][aria-pressed="true"]{background:transparent;color:#e30613;font-weight:700}
#dsw>button[data-m]::before{content:"";position:absolute;left:0;right:0;top:-5px;bottom:-5px}
#dsw .markb{margin:2px 0;padding:0;height:16px;justify-content:center;align-items:center}
#dsw .mark{width:46px;height:16px}
@keyframes flP{0%,100%{opacity:0}50%{opacity:1}}
#dsw .mark .fl{animation:flP 2.4s ease-in-out infinite}
@media (prefers-reduced-motion:reduce){#dsw .mark .fl{animation:none;opacity:1}}
/* etwas mehr Luft um den Titelblock, mittig */
.home .titlebar{height:58px!important;padding-top:0!important;padding-bottom:0!important;align-items:center!important}
.home .brand{align-items:center!important}
/* Logo ganz links, rechts Flagge + Schalter; die Flagge blinkt mit dem Modus: Umriss = STUDIEREN, Farbe = STAUNEN */
.home h1.logo{justify-content:flex-start!important}
.home .brand{gap:8px;align-items:center}
.home #markb{display:flex}
.home #markb{margin:0}
.mark .fl{transition:opacity .6s}
/* Abschnitte des anderen Modus ausblenden */
html[data-dmode="d"] #p-quotes,html[data-dmode="d"] #p-rede,html[data-dmode="d"] #p-hist,html[data-dmode="d"] #p-study,
html[data-dmode="s"] #p-home,html[data-dmode="s"] #p-test,html[data-dmode="s"] #p-links,html[data-dmode="s"] #p-wow{display:none!important}
/* der vierte Balken: Name + kleine Kleinbuchstaben-Liste, kein [04] */
.hb[data-k="wow"] small,.hb[data-k="study"] small{text-transform:none;letter-spacing:.2px;font-size:10px!important;margin-left:auto!important;margin-right:6px!important;opacity:.75}
/* Farben: bleiben wie bisher nach Platz (rosa, gruen, blau, gelb), der vierte Balken ist in beiden Modi gelb */
</style>
'''
JS = '''<script id="stack3-js">(function(){
const NAMES={home:"grammatik · tests · hilfsmittel",wow:"zitate · redewendungen · geschichte"};
const bars=[].slice.call(document.querySelectorAll("#hscroll>.hb"));
const keys=SECS.map(x=>x[0]);
bars.forEach((b,i)=>{b.setAttribute("data-k",keys[i]);});
if(DMODE==="s")bars.slice(0,3).forEach((b,i)=>{const sm=b.querySelector("small");if(sm)sm.textContent="["+"ABC"[i]+"]";});
const last=bars[bars.length-1],lk=keys[keys.length-1];
if(last){const sm=last.querySelector("small");if(sm)sm.textContent=lk==="wow"?"zitate · redewendungen · geschichte":"grammatik · tests · hilfsmittel";
  last.addEventListener("click",()=>go(lk==="wow"?"s":"d"));}
function go(m){try{sessionStorage.setItem("dochMode",m);sessionStorage.setItem("dochSwitched","1");}catch(e){}location.reload();}
const fb=document.getElementById("markb"),sw=document.getElementById("dsw");
if(fb&&sw){sw.insertBefore(fb,sw.children[1]);fb.classList.remove("on");fb.onclick=()=>go(DMODE==="s"?"d":"s");}

if(sw){[].forEach.call(sw.querySelectorAll("button[data-m]"),b=>{b.setAttribute("aria-pressed",String(b.dataset.m===DMODE));b.onclick=()=>{if(b.dataset.m!==DMODE)go(b.dataset.m);};});}
try{if(sessionStorage.getItem("dochSwitched")==="1"){sessionStorage.removeItem("dochSwitched");
  const run=()=>{SC.scrollTo({top:secTop(0),behavior:"auto"});};setTimeout(run,350);setTimeout(run,1000);}}catch(e){}
})();</script>
'''
rep('<script id="info-link-js">', CSS + JS + '<script id="info-link-js">')
if '--live' in sys.argv:
    import re
    if 'id="stack3-css"' in open('index.html', encoding='utf-8').read():
        print('schon live'); sys.exit(0)
    s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1) + '2026-11-20e' + m.group(3), s, count=1)
    open('index.html', 'w', encoding='utf-8').write(s)
    print('ok -> index.html (live)')
else:
    open('stack3.html', 'w', encoding='utf-8').write(s)
    print('ok -> stack3.html')
