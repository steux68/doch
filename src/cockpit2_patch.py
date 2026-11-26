# DOCH! 26.11.2026: Cockpit verfeinert: weisse 4-px-Fugen zwischen Niveau, Karten und Regal sowie zwischen Zeiten und Faelle;
# Regal-Kacheln grau (#f4f4f2) mit weniger Innenabstand. Idempotent.
import re, sys
s = open('index.html', encoding='utf-8').read()
if 'id="cockpit2-css"' in s: sys.exit('schon angewendet')
css = ('<style id="cockpit2-css">'
       '#p-home #cockpit{background:#fff!important;padding:0!important}'
       '#p-home #cockpit>.lvsel{background:#f4f4f2;margin:0 0 4px!important}'
       '#p-home #cockpit>.rcb{margin:0 0 4px!important}'
       '#p-home #cockpit>#sehb{padding:0 18px 0 0!important}'
       '#cockpit .sehg{gap:4px!important}'
       '#cockpit .sehk{background:#f4f4f2!important;padding:6px 8px 8px!important}'
       '#cockpit .sehk b{margin-bottom:4px!important;line-height:1.2}'
       '</style>')
s = s.rstrip('\n') + '\n' + css + '\n'
if '--noversion' not in sys.argv:
    s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1) + '2026-11-26zj' + m.group(3), s, count=1)
open('index.html', 'w', encoding='utf-8').write(s); print('ok')
