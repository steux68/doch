# Aktiv-Farbe einheitlich: gelb (#ffec99) statt Limette bei gewaehlten Knoepfen. 06.11.2026.
import re, sys
SEL = {'P': ['#theo .sub button[aria-pressed="true"]','.zch button[aria-pressed="true"]','.tlc .tltk.on','.tls button.on'],
       'D': ['.timer button[aria-pressed="true"]','.nw .art.on','.lvb[aria-pressed="true"]','.tlen button[aria-pressed="true"]','.wchips button[aria-pressed="true"]','.tlc .tltk.on','.tls button.on']}[sys.argv[1]]
VER = sys.argv[2]
s = open('index.html', encoding='utf-8').read()
if '/* active-yellow */' in s:
    print('schon angewendet'); sys.exit(0)
CSS = '\n/* active-yellow */\n' + ','.join(SEL) + '{background:#ffec99!important;color:#111;box-shadow:none!important}\n'
i = s.rindex('</style>'); s = s[:i] + CSS + s[i:]
s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1)+VER+m.group(3), s, count=1)
open('index.html','w',encoding='utf-8').write(s); print('ok')
