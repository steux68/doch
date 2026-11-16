#!/usr/bin/env python3
"""DOCH: Thema 'Lange Wörter' (lang): Komposita von hinten lesen, Artikel, Fugen, Bindestrich. Eigene Formulierung, Wörter nur als Beispiele."""
import re, sys
p="index.html"; s=open(p,encoding="utf-8").read()
if "GT.lang=" in s: sys.exit("already patched")
def J(l): return "["+",".join('"%s"'%x for x in l)+"]"
def Q(sent,o,why,lv): return ' {s:"%s",o:%s,why:"%s",lv:"%s"}'%(sent,J(o),why,lv)
def rows(items): return '<div class="rows">'+"".join('<div><span>%s</span><span>%s</span></div>'%(a,b) for a,b in items)+'</div>'
def tc(h,items,note): return '<div class="tc df"><h3>%s</h3>%s<p class="tline">%s</p></div>'%(h,rows(items),note)
def card(b,st,tx,gt): return ' {b:"%s",st:%s,tx:"%s",gt:"%s"}'%(b,st,tx,gt)
def R(h,l): return 'ruleSt("%s",%s)'%(h,J(l))
C=[
 card("Von hinten",R("Read from the back",["Rechts·schutz·versicherungs·gesellschaft","= eine Gesellschaft","für Versicherungen","für den Rechtsschutz"]),"The last part is the head","A long compound is a chain. The last noun says what it is, and everything in front describes it. The head also gives the article: die Gesellschaft."),
 card("Teile finden",R("Cut it into small words",["Kraft·fahr·zeug·haftpflicht·versicherung","Mindest·haltbarkeits·datum","Lebens·abschnitts·gefährte","Arbeits·unfähigkeits·bescheinigung","Streich·holz·schächtel·chen"]),"Find the small words first","Look for words you know. Then check what is left over: that is a joint letter or an ending."),
 card("Fuge -s",R("The joint -s",["Geschwindigkeit·s·begrenzung","Mindesthaltbarkeit·s·datum","Lebens·abschnitt","Wohnung·s·bau","Arbeit·s·zeit"]),"After -ung, -heit, -keit, -ion, -ität, -schaft","The joint -s is very common. It is almost always there after these endings. Otherwise it is part of the word and you learn it with the word."),
 card("Keine Fuge",R("No joint letter",["Brand·schutz·bestimmung","Bau·genehmigung","Einkommen·steuer·erklärung","Personal·ausweis"]),"Many compounds have no joint","Duden writes Einkommensteuer. You will also see Einkommenssteuer, but the standard form has no extra s."),
 card("Artikel",R("The head gives the article",["die Gesellschaft → die Versicherungsgesellschaft","das Datum → das Mindesthaltbarkeitsdatum","der Ausweis → der Personalausweis","das Gericht → das Bundesverfassungsgericht","-chen → das Streichholzschächtelchen"]),"Always take the article from the last noun","Even with 40 letters, only the last part matters. A diminutive ending -chen or -lein makes the word neuter."),
 card("Drei Buchstaben",R("Three letters in a row",["Schiff·fahrt → Schifffahrt","Still·leben → Stillleben","Brenn·nessel → Brennnessel","Bett·tuch → Betttuch"]),"Since the 1996 reform you keep all three","When a word ends and the next one starts with the same letter, you write both. A hyphen is allowed for easier reading: Schiff-Fahrt."),
 card("Bindestrich",R("Hyphen for readability",["Kfz-Haftpflichtversicherung","E-Mail-Adresse","24-Stunden-Dienst","Kraftfahrzeug-Haftpflichtversicherung"]),"A hyphen helps with abbreviations, numbers and very long words","Use it when a word would be hard to read or contains an abbreviation or a number."),
]
QS=[
 Q("___ Versicherungsgesellschaft",["die","der","das"],"The last noun decides: die Gesellschaft.","A2"),
 Q("___ Mindesthaltbarkeitsdatum",["das","der","die"],"The last noun decides: das Datum.","A2"),
 Q("___ Personalausweis",["der","die","das"],"The last noun decides: der Ausweis.","A2"),
 Q("___ Einkommensteuererklärung",["die","der","das"],"The last noun decides: die Erklärung.","A2"),
 Q("___ Bundesverfassungsgericht",["das","der","die"],"The last noun decides: das Gericht.","B1"),
 Q("___ Streichholzschächtelchen",["das","die","der"],"-chen makes the word neuter: das Schächtelchen.","B1"),
 Q("___ Geschwindigkeitsbegrenzung",["die","der","das"],"The last noun decides: die Begrenzung.","B1"),
 Q("___ Lebensabschnittsgefährte",["der","die","das"],"The last noun decides: der Gefährte.","B1"),
 Q("Geschwindigkeit___begrenzung",["s","n","en"],"After -keit and -heit the joint is -s. Geschwindigkeit ends in -keit.","B1"),
 Q("Mindesthaltbarkeit___datum",["s","n","en"],"After -keit the joint is -s: Mindesthaltbarkeitsdatum.","B1"),
 Q("Brand___schutz",["(nichts)","s","n"],"No joint letter: Brandschutz.","B1"),
 Q("Einkommen___steuer",["(nichts)","s","n"],"Duden: Einkommensteuer, without a joint.","B2"),
 Q("Lebens___abschnitt",["s","n","e"],"Lebensabschnitt has a joint -s.","B1"),
 Q("Wohnung___bau",["s","n","en"],"After -ung the joint is -s: Wohnungsbau.","B1"),
 Q("Arbeit___unfähigkeit",["s","n","(nichts)"],"Arbeitsunfähigkeit has a joint -s.","B2"),
 Q("Rechtsschutzversicherungsgesellschaft besteht aus ___ Nomen.",["vier","drei","sechs"],"Recht, Schutz, Versicherung, Gesellschaft: four nouns.","B2"),
 Q("Kraftfahrzeug besteht aus ___ Wörtern.",["drei","zwei","vier"],"Kraft, fahr(en), Zeug: three words.","B2"),
 Q("Still + Leben = ___",["Stillleben","Stilleben","Stillebben"],"Since the 1996 reform you keep all three l.","B2"),
 Q("Schiff + Fahrt = ___",["Schifffahrt","Schiffahrt","Schifahrt"],"Three f are kept: Schifffahrt.","B2"),
 Q("Brenn + Nessel = ___",["Brennnessel","Brennessel","Brenessel"],"Three n are kept: Brennnessel.","B2"),
 Q("Ein Streichholzschächtelchen ist eine kleine ___.",["Schachtel","Streichholz","Holz"],"The last noun is the head: it is a small box.","A2"),
 Q("Ein Fußballschuh ist ein ___.",["Schuh","Ball","Fuß"],"The last noun is the head: Schuh.","A2"),
 Q("Eine Kinderzimmertür ist eine ___.",["Tür","Zimmer","Kinder"],"The last noun is the head: Tür.","A2"),
 Q("Man schreibt auch: Kfz___Haftpflichtversicherung.",["-","/","."],"A hyphen makes long words easier to read.","B2"),
]
TH=[
 tc("Lesen",[("1","Den letzten Teil finden: das ist der Kern"),("2","Die kleinen Wörter davor suchen"),("3","Fuge oder Endung erkennen")],"Von hinten nach vorne."),
 tc("Fuge",[("-s","nach -ung, -heit, -keit, -ion, -ität"),("(nichts)","Brandschutz, Baugenehmigung, Einkommensteuer"),("3 Buchstaben","Schifffahrt, Stillleben, Brennnessel")],"Ein Bindestrich darf bei sehr langen Wörtern helfen."),
 tc("Artikel",[("der, die, das","vom letzten Nomen"),("-chen, -lein","immer das")],"Auch bei 40 Buchstaben zählt nur der Schluss."),
]
LG='<span><b class="wt k lgk">·</b> Teile</span>'
BL=('GT.lang={name:"Lange Wörter",badge:"Kompositum",tip:"Read from the back: the last noun gives the meaning and the article.",src:["duden","grammis","lingolia"],\n'
 ' lg:\'%s\',\n cards:[\n'%LG+",\n".join(C)+'],\n q:[\n'+",\n".join(QS)+'],\n th:`'+"".join(TH)+'`};\n')
a='/* ---------- topics + home ---------- */'
if s.count(a)!=1: sys.exit("Anker topics")
s=s.replace(a,"/* lang */\n"+BL+a)
a=' {t:"wortb",'
i=s.find(a); assert i>0
j=s.index("\n",i)+1
s=s[:j]+' {t:"lang",n:"Lange Wörter",tag:"Mindesthaltbarkeitsdatum",ds:"Komposita von hinten lesen, Artikel, Fugen, Bindestrich · A2–C1"},\n'+s[j:]
a='t:["oest","wortb","zungen","fehler"]'
if s.count(a)!=1: sys.exit("Anker Gruppe")
s=s.replace(a,'t:["oest","wortb","lang","zungen","fehler"]')
a='if(k==="oest")return'
if s.count(a)!=1: sys.exit("Anker lab")
s=s.replace(a,'if(k==="lang")return "Artikel oder Fuge";'+a)
m=re.search(r'name="app-version" content="(\d{4}-\d\d-\d\d)([a-z]?)"',s)
s=s.replace(m.group(0),'name="app-version" content="%s%s"'%(m.group(1),chr(ord(m.group(2) or "`")+1)))
open(p,"w",encoding="utf-8").write(s); print("OK")
