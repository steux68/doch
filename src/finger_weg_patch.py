# DOCH! 26.11.2026: Erstes Mal "Finger-Weg": kleiner roter Punkt mit Welle neben dem Ziel + gelbes Etikett.
# Schritt 1 (Start): Punkt links neben Knoten 01, Etikett "Tippe einen Punkt." darueber.
# Schritt 2 (erstes Thema): Punkt unter dem Weiter-Pfeil, Etikett "weiter".
# Merkt sich in localStorage "doch-fw" (0/1/2), keine Linien, nichts auf Linien/Punkten, reduzierte Bewegung = ruhig. Idempotent.
import re, sys
s = open('index.html', encoding='utf-8').read()
if 'id="fw-css"' in s: sys.exit('schon angewendet')
RED = '#a30b17'
css = ('<style id="fw-css">'
 '.fw{position:fixed;z-index:99990;pointer-events:none;opacity:0;transition:opacity .35s}.fw.on{opacity:1}'
 '.fw-d{width:0;height:0}'
 '.fw-d i{position:absolute;left:-12px;top:-12px;width:24px;height:24px;border-radius:50%;border:2px solid @R@;opacity:0;animation:fwrip 3.6s linear infinite}'
 '.fw-d i+i{animation-delay:.45s}'
 '.fw-d u{position:absolute;left:-5px;top:-5px;width:10px;height:10px;border-radius:50%;background:@R@;text-decoration:none;animation:fwcore 3.6s linear infinite}'
 '@keyframes fwrip{0%,6%{transform:scale(.3);opacity:0}10%{opacity:.9}34%{transform:scale(1);opacity:0}100%{opacity:0}}'
 '@keyframes fwcore{0%,4%{transform:scale(0)}9%{transform:scale(1)}30%{transform:none}34%{transform:translate(var(--kx),var(--ky))}38%{transform:none}42%{transform:translate(var(--kx),var(--ky))}46%,100%{transform:none}}'
 '.fw-l{background:#cdff3e;color:#222;border-radius:10px;font:700 14px/1.25 Carlito,sans-serif;padding:4px 10px;white-space:nowrap}'
 '.fw-l span{display:block;overflow:hidden;width:0;animation:fwty 1s steps(var(--n),end) .35s forwards}'
 '@keyframes fwty{to{width:var(--w)}}'
 '@media (prefers-reduced-motion:reduce){.fw-d i{display:none}.fw-d u{animation:none}.fw-l span{animation:none;width:auto}}'
 '</style>').replace('@R@', RED)
js = r'''<script id="fw-js">(function(){
var K="doch-fw",els=[],tm=0;
function get(){try{return +localStorage.getItem(K)||0}catch(e){return 0}}
function put(n){try{if(get()<n)localStorage.setItem(K,n)}catch(e){}}
function $(i){return document.getElementById(i)}
function clear(){clearTimeout(tm);els.forEach(function(e){e.remove()});els=[];}
function dot(x,y,kx,ky){var d=document.createElement("div");d.className="fw fw-d";d.style.left=x+"px";d.style.top=y+"px";d.style.setProperty("--kx",kx+"px");d.style.setProperty("--ky",ky+"px");d.innerHTML="<i></i><i></i><u></u>";document.body.appendChild(d);els.push(d);setTimeout(function(){d.classList.add("on")},20);}
function lab(txt,x,y,align,maxR){var l=document.createElement("div");l.className="fw fw-l";l.innerHTML="<span>"+txt+"</span>";l.style.left="0px";l.style.top=y+"px";document.body.appendChild(l);var sp=l.firstChild;sp.style.setProperty("--w",sp.scrollWidth+"px");sp.style.setProperty("--n",txt.length);var w=sp.scrollWidth+22;var left=align==="c"?x-w/2:x;if(maxR&&left+w>maxR)left=maxR-w;l.style.left=Math.max(4,left)+"px";els.push(l);setTimeout(function(){l.classList.add("on")},20);}
function arm(){tm=setTimeout(clear,14000);}
function show1(){clear();if(get()>=1)return;var h=$("home"),hs=$("hscroll");if(!h||h.hidden||(hs&&hs.scrollTop>4)||($("pop")&&!$("pop").hidden))return;
 var b=document.querySelector("#tstage .pin.l b");if(!b)return;var r=b.getBoundingClientRect(),st=$("tstage").getBoundingClientRect();if(!r.width)return;
 var x=r.left-20,y=r.top+r.height/2;dot(x,y,5,0);lab("Tippe einen Punkt.",st.left,y-14-8-26,"l",0);arm();}
function show2(){clear();if(get()>=2)return;var t=$("topic");if(!t||t.hidden)return;var a=document.querySelectorAll("#obar .ob-a")[1];if(!a)return;var r=a.getBoundingClientRect();if(!r.width)return;
 var cx=r.left+r.width/2,st=$("topic").getBoundingClientRect();dot(cx,r.bottom+9,0,-5);lab("weiter",cx,r.bottom+42,"c",r.right);arm();}
document.addEventListener("pointerdown",function(e){if(!els.length)return;var t=e.target;if(t.closest&&t.closest("#tstage .pin"))put(1);if(t.closest&&t.closest("#obar .ob-a"))put(2);else if(!$("topic").hidden)put(2);clear();},true);
var hs=$("hscroll");if(hs)hs.addEventListener("scroll",function(){if(els.length)clear();},{passive:true});
window.addEventListener("resize",function(){if(els.length)clear();});
var oT=window.openTopic;if(typeof oT==="function")window.openTopic=function(){clear();var r=oT.apply(this,arguments);setTimeout(show2,900);return r;};
var oH=window.goHome;if(typeof oH==="function")window.goHome=function(){clear();var r=oH.apply(this,arguments);setTimeout(show1,700);return r;};
setTimeout(show1,1800);
})();</script>'''
assert '</head>' in s
s = s.replace('</head>', css + '</head>', 1)
s = s.rstrip('\n') + '\n' + js + '\n'
if '--noversion' not in sys.argv:
    s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1) + '2026-11-26r' + m.group(3), s, count=1)
open('index.html', 'w', encoding='utf-8').write(s)
print('ok')
