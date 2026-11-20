# 20.11.2026: eigener Balken IMPRESSUM (5. Balken, in beiden Modi) mit Urheber-Zeile, update/home, Info, Bilder-Hinweis, Impressum, Version.
# Der Abschnitt hinter dem STAUNEN-/STUDIEREN-Balken zeigt statt Leere die drei Eintraege des anderen Modus zum Antippen. Idempotent.
import re, sys
s = open('index.html', encoding='utf-8').read()
if 'id="p-imp"' in s:
    print('schon vorhanden'); sys.exit(0)
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (a[:70], s.count(a)); s = s.replace(a, b)
# 1. fuenfter Balken
rep('["study","Studieren"]]:[["home","Grammatik"],["test","Tests"],["links","Hilfsmittel"],["wow","Staunen"]];',
    '["study","Studieren"],["imp","Impressum"]]:[["home","Grammatik"],["test","Tests"],["links","Hilfsmittel"],["wow","Staunen"],["imp","Impressum"]];')
rep('<section class="hp" id="p-study"></section>', '<section class="hp" id="p-study"></section><section class="hp" id="p-imp"></section>')
# 2. Wechselbalken ist jetzt der vierte, nicht der letzte; Sprungziel nach dem Neuladen
rep('const last=bars[bars.length-1],lk=keys[keys.length-1];', 'const last=bars[3],lk=keys[3];')
rep('const run=()=>{SC.scrollTo({top:secTop(0),behavior:"auto"});};setTimeout(run,350);setTimeout(run,1000);',
    'const run=()=>{let k=0;try{k=+(sessionStorage.getItem("dochTarget")||0);}catch(e){}SC.scrollTo({top:secTop(k),behavior:"auto"});};setTimeout(run,350);setTimeout(run,1000);setTimeout(()=>{try{sessionStorage.removeItem("dochTarget");}catch(e){}},1300);')
# 3. Fuss-Skript neu: Impressum-Abschnitt + Einstieg im Abschnitt des Wechselbalkens
i = s.index('<script id="stack3-foot">'); j = s.index('</script>', i) + len('</script>')
JS = '''<script id="stack3-foot">(function(){const $=id=>document.getElementById(id),sb=$("setb");if(!sb)return;
const cr=sb.querySelector(".ucr"),imp=$("impH");
const tl=[].slice.call(sb.querySelectorAll("p.tline"));
const ib=document.querySelectorAll("#hscroll>.hb");if(ib[4]){const sm=ib[4].querySelector("small");if(sm)sm.textContent="";}
function fnd(re){return tl.filter(p=>re.test(p.textContent))[0];}
/* IMPRESSUM */
(function(){const sec=$("p-imp");if(!sec)return;const w=document.createElement("div");w.className="endblk";
 if(cr)w.appendChild(cr.cloneNode(true));
 const u=document.createElement("div");u.className="utl";
 [["updbtn","update"],["homebtn","home"]].forEach(a=>{const o=$(a[0]);if(!o)return;const b=document.createElement("button");b.type="button";b.innerHTML=o.innerHTML;b.onclick=()=>o.click();u.appendChild(b);});
 w.appendChild(u);
 const b=document.createElement("button");b.type="button";b.className="endinfo";b.textContent="Info & Einstellungen";b.onclick=()=>{const c=$("cogb");if(c)c.click();};w.appendChild(b);
 const bi=fnd(/^Bilder:/);if(bi)w.appendChild(bi.cloneNode(true));
 if(imp){const h=imp.cloneNode(true);h.removeAttribute("id");w.appendChild(h);const t=imp.nextElementSibling;if(t)w.appendChild(t.cloneNode(true));}
 const v=fnd(/^Version /);if(v)w.appendChild(v.cloneNode(true));
 sec.appendChild(w);})();
/* Einstieg: hinter dem STAUNEN-Balken die drei Eintraege des anderen Modus, hinter dem STUDIEREN-Balken ebenso */
function enter(sec,m,list){if(!sec)return;const w=document.createElement("div");w.className="endblk enter";
 list.forEach((n,i)=>{const b=document.createElement("button");b.type="button";b.className="enterrow";b.innerHTML="<b>"+n[0]+"</b><small>"+n[1]+"</small>";
  b.onclick=()=>{try{sessionStorage.setItem("dochMode",m);sessionStorage.setItem("dochSwitched","1");sessionStorage.setItem("dochTarget",String(i));}catch(e){}location.reload();};w.appendChild(b);});
 sec.appendChild(w);}
enter($("p-wow"),"s",[["Zitate","[A]"],["Redewendungen","[B]"],["Geschichte","[C]"]]);
enter($("p-study"),"d",[["Grammatik","[01]"],["Tests","[02]"],["Hilfsmittel","[03]"]]);
})();</script>'''
s = s[:i] + JS + s[j:]
# 4. Stil fuer die Einstiegszeilen
rep('</style>\n<script id="stack3-foot">', '.endblk.enter{padding:8px 0 24px}\n.enterrow{display:flex;justify-content:space-between;align-items:center;width:100%;height:34px;padding:0;border:0;background:none;font:inherit;font-size:14px;text-transform:uppercase;letter-spacing:1.4px;color:#222;position:relative;text-align:left}\n.enterrow small{font-size:10px;letter-spacing:.5px;color:#777}\n.enterrow::after{content:"";position:absolute;left:0;right:0;bottom:0;height:1px;pointer-events:none;background:repeating-linear-gradient(to right,#b8b8b8 0 1px,transparent 1px 3px)}\n</style>\n<script id="stack3-foot">')
s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1) + '2026-11-20g' + m.group(3), s, count=1)
open('index.html', 'w', encoding='utf-8').write(s)
print('ok')
