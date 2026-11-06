# DOCH!: Fotos gepunktet (Rahmen aussen), gleicher Abstand oben/unten wie Text. 06.11.2026.
import re, sys
s = open('index.html', encoding='utf-8').read()
if '/* photo-uniform */' in s:
    print('schon angewendet'); sys.exit(0)
CSS='''
/* photo-uniform */
.qt .pic{box-sizing:border-box;border:1px dotted #b8b8b8!important;margin:8px 0}
.qt .pic::after{display:none!important}
.qt,.hp .qt.alt{min-height:108px!important}
.tlth{box-sizing:border-box;border:1px dotted #b8b8b8}
.tlth::after{display:none!important}
'''
i=s.rindex('</style>'); s=s[:i]+CSS+s[i:]
s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-11-06w'+m.group(3),s,count=1)
open('index.html','w',encoding='utf-8').write(s); print('ok')
