# 18.11.2026: Die App startet wieder auf der Karte (Titelseite): die Titelseite bekommt einen eigenen Einrastpunkt,
# sonst zog das Einrasten (scroll-snap) beim Start zur Grammatik. Zurueck: git revert dieses Commit. Idempotent.
import re, sys
s = open('index.html', encoding='utf-8').read()
if 'id="titlesnap-css"' in s:
    print('schon vorhanden'); sys.exit(0)
assert s.count('</head>') == 1
s = s.replace('</head>', '<style id="titlesnap-css">#p-title{scroll-snap-align:start}</style>\n</head>')
s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1) + '2026-11-18d' + m.group(3), s, count=1)
open('index.html', 'w', encoding='utf-8').write(s)
print('ok')
