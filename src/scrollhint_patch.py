# Test: Scroll-Hinweis (durchsichtiger Kreis mit Pfeil) + kurze Tipp-Welle. Schreibt NUR hint.html (Testkopie), index.html bleibt unberührt. 19.11.2026
import sys
s = open('index.html', encoding='utf-8').read()
if 'id="scrollhint-css"' in s:
    print('schon vorhanden'); sys.exit(0)
CSS = '''<style id="scrollhint-css">
/* 19.11: Scroll-Hinweis + Tipp-Welle: weiss ca. 55 %, feine graue Linie wie die Pfeile, kein Farbton (rot-grün-sicher), fängt keine Berührung ab */
#sh,.rip{position:fixed;z-index:60;pointer-events:none;border-radius:50%;background:rgba(255,255,255,.55);box-shadow:0 0 0 1px rgba(0,0,0,.1);-webkit-backdrop-filter:blur(3px);backdrop-filter:blur(3px)}
#sh{width:30px;height:30px;margin-left:-15px;opacity:0;transition:opacity .5s}
#sh.on{opacity:.9;animation:shn 2s ease-in-out infinite}
#sh.up.on{animation-name:shu}
#sh svg{display:block;width:30px;height:30px;fill:none;stroke:#555;stroke-width:1.6;stroke-linecap:round;stroke-linejoin:round}
#sh.up svg{transform:rotate(180deg)}
@keyframes shn{0%,100%{transform:translateY(0);opacity:.55}50%{transform:translateY(5px);opacity:.95}}
@keyframes shu{0%,100%{transform:translateY(0);opacity:.55}50%{transform:translateY(-5px);opacity:.95}}
.rip{width:44px;height:44px;margin:-22px 0 0 -22px;animation:rip .5s ease-out forwards}
@keyframes rip{from{transform:scale(.3);opacity:.9}to{transform:scale(1.15);opacity:0}}
@media (prefers-reduced-motion:reduce){#sh.on{animation:none}.rip{animation-duration:.01s}}
</style>
'''
JS = '''<script id="scrollhint-js">(function(){
var app=document.querySelector(".app")||document.body,KEY="doch-sh",done=0,cur=null,last=0,idle=0,moved=0,startTop=0;
try{done=+localStorage.getItem(KEY)||0}catch(e){}
var sh=document.createElement("div");sh.id="sh";sh.innerHTML='<svg viewBox="0 0 30 30"><polyline points="10,12.5 15,17.5 20,12.5"/></svg>';document.body.appendChild(sh);
/* Tipp-Welle */
addEventListener("pointerdown",function(e){var r=document.createElement("div");r.className="rip";r.style.left=e.clientX+"px";r.style.top=e.clientY+"px";document.body.appendChild(r);setTimeout(function(){r.remove()},600);},true);
/* scrollbares Feld finden: das grösste sichtbare */
function find(){var best=null,ba=0,list=document.querySelectorAll("div,section,main,article"),i,el,r,a;
 for(i=0;i<list.length;i++){el=list[i];if(el.scrollHeight<=el.clientHeight+8||el.clientHeight<150)continue;
  var o=getComputedStyle(el).overflowY;if(o!=="auto"&&o!=="scroll")continue;
  r=el.getBoundingClientRect();if(r.width<100||r.bottom<=0||r.top>=innerHeight)continue;
  a=Math.min(r.bottom,innerHeight)-Math.max(r.top,0);a*=r.width;if(a>ba){ba=a;best=el}}
 return best;}
function blocked(){var a=document.activeElement,m=app.dataset?app.dataset.mode:"";
 return app.classList.contains("kbo")||m==="game"||(a&&/^(INPUT|TEXTAREA)$/.test(a.tagName));}
function upd(){clearTimeout(idle);
 if(done>=4||blocked()){sh.classList.remove("on");return;}
 cur=find();if(!cur){sh.classList.remove("on");return;}
 var r=cur.getBoundingClientRect(),st=cur.scrollTop,max=cur.scrollHeight-cur.clientHeight,down=st<max-8;
 if(!down&&st<8){sh.classList.remove("on");return;}
 sh.classList.toggle("up",!down);
 sh.style.left=(r.left+r.width/2)+"px";sh.style.top=(Math.min(r.bottom,innerHeight)-44)+"px";
 sh.classList.add("on");}
function later(){clearTimeout(idle);idle=setTimeout(upd,700);}
addEventListener("scroll",function(e){var t=e.target;sh.classList.remove("on");
 if(t&&t.nodeType===1){if(t!==cur){cur=t;startTop=t.scrollTop;moved=0}moved=Math.max(moved,Math.abs(t.scrollTop-startTop));}
 clearTimeout(last);last=setTimeout(function(){if(moved>60){done++;try{localStorage.setItem(KEY,done)}catch(e){}}moved=0;if(cur)startTop=cur.scrollTop;},800);
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
