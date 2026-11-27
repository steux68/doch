#!/usr/bin/env python3
"""Staunen -> Grammatikwoerter: (1) Ueberblick oben: alle 4 Gruppen mit ihren Woertern auf einen Blick,
Antippen springt zur Karte; (2) "Die Geschichte" ist offen; (3) Geschichtstexte leserfreundlicher
(kuerzere Saetze, Fachwoerter uebersetzt; Fakten unveraendert nach DWDS).
Aufruf: python3 src/gram_ueberblick_test.py [live]   DOCH_SRC/DOCH_OUT fuer Ketten. Idempotent ueber id="gwu-css"."""
import os,sys
LIVE='live' in sys.argv[1:]
root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
s=open(os.environ.get('DOCH_SRC',os.path.join(root,'index.html')),encoding='utf-8').read()
if 'id="gwu-css"' in s: print('already'); raise SystemExit

X={
"Aus griechisch grammatikḗ (téchnē), „Kunst der Buchstaben“, zu grámma, „Buchstabe, Geschriebenes“ (gráphein, ritzen, schreiben). Über das Lateinische kam das Wort ins Althochdeutsche (grammatih um 1000); die heutige Form Grammatik gibt es seit dem 16. Jahrhundert.":
"Grammatik heißt wörtlich „die Kunst der Buchstaben“. Das Wort ist griechisch: grámma ist der Buchstabe, gráphein heißt ritzen oder schreiben. Über das Lateinische kam es ins Althochdeutsche – um das Jahr 1000 schrieb man grammatih. Die heutige Form gibt es seit dem 16. Jahrhundert.",
"Aus lateinisch cāsus nōminātīvus, „Fall des Nennens“ (zu nōmināre, nennen). Als deutsches Wort zuerst 1691 bei Kaspar von Stieler. Daneben standen Nennendung und später bei Gottsched Nennfall.":
"Der Nominativ ist der Fall, der etwas nennt: wer oder was etwas tut. Der Name kommt von lateinisch nōmināre, „nennen“. Als deutsches Wort steht Nominativ zuerst 1691 bei Kaspar von Stieler. Es gab auch deutsche Namen: Nennendung und später, bei Gottsched, Nennfall.",
"Aus lateinisch cāsus accūsātīvus, „Fall der Anklage“ (zu accūsāre, anklagen). Das ist ein Übersetzungsfehler: Das griechische Vorbild aitiatikḗ meinte den Fall, den das Verb bewirkt, und kommt von aition, „Ursache“. Deutsche Namen wie Klagendung (1641) und Klagefall (Lessing 1759) setzten sich nicht durch; im 19. Jahrhundert wurde Akkusativ üblich.":
"Hinter dem Namen steckt ein Übersetzungsfehler. Die Griechen sagten aitiatikḗ: der Fall für das, was das Verb bewirkt (von aition, „Ursache“). Im Lateinischen wurde daraus accūsātīvus – der „Fall der Anklage“ (accūsāre, anklagen). Deutsche Namen wie Klagendung (1641) und Klagefall (Lessing, 1759) setzten sich nicht durch. Erst im 19. Jahrhundert wurde Akkusativ üblich.",
"Aus lateinisch cāsus datīvus, „Fall des Gebens“, nach griechisch dotikḗ ptōsis. Beide gehören zu „geben“ (dare, didónai). Frühe deutsche Übersetzungen waren Drittfall (frühes 17. Jahrhundert) und Gebendung (spätes 17. Jahrhundert), etwa gleichzeitig kommt Dativ als deutsches Wort auf.":
"Der Dativ ist der Fall des Gebens: Er sagt, wem etwas gegeben wird. Lateinisch dare und griechisch didónai heißen beide „geben“. Im 17. Jahrhundert versuchte man es auf Deutsch – zuerst mit Drittfall, später mit Gebendung. Etwa zur selben Zeit kam Dativ als deutsches Wort auf.",
"Aus lateinisch cāsus genitīvus, nach griechisch genikḗ ptōsis, dem „allgemeinen Fall“ (zur Gattung gehörig). Lateinische Grammatiker brachten es fälschlich mit „zeugen“ zusammen; darum hieß der Fall im Deutschen auch Zeugefall. Andere Versuche: Besitzfall (1619). Genitiv oder Genetiv setzt sich Mitte des 18. Jahrhunderts durch.":
"Die Griechen nannten ihn genikḗ ptōsis, den „allgemeinen Fall“: den Fall, der die Gattung angibt. Lateinische Grammatiker verbanden das Wort fälschlich mit „zeugen“. Deshalb hieß er auf Deutsch auch Zeugefall. 1619 versuchte man es mit Besitzfall. Durchgesetzt hat sich Mitte des 18. Jahrhunderts Genitiv (oder Genetiv).",
"Aus lateinisch verbum, „Wort“. Im 15. Jahrhundert kam es als Fachwort in die deutschen Grammatiken. Daneben gab es Namen wie Zeitwort, Sagwort und Tätigkeitswort. Die Form Verb ist seit der ersten Hälfte des 18. Jahrhunderts belegt, wurde aber erst Ende des 19. Jahrhunderts üblich.":
"Verb heißt einfach „Wort“ – lateinisch verbum. Im 15. Jahrhundert tauchte es als Fachwort in deutschen Grammatiken auf. Daneben gab es deutsche Namen: Zeitwort, Sagwort, Tätigkeitswort. Die kurze Form Verb gibt es seit dem frühen 18. Jahrhundert; üblich wurde sie aber erst Ende des 19. Jahrhunderts.",
"Aus lateinisch articulus, „kleines Gelenk, Glied“ (zu artus, Glied). 1291 ist es zuerst als Abschnitt eines Vertrags belegt. Als Grammatikwort, gleichsam ein „Gelenk“ im Satz, wurde es im 16. Jahrhundert entlehnt und ist seit dem 17. Jahrhundert der übliche Name für der, die, das. Der Zeitungsartikel kommt erst im 18. Jahrhundert.":
"Lateinisch articulus heißt „kleines Gelenk, Glied“. Der Artikel ist also ein kleines Gelenk im Satz. Zuerst, 1291, bezeichnete das Wort einen Abschnitt in einem Vertrag. Als Grammatikwort kam es im 16. Jahrhundert; seit dem 17. Jahrhundert ist es der übliche Name für der, die, das. Den Zeitungsartikel gibt es erst seit dem 18. Jahrhundert.",
"Aus lateinisch praepositio, „das Voranstellen“ (zu praepōnere, voranstellen). Mitte des 17. Jahrhunderts als Fachwort entlehnt. Deutsche Namen waren Vorwort (Schottelius 1641) und Vorsetzwort; seit 1801 setzte Campe Verhältniswort dagegen, und das wurde die deutsche Entsprechung.":
"Die Präposition steht vor dem Nomen – genau das sagt ihr Name: lateinisch praepōnere heißt „voranstellen“. Mitte des 17. Jahrhunderts wurde das Wort im Deutschen zum Fachwort. Schottelius sagte 1641 Vorwort, andere Vorsetzwort. 1801 schlug Campe Verhältniswort vor – das ist bis heute das deutsche Wort dafür.",
"Aus spätlateinisch (modus) coniūnctīvus, „verbindende Form“, zu coniungere, verbinden. Dasselbe Verb steckt in Konjunktion. Im 17. Jahrhundert ins Deutsche übernommen; bis ins 19. Jahrhundert schrieb man oft noch Conjunctivus.":
"Konjunktiv heißt „verbindende Form“, von lateinisch coniungere, „verbinden“. Dasselbe Verb steckt in Konjunktion, dem Bindewort. Ins Deutsche kam der Begriff im 17. Jahrhundert; bis ins 19. Jahrhundert schrieb man oft noch Conjunctivus.",
"Als Fachwort prägte es Jacob Grimm 1819 für den vererbten Vokalwechsel in verwandten Wörtern. Vorher kam das Wort im 17. und 18. Jahrhundert nur gelegentlich vor, locker für einen schiefen, unreinen Klang. Es setzt sich aus ab und Laut zusammen.":
"Das Wort ist einfach gebaut: ab + Laut. Im 17. und 18. Jahrhundert kam es nur selten vor, locker für einen schiefen, unreinen Klang. 1819 machte Jacob Grimm daraus ein Fachwort – für den alten, vererbten Vokalwechsel in verwandten Wörtern wie singen, sang, gesungen.",
}
for a,b in X.items():
    assert s.count(a)==1,a[:40]; s=s.replace(a,b)
A="</div><details><summary>Die Geschichte</summary>"
assert s.count(A)==1; s=s.replace(A,"</div><details open><summary>Die Geschichte</summary>")

CSS='''<style id="gwu-css">
/* Staunen: Geschichte und Grammatikwoerter scrollen selbst; die Kappung aus Studieren (max-height + overflow:hidden) darf hier nicht greifen */
html[data-dmode="s"] #hscroll[data-sec="gram"] #p-gram,html[data-dmode="s"] #hscroll[data-sec="hist"] #p-hist{overflow-y:auto!important;max-height:none!important;-webkit-overflow-scrolling:touch;overscroll-behavior-y:contain}
#p-gram .gwu{margin:6px 0 4px;padding:12px 12px 10px;background:#fff;border:1px dotted #b8b8b8}
#p-gram .gwu>p{margin:0 0 8px;font-size:12px;letter-spacing:.14em;font-weight:700;text-transform:uppercase;color:#555}
#p-gram .gwu .r{padding:8px 0 10px;border-top:1px dotted #d0d0d0}
#p-gram .gwu .r>i{display:block;font-style:normal;font-size:12px;line-height:1.25;color:var(--red);font-weight:700;margin-bottom:6px}
#p-gram .gwu .r>span{display:flex;flex-wrap:wrap;gap:5px}
#p-gram .gwu button{font:inherit;font-size:14px;min-height:34px;padding:4px 8px;border:1px solid #cfcfcf;border-left:4px solid var(--cc,#bfe4d6);background:#f7f7f5;color:#1a1a1a;cursor:pointer}
#p-gram .gwu button:active{background:#e9e9e6}
#p-gram .fwc.flash{animation:gwuF 1.2s ease-out}
@keyframes gwuF{0%{box-shadow:0 0 0 3px #cdff3e}100%{box-shadow:0 0 0 3px transparent}}
@media (max-width:360px){#p-gram .gwu{padding:10px 8px}#p-gram .gwu button{font-size:13px;padding:4px 6px;border-left-width:3px}#p-gram .gwu .r>span{gap:4px}}
</style>'''
JS='''<script id="gwu-js">(function(){try{if(typeof DMODE==="undefined"||DMODE!=="s")return;var P=document.getElementById("p-gram");if(!P||P.querySelector(".gwu"))return;
var H=[].slice.call(P.querySelectorAll("h3.fwh"));if(!H.length)return;var n=0,rows="";
H.forEach(function(h){var b="";for(var e=h.nextElementSibling;e&&e.tagName!=="H3";e=e.nextElementSibling){if(!e.classList.contains("fwc"))continue;n++;e.id="gw"+n;
 var w=(e.querySelector(".fwt b")||{}).textContent||"",cc=e.style.getPropertyValue("--cc");
 b+='<button type="button" data-t="gw'+n+'"'+(cc?' style="--cc:'+cc+'"':'')+'>'+w.replace(/^(der|die|das) /,"")+'</button>';}
 rows+='<div class="r"><i>'+h.textContent+'</i><span>'+b+'</span></div>';});
var d=document.createElement("nav");d.className="gwu";d.setAttribute("aria-label","Überblick");
d.innerHTML='<p>Überblick · '+n+' Wörter in '+H.length+' Gruppen</p>'+rows;P.insertBefore(d,P.firstChild);
d.addEventListener("click",function(e){var b=e.target.closest("button");if(!b)return;var c=document.getElementById(b.dataset.t);if(!c)return;
 P.scrollTo({top:c.offsetTop-P.offsetTop-8,behavior:"smooth"});c.classList.remove("flash");void c.offsetWidth;c.classList.add("flash");});
}catch(e){}})();</script>'''
s=s+CSS+JS
out=os.environ.get('DOCH_OUT') or os.path.join(root,'index.html' if LIVE else 'gramm7.html')
open(out,'w',encoding='utf-8').write(s);print('wrote',out)
