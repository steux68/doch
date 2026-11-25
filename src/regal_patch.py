# DOCH! 26.11.2026: Grammatik-Ansicht leiser, aber sichtbar: Zeiten / Faelle / Artikel als EIN seitlich wischbares Regal
# (der naechste Kasten schaut am Rand heraus), Platzhalter "Bald mehr" entfernt, Niveau-Knoepfe ohne graue Flaechen. Idempotent.
import re, sys
s = open('index.html', encoding='utf-8').read()
if 'id="regal-css"' in s: sys.exit('schon angewendet')
css = ('<style id="regal-css">'
 '#sehb{display:flex!important;gap:8px;overflow-x:auto;overflow-y:hidden;scrollbar-width:none;margin-right:-18px!important;padding-right:18px;scroll-snap-type:x proximity;-webkit-overflow-scrolling:touch}'
 '#sehb::-webkit-scrollbar{display:none}'
 '#sehb .sehg{display:contents!important}'
 '#sehb .sehk{flex:0 0 66%;scroll-snap-align:start;background:#f6f6f4}'
 '#sehb .sehk:not([data-sv]):not(#goArtH){display:none!important}'
 '#sehb .sehk::after{display:none}'
 '#sehb .sehk i{height:28px}'
 '.lvsel .lvb{min-height:30px!important;background:transparent!important}'
 '.lvsel .lvb[aria-pressed="true"],.lvsel .lvb.on,.lvsel .lvb.act{background:#cdff3e!important}'
 '</style>')
assert '</head>' in s
s = s.replace('</head>', css + '</head>', 1)
if '--noversion' not in sys.argv:
    s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1) + '2026-11-26t' + m.group(3), s, count=1)
open('index.html', 'w', encoding='utf-8').write(s)
print('ok')
