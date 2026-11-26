# DOCH! 26.11.2026: Tests-Liste (Lueckentext / Text pruefen / Einstellungen) wie die Grammatik-Gruppen: graue Kreise 30 px mit Nummer,
# Titel 19,5 px fett, Untertext 14 px, Zeilen grau/weiss/grau, Abstand zu Hilfsmittel 28 px. Einstellungen behaelt das Zahnrad. Idempotent.
import re, sys
s = open('index.html', encoding='utf-8').read()
if 'id="tests-zeilen-css"' in s: sys.exit('schon angewendet')
css = ('<style id="tests-zeilen-css">'
       '#p-test .tests.rows2 .tst .no{width:30px;height:30px;display:grid;place-items:center;font-size:12px;font-weight:700}'
       '#p-test .tests.rows2 #goLueck .no,#p-test .tests.rows2 #goWrite .no{background:#777;color:#fff;border-radius:50%}'
       '#p-test .tests.rows2 .tst b{font-size:19.52px}'
       '#p-test .tests.rows2 .tst small{font-size:14px}'
       '#p-test .tests.rows2 #goLueck,#p-test .tests.rows2 #goSet{background:#f4f4f2!important}'
       '#p-test .tests.rows2 #goWrite{background:#fff!important}'
       '#p-test{margin-bottom:28px!important}'
       '#p-test .tests.rows2{margin-top:0!important}#p-test .tests.rows2 #goLueck{border-top:4px solid #fff!important;height:62px!important}'
       '#p-test .tests.rows2 .tst .tl{background:transparent!important}#p-test .tests.rows2{margin-top:4px!important}'
       '</style>')
s = s.rstrip('\n') + '\n' + css + '\n'
if '--noversion' not in sys.argv:
    s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1) + '2026-11-26zq' + m.group(3), s, count=1)
open('index.html', 'w', encoding='utf-8').write(s); print('ok')
