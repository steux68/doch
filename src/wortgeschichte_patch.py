#!/usr/bin/env python3
"""Geschichte-Zeitleiste: 13 Wortgeschichten (Angst bis Treppenwitz) als Eintraege vom Typ 'wort'. Daten nur nach DWDS geprueft. Idempotent."""
import os,re
from urllib.parse import quote
root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
p=os.path.join(root,"index.html");s=open(p,encoding="utf-8").read()
if 'ini:"angust"' in s: print("already");raise SystemExit
def shrink(w):
    n=len(w);f=1 if n<=8 else .78 if n<=10 else .6 if n<=13 else .5
    return w if f==1 else '<span style="font-size:%.2fem">%s</span>'%(f,w)
E=[
(790,"8. Jh.","angust","„Enge“","→ Angst","Angst","Althochdeutsch <i>angust</i>, im 8. Jahrhundert belegt. Das Wort ist mit <i>eng</i> verwandt: Angst war ursprünglich die Enge, das Gefühl, dass es zu eng wird. Dieselbe Wurzel steckt im lateinischen <i>angustus</i>, „eng“."),
(850,"9. Jh.","gimuoti","„Gemüt“","→ gemütlich","gemütlich","Althochdeutsch <i>gimuoti</i> (9. Jahrhundert) meint das Gemüt, alle Kräfte von Sinn und Gefühl. Daraus wird <i>gemütlich</i>. Im 18. Jahrhundert, auch im Pietismus, bekommt das Wort seinen warmen Klang: was das Gefühl anspricht."),
(1050,"11. Jh.","heimōti","„Heimat“","→ Heimat","Heimat","Aus <i>Heim</i> und einer Endung entsteht im 11. Jahrhundert <i>heimōti</i>. Die Form <i>Heimat</i> taucht im 15. Jahrhundert auf und setzt sich im 16. durch. Bis ins 17. Jahrhundert war das Wort noch sächlich: <i>das Heimat</i>."),
(1205,"Mhd.","sensuht","„Sehnsucht“","→ Sehnsucht","Sehnsucht","Mittelhochdeutsch <i>sensuht</i>. <i>Sucht</i> war ursprünglich eine Krankheit: Sehnsucht galt als quälendes Leiden. Woher <i>sehnen</i> kommt, ist unsicher."),
(1350,"14. Jh.","ōrwurm","„Insekt“","→ Ohrwurm","Ohrwurm","Im 14. Jahrhundert ist <i>ōrwurm</i> ein Insekt. Man glaubte irrig, es krieche in die Ohren. Im 18. Jahrhundert nennt man so einen Schmeichler; erst Mitte des 20. Jahrhunderts wird daraus die Melodie, die man nicht mehr loswird."),
(1550,"16. Jh.","Feierabend","„Ruhezeit“","","Feierabend","<i>Feier-</i> geht über lateinisch <i>feriae</i> auf die Ruhetage zurück; schon um 800 gibt es dafür althochdeutsch <i>fīra</i>. Im 16. Jahrhundert bedeutet <i>Feierabend</i> die abendliche Ruhezeit nach dem Arbeitstag."),
(1560,"16. Jh.","Schadenfreude","„Freude am Schaden“","","Schadenfreude","Seit dem 16. Jahrhundert belegt: <i>Schaden</i> + <i>Freude</i>, die Freude über den Schaden, der anderen entsteht."),
(1769,"1769","Zeitgeist","„Geist der Zeit“","","Zeitgeist","Herder verwendet das Wort 1769 für die Haltung einer Epoche. Ein Vorläufer, der „Genius unserer Zeit“, steht schon 1739 bei Zinzendorf."),
(1780,"2. Hälfte 18. Jh.","verschlimmbessern","„verbessern + verschlimmern“","","verschlimmbessern","Georg Christoph Lichtenberg prägt das Wort in der zweiten Hälfte des 18. Jahrhunderts: eine Mischung aus <i>verschlimmern</i> und <i>verbessern</i>. Das Substantiv <i>Verschlimmbesserung</i> folgt Mitte des 19. Jahrhunderts."),
(1796,"1796","Doppeltgänger","„Doppelgänger“","","Doppelgänger","Bei Jean Paul steht 1796 zuerst <i>Doppeltgänger</i>, für Menschen, die sich selbst sehen. In der Zusammensetzung mit <i>doppelt</i> fällt das <i>-t</i> später weg."),
(1830,"nach 1830","Weltschmerz","„Welt + Schmerz“","","Weltschmerz","Das Wort geht auf Jean Paul zurück. Nach 1830 macht Heine es zum Modewort; später spotten Dichter wie Eichendorff darüber."),
(1840,"1840","Kindergarten","„Garten für Kinder“","","Kindergarten","Friedrich Fröbel prägt das Wort 1840 für seine Vorschule für kleine Kinder."),
(1850,"um 1850","Treppenwitz","„l’esprit d’escalier“","","Treppenwitz","Um 1850 aus dem Französischen übersetzt: <i>l’esprit d’escalier</i>, der Witz, der einem erst auf der Treppe einfällt. Die Idee geht wohl auf Diderot zurück."),
]
i=s.index('const TL=[');j=s.index('\n];',i);tl=s[i:j]
lines=tl.split('\n')
def ins(e):
    y,d,big,smp,abc,slug,x=e
    for w in (big,smp,abc,x): assert '"' not in w.replace('„','').replace('“','') or True
    lab='' if len(d)<=6 else ''
    ent=' {y:%d,d:"%s",t:"%s",ty:"wort",smp:\'<b>%s</b><em>%s</em>\',big:%s,abc:"%s",ini:"%s",x:"%s",l:["https://www.dwds.de/wb/%s","DWDS"]},'%(y,d,(big if big==slug else big+' → '+slug),big,smp,repr(shrink(big)).replace("'",'"') if False else '"'+shrink(big).replace('"',"'")+'"',abc.replace('"',"'"),big,x.replace('"',"'"),quote(slug))
    return ent
out=[]
pend=sorted(E)
for ln in lines:
    m=re.match(r' \{y:(\d+)',ln)
    if m:
        y=int(m.group(1))
        while pend and pend[0][0]<y: out.append(ins(pend.pop(0)))
    out.append(ln)
while pend: out.append(ins(pend.pop(0)))
s=s[:i]+'\n'.join(out)+s[j:]
open(p,'w',encoding='utf-8').write(s);print('ok',len(E))
