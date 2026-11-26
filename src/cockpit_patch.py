# DOCH! 26.11.2026: Grammatik-Start als "Cockpit": Niveau-Chips, Heute-Karten und Regal (Zeiten/Faelle/Artikel) in EINEM grauen Block,
# darueber und darunter je ein kleiner weisser Streifen (8 px). Idempotent.
import re, sys
s = open('index.html', encoding='utf-8').read()
if 'id="cockpit-css"' in s: sys.exit('schon angewendet')
css = ('<style id="cockpit-css">#p-home{background:#fff!important;gap:8px!important;padding-top:8px!important}'
       '#cockpit{order:1;background:#f4f4f2;display:flex;flex-direction:column;padding:0 0 8px;margin:0}'
       '#p-home #cockpit>.lvsel{margin:0 0 4px!important}#p-home #cockpit>.rcb{margin:0 0 4px!important}#p-home #cockpit>#sehb{margin:0!important}'
       '#cockpit .rcb:not(:has(button:not([hidden]))){display:none}</style>')
js = ('<script id="cockpit-js">(function(){var h=document.getElementById("p-home");if(!h)return;var l=h.querySelector(".lvsel"),r=h.querySelector(".rcb"),e=document.getElementById("sehb");'
      'if(!l||!r||!e||document.getElementById("cockpit"))return;var c=document.createElement("div");c.id="cockpit";h.insertBefore(c,h.firstChild);c.appendChild(l);c.appendChild(r);c.appendChild(e);})();</script>')
s = s.replace('</head>', css + '</head>', 1)
s = s.rstrip('\n') + '\n' + js + '\n'
if '--noversion' not in sys.argv:
    s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1) + '2026-11-26zi' + m.group(3), s, count=1)
open('index.html', 'w', encoding='utf-8').write(s); print('ok')
