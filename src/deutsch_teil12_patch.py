#!/usr/bin/env python3
"""DOCH: 'Lernen auf Deutsch' Teil 12 - letzte Reste (Satzbau-Notizen, why, Theorie)."""
import re
p="index.html"; s=open(p,encoding="utf-8").read()
R=[
("English keeps “I” before the verb. German keeps the verb second, so “ich” moves behind it.","Im Englischen bleibt „I“ vor dem Verb. Im Deutschen bleibt das Verb an zweiter Stelle, also rückt „ich“ dahinter."),
("The whole weil-clause fills the Vorfeld, so the verb comes straight after the comma.","Der ganze weil-Satz füllt das Vorfeld, also folgt das Verb direkt nach dem Komma."),
("fragen + Akkusativ. Akkusativ of sie is sie.","fragen + Akkusativ. Der Akkusativ von sie ist sie."),
("jemanden an etwas erinnern: the person is Akkusativ.","jemanden an etwas erinnern: Die Person steht im Akkusativ."),
("zeigen: dir is the DAT person, the thing shown is AKK.","zeigen: dir ist die Person im Dativ, das Gezeigte steht im Akkusativ."),
("jemanden um etwas bitten: the person is Akkusativ.","jemanden um etwas bitten: Die Person steht im Akkusativ."),
("Owner er → sein. Fahrrad is neuter in the Akkusativ: no ending.","Besitzer er → sein. Fahrrad ist im Akkusativ ein Neutrum: keine Endung."),
("After der, die, das: only -e or -en","Nach der, die, das: nur -e oder -en"),
("Der Architekt zeigt dem Kunden den Plan. Ask the verb: Wer? Wem? Was? Then pick the article by gender.","Der Architekt zeigt dem Kunden den Plan. Frage das Verb: Wer? Wem? Was? Dann wähle den Artikel nach dem Genus."),
("masculine and neuter nouns add -s or -es: des Hauses, des Mannes","maskuline und neutrale Nomen bekommen -s oder -es: des Hauses, des Mannes"),
("Purpose with a different subject: damit.","Zweck mit einem anderen Subjekt: damit."),
("Dem Patienten wird geholfen. · Hier wird gearbeitet. · Es wird getanzt. The verb is always singular.","Dem Patienten wird geholfen. · Hier wird gearbeitet. · Es wird getanzt. Das Verb steht immer im Singular."),
("Direct object: Wen oder was?","Akkusativobjekt: Wen oder was?"),
("One short sentence beats a list","Ein kurzer Satz schlägt eine Liste"),
("Say the sentence aloud and change the noun: mit dem Bus, mit der Bahn, mit dem Auto.","Sprich den Satz laut und tausche das Nomen aus: mit dem Bus, mit der Bahn, mit dem Auto."),
("nachdem + Plusquamperfekt before the Präteritum: gegessen hatte.","nachdem + Plusquamperfekt vor dem Präteritum: gegessen hatte."),
("The answer is bis, so the question is bis wann.","Die Antwort ist bis, also lautet die Frage bis wann."),
("je … desto: the more A, the more B.","je … desto: Je mehr A, desto mehr B."),
(". The part you stress moves back or to the front.",". Der betonte Teil rückt nach hinten oder nach vorn."),
("man takes the er-form: man darf.","man nimmt die er-Form: man darf."),
("Refers to the whole clause: was.","Bezieht sich auf den ganzen Satz: was."),
("wer …, der …: der is the subject of braucht.","wer …, der …: der ist das Subjekt von braucht."),
("The second clause needs a subject: der (wem only belongs to gefällt).","Der zweite Satz braucht ein Subjekt: der (wem gehört nur zu gefällt)."),
]
miss=0
for o,n in R:
    c=s.count(o)
    if c==0: print("MISS",o[:60]); miss+=1; continue
    s=s.replace(o,n)
if miss==len(R): raise SystemExit("already patched")
s,c=re.subn(r'(<meta name="app-version" content="2026-11-24)([a-z])(")',lambda m:m.group(1)+chr(ord(m.group(2))+1)+m.group(3),s,count=1); assert c==1
open(p,"w",encoding="utf-8").write(s); print("ok",len(R)-miss)
# Hinweis: weitere 10 Einzelsätze wurden danach direkt ersetzt (gefallen, Pronomen, n-Nomen, da, von, w, dessen).
