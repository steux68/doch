#!/usr/bin/env python3
"""DOCH: Thema 'Präteritum & Futur' (praet), eigene Formulierung."""
import re, sys
p="index.html"; s=open(p,encoding="utf-8").read()
if "GT.praet=" in s: sys.exit("already patched")
def J(l): return "["+",".join('"%s"'%x for x in l)+"]"
def Q(sent,o,why,lv): return ' {s:"%s",o:%s,why:"%s",lv:"%s"}'%(sent,J(o),why,lv)
def rows(items): return '<div class="rows">'+"".join('<div><span>%s</span><span>%s</span></div>'%(a,b) for a,b in items)+'</div>'
def tc(h,items,note): return '<div class="tc df"><h3>%s</h3>%s<p class="tline">%s</p></div>'%(h,rows(items),note)
def card(b,st,tx,gt): return ' {b:"%s",st:%s,tx:"%s",gt:"%s"}'%(b,st,tx,gt)
def R(h,l): return 'ruleSt("%s",%s)'%(h,J(l))
C=[
 card("Regelmäßig",R("Stem + -te",["ich machte","du machtest","er machte","wir machten","ihr machtet","sie machten"]),"Regular verbs: stem + -te + ending","With stems in -t or -d, or after a consonant + m or n, add an -e: arbeitete, redete, öffnete, atmete."),
 card("Unregelmäßig",R("The vowel changes",["gehen – ging","kommen – kam","sehen – sah","geben – gab","finden – fand","schreiben – schrieb","bleiben – blieb","essen – aß"]),"Strong verbs: new vowel, no -te","Ich ging, er ging: no ending in the first and third person singular. Wir gingen. Always learn three forms: gehen – ging – gegangen."),
 card("Mischverben",R("Vowel change and -te",["denken – dachte","bringen – brachte","kennen – kannte","wissen – wusste","nennen – nannte","rennen – rannte"]),"Both changes at once","These verbs change the vowel and also take -te. There are only a few, so learn them as a group."),
 card("Modal · sein · haben",R("Often used in speech",["können – konnte","müssen – musste","dürfen – durfte","wollen – wollte","sollen – sollte","sein – war","haben – hatte"]),"The Präteritum is normal here, even in conversation","Ich war müde. Ich hatte keine Zeit. Ich konnte nicht kommen. Modal verbs lose the umlaut: können → konnte, müssen → musste."),
 card("Trennbar",R("Prefix at the end",["Er stand um sieben auf.","Sie rief mich gestern an.","Wir kamen spät an.","Weil er um sieben aufstand, …"]),"Main clause: prefix last. Nebensatz: one word again","The prefix goes to the end of the main clause. In a Nebensatz verb and prefix join and the verb goes last."),
 card("Perfekt oder Präteritum",R("Which one?",["Im Gespräch: Ich habe ihn gesehen.","In einer Geschichte: Ich sah ihn.","In einem Bericht: Er kam um acht an.","Immer üblich: war, hatte, konnte, musste"]),"Speaking → Perfekt. Writing a story or report → Präteritum","In speech, and especially in the south, people prefer the Perfekt. Written narrative uses the Präteritum. The meaning is the same."),
 card("Futur",R("werden + Infinitiv",["Ich werde nach Wien ziehen.","Es wird morgen regnen.","Er wird wohl krank sein. (guess)","Du wirst jetzt aufräumen! (order)","Morgen rufe ich dich an. (Präsens)"]),"Futur I is not the only way to talk about the future","Everyday future is often the Präsens with a time word: Morgen rufe ich dich an. Futur I also expresses a guess or a strong order. Futur II: Er wird schon angekommen sein."),
]
QS=[
 Q("Ich ___ gestern zu Hause. (sein)",["war","wurde","hatte"],"sein → war.","A2"),
 Q("Wir ___ gestern ins Kino. (gehen)",["gingen","gehten","gangen"],"gehen – ging – gegangen. Plural: wir gingen.","A2"),
 Q("Er ___ gestern ein Buch. (lesen)",["las","lesete","liest"],"lesen – las – gelesen.","A2"),
 Q("Ich ___ gestern Fußball. (spielen)",["spielte","spielete","spielt"],"Regular verb: stem + -te.","A2"),
 Q("Gestern ___ wir lange auf den Bus. (warten)",["warteten","wartten","warten"],"Stem in -t: add -e: wartete, warteten.","A2"),
 Q("Gestern ___ er zum Bahnhof. (laufen)",["lief","laufte","lauf"],"laufen – lief – gelaufen.","A2"),
 Q("Wir ___ gestern Pizza. (essen)",["aßen","essten","aßt"],"essen – aß – gegessen. Plural: wir aßen.","A2"),
 Q("Du ___ gestern sehr müde. (sein)",["warst","bist","wart"],"du warst.","A2"),
 Q("Ich ___ ihn gestern in der Stadt. (sehen)",["sah","sehte","gesehen"],"sehen – sah – gesehen.","B1"),
 Q("Er ___ gestern nicht kommen. (können)",["konnte","könnte","kannte"],"Modal: können → konnte, without the umlaut.","B1"),
 Q("Früher ___ ich nicht lange aufbleiben. (dürfen)",["durfte","dürfte","darfte"],"dürfen → durfte, without the umlaut.","B1"),
 Q("Er ___ gestern lange arbeiten. (müssen)",["musste","müsste","gemusst"],"müssen → musste. müsste is Konjunktiv II.","B1"),
 Q("Gestern ___ er die Tür. (öffnen)",["öffnete","öffnte","öffnet"],"Stem ends in -n after a consonant: add -e: öffnete.","B1"),
 Q("Er ___ um sieben auf. (aufstehen)",["stand","aufstand","stehte"],"Präteritum of stehen is stand. The prefix auf goes to the end.","B1"),
 Q("Ich ___ gestern lange darüber nach. (nachdenken)",["dachte","denkte","gedacht"],"Mixed verb: denken – dachte – gedacht.","B1"),
 Q("Gestern ___ er mir das Buch. (bringen)",["brachte","bringte","brang"],"Mixed verb: bringen – brachte – gebracht.","B1"),
 Q("Ich ___ nicht, dass er krank war. (wissen)",["wusste","wisste","weiß"],"Mixed verb: wissen – wusste – gewusst.","B1"),
 Q("Beim Erzählen im Gespräch sagt man oft: Ich ___ ihn gestern gesehen.",["habe","hatte","war"],"In speech the Perfekt is usual: ich habe gesehen.","B1"),
 Q("Morgen ___ es regnen. (werden)",["wird","wirst","werden"],"Futur I: es wird + Infinitiv.","A2"),
 Q("Ich ___ nächstes Jahr nach Wien ziehen. (werden)",["werde","wirde","würde"],"Futur I: ich werde + Infinitiv.","B1"),
 Q("Er ist nicht da. Er ___ wohl krank sein. (werden)",["wird","ist","wurde"],"Futur I can express a guess: er wird wohl krank sein.","B2"),
 Q("Morgen ___ ich dich an. (anrufen)",["rufe","anrufe","rufte"],"The future is often the Präsens with a time word. The prefix an goes to the end.","B1"),
 Q("Du ___ jetzt sofort aufräumen! (werden)",["wirst","wurdest","würdest"],"Futur I can be a strong order.","C1"),
 Q("Er ___ den Weg gut. (kennen)",["kannte","kennte","konnte"],"Mixed verb: kennen – kannte – gekannt.","B2"),
]
TH=[
 tc("Endungen",[("ich","– oder -te"),("du","-st oder -test"),("er, sie, es","– oder -te"),("wir","-en oder -ten"),("ihr","-t oder -tet"),("sie, Sie","-en oder -ten")],"Strong verbs: no ending in ich and er. Regular verbs: -te before the ending."),
 tc("Wichtige Verben",[("sein","war"),("haben","hatte"),("werden","wurde"),("können","konnte"),("müssen","musste"),("wissen","wusste"),("denken","dachte"),("bringen","brachte")],"Lerne drei Formen: Infinitiv, Präteritum, Partizip II."),
 tc("Futur",[("Futur I","werde + Infinitiv"),("Vermutung","Er wird wohl krank sein."),("Befehl","Du wirst jetzt aufräumen!"),("Futur II","Er wird schon angekommen sein.")],"Im Alltag reicht oft das Präsens mit Zeitangabe."),
]
LG='<span><b class="wt v lgk">ging</b> Präteritum</span><span><b class="wt k lgk">wird</b> Futur</span>'
BL=('GT.praet={name:"Präteritum & Futur",badge:"Zeitform",tip:"Regular: stem + -te. Strong verbs change the vowel. Future: werden + Infinitiv.",src:["duden","grammis","lingolia"],\n'
 ' lg:\'%s\',\n cards:[\n'%LG+",\n".join(C)+'],\n q:[\n'+",\n".join(QS)+'],\n th:`'+"".join(TH)+'`};\n')
a='/* ---------- topics + home ---------- */'
if s.count(a)!=1: sys.exit("Anker topics")
s=s.replace(a,"/* praet */\n"+BL+a)
a=' {t:"perf",'
i=s.find(a); assert i>0
j=s.index("\n",i)+1
s=s[:j]+' {t:"praet",n:"Präteritum & Futur",tag:"ging · wird gehen",ds:"Formen, Mischverben, Modal, Perfekt oder Präteritum, Futur · A2–C1"},\n'+s[j:]
a='{n:"Verb",t:["praes","refl","modal","perf","pass","k2","k1"],soon:"Präteritum · Futur"}'
if s.count(a)!=1: sys.exit("Anker Verb")
s=s.replace(a,'{n:"Verb",t:["praes","refl","modal","perf","praet","pass","k2","k1"]}')
a='if(k==="lang")return'
if s.count(a)!=1: sys.exit("Anker lab")
s=s.replace(a,'if(k==="praet")return "Verbform im Präteritum oder Futur";'+a)
m=re.search(r'name="app-version" content="(\d{4}-\d\d-\d\d)([a-z]?)"',s)
s=s.replace(m.group(0),'name="app-version" content="%s%s"'%(m.group(1),chr(ord(m.group(2) or "`")+1)))
open(p,"w",encoding="utf-8").write(s); print("OK")
