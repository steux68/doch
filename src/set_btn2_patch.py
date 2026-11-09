# Einstellungen: Zahnrad in der Tests-Zeile, vertikales Zahnrad auf der Titelseite entfernt (Zeile öffnet über das versteckte Zahnrad). Idempotent. 09.11.2026
import re,sys
s=open('index.html',encoding='utf-8').read()
if 'id="set-btn2-css"' in s: sys.exit('schon angewendet')
old='<b>Einstellungen</b><small>Timer'
assert s.count(old)==1
cog='<svg viewBox="-12 -12 24 24" width="24" height="24" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round" d="M-1.9-9.2h3.8l.6 2.5 1.6.7 2.2-1.4 2.7 2.7-1.4 2.2.7 1.6 2.5.6v3.8l-2.5.6-.7 1.6 1.4 2.2-2.7 2.7-2.2-1.4-1.6.7-.6 2.5h-3.8l-.6-2.5-1.6-.7-2.2 1.4-2.7-2.7 1.4-2.2-.7-1.6-2.5-.6v-3.8l2.5-.6.7-1.6-1.4-2.2 2.7-2.7 2.2 1.4 1.6-.7z"/><circle r="3.2" fill="none" stroke="currentColor" stroke-width="1.6"/></svg>'
s=s.replace(old,'<b class="setb">'+cog+'Einstellungen</b><small>Timer',1)
CSS='<style id="set-btn2-css">.cogb{display:none!important}#goSet .setb{display:inline-flex;align-items:center;gap:10px}#goSet .setb svg{flex:none}</style>\n'
i=s.rindex('</style>')+len('</style>')
s=s[:i]+'\n'+CSS+s[i:]
if '--noversion' not in sys.argv:
    s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-11-09c'+m.group(3),s,count=1)
open('index.html','w',encoding='utf-8').write(s)
