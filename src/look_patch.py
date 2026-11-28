# 28.11.2026: Look-Audit (AUDIT_LOOK_2026-11-28.md), Punkte 1–2: Schriftgrößen nur 12/14/16, Versal-Labels .12em.
# „ENTDECKEN“ 10 -> 12 px; „mehr Hilfsmittel“ 13 -> 14 px; „Staunen [C] →“ .08 -> .12em.
# Aufruf: python3 src/look_patch.py NEUE_VERSION   danach: python3 src/version_sync.py
import sys,re
VER=sys.argv[1];f='index.html';s=open(f,encoding='utf-8').read()
BLK=('<style id="look-css">/* 28.11. Look-Audit */'
 'html body .rcb small{font-size:12px!important;letter-spacing:.12em!important}'
 'html body .mrow .l1 .cvt,html body .mrow .l1 b{font-size:14px!important}'
 'html body .gwk{letter-spacing:.12em!important}</style>')
if 'id="look-css"' in s: s=re.sub(r'<style id="look-css">.*?</style>',lambda m:BLK,s,flags=re.S)
else: s=s.rstrip('\n')+'\n'+BLK+'\n'
s=re.sub(r'(<meta name="app-version" content=")[^"]+(")',lambda m:m.group(1)+VER+m.group(2),s,count=1)
open(f,'w',encoding='utf-8').write(s);print(f,'ok',VER)
