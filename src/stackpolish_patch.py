# 18.11.2026: Balken-Feinschliff - Text der Balken buendig mit dem Seitentext, Abschnitte alle hellgrau mit weisser Luecke dazwischen,
# Einrasten (scroll-snap) am Balken, Gross-Schreibung der Balken. Idempotent. Mit --preview wird stack2.html statt index.html geschrieben.
import re, sys
s = open('index.html', encoding='utf-8').read()
if 'id="stackpolish-css"' in s:
    print('schon vorhanden'); sys.exit(0)
css = '''<style id="stackpolish-css">
/* 1. Balkentext buendig mit dem Seitentext (alles an einer Linie) */
.hb{padding-left:0!important;padding-right:0!important}
.hp .rows div,.hp .hi,.hp .hi:nth-child(odd),.hp .rwi,.hp .qt,.hp .qt.alt{padding-left:0!important;padding-right:0!important}
/* 2. Abschnitte: alle hellgrau, dazwischen eine weisse Luecke */
#p-home,#p-test,#p-links,#p-quotes,#p-rede,#p-hist{background:#f4f4f2!important;margin-bottom:12px!important}
.hp .qt,.hp .qt.alt,.hp .rwi,.hp .rwi:nth-child(odd),.hp .hi,.hp .hi:nth-child(odd){background-color:transparent!important}
/* 3. Einrasten: nach dem Wischen rastet der Abschnitt unter seinem Balken ein */
#hscroll{scroll-snap-type:y proximity!important}
#p-home,#p-test,#p-links,#p-quotes,#p-rede,#p-hist{scroll-snap-align:start}
</style>
</head>'''
assert s.count('</head>') == 1
s = s.replace('</head>', css)
out = 'stack2.html' if '--preview' in sys.argv else 'index.html'
if out == 'stack2.html':
    s = re.sub(r'<title>[^<]*</title>', '<title>DOCH! TEST Feinschliff</title>', s, count=1)
else:
    s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1) + '2026-11-18b' + m.group(3), s, count=1)
open(out, 'w', encoding='utf-8').write(s)
print('ok', out)
