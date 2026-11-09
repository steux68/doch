# Einstellungen-Zahnrad: links, gleiche Hoehe und gleicher Randabstand wie das senkrechte Copyright rechts. Idempotent. 09.11.2026
import re,sys
s=open('index.html',encoding='utf-8').read()
if 'id="cog-left-css"' in s: sys.exit('schon angewendet')
old="cg.style.setProperty('--cogb',(Math.max(60,innerHeight-b+14)+f.offsetWidth+10)+'px');"
assert s.count(old)==1
s=s.replace(old,"var bb=0;[].forEach.call(f.children,function(c){var r=c.getBoundingClientRect();if(r.width>0&&r.height>0&&r.bottom>bb)bb=r.bottom;});cg.style.setProperty('--cogb',Math.max(10,innerHeight-(bb||innerHeight-Math.max(60,innerHeight-b+14)))+'px');",1)
CSS='<style id="cog-left-css">.cogb{right:auto;left:14px;transition:opacity .35s,bottom .65s cubic-bezier(.4,.1,.2,1)}</style>\n'
assert s.count('</head>')==1
s=s.replace('</head>',CSS+'</head>',1)
if '--noversion' not in sys.argv:
    s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-11-09a'+m.group(3),s,count=1)
open('index.html','w',encoding='utf-8').write(s)
