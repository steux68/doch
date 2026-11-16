#!/usr/bin/env python3
"""DOCH: Thema 'Indefinitpronomen & Partikeln' (indef), eigene Formulierung."""
from _gt_common import *
C=[
 card("man",R("One, you, people",["Man sagt, dass …","Wie schreibt man das?","Hier darf man nicht rauchen.","Man muss sich anmelden.","Das kann einem passieren.","Das macht einen müde."]),"man = people in general, with er-form of the verb","Man is only Nominativ. For Akkusativ use einen, for Dativ einem. Do not mix it up with der Mann (capital letter, a male person). The possessive is sein: Wenn man seine Karte vergisst, …"),
 card("jemand · niemand",R("Somebody, nobody",["Ist jemand da?","Niemand weiß das.","Ich habe niemandem davon erzählt.","Ich helfe jemandem.","Das ist jemandes Idee."]),"Like a noun, singular, no article","They take the same cases as a person: Dativ jemandem, niemandem. Genitiv jemandes. Akkusativ jemanden or jemand, both are fine. Niemand already means nobody, so do not add nicht."),
 card("etwas · nichts",R("Something, nothing",["Ich brauche etwas Zeit.","Ich möchte etwas Kaltes.","Es gibt nichts Neues.","Das ist nichts Besonderes.","Im Kühlschrank ist nichts.","Alles Gute!"]),"After them, an adjective is a capital neuter noun","etwas Kaltes, nichts Neues, alles Gute: the adjective gets a capital letter and the ending -es (after alles: -e). In speech people often say was instead of etwas: Hast du was gesagt?"),
 card("alle · jeder",R("All and each",["Alle sind da.","Alles ist gut.","Alle Kinder spielen.","Jedes Kind braucht Liebe.","Jeder weiß das.","Das ist alles, was ich weiß."]),"alle = plural · alles = singular things · jeder = one by one","Alle takes the plural verb: alle sind. Alles takes the singular: alles ist gut. Jeder, jede, jedes is singular and works like dieser: jedem Kind, jeden Tag. After alles use the relative word was."),
 card("einige · manche · viele",R("Some, many, few",["einige Leute","manche Menschen","viele neue Bücher","wenige alte Häuser","ein paar Tage","mehrere Möglichkeiten"]),"Plural words for amounts","Einige and mehrere mean a smaller group. Manche means some, but not all. Ein paar never takes an ending. After viele and wenige the adjective gets the ending -e: viele neue Bücher."),
 card("irgend-",R("Any, some, whichever",["irgendwo","irgendwann","irgendwie","irgendjemand","irgendetwas","irgendwelche Fragen"]),"irgend- makes it vague","Use it when you do not know or do not care exactly which one. Irgendwann ruft er an means that he will call at some time. Gibt es irgendwelche Fragen? is the polite plural."),
 card("doch · ja",R("Spoken-style particles",["Das weißt du doch!","Komm doch mal vorbei!","Ich komme ja schon!","Das ist ja toll!","Kommst du nicht? – Doch!"]),"They add attitude, not facts","Doch in a statement means: you know that. In a request it makes an offer friendlier. Ja means as you know, or is a sign of surprise. As an answer to a negative question doch means yes after all."),
 card("mal · eben · halt",R("Spoken-style particles",["Schau mal!","Kannst du mir mal helfen?","Das ist eben so.","Das ist halt so.","Dann nimm eben den Bus."]),"mal softens · eben, halt = that is just how it is","Mal makes a request lighter. Eben and halt both mean that you cannot change it. Halt is typical in Austria and the south, eben is used everywhere. Do not use them in formal writing."),
 card("denn · wohl · eigentlich",R("Spoken-style particles",["Was machst du denn da?","Wo bist du denn?","Er ist wohl krank.","Sie sind wohl schon weg.","Wie spät ist es eigentlich?","Eigentlich wollte ich gehen."]),"denn = interested question · wohl = probably · eigentlich = by the way","Denn is only found in questions. Wohl means probably, you are guessing. Eigentlich can mean by the way, or in truth, or originally. Wohl and eigentlich are also fine in writing."),
]
QS=[
 Q("Wie sagt ___ das auf Deutsch?",["man","Mann","einen"],"man = people in general. Mann is a male person.","A2"),
 Q("Ich habe Hunger, aber im Kühlschrank ist ___ zu essen.",["nichts","niemand","jemand"],"nichts is for things. niemand is for people.","A2"),
 Q("___ Kinder spielen im Garten.",["Alle","Jedes","Jede"],"alle + plural noun. jedes needs a singular noun.","A2"),
 Q("___ Kind braucht Liebe.",["Jedes","Alle","Alles"],"jedes + singular neuter noun.","A2"),
 Q("___ ist in Ordnung.",["Alles","Alle","Allen"],"alles = everything, with the singular verb ist.","A2"),
 Q("Das kann ___ passieren.",["einem","man","einen"],"man has no Dativ. Use einem: Das kann einem passieren.","B1"),
 Q("Ich habe ___ davon erzählt.",["niemandem","niemanden","niemandes"],"erzählen takes the Dativ: niemandem.","B1"),
 Q("Ich möchte etwas ___ trinken. (kalt)",["Kaltes","kaltes","Kalt"],"etwas + capital neuter adjective: etwas Kaltes.","B1"),
 Q("Alles ___ zum Geburtstag!",["Gute","Guten","Gutes"],"The fixed phrase is Alles Gute.","B1"),
 Q("Das ist alles, ___ ich weiß.",["was","das","dass"],"After alles the relative word is was.","B1"),
 Q("Er schenkt ___ Kind ein Buch. (jeder)",["jedem","jedes","jeden"],"schenken takes the Dativ: jedem Kind.","B1"),
 Q("___ Leute mögen keine Pilze.",["Manche","Mancher","Jedes"],"manche + plural noun = some people.","B1"),
 Q("Ich habe nur ___ Freunde hier.",["wenige","wenig","weniger"],"wenige + plural noun = few.","B1"),
 Q("Kommst du nicht mit? – ___, ich komme.",["Doch","Ja","Nein"],"Doch contradicts a negative question.","B1"),
 Q("Schau ___, wie schön das ist! (spoken)",["mal","wohl","denn"],"mal softens a request.","B1"),
 Q("Sie hat viele ___ Bücher. (neu)",["neue","neues","neuem"],"After viele the plural ending is -e.","B2"),
 Q("Gibt es noch ___ Fragen?",["irgendwelche","irgendeine","irgendein"],"The plural form is irgendwelche.","B2"),
 Q("Das weißt du ___! (spoken)",["doch","denn","mal"],"doch in a statement means: you know that.","B2"),
 Q("Was machst du ___ da? (spoken)",["denn","doch","mal"],"denn shows curiosity in a question.","B2"),
 Q("Der Zug hat Verspätung. Das ist ___ so. (spoken)",["halt","denn","mal"],"halt = that is just how it is.","B2"),
 Q("Die Lichter sind aus. Sie sind ___ schon schlafen gegangen.",["wohl","denn","mal"],"wohl = probably.","B2"),
 Q("Warte, ich komme ___ schon! (spoken)",["ja","mal","denn"],"ja = as you know, or a little impatient.","C1"),
 Q("Wie spät ist es ___? (spoken)",["eigentlich","doch","halt"],"eigentlich in a question means by the way.","C1"),
 Q("Das hat ___ von uns gewusst.",["jeder","alle","alles"],"jeder von uns takes a singular verb: hat gewusst.","B2"),
]
TH=[
 tc("man und Co.",[("Nom","man"),("Akk","einen"),("Dat","einem"),("Possessiv","sein"),("jemand, niemand","Dat: jemandem, niemandem")],"Man ist nur Nominativ."),
 tc("Mengen",[("alle","Plural: alle sind da"),("alles","Singular: alles ist gut"),("jeder","Singular, wie dieser"),("manche","einige, nicht alle"),("viele, wenige","Plural, Adjektiv -e"),("ein paar","ohne Endung")],"Nach alles, etwas, nichts: Adjektiv groß, -es."),
 tc("Partikeln (gesprochen)",[("doch","das weißt du doch"),("ja","ich komme ja schon"),("mal","bitte weicher"),("eben, halt","so ist es"),("denn","Frage mit Interesse"),("wohl","vermutlich"),("eigentlich","übrigens, ursprünglich")],"Fast nur im Gespräch. halt: eher Süden, Österreich."),
]
apply("indef","Indefinitpronomen & Partikeln","Stil","man, jemand, etwas, alle, jeder. Particles like doch, mal, halt, denn are spoken style.",
 '<span><b class="wt k lgk">man</b> allgemein</span><span><b class="wt v lgk">doch · mal</b> Partikel</span>',
 C,QS,TH,"nom",
 ' {t:"indef",n:"Indefinitpronomen & Partikeln",tag:"man · jemand · doch · mal",ds:"man, jemand, etwas, alle, jeder, irgend-, Modalpartikeln · A2–C1"},',
 '{n:"Stil · C1",t:["nvv","nom"],soon:"Partikeln"}',
 '{n:"Stil · C1",t:["nvv","nom","indef"]}',
 "Indefinitpronomen oder Partikel")
