# DOCH! 26.11.2026: (1) Cockpit-Reihenfolge: Heute-Karten (Entdecken / Fehler wiederholen) oben, dann Niveau-Chips, dann Regal.
# (2) Gruppenkoepfe (Satz, Nomen & Faelle ...): Fortschritt wie bei den Themen: gepunktete Linie, roter Punkt, Prozent. Idempotent.
import re, sys
s = open('index.html', encoding='utf-8').read()
if 'id="cockpit3-css"' in s: sys.exit('schon angewendet')
css = ('<style id="cockpit3-css">'
       '#p-home #cockpit>.rcb{order:1}#p-home #cockpit>.lvsel{order:2}#p-home #cockpit>#sehb{order:3}'
       '.grp .grh .prog{position:relative;height:1px!important;background:repeating-linear-gradient(to right,#b8b8b8 0 1px,transparent 1px 3px)!important;overflow:visible}'
       '.grp .grh .prog i{position:absolute;left:0;top:0;height:0!important;background:none!important;max-width:100%}'
       '.grp .grh .prog i::after{content:"";position:absolute;right:-4px;top:-4px;width:8px;height:8px;border-radius:50%;background:#e30613}'
       '.grp .grh .prog[data-pct]::before{content:attr(data-pct);position:absolute;right:0;bottom:6px;font-size:12px;line-height:1;color:#333}'
       '</style>')
js = ('<script id="cockpit3-js">(function(){if(typeof renderHome!=="function")return;var r=renderHome;'
      'function pc(){try{document.querySelectorAll(".grp .grh .prog").forEach(function(p){var i=p.querySelector("i"),w=i?parseFloat(i.style.width)||0:0;'
      'if(w>0)p.setAttribute("data-pct",Math.round(w)+" %");else p.removeAttribute("data-pct");});}catch(e){}}'
      'renderHome=function(){var x=r.apply(this,arguments);pc();return x;};pc();})();</script>')
s = s.replace('</head>', '', 1)
s = s.rstrip('\n') + '\n' + css + '\n' + js + '\n'
if '--noversion' not in sys.argv:
    s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1) + '2026-11-26zm' + m.group(3), s, count=1)
open('index.html', 'w', encoding='utf-8').write(s); print('ok')
