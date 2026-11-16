#!/usr/bin/env python3
"""DOCH: neue Gruppe 'Wortschatz & Spaß': Österreichisch (oest), Wortbildung (wortb), Zungenbrecher (zungen), Fehlerjagd (fehler). Eigene Formulierung."""
import re, sys
p="index.html"; s=open(p,encoding="utf-8").read()
if "GT.oest=" in s: sys.exit("already patched")
def J(l): return "["+",".join('"%s"'%x for x in l)+"]"
def Q(sent,o,why,lv): return ' {s:"%s",o:%s,why:"%s",lv:"%s"}'%(sent,J(o),why,lv)
def rows(items): return '<div class="rows">'+"".join('<div><span>%s</span><span>%s</span></div>'%(a,b) for a,b in items)+'</div>'
def tc(h,items,note): return '<div class="tc df"><h3>%s</h3>%s<p class="tline">%s</p></div>'%(h,rows(items),note)
def card(b,st,tx,gt,say=None): return ' {b:"%s",st:%s,tx:"%s",gt:"%s"%s}'%(b,st,tx,gt,(',say:"%s"'%say) if say else "")
def GT(key,name,badge,tip,lg,C,QS,TH): return ('GT.%s={name:"%s",badge:"%s",tip:"%s",src:["duden","grammis","lingolia"],\n lg:\'%s\',\n cards:[\n'%(key,name,badge,tip,lg)+",\n".join(C)+'],\n q:[\n'+",\n".join(QS)+'],\n th:`'+''.join(TH)+'`};\n')
def R(h,l): return 'ruleSt("%s",%s)'%(h,J(l))

# ---------------- Österreichisch ----------------
OE_C=[
 card("Essen",R("Essen und Trinken",["Erdäpfel (Kartoffeln)","Paradeiser (Tomaten)","Karfiol (Blumenkohl)","Marillen (Aprikosen)","Topfen (Quark)","Schlagobers (Schlagsahne)","Faschiertes (Hackfleisch)","Semmel (Brötchen)"]),"Words you hear at the market","These are standard in Austria and appear in shops, menus and newspapers. Germans understand most of them."),
 card("Küche",R("Küche und Süßes",["Palatschinken (Pfannkuchen)","Eierschwammerl (Pfifferlinge)","Ribisel (Johannisbeeren)","Zuckerl (Bonbon)","Kren (Meerrettich)","Jause (Brotzeit)","Staubzucker (Puderzucker)","Fisolen (grüne Bohnen)"]),"More food words","Jause is a small meal or snack in between. In a Beisl or at a Heuriger you will see many of these on the menu."),
 card("Haus",R("Haus und Wohnung",["Sackerl (Tüte)","Stiege (Treppe)","Sessel (Stuhl)","Polster (Kissen)","Kasten (Schrank)","Gehsteig (Bürgersteig)","Mistkübel (Mülleimer)"]),"Things at home and on the street","Stiege and Stiegenhaus are the usual words in Austria. A Kasten is any cupboard or wardrobe."),
 card("Alltag",R("Alltag und Zeit",["Jänner (Januar)","Feber (Februar)","heuer (dieses Jahr)","Trafik (Tabakladen)","Kassa (Kasse)","Packerl (Päckchen)","Leiberl (T-Shirt)","Gewand (Kleidung)"]),"Months, shops and clothes","Jänner is the normal word in Austria. Feber is also correct but you hear it less. heuer means this year."),
 card("Amt",R("Amt, Arzt und Schule",["Meldezettel (Anmeldung beim Amt)","Zahlschein (Überweisungsformular)","Ordination (Arztpraxis)","Krankenstand (Krankschreibung)","Spital (Krankenhaus)","Matura (Abitur)","Hausübung (Hausaufgabe)"]),"Useful for forms and appointments","You need Meldezettel when you move to a new flat. Ordination is the doctor's practice. Matura is the school-leaving exam."),
 card("Bau",R("Bau und Handwerk",["Baubewilligung (Baugenehmigung)","Stiegenhaus (Treppenhaus)","Rauchfang (Schornstein)","Tischler (Schreiner)","Fleischhauer (Metzger)","Rauchfangkehrer (Schornsteinfeger)"]),"Words for your own field","In Austria a building permit is a Baubewilligung. Use this word in emails to the Behörde in Vienna."),
 card("Grammatik",R("Small grammar differences",["Wir sind lange gesessen. (nicht: haben)","Ich bin gestanden. (nicht: habe)","Es ist gelegen. (nicht: hat)","das E-Mail (auch: die E-Mail)"]),"Perfekt with sein, and gender","In Austria and the south, sitzen, stehen and liegen form the Perfekt with sein. In writing for exams, both forms are understood. Pick one and stay with it."),
 card("Gruß",R("Hello and goodbye",["Grüß Gott (Guten Tag)","Servus (Hallo und Tschüss)","Baba (Tschüss, unter Freunden)","Auf Wiederschauen (Auf Wiedersehen)"]),"Greetings","Grüß Gott is polite, Servus is relaxed and works both ways, Baba is only for friends."),
 card("Schweiz",R("Switzerland in four lines",["Velo (Fahrrad)","Trottoir (Gehsteig)","Grüezi (Guten Tag)","Strasse (ohne ß)"]),"Just so you recognise them","Swiss standard German has no ß. You do not need to learn more for Austria or for the exam."),
]
OE_Q=[
 Q("Kartoffel heißt in Österreich meist ___.",["Erdäpfel","Paradeiser","Marillen"],"Erdäpfel = Kartoffeln.","A2"),
 Q("Tomaten nennt man in Österreich ___.",["Paradeiser","Karfiol","Erdäpfel"],"Paradeiser = Tomaten.","A2"),
 Q("Aprikosen heißen in Österreich ___.",["Marillen","Ribisel","Fisolen"],"Marillen = Aprikosen.","A2"),
 Q("Quark heißt in Österreich ___.",["Topfen","Obers","Kren"],"Topfen = Quark.","A2"),
 Q("Schlagsahne heißt in Österreich ___.",["Schlagobers","Topfen","Staubzucker"],"Schlagobers = Schlagsahne.","A2"),
 Q("Zum Frühstück esse ich eine ___. (Brötchen)",["Semmel","Schrippe","Weck"],"Semmel is the Austrian word.","A2"),
 Q("Im Supermarkt brauche ich ein ___. (Tüte)",["Sackerl","Kasten","Polster"],"Sackerl = Tüte.","A2"),
 Q("Der Januar heißt in Österreich ___.",["Jänner","Feber","Heuer"],"Jänner = Januar.","A2"),
 Q("heuer bedeutet ___.",["dieses Jahr","letztes Jahr","nächstes Jahr"],"heuer = dieses Jahr.","A2"),
 Q("Die Treppe heißt in Österreich meist ___.",["Stiege","Sessel","Kasten"],"Stiege = Treppe.","B1"),
 Q("Das Kissen heißt in Österreich ___.",["Polster","Sessel","Gewand"],"Polster = Kissen.","B1"),
 Q("Der Schrank heißt in Österreich oft ___.",["Kasten","Polster","Stiege"],"Kasten = Schrank.","B1"),
 Q("Der Bürgersteig heißt in Österreich ___.",["Gehsteig","Stiege","Trafik"],"Gehsteig = Bürgersteig.","B1"),
 Q("Zigaretten und Zeitungen kauft man in der ___.",["Trafik","Ordination","Kassa"],"Trafik = Tabakladen.","B1"),
 Q("Die Arztpraxis heißt in Österreich oft ___.",["Ordination","Spital","Matura"],"Ordination = Arztpraxis.","B1"),
 Q("Das Krankenhaus heißt in Österreich auch ___.",["Spital","Ordination","Trafik"],"Spital = Krankenhaus.","B1"),
 Q("Das Abitur heißt in Österreich ___.",["Matura","Hausübung","Jause"],"Matura = Abitur.","B1"),
 Q("Hausaufgaben heißen in Österreich ___.",["Hausübungen","Matura","Gewand"],"Hausübung = Hausaufgabe.","B1"),
 Q("Den Metzger nennt man in Österreich meist ___.",["Fleischhauer","Tischler","Rauchfangkehrer"],"Fleischhauer = Metzger.","B1"),
 Q("Für Baugenehmigung sagt man in Österreich ___.",["Baubewilligung","Meldezettel","Zahlschein"],"Baubewilligung = Baugenehmigung.","B2"),
 Q("Bei der Anmeldung in Wien braucht man den ___.",["Meldezettel","Zahlschein","Kasten"],"Meldezettel = Anmeldung beim Amt.","B2"),
 Q("Kleidung heißt in Österreich oft ___.",["Gewand","Polster","Sackerl"],"Gewand = Kleidung.","B2"),
 Q("Wir ___ lange im Café gesessen.",["sind","haben","werden"],"In Austria and the south, sitzen forms the Perfekt with sein.","B2"),
 Q("Zum Abschied sagt man unter Freunden: Servus oder ___.",["Baba","Grüß Gott","Mahlzeit"],"Baba is the friendly goodbye. Grüß Gott is a greeting.","B2"),
]
OE_TH=[
 tc("Essen",[("Erdäpfel","Kartoffeln"),("Paradeiser","Tomaten"),("Marillen","Aprikosen"),("Topfen","Quark"),("Schlagobers","Schlagsahne"),("Semmel","Brötchen")],"Standard Austrian German, not dialect."),
 tc("Alltag",[("Sackerl","Tüte"),("Stiege","Treppe"),("Polster","Kissen"),("Kasten","Schrank"),("Gehsteig","Bürgersteig"),("Jänner","Januar")],"Also: Gewand (Kleidung), heuer (dieses Jahr)."),
 tc("Amt und Bau",[("Meldezettel","Anmeldung"),("Ordination","Arztpraxis"),("Matura","Abitur"),("Baubewilligung","Baugenehmigung")],"Use these in letters and emails in Austria."),
]
OE=GT("oest","Österreichisch","Wort","Learn the Austrian word with the German one: Paradeiser = Tomate.",'<span><b class="wt k lgk">AT</b> Österreich</span>',OE_C,OE_Q,OE_TH)

# ---------------- Wortbildung ----------------
WB_C=[
 card("Komposita",R("Der letzte Teil entscheidet",["der Tisch + die Lampe = die Tischlampe","das Haus + die Tür = die Haustür","das Auto + die Bahn = die Autobahn","das Kind + das Zimmer = das Kinderzimmer"]),"The last word gives the article and the plural","Read a compound from the back: Kinderzimmer is a kind of Zimmer, so it is das Zimmer."),
 card("Fugen",R("Fugenelemente",["Meinung + s + Freiheit","Gesundheit + s + Amt","Wohnung + s + Bau","Blume + n + Vase","Kind + er + Zimmer"]),"Sometimes a letter joins the parts","After -ung, -heit, -keit, -ion, -ität, -schaft, -ling and -tum the joint is almost always -s. Otherwise learn the joint with the word."),
 card("Nomen",R("Endungen und Artikel",["-ung, -heit, -keit, -schaft: die","-ion, -ität: die","-chen, -lein: das","-er, -ling, -ismus: der","-ment: das (mostly)"]),"The ending tells you the article","Exceptions exist: der Zement, der Irrtum, der Reichtum. -tum is usually das (das Eigentum)."),
 card("-heit · -keit",R("Adjektiv → Nomen",["krank → die Krankheit","frei → die Freiheit","freundlich → die Freundlichkeit","möglich → die Möglichkeit","sauber → die Sauberkeit"]),"-keit after -lich, -ig, -bar, -sam, -er","Short adjectives take -heit: Krankheit, Freiheit. After -lich, -ig, -bar and -sam take -keit."),
 card("Adjektiv",R("Endungen und Bedeutung",["wasch-bar (can be washed)","arbeits-los (without)","sinn-voll (full of)","erfolg-reich (rich in)","fehler-haft (with faults)","arbeits-fähig (able to)"]),"-bar · -los · -voll · -reich · -haft · -fähig","-bar says that something can be done. -los means without. -voll and -reich mean with a lot of. Also: -lich, -ig, -isch (sonnig, freundlich, typisch)."),
 card("Verb",R("Vorsilben",["be-arbeiten","ver-kaufen","er-reichen","ent-decken","zer-brechen","miss-verstehen"]),"be- · ver- · er- · ent- · zer- · miss-","These prefixes are not separable and the Partizip has no ge-: Ich habe den Plan bearbeitet. zer- means apart, ent- means away or the start of something."),
 card("-ieren",R("Fremdwörter",["studieren → studiert","renovieren → renoviert","kopieren → kopiert","reparieren → repariert"]),"Verbs in -ieren never take ge-","The Partizip stays without ge-: Er hat Architektur studiert. The same holds for all verbs in -ieren."),
]
WB_Q=[
 Q("Tisch + Lampe = ___ Tischlampe",["die","der","das"],"The last word decides: die Lampe.","A2"),
 Q("Auto + Bahn = ___ Autobahn",["die","der","das"],"The last word decides: die Bahn.","A2"),
 Q("Kind + Zimmer = ___ Kinderzimmer",["das","der","die"],"The last word decides: das Zimmer.","A2"),
 Q("Eine Frau, die lehrt, ist eine Lehrer___.",["in","e","chen"],"-in makes the feminine form: Lehrerin.","A2"),
 Q("Ein kleines Haus ist ein Häus___.",["chen","ung","keit"],"-chen makes a small thing, and the article is das.","A2"),
 Q("Krank___ ist nicht schön.",["heit","keit","ung"],"Short adjective + -heit: die Krankheit.","A2"),
 Q("Die Plan___ des Hauses dauert lange.",["ung","heit","schaft"],"planen → die Planung (-ung makes a noun from a verb).","A2"),
 Q("Wer keine Arbeit hat, ist arbeits___.",["los","voll","frei"],"-los means without: arbeitslos.","A2"),
 Q("Ein Pullover, den man waschen kann, ist wasch___.",["bar","los","sam"],"-bar means can be done: waschbar.","B1"),
 Q("Ein Tag mit viel Sonne ist sonn___.",["ig","lich","isch"],"Sonne + -ig: sonnig.","B1"),
 Q("Wer viel Erfolg hat, ist erfolg___.",["reich","voll","los"],"-reich: rich in. erfolgreich.","B1"),
 Q("freundlich → die Freundlich___",["keit","heit","ung"],"After -lich the noun ends in -keit.","B1"),
 Q("Die Meinung___freiheit ist wichtig.",["s","n","en"],"After -ung the joint is -s: Meinungsfreiheit.","B1"),
 Q("Das Gesundheit___amt hat geöffnet.",["s","n","e"],"After -heit the joint is -s: Gesundheitsamt.","B1"),
 Q("Die Blume___vase steht auf dem Tisch.",["n","s","e"],"Blume + n: Blumenvase.","B1"),
 Q("Das Glas ist ___brochen.",["zer","be","er"],"zer- means apart: zerbrochen.","B1"),
 Q("Er hat das Auto ___kauft.",["ver","be","er"],"verkaufen = sell.","B1"),
 Q("Er hat Architektur ___. (studieren)",["studiert","gestudiert","studieren"],"Verbs in -ieren have no ge- in the Partizip.","B1"),
 Q("Wir haben die Küche ___. (renovieren)",["renoviert","gerenoviert","renovierte"],"Verbs in -ieren have no ge- in the Partizip.","B1"),
 Q("Ich habe den Plan ___. (bearbeiten)",["bearbeitet","gebearbeitet","bearbeiten"],"Inseparable prefix be-: no ge-.","B1"),
 Q("___ Instrument",["das","der","die"],"-ment is usually das.","B2"),
 Q("Er ist krank und nicht arbeits___.",["fähig","bar","los"],"-fähig means able to: arbeitsfähig.","B2"),
 Q("Ein Text voller Fehler ist fehler___.",["haft","reich","voll"],"-haft: with faults. fehlerhaft.","B2"),
 Q("___ Eigentum",["das","der","die"],"-tum is usually das. Exceptions: der Irrtum, der Reichtum.","C1"),
]
WB_TH=[
 tc("Komposita",[("Genus","vom letzten Wort"),("Fuge -s","nach -ung, -heit, -keit, -ion, -ität"),("Fuge -n","Blumenvase"),("Fuge -er","Kinderzimmer")],"Read a compound from the back."),
 tc("Nomen",[("die","-ung, -heit, -keit, -schaft, -ion, -ität"),("das","-chen, -lein, -ment, -tum"),("der","-er, -ling, -ismus")],"Ending → article. Exceptions: der Irrtum, der Reichtum, der Zement."),
 tc("Adjektiv und Verb",[("-bar","kann man: waschbar"),("-los","ohne: arbeitslos"),("-voll, -reich","mit viel: sinnvoll, erfolgreich"),("be- ver- er- ent- zer-","Partizip ohne ge-")],"-ieren verbs also take no ge-."),
]
WB=GT("wortb","Wortbildung","Wort","Read a long word from the back, and look at the ending.",'<span><b class="wt k lgk">-ung</b> Endung</span><span><b class="wt v lgk">ver-</b> Vorsilbe</span>',WB_C,WB_Q,WB_TH)

# ---------------- Zungenbrecher ----------------
ZB_C=[
 card("Fritz",R("Fischers Fritz",["Fischers Fritz fischt frische Fische,","frische Fische fischt Fischers Fritz."]),"f · fr · sch","Slowly first. Press the lower lip lightly against the upper teeth for f.","Fischers Fritz fischt frische Fische, frische Fische fischt Fischers Fritz."),
 card("Blaukraut",R("Blaukraut",["Blaukraut bleibt Blaukraut","und Brautkleid bleibt Brautkleid."]),"bl · br · kl","The r is the hard part. Keep it short and relaxed.","Blaukraut bleibt Blaukraut und Brautkleid bleibt Brautkleid."),
 card("Zwetschgen",R("Zwetschgen",["Zwischen zwei Zwetschgenzweigen","zwitschern zwei Schwalben."]),"zw · tsch · schw","z is pronounced ts. In Austria the plum is a Zwetschke.","Zwischen zwei Zwetschgenzweigen zwitschern zwei Schwalben."),
 card("Ameisen",R("Ameisen",["Acht alte Ameisen aßen Ananas am Abend."]),"A-Laute","Open the mouth wide for every a. Short a and long a alternate.","Acht alte Ameisen aßen Ananas am Abend."),
 card("Wiener",R("Wiener Waschweiber",["Wir Wiener Waschweiber wollten weiße Wäsche waschen,","wenn wir wüssten, wo warmes Wasser wäre."]),"w (wie v)","German w is like English v. Do not use the English w.","Wir Wiener Waschweiber wollten weiße Wäsche waschen, wenn wir wüssten, wo warmes Wasser wäre."),
 card("Hemden",R("Hermanns Hemden",["Hinter Hermann Hannes Haus","hängen hundert Hemden raus."]),"h","Breathe out softly for h. Do not drop it and do not press it.","Hinter Hermann Hannes Haus hängen hundert Hemden raus."),
 card("Ziegen",R("Zehn zahme Ziegen",["Zehn zahme Ziegen zogen zehn Zentner Zucker zum Zoo."]),"z (ts)","Start every z with t-s in one movement.","Zehn zahme Ziegen zogen zehn Zentner Zucker zum Zoo."),
 card("Dachdecker",R("Der dicke Dachdecker",["Der dicke Dachdecker deckte dir dein Dach."]),"d · ch","Clear d at the front of the tongue, and the ch after a stays soft.","Der dicke Dachdecker deckte dir dein Dach."),
 card("Klapper",R("Klapperschlangen",["Es klapperten die Klapperschlangen,","bis ihre Klappern schlapper klangen."]),"kl · schl","The hardest one. Say kl-kl-kl, then add schl.","Es klapperten die Klapperschlangen, bis ihre Klappern schlapper klangen."),
]
ZB_Q=[
 Q("Fischers Fritz fischt frische ___.",["Fische","Frösche","Fliegen"],"Fischers Fritz fischt frische Fische.","A2"),
 Q("Blaukraut bleibt Blaukraut und Brautkleid bleibt ___.",["Brautkleid","Blaukraut","Brautkraut"],"Blaukraut bleibt Blaukraut und Brautkleid bleibt Brautkleid.","A2"),
 Q("Zwischen zwei Zwetschgenzweigen zwitschern zwei ___.",["Schwalben","Spatzen","Amseln"],"Zwischen zwei Zwetschgenzweigen zwitschern zwei Schwalben.","B1"),
 Q("Acht alte Ameisen aßen ___ am Abend.",["Ananas","Äpfel","Aprikosen"],"Acht alte Ameisen aßen Ananas am Abend.","A2"),
 Q("Wir Wiener Waschweiber wollten weiße ___ waschen.",["Wäsche","Wolle","Westen"],"Wir Wiener Waschweiber wollten weiße Wäsche waschen.","B1"),
 Q("Hinter Hermann Hannes Haus hängen hundert ___ raus.",["Hemden","Hosen","Hüte"],"Hinter Hermann Hannes Haus hängen hundert Hemden raus.","A2"),
 Q("Zehn zahme Ziegen zogen zehn Zentner ___ zum Zoo.",["Zucker","Zwiebeln","Ziegel"],"Zehn zahme Ziegen zogen zehn Zentner Zucker zum Zoo.","A2"),
 Q("Der dicke Dachdecker deckte dir dein ___.",["Dach","Haus","Fach"],"Der dicke Dachdecker deckte dir dein Dach.","A2"),
 Q("Es klapperten die Klapperschlangen, bis ihre ___ schlapper klangen.",["Klappern","Schuppen","Rasseln"],"…bis ihre Klappern schlapper klangen.","B2"),
 Q("Im Satz „Zehn zahme Ziegen“ übst du den Laut ___.",["z","sch","w"],"The letter z is pronounced ts.","A2"),
 Q("Im Satz „Wiener Waschweiber“ klingt w wie ___.",["v","w","f"],"German w sounds like English v.","B1"),
 Q("Im Wort „Zwetschge“ steht am Anfang der Laut ___.",["zw","sch","tsch"],"Zw is pronounced tsv.","B2"),
]
ZB_TH=[
 tc("Laute",[("f, fr","Fischers Fritz"),("bl, br","Blaukraut"),("z","Zehn zahme Ziegen"),("w","Wiener Waschweiber"),("h","Hermanns Hemden"),("kl, schl","Klapperschlangen")],"Tap Anhören in Lernen and say each one after the voice."),
 tc("So übst du",[("1","langsam, jedes Wort deutlich"),("2","drei Mal ohne Fehler"),("3","schneller, ohne den Laut zu verlieren")],"Speed comes last."),
]
ZB=GT("zungen","Zungenbrecher","Laut","Say it slowly first. Speed comes last.",'<span><b class="wt k lgk">z</b> Laut</span>',ZB_C,ZB_Q,ZB_TH)

# ---------------- Fehlerjagd ----------------
FJ=[
 ("Ich habe gestern nach Hause gegangen.",["habe … gegangen","gestern","nach Hause"],"gehen forms the Perfekt with sein: Ich bin gestern nach Hause gegangen.","A2"),
 ("Wir fahren mit den Bus zur Arbeit.",["mit den Bus","Wir fahren","zur Arbeit"],"mit + Dativ: mit dem Bus.","A2"),
 ("Ich bin müde, weil ich habe schlecht geschlafen.",["weil ich habe","Ich bin müde","schlecht geschlafen"],"After weil the verb goes last: weil ich schlecht geschlafen habe.","A2"),
 ("Gestern ich habe einen Film gesehen.",["Gestern ich habe","einen Film","gesehen"],"The verb stays in position 2: Gestern habe ich einen Film gesehen.","A2"),
 ("Ich danke dir für dein Einladung.",["für dein Einladung","Ich danke","dir"],"die Einladung is feminine, so: für deine Einladung.","A2"),
 ("Sie hat ein schönen Mantel gekauft.",["ein schönen Mantel","Sie hat","gekauft"],"Akkusativ masculine: einen schönen Mantel.","A2"),
 ("Die Kinder spielen in der Garten.",["in der Garten","Die Kinder","spielen"],"der Garten is masculine, Dativ: in dem Garten = im Garten.","A2"),
 ("Ich möchte gern ein Kaffee trinken.",["ein Kaffee","Ich möchte gern","trinken"],"Akkusativ masculine: einen Kaffee.","A2"),
 ("Er fragt mich, ob kommst du heute mit.",["ob kommst du","Er fragt mich","heute mit"],"In the Nebensatz the verb goes last: ob du heute mitkommst.","B1"),
 ("Ich warte seit zwei Stunden für den Bus.",["für den Bus","seit zwei Stunden","Ich warte"],"warten auf + Akkusativ: auf den Bus.","B1"),
 ("Obwohl es regnet, wir gehen spazieren.",["wir gehen","Obwohl es regnet","spazieren"],"After a Nebensatz the main verb comes first: gehen wir spazieren.","B1"),
 ("Ich interessiere mich an Architektur.",["an Architektur","Ich interessiere","mich"],"sich interessieren für: für Architektur.","B1"),
 ("Ich habe mich die Hände gewaschen.",["mich die Hände","Ich habe","gewaschen"],"With another Akkusativ object the pronoun is Dativ: mir die Hände.","B1"),
 ("Das ist die Frau, die ich gestern geholfen habe.",["die ich gestern","Das ist die Frau","geholfen habe"],"helfen + Dativ: die Frau, der ich geholfen habe.","B1"),
 ("Ich habe gestern vergessen, dir anzurufen.",["dir anzurufen","Ich habe","gestern vergessen"],"anrufen + Akkusativ: dich anzurufen.","B1"),
 ("Sie arbeitet als eine Architektin in Wien.",["als eine Architektin","Sie arbeitet","in Wien"],"For jobs, als has no article: als Architektin.","B1"),
 ("Er hat gestern lange arbeiten gemusst.",["arbeiten gemusst","Er hat","gestern lange"],"Modal verb in the Perfekt: hat arbeiten müssen (double infinitive).","B2"),
 ("Wegen dem schlechten Wetter bleiben wir zu Hause.",["Wegen dem schlechten Wetter","bleiben wir","zu Hause"],"Standard written German: wegen + Genitiv, wegen des schlechten Wetters. The Dativ is common in speech.","B2"),
 ("Sie hat ihrem Bruder ein Buch geschenkt, dass sie gestern gekauft hat.",["dass sie gestern gekauft hat","Sie hat ihrem Bruder","ein Buch geschenkt"],"A relative clause needs das, not dass: ein Buch, das sie gekauft hat.","B2"),
 ("Je mehr ich übe, umso ich werde besser.",["umso ich werde","Je mehr ich übe","besser"],"After je … umso the verb stays in position 2: umso besser werde ich.","B2"),
 ("Man soll nicht vergessen, dass die Regeln ändern sich.",["dass die Regeln","Man soll nicht vergessen","ändern sich"],"After dass the verb goes last: dass sich die Regeln ändern.","B2"),
 ("Das Projekt, dessen die Planung lange dauerte, wurde genehmigt.",["dessen die Planung","Das Projekt","wurde genehmigt"],"The relative pronoun dessen replaces the article: dessen Planung.","C1"),
 ("Er bestand darauf, dass das Treffen wird stattfinden.",["wird stattfinden","Er bestand darauf","dass das Treffen"],"In the Nebensatz the finite verb is last: dass das Treffen stattfinden wird.","C1"),
 ("Ich hätte das früher gewusst, wenn du mir hättest gesagt.",["hättest gesagt","Ich hätte das früher gewusst","wenn du mir"],"The finite verb goes last: wenn du es mir gesagt hättest.","C1"),
]
FJ_Q=[Q(a,b,c,d) for a,b,c,d in FJ]
FJ_TH=[
 tc("Wo suchst du?",[("Verb","Position 2, oder am Ende im Nebensatz"),("Fall","mit + Dativ, für + Akkusativ, helfen + Dativ"),("Artikel","der, die, das und die Endung"),("Hilfsverb","sein oder haben im Perfekt")],"Check these four first. One of them is almost always the mistake."),
]
FE=GT("fehler","Fehlerjagd","Fehler: tippe die falsche Stelle","Check the verb position first, then the case, then the article.",'<span><b class="wt k lgk">!</b> Fehler</span>',[
 card("Verb",R("Verb am falschen Platz",["Gestern ich habe einen Film gesehen. ✗","Gestern habe ich einen Film gesehen. ✓"]),"Position 2","In a main clause the finite verb is the second element. After a Nebensatz it comes first."),
 card("Fall",R("Falscher Fall",["mit den Bus ✗ · mit dem Bus ✓","für dem Chef ✗ · für den Chef ✓","Ich helfe ihn ✗ · Ich helfe ihm ✓"]),"mit + Dativ · für + Akkusativ · helfen + Dativ","Learn the case together with the preposition or the verb."),
 card("Artikel",R("Falscher Artikel",["ein Kaffee ✗ · einen Kaffee ✓","in der Garten ✗ · im Garten ✓","dein Einladung ✗ · deine Einladung ✓"]),"Genus and Fall","Check the gender of the noun, then the case."),
 card("Nebensatz",R("Nebensatz",["weil ich habe Zeit ✗ · weil ich Zeit habe ✓","ob kommst du ✗ · ob du kommst ✓"]),"The verb goes last","After weil, dass, ob, wenn, obwohl the conjugated verb is the last word."),
 card("Hilfsverb",R("sein oder haben",["Ich habe gegangen ✗ · Ich bin gegangen ✓","Er hat angekommen ✗ · Er ist angekommen ✓"]),"Movement and change take sein","gehen, fahren, kommen, ankommen, einschlafen all form the Perfekt with sein."),
],FJ_Q,FJ_TH)

# ---------------- einbauen ----------------
a='/* ---------- topics + home ---------- */'
if s.count(a)!=1: sys.exit("Anker topics")
s=s.replace(a,"/* wortschatz */\n"+OE+WB+ZB+FE+a)
a=' {t:"k1",'
i=s.find(a); assert i>0
j=s.index("\n",i)+1
s=s[:j]+(' {t:"oest",n:"Österreichisch",tag:"Paradeiser · Sackerl",ds:"Wörter und kleine Unterschiede, Amt und Bau · A2–B2"},\n'
 ' {t:"wortb",n:"Wortbildung",tag:"-ung · -bar · ver-",ds:"Komposita, Endungen, Vorsilben, Artikel erkennen · A2–C1"},\n'
 ' {t:"zungen",n:"Zungenbrecher",tag:"Fischers Fritz",ds:"Laute üben mit Anhören · A2–B2"},\n'
 ' {t:"fehler",n:"Fehlerjagd",tag:"Wo ist der Fehler?",ds:"die falsche Stelle im Satz finden · A2–C1"},\n')+s[j:]
a='{n:"Stil · C1",t:["nvv","nom"],soon:"Partikeln"}'
if s.count(a)!=1: sys.exit("Anker Gruppe")
s=s.replace(a,a[:-1]+'},\n {n:"Wortschatz & Spaß",t:["oest","wortb","zungen","fehler"]}')
a='if(k==="art")return "Artikel";'
if s.count(a)!=1: sys.exit("Anker lab")
s=s.replace(a,a+'if(k==="oest")return "Österreichisches Wort";if(k==="wortb")return "Endung, Vorsilbe oder Artikel";if(k==="zungen")return "Welches Wort?";if(k==="fehler")return "Wo steckt der Fehler? Tippe die falsche Stelle.";')
m=re.search(r'name="app-version" content="(\d{4}-\d\d-\d\d)([a-z]?)"',s)
new=m.group(1)+chr(ord(m.group(2) or "`")+1)
s=s.replace(m.group(0),'name="app-version" content="%s"'%new)
open(p,"w",encoding="utf-8").write(s); print("OK",new)
