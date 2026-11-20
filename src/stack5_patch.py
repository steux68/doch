# 20.11.2026: STAUNEN hat wieder seine Startseite mit der Karte und den Pins A B C.
# Antippen eines Pins oder Balkens oeffnet dann die Ansicht mit den Balken oben (Abschnitt offen); Tipp aufs DOCH-Logo = zurueck zur Karte.
import re
s = open('index.html', encoding='utf-8').read()
if 'stack5' in s: print('schon live'); raise SystemExit
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (a[:70], s.count(a)); s = s.replace(a, b)
i = s.index('<style id="stack4-css">'); k = s.index('/* STAUNEN: die drei Balken oben', i); j = s.index('</style>', k)
blk = s[k:j].replace('html[data-dmode="s"]', 'html[data-dmode="s"][data-sopen]')
s = s[:k] + blk + s[j:]
old = ' bs.slice(0,3).forEach((b,i)=>{b.style.bottom="auto";b.addEventListener("click",e=>{e.stopImmediatePropagation();pick(i);},true);});\n pick(0);}'
new = ''' /* stack5 */
 function openS(i){document.documentElement.setAttribute("data-sopen","1");pick(i);}
 bs.slice(0,3).forEach((b,i)=>{b.addEventListener("click",e=>{e.stopImmediatePropagation();openS(i);},true);});
 [].slice.call(document.querySelectorAll("#tstage .pin")).forEach(p=>{const i=sec.indexOf(p.dataset.k);if(i<0)return;p.addEventListener("click",e=>{e.stopImmediatePropagation();e.preventDefault();openS(i);},true);});
 const lg=document.querySelector(".home h1.logo");if(lg){lg.style.cursor="pointer";lg.addEventListener("click",()=>{document.documentElement.removeAttribute("data-sopen");bs.forEach(b=>b.classList.remove("sel"));sc.scrollTop=0;});}
 sc.setAttribute("data-sec","quotes");}'''
rep(old, new)
s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1) + '2026-11-20n' + m.group(3), s, count=1)
open('index.html', 'w', encoding='utf-8').write(s); print('ok')
