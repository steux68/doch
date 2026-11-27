#!/usr/bin/env python3
"""Staunen-Titelseite: das Zitat haengt in einem barocken Goldrahmen an Draht und Nagel.
Beim Wischen/Scrollen pendelt der Rahmen leicht (gedaempftes Pendel; aus bei prefers-reduced-motion).
Rahmenbild: img/rahmen-gold.webp, Pixabay 1978727 (Pixabay Content License, frei nutzbar), von Steuart ausgesucht 27.11.2026.
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
#stnT .hang{position:relative;margin:14px auto 22px;padding-top:44px;transform-origin:50% 6px;will-change:transform}
#stnT .hang .nail{position:absolute;left:50%;top:0;width:12px;height:12px;margin-left:-6px;border-radius:50%;z-index:3;
 background:radial-gradient(circle at 35% 30%,#fff 0 1px,#b9bcc0 2px,#6d7176 5px,#3d4044 6px);box-shadow:1px 2px 2px rgba(0,0,0,.35)}
#stnT .hang .wire{position:absolute;left:0;top:0;width:100%;height:170px;z-index:0;overflow:visible}
#stnT .gf{position:relative;z-index:1;aspect-ratio:2387/3600;width:100%}
#stnT .gf::before{content:"";position:absolute;left:15.5%;right:15%;top:26%;bottom:13%;background:#fbf7ea;box-shadow:inset 0 2px 10px rgba(70,45,5,.35);z-index:0}
#stnT .gf::after{content:"";position:absolute;inset:0;background:url(img/rahmen-gold.webp) center/100% 100% no-repeat;z-index:1;pointer-events:none;filter:drop-shadow(0 8px 8px rgba(0,0,0,.35))}
#stnT .gf .stq{position:absolute;left:21%;right:20.5%;top:31%;bottom:19%;transition:opacity .22s;z-index:2;justify-content:center;padding:0;gap:4px;overflow:hidden;font-size:var(--fz,16px)}
#stnT .gf .pic{width:4.6em;height:4.6em;margin-bottom:2px;box-shadow:0 0 0 1px #8a6212}
#stnT .gf .tap{position:absolute;right:22%;top:32%;width:16px;height:16px;margin:-8px -8px 0 0;border-radius:50%;background:#cdff3e;border:1.5px solid #1a1a1a;z-index:3;pointer-events:none}
#stnT .gf .tap::after{content:"";position:absolute;inset:-7px;border:1.5px solid rgba(227,6,19,.55);border-radius:50%;animation:dsRing 2.4s ease-out infinite}
#stnT .gf q{font-size:1em;line-height:1.3}#stnT .gf b{font-size:.92em}#stnT .gf small{font-size:.74em;line-height:1.3}#stnT .gf .stq.tight .pic{width:3.4em;height:3.4em}
</style>'''

JS='''<script id="rahmen-js">(function(){try{var T=document.getElementById("stnT"),SC=document.getElementById("hscroll");if(!T||!SC)return;
function wrap(){var a=T.querySelector(":scope>a.stq");if(!a)return null;var h=document.createElement("div");h.className="hang";
 h.innerHTML='<svg class="wire" viewBox="0 0 100 170" preserveAspectRatio="none" aria-hidden="true"><path d="M20 168 L50 6 L80 168" fill="none" stroke="#55585c" stroke-width="1.4" vector-effect="non-scaling-stroke" stroke-linejoin="round"/></svg><span class="nail" aria-hidden="true"></span><div class="gf"><span class="tap" aria-hidden="true"></span></div>';
 T.insertBefore(h,a);h.querySelector(".gf").appendChild(a);a.setAttribute("aria-label","Nächstes Zitat");a.title="Antippen: nächstes Zitat";return h;}
var H=wrap();if(!H)return;var A=H.querySelector(".stq");
function fit(){var W=T.clientWidth,Ht=T.clientHeight;if(!W||!Ht)return;var w=Math.min(W*.72,330,(Ht-130)/1.508);w=Math.max(w,200);H.style.width=Math.round(w)+"px";
 var f=Math.min(18,w/18);A.style.setProperty("--fz",f+"px");if(A.clientHeight<40)return;A.classList.remove("tight");var n=0;function need(){var c=A.children;return c[c.length-1].getBoundingClientRect().bottom-c[0].getBoundingClientRect().top;}
 while(need()>A.clientHeight-4&&f>9&&n++<40){f-=.5;if(f<12.5)A.classList.add("tight");A.style.setProperty("--fz",f+"px");}}
fit();requestAnimationFrame(fit);setTimeout(fit,300);addEventListener("resize",fit);new MutationObserver(fit).observe(SC,{attributes:true,attributeFilter:["data-n"]});
var im=A.querySelector("img");if(im)im.addEventListener("load",fit);
var RM=window.matchMedia&&matchMedia("(prefers-reduced-motion: reduce)").matches;
var th=0,om=0,run=0,last=0,K=20,C=1.1,MAX=7;
function step(t){var dt=Math.min(.04,(t-last)/1000||.016);last=t;om+=(-K*th-C*om)*dt;th+=om*dt;
 if(th>MAX){th=MAX;om=-om*.3}else if(th<-MAX){th=-MAX;om=-om*.3}
 H.style.transform="rotate("+th.toFixed(3)+"deg)";
 if(Math.abs(th)<.03&&Math.abs(om)<.05){th=0;om=0;H.style.transform="";run=0;return;}requestAnimationFrame(step);}
function kick(v){if(RM||SC.getAttribute("data-n")!=="0")return;om+=v;if(om>60)om=60;if(om<-60)om=-60;if(!run){run=1;last=performance.now();requestAnimationFrame(step);}}
var y=0,x=0,sgn=1;
SC.addEventListener("touchstart",function(e){var t=e.touches[0];y=t.clientY;x=t.clientX;},{passive:true});
SC.addEventListener("touchmove",function(e){var t=e.touches[0],dy=t.clientY-y,dx=t.clientX-x;y=t.clientY;x=t.clientX;
 kick(Math.abs(dx)>Math.abs(dy)*.5?dx*1.2:-dy*.9);},{passive:true});
SC.addEventListener("wheel",function(e){kick(-e.deltaY*.08*(sgn=-sgn));},{passive:true});
setTimeout(function(){kick(14)},450);
var E=function(s){return String(s==null?"":s).replace(/[&<>"]/g,function(m){return{"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[m];});};
function nextQ(){if(typeof QUOTES==="undefined")return;var L=QUOTES.filter(function(x){return x&&!x.sec&&x.q;}),n=L.length;if(n<2)return;
 var st=[7,5,3,11,13,17,19,23],k=3;for(var a=0;a<st.length;a++){var g=st[a],b=n;while(b){var r=g%b;g=b;b=r;}if(g===1){k=st[a];break;}}
 var c=0;try{c=parseInt(localStorage.getItem("stnQ")||"0",10)||0;}catch(e){}c++;try{localStorage.setItem("stnQ",String(c));}catch(e){}
 var x=L[(c*k)%n];A.style.opacity=0;setTimeout(function(){A.href=x.u;A.innerHTML='<span class="pic" aria-hidden="true"><i>'+E(x.pic)+'</i>'+(x.w?'<img alt="" data-w="'+E(x.w.join("|"))+'">':'')+'</span><q>'+E(x.q)+'</q><b>'+E(x.who)+'</b><small>'+E(x.when)+' · Wikipedia ↗</small>';
 try{loadPics(A)}catch(e){}var im=A.querySelector("img");if(im)im.addEventListener("load",fit);fit();A.style.opacity=1;},220);}
H.addEventListener("click",function(e){if(e.target.closest&&e.target.closest("small"))return;e.preventDefault();kick((Math.random()<.5?-1:1)*34);nextQ();});
}catch(e){}})();</script>'''

OLD='function go(d){const i=cur(),j=i+d,B=bars();if(i<0||j<0||j>3||!B[j]||Date.now()<busy)return;busy=Date.now()+900;B[j].click();}'
assert OLD in s
s=s.replace(OLD,'function go(d){const B=bars();if(sc.getAttribute("data-n")==="0"){if(d>0&&B[0]&&Date.now()>=busy){busy=Date.now()+900;B[0].click();}return;}const i=cur(),j=i+d;if(i<0||j<0||j>3||!B[j]||Date.now()<busy)return;busy=Date.now()+900;B[j].click();}')
s=s+CSS+JS
out=os.path.join(root,'index.html' if LIVE else 'rahmen4.html')
open(out,'w',encoding='utf-8').write(s);print('wrote',out)
