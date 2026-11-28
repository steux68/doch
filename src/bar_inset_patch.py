# 28.11.2026: Breiten-Regel (alle 3 Apps): Kästen (Balken, Karten, Reiter, Bilder, Punktlinien) gehen genau bis zur Strichlinie
# (Ende der kleinen Ticks, 18 px vom Rand). Text IN einem farbigen/grauen Kasten sitzt 10 px eingerückt, Text auf Weiß auf der Linie.
# Hier: Abschnitts-Balken (.hb) bekommen 10 px Innenabstand links und rechts wie bei dasein-design (offener Balken: 10 + 8 px).
# Aufruf: python3 src/bar_inset_patch.py NEUE_VERSION   danach: python3 src/version_sync.py
import sys,re
VER=sys.argv[1];f='index.html';s=open(f,encoding='utf-8').read()
BLK='<style id="bar-inset-css">/* 28.11.: Balken-Text 10 px eingerückt wie dasein-design */html body .hb.hb{padding-left:10px!important;padding-right:10px!important}</style>'
if 'id="bar-inset-css"' in s: s=re.sub(r'<style id="bar-inset-css">.*?</style>',lambda m:BLK,s,flags=re.S)
else: s=(s.replace('</body>',BLK+'\n</body>',1) if '</body>' in s else s.rstrip('\n')+'\n'+BLK+'\n')
s=re.sub(r'(<meta name="app-version" content=")[^"]+(")',lambda m:m.group(1)+VER+m.group(2),s,count=1)
open(f,'w',encoding='utf-8').write(s);print(f,'ok',VER)
