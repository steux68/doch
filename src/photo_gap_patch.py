# DOCH!: Textoberkante = Fotooberkante in Zitaten. 06.11.2026.
import re, sys
s = open('index.html', encoding='utf-8').read()
if '/* photo-gap */' in s:
    print('schon angewendet'); sys.exit(0)
CSS='''
/* photo-gap */
.qt,.hp .qt.alt{padding:8px 0!important;min-height:0!important}
.qt .pic{margin:0!important}
.qt .qb{padding:0 8px 0 0!important}
.qt b.who{line-height:1.1;display:block;margin-top:-3px}
'''
i=s.rindex('</style>'); s=s[:i]+CSS+s[i:]
s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-11-06x'+m.group(3),s,count=1)
open('index.html','w',encoding='utf-8').write(s); print('ok')
