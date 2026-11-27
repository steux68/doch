#!/usr/bin/env python3
"""Staunen-Titelseite: das Zitat haengt in einem barocken Goldrahmen an Draht und Nagel.
Beim Wischen/Scrollen pendelt der Rahmen leicht (gedaempftes Pendel; aus bei prefers-reduced-motion).
Rahmen und Ornamente sind selbst gezeichnet (SVG/CSS), keine fremden Bilder.
Aufruf:  python3 src/rahmen_test.py        -> Testkopie rahmen1.html
         python3 src/rahmen_test.py live   -> index.html
Idempotent ueber id="rahmen-css"."""
import os,sys,urllib.parse
LIVE=len(sys.argv)>1 and sys.argv[1]=='live'
root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
s=open(os.path.join(root,'index.html'),encoding='utf-8').read()
if 'id="rahmen-css"' in s: print('already'); raise SystemExit

GRAD=('<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1">'
 '<stop offset="0" stop-color="#fff2b0"/><stop offset=".35" stop-color="#e2b54a"/>'
 '<stop offset=".7" stop-color="#a8741a"/><stop offset="1" stop-color="#f0cf6e"/></linearGradient></defs>')
ST='fill="url(#g)" stroke="#5e3f08" stroke-width=".9" stroke-linejoin="round"'
# Ecke: Akanthusblaetter entlang beider Kanten, Rosette, Voluten
leaf='M4 4C18 1 34 3 50 10C44 13 37 12 31 11C36 15 38 20 36 26C31 19 22 13 4 4Z'
curl='M50 10c6 1 8 7 4 10c-3 2-7 0-6-3c1-2 3-2 4-1'
leaf2='M8 8C14 14 22 18 28 30C22 28 16 22 8 8Z'
corner=('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">'+GRAD+
 '<g '+ST+'><path d="'+leaf+'"/><path d="'+leaf+'" transform="matrix(0 1 1 0 0 0)"/><path d="'+leaf2+'"/></g>'+
 '<g fill="none" stroke="#5e3f08" stroke-width="1.6" stroke-linecap="round"><path d="'+curl+'"/><path d="'+curl+'" transform="matrix(0 1 1 0 0 0)"/></g>'+
 '<circle cx="12" cy="12" r="8" '+ST+'/><circle cx="12" cy="12" r="3.6" fill="#fff4c2" stroke="#5e3f08" stroke-width=".8"/></svg>')
# Kartusche oben: Muschel aus Faecherrippen mit Voluten
import math
ribs=''.join('<path d="M40 30 L%.1f %.1f A6 6 0 0 1 %.1f %.1f Z"/>'%(
  40+26*math.cos(a-0.12),30-26*math.sin(a-0.12),40+26*math.cos(a+0.12),30-26*math.sin(a+0.12))
  for a in [math.pi*(0.12+0.76*i/8) for i in range(9)])
shell=('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 80 34">'+GRAD+
 '<g %s>%s<path d="M6 30C2 22 10 16 16 22C12 22 11 26 14 28Z"/><path d="M74 30C78 22 70 16 64 22C68 22 69 26 66 28Z"/>'
 '<ellipse cx="40" cy="30" rx="9" ry="4"/></g></svg>')%(ST,ribs)
import base64
u=lambda x:'url(data:image/svg+xml;base64,'+base64.b64encode(x.encode()).decode()+')'
U_C=u(corner); U_S=u(shell)

CSS='''<style id="rahmen-css">
html[data-dmode="s"] #hscroll[data-n="0"]>#stnT{align-items:safe center}
#stnT .hang{position:relative;margin:4px auto 18px;padding-top:58px;width:min(300px,86%);transform-origin:50% 8px;will-change:transform}
#stnT .hang .nail{position:absolute;left:50%;top:2px;width:12px;height:12px;margin-left:-6px;border-radius:50%;z-index:3;
 background:radial-gradient(circle at 35% 30%,#fff 0 1px,#b9bcc0 2px,#6d7176 5px,#3d4044 6px);box-shadow:1px 2px 2px rgba(0,0,0,.35)}
#stnT .hang .wire{position:absolute;left:0;top:0;width:100%;height:76px;z-index:0;overflow:visible}
#stnT .gf{position:relative;z-index:1;padding:20px;border-radius:3px;
 background:linear-gradient(135deg,#8a5d12 0%,#e9c25a 14%,#fff0b0 22%,#c08a24 34%,#f2d27a 50%,#9a6a16 66%,#f6dc8a 78%,#b07c1c 90%,#6e4a0c 100%);
 box-shadow:0 14px 22px -8px rgba(0,0,0,.45),0 2px 4px rgba(0,0,0,.25),inset 0 0 0 1.5px #4e3406,inset 0 0 0 4px #f6dc8a,inset 0 0 0 5.5px #7a540e,
 inset 0 0 0 13px rgba(0,0,0,0),inset 0 0 0 14px #5e3f08}
#stnT .gf::before{content:"";position:absolute;inset:6px;pointer-events:none;border-radius:2px;
 background:radial-gradient(circle,#fff6c8 0 1.6px,#c8962c 2.2px,#6e4a0c 3px,transparent 3.4px) 0 0/8px 8px;
 -webkit-mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);-webkit-mask-composite:xor;mask:linear-gradient(#000 0 0) content-box exclude,linear-gradient(#000 0 0);padding:7px}
#stnT .gf>.orn{position:absolute;width:46px;height:46px;background:'''+U_C+''' center/contain no-repeat;pointer-events:none;z-index:2;filter:drop-shadow(0 1px 1px rgba(0,0,0,.35))}
#stnT .gf>.o1{left:-9px;top:-9px}#stnT .gf>.o2{right:-9px;top:-9px;transform:scaleX(-1)}
#stnT .gf>.o3{left:-9px;bottom:-9px;transform:scaleY(-1)}#stnT .gf>.o4{right:-9px;bottom:-9px;transform:scale(-1)}
#stnT .gf>.shell{position:absolute;left:50%;top:-17px;width:76px;height:32px;margin-left:-38px;background:'''+U_S+''' center/contain no-repeat;z-index:2;pointer-events:none;filter:drop-shadow(0 1px 1px rgba(0,0,0,.35))}
#stnT .gf>.shell.b{top:auto;bottom:-17px;transform:scaleY(-1)}
#stnT .gf .stq{background:#fbf7ea;padding:16px 14px 14px;gap:6px;box-shadow:inset 0 0 0 1px #8a6212,inset 0 3px 8px rgba(70,45,5,.35)}
#stnT .gf .pic{width:108px;height:108px;margin-bottom:4px;box-shadow:0 0 0 1px #8a6212}
#stnT .gf q{font-size:17px}
@media (max-width:350px){#stnT .gf q{font-size:16px}#stnT .gf .pic{width:92px;height:92px}}
</style>'''

JS='''<script id="rahmen-js">(function(){try{var T=document.getElementById("stnT"),SC=document.getElementById("hscroll");if(!T||!SC)return;
function wrap(){var a=T.querySelector(":scope>a.stq");if(!a)return null;var h=document.createElement("div");h.className="hang";
 h.innerHTML='<svg class="wire" viewBox="0 0 100 76" preserveAspectRatio="none" aria-hidden="true"><path d="M24 74 L50 6 L76 74" fill="none" stroke="#55585c" stroke-width="1.4" vector-effect="non-scaling-stroke" stroke-linejoin="round"/></svg><span class="nail" aria-hidden="true"></span><div class="gf"><i class="orn o1"></i><i class="orn o2"></i><i class="orn o3"></i><i class="orn o4"></i><i class="shell"></i><i class="shell b"></i></div>';
 T.insertBefore(h,a);h.querySelector(".gf").appendChild(a);return h;}
var H=wrap();if(!H)return;
if(window.matchMedia&&matchMedia("(prefers-reduced-motion: reduce)").matches)return;
var th=0,om=0,run=0,last=0,K=20,C=1.1,MAX=7;
function step(t){var dt=Math.min(.04,(t-last)/1000||.016);last=t;om+=(-K*th-C*om)*dt;th+=om*dt;
 if(th>MAX){th=MAX;om=-om*.3}else if(th<-MAX){th=-MAX;om=-om*.3}
 H.style.transform="rotate("+th.toFixed(3)+"deg)";
 if(Math.abs(th)<.03&&Math.abs(om)<.05){th=0;om=0;H.style.transform="";run=0;return;}requestAnimationFrame(step);}
function kick(v){if(SC.getAttribute("data-n")!=="0")return;om+=v;if(om>60)om=60;if(om<-60)om=-60;if(!run){run=1;last=performance.now();requestAnimationFrame(step);}}
var y=0,x=0,sgn=1;
SC.addEventListener("touchstart",function(e){var t=e.touches[0];y=t.clientY;x=t.clientX;},{passive:true});
SC.addEventListener("touchmove",function(e){var t=e.touches[0],dy=t.clientY-y,dx=t.clientX-x;y=t.clientY;x=t.clientX;
 kick(Math.abs(dx)>Math.abs(dy)*.5?dx*1.2:-dy*.9);},{passive:true});
SC.addEventListener("wheel",function(e){kick(-e.deltaY*.08*(sgn=-sgn));},{passive:true});
setTimeout(function(){kick(14)},450);
}catch(e){}})();</script>'''

s=s+CSS+JS
out=os.path.join(root,'index.html' if LIVE else 'rahmen1.html')
open(out,'w',encoding='utf-8').write(s);print('wrote',out)
