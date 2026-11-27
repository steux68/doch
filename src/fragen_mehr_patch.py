#!/usr/bin/env python3
"""DOCH: more questions for ten small topics, each to 30 (27 Nov 2026). Own wording.
Format per line: (Satz, [richtig, falsch, falsch], Begründung, Niveau). The right answer is always first."""
import re, sys
p = "index.html"; s = open(p, encoding="utf-8").read()
if "/* fragen-mehr */" in s: sys.exit("already patched")

D = {}

D["k1"] = [
 ("Der Sprecher erklärt, das Unternehmen ___ gute Zahlen. (haben)", ["habe","hat","hätte"], "Konjunktiv I von haben, 3. Person: habe.", "B2"),
 ("Sie sagt, sie ___ krank. (sein)", ["sei","ist","wäre"], "Konjunktiv I von sein: sie sei.", "B2"),
 ("Er sagt, sie ___ heute nicht. (kommen)", ["komme","kommt","käme"], "Konjunktiv I: Stamm + e → komme.", "B2"),
 ("Der Zeuge gab an, er ___ nichts gesehen. (haben)", ["habe","hat","hätte"], "Vergangenes in der indirekten Rede: habe + Partizip II.", "C1"),
 ("Sie meinte, er ___ gestern in Linz gewesen. (sein)", ["sei","ist","wäre"], "Konjunktiv I Perfekt: sei + gewesen.", "C1"),
 ("Die Ärzte betonen, man ___ auf genug Schlaf achten. (sollen)", ["solle","soll","sollte"], "Konjunktiv I von sollen: man solle.", "C1"),
 ("Sie sagten, sie ___ keine Zeit. (haben)", ["hätten","haben","hatten"], "sie haben klingt wie der Indikativ, deshalb nimmt man Konjunktiv II: hätten.", "C1"),
 ("Der Autor schreibt, die Stadt ___ im Krieg zerstört worden. (sein)", ["sei","ist","wäre"], "Passiv Perfekt im Konjunktiv I: sei … worden.", "C1"),
 ("Sie sagte, sie ___ morgen früh abgeholt. (werden)", ["werde","wird","würde"], "Konjunktiv I von werden: sie werde.", "C1"),
 ("Er erklärt: „Ich bin müde.“ → Er erklärt, er ___ müde.", ["sei","bin","war"], "In der indirekten Rede steht Konjunktiv I: er sei.", "B2"),
 ("Er sagt: „Ich habe Hunger.“ → Er sagt, er ___ Hunger.", ["habe","hat","hatte"], "ich habe → er habe (Konjunktiv I).", "B2"),
 ("Sie sagt: „Wir kommen morgen.“ → Sie sagt, sie ___ morgen.", ["kämen","kommen","kamen"], "sie kommen klingt wie der Indikativ, deshalb Konjunktiv II: kämen.", "C1"),
 ("Er meinte, wir ___ nicht warten. (müssen)", ["müssten","müssen","mussten"], "wir müssen = Indikativ, deshalb Konjunktiv II: müssten.", "C1"),
 ("In der Zeitung steht, der Minister ___ zurückgetreten. (sein)", ["sei","ist","wäre"], "Perfekt im Konjunktiv I: sei zurückgetreten.", "B2"),
 ("Der Sprecher sagte, das Gesetz ___ bald in Kraft. (treten)", ["trete","tritt","träte"], "Konjunktiv I von treten: er/es trete.", "C1"),
 ("Sie meinte, er ___ das Geld nicht. (brauchen)", ["brauche","braucht","brauchte"], "Konjunktiv I: Stamm + e → brauche.", "B2"),
 ("Er sagt: „Ich kann nicht kommen.“ → Er sagt, er ___ nicht kommen. (können)", ["könne","kann","könnte"], "Konjunktiv I von können: er könne.", "B2"),
]

D["nom"] = [
 ("die Kinder, die spielen → die ___ Kinder", ["spielenden","gespielten","spielende"], "Aktiv, gleichzeitig: Partizip I spielend, Endung -en (Plural nach die).", "B2"),
 ("der Mann, der schläft → der ___ Mann", ["schlafende","geschlafene","schlafenden"], "Partizip I schlafend, Endung -e (Nominativ nach der).", "B2"),
 ("das Auto, das gestohlen wurde → das ___ Auto", ["gestohlene","stehlende","gestohlenes"], "Passiv, abgeschlossen: Partizip II, -e nach das.", "B2"),
 ("die Rechnung, die bezahlt wurde → die ___ Rechnung", ["bezahlte","bezahlende","bezahlten"], "Passiv, abgeschlossen: Partizip II, -e nach die (Singular).", "B2"),
 ("ein Problem, das gelöst werden muss → ein zu ___ Problem", ["lösendes","lösende","gelöstes"], "zu + Partizip I, Endung -es (neutral nach ein).", "C1"),
 ("die Fragen, die gestellt wurden → die ___ Fragen", ["gestellten","stellenden","gestellte"], "Partizip II, Endung -en (Plural nach die).", "B2"),
 ("Wegen des ___ Verkehrs kamen wir zu spät. (zunehmen)", ["zunehmenden","zugenommenen","zunehmende"], "Partizip I, Genitiv maskulin nach des: -en.", "C1"),
 ("Weil es regnete, fiel das Fest aus. → ___ des Regens fiel das Fest aus.", ["Wegen","Trotz","Durch"], "Nominalstil: weil → wegen + Genitiv.", "B2"),
 ("Obwohl es regnete, gingen wir spazieren. → ___ des Regens gingen wir spazieren.", ["Trotz","Wegen","Durch"], "Nominalstil: obwohl → trotz + Genitiv.", "B2"),
 ("Nachdem das Haus saniert worden war, … → ___ der Sanierung des Hauses, …", ["Nach","Wegen","Seit"], "Nominalstil: nachdem → nach + Dativ.", "B2"),
 ("der Bericht, der gestern veröffentlicht wurde → der gestern ___ Bericht", ["veröffentlichte","veröffentlichende","veröffentlichter"], "Partizip II, Endung -e (Nominativ maskulin nach der).", "C1"),
 ("die Studierenden, die an der Prüfung teilnehmen → die an der Prüfung ___ Studierenden", ["teilnehmenden","teilgenommenen","teilnehmende"], "Partizip I, Endung -en (Plural nach die).", "C1"),
 ("der Student, der gerade liest → der gerade ___ Student", ["lesende","gelesene","lesenden"], "Aktiv, gleichzeitig: Partizip I, -e nach der.", "B2"),
 ("ein Haus, das vor 100 Jahren gebaut wurde → ein vor 100 Jahren ___ Haus", ["gebautes","bauendes","gebaute"], "Partizip II, Endung -es (neutral nach ein).", "C1"),
 ("Man darf hier nicht rauchen. → Das ___ ist hier verboten.", ["Rauchen","Raucher","Rauch"], "Nominalstil: das Verb wird zum Nomen, großgeschrieben: das Rauchen.", "B2"),
 ("Nachdem er angekommen war, … → Nach seiner ___, …", ["Ankunft","Ankommen","Angekommenen"], "Nominalstil: ankommen → die Ankunft.", "B2"),
]

D["tekamolo"] = [
 ("„gestern“ beantwortet die Frage …", ["Wann?","Wo?","Wie?"], "Ein Zeitpunkt ist Temporal (wann?).", "A2"),
 ("„im Garten“ beantwortet die Frage …", ["Wo?","Wann?","Wie?"], "Ein Ort ist Lokal (wo?).", "A2"),
 ("„gern“ beantwortet die Frage …", ["Wie?","Wohin?","Wann?"], "Wie etwas geschieht, ist Modal (wie?).", "A2"),
 ("„aus Angst“ beantwortet die Frage …", ["Warum?","Wie?","Wo?"], "Ein Grund ist Kausal (warum?).", "B1"),
 ("„bis Freitag“ beantwortet die Frage …", ["Bis wann?","Wohin?","Warum?"], "Eine Zeitgrenze ist Temporal (bis wann?).", "B1"),
 ("„vor dem Haus“ beantwortet die Frage …", ["Wo?","Wohin?","Wann?"], "Ein Ort ist Lokal (wo?).", "A2"),
 ("Neutrale Reihenfolge: Wir fahren ___.", ["im Sommer mit dem Rad nach Italien","mit dem Rad im Sommer nach Italien","nach Italien im Sommer mit dem Rad"], "Te – Mo – Lo: im Sommer, mit dem Rad, nach Italien.", "B1"),
 ("Neutrale Reihenfolge: Sie wohnt ___.", ["seit zwei Jahren gern in Wien","gern in Wien seit zwei Jahren","in Wien seit zwei Jahren gern"], "Te – Mo – Lo: seit zwei Jahren, gern, in Wien.", "B1"),
 ("Neutrale Reihenfolge: Der Zug fährt ___ ab.", ["heute wegen der Verspätung von Gleis 3","von Gleis 3 heute wegen der Verspätung","wegen der Verspätung von Gleis 3 heute"], "Te – Ka – Lo: heute, wegen der Verspätung, von Gleis 3.", "B2"),
 ("Neutrale Reihenfolge: Ich lese ___.", ["abends gern im Bett","gern abends im Bett","im Bett abends gern"], "Te – Mo – Lo: abends, gern, im Bett.", "B1"),
 ("Ich schicke ___ heute.", ["sie ihm","ihm sie","dem Kind sie"], "Zwei Pronomen: Akkusativ vor Dativ: sie ihm.", "B1"),
 ("Ich gebe ___.", ["ihm das Buch","das Buch ihm"], "Ein Pronomen steht vor dem Nomen: ihm das Buch.", "B1"),
 ("Wegen des Staus ___ wir zu spät.", ["kamen","wir kamen","gekommen"], "Auf Platz 1 steht die Angabe, das Verb steht auf Platz 2.", "B1"),
 ("Im Sommer ___ wir oft am See.", ["sind","wir","waren"], "Das konjugierte Verb steht immer auf Platz 2: Im Sommer sind wir …", "A2"),
 ("Die richtige Reihenfolge ist …", ["Temporal – Kausal – Modal – Lokal","Lokal – Modal – Kausal – Temporal","Modal – Lokal – Temporal – Kausal"], "TEKAMOLO: Te – Ka – Mo – Lo.", "A2"),
]

D["rel"] = [
 ("Das ist die Frau, ___ ich gestern getroffen habe.", ["die","der","den"], "Ich habe sie getroffen: Akkusativ feminin → die.", "B1"),
 ("Die Kinder, ___ im Garten spielen, sind meine Nachbarn.", ["die","denen","den"], "Sie spielen: Nominativ Plural → die.", "B1"),
 ("Der Hund, ___ ich gefüttert habe, heißt Rex.", ["den","der","dem"], "Ich habe ihn gefüttert: Akkusativ maskulin → den.", "B1"),
 ("Das Kind, ___ ich ein Buch geschenkt habe, freut sich.", ["dem","das","den"], "Ich habe ihm ein Buch geschenkt: Dativ neutral → dem.", "B1"),
 ("Die Nachbarn, ___ Hund bellt, sind nett.", ["deren","dessen","denen"], "Genitiv Plural: deren (deren Hund = der Hund der Nachbarn).", "B2"),
 ("Der Autor, ___ Roman ich gelesen habe, kommt aus Linz.", ["dessen","deren","den"], "Genitiv maskulin: dessen (dessen Roman).", "B2"),
 ("Das Mädchen, ___ Fahrrad kaputt ist, geht zu Fuß.", ["dessen","deren","das"], "Das Mädchen ist neutral, deshalb Genitiv dessen.", "B2"),
 ("Der Zug, mit ___ wir fahren, hat Verspätung.", ["dem","den","der"], "mit + Dativ, maskulin: dem.", "B1"),
 ("Die Straße, durch ___ wir gehen, ist eng.", ["die","der","den"], "durch + Akkusativ, feminin: die.", "B1"),
 ("Der Kollege, auf ___ ich mich verlassen kann, ist sehr zuverlässig.", ["den","dem","der"], "sich verlassen auf + Akkusativ, maskulin: den.", "B2"),
 ("Alles, ___ ich weiß, habe ich dir gesagt.", ["was","das","dem"], "Nach alles steht was.", "B2"),
 ("Er hat das Rennen gewonnen, ___ alle überrascht hat.", ["was","das","dem"], "Bezieht sich der Relativsatz auf den ganzen Satz, steht was.", "C1"),
 ("Das Einzige, ___ mich stört, ist der Lärm.", ["was","das","dem"], "Nach das Einzige steht was.", "C1"),
 ("Die Frau, mit ___ ich gesprochen habe, ist Ärztin.", ["der","die","deren"], "mit + Dativ, feminin: der.", "B1"),
]

D["k2"] = [
 ("Wenn ich reich ___, würde ich um die Welt reisen. (sein)", ["wäre","bin","war"], "Irreal: wäre.", "B1"),
 ("Wenn wir mehr Platz ___, könnten wir eine Küche einbauen. (haben)", ["hätten","haben","hatten"], "Irreal: hätten.", "B1"),
 ("Wenn du mich gefragt ___, hätte ich dir geholfen. (haben)", ["hättest","hast","hattest"], "Irreal in der Vergangenheit: hättest + Partizip II.", "B2"),
 ("Ohne deine Hilfe ___ ich es nicht geschafft. (haben)", ["hätte","habe","hatte"], "Irreal in der Vergangenheit: hätte … geschafft.", "B2"),
 ("Das ___ du nicht tun sollen. (haben)", ["hättest","hast","hattest"], "Vorwurf über Vergangenes: hättest … tun sollen.", "B2"),
 ("___ ich doch nur früher aufgestanden! (sein)", ["Wäre","War","Würde"], "Wunsch über Vergangenes: Wäre ich doch … aufgestanden!", "B2"),
 ("Es wäre schön, wenn du mir bei der Arbeit helfen ___.", ["würdest","wirst","wurdest"], "Höflicher Wunsch: helfen würdest.", "B2"),
 ("___ ich Sie um einen Gefallen bitten? (dürfen)", ["Dürfte","Darf","Durfte"], "Sehr höflich: Dürfte ich …?", "B2"),
 ("Sie sieht aus, als ___ sie nicht geschlafen. (haben)", ["hätte","hat","hatte"], "Vergleich, der nicht stimmt: als hätte sie …", "B2"),
 ("Sie spricht, als ___ sie die Chefin. (sein)", ["wäre","ist","war"], "Vergleich, der nicht stimmt: als wäre sie …", "B2"),
 ("Hätte ich das gewusst, ___ ich nicht gekommen. (sein)", ["wäre","hätte","würde"], "Ohne wenn: Hätte ich das gewusst, wäre ich … gekommen.", "B2"),
 ("Wenn er mehr gelernt ___, hätte er die Prüfung bestanden. (haben)", ["hätte","hat","hatte"], "Irreal in der Vergangenheit: hätte … gelernt.", "B2"),
 ("Ich wäre gern gekommen, aber ich ___ krank. (sein)", ["war","wäre","bin"], "Der Grund ist wirklich: ich war krank. Nur der Wunsch ist irreal.", "B2"),
 ("Das ___ ein Fehler gewesen sein. (Vermutung)", ["dürfte","darf","durfte"], "Vermutung: dürfte … gewesen sein.", "C1"),
]

D["konn2"] = [
 ("Der Antrag wurde abgelehnt, ___ er unvollständig war.", ["da","damit","sodass"], "da gibt einen Grund an: Der Antrag war unvollständig.", "B2"),
 ("___ der Verkehr dicht war, kamen wir pünktlich an.", ["Obwohl","Weil","Sodass"], "Gegensatz: Trotz dichten Verkehrs kamen wir pünktlich an.", "B2"),
 ("Das Gebäude ist alt, ___ steht es unter Denkmalschutz.", ["deshalb","obwohl","sodass"], "deshalb gibt die Folge an, danach steht das Verb auf Platz 2.", "B2"),
 ("Je länger wir warten, ___ teurer wird es.", ["desto","je","dass"], "je … desto + Komparativ.", "B2"),
 ("___ er sich entschuldigt hatte, war die Sache erledigt.", ["Nachdem","Bevor","Während"], "nachdem: Das Entschuldigen war zuerst, danach war es erledigt.", "B2"),
 ("Er arbeitet viel, ___ er will die Prüfung bestehen.", ["denn","weil","dass"], "denn steht vor einem Hauptsatz: Das Verb bleibt auf Platz 2.", "B1"),
 ("Das Auto ist teuer, ___ ist es sehr sparsam.", ["dafür","weil","sodass"], "dafür gleicht einen Nachteil aus.", "B2"),
 ("___ wir unterschreiben, möchten wir alles prüfen.", ["Bevor","Nachdem","Seit"], "bevor: zuerst prüfen, dann unterschreiben.", "B2"),
 ("Sie ist krank. Trotzdem ___ sie zur Arbeit.", ["geht","sie geht","gegangen"], "Nach trotzdem steht das Verb auf Platz 2.", "B2"),
 ("Entweder du hilfst mir, ___ ich mache es allein.", ["oder","sondern","denn"], "entweder … oder.", "B1"),
 ("Wir haben nicht nur gewonnen, ___ auch viel Spaß gehabt.", ["sondern","aber","oder"], "nicht nur … sondern auch.", "B1"),
 ("Das Projekt gelingt nur, ___ alle zusammenarbeiten.", ["wenn","obwohl","sodass"], "wenn gibt hier die Bedingung an.", "B2"),
 ("Wir schließen das Fenster, ___ es nicht zieht.", ["damit","obwohl","wohingegen"], "damit gibt den Zweck an.", "B2"),
 ("Die Preise sind gesunken. ___ ist die Nachfrage gestiegen.", ["Folglich","Obwohl","Indem"], "folglich gibt die Folge an: Danach steht das Verb auf Platz 2.", "C1"),
]

D["nvv"] = [
 ("Wir ___ mehrere Angebote in Betracht.", ["ziehen","stellen","nehmen"], "in Betracht ziehen = überlegen.", "B2"),
 ("Der Leiter ___ den Vorschlag zur Diskussion.", ["stellt","gibt","nimmt"], "zur Diskussion stellen.", "B2"),
 ("Das neue Gesetz ___ am 1. Januar in Kraft.", ["tritt","kommt","geht"], "in Kraft treten.", "B2"),
 ("Bei der Sanierung ___ neue Maschinen zum Einsatz.", ["kommen","gehen","stehen"], "zum Einsatz kommen.", "B2"),
 ("Bitte ___ Sie mir bis Montag Bescheid.", ["geben","machen","nehmen"], "Bescheid geben.", "B1"),
 ("Viele Eltern ___ die Förderung in Anspruch.", ["nehmen","machen","geben"], "in Anspruch nehmen.", "B2"),
 ("Wer ___ die Verantwortung für den Fehler?", ["übernimmt","macht","gibt"], "Verantwortung übernehmen.", "B2"),
 ("Die Opposition ___ scharfe Kritik an dem Plan.", ["übt","macht","gibt"], "Kritik üben.", "B2"),
 ("Sie ___ von ihrem Recht Gebrauch.", ["macht","nimmt","gibt"], "von etwas Gebrauch machen.", "B2"),
 ("Bitte ___ Sie Kontakt mit uns auf.", ["nehmen","machen","geben"], "Kontakt aufnehmen.", "B1"),
 ("Das Team ___ sein Können unter Beweis.", ["stellt","gibt","setzt"], "unter Beweis stellen.", "C1"),
 ("Der Preis ___ keine große Rolle.", ["spielt","macht","stellt"], "eine Rolle spielen.", "B1"),
 ("Jeder kann einen Beitrag zum Umweltschutz ___.", ["leisten","machen","geben"], "einen Beitrag leisten.", "B2"),
 ("Sie können bis Freitag einen Antrag ___.", ["stellen","machen","geben"], "einen Antrag stellen.", "B1"),
]

D["pass"] = [
 ("Das Essen ___ gerade gekocht. (werden)", ["wird","hat","ist"], "Passiv Präsens: wird + Partizip II.", "B1"),
 ("Gestern ___ viel gearbeitet. (werden)", ["wurde","wird","worden"], "Unpersönliches Passiv im Präteritum: wurde … gearbeitet.", "B2"),
 ("Die Tür ist ___. (öffnen)", ["geöffnet","geöffnen","öffnet"], "Zustandspassiv: sein + Partizip II.", "B1"),
 ("Die Brücke wird gerade ___. (renovieren)", ["renoviert","renovieren","renovierte"], "Passiv Präsens: wird + Partizip II.", "B1"),
 ("Der Fehler konnte nicht mehr ___ werden. (korrigieren)", ["korrigiert","korrigieren","korrigierend"], "Passiv mit Modalverb: Partizip II + werden.", "B2"),
 ("Die Mitarbeiter ___ über die Änderung informiert worden. (sein)", ["sind","wurden","werden"], "Passiv Perfekt: sind … informiert worden.", "B2"),
 ("Das Formular muss ausgefüllt ___.", ["werden","worden","sein"], "Passiv mit Modalverb: Partizip II + werden.", "B2"),
 ("Das ist nicht zu ___. (ändern)", ["ändern","geändert","änderbar"], "sein + zu + Infinitiv: Das kann nicht geändert werden.", "B2"),
 ("Die Tür ___ sich nicht öffnen. (lassen)", ["lässt","lasst","lassen"], "sich lassen + Infinitiv: Es ist nicht möglich.", "B2"),
 ("Der Student wurde vom Professor ___. (loben)", ["gelobt","loben","lobte"], "Passiv Präteritum: wurde + Partizip II.", "B1"),
 ("Von wem ___ das Bild gemalt? (werden)", ["wurde","wird","worden"], "Passiv Präteritum: wurde … gemalt.", "B1"),
 ("Bei der Hochzeit wurde viel ___. (tanzen)", ["getanzt","tanzen","tanzte"], "Unpersönliches Passiv: Es wurde viel getanzt.", "B2"),
 ("Seit gestern ___ die Straße gesperrt.", ["ist","wird","wurde"], "Zustandspassiv: Das Ergebnis besteht jetzt noch: ist gesperrt.", "B2"),
]

D["perf"] = [
 ("Sie ___ nach Hause gegangen. (gehen)", ["ist","hat","wird"], "Bewegung: sein.", "A2"),
 ("Ich ___ gestern den ganzen Tag gelesen. (lesen)", ["habe","bin","war"], "lesen: haben.", "A2"),
 ("Er ___ seinen Schlüssel verloren. (verlieren)", ["hat","ist","wird"], "verlieren hat ein Objekt: haben.", "A2"),
 ("Er ___ letzte Woche eingeschlafen. (einschlafen)", ["ist","hat","wird"], "Änderung eines Zustands: sein.", "A2"),
 ("Ich habe lange ___. (schlafen)", ["geschlafen","geschlaft","schlief"], "schlafen → geschlafen.", "A2"),
 ("Hast du das Buch schon ___? (lesen)", ["gelesen","gelest","gelesst"], "lesen → gelesen.", "A2"),
 ("Wir haben im Urlaub viel ___. (sehen)", ["gesehen","gesieht","sah"], "sehen → gesehen.", "A2"),
 ("Das Kind hat die Vase ___. (zerbrechen)", ["zerbrochen","gebrochen","zerbricht"], "zerbrechen → zerbrochen (ohne ge-, weil zer- nicht trennbar ist).", "B1"),
 ("Nachdem wir angekommen ___, haben wir gegessen. (sein)", ["waren","haben","wurden"], "Plusquamperfekt: waren angekommen.", "B1"),
 ("Als ich ankam, ___ der Zug schon abgefahren. (sein)", ["war","hatte","wurde"], "Plusquamperfekt: war abgefahren.", "B1"),
 ("Letzte Woche ___ ich im Theater. (sein)", ["war","bin","wurde"], "Präteritum von sein: ich war.", "A2"),
 ("Sie ___ drei Jahre in Graz gelebt. (haben)", ["hat","ist","war"], "leben: haben.", "A2"),
 ("Morgen um diese Zeit ___ wir schon gelandet sein. (werden)", ["werden","wurden","haben"], "Futur II: werden + Partizip II + sein.", "C1"),
]

D["vprep"] = [
 ("Ich träume ___ einem eigenen Haus.", ["von","über","an"], "träumen von + Dativ.", "B1"),
 ("Er hat mich ___ Hilfe gebeten.", ["um","für","auf"], "bitten um + Akkusativ.", "B1"),
 ("Sie hat sich ___ ihre Kollegin geärgert.", ["über","auf","an"], "sich ärgern über + Akkusativ.", "B1"),
 ("Wir gratulieren dir ___ Geburtstag.", ["zum","für","am"], "gratulieren zu + Dativ: zum.", "A2"),
 ("___ ärgerst du dich? Über den Lärm.", ["Worüber","Woran","Wofür"], "sich ärgern über → worüber.", "B1"),
 ("Die Firma sucht ___ neuen Mitarbeitern.", ["nach","für","um"], "suchen nach + Dativ.", "B1"),
 ("Sie verlässt sich ___ ihren Mann.", ["auf","an","für"], "sich verlassen auf + Akkusativ.", "B1"),
 ("Ich halte ihn ___ einen guten Architekten.", ["für","als","zu"], "halten für + Akkusativ.", "B2"),
 ("Es handelt sich ___ einen Irrtum.", ["um","über","von"], "sich handeln um + Akkusativ.", "B2"),
 ("Sie entscheidet sich ___ das rote Kleid.", ["für","auf","zu"], "sich entscheiden für + Akkusativ.", "B1"),
 ("Wie reagierst du ___ Kritik?", ["auf","für","an"], "reagieren auf + Akkusativ.", "B2"),
]

def J(l): return "[" + ",".join('"%s"' % x for x in l) + "]"
def Q(t): return ' {s:"%s",o:%s,why:"%s",lv:"%s"}' % (t[0], J(t[1]), t[2], t[3])

for k, qs in D.items():
    st = s.find("GT.%s={" % k)
    if st < 0: sys.exit("no topic " + k)
    q = s.find(" q:[", st)
    end = s.find("}],\n th:`", q)
    if q < 0 or end < 0: sys.exit("no end " + k)
    old = s[q:end]
    have = set(re.findall(r'\{s:"([^"]*)"', old))
    for t in qs:
        if t[0] in have: sys.exit("duplicate in %s: %s" % (k, t[0]))
        if len(set(t[1])) != len(t[1]): sys.exit("equal options: " + t[0])
        if '"' in t[0] or '"' in t[2]: sys.exit("quote char: " + t[0])
    s = s[:end] + "},\n" + ",\n".join(Q(t) for t in qs) + s[end + 1:]
    print(k, "+", len(qs))

s = s.replace("/* ---------- topics + home ---------- */", "/* fragen-mehr */\n/* ---------- topics + home ---------- */", 1)
new = "2026-11-27-fragen"
m = re.search(r'name="app-version" content="([^"]*)"', s)
s = s.replace(m.group(0), 'name="app-version" content="%s"' % new)
open(p, "w", encoding="utf-8").write(s)
open("version.txt", "w").write(new + "\n")
print("OK", new)
