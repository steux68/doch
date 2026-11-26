# DOCH! 26.11.2026 (Nacht): (1) leere "Bald mehr"-Kachel im Regal entfernt (Sackgasse), (2) Lernen: Knopf "Jetzt du: Spiel starten" unter der Karte,
# im Stil der Chips (grau, 44 px hoch, Pfeil rechts). Nur im Modus "learn" sichtbar. Idempotent.
import re, sys
s = open('index.html', encoding='utf-8').read()
if 'id="goGame-css"' in s: sys.exit('schon angewendet')
tile = re.search(r'<div class="sehk" id="phH"[^>]*>.*?</div>', s, re.S)
assert tile and 'Bald mehr' in tile.group(0)
s = s.replace(tile.group(0), '', 1)
css = ('<style id="goGame-css">#goGame{display:none}'
       '.app[data-mode="learn"] #goGame{display:flex;align-items:center;justify-content:space-between;flex:none;box-sizing:border-box;width:100%;margin:14px 0 10px;height:44px;min-height:44px;padding:0 14px;border:0;border-radius:0;background:#ececea;color:#1a1a1a;font:inherit;font-size:14px;cursor:pointer;-webkit-tap-highlight-color:transparent}'
       '.app[data-mode="learn"] #goGame b{font-weight:700}.app[data-mode="learn"] #goGame:active{background:#cdff3e}'
       '</style>')
s = s.replace('</head>', css + '</head>', 1)
js = ('<script id="goGame-js">(function(){var g=document.getElementById("gqpop")||document.getElementById("lg");if(!g||!g.parentNode)return;var b=document.createElement("button");b.type="button";b.id="goGame";'
      'b.innerHTML=\'<b>Jetzt du: Spiel starten</b><span aria-hidden="true">\\u2192</span>\';g.parentNode.insertBefore(b,g.nextSibling);b.addEventListener("click",function(){if(typeof setMode==="function")setMode("game");});})();</script>')
s = s.rstrip('\n') + '\n' + js + '\n'
if '--noversion' not in sys.argv:
    s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1) + '2026-11-26zh' + m.group(3), s, count=1)
open('index.html', 'w', encoding='utf-8').write(s); print('ok')
