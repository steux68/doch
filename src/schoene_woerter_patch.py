#!/usr/bin/env python3
"""Staunen > Redewendungen: neuer Filter 'Wörter mit Geschichte' (14 schöne Wörter). Eigene Formulierung, keine Herkunftsbehauptungen ohne Quelle. Idempotent."""
import os
root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
p=os.path.join(root,"index.html");s=open(p,encoding="utf-8").read()
if '["wort","B2","das Fernweh"' in s: print("already");raise SystemExit
W=[
("B2","das Fernweh","die Sehnsucht nach der Ferne, nach fremden Orten (Fern + Weh, das Gegenstück zu Heimweh)","wanderlust, a longing for faraway places","Sobald die ersten warmen Tage kommen, packt mich das Fernweh."),
("B2","die Schadenfreude","Freude über das Missgeschick eines anderen (Schaden + Freude)","joy at someone else's misfortune (English borrowed the word)","Ich gebe zu, ich habe etwas Schadenfreude gespürt, als der Chef im Regen stand."),
("B1","der Feierabend","das Ende des Arbeitstages und die freie Zeit danach","the end of the working day, and the free evening after it","Um fünf ist Feierabend, dann gehe ich laufen."),
("C1","das Fingerspitzengefühl","die Fähigkeit, in einer heiklen Lage genau das Richtige zu tun (Gefühl in den Fingerspitzen)","tact, a delicate touch","Für diese Verhandlung braucht man viel Fingerspitzengefühl."),
("C1","die Torschlusspanik","die Angst, etwas zu verpassen, wenn die Zeit knapp wird (das Bild: das Tor, das gleich schließt)","fear of missing the last chance","Kurz vor dem Ende der Aktion kam bei vielen die Torschlusspanik."),
("C1","der Weltschmerz","tiefe Traurigkeit über den Zustand der Welt (Welt + Schmerz)","world-weariness, sorrow about the state of the world","Nach den Nachrichten überkam ihn ein leiser Weltschmerz."),
("B2","der Zeitgeist","die Haltung und der Geschmack einer Zeit (Zeit + Geist; auch im Englischen gebräuchlich)","the spirit of the age","Der Roman trifft genau den Zeitgeist der neunziger Jahre."),
("B1","der Ohrwurm","eine Melodie, die man nicht mehr aus dem Kopf bekommt (Ohr + Wurm)","an earworm, a tune stuck in your head","Seit gestern habe ich diesen Ohrwurm und werde ihn nicht los."),
("B2","der Kummerspeck","das Gewicht, das man durch Kummer und Trösten mit Essen zugenommen hat (Kummer + Speck)","weight gained from comfort eating when sad","Nach der Trennung hat sie sich ordentlich Kummerspeck angefuttert."),
("C1","das Backpfeifengesicht","ein Gesicht, das zum Ohrfeigen reizt – humorvoll gemeint (Backpfeife = Ohrfeige)","a face that begs to be slapped (said with a wink)","Mit diesem Grinsen hat er ein richtiges Backpfeifengesicht."),
("B2","die Sehnsucht","ein starkes, oft schmerzliches Verlangen nach etwas Fernem oder Verlorenem","a deep longing","Sie sprach mit Sehnsucht von ihrer Kindheit am Meer."),
("C1","der Treppenwitz","die gute Antwort, die einem erst auf der Treppe einfällt – zu spät","the perfect reply that comes to you too late","Mein bester Spruch war leider ein Treppenwitz."),
("C1","verschlimmbessern","etwas verbessern wollen und es dabei verschlechtern (verschlimmern + verbessern)","to make worse by trying to improve","Lass den Text jetzt in Ruhe, sonst verschlimmbesserst du ihn nur."),
("B1","gemütlich","warm, behaglich und angenehm – von Räumen, Abenden und Menschen","cosy, snug, pleasantly relaxed","Wir haben es uns auf dem Sofa gemütlich gemacht."),
]
rows=''.join('["wort","%s","%s","%s","%s","%s",null,null],'%(l,w,e,en,x) for l,w,e,en,x in W)
for l,w,e,en,x in W:
    assert '"' not in (w+e+en+x), w
rows=rows.rstrip(',')
a='"to put the cart before the horse","Erst bauen und dann planen? Das heißt, das Pferd von hinten aufzäumen.",null,null]];'
assert s.count(a)==1
s=s.replace(a,a[:-2]+','+rows+'];')
b='["arg", "Argumentieren"]];'
assert s.count(b)==1
s=s.replace(b,'["arg", "Argumentieren"], ["wort", "Wörter mit Geschichte"]];')
open(p,'w',encoding='utf-8').write(s);print('ok',len(W))
