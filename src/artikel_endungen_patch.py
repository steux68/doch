#!/usr/bin/env python3
"""Artikel: mehr Endungen + Ausnahmen (2026-11-21k), eigene Formulierung nach der Idee eines Lernblatts. Idempotent."""
import os,re
root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
p=os.path.join(root,"index.html");s=open(p,encoding="utf-8").read()
if '"Reichtum"' in s: print("already patched");raise SystemExit
def rep(a,b):
    global s
    assert s.count(a)==1,a
    s=s.replace(a,b)
rep('"-enz","-anz"])','"-enz","-anz","-ade"])')
rep('"-nis","Verb als Nomen"','"-nis","-o","-ett","-zeug","-men","-em","Verb als Nomen"')
rep('"-ant","-ent","-or","Tage"','"-ant","-ent","-or","-iker","-eur","-är","-loge","-ast","Tage"')
rep('<div><span>-e</span><span>der Junge, der Name, das Auge, das Ende.</span></div>',
    '<div><span>-e</span><span>der Junge, der Name, das Auge, das Ende.</span></div>\n<div><span>-tum</span><span>das Eigentum, das Brauchtum, but <b>der</b> Reichtum, <b>der</b> Irrtum.</span></div>\n<div><span>-nis</span><span>das Ergebnis, das Geheimnis, but <b>die</b> Kenntnis, <b>die</b> Erkenntnis, <b>die</b> Finsternis.</span></div>')
W=[("der","Musiker","musician","-iker → der","B1"),("der","Chemiker","chemist","-iker → der","B2"),("der","Elektriker","electrician","-iker → der","B1"),
("der","Chauffeur","driver","-eur → der","B2"),("der","Friseur","hairdresser","-eur → der","B1"),("der","Millionär","millionaire","-är → der","B2"),
("der","Biologe","biologist","-loge → der","C1"),("der","Gast","guest","-ast → der","A2"),("der","Kontrast","contrast","-ast → der","B2"),
("der","Pianist","pianist","-ist → der","B1"),("der","Tourist","tourist","-ist → der","A2"),("der","Student","student","-ent → der","A1"),("der","Realismus","realism","-ismus → der","B2"),
("die","Olympiade","Olympic Games","-ade → die","B2"),("die","Eleganz","elegance","-anz → die","B2"),("die","Bilanz","balance sheet","-anz → die","C1"),
("das","Foto","photo","-o → mostly das","A1"),("das","Konto","account","-o → mostly das","A2"),("das","Problem","problem","-em → das","A2"),("das","System","system","-em → das","B1"),
("das","Thema","topic","-ma → das","A2"),("das","Schicksal","fate","-sal → mostly das","B2"),("das","Flugzeug","aeroplane","-zeug → das","A2"),("das","Werkzeug","tool","-zeug → das","B1"),
("das","Duett","duet","-ett → das","C1"),("das","Skelett","skeleton","-ett → das","C1"),("das","Volumen","volume","-men → das","C1"),("das","Phänomen","phenomenon","-men → das","C1"),
("das","Geheimnis","secret","-nis → mostly das","B1"),("das","Eigentum","property","-tum → mostly das","B2"),("das","Brauchtum","custom","-tum → mostly das","C1"),
("der","Reichtum","wealth","Exception: -tum, but der","B2"),("der","Irrtum","mistake","Exception: -tum, but der","B2"),
("die","Kenntnis","knowledge","Exception: -nis, but die","B2"),("die","Erkenntnis","insight","Exception: -nis, but die","C1"),("die","Finsternis","darkness","Exception: -nis, but die","C1")]
j=s.index('const ART=[');k=s.index('\n];',j)
extra="".join(',["%s","%s","%s","%s","%s"]'%w for w in W)
s=s[:k]+extra+s[k:]
s=re.sub(r'<meta name="app-version" content="[^"]+">','<meta name="app-version" content="2026-11-21k">',s,count=1)
open(p,"w",encoding="utf-8").write(s);print("ok",len(W))
