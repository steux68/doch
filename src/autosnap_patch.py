#!/usr/bin/env python3
"""Seitenweise einrasten (Steuart, 13 Nov): Wenn das Scrollen zur Ruhe kommt und ein Abschnittsanfang (Menueleiste) nah ist,
springt die Seite von selbst dorthin, statt halb zwischen zwei Abschnitten stehen zu bleiben. Vorwaerts bis 45 % der Hoehe,
zurueck zum aktuellen Anfang nur bis 18 % (damit man in langen Abschnitten in Ruhe lesen kann). Idempotent."""
f="index.html"
s=open(f,encoding="utf8").read()
if 'id="autosnap-js"' in s:
    print("already patched"); raise SystemExit
js='''<script id="autosnap-js">/* rastet am Abschnittsanfang ein, wenn das Scrollen aufhoert und ein Anfang nah ist */
(function(){try{if(typeof SC==="undefined"||typeof allTop!=="function"||typeof ALLP==="undefined")return;
var last=SC.scrollTop,dir=0,timer=0,touching=false,busy=0;
function open(){return !!document.querySelector(".tlpop:not([hidden]),dialog[open]");}
function pts(){return ALLP.map(function(_,i){return Math.round(allTop(i));});}
function settle(){if(touching||open())return;var y=SC.scrollTop,V=SC.clientHeight,P=pts(),best=null,bd=1e9,max=SC.scrollHeight-V;
 P.forEach(function(p){if(p>max+2)return;var d=p-y,a=Math.abs(d);if(a<3)return;var lim=d>0?(dir>=0?.45:.18):(dir<=0?.45:.18);if(a<lim*V&&a<bd){bd=a;best=p;}});
 if(best===null)return;busy=Date.now()+900;SC.scrollTo({top:best,behavior:(typeof reduceM!=="undefined"&&reduceM)?"auto":"smooth"});}
SC.addEventListener("scroll",function(){var y=SC.scrollTop;if(Math.abs(y-last)>0){dir=y>last?1:-1;last=y;}if(Date.now()<busy)return;clearTimeout(timer);timer=setTimeout(settle,160);},{passive:true});
SC.addEventListener("touchstart",function(){touching=true;clearTimeout(timer);},{passive:true});
SC.addEventListener("touchend",function(){touching=false;clearTimeout(timer);timer=setTimeout(settle,220);},{passive:true});
SC.addEventListener("touchcancel",function(){touching=false;},{passive:true});
window.__snapSettle=settle;}catch(e){}})();
</script>
'''
marker='<script id="spiel-js">'
assert s.count(marker)==1
s=s.replace(marker,js+marker)
assert s.count('content="2026-11-13c"')==1
s=s.replace('content="2026-11-13c"','content="2026-11-13d"')
open(f,"w",encoding="utf8").write(s)
print("patched")
