#!/usr/bin/env python3
"""Schreibt die Version aus <meta name="app-version"> in index.html nach version.txt.
Nach jeder Versionsänderung ausführen (die App prüft beim Öffnen nur diese kleine Datei)."""
import os,re
root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
s=open(os.path.join(root,'index.html'),encoding='utf-8').read()
v=re.search(r'name="app-version" content="([^"]+)"',s).group(1)
open(os.path.join(root,'version.txt'),'w',encoding='utf-8').write(v+'\n')
print('version.txt =',v)
