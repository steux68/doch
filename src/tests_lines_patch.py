# Tests: duenne Linie zwischen A1 bis C1 (Zellen), Gemischt in der Aktiv-Gelb, Fragetext (rot) kleiner. 06.11.2026.
import re, sys
s = open('index.html', encoding='utf-8').read()
if '/* tests-lines */' in s:
    print('schon angewendet'); sys.exit(0)
CSS = '''
/* tests-lines */
.tests{gap:1px!important;background:#cfcfcf;border:1px solid #cfcfcf;margin-top:6px}
.tests .tst{background:#f6f6f6!important;min-height:58px}
.tests .tst[data-l="mix"]{background:#ffec99!important}
.tests .tst:active{background:#ffec99!important}
#panel .card.df #tx,.app[data-mode="game"] #panel .card.df #tx{font-size:16px!important;line-height:1.3;text-transform:none;letter-spacing:0}
'''
i = s.rindex('</style>'); s = s[:i] + CSS + s[i:]
s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1)+'2026-11-06h'+m.group(3), s, count=1)
open('index.html','w',encoding='utf-8').write(s); print('ok')
