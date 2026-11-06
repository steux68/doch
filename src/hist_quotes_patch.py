# DOCH!: Zeitleiste buendig + groessere Bilder, Tests-Raster gepunktet, Zitat-Portraits quadratisch. 06.11.2026.
import re, sys
s = open('index.html', encoding='utf-8').read()
if '/* hist-quotes */' in s:
    print('schon angewendet'); sys.exit(0)
a='Math.max(2,P[0][1]-(P[0][0]-y)*.2)'
assert a in s
s=s.replace(a,'Math.max(0,P[0][1]-(P[0][0]-y)*.2)')
b0='const a=Math.max(0,tlX(r[0],G))'
assert b0 in s
s=s.replace(b0,'const a=r[0]<=-200?0:Math.max(0,tlX(r[0],G))')
assert 'th=Math.min(64,' in s
s=s.replace('th=Math.min(64,','th=Math.min(76,')
CSS='''
/* hist-quotes */
.tests{gap:0!important;background:none!important;border:0!important;border-top:1px dotted #b8b8b8!important;border-left:1px dotted #b8b8b8!important;margin-top:6px}
.tests .tst{border-right:1px dotted #b8b8b8;border-bottom:1px dotted #b8b8b8}
.tlth{outline:0!important;box-sizing:border-box}
.tlcd:active .tlth{outline:0!important;background:#cdff3e}
.qt,.hp .qt.alt{padding:8px!important;grid-template-columns:72px minmax(0,1fr)!important;align-items:center}
.qt .pic{width:72px!important;height:72px!important;box-sizing:border-box;border:1px dotted #b8b8b8;align-self:center}
.qt .pic::after{display:none!important}
.qt .pic img{object-position:50% 25%}
'''
i=s.rindex('</style>'); s=s[:i]+CSS+s[i:]
s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-11-06t'+m.group(3),s,count=1)
open('index.html','w',encoding='utf-8').write(s); print('ok')
