# Navigation: sechs Reiter als graues 3x2-Band unter dem Logo, immer sichtbar; Antippen zeigt nur diesen Bereich
# (statt Stapel aus Leisten, die ueber den Text scrollen). Aktiv = gelb. Logo/Start = Kartenbild. 06.11.2026.
import re, sys
s = open('index.html', encoding='utf-8').read()
if 'id="tabs-js"' in s:
    print('schon angewendet'); sys.exit(0)
CSS = '''
/* tabs-nav */
#hscroll>.hb,.sback,#scrD{display:none!important}
#hnav{display:grid;grid-template-columns:1fr 1fr 1fr;gap:1px;margin:6px 0 0;padding:0;background:#fff;flex:none}
#hnav .hnb{appearance:none;border:0;border-radius:0;background:#efefef;color:#333;font:400 14px/1.2 inherit;font-family:inherit;padding:10px 4px;text-align:center;cursor:pointer;-webkit-tap-highlight-color:transparent}
#hnav .hnb[aria-pressed="true"]{background:#ffec99;color:#111;font-weight:700}
#hscroll>section.tabhide,#hscroll>.mrow.tabhide{display:none!important}
#hscroll>section.hp{min-height:0!important}
'''
JS = '''<script id="tabs-js">(function(){
var SC=document.getElementById("hscroll"),HB=document.getElementById("hbody");if(!SC||!HB||typeof SECS==="undefined")return;
var nav=document.createElement("div");nav.id="hnav";nav.setAttribute("role","tablist");HB.insertBefore(nav,SC);
var cur=-1;
function sec(k){return document.getElementById("p-"+k);}
function show(i){cur=i;
 [].forEach.call(SC.children,function(e){if(e.classList.contains("hb"))return;e.classList.add("tabhide");});
 var el=i<0?document.getElementById("p-title"):sec(SECS[i][0]);if(el){el.classList.remove("tabhide");
  if(i>=0){var n=el.nextElementSibling;if(n&&n.classList.contains("mrow"))n.classList.remove("tabhide");}}
 [].forEach.call(nav.children,function(b,k){b.setAttribute("aria-pressed",k===i?"true":"false");});
 SC.scrollTop=0;if(i<0&&typeof enterMap==="function"){try{enterMap();}catch(e){}}}
SECS.forEach(function(r,i){var b=document.createElement("button");b.type="button";b.className="hnb";b.textContent=r[1];b.setAttribute("role","tab");b.onclick=function(){show(i);};nav.appendChild(b);});
window.tapGo=function(el,i){show(i);};
window.toTitle=function(){show(-1);};
show(-1);
var lg=document.querySelector("h1.logo");if(lg)lg.addEventListener("click",function(){show(-1);});
})();</script>
'''
i = s.rindex('</style>'); s = s[:i] + CSS + s[i:]
s = s.rstrip() + '\n' + JS
s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1)+'2026-11-06g'+m.group(3), s, count=1)
open('index.html','w',encoding='utf-8').write(s); print('ok')
