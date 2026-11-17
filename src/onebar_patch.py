# Mock-up A "One bar": im Lernen-Modus EINE Leiste unten (‹ Zähler › + die bisherigen Knöpfe Anhören / Zum Spiel);
# Pfeile oben, doppelte Zähler, alte Knopfreihe und der Kompass-Balken entfallen (nur data-mode="learn"). Idempotent. 17.11.2026
import re, sys
s = open('index.html', encoding='utf-8').read()
if 'id="onebar-css"' in s:
    print('schon vorhanden'); sys.exit(0)
CSS = '''<style id="onebar-css">
.app[data-mode="learn"] #lg:not(:has(button)){display:none}
.app[data-mode="learn"] .tlar{display:none!important}
.app[data-mode="learn"] #panel .card .top .count,.app[data-mode="learn"] #panel #pcn{display:none!important}
.app[data-mode="learn"] #panel .btns,.app[data-mode="learn"] #tabar{display:none!important}
#obar{display:none}
.app[data-mode="learn"] #obar{display:flex;flex:none;position:relative;margin:0 0 6px;background:#fff}
#obar>*{position:relative;flex:1 1 0;min-width:0;height:44px;display:flex;align-items:center;justify-content:center;border:0;background:none;padding:0 4px;font:inherit;font-size:13px;letter-spacing:.04em;color:inherit;white-space:nowrap}
#obar>*::after{content:"";position:absolute;inset:0;pointer-events:none;z-index:3;background:var(--df) left top/100% 1px no-repeat,var(--dfv) right top/1px 100% no-repeat}
#obar>*:last-child::after{background:var(--df) left top/100% 1px no-repeat}
#obar .ob-a{flex:0 0 44px;font-size:20px}
#obar .ob-n{flex:0 0 56px;color:#555;font-variant-numeric:tabular-nums}
#obar .ob-n b{font-weight:700;color:#3a3c37}
#obar .go{background:var(--lime,#cdff3e);font-weight:700}
#obar button:disabled{opacity:.35}
</style>
'''
JS = '''<script id="onebar-js">(function(){const $=id=>document.getElementById(id),app=document.querySelector(".app");if(!app||!$("tabar"))return;
const bar=document.createElement("div");bar.id="obar";$("tabar").parentNode.insertBefore(bar,$("tabar"));
function cell(c,h,fn,d){const b=document.createElement("button");b.type="button";b.className=c;b.innerHTML=h;b.disabled=!!d;b.onclick=fn;return b;}
let t=0;function build(){t=0;bar.innerHTML="";if(app.dataset.mode!=="learn")return;
 const z=$("bZ"),w=$("bW"),c=$("ct"),m=/(\\d+)\\s*\\/\\s*(\\d+)/.exec(c?c.textContent:"");
 if(z)bar.appendChild(cell("ob-a","\\u2039",()=>z.click(),z.disabled));
 if(m){const n=document.createElement("div");n.className="ob-n";n.innerHTML="<b>"+("0"+m[1]).slice(-2)+"</b>\\u2009/\\u2009"+m[2];bar.appendChild(n);}
 if(w)bar.appendChild(cell("ob-a","\\u203a",()=>w.click(),w.disabled));
 [].forEach.call($("btns2").querySelectorAll("button"),x=>bar.appendChild(cell("ob-t"+(/Spiel/.test(x.textContent)?" go":""),x.textContent,()=>x.click(),x.disabled)));}
function q(){if(!t)t=setTimeout(build,0);}
const mo=new MutationObserver(q);[$("btns1"),$("btns2"),$("ct")].forEach(e=>e&&mo.observe(e,{childList:true,subtree:true,characterData:true,attributes:true}));
mo.observe(app,{attributes:true,attributeFilter:["data-mode"]});build();})();</script>
'''
a = '<script id="info-link-js">'
assert s.count(a) == 1
s = s.replace(a, CSS + JS + a)
if '--noversion' not in sys.argv:
    s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1) + '2026-11-17e' + m.group(3), s, count=1)
open('index.html', 'w', encoding='utf-8').write(s)
print('ok')
