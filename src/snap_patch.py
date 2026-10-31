# Fehler: Beim Laden sprang DOCH! per Scroll-Snap (y proximity, #p-hist start) auf die Geschichte statt auf die Startseite.
# Behebung: Snap am Hauptcontainer abschalten. Idempotent. Aufruf im Repo-Hauptordner: python3 -I src/snap_patch.py
import re
P="index.html";s=open(P,encoding="utf-8").read()
s=s.replace("#hscroll{scroll-snap-type:y proximity}#p-hist{scroll-snap-align:start}","#hscroll{scroll-snap-type:none}#p-hist{scroll-snap-align:none}")
s=re.sub(r'(<meta name="app-version" content=")[^"]*(")',lambda m:m.group(1)+'2026-11-01a'+m.group(2),s,count=1)
open(P,"w",encoding="utf-8").write(s)
