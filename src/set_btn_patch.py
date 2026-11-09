# Tests-Seite: Zeile "Einstellungen" (öffnet dasselbe Pop-up wie das Zahnrad). Idempotent. 09.11.2026
import re,sys
s=open('index.html',encoding='utf-8').read()
if 'id="goSet"' in s: sys.exit('schon angewendet')
old="mit LanguageTool</small></button></div></div>';"
assert s.count(old)==1
new=("mit LanguageTool</small></button>'+"
 "'<button class=\"tst wide\" id=\"goSet\"><b>Einstellungen</b><small>Timer · Artikel-Hilfe · neueste Version</small></button></div></div>';")
s=s.replace(old,new,1)
old2='$("goWrite").onclick=()=>openTopic("write");'
assert s.count(old2)==1
s=s.replace(old2,old2+'$("goSet").onclick=()=>{const c=$("cogb");if(c)c.click();};',1)
if '--noversion' not in sys.argv:
    s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-11-09b'+m.group(3),s,count=1)
open('index.html','w',encoding='utf-8').write(s)
