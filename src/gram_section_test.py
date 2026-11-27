#!/usr/bin/env python3
"""Staunen bekommt eine vierte Leiste "Grammatikwörter" (Zitate A, Geschichte B, Grammatikwörter C, Redewendungen D) mit Karten.
Aufruf:  python3 src/gram_section_test.py          -> schreibt die Testkopie gramm5.html (index.html bleibt unberuehrt)
         python3 src/gram_section_test.py live     -> schreibt index.html
Die Grammatikwort-Zeilen und der Chip aus Redewendungen (src/gramm_woerter_patch.py) werden dabei entfernt. Alle Herkunftsangaben: DWDS, geprueft 27.11.2026."""
import os,re,sys,json
from urllib.parse import quote
LIVE=len(sys.argv)>1 and sys.argv[1]=='live'
root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
s=open(os.path.join(root,'index.html'),encoding='utf-8').read()
if 'id="p-gram"' in s: print('already'); raise SystemExit
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)

# 0 alten Filter aus Redewendungen entfernen
i=s.index(',["gram","A1","die Grammatik"'); j=s.index('];',i); s=s[:i]+s[j:]
rep(', ["gram", "Grammatikwörter"]];','];')

# 1 HTML: Abschnitt zwischen Geschichte und Redewendungen
rep('id="p-hist"></section><section class="hp" id="p-rede"></section>','id="p-hist"></section><section class="hp" id="p-gram"></section><section class="hp" id="p-rede"></section>')
# 2 Leisten-Liste
rep('[["quotes","Zitate"],["hist","Geschichte"],["rede","Redewendungen"],["study","Studieren"]]','[["quotes","Zitate"],["hist","Geschichte"],["gram","Grammatikwörter"],["rede","Redewendungen"],["study","Studieren"]]')
# 3 Zahl der Inhalts-Leisten: Staunen 4, Studieren 3
rep('function bars(){return [].slice.call(SC.querySelectorAll(":scope>.hb")).slice(0,3);}','function bars(){return [].slice.call(SC.querySelectorAll(":scope>.hb")).slice(0,DMODE==="s"?4:3);}')
rep('var bars=function(){return [].slice.call(sc.querySelectorAll(":scope>.hb")).slice(0,3)}','var bars=function(){return [].slice.call(sc.querySelectorAll(":scope>.hb")).slice(0,4)}')
rep('function bars(){return [].slice.call(sc.querySelectorAll(":scope>.hb")).slice(0,3);}','function bars(){return [].slice.call(sc.querySelectorAll(":scope>.hb")).slice(0,4);}')
rep('if(DMODE==="s")bars.slice(0,3).forEach((b,i)=>{const sm=b.querySelector("small");if(sm)sm.textContent="["+"ABC"[i]+"]";});','if(DMODE==="s")bars.slice(0,4).forEach((b,i)=>{const sm=b.querySelector("small");if(sm)sm.textContent="["+"ABCD"[i]+"]";});')
rep('bs.slice(0,3).forEach','bs.slice(0,4).forEach',2)
rep('sec=["quotes","hist","rede"]','sec=["quotes","hist","gram","rede"]')
rep('[$("p-quotes"),$("p-rede"),$("p-hist")].forEach(e=>e&&(e.scrollTop=0))','[$("p-quotes"),$("p-rede"),$("p-hist"),$("p-gram")].forEach(e=>e&&(e.scrollTop=0))')
rep('pick(t0>=0&&t0<3?t0:0)','pick(t0>=0&&t0<4?t0:0)')
rep('Math.min(3,tg+1)','Math.min(4,tg+1)')
rep('PN=["p-quotes","p-hist","p-rede"]','PN=["p-quotes","p-hist","p-gram","p-rede"]')
rep('const last=bars[3],lk=keys[3];','const LI=DMODE==="s"?4:3,last=bars[LI],lk=keys[LI];')
rep('const lb=document.querySelectorAll("#hscroll>.hb")[3];','const lb=document.querySelectorAll("#hscroll>.hb")[DMODE==="s"?4:3];',2)
rep('lk==="wow"?"zitate · redewendungen · geschichte":','lk==="wow"?"zitate · geschichte · grammatikwörter · redewendungen":')
# 4 Buchstaben und Pins der Titelseite
rep('quotes:["s",0],hist:["s",1],rede:["s",2]},L={quotes:"A",hist:"B",rede:"C"}','quotes:["s",0],hist:["s",1],gram:["s",2],rede:["s",3]},L={quotes:"A",hist:"B",gram:"C",rede:"D"}')
pin='<span>Geschichte</span></button>'
rep(pin,pin+'<button class="pin l" data-k="gram" data-x="363.5" data-y="389.0" data-row="0.30" style="--k:6" aria-label="Grammatikwörter [C] – Kassel"><b>07</b><span>Grammatikwörter</span></button>')
rep('wow:"zitate · redewendungen · geschichte"','wow:"zitate · geschichte · grammatikwörter · redewendungen"')
# 5 CSS: Sichtbarkeit, Reihenfolge, Farben
rep('html[data-dmode="d"] #p-quotes,html[data-dmode="d"] #p-rede,html[data-dmode="d"] #p-hist,','html[data-dmode="d"] #p-quotes,html[data-dmode="d"] #p-rede,html[data-dmode="d"] #p-hist,html[data-dmode="d"] #p-gram,')
rep('html[data-dmode="s"] #p-quotes,html[data-dmode="s"] #p-rede,html[data-dmode="s"] #p-hist{display:none!important}','html[data-dmode="s"] #p-quotes,html[data-dmode="s"] #p-rede,html[data-dmode="s"] #p-hist,html[data-dmode="s"] #p-gram{display:none!important}')
rep('html[data-dmode="s"] #hscroll[data-sec="hist"] #p-hist{display:block!important;','html[data-dmode="s"] #hscroll[data-sec="hist"] #p-hist,html[data-dmode="s"] #hscroll[data-sec="gram"] #p-gram{display:block!important;')
rep('html[data-dmode="s"] #hscroll[data-n="0"] #p-quotes,','html[data-dmode="s"] #hscroll[data-n="0"] #p-gram,html[data-dmode="s"] #hscroll[data-n="0"] #p-quotes,')
rep('#p-home,#p-links,#p-hist{background:#f4f4f2}','#p-home,#p-links,#p-hist,#p-gram{background:#f4f4f2}')
rep('#p-home,#p-test,#p-links,#p-quotes,#p-rede,#p-hist{background:#f4f4f2!important}','#p-home,#p-test,#p-links,#p-quotes,#p-rede,#p-hist,#p-gram{background:#f4f4f2!important}')
rep('#p-home,#p-test,#p-links,#p-quotes,#p-rede,#p-hist{scroll-snap-align:start}','#p-home,#p-test,#p-links,#p-quotes,#p-rede,#p-hist,#p-gram{scroll-snap-align:start}')
rep('html[data-dmode="s"] #hscroll>.hb[data-i="3"]{order:20;margin-top:12px!important}','html[data-dmode="s"] #hscroll>.hb[data-i="3"]{order:14}\nhtml[data-dmode="s"] #hscroll[data-n="4"]>.hb[data-i="0"]{order:0}html[data-dmode="s"] #hscroll[data-n="4"]>.hb[data-i="1"]{order:1}html[data-dmode="s"] #hscroll[data-n="4"]>.hb[data-i="2"]{order:2}html[data-dmode="s"] #hscroll[data-n="4"]>.hb[data-i="3"]{order:3}\nhtml[data-dmode="s"] #hscroll>.hb[data-i="4"]{order:20;margin-top:12px!important}\nhtml[data-dmode="s"] #hscroll>.capm.p-gram{display:none!important}',2)

CSS='''<style id="gram-css">
/* Staunen: vierte Leiste. Farben nach Platz: blass blau, creme, mittelblau, flieder, dann gelb (Studieren) */
html[data-dmode="s"] body #hscroll>.hb[data-i="2"]{--pc:#bfe4d6;--pcs:#8fcdb6;background-color:#bfe4d6!important}
html[data-dmode="s"] body #hscroll>.hb[data-i="3"]{--pc:#e1d9f3;--pcs:#c4b6e6;background-color:#e1d9f3!important}
html[data-dmode="s"] body #hscroll>.hb[data-i="4"]{--pc:#f2c14e;--pcs:#e0a622;background-color:#f2c14e!important}
html[data-dmode="s"] #hscroll>.hb[data-i="3"] b{display:inline;gap:0}
html[data-dmode="s"] #hscroll>.hb[data-i="4"] b{display:inline-flex;align-items:center;gap:8px;line-height:1}
html[data-dmode="s"] #hscroll>.hb[data-i="4"] b span{display:block;line-height:1}
html[data-dmode="s"] #hscroll>.hb[data-i="3"] small{text-transform:none;letter-spacing:0;font-size:inherit;margin:0;opacity:1}
html[data-dmode="s"] #hscroll>.hb[data-i="3"]::after{content:none}
/* Karten */
#p-gram{padding:2px 0 28px}
#p-gram .fwh{margin:18px 0 8px;color:var(--red);font-size:13px;letter-spacing:.14em;font-weight:700;text-transform:uppercase}
#p-gram .fwc{position:relative;margin:0 0 10px;padding:0 0 6px;background:#fff;border:1px dotted #b8b8b8}
#p-gram .fwc::before{content:"";position:absolute;left:0;top:0;bottom:0;width:7px;background:var(--cc,#d6d6d1)}
#p-gram .fwt{display:flex;justify-content:space-between;align-items:baseline;gap:8px;padding:10px 12px 0 17px}
#p-gram .fwt b{font-size:21px;line-height:1.2}
#p-gram .fwt .lv{flex:none;font-size:12px;letter-spacing:.08em;color:#555}
#p-gram .fwk{margin:2px 12px 0 17px;color:var(--red);font-size:12px;letter-spacing:.1em;font-weight:700;text-transform:uppercase}
#p-gram .fwq{margin:4px 12px 0 17px;font-size:15px;line-height:1.35}
#p-gram .fwp{display:flex;align-items:stretch;margin:10px 12px 8px 17px}
#p-gram .fws{position:relative;flex:1 1 0;min-width:0;margin-left:-1px;padding:6px 8px;background:#f4f4f2;border:1px dotted #9a9a96}
#p-gram .fws+.fws{margin-left:14px}
#p-gram .fws+.fws::before{content:"";position:absolute;left:-13px;top:50%;width:12px;height:12px;margin-top:-6px;background:linear-gradient(#0000 0,#0000 0),no-repeat center/100% 100%;background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 12 12'%3E%3Cpath d='M1 6h9M6.5 2l4 4-4 4' fill='none' stroke='%23222' stroke-width='1.4'/%3E%3C/svg%3E") center/100% 100% no-repeat}
#p-gram .fws i{display:block;font-style:normal;font-size:10px;letter-spacing:.06em;text-transform:uppercase;color:#666}
#p-gram .fws b{display:block;margin-top:1px;font-size:14px;line-height:1.2;overflow-wrap:break-word}
@media(max-width:360px){#p-gram .fwp{flex-direction:column}#p-gram .fws+.fws{margin:14px 0 0}#p-gram .fws+.fws::before{left:50%;top:-13px;margin:0 0 0 -6px;transform:rotate(90deg)}}
#p-gram .fws small{display:block;margin-top:2px;font-size:12px;line-height:1.25;color:#555}
#p-gram .fws.end{background:var(--cc,#e4e4e0);border-style:solid;border-color:#7a7a76}
#p-gram details{padding:0 12px 4px 17px}
#p-gram summary{list-style:none;cursor:pointer;font-size:13px;letter-spacing:.06em;color:#222;padding:3px 0}
#p-gram summary::-webkit-details-marker{display:none}
#p-gram summary::before{content:"+";display:inline-block;width:16px;color:var(--red);font-weight:700}
#p-gram details[open] summary::before{content:"\\2013"}
#p-gram details p{margin:6px 0;font-size:14px;line-height:1.45}
#p-gram details .ex{font-style:italic;color:#333}
#p-gram details a{color:var(--link,#3a4fb8)}
</style>'''

# 6 Karten-Inhalt
C={'nom':'#ededeb','akk':'#f0be83','dat':'#c3ccfc','gen':'#c4a6ee'}
G=[
("Das Wort selbst",[
 dict(w="die Grammatik",lv="A1",hook="Die Kunst der Buchstaben",q="die Lehre vom Bau einer Sprache und ihren Regeln",ex="Ohne Grammatik versteht man den Satz nicht richtig.",slug="Grammatik",
  steps=[("griechisch","grammatikḗ","Kunst der Buchstaben"),("althochdeutsch","grammatih","um 1000"),("deutsch","Grammatik","16. Jh.")],
  x="Aus griechisch grammatikḗ (téchnē), „Kunst der Buchstaben“, zu grámma, „Buchstabe, Geschriebenes“ (gráphein, ritzen, schreiben). Über das Lateinische kam das Wort ins Althochdeutsche (grammatih um 1000); die heutige Form Grammatik gibt es seit dem 16. Jahrhundert.")]),
("Die vier Fälle",[
 dict(w="der Nominativ",lv="A2",hook="Der Fall, der etwas nennt",q="der Fall des Subjekts: wer oder was?",ex="Der Hund schläft im Garten.",slug="Nominativ",c=C['nom'],
  steps=[("lateinisch","cāsus nōminātīvus","Fall des Nennens"),("deutsch","Nominativ","1691, Stieler")],
  x="Aus lateinisch cāsus nōminātīvus, „Fall des Nennens“ (zu nōmināre, nennen). Als deutsches Wort zuerst 1691 bei Kaspar von Stieler. Daneben standen Nennendung und später bei Gottsched Nennfall."),
 dict(w="der Akkusativ",lv="A2",hook="Ein Übersetzungsfehler",q="der Fall des direkten Objekts: wen oder was?",ex="Ich sehe den Hund.",slug="Akkusativ",c=C['akk'],
  steps=[("griechisch","aitiatikḗ","Fall der Ursache"),("lateinisch","cāsus accūsātīvus","Fall der Anklage"),("deutsch","Akkusativ","19. Jh.")],
  x="Aus lateinisch cāsus accūsātīvus, „Fall der Anklage“ (zu accūsāre, anklagen). Das ist ein Übersetzungsfehler: Das griechische Vorbild aitiatikḗ meinte den Fall, den das Verb bewirkt, und kommt von aition, „Ursache“. Deutsche Namen wie Klagendung (1641) und Klagefall (Lessing 1759) setzten sich nicht durch; im 19. Jahrhundert wurde Akkusativ üblich."),
 dict(w="der Dativ",lv="A2",hook="Der Fall des Gebens",q="der Fall des Empfängers: wem?",ex="Ich gebe dem Kind einen Apfel.",slug="Dativ",c=C['dat'],
  steps=[("griechisch","dotikḗ ptōsis","Fall des Gebens"),("lateinisch","cāsus datīvus","Fall des Gebens"),("deutsch","Dativ","spätes 17. Jh.")],
  x="Aus lateinisch cāsus datīvus, „Fall des Gebens“, nach griechisch dotikḗ ptōsis. Beide gehören zu „geben“ (dare, didónai). Frühe deutsche Übersetzungen waren Drittfall (frühes 17. Jahrhundert) und Gebendung (spätes 17. Jahrhundert), etwa gleichzeitig kommt Dativ als deutsches Wort auf."),
 dict(w="der Genitiv",lv="B1",hook="Eigentlich: der Zeugefall",q="der Fall des Besitzes: wessen?",ex="Das ist das Auto meines Vaters.",slug="Genitiv",c=C['gen'],
  steps=[("griechisch","genikḗ ptōsis","allgemeiner Fall"),("lateinisch","cāsus genitīvus","fälschlich: Zeugefall"),("deutsch","Genitiv","Mitte 18. Jh.")],
  x="Aus lateinisch cāsus genitīvus, nach griechisch genikḗ ptōsis, dem „allgemeinen Fall“ (zur Gattung gehörig). Lateinische Grammatiker brachten es fälschlich mit „zeugen“ zusammen; darum hieß der Fall im Deutschen auch Zeugefall. Andere Versuche: Besitzfall (1619). Genitiv oder Genetiv setzt sich Mitte des 18. Jahrhunderts durch.")]),
("Wortarten",[
 dict(w="das Verb",lv="A1",hook="Einfach: das Wort",q="das Wort für eine Handlung oder einen Zustand",ex="Im Satz steht das Verb an zweiter Stelle.",slug="Verb",
  steps=[("lateinisch","verbum","Wort"),("deutsch","Verb","Anfang 18. Jh.")],
  x="Aus lateinisch verbum, „Wort“. Im 15. Jahrhundert kam es als Fachwort in die deutschen Grammatiken. Daneben gab es Namen wie Zeitwort, Sagwort und Tätigkeitswort. Die Form Verb ist seit der ersten Hälfte des 18. Jahrhunderts belegt, wurde aber erst Ende des 19. Jahrhunderts üblich."),
 dict(w="der Artikel",lv="A1",hook="Ein kleines Gelenk",q="das kleine Wort vor dem Nomen: der, die, das",ex="Der Artikel verrät das Geschlecht des Nomens.",slug="Artikel",
  steps=[("lateinisch","articulus","kleines Gelenk"),("deutsch","Artikel","16. Jh. als Grammatikwort")],
  x="Aus lateinisch articulus, „kleines Gelenk, Glied“ (zu artus, Glied). 1291 ist es zuerst als Abschnitt eines Vertrags belegt. Als Grammatikwort, gleichsam ein „Gelenk“ im Satz, wurde es im 16. Jahrhundert entlehnt und ist seit dem 17. Jahrhundert der übliche Name für der, die, das. Der Zeitungsartikel kommt erst im 18. Jahrhundert."),
 dict(w="die Präposition",lv="B1",hook="Das Voranstellen",q="das Wort vor einem Nomen, das den Fall bestimmt: in, auf, mit",ex="Ich warte auf den Bus.",slug="Präposition",
  steps=[("lateinisch","praepositio","das Voranstellen"),("deutsch","Präposition","Mitte 17. Jh."),("deutsch","Verhältniswort","Campe, 1801")],
  x="Aus lateinisch praepositio, „das Voranstellen“ (zu praepōnere, voranstellen). Mitte des 17. Jahrhunderts als Fachwort entlehnt. Deutsche Namen waren Vorwort (Schottelius 1641) und Vorsetzwort; seit 1801 setzte Campe Verhältniswort dagegen, und das wurde die deutsche Entsprechung.")]),
("Formen und Laute",[
 dict(w="der Konjunktiv",lv="B2",hook="Die verbindende Form",q="die Verbform für Wunsch, Möglichkeit und indirekte Rede",ex="Wenn ich Zeit hätte, käme ich mit.",slug="Konjunktiv",
  steps=[("spätlateinisch","coniūnctīvus","verbindende Form"),("deutsch","Konjunktiv","17. Jh.")],
  x="Aus spätlateinisch (modus) coniūnctīvus, „verbindende Form“, zu coniungere, verbinden. Dasselbe Verb steckt in Konjunktion. Im 17. Jahrhundert ins Deutsche übernommen; bis ins 19. Jahrhundert schrieb man oft noch Conjunctivus."),
 dict(w="der Ablaut",lv="C1",hook="1819 von Jacob Grimm",q="der feste Vokalwechsel in verwandten Wörtern: singen, sang, gesungen",ex="Der Ablaut zeigt sich bei starken Verben wie singen, sang, gesungen.",slug="Ablaut",
  steps=[("deutsch","ab + Laut","vorher: schiefer Klang"),("deutsch","Ablaut","Grimm, 1819")],
  x="Als Fachwort prägte es Jacob Grimm 1819 für den vererbten Vokalwechsel in verwandten Wörtern. Vorher kam das Wort im 17. und 18. Jahrhundert nur gelegentlich vor, locker für einen schiefen, unreinen Klang. Es setzt sich aus ab und Laut zusammen.")]),
]
for g,items in G:
    for it in items:
        it['u']="https://www.dwds.de/wb/"+quote(it['slug'])
JS='''<script id="gram-js">/* Staunen: Grammatikwörter als Karten (Herkunft nach DWDS) */
(function(){if(typeof DMODE==="undefined"||DMODE!=="s")return;var P=document.getElementById("p-gram");if(!P)return;
var G=%s;
function E(t){return String(t==null?"":t).replace(/[&<>"]/g,function(m){return{"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[m]})}
var h="";G.forEach(function(g){h+='<h3 class="fwh">'+E(g[0])+'</h3>';g[1].forEach(function(it){
 h+='<article class="fwc"'+(it.c?' style="--cc:'+it.c+'"':'')+'><div class="fwt"><b>'+E(it.w)+'</b><span class="lv">'+E(it.lv)+'</span></div><div class="fwk">'+E(it.hook)+'</div><p class="fwq">'+E(it.q)+'</p><div class="fwp">';
 it.steps.forEach(function(s,k){h+='<div class="fws'+(k===it.steps.length-1?' end':'')+'"><i>'+E(s[0])+'</i><b>'+E(s[1])+'</b><small>'+E(s[2])+'</small></div>';});
 h+='</div><details><summary>Die Geschichte</summary><p>'+E(it.x)+'</p><p class="ex">Beispiel: '+E(it.ex)+'</p><p><a href="'+E(it.u)+'" target="_blank" rel="noopener">DWDS \\u2197</a></p></details></article>';});});
P.innerHTML=h;})();</script>''' % json.dumps(G,ensure_ascii=False)

# 7 Wisch-Skript (Staunen) fuer vier Abschnitte; es laeuft vor dem alten Wisch-Code (capture + stopImmediatePropagation) und schaltet ihn in Staunen aus
rep('const SEC=["quotes","hist","rede"];','const SEC=["quotes","hist","gram","rede"];')
rep('if(i<0||j<0||j>2||!B[j]','if(i<0||j<0||j>3||!B[j]')
rep('sc.addEventListener("touchend",e=>{if(!E)return;','sc.addEventListener("touchend",e=>{e.stopImmediatePropagation();if(!E)return;')
rep('if(dy<0&&En.end&&n.end)go(1);else if(dy>0&&En.top&&n.top)go(-1);},{passive:true});','if(dy<0&&En.end&&n.end)go(1);else if(dy>0&&En.top&&n.top)go(-1);},{passive:true,capture:true});')
rep('sc.addEventListener("wheel",e=>{const gap=','sc.addEventListener("wheel",e=>{e.stopImmediatePropagation();const gap=')
rep('else if(e.deltaY<0&&n.top)go(-1);},{passive:true});','else if(e.deltaY<0&&n.top)go(-1);},{passive:true,capture:true});')

# 8 einfuegen
k=s.rindex('</head>') if '</head>' in s else s.rindex('</style>')+8
s=s[:k]+CSS+s[k:]
b=s.rindex('</body>') if '</body>' in s else len(s)
s=s[:b]+JS+s[b:]
if LIVE:
    m=re.search(r'(<meta name="app-version" content=")([^"]*)(")',s); s=s.replace(m.group(0),m.group(1)+'2026-11-28-fachwoerter'+m.group(3),1)
    open(os.path.join(root,'index.html'),'w',encoding='utf-8').write(s); print('live ok')
else:
    s=s.replace('<title>','<title>[Test Fachwörter] ',1)
    open(os.path.join(root,'gramm5.html'),'w',encoding='utf-8').write(s); print('ok')
