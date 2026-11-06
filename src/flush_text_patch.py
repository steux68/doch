# DOCH!: wie dasein-design – Text buendig mit Bloecken/Kanten (kein Extra-Einzug), Fotos mit gepunktetem Rahmen. 06.11.2026.
import re, sys
s = open('index.html', encoding='utf-8').read()
if '/* flush-text */' in s:
    print('schon angewendet'); sys.exit(0)
CSS='''
/* flush-text */
.hp .tc>h3,.hp .tc>.tline,.hp .tc>p,.hp .qsec,.hp .tlen{padding-left:0!important;padding-right:0!important}
.hp .hi,.hp .hi:nth-child(odd){padding-left:0!important;padding-right:0!important}
.qt .pic::after{display:block!important}
'''
i=s.rindex('</style>'); s=s[:i]+CSS+s[i:]
s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-11-06v'+m.group(3),s,count=1)
open('index.html','w',encoding='utf-8').write(s); print('ok')
