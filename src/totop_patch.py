# DOCH!: leere Scroll-Leiste weg, kleiner Chevron unten rechts zurueck nach oben. 06.11.2026.
import re, sys
s=open('index.html',encoding='utf-8').read()
if '/* totop */' in s: print('schon angewendet'); sys.exit(0)
CSS='''
/* totop */
#abar{display:none!important}
#toTop{position:fixed;right:10px;bottom:calc(10px + env(safe-area-inset-bottom,0px));z-index:40;width:34px;height:34px;padding:0;display:flex;align-items:center;justify-content:center;
 background:rgba(255,255,255,.94);border:1px dotted #b8b8b8;border-radius:0;opacity:0;pointer-events:none;transition:opacity .25s;-webkit-tap-highlight-color:transparent}
#toTop.on{opacity:1;pointer-events:auto}
#toTop svg{width:20px;height:20px;fill:none;stroke:#3a3c37;stroke-width:1.6;stroke-linecap:round;stroke-linejoin:round}
'''
JS='''<button type="button" id="toTop" aria-label="nach oben"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 15L12 8L19 15"/></svg></button><script id="totop-js">(function(){var b=document.getElementById('toTop'),h=document.getElementById('hscroll');if(!b||!h)return;
function vis(){return h.offsetParent!==null&&h.getBoundingClientRect().height>0;}
function upd(){var y=innerHeight-10;[].forEach.call(h.querySelectorAll('.hb'),function(x){var r=x.getBoundingClientRect();if(r.top>innerHeight*.5&&r.top<y)y=r.top;});b.style.bottom=Math.max(10,innerHeight-y+8)+'px';b.classList.toggle('on',vis()&&h.scrollTop>260);}
b.onclick=function(){h.scrollTo({top:0,behavior:'smooth'});};h.addEventListener('scroll',upd,{passive:true});addEventListener('resize',upd);setInterval(upd,500);upd();})();</script>'''
i=s.rindex('</style>'); s=s[:i]+CSS+s[i:]
s=s.rstrip('\n')+'\n'+JS+'\n'
s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-11-06i'+m.group(3),s,count=1)
open('index.html','w',encoding='utf-8').write(s); print('ok')
