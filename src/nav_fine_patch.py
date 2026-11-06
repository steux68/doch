# Navigationsleisten unten: sehr feine punktierte Linien (1px/3px, hellgrau), grau im Ruhezustand, auf der Titelseite pulsierend bunt, aktiv neongelb. 06.11.2026.
import re, sys
s = open('index.html', encoding='utf-8').read()
if '/* nav-fine */' in s:
    print('schon angewendet'); sys.exit(0)
CSS = '''
/* nav-fine */
#hnav{border-top:0!important;background:#fff!important}
#hnav .hnb{border:0!important;background-color:#f2f2f2;
 background-image:repeating-linear-gradient(to right,#b8b8b8 0 1px,transparent 1px 3px),repeating-linear-gradient(to right,#b8b8b8 0 1px,transparent 1px 3px)!important;
 background-size:100% 1px,100% 1px!important;background-position:left top,left bottom!important;background-repeat:no-repeat!important}
#hnav .hnb:nth-child(odd){background-image:repeating-linear-gradient(to right,#b8b8b8 0 1px,transparent 1px 3px),repeating-linear-gradient(to right,#b8b8b8 0 1px,transparent 1px 3px),repeating-linear-gradient(to bottom,#b8b8b8 0 1px,transparent 1px 3px)!important;
 background-size:100% 1px,100% 1px,1px 100%!important;background-position:left top,left bottom,right top!important}
#hnav .hnb[aria-pressed="true"]{background-color:#cdff3e!important}
'''
i = s.rindex('</style>'); s = s[:i] + CSS + s[i:]
s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1)+'2026-11-06o'+m.group(3), s, count=1)
open('index.html','w',encoding='utf-8').write(s); print('ok')
