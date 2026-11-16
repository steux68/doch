#!/usr/bin/env python3
"""DOCH: Thema 'Zeitangaben' (zeit), eigene Formulierung."""
from _gt_common import *
C=[
 card("am · um · im",R("Three basic words",["am Montag","am 3. Mai","am Abend","am Wochenende","um acht Uhr","um Mitternacht","im Mai","im Winter","im Jahr 2020"]),"am = day or part of day · um = clock time · im = month, season, year","Use am for days, dates and parts of a day. Use um for exact clock times. Use im for months, seasons and years. Careful with the night: in der Nacht."),
 card("in · an",R("Later, and on special days",["in einer Woche","in drei Tagen","in zwei Stunden","in der Nacht","in den Ferien","an diesem Tag","an Weihnachten"]),"in + time = how long from now","In einer Woche means one week from now. Say in der Nacht. For single days you can also use an: an diesem Tag, an einem Montag."),
 card("seit · vor",R("Since or ago",["Ich wohne seit drei Jahren hier.","Ich bin vor drei Jahren umgezogen.","Seit Montag bin ich krank.","Vor einer Woche war er hier."]),"seit = still going on · vor = in the past, finished","Both take the Dativ. Seit goes with the Präsens (it is still true). Vor goes with the Perfekt or Präteritum (it is over)."),
 card("ab · bis · für",R("Start, end and length",["Ab Montag arbeite ich zu Hause.","Bis Freitag bin ich im Urlaub.","Wir bleiben für zwei Wochen.","Ab nächster Woche","Bis nächsten Monat"]),"ab = from then on · bis = until then · für = for a planned period","Ab takes the Dativ. Bis and für take the Akkusativ. Bis has no article before simple dates: bis Freitag."),
 card("während · innerhalb",R("Gen or Dativ?",["während des Studiums","während der Pause","innerhalb einer Woche","innerhalb von drei Tagen","nach dem Essen","vor dem Frühstück"]),"Both take the Genitiv in careful German","Während means at the same time as. Innerhalb means not later than. Innerhalb von + number is common: innerhalb von drei Tagen. Nach and vor take the Dativ."),
 card("Fragewörter",R("Ask the right question",["Wann kommst du? – Um acht.","Wie lange bleibst du? – Zwei Wochen.","Seit wann wohnst du hier? – Seit 2019.","Bis wann ist offen? – Bis 18 Uhr.","Wie oft gehst du? – Zweimal pro Woche."]),"Each question word matches one kind of answer","Wann asks for a point in time. Wie lange asks for the length. Seit wann asks about the start of something still going on. Bis wann asks for the end."),
 card("Tageszeiten",R("Adverbs of time",["heute Morgen","gestern Abend","heute Nacht","morgen früh","übermorgen","montags","abends","morgens"]),"Capital letter after heute, gestern, morgen","The part of the day after heute or gestern is a noun: heute Morgen, gestern Abend. Words on -s are adverbs and stay small: abends, morgens, montags means every Monday."),
 card("Datum · Uhrzeit",R("Date and clock",["der dritte Mai","am dritten Mai","Viertel nach acht (8:15)","halb acht (7:30)","Viertel vor acht (7:45)","fünf vor zwölf (11:55)","19 Uhr 30 (19:30)"]),"The date is an ordinal number","Say the number as an ordinal: heute ist der dritte Mai, am ersten Januar. In speech halb acht means half an hour before eight, so 7:30. Official times use the 24-hour clock."),
 card("Akkusativ",R("No preposition",["jeden Tag","letzte Woche","letzten Sommer","nächsten Monat","den ganzen Tag","einen Monat lang","jeden Montag"]),"Many time phrases stand in the Akkusativ","With jeder, letzter, nächster, ganz and this group of words you do not need a preposition. The ending is the Akkusativ: jeden Tag, letzten Sommer."),
]
QS=[
 Q("Ich stehe ___ sieben Uhr auf.",["um","am","im"],"Clock time: um sieben Uhr.","A2"),
 Q("Der Kurs beginnt ___ Montag.",["am","um","im"],"Days: am Montag.","A2"),
 Q("Wir fahren ___ Juli nach Italien.",["im","am","um"],"Months: im Juli.","A2"),
 Q("___ Winter ist es in Wien kalt.",["Im","Am","Um"],"Seasons: im Winter.","A2"),
 Q("Ich wohne ___ drei Jahren in Wien.",["seit","vor","für"],"Still going on: seit drei Jahren.","A2"),
 Q("Ich bin ___ drei Jahren nach Wien gezogen.",["vor","seit","in"],"Finished in the past: vor drei Jahren.","A2"),
 Q("___ beginnt der Film? – Um acht.",["Wann","Wie lange","Wie oft"],"Wann asks for a point in time.","A2"),
 Q("Nächsten Sommer bleiben wir ___ zwei Wochen in Graz.",["für","seit","vor"],"für + Akkusativ = a planned period.","A2"),
 Q("Ich warte ___ morgen auf deine Antwort.",["bis","seit","vor"],"bis morgen = until tomorrow.","B1"),
 Q("Ich habe ___ 3. Mai Geburtstag.",["am","im","um"],"Dates: am 3. Mai.","B1"),
 Q("___ einer Woche habe ich Urlaub.",["In","Am","Um"],"in einer Woche = one week from now.","B1"),
 Q("Was machst du ___ Wochenende?",["am","im","um"],"am Wochenende.","B1"),
 Q("___ dauert der Film? – Zwei Stunden.",["Wie lange","Wann","Seit wann"],"Wie lange asks for the length of time.","B1"),
 Q("Es ist 7:30 Uhr. Es ist ___ acht.",["halb","Viertel","fünf"],"halb acht = 7:30.","B1"),
 Q("Es ist 8:15 Uhr. Es ist ___ nach acht.",["Viertel","halb","eine"],"Viertel nach acht = 8:15.","B1"),
 Q("___ Sommer waren wir in Italien.",["Letzten","Letzter","Letzte"],"der Sommer in the Akkusativ: letzten Sommer.","B1"),
 Q("Er trainiert ___ Tag.",["jeden","jeder","jedem"],"Akkusativ: jeden Tag.","B1"),
 Q("___ wann ist das Geschäft geöffnet? – Bis 20 Uhr.",["Bis","Seit","Ab"],"The answer is bis, so the question is bis wann.","B2"),
 Q("Ich bin ___ 1990 geboren.",["im Jahr","in","am"],"im Jahr 1990. Do not say in 1990.","B2"),
 Q("Das Paket kommt ___ von drei Tagen.",["innerhalb","während","seit"],"innerhalb von drei Tagen = in less than three days.","B2"),
 Q("Gestern ___ war ich im Kino.",["Abend","Abends","Abenden"],"gestern Abend: a noun after gestern, with a capital letter.","B2"),
 Q("Sie hat ___ Tag gearbeitet. (ganz)",["den ganzen","der ganze","dem ganzen"],"Akkusativ: den ganzen Tag.","B2"),
 Q("___ des Gesprächs schaute er mehrmals auf die Uhr.",["Während","Seit","Bis"],"Während + Genitiv = at the same time.","C1"),
 Q("Die Antwort kam ___ weniger Minuten.",["innerhalb","seit","bis"],"innerhalb weniger Minuten: Genitiv plural, no von.","C1"),
]
TH=[
 tc("am · um · im",[("am","Montag, 3. Mai, Abend, Wochenende"),("um","acht Uhr, Mitternacht"),("im","Mai, Winter, Jahr 2020"),("in","einer Woche (ab jetzt)")],"Tag und Datum: am. Uhrzeit: um. Monat und Jahreszeit: im."),
 tc("Dauer und Grenzen",[("seit + Dat","drei Jahren (läuft noch)"),("vor + Dat","drei Jahren (vorbei)"),("ab + Dat","Montag (von da an)"),("bis + Akk","Freitag (bis dahin)"),("für + Akk","zwei Wochen (geplant)"),("während + Gen","des Studiums")],"Seit und vor: nicht verwechseln."),
 tc("Fragen",[("Wann?","Um acht."),("Wie lange?","Zwei Stunden."),("Seit wann?","Seit 2019."),("Bis wann?","Bis Freitag."),("Wie oft?","Zweimal pro Woche.")],"Jede Frage hat ihre Art von Antwort."),
]
apply("zeit","Zeitangaben","Präposition","am Tag, um Uhrzeit, im Monat. Seit = läuft noch. Vor = vorbei.",
 '<span><b class="wt k lgk">am · um · im</b> Zeit</span><span><b class="wt v lgk">seit</b> läuft noch</span>',
 C,QS,TH,"pfall",
 ' {t:"zeit",n:"Zeitangaben",tag:"am · um · im · seit · vor",ds:"am, um, im, seit, vor, ab, bis, für, während, Fragewörter, Datum und Uhrzeit · A2–C1"},',
 '{n:"Präpositionen",t:["prep","pfall","vprep"],soon:"Zeitangaben"}',
 '{n:"Präpositionen",t:["prep","pfall","zeit","vprep"]}',
 "Präposition oder Zeitwort")
