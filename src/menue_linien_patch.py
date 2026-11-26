# DOCH! 26.11.2026: Menuebalken ohne gepunktete Trennlinien (Farbkontrast genuegt). Idempotent.
import re, sys
s = open('index.html', encoding='utf-8').read()
if 'id="menue-linien-css"' in s: sys.exit('schon angewendet')
css = ('<style id="menue-linien-css">html body #hscroll>.hb.hb[data-i]{background-image:none!important}'
       '#hscroll>.hb.hb[data-i="0"]{margin-bottom:-1px!important}'
       ''
       '#hscroll>.hb.hb[data-i="0"]{margin-top:14px!important}'
       'html body #hscroll>.hb.hb[data-i]::before,html body #hscroll>.hb.hb[data-i]::after{display:none!important}</style>')
s = s.rstrip('\n') + '\n' + css + '\n'
if '--noversion' not in sys.argv:
    s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1) + '2026-11-26zr' + m.group(3), s, count=1)
open('index.html', 'w', encoding='utf-8').write(s); print('ok')
