# Geschichte (letzter Reiter) dockt oben an: Platz unter der letzten Seite, falls sie zu kurz zum Hochscrollen ist. Idempotent. 09.11.2026
import re,sys
s=open('index.html',encoding='utf-8').read()
if 'tailDock' in s: sys.exit('schon angewendet')
old="const secTop=i=>Math.max(0,PAGES[i].offsetTop-((i>>1)*HB+22));"
assert s.count(old)==1
new=old+("\nfunction tailDock(){const e=PAGES[PAGES.length-1];if(!e)return;e.style.marginBottom='';const need=secTop(PAGES.length-1)-(SC.scrollHeight-SC.clientHeight);if(need>0)e.style.marginBottom=Math.ceil(need)+'px';}\n"
 "window.addEventListener('resize',tailDock);window.addEventListener('load',tailDock);[300,1200,3000].forEach(ms=>setTimeout(tailDock,ms));if(window.ResizeObserver){try{new ResizeObserver(tailDock).observe(PAGES[PAGES.length-1]);}catch(_){}}tailDock();")
s=s.replace(old,new,1)
if '--noversion' not in sys.argv:
    s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-11-09d'+m.group(3),s,count=1)
open('index.html','w',encoding='utf-8').write(s)
