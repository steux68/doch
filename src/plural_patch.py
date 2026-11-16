#!/usr/bin/env python3
"""DOCH: Thema 'Plural & n-Deklination' (plural), eigene Formulierung."""
from _gt_common import *
C=[
 card("-e · -¨e",R("Often for masculine nouns",["der Hund → die Hunde","der Tisch → die Tische","der Stuhl → die Stühle","die Stadt → die Städte","der Arzt → die Ärzte","die Hand → die Hände"]),"Ending -e, often with an umlaut","Many masculine nouns and a few feminine ones take -e. If the vowel is a, o or u, it often gets an umlaut. There is no safe rule, so learn the plural with the noun."),
 card("-er",R("Mostly neuter",["das Kind → die Kinder","das Haus → die Häuser","das Buch → die Bücher","das Bild → die Bilder","das Land → die Länder","der Mann → die Männer"]),"Ending -er, with an umlaut when possible","This group is mostly neuter, plus a few masculine nouns like Mann. The vowels a, o, u always get an umlaut here."),
 card("-(e)n",R("Mostly feminine",["die Frau → die Frauen","die Lampe → die Lampen","die Zeitung → die Zeitungen","die Wohnung → die Wohnungen","die Universität → die Universitäten","die Freundin → die Freundinnen"]),"Ending -n or -en, never an umlaut","Most feminine nouns take -(e)n. Nouns on -in double the n: Freundin → Freundinnen."),
 card("-s · ohne Endung",R("Two small groups",["das Auto → die Autos","das Hotel → die Hotels","das Handy → die Handys","der Lehrer → die Lehrer","das Zimmer → die Zimmer","das Mädchen → die Mädchen","der Vater → die Väter","der Garten → die Gärten"]),"-s for newer and foreign words, no ending for -er, -el, -en","The -s plural is typical for words from other languages. Nouns on -er, -el, -en and the diminutives -chen and -lein have no ending. A few get an umlaut: Vater → Väter."),
 card("Genus-Tipps",R("Gender gives a hint",["-ung → die Zeitungen","-heit, -keit → die Freiheiten","-schaft → die Freundschaften","-ion → die Nationen","-ismus → -ismen","-um → -en: das Museum → die Museen"]),"Feminine → -(e)n, nearly always","Feminine nouns on -ung, -heit, -keit, -schaft, -ion and -ität take -(e)n. Latin nouns on -um often change to -en: das Zentrum → die Zentren."),
 card("n-Deklination",R("-n in every case except Nominativ",["der Student → den Studenten","der Kollege → dem Kollegen","der Junge → des Jungen","der Mensch → den Menschen","der Nachbar → dem Nachbarn","der Held → den Helden","der Kunde → den Kunden","der Herr → den Herrn"]),"A small group of masculine nouns","These nouns end in -(e)n in Akkusativ, Dativ and Genitiv, singular and plural. Most are people or animals: nouns on -e (Kollege), -ent, -ist, -ant (Student, Tourist, Praktikant) and a few single words."),
 card("Sonderfälle",R("Genitive with -ns",["der Name → des Namens","der Buchstabe → des Buchstabens","der Gedanke → des Gedankens","das Herz → des Herzens","der Name → den Namen"]),"A few n-nouns have -ns in the Genitiv","The few words with -ns in the Genitiv are used often. Akkusativ and Dativ are normal: den Namen, dem Namen. The word das Herz is neuter but works the same way."),
 card("Nur Plural · nur Singular",R("No partner form",["die Leute (plural only)","die Eltern (plural only)","die Ferien (plural only)","die Kosten (plural only)","das Gepäck (singular only)","das Obst (singular only)"]),"Some nouns exist in one number only","You say: viele Leute, but not eine Leute. Use a quantity word with singular nouns: viel Gepäck, ein Stück Obst."),
 card("Komposita",R("The last part decides",["der Apfelbaum → die Apfelbäume","das Wohnzimmer → die Wohnzimmer","die Haustür → die Haustüren","der Bahnhof → die Bahnhöfe"]),"Plural of a compound = plural of its last word","Look only at the last part. Baum → Bäume, so Apfelbaum → Apfelbäume. The first part stays the same."),
]
QS=[
 Q("Auf dem Tisch liegen zwei ___. (Buch)",["Bücher","Büchen","Büchers"],"Buch → Bücher. Plural -er with an umlaut.","A2"),
 Q("In dieser Stadt gibt es drei ___. (Hotel)",["Hotels","Hotele","Hoteln"],"Words from other languages often take -s: Hotels.","A2"),
 Q("Die ___ spielen im Garten. (Kind)",["Kinder","Kinde","Kinden"],"Kind → Kinder.","A2"),
 Q("In meiner Familie gibt es zwei ___. (Bruder)",["Brüder","Brüdern","Bruders"],"Bruder → Brüder. No ending, but an umlaut.","A2"),
 Q("Die ___ in diesem Haus sind sehr teuer. (Wohnung)",["Wohnungen","Wohnunge","Wohnungs"],"Feminine nouns on -ung take -en.","A2"),
 Q("Viele ___ sprechen hier Englisch. (Mensch)",["Menschen","Mensche","Menschs"],"Mensch belongs to the n-Deklination: Menschen.","A2"),
 Q("In der Straße stehen viele alte ___. (Haus)",["Häuser","Haus","Hause"],"Haus → Häuser.","A2"),
 Q("In den ___ fahren wir ans Meer.",["Ferien","Ferie","Ferienen"],"Ferien is plural only. The Dativ plural has no further -n here.","B1"),
 Q("Ich helfe meinem ___ beim Umzug. (Nachbar)",["Nachbarn","Nachbar","Nachbarns"],"Nachbar is an n-noun: dem Nachbarn.","B1"),
 Q("Das ist das Auto meines ___. (Kollege)",["Kollegen","Kollege","Kollegens"],"n-Deklination: des Kollegen.","B1"),
 Q("Sie fragt den ___ nach dem Weg. (Herr)",["Herrn","Herr","Herrens"],"Herr is an n-noun: den Herrn (singular), die Herren (plural).","B1"),
 Q("Ich habe den ___ der Frau vergessen. (Name)",["Namen","Name","Names"],"Akkusativ: den Namen.","B1"),
 Q("Die Stadt ehrt den ___. (Held)",["Helden","Held","Heldes"],"Held is an n-noun: den Helden.","B1"),
 Q("In der Schule arbeiten viele ___. (Lehrerin)",["Lehrerinnen","Lehrerins","Lehrerine"],"Nouns on -in double the n: Lehrerinnen.","B1"),
 Q("Die ___ der Stadt zeigen moderne Kunst. (Museum)",["Museen","Museums","Museume"],"Latin -um changes to -en: Museen.","B1"),
 Q("Die ___ der Reise sind hoch.",["Kosten","Kost","Kosts"],"Kosten is a plural noun.","B1"),
 Q("Ich habe heute viel ___ dabei. (Gepäck)",["Gepäck","Gepäcke","Gepäcker"],"Gepäck has no plural. Use viel with it.","B1"),
 Q("Im Garten wachsen zwei ___. (Apfelbaum)",["Apfelbäume","Apfelbaume","Äpfelbäume"],"The last word decides: Baum → Bäume.","B1"),
 Q("Das ist die Schreibweise des ___. (Name)",["Namens","Namen","Name"],"Genitiv singular of Name: des Namens.","B2"),
 Q("Wir besprechen heute mehrere ___. (Thema)",["Themen","Thema","Themas"],"Thema → Themen. The Latin -a becomes -en.","B2"),
 Q("Ich habe alle ___ gespeichert. (Datum)",["Daten","Datums","Datumen"],"Datum → Daten.","B2"),
 Q("Der Chef lobt den ___. (Praktikant)",["Praktikanten","Praktikant","Praktikantes"],"Nouns on -ant are n-nouns: den Praktikanten.","B2"),
 Q("Er hörte den Schlag seines ___.",["Herzens","Herz","Herzes"],"Das Herz: Genitiv des Herzens.","C1"),
 Q("Diesen ___ konnte er nicht fassen. (Gedanke)",["Gedanken","Gedanke","Gedankes"],"Akkusativ of Gedanke: den Gedanken.","C1"),
]
TH=[
 tc("Endungen",[("-e / -¨e","Hund → Hunde, Stuhl → Stühle"),("-er / -¨er","Kind → Kinder, Haus → Häuser"),("-(e)n","Frau → Frauen, Lampe → Lampen"),("-s","Auto → Autos, Hotel → Hotels"),("ohne","Lehrer, Zimmer, Mädchen")],"Lerne den Plural immer mit dem Nomen."),
 tc("n-Deklination",[("Nom","der Student"),("Akk","den Studenten"),("Dat","dem Studenten"),("Gen","des Studenten"),("Plural","die Studenten")],"Nur maskulin. Besonders: des Namens, des Herzens."),
 tc("Genus-Tipps",[("-ung, -heit, -keit","→ -en"),("-schaft, -ion, -ität","→ -en"),("-in","→ -innen"),("-um (lat.)","→ -en: Museum → Museen"),("Kompositum","der letzte Teil zählt")],"Weiblich meist -(e)n."),
]
apply("plural","Plural & n-Deklination","Nomen","Learn the plural with the noun. Feminine mostly -(e)n. A small group of masculine nouns takes -n.",
 '<span><b class="wt k lgk">-en</b> Plural</span><span><b class="wt v lgk">den Studenten</b> n-Deklination</span>',
 C,QS,TH,"vkas",
 ' {t:"plural",n:"Plural & n-Deklination",tag:"Student → Studenten",ds:"Pluralendungen, Genus-Tipps, n-Deklination, nur Plural · A2–C1"},',
 '{n:"Nomen & Fälle",t:["art","fall","vkas","gen"],soon:"Plural · n-Deklination"}',
 '{n:"Nomen & Fälle",t:["art","fall","vkas","plural","gen"]}',
 "Pluralform oder Artikel")
