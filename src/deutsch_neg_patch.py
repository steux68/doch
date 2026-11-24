#!/usr/bin/env python3
"""DOCH: Pilot 'Lernen auf Deutsch' - Verneinung (Karten, Tipp, Warum-Karte). Eigene Formulierung. Idempotent."""
import sys
p="index.html"; s=open(p,encoding="utf-8").read()
a=s.find("GT.neg={"); b=s.find("\nGT.",a+10); assert a>0 and b>a
seg=s[a:b]
if "Erst fragen: Ist es ein Nomen" in seg: sys.exit("already patched")
R=[
 ("First ask: is it a noun with ein or no article? Then kein. Everything else: nicht.","Erst fragen: Ist es ein Nomen mit ein oder ohne Artikel? Dann kein. Alles andere: nicht."),
 ("A noun with <b>ein</b>, or with no article at all, is negated with <b>kein</b>. English: no, not a.","Ein Nomen mit <b>ein</b> oder ganz ohne Artikel verneinst du mit <b>kein</b>."),
 ("kein takes the endings of ein","kein hat die Endungen von ein"),
 ("Kaffee → keinen Kaffee. Unlike ein, kein has a plural: <b>keine</b> Pläne.","Kaffee → keinen Kaffee. Anders als ein hat kein einen Plural: <b>keine</b> Pläne."),
 ("With a definite article, a possessive (mein, dein …) or a name, use <b>nicht</b>. Das ist nicht mein Auto.","Bei bestimmtem Artikel, Possessivwort (mein, dein …) oder Namen steht <b>nicht</b>. Das ist nicht mein Auto."),
 ("nicht before Verb 2","nicht vor Verb 2"),
 ("To negate the whole sentence, <b>nicht</b> goes as late as possible, but before the second part of the bracket.","Verneinst du den ganzen Satz, steht <b>nicht</b> möglichst weit hinten, aber vor dem zweiten Teil der Satzklammer."),
 ("nicht before the prefix","nicht vor der Vorsilbe"),
 ("The prefix closes the bracket, so <b>nicht</b> comes just before it. Time words like morgen come before nicht.","Die Vorsilbe schließt die Klammer, also steht <b>nicht</b> direkt davor. Zeitangaben wie morgen stehen vor nicht."),
 ("<b>nicht</b> stands directly before an adjective or an adverb of manner: nicht groß, nicht gut, nicht schnell.","<b>nicht</b> steht direkt vor einem Adjektiv oder einem Adverb der Art und Weise: nicht groß, nicht gut, nicht schnell."),
 ("nicht before place and direction","nicht vor Ort und Richtung"),
 ("<b>nicht</b> goes before a phrase of place or direction: nicht nach Wien, nicht im Büro.","<b>nicht</b> steht vor einer Orts- oder Richtungsangabe: nicht nach Wien, nicht im Büro."),
 ("To negate one part only, put <b>nicht</b> directly before it and give the correction with <b>sondern</b>.","Verneinst du nur einen Teil, setze <b>nicht</b> direkt davor und korrigiere mit <b>sondern</b>."),
]
for o,n in R:
    assert seg.count(o)==1,("seg",o)
    seg=seg.replace(o,n)
s=s[:a]+seg+s[b:]
W=[("Why does nicht end in -t?","Warum endet nicht auf -t?"),
 ("Old High German niwiht meant 'not a thing' – the same word as English 'not a whit'. It once came with a second ni, like French ne … pas; the little ni fell away and nicht did the whole job. kein is the same idea: ni + ein, 'not one'.","Im Althochdeutschen bedeutete niwiht „nicht ein Ding“ – es ist dasselbe Wort wie englisch „not a whit“. Früher kam noch ein zweites ni dazu, ähnlich wie im Französischen bei ne … pas; das kleine ni fiel weg, und nicht übernahm die ganze Aufgabe. kein folgt derselben Idee: ni + ein, „nicht ein“.")]
for o,n in W:
    assert s.count(o)==1,("why",o)
    s=s.replace(o,n)
import re
m=re.search(r'name="app-version" content="(\d{4}-\d\d-\d\d)([a-z]?)"',s)
new=m.group(1)+chr(ord(m.group(2) or "`")+1)
s=s.replace(m.group(0),'name="app-version" content="%s"'%new)
open(p,"w",encoding="utf-8").write(s); print("OK",new)
