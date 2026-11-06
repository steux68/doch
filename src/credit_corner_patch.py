# DOCH!: Urheberhinweis wie bei PASSAGE: auf der Titelseite senkrecht unten rechts, am Seitenende waagrecht (animiert), sonst unsichtbar.
# Ausserdem: Wischen/Scrollen auf der Titelseite oeffnet den ersten Bereich. 06.11.2026.
import re, sys
s = open('index.html', encoding='utf-8').read()
if '/* credit-corner */' in s:
    print('schon angewendet'); sys.exit(0)
CSS = '''
/* credit-corner */
#home:not([hidden]) ~ footer.copy{display:flex!important}
#topic:not([hidden]) ~ footer.copy{display:none!important}
footer.copy{position:fixed;left:auto;top:auto;right:14px;bottom:var(--cb,150px);width:var(--cw,270px);height:24px;z-index:46;border:0;padding:0;margin:0;gap:8px;
 background:none;justify-content:center;align-items:center;white-space:nowrap;transform-origin:100% 100%;transform:translateY(calc(var(--cw,270px) * -1)) rotate(-90deg);opacity:0;pointer-events:none;
 transition:transform .65s cubic-bezier(.4,.1,.2,1),bottom .65s cubic-bezier(.4,.1,.2,1),width .65s,right .65s,opacity .35s}
footer.copy.cv{opacity:1}
footer.copy.ch{opacity:1;right:10px;width:calc(100vw - 20px);bottom:var(--cbh,60px);transform:translateY(0) rotate(0);box-sizing:border-box;height:28px;padding-top:2px;gap:6px;
 border-top:1px dotted #b8b8b8;background:#fff}
footer.copy img{height:20px}footer.copy.ch img{height:13px}
footer.copy span{font-size:12px}footer.copy.ch span{font-size:11px}
#hscroll::after{content:"";display:block;height:36px}
#p-sets footer.copy{display:none!important}
@media (max-height:700px){footer.copy{--cw:240px}footer.copy.cv img{display:none}}
'''
JS = '''<script id="credit-corner-js">(function(){var f=document.querySelector('#home ~ footer.copy'),h=document.getElementById('hscroll'),n=document.getElementById('hnav');if(!f||!h||!n)return;
function title(){return !n.querySelector('[aria-pressed="true"]');}
function upd(){var on=h.offsetParent!==null&&h.getBoundingClientRect().height>0,nt=n.getBoundingClientRect().top,t=title(),
 end=h.scrollTop+h.clientHeight>=h.scrollHeight-6;
 f.style.setProperty('--cb',Math.max(60,innerHeight-nt+14)+'px');f.style.setProperty('--cbh',Math.max(30,innerHeight-nt+2)+'px');
 f.classList.toggle('cv',on&&t);f.classList.toggle('ch',on&&!t&&end);}
upd();h.addEventListener('scroll',upd,{passive:true});addEventListener('resize',upd);setInterval(upd,400);
/* Titelseite: nach oben wischen oder abwaerts scrollen oeffnet den ersten Bereich */
var y0=null;function go(){if(title()&&n.children[0])n.children[0].click();}
document.addEventListener('touchstart',function(e){y0=title()&&h.contains(e.target)?e.touches[0].clientY:null;},{passive:true});
document.addEventListener('touchmove',function(e){if(y0!==null&&y0-e.touches[0].clientY>36){y0=null;go();}},{passive:true});
document.addEventListener('wheel',function(e){if(e.deltaY>20&&h.offsetParent!==null)go();},{passive:true});
})();</script>
'''
i = s.rindex('</style>'); s = s[:i] + CSS + s[i:]
s = s.rstrip() + '\n' + JS
s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1)+'2026-11-06n'+m.group(3), s, count=1)
open('index.html','w',encoding='utf-8').write(s); print('ok')
