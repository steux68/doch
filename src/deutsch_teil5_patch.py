#!/usr/bin/env python3
"""DOCH: 'Lernen auf Deutsch' Teil 5 - nvv, nom (inkl. Quellen-Tipps), vkas, oest. Eigene Formulierung. Idempotent."""
import sys,re
p="index.html"; s=open(p,encoding="utf-8").read()
if "Das Nomen trägt die Bedeutung, das Verb ist fast leer" in s: sys.exit("already patched")
miss=[]
def apply(k,R):
    global s
    a=s.find("GT.%s={"%k); b=s.find("\nGT.",a+10)
    if b<0: b=s.find("\n/* =====",a+10)
    assert a>0 and b>a,k
    seg=s[a:b]
    for o,n in R:
        if seg.count(o)<1: miss.append((k,o[:70])); continue
        seg=seg.replace(o,n)
    s=s[:a]+seg+s[b:]
NVV=[
("The noun carries the meaning, the verb is almost empty. Learn noun + verb as one block.","Das Nomen trägt die Bedeutung, das Verb ist fast leer. Lerne Nomen + Verb als einen Block."),
("Noun + almost empty verb = one meaning","Nomen + fast leeres Verb = eine Bedeutung"),
("Formal register for letters, reports and lectures. Most can be replaced by one verb.","Formale Sprache für Briefe, Berichte und Vorträge. Die meisten lassen sich durch ein einzelnes Verb ersetzen."),
("stellen = make it so · stehen = it is so","stellen = etwas herbeiführen · stehen = es ist so"),
("With nehmen","Mit nehmen"),
("Stellung nehmen zu = comment on. Rücksicht nehmen auf = be considerate of.","Stellung nehmen zu = sich äußern zu. Rücksicht nehmen auf = jemanden berücksichtigen."),
("bringen = active · kommen = passive meaning","bringen = aktiv · kommen = passive Bedeutung"),
("treffen = decide · finden = passive meaning","treffen = entscheiden · finden = passive Bedeutung"),
("Each has a one-word equivalent","Jede hat ein Verb als Entsprechung"),
("Use the noun version for formal writing, the verb for speech.","Die Nomenform passt zu formalen Texten, das Verb zur gesprochenen Sprache."),
("It is available: zur Verfügung stehen.","Es ist verfügbar: zur Verfügung stehen."),
("Someone makes it available: zur Verfügung stellen.","Jemand stellt es bereit: zur Verfügung stellen."),
("in Frage kommen = be possible.","in Frage kommen = möglich sein."),
("in Frage stellen = doubt.","in Frage stellen = bezweifeln."),
("zur Sprache kommen = was discussed.","zur Sprache kommen = besprochen werden."),
("Anwendung finden = wird angewendet.","Anwendung finden = wird angewendet."),
("Maßnahmen ergreifen (or treffen).","Maßnahmen ergreifen (oder treffen)."),
("in Kontakt stehen (be in contact).","in Kontakt stehen (Kontakt haben)."),
("zu Ende bringen = finish.","zu Ende bringen = beenden."),
("<p>A noun carries the meaning, the verb is almost empty. Typical of formal German: letters, reports, lectures.</p>","<p>Ein Nomen trägt die Bedeutung, das Verb ist fast leer. Typisch für formales Deutsch: Briefe, Berichte, Vorträge.</p>"),
("<span>make available / be available</span>","<span>bereitstellen / verfügbar sein</span>"),
("<span>doubt, question</span>","<span>bezweifeln, infrage stellen</span>"),
("<span>apply (beantragen)</span>","<span>(beantragen)</span>"),
("<span>invoice (berechnen)</span>","<span>(berechnen)</span>"),
("<span>be under pressure</span>","<span>Druck haben</span>"),
("<span>be under discussion</span>","<span>besprochen werden</span>"),
("<span>comment on (sich äußern)</span>","<span>(sich äußern)</span>"),
("<span>be considerate of</span>","<span>berücksichtigen</span>"),
("<span>make use of (nutzen)</span>","<span>(nutzen)</span>"),
("<span>refer to (sich beziehen)</span>","<span>(sich beziehen)</span>"),
("<span>commission (beauftragen)</span>","<span>(beauftragen)</span>"),
("<span>inform (informieren)</span>","<span>(informieren)</span>"),
("<span>be discussed / raise</span>","<span>besprochen werden / ansprechen</span>"),
("<span>be expressed / express</span>","<span>sich zeigen / ausdrücken</span>"),
("<span>be an option</span>","<span>eine Möglichkeit sein</span>"),
("<span>finish (beenden)</span>","<span>(beenden)</span>"),
("<span>be applied (angewendet werden)</span>","<span>(angewendet werden)</span>"),
("<span>be approved</span>","<span>genehmigt werden</span>"),
("kommen and finden often have a passive meaning.","kommen und finden haben oft eine passive Bedeutung."),
]
NOM=[
("Long attributes: find the article and its noun first, then read the middle backwards.","Lange Attribute: Zuerst Artikel und Nomen finden, dann die Mitte rückwärts lesen."),
("A relative clause packed in front of the noun","Ein Relativsatz, der vor dem Nomen steht"),
("Typical of written and academic German. The participle takes a normal adjective ending.","Typisch für geschriebenes und wissenschaftliches Deutsch. Das Partizip bekommt eine normale Adjektivendung."),
("Partizip I: Infinitiv + d, active, happening now","Partizip I: Infinitiv + d, aktiv, gleichzeitig"),
("Partizip II: passive or finished","Partizip II: passiv oder abgeschlossen"),
("zu + Partizip I = must or can be done (C1)","zu + Partizip I = muss oder kann getan werden (C1)"),
("How to read long attributes","So liest du lange Attribute"),
("1. Article and noun: die Fassade. 2. The participle before the noun: kritisierte. 3. The rest: von vielen Architekten, seit Jahren.","1. Artikel und Nomen: die Fassade. 2. Das Partizip vor dem Nomen: kritisierte. 3. Der Rest: von vielen Architekten, seit Jahren."),
("Nebensatz → Präposition + Nomen","Nebensatz → Präposition + Nomen"),
("Same content, two styles","Gleicher Inhalt, zwei Stile"),
("Verbalstil for speech and clear writing. Nominalstil for reports, exams and lectures. At C1 you need both directions.","Verbalstil für das Gespräch und klare Texte. Nominalstil für Berichte, Prüfungen und Vorträge. Auf C1 brauchst du beide Richtungen."),
("Active, now: Partizip I steigend, ending -en after die (plural).","Aktiv, gleichzeitig: Partizip I steigend, Endung -en nach die (Plural)."),
("Passive, finished: Partizip II, -e after das.","Passiv, abgeschlossen: Partizip II, -e nach das."),
("zu + Partizip I, -en after die (plural).","zu + Partizip I, -en nach die (Plural)."),
("Partizip I, -es after ein (neuter).","Partizip I, -es nach ein (Neutrum)."),
("The bridge is planned: Partizip II, -e after die (feminine singular).","Die Brücke wird geplant: Partizip II, -e nach die (feminin Singular)."),
("Partizip I, -en after die (plural).","Partizip I, -en nach die (Plural)."),
("Partizip II, -e after der (Nominativ).","Partizip II, -e nach der (Nominativ)."),
("<span>Article + noun: die Fassade</span>","<span>Artikel + Nomen: die Fassade</span>"),
("<span>Participle before the noun: kritisierte</span>","<span>Partizip vor dem Nomen: kritisierte</span>"),
("<span>The rest, backwards: seit Jahren</span>","<span>Der Rest, rückwärts: seit Jahren</span>"),
("Infinitiv + d · active, at the same time:","Infinitiv + d · aktiv, gleichzeitig:"),
("passive or finished: das renovierte Haus","passiv oder abgeschlossen: das renovierte Haus"),
("must / can be done: die zu prüfenden","muss / kann getan werden: die zu prüfenden"),
("The participle takes normal adjective endings.","Das Partizip bekommt normale Adjektivendungen."),
# Quellen-Seite (Teil des Segments)
("Tip: DWDS shows how a word is really used, with its typical partners. Duden settles spelling and grammar questions.","Tipp: DWDS zeigt, wie ein Wort wirklich benutzt wird, mit seinen typischen Partnern. Der Duden klärt Fragen zu Rechtschreibung und Grammatik."),
("Look up a verb here when you are unsure of the Perfekt, the Präteritum or the Konjunktiv.","Schlage hier ein Verb nach, wenn du bei Perfekt, Präteritum oder Konjunktiv unsicher bist."),
("Read the same story in Austrian, German and Swiss news and notice the different words (Jänner / Januar, Paradeiser / Tomate).","Lies dieselbe Geschichte in österreichischen, deutschen und Schweizer Nachrichten und achte auf die verschiedenen Wörter (Jänner / Januar, Paradeiser / Tomate)."),
("Write first from your own head, then check. A spell checker that corrects while you type teaches you nothing.","Schreibe zuerst aus dem Kopf und prüfe danach. Eine Rechtschreibprüfung, die beim Tippen korrigiert, bringt dir nichts bei."),
("Elementar: everyday phrases, simple sentences about yourself, routine tasks.","Elementar: Alltagsausdrücke, einfache Sätze über sich selbst, Routineaufgaben."),
("Selbstständig: work and travel situations, opinions with reasons, B2 fluent with native speakers.","Selbstständig: Situationen bei Arbeit und auf Reisen, Meinungen mit Begründung, auf B2 flüssig mit Muttersprachlern."),
("Kompetent: complex texts, flexible and precise for work, study and lectures.","Kompetent: komplexe Texte, flexibel und genau in Beruf, Studium und Vorträgen."),
("The levels are defined by the Council of Europe for all languages. Profile deutsch maps them to German grammar and vocabulary. Levels in this app are a guide.","Der Europarat hat die Stufen für alle Sprachen festgelegt. Profile deutsch ordnet ihnen deutsche Grammatik und Wortschatz zu. Die Stufen in dieser App sind eine Orientierung."),
("Free sentence collections vary in quality. Check them against Duden or DWDS (see Wörterbücher).","Freie Satzsammlungen sind unterschiedlich gut. Prüfe sie mit dem Duden oder DWDS (siehe Wörterbücher)."),
]
VKAS=[
("Learn the case together with the verb: helfen + Dativ, brauchen + Akkusativ.","Lerne den Fall zusammen mit dem Verb: helfen + Dativ, brauchen + Akkusativ."),
("A small group takes only the Dativ","Eine kleine Gruppe hat nur den Dativ"),
("Also: antworten, folgen, passen, schmecken, fehlen, zuhören, glauben (a person), begegnen.","Außerdem: antworten, folgen, passen, schmecken, fehlen, zuhören, glauben (einer Person), begegnen."),
("Two objects: person Dativ, thing Akkusativ","Zwei Objekte: Person Dativ, Sache Akkusativ"),
("Also: bringen, erklären, empfehlen, leihen, schreiben, sagen. Two nouns: Dativ first. Two pronouns: Akkusativ first.","Außerdem: bringen, erklären, empfehlen, leihen, schreiben, sagen. Zwei Nomen: Dativ zuerst. Zwei Pronomen: Akkusativ zuerst."),
("The noun after these verbs stays Nominativ","Das Nomen nach diesen Verben bleibt Nominativ"),
("There is no object here. The noun says the same as the subject. Also: heißen, scheinen.","Hier gibt es kein Objekt. Das Nomen sagt dasselbe wie das Subjekt. Außerdem: heißen, scheinen."),
("Same meaning, different case","Gleiche Bedeutung, anderer Fall"),
("helfen + Dativ, but unterstützen + Akkusativ","helfen + Dativ, aber unterstützen + Akkusativ"),
("folgen + Dativ, but begleiten + Akkusativ","folgen + Dativ, aber begleiten + Akkusativ"),
("antworten + Dativ, but fragen + Akkusativ","antworten + Dativ, aber fragen + Akkusativ"),
("Check each new verb in a dictionary","Schlage jedes neue Verb im Wörterbuch nach"),
("Ich helfe ihm, but Ich unterstütze ihn. English does not show the difference, so learn the case with the verb.","Ich helfe ihm, aber Ich unterstütze ihn. Lerne den Fall immer mit dem Verb."),
("With another object, mich becomes mir","Mit einem weiteren Objekt wird mich zu mir"),
("If the sentence already has an Akkusativ object, the reflexive pronoun is Dativ.","Hat der Satz schon ein Akkusativobjekt, steht das Reflexivpronomen im Dativ."),
("Very few verbs, formal (C1)","Sehr wenige Verben, formal (C1)"),
("Rare in everyday speech. You will meet them in speeches, laws and written reports.","Im Alltag selten. Du begegnest ihnen in Reden, Gesetzen und schriftlichen Berichten."),
("gefallen + Dativ; feminine → der Kundin.","gefallen + Dativ; feminin → der Kundin."),
("brauchen + Akkusativ; masculine → einen.","brauchen + Akkusativ; maskulin → einen."),
("schenken: the person is Dativ; feminine → seiner.","schenken: Die Person steht im Dativ; feminin → seiner."),
("zeigen: the person is Dativ: uns.","zeigen: Die Person steht im Dativ: uns."),
("antworten + Dativ; feminine → der Lehrerin.","antworten + Dativ; feminin → der Lehrerin."),
("fehlen + Dativ for the person; the missing thing is the subject, so Nominativ: ein Stift.","fehlen + Dativ für die Person; das Fehlende ist das Subjekt, also Nominativ: ein Stift."),
("Another Akkusativ object (die Hände) is present, so the pronoun is Dativ: mir.","Ein anderes Akkusativobjekt (die Hände) ist da, also steht das Pronomen im Dativ: mir."),
("No other object: the pronoun is Akkusativ: mich.","Kein anderes Objekt: Das Pronomen steht im Akkusativ: mich."),
("After sein the noun stays Nominativ: ein Architekt.","Nach sein bleibt das Nomen im Nominativ: ein Architekt."),
("glauben + Dativ when you believe a person: ihm.","glauben + Dativ, wenn man einer Person glaubt: ihm."),
("erklären: the person is Dativ; plural → den Schülern.","erklären: Die Person steht im Dativ; Plural → den Schülern."),
("leihen: the person is Dativ: dir.","leihen: Die Person steht im Dativ: dir."),
("gedenken + Genitiv (C1); plural → der.","gedenken + Genitiv (C1); Plural → der."),
("bedürfen + Genitiv (C1); feminine → einer.","bedürfen + Genitiv (C1); feminin → einer."),
("Ask the question after the verb. The answer tells you the case.","Stelle die Frage nach dem Verb. Die Antwort zeigt dir den Fall."),
("<span>Person</span><span>Dativ: Ich gebe dem Kind</span>","<span>Person</span><span>Dativ: Ich gebe dem Kind</span>"),
("<span>Sache</span><span>Akkusativ: einen Apfel.</span>","<span>Sache</span><span>Akkusativ: einen Apfel.</span>"),
]
OEST=[
("Learn the Austrian word with the German one: Paradeiser = Tomate.","Lerne das österreichische Wort zusammen mit dem deutschen: Paradeiser = Tomate."),
("Words you hear at the market","Wörter vom Markt"),
("These are standard in Austria and appear in shops, menus and newspapers. Germans understand most of them.","Diese Wörter sind in Österreich Standard und stehen in Geschäften, auf Speisekarten und in Zeitungen. Die meisten verstehen auch Deutsche."),
("More food words","Weitere Wörter rund ums Essen"),
("Jause is a small meal or snack in between. In a Beisl or at a Heuriger you will see many of these on the menu.","Eine Jause ist eine kleine Mahlzeit zwischendurch. In einem Beisl oder beim Heurigen stehen viele davon auf der Karte."),
("Things at home and on the street","Dinge zu Hause und auf der Straße"),
("Stiege and Stiegenhaus are the usual words in Austria. A Kasten is any cupboard or wardrobe.","Stiege und Stiegenhaus sind in Österreich die üblichen Wörter. Ein Kasten ist jeder Schrank."),
("Months, shops and clothes","Monate, Geschäfte und Kleidung"),
("Jänner is the normal word in Austria. Feber is dated and now rare; most people say Februar. heuer means this year.","Jänner ist in Österreich das normale Wort. Feber ist veraltet und selten; die meisten sagen Februar. heuer heißt dieses Jahr."),
("Drinks and places in Vienna","Getränke und Orte in Wien"),
("A Melange is coffee with a lot of hot milk. A Seidl is a small beer. In a Beisl you eat simple Austrian food.","Eine Melange ist Kaffee mit viel heißer Milch. Ein Seidl ist ein kleines Bier. Im Beisl isst man einfache österreichische Küche."),
("Words on signs and in conversation","Wörter auf Schildern und im Gespräch"),
("Anrainer frei means residents only. A Fenstertag is a working day between a holiday and the weekend.","Anrainer frei heißt: nur für Anwohner. Ein Fenstertag ist ein Arbeitstag zwischen einem Feiertag und dem Wochenende."),
("Useful for forms and appointments","Nützlich für Formulare und Termine"),
("You need Meldezettel when you move to a new flat. Ordination is the doctor's practice. Matura is the school-leaving exam.","Den Meldezettel brauchst du bei einem Umzug. Die Ordination ist die Praxis der Ärztin oder des Arztes. Die Matura ist die Abschlussprüfung der Schule."),
("Words for your own field","Wörter für das eigene Fach"),
("In Austria a building permit is a Baubewilligung. Use this word in emails to the Behörde in Vienna.","In Österreich heißt die Baugenehmigung Baubewilligung. Benutze dieses Wort in E-Mails an die Behörde in Wien."),
("Small grammar differences","Kleine Unterschiede in der Grammatik"),
("Perfekt with sein, and gender","Perfekt mit sein und das Genus"),
("Duden marks sein as süddeutsch, österreichisch, schweizerisch. The standard form in Germany is haben. Both are understood.","Der Duden kennzeichnet sein als süddeutsch, österreichisch, schweizerisch. In Deutschland ist haben die Standardform. Beide werden verstanden."),
("Hello and goodbye","Hallo und Auf Wiedersehen"),
("Grüß Gott is polite, Servus is relaxed and works both ways, Baba is only for friends.","Grüß Gott ist höflich, Servus ist locker und gilt für Hallo und Tschüss, Baba nur unter Freunden."),
("Just so you recognise them","Damit du sie erkennst"),
("Swiss standard German has no ß. You do not need to learn more for Austria or for the exam.","Das Schweizer Hochdeutsch hat kein ß. Für Österreich und für die Prüfung musst du nicht mehr lernen."),
("Semmel is the Austrian word.","Semmel ist das österreichische Wort."),
("In Austria and the south, sitzen forms the Perfekt with sein.","In Österreich und im Süden bildet sitzen das Perfekt mit sein."),
("Baba is the friendly goodbye. Grüß Gott is a greeting.","Baba ist der freundliche Abschied. Grüß Gott ist ein Gruß."),
("Standard Austrian German, not dialect.","Österreichisches Standarddeutsch, kein Dialekt."),
("Use these in letters and emails in Austria.","Benutze diese Wörter in Briefen und E-Mails in Österreich."),
('("Small grammar','("Small grammar'),
]
OEST=[x for x in OEST if x[0]!=x[1]]
WHYR=[
("Why do officials say zur Anwendung kommen?","Warum sagen Behörden zur Anwendung kommen?"),
("Since the chancelleries of the late Middle Ages, official German has loved nouns: a noun plus an almost empty verb such as kommen, stellen, nehmen. zur Anwendung kommen simply means angewendet werden. It sounds formal and precise – good in letters and reports, tiring when overdone.","Seit den Kanzleien des späten Mittelalters liebt das Amtsdeutsch Nomen: ein Nomen plus ein fast leeres Verb wie kommen, stellen, nehmen. zur Anwendung kommen heißt einfach angewendet werden. Es klingt förmlich und genau – gut in Briefen und Berichten, anstrengend, wenn man es übertreibt."),
("Why is German so fond of long nouns?","Warum liebt das Deutsche lange Nomen?"),
("German glues words together where English uses 'of': one word for a whole phrase. Twain joked that some German words are so long they have a perspective. Nominalstil packs a clause into a noun: die Planung des Neubaus instead of dass man den Neubau plant.","Das Deutsche klebt Wörter zusammen: ein Wort für eine ganze Wendung. Twain scherzte, manche deutschen Wörter seien so lang, dass sie eine Perspektive hätten. Der Nominalstil packt einen Satz in ein Nomen: die Planung des Neubaus statt dass man den Neubau plant."),
]
apply("nvv",NVV);apply("nom",NOM);apply("vkas",VKAS);apply("oest",OEST)
a=s.find("const WHY={"); e=s.find("\n",a); w=s[a:e]
for o,n in WHYR:
    if w.count(o)!=1: miss.append(("WHY",o[:70])); continue
    w=w.replace(o,n)
s=s[:a]+w+s[e:]
if miss:
    for m in miss: print("MISS",m)
    sys.exit("misses - nothing written")
s,c=re.subn(r'(<meta name="app-version" content="2026-11-24)([a-z])(")',lambda m:m.group(1)+chr(ord(m.group(2))+1)+m.group(3),s,count=1)
assert c==1
open(p,"w",encoding="utf-8").write(s); print("ok")
