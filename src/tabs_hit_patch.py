# 25.11.2026: Reiter Lernen | Spiel | Theorie hatten nur ca. 23 px tippbare Hoehe, weil overflow:hidden die unsichtbare 44-px-Flaeche (.hitx::after) abschnitt.
# Jetzt overflow:visible + Flaeche bis ca. 44 px; sichtbar aendert sich nichts. Nur CSS. Idempotent.
import re, sys
s = open('index.html', encoding='utf-8').read()
if 'id="tabs-hit-css"' in s: sys.exit('schon angewendet')
css = ('<style id="tabs-hit-css">#seg button.hitx,.seg button.hitx{overflow:visible!important}'
       '#seg button.hitx::after,.seg button.hitx::after{left:0!important;right:0!important;height:44px!important}'
       '#infoLink.ilink{position:relative}#infoLink.ilink::after{content:\"\";position:absolute;left:-14px;right:-14px;top:-6px;bottom:-6px}</style>')
s = s.replace('</head>', css + '</head>', 1) if '</head>' in s else s
if '--noversion' not in sys.argv:
    s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1) + '2026-11-26q' + m.group(3), s, count=1)
open('index.html', 'w', encoding='utf-8').write(s)
print('ok')
