# DOCH! 26.11.2026: Tests: Abstand unter Bereich/Start-Knopf auf 8 px (wie im Cockpit der Grammatik). Idempotent.
import re, sys
s = open('index.html', encoding='utf-8').read()
if 'id="test-unten-css"' in s: sys.exit('schon angewendet')
css = '<style id="test-unten-css">#p-test .bk{margin-bottom:0!important}#p-test .tc.tpg,#p-test .tpg{padding-bottom:8px!important}</style>'
s = s.rstrip('\n') + '\n' + css + '\n'
if '--noversion' not in sys.argv:
    s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1) + '2026-11-26zo' + m.group(3), s, count=1)
open('index.html', 'w', encoding='utf-8').write(s); print('ok')
