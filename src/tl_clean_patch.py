# Geschichte-Popup: Bild ohne grauen Kasten/Rahmen, keine Strichlinie ueber der Jahresleiste. 06.11.2026.
import re, sys
s = open('index.html', encoding='utf-8').read()
if '/* tl-clean */' in s:
    print('schon angewendet'); sys.exit(0)
CSS = '\n/* tl-clean */\n.tlpop .gfig{background:#fff!important;outline:0!important}\n.tlpop .tls{border-top:0!important}\n'
i = s.rindex('</style>'); s = s[:i] + CSS + s[i:]
s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1)+'2026-11-06f'+m.group(3), s, count=1)
open('index.html','w',encoding='utf-8').write(s); print('ok')
