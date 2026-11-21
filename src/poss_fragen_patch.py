#!/usr/bin/env python3
"""Possessivartikel: 15 Uebungsfragen im Thema Faelle (2026-11-21q). Eigene Formulierung. Idempotent."""
import os,re
root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
p=os.path.join(root,"index.html");s=open(p,encoding="utf-8").read()
if "Anna liest ___ Buch. (sie)" in s: print("already patched");raise SystemExit
a=''' {s:"Der Sattel passt ___ Pferd nicht.",n:"das Pferd",cs:"Dativ",o:["dem", "das", "den"],why:"passen (= to fit) + Dativ.",lv:"B1"}
].map(q=>Object.assign({k:"f",c:0},q)));'''
assert s.count(a)==1
Q=[
("Peter repariert ___ Fahrrad. (er)","sein Fahrrad","Akkusativ",["sein","seine","ihr"],"Owner er → sein. Fahrrad is neuter in the Akkusativ: no ending.","A1"),
("Anna liest ___ Buch. (sie)","ihr Buch","Akkusativ",["ihr","sein","ihre"],"Owner sie → ihr. Buch is neuter in the Akkusativ: no ending.","A1"),
("Ich vermisse ___ Familie. (ich)","meine Familie","Akkusativ",["meine","meinen","meiner"],"vermissen + Akkusativ. Familie is feminine: meine.","A1"),
("Hast du ___ Schlüssel gefunden? (du)","dein Schlüssel","Akkusativ",["deinen","dein","deinem"],"Akkusativ masculine takes -en: dein → deinen.","A1"),
("Wir machen ___ Hausaufgaben. (wir)","unsere Hausaufgaben","Akkusativ",["unsere","unseren","unser"],"Plural in the Akkusativ: unsere.","A1"),
("Ich helfe ___ Schwester beim Umzug. (ich)","meine Schwester","Dativ",["meiner","meine","meinem"],"helfen + Dativ. Feminine Dativ: meine → meiner.","A2"),
("Er wohnt bei ___ Großmutter. (er)","seine Großmutter","Dativ",["seiner","seine","ihrer"],"bei + Dativ. Owner er → sein-, feminine Dativ: seiner.","A2"),
("Wir fahren mit ___ Kindern in den Urlaub. (wir)","unsere Kinder","Dativ",["unseren","unsere","unserer"],"mit + Dativ plural: unseren Kindern.","A2"),
("Ihr habt ___ Auto vergessen. (ihr)","euer Auto","Akkusativ",["euer","unser","eure"],"Owner ihr → euer. Auto is neuter in the Akkusativ: no ending.","A2"),
("Kinder, habt ihr ___ Jacken mitgenommen? (ihr)","eure Jacken","Akkusativ",["eure","euer","euren"],"Plural in the Akkusativ: eure. The e before r stays when an ending follows: eure, not euere.","A2"),
("Sie ruft ___ Mann an. (sie)","ihr Mann","Akkusativ",["ihren","ihr","seinen"],"Owner sie → ihr-. anrufen + Akkusativ, masculine: ihren.","A2"),
("Frau Berger, ist das ___ Tasche? (Sie)","Ihre Tasche","Nominativ",["Ihre","Ihr","Deine"],"Formal Sie → Ihr-, with a capital letter. Tasche is feminine: Ihre.","A2"),
("Ohne ___ Hilfe schaffe ich das nicht. (du)","deine Hilfe","Akkusativ",["deine","dein","deiner"],"ohne is always Akkusativ. Hilfe is feminine: deine.","A2"),
("Sie erklärt ___ Kollegen den Plan. (sie)","ihr Kollege","Dativ",["ihrem","ihren","seinem"],"erklären: the person is Dativ. Owner sie → ihr-, masculine Dativ: ihrem.","B1"),
("Der Architekt zeigt ___ Kunden den Entwurf. (er)","sein Kunde","Dativ",["seinem","seinen","ihrem"],"zeigen: the person is Dativ. Owner er → sein-, masculine Dativ: seinem. (Kunde adds -n only in Akkusativ, Dativ and Genitiv: seinem Kunden.)","B1"),
]
def esc(x): return x.replace('"','\\"')
lines=[]
for t,n,cs,o,w,lv in Q:
    lines.append(' {s:"%s",n:"%s",cs:"%s",o:[%s],why:"%s",lv:"%s"}'%(esc(t),esc(n),cs,",".join('"%s"'%esc(x) for x in o),esc(w),lv))
b=a.replace('"B1"}\n].map',  '"B1"},\n'+",\n".join(lines)+'\n].map')
s=s.replace(a,b)
s=re.sub(r'<meta name="app-version" content="[^"]+">','<meta name="app-version" content="2026-11-21q">',s,count=1)
open(p,"w",encoding="utf-8").write(s);print("ok",len(Q))
