# DOCH! 26.11.2026: Schalter learn | wonder: 14 px statt 12 px und dunkleres Grau fuer den ausgeschalteten Teil (5,3:1 statt 3,5:1). Idempotent.
import re, sys
s = open('index.html', encoding='utf-8').read()
if 'id="lesbar-css"' in s: sys.exit('schon angewendet')
css = '<style id="lesbar-css">#dsw4{font-size:14px;color:#6b6b67}#dsw4[data-m="d"] .t1,#dsw4[data-m="s"] .t2{color:#222}</style>'
s = s.replace('</head>', css + '</head>', 1)
if '--noversion' not in sys.argv:
    s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1) + '2026-11-26zf' + m.group(3), s, count=1)
open('index.html', 'w', encoding='utf-8').write(s); print('ok')
