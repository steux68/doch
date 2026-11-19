# Test: Scroll-Hinweis (durchsichtiger Kreis mit Pfeil) + kurze Tipp-Welle. Schreibt NUR hint.html (Testkopie), index.html bleibt unberührt. 19.11.2026
import sys
s = open('index.html', encoding='utf-8').read()
if 'id="scrollhint-css"' in s:
    print('schon vorhanden'); sys.exit(0)
CSS = '''<style id="scrollhint-css">
/* 19.11: Scroll-Hinweis + Tipp-Welle: rund, durchsichtiges Gelb (wie der Spiel-Modus) mit feiner grauer Linie, fängt keine Berührung ab */
#sh,.rip{position:fixed;z-index:60;pointer-events:none;border-radius:50%;background:rgba(255,212,0,.6);box-shadow:0 0 0 1px rgba(0,0,0,.12);-webkit-backdrop-filter:blur(3px);backdrop-filter:blur(3px)}
#sh{width:30px;height:30px;margin:-15px 0 0 -15px;opacity:0;transition:opacity .5s}
#sh.on{opacity:.95;animation:shd 2s ease-in-out infinite}
#sh.u.on{animation-name:shu}#sh.r.on{animation-name:shr}#sh.l.on{animation-name:shl}#sh.b.on{animation-name:shb}
#sh svg{display:block;width:30px;height:30px;fill:none;stroke:#3a3c37;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}
#sh svg *{display:none}
#sh.d .pd,#sh.u .pu,#sh.r .pr,#sh.l .pl,#sh.b.v .pu,#sh.b.v .pd,#sh.b.h .pl,#sh.b.h .pr{display:inline}
#sh.b.v .pu{transform:translateY(-3px)}#sh.b.v .pd{transform:translateY(3px)}#sh.b.h .pl{transform:translateX(-3px)}#sh.b.h .pr{transform:translateX(3px)}
@keyframes shd{0%,100%{transform:translateY(0);opacity:.6}50%{transform:translateY(5px);opacity:1}}
@keyframes shu{0%,100%{transform:translateY(0);opacity:.6}50%{transform:translateY(-5px);opacity:1}}
@keyframes shr{0%,100%{transform:translateX(0);opacity:.6}50%{transform:translateX(5px);opacity:1}}
@keyframes shl{0%,100%{transform:translateX(0);opacity:.6}50%{transform:translateX(-5px);opacity:1}}
@keyframes shb{0%,100%{opacity:.6}50%{opacity:1}}
.rip{width:44px;height:44px;margin:-22px 0 0 -22px;animation:rip .55s ease-out forwards}
@keyframes rip{from{transform:scale(.3);opacity:.95}to{transform:scale(1.15);opacity:0}}
@media (prefers-reduced-motion:reduce){#sh.on{animation:none}.rip{animation-duration:.01s}}
</style>
'''
JS = '''<script id="scrollhint-js">(function(){
var app=document.querySelector(".app")||document.body,KEY="doch-sh",done=0,cur=null,last=0,idle=0,moved=0,startPos=0;
try{done=+localStorage.getItem(KEY)||0}catch(e){}
var sh=document.createElement("div");sh.id="sh";
sh.innerHTML='<svg viewBox="0 0 30 30"><polyline class="pd" points="10,12.5 15,17.5 20,12.5"/><polyline class="pu" points="10,17.5 15,12.5 20,17.5"/><polyline class="pr" points="12.5,10 17.5,15 12.5,20"/><polyline class="pl" points="17.5,10 12.5,15 17.5,20"/></svg>';
document.body.appendChild(sh);
/* Tipp-Welle */
addEventListener("pointerdown",function(e){var r=document.createElement("div");r.className="rip";r.style.left=e.clientX+"px";r.style.top=e.clientY+"px";document.body.appendChild(r);setTimeout(function(){r.remove()},650);},true);
/* grösstes sichtbares scrollbares Feld (senkrecht bevorzugt, sonst waagrecht) */
function find(){var best=null,ba=0,list=document.querySelectorAll("div,section,main,article,ul"),i,el,r,a,cs,v,h;
 for(i=0;i<list.length;i++){el=list[i];
  v=el.scrollHeight>el.clientHeight+8&&el.clientHeight>150;h=el.scrollWidth>el.clientWidth+8&&el.clientWidth>150&&el.clientHeight>30;
  if(!v&&!h)continue;cs=getComputedStyle(el);
  if(v&&cs.overflowY!=="auto"&&cs.overflowY!=="scroll")v=false;
  if(h&&cs.overflowX!=="auto"&&cs.overflowX!=="scroll")h=false;
  if(!v&&!h)continue;
  r=el.getBoundingClientRect();if(r.width<100||r.height<30||r.bottom<=0||r.top>=innerHeight||r.right<=0||r.left>=innerWidth)continue;
  a=(Math.min(r.bottom,innerHeight)-Math.max(r.top,0))*(Math.min(r.right,innerWidth)-Math.max(r.left,0));if(v)a*=2;
  if(a>ba){ba=a;best={el:el,v:v,r:r}}}
 return best;}
function blocked(){var a=document.activeElement,m=app.dataset?app.dataset.mode:"";
 return app.classList.contains("kbo")||m==="game"||(a&&/^(INPUT|TEXTAREA)$/.test(a.tagName));}
function upd(){clearTimeout(idle);
 if(done>=8||blocked()){sh.classList.remove("on");return;}
 var f=find();if(!f){sh.classList.remove("on");return;}
 cur=f.el;var r=f.r,pos=f.v?cur.scrollTop:cur.scrollLeft,max=f.v?cur.scrollHeight-cur.clientHeight:cur.scrollWidth-cur.clientWidth,
  more=pos<max-8,less=pos>8,cls;
 if(!more&&!less){sh.classList.remove("on");return;}
 cls=(more&&less)?"b "+(f.v?"v":"h"):(more?(f.v?"d":"r"):(f.v?"u":"l"));
 sh.className=cls;
 var R=Math.min(r.right,innerWidth),B=Math.min(r.bottom,innerHeight),L=Math.max(r.left,0),T=Math.max(r.top,0);
 if(f.v){sh.style.left=((L+R)/2)+"px";sh.style.top=(B-30)+"px";}
 else{sh.style.top=((T+B)/2)+"px";sh.style.left=(more?R-28:L+28)+"px";}
 var u=document.elementFromPoint(parseFloat(sh.style.left),parseFloat(sh.style.top));if(!u||!(cur.contains(u)||u===cur)){sh.classList.remove("on");return;}
 sh.classList.add("on");}
function later(){clearTimeout(idle);idle=setTimeout(upd,700);}
addEventListener("scroll",function(e){var t=e.target;sh.classList.remove("on");
 if(t&&t.nodeType===1){var p=Math.max(t.scrollTop,t.scrollLeft);if(t!==cur){cur=t;startPos=p;moved=0}moved=Math.max(moved,Math.abs(p-startPos));}
 clearTimeout(last);last=setTimeout(function(){if(moved>60){done++;try{localStorage.setItem(KEY,done)}catch(e){}}moved=0;if(cur)startPos=Math.max(cur.scrollTop,cur.scrollLeft);},800);
 later();},true);
addEventListener("resize",later);addEventListener("focusout",later);addEventListener("focusin",upd);
new MutationObserver(later).observe(app,{attributes:true,subtree:true,childList:true,attributeFilter:["data-mode","class","hidden"]});
setInterval(function(){if(!sh.classList.contains("on"))upd()},2500);setTimeout(upd,800);
})();</script>
'''
a = '<script id="info-link-js">'
assert s.count(a) == 1
s = s.replace(a, CSS + JS + a)
open('hint.html', 'w', encoding='utf-8').write(s)
print('hint.html geschrieben')
