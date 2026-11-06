# 06.11.2026: Der wandernde Reiter bleibt gelb, bis er oben angekommen ist; erst dann uebernimmt der naechste (vorher sprang Gelb bei Materialien/Links zu frueh weiter). Idempotent.
import re,sys
s=open('index.html',encoding='utf-8').read()
old="BARS.forEach((b,k)=>{if(isUp(b))c=k;});"
new="for(let k=0;k<BARS.length;k++){const b=BARS[k];if(!isUp(b))continue;c=k;if(b.getBoundingClientRect().top>SC.getBoundingClientRect().top+parseFloat(b.style.top)+2)break;}"
if new not in s:
    assert s.count(old)==1
    s=s.replace(old,new)
if '--noversion' not in sys.argv:
    s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-11-06a'+m.group(3),s,count=1)
open('index.html','w',encoding='utf-8').write(s)
