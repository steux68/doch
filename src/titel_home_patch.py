# DOCH! 25.11.2026: in jedem Thema (alle 42) fuehrt ein Tipp auf die Titelleiste (Titel oder freie Flaeche) wie "Start" nach Hause.
# Vorher reagierte nur der kleine "Start"-Knopf. Idempotent.
import re, sys
s = open('index.html', encoding='utf-8').read()
if 'id="titel-home-js"' in s: sys.exit('schon angewendet')
css = '<style id="titel-home-css">#topic .titlebar{cursor:pointer;-webkit-tap-highlight-color:transparent}#topic .titlebar #ttl{padding:8px 0}</style>'
js = ('<script id="titel-home-js">(function(){var bar=document.querySelector("#topic .titlebar"),back=document.getElementById("back");'
      'if(!bar||!back)return;bar.addEventListener("click",function(e){if(e.target.closest("#back"))return;back.click();});'
      'var t=document.getElementById("ttl");if(t){t.setAttribute("role","button");t.setAttribute("aria-label","Zurück zum Start");}})();</script>')
assert s.count('</head>') >= 1
s = s.replace('</head>', css + '</head>', 1)
s = s.rstrip('\n') + '\n' + js + '\n'  # die Datei endet ohne </body>; Skript ans Ende
if '--noversion' not in sys.argv:
    s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1) + '2026-11-26o' + m.group(3), s, count=1)
open('index.html', 'w', encoding='utf-8').write(s)
print('ok')
