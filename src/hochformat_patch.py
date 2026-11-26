# Audit 27.11., Punkt 10 (Steuart: Weg B): installierte App nur im Hochformat ("orientation":"portrait" im Manifest).
# Wirkt nur in der installierten App (Android/Chrome), nicht im normalen Browser-Tab. DOCH bekommt dabei auch "lang":"de".
# Aufruf aus dem Repo-Ordner: python3 src/hochformat_patch.py manifest.webmanifest [weitere …]
import sys,json
for f in sys.argv[1:]:
    raw=open(f,encoding='utf-8').read(); m=json.loads(raw)
    m['orientation']='portrait'; m.setdefault('lang','de')
    out=json.dumps(m,ensure_ascii=False,indent=None if '\n' not in raw.strip() else 1,separators=(',',':') if '\n' not in raw.strip() else (',',': '))
    open(f,'w',encoding='utf-8').write(out+('\n' if raw.endswith('\n') else '')); print(f,'ok')
