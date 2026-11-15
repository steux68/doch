#!/usr/bin/env python3
"""DOCH Genitiv: Präpositionen in drei Karten (häufig · Ort & Zeit · Grund & Amtssprache) + 12 neue Spielfragen (eigene Formulierung)."""
import re, sys
p="index.html"; s=open(p,encoding="utf-8").read()
if "/* gen-praep */" in s: sys.exit("already patched")
old=''' {b:"Präp.",st:ruleSt("wegen · trotz · während · statt",["wegen des Regens","trotz der Kälte","während der Sitzung","innerhalb einer Woche"]),tx:"Prepositions with Genitiv",gt:"Also: aufgrund, außerhalb, innerhalb, anstatt."},
'''
new=''' /* gen-praep */
 {b:"Präp. A",st:ruleSt("wegen · trotz · während · statt",["wegen des Regens","trotz der Kälte","während der Sitzung","statt eines Plans"]),tx:"The four common ones: use the Genitiv",gt:"Also anstatt (= statt). In speech you often hear wegen + Dativ, but write the Genitiv."},
 {b:"Präp. B",st:ruleSt("innerhalb · außerhalb · oberhalb · unterhalb",["innerhalb einer Woche","außerhalb der Stadt","oberhalb des Dorfes","unterhalb der Brücke"]),tx:"Place and time, slightly formal",gt:"All four end in -halb. After them comes the Genitiv: außerhalb der Stadt."},
 {b:"Präp. C",st:ruleSt("aufgrund · infolge · angesichts · hinsichtlich",["aufgrund des Wetters","infolge eines Unfalls","angesichts der Lage","hinsichtlich des Preises"]),tx:"Reason and official language (B2–C1)",gt:"Typical in letters, news and contracts. Also: bezüglich, anlässlich, zugunsten."},
'''
if s.count(old)!=1: sys.exit("Anker Karte")
s=s.replace(old,new)
anchor=''' {s:"Das bedarf ___ Erklärung.",lv:"C1",o:["einer","eine","einem"],why:"bedürfen + Genitiv (C1).",h:"eine Erklärung",r:"einer Erklärung"}
];'''
if s.count(anchor)!=1: sys.exit("Anker Fragen")
def q(sent,lv,o,why,h,r): return ' {s:"%s",lv:"%s",o:%s,why:"%s",h:"%s",r:"%s"}'%(sent,lv,o,why,h,r)
Q=[
 q("Statt ___ Kaffees nehme ich einen Tee.","B1",'["des","dem","den"]',"statt + Genitiv; masculine → des Kaffees.","der Kaffee","des Kaffees"),
 q("Trotz ___ Verspätung sind wir pünktlich.","B1",'["der","die","dem"]',"trotz + Genitiv; feminine → der.","die Verspätung","der Verspätung"),
 q("Während ___ Pause ruft sie an.","B1",'["der","die","dem"]',"während + Genitiv; feminine → der.","die Pause","der Pause"),
 q("Außerhalb ___ Stadt gibt es einen See.","B2",'["der","die","dem"]',"außerhalb + Genitiv; feminine → der.","die Stadt","der Stadt"),
 q("Oberhalb ___ Dorfes steht eine Kapelle.","B2",'["des","dem","das"]',"oberhalb + Genitiv; neuter → des Dorfes.","das Dorf","des Dorfes"),
 q("Unterhalb ___ Brücke fließt der Fluss langsam.","B2",'["der","die","dem"]',"unterhalb + Genitiv; feminine → der.","die Brücke","der Brücke"),
 q("Innerhalb ___ Monats muss die Rechnung bezahlt werden.","B2",'["des","dem","den"]',"innerhalb + Genitiv; masculine → des Monats.","der Monat","des Monats"),
 q("Aufgrund ___ Unfalls blieb die Straße gesperrt.","C1",'["des","dem","den"]',"aufgrund + Genitiv; masculine → des Unfalls.","der Unfall","des Unfalls"),
 q("Angesichts ___ Lage müssen wir sofort handeln.","C1",'["der","die","dem"]',"angesichts + Genitiv; feminine → der.","die Lage","der Lage"),
 q("Infolge ___ Sturms fiel der Strom aus.","C1",'["des","dem","den"]',"infolge + Genitiv; masculine → des Sturms.","der Sturm","des Sturms"),
 q("Bezüglich ___ Anfrage melden wir uns morgen.","C1",'["Ihrer","Ihre","Ihrem"]',"bezüglich + Genitiv; feminine → Ihrer.","Ihre Anfrage","Ihrer Anfrage"),
 q("Hinsichtlich ___ Preises sind wir flexibel.","C1",'["des","dem","den"]',"hinsichtlich + Genitiv; masculine → des Preises.","der Preis","des Preises"),
]
s=s.replace(anchor,anchor[:-3].rstrip()+",\n"+",\n".join(Q)+"\n];")
m=re.search(r'name="app-version" content="(\d{4}-\d\d-\d\d)([a-z]?)"',s)
s=s.replace(m.group(0),'name="app-version" content="%s%s"'%(m.group(1),chr(ord(m.group(2) or "`")+1)))
open(p,"w",encoding="utf-8").write(s); print("OK")
