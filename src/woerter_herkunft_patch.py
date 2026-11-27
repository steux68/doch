#!/usr/bin/env python3
"""Herkunft (Etymologie) fuer die 'Woerter mit Geschichte', nur nach DWDS geprueft; 4 neue Woerter (Kindergarten, Doppelgaenger, Heimat, Angst). Ohne DWDS-Beleg bleibt Herkunft leer. Idempotent."""
import os,json
root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
p=os.path.join(root,"index.html");s=open(p,encoding="utf-8").read()
if '"das Kindergarten"' in s or '"der Kindergarten"' in s: print("already");raise SystemExit
H={
"die Schadenfreude":("Seit dem 16. Jahrhundert belegt: Schaden + Freude, die Freude über den Schaden, der anderen entsteht.","Schadenfreude"),
"der Feierabend":("Feier- geht auf lateinisch feriae zurück, die Ruhetage. Im 16. Jahrhundert bedeutet das Wort die abendliche Ruhezeit nach dem Arbeitstag.","Feierabend"),
"der Zeitgeist":("Zuerst 1769 bei Herder belegt, als Haltung einer Epoche. Ein Vorläufer, der „Genius unserer Zeit“, steht schon 1739 bei Zinzendorf.","Zeitgeist"),
"der Weltschmerz":("Das Wort geht auf Jean Paul zurück. Nach 1830 machte Heine es zum Modewort; später spotteten Dichter wie Eichendorff darüber.","Weltschmerz"),
"der Ohrwurm":("Als Insekt seit dem 14. Jahrhundert belegt (mittelhochdeutsch ōrwurm); man glaubte irrig, es krieche ins Ohr. Die Bedeutung „einprägsame Melodie“ kommt erst Mitte des 20. Jahrhunderts.","Ohrwurm"),
"die Sehnsucht":("Mittelhochdeutsch sensuht. Sucht war ursprünglich eine Krankheit; Sehnsucht galt also als quälendes Leiden. Woher sehnen kommt, ist unsicher.","Sehnsucht"),
"der Treppenwitz":("Um 1850 aus dem Französischen übersetzt (l'esprit d'escalier). Die Idee geht wohl auf Diderot zurück: Man findet die kluge Antwort erst auf der untersten Stufe.","Treppenwitz"),
"verschlimmbessern":("Von Georg Christoph Lichtenberg im 18. Jahrhundert geprägt, eine Mischung aus verschlimmern und verbessern.","verschlimmbessern"),
"gemütlich":("Von Gemüt, dem alten Wort für Sinn und Stimmung (althochdeutsch gimuoti, 9. Jahrhundert). Im 18. Jahrhundert wurde gemütlich zum Wort für das, was das Gefühl anspricht.","gemütlich"),
}
for w,(t,slug) in H.items():
    i=s.index('"wort","')  # first
    k=s.index(',"%s",'%w,i)
    e=s.index(',null,null]',k)
    assert e-k<700,(w,e-k)
    from urllib.parse import quote
    link=["https://www.dwds.de/wb/"+quote(slug),"DWDS"]
    s=s[:e]+','+json.dumps(t,ensure_ascii=False)+','+json.dumps(link,ensure_ascii=False)+']'+s[e+len(',null,null]'):]
N=[
("B1","der Kindergarten","die Vorschule für kleine Kinder (Kinder + Garten); das Wort wird auch im Englischen benutzt","preschool (the German word is used in English too)","Unsere Tochter geht seit September in den Kindergarten.","1840 von Friedrich Fröbel für seine Vorschule für kleine Kinder geprägt.","Kindergarten"),
("C1","der Doppelgänger","ein Mensch, der einem anderen zum Verwechseln ähnlich sieht (doppelt + Gänger)","a lookalike, a double","Auf dem Foto sah er aus wie sein eigener Doppelgänger.","Zuerst als Doppeltgänger 1796 bei Jean Paul belegt, für Menschen, die sich selbst sehen. Das -t fällt in der Zusammensetzung weg.","Doppelgänger"),
("B2","die Heimat","der Ort oder das Land, wo man herkommt und sich zu Hause fühlt – schwer ins Englische zu übersetzen","home, homeland (no single English word)","Für viele Menschen ist Heimat vor allem ein Gefühl.","Von Heim mit einer Endung gebildet (althochdeutsch heimōti, 11. Jahrhundert). Seit dem 15. Jahrhundert Heimat; früher war das Wort sächlich.","Heimat"),
("B1","die Angst","das Gefühl, bedroht zu sein oder dass etwas Schlimmes passiert","fear, anxiety","Ich habe keine Angst vor der Prüfung, nur etwas Respekt.","Althochdeutsch angust (8. Jahrhundert), verwandt mit eng: ursprünglich der Zustand der Enge.","Angst"),
]
rows=''
for l,w,e,en,x,h,slug in N:
    for t in (w,e,en,x,h): assert '"' not in t,t
    rows+=',["wort","%s","%s","%s","%s","%s",%s,%s]'%(l,w,e,en,x,json.dumps(h,ensure_ascii=False),json.dumps(["https://www.dwds.de/wb/"+quote(slug),"DWDS"],ensure_ascii=False))
a='"wort","C1","verschlimmbessern"'
# append new rows after the last wort row: find the end of RW array
j=s.index('];',s.index('"wort","B1","gemütlich"'))
s=s[:j]+rows+s[j:]
open(p,'w',encoding='utf-8').write(s);print('ok',len(H),len(N))
