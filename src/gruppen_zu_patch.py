# DOCH! 26.11.2026: Grammatik-Gruppen starten alle geschlossen (kein automatisch offenes "Satz"); geschlossene Gruppen im Wechsel grau/weiss (1 grau, 2 weiss, 3 grau ...). Idempotent.
import re, sys
s = open('index.html', encoding='utf-8').read()
if 'id="gruppen-zu-css"' in s: sys.exit('schon angewendet')
css = ('<style id="gruppen-zu-css">#home .grp:not(.open):nth-child(odd){background:#f4f4f2!important}'
       '#home .grp:not(.open):nth-child(even){background:#fff!important}</style>')
js = ('<script id="gruppen-zu-js">(function(){try{if(typeof store!=="undefined"&&typeof renderHome==="function"){store.grp=-1;if(typeof save==="function")save();renderHome();}}catch(e){}})();</script>')
s = s.rstrip('\n') + '\n' + css + '\n' + js + '\n'
if '--noversion' not in sys.argv:
    s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1) + '2026-11-26zn' + m.group(3), s, count=1)
open('index.html', 'w', encoding='utf-8').write(s); print('ok')
