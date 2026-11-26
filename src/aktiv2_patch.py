# Audit 27.11., Punkt 5 (Steuart hat das Mock-up „nachher · normal“ freigegeben): aktiv = Neon + fett + 2-px-Linie unten; gelbe Leiste [02] Sand #f2e2b0; DOCH „Entdecken/Weitermachen/Fehler“-Karte hellgrau.
# Aufruf: python3 src/aktiv2_patch.py index.html NEUE_VERSION   danach: python3 src/version_sync.py
import sys,re,os
f,VER=sys.argv[1],sys.argv[2]
CSS=open(os.path.join(os.path.dirname(__file__),'aktiv2.css.html'),encoding='utf-8').read().strip()
s=open(f,encoding='utf-8').read()
if '<style id="aktiv2-css">' in s: s=re.sub(r'<style id="aktiv2-css">.*?</style>',lambda m:CSS,s,flags=re.S)
else:
    s=s.rstrip('\n')+'\n'+CSS+'\n'   # ans Ende: zuletzt in der Kaskade
s=re.sub(r'(<meta name="app-version" content=")[^"]+(")',lambda m:m.group(1)+VER+m.group(2),s,count=1)
open(f,'w',encoding='utf-8').write(s); print(f,'ok',VER)
