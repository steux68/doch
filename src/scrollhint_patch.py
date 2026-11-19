# Test: Scroll-Hinweis (durchsichtiger Kreis mit Pfeil) + kurze Tipp-Welle. Schreibt NUR hint.html (Testkopie), index.html bleibt unberührt. 19.11.2026
import sys
s = open('index.html', encoding='utf-8').read()
if 'id="scrollhint-css"' in s:
    print('schon vorhanden'); sys.exit(0)
CSS = '''<style id="scrollhint-css">
/* 19.11: Tipp-Welle: schwarzer Punkt + graue Ringe (wie die Dasein-Kreise), fängt keine Berührung ab, liegt über allen Pop-ups */
.rip{position:fixed;z-index:2000;pointer-events:none;border-radius:50%}
.rip{width:44px;height:44px;margin:-22px 0 0 -22px;background:radial-gradient(circle,#000 0 2.5px,transparent 3px);animation:ripd 1.1s ease-out forwards}
.rip::before,.rip::after{content:"";position:absolute;inset:0;border-radius:50%;border:1.5px solid #222;opacity:0;animation:ripr 1.1s ease-out forwards}
.rip::after{border-color:#9a9a9a;animation-delay:.2s}
@keyframes ripr{0%{transform:scale(.12);opacity:1}100%{transform:scale(1);opacity:0}}
@keyframes ripd{0%{opacity:1}100%{opacity:0}}
.rip.tease{animation:tg 2.2s ease-in-out forwards}
.rip.tease::before,.rip.tease::after{animation-duration:.7s;animation-iteration-count:3}
@keyframes tg{0%{opacity:0;transform:translateX(0)}12%{opacity:1}55%{opacity:1;transform:translateX(var(--dx,-110px))}100%{opacity:0;transform:translateX(0)}}
@media (prefers-reduced-motion:reduce){.rip{animation-duration:.01s}}
</style>
'''
JS = '''<script id="scrollhint-js">(function(){
/* Tipp-Welle: schwarzer Punkt + graue Ringe, folgt dem Finger ein Stück */
var rp=null,rx=0,ry=0;
addEventListener("pointerdown",function(e){var r=document.createElement("div");r.className="rip";r.style.left=e.clientX+"px";r.style.top=e.clientY+"px";document.body.appendChild(r);rp=r;rx=e.clientX;ry=e.clientY;setTimeout(function(){r.remove();if(rp===r)rp=null},1400);},true);
function fol(x,y){if(!rp)return;var dx=Math.max(-70,Math.min(70,(x-rx)*.55)),dy=Math.max(-70,Math.min(70,(y-ry)*.55));rp.style.transform="translate("+dx+"px,"+dy+"px)";}
addEventListener("touchmove",function(e){var t=e.touches[0];if(t)fol(t.clientX,t.clientY)},{passive:true,capture:true});
addEventListener("mousemove",function(e){if(e.buttons)fol(e.clientX,e.clientY)},true);
})();</script>
'''

BCSS = '''<style id="barfx-css">
/* 19.11: Mikro-Animation der Menüleisten: beim Halten wölbt sich die Leiste (Höhe x1,5, Schrift x1,3) und federt beim Loslassen zurück;
   rastet eine Leiste oben ein, kurz grösser, dann kleiner, dann fest. Nur transform/zoom, kein Layout-Sprung. */
.hb{transition:transform .38s cubic-bezier(.3,1.7,.5,1)}
.hb>b,.hb>small{transition:font-size .38s cubic-bezier(.3,1.7,.5,1),transform .38s cubic-bezier(.3,1.7,.5,1);transform-origin:left center}
.hb.hold{z-index:40;transform:scale(1,1.5);transition:transform .2s cubic-bezier(.2,1.3,.4,1)}
.hb.hold>b{font-size:16.2px}.hb.hold>small{font-size:12.4px}
.hb.hold>b,.hb.hold>small{transform:scale(1,.667);transition:font-size .2s cubic-bezier(.2,1.3,.4,1),transform .2s cubic-bezier(.2,1.3,.4,1)}
.hb.lock:not(.hold){z-index:40;animation:blk .6s ease-out}
.hb.lock:not(.hold)>b{animation:blkb .6s ease-out}.hb.lock:not(.hold)>small{animation:blks .6s ease-out}
@keyframes blk{0%{transform:scale(1,1)}32%{transform:scale(1,1.5)}68%{transform:scale(1,.9)}100%{transform:scale(1,1)}}
@keyframes blkb{0%{font-size:12.5px;transform:none}32%{font-size:16.2px;transform:scale(1,.667)}68%{font-size:11.9px;transform:scale(1,1.11)}100%{font-size:12.5px;transform:none}}
@keyframes blks{0%{font-size:9.5px;transform:none}32%{font-size:12.4px;transform:scale(1,.667)}68%{font-size:9px;transform:scale(1,1.11)}100%{font-size:9.5px;transform:none}}
@media (prefers-reduced-motion:reduce){.hb,.hb>b,.hb>small{transition:none!important;animation:none!important}}
</style>
'''
BJS = '''<script id="barfx-js">(function(){
var SC=document.getElementById("hscroll");if(!SC)return;
var held=[],t0=0,stuck=new WeakMap(),raf=0,ready=0;
function on(e){var b=e.target&&e.target.closest?e.target.closest(".hb"):null;if(!b)return;b.classList.remove("lock");b.classList.add("hold");held.push(b);t0=Date.now();}
function off(){var l=held;held=[];if(!l.length)return;var w=Math.max(0,170-(Date.now()-t0));setTimeout(function(){l.forEach(function(b){b.classList.remove("hold")})},w);}
document.addEventListener("touchstart",on,{passive:true,capture:true});
document.addEventListener("mousedown",on,true);
["touchend","touchcancel","mouseup","dragend","blur"].forEach(function(n){addEventListener(n,off,true)});
/* Wisch-Andeutung der Zeitleiste: der Punkt wischt von rechts nach links (Finger-Richtung), die Leiste rutscht mit; am Ende umgekehrt */
function swipeTease(lift){var tl=document.getElementById("tl"),hb=SC.querySelector('.hb[data-i="5"]');if(!tl||!hb)return false;
 var r=tl.getBoundingClientRect();if(r.width<100||r.bottom<=0||r.top>=innerHeight*.9)return false;
 var u=document.elementFromPoint(r.left+r.width/2,r.top+r.height/2);if(!u||!tl.contains(u))return false;
 var max=tl.scrollWidth-tl.clientWidth,sl=tl.scrollLeft,dir=sl>=max-5?-1:1,am=sl<5?40:22;
 var d=document.createElement("div");d.className="rip tease";d.style.setProperty("--dx",(dir>0?-110:110)+"px");d.style.left=(dir>0?r.right-60:r.left+60)+"px";d.style.top=(r.top+r.height/2)+"px";document.body.appendChild(d);setTimeout(function(){d.remove()},2400);
  setTimeout(function(){tl.scrollTo({left:sl+dir*am,behavior:"smooth"})},300);
 setTimeout(function(){tl.scrollTo({left:sl,behavior:"smooth"})},1300);return true;}
function check(){raf=0;var ct=SC.getBoundingClientRect().top,bars=SC.querySelectorAll(".hb"),i,b,r,top,s;
 for(i=0;i<bars.length;i++){b=bars[i];r=b.getBoundingClientRect();top=parseFloat(b.style.top);if(isNaN(top))top=0;
  s=r.height>0&&r.top<=ct+top+1&&r.top>=ct-2;
  if(ready&&s&&stuck.get(b)===false&&!b.classList.contains("hold")){b.classList.remove("lock");void b.offsetWidth;b.classList.add("lock");(function(x){setTimeout(function(){x.classList.remove("lock")},700)})(b);}
  stuck.set(b,s);}
 ready=1;}
/* Hinweis-Zyklen: kommt man auf eine Seite, wischt die Zeitleiste 3-mal; danach je Ziel aus, bis die App neu geöffnet wird. Eine Berührung bricht den Zyklus ab. */
var done2={},busy=0,lastInt=Date.now(),GAP=1700;
function cycle(n,step){var t0=Date.now(),i=0;busy=1;(function go(){if(lastInt>t0||!step(i)){busy=0;return}if(++i<n)setTimeout(go,GAP);else setTimeout(function(){busy=0},GAP)})();}
function ctx(){if(busy||document.hidden||Date.now()-lastInt<1200)return;
 var a=document.activeElement,app=document.querySelector(".app");
 if((a&&/^(INPUT|TEXTAREA)$/.test(a.tagName))||(app&&(app.dataset.mode==="game"||app.classList.contains("kbo"))))return;
 var hb5=SC.querySelector('.hb[data-i="5"]');
 if(hb5&&stuck.get(hb5)===true){if(done2.tl)return;done2.tl=1;cycle(3,function(i){var ok=swipeTease(i===0);if(!ok&&i===0)done2.tl=0;return ok});return;}
}
["pointerdown","touchstart","touchmove","keydown","wheel"].forEach(function(n){addEventListener(n,function(){lastInt=Date.now()},{passive:true,capture:true})});
SC.addEventListener("scroll",function(){lastInt=Date.now()},{passive:true});
setInterval(ctx,1500);
SC.addEventListener("scroll",function(){if(!raf)raf=requestAnimationFrame(check)},{passive:true});
check();
})();</script>
'''
a = '<script id="info-link-js">'
assert s.count(a) == 1
s = s.replace(a, CSS + JS + BCSS + BJS + a)
out = 'index.html' if 'live' in sys.argv else 'hint.html'
open(out, 'w', encoding='utf-8').write(s)
print(out, 'geschrieben')
