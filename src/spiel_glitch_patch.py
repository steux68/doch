# DOCH! 25.11.2026: Spiel-Ansicht: Legende mit Abstand, Mikrofon-Hinweis einzeilig (kein Ueberlappen). Idempotent.
import re, sys
s = open('index.html', encoding='utf-8').read()
if 'id="spiel-glitch-css"' in s: sys.exit('schon angewendet')
a = 'Sprechen: ins Feld tippen und das Mikrofon der Tastatur nutzen.'
assert s.count(a) == 1
s = s.replace(a, 'Sprechen: Mikrofon der Tastatur nutzen.')
css = '<style id="spiel-glitch-css">.app[data-mode="game"] #lg{display:flex;justify-content:center;gap:4px 12px;flex-wrap:wrap;white-space:normal}.app[data-mode="game"] #lg span{display:inline-flex;align-items:center;gap:4px}</style>'
i = s.rindex('</head>'); s = s[:i] + css + s[i:]
if '--noversion' not in sys.argv:
    s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1)+'2026-11-25g'+m.group(3), s, count=1)
open('index.html', 'w', encoding='utf-8').write(s); print('ok')
