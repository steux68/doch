# DOCH! 26.11.2026: Titelband einheitlich (58 px hoch, Logo 42 px hoch mit Luft, Schalter learn|wonder wie in Passage/dasein-design: Pille 28x15, mittig). Idempotent.
import re, sys
s = open('index.html', encoding='utf-8').read()
if 'id="header-einheit-css"' in s: sys.exit('schon angewendet')
css = ('<style id="header-einheit-css">.titlebar{height:58px!important;box-sizing:border-box!important;padding-top:0!important;padding-bottom:0!important}'
       '.titlebar .logo svg{height:42px!important;width:auto!important}.titlebar .logo{height:42px!important;width:auto!important}'
       '#dsw4 .pill{width:28px!important;height:15px!important}#dsw4 .pill .knob,#dsw4 .knob{width:9px!important;height:9px!important}#dsw4{gap:4px!important}#dsw4 .t2{color:#555!important}#dsw4{min-width:104px!important;justify-content:flex-end}</style>')
s = s.rstrip('\n') + '\n' + css + '\n'
if '--noversion' not in sys.argv:
    s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1) + '2026-11-26zs' + m.group(3), s, count=1)
open('index.html', 'w', encoding='utf-8').write(s); print('ok')
