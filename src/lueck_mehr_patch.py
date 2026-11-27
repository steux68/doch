#!/usr/bin/env python3
"""DOCH: ten more Lückentexte, two per level A1–C1 (27 Nov 2026). Own wording.
Gap = {Antwort/Alternative|Grundform|Schwierigkeit 1–3|Erklärung}. Aim: about half hard."""
import re, sys
p = "index.html"; s = open(p, encoding="utf-8").read()
if 'id:"a1d"' in s: sys.exit("already patched")
NEW = r'''
{id:"a1d",lv:"A1",t:"Meine Familie",x:`Das {ist||1|sein: das ist.} meine Familie. Mein Vater {heißt|heißen|1|er → Endung -t.} Peter, meine Mutter heißt Anna. Ich {habe|haben|1|ich habe.} {einen|ein|3|Akkusativ maskulin: der Bruder → Ich habe einen Bruder.} Bruder und eine Schwester. Mein Bruder {ist|sein|1|er ist.} zwölf Jahre alt. Er {liest|lesen|2|lesen: du liest, er liest (e → ie).} gern Comics. Meine Schwester {fährt|fahren|2|fahren: du fährst, sie fährt (a → ä).} jeden Tag mit dem Rad zur Schule.

Wir {wohnen|wohnen|1|wir → Endung -en.} in einer Wohnung in Salzburg. Die Wohnung hat drei Zimmer und {einen|ein|3|Akkusativ maskulin: der Balkon → einen Balkon.} Balkon. Am Sonntag {besuchen|besuchen|1|wir → Endung -en.} wir {unsere|unser|3|Akkusativ Plural: die Großeltern → unsere Großeltern.} Großeltern. Oma kocht immer Knödel. Ich {mag|mögen|3|mögen: ich mag, du magst, er mag (unregelmäßig).} Knödel sehr! Mein Opa {spielt|spielen|1|er → Endung -t.} mit {mir|ich|3|„mit“ + Dativ: ich → mir.} Karten.`},
{id:"a1e",lv:"A1",t:"Im Café",x:`„Guten Tag! Was {möchten|mögen|3|Höflich fragen: Sie möchten (möchte-Form von mögen).} Sie?“ – „Ich {hätte|haben|3|Höflich bestellen: Ich hätte gern … (Konjunktiv II von haben).} gern einen Tee und {ein|ein|2|das Wasser → ein Wasser: Akkusativ neutral ohne Endung.} Wasser.“

Meine Freundin Mia kommt auch. Sie {nimmt|nehmen|2|nehmen: du nimmst, sie nimmt.} einen Kaffee und ein Stück Kuchen. Der Kuchen {ist||1|er ist.} sehr gut. Wir {sitzen|sitzen|1|wir → Endung -en.} am Fenster und {sprechen|sprechen|1|wir sprechen: bei „wir“ kein Vokalwechsel.} über {den|der|3|„über“ + Akkusativ: der Urlaub → über den Urlaub.} Urlaub. Mia {fliegt|fliegen|1|sie → Endung -t.} im Sommer nach Spanien.

Dann {zahlen|zahlen|1|wir → Endung -en.} wir. „Zusammen oder getrennt?“, fragt die Kellnerin. „Getrennt, bitte.“ Ich {bezahle|bezahlen|2|ich → Endung -e.} sieben Euro. Mia {gibt|geben|3|geben: du gibst, sie gibt (e → i).} der Kellnerin ein Trinkgeld. Morgen {treffen|treffen|1|wir → Endung -en.} wir {uns|wir|3|Reflexivpronomen: wir treffen uns.} wieder.`},
{id:"a2d",lv:"A2",t:"Mit dem Zug nach Zürich",x:`Letzten Freitag {bin|sein|3|Perfekt mit „sein“ bei Bewegung: ich bin gefahren.} ich mit dem Zug nach Zürich {gefahren|fahren|2|Partizip II von fahren: gefahren.}. Der Zug {ist|sein|2|abfahren bildet das Perfekt mit sein.} pünktlich um acht Uhr {abgefahren|abfahren|3|Trennbares Verb im Partizip II: ab-ge-fahren.}. Ich {habe|haben|2|lesen bildet das Perfekt mit haben.} ein Buch gelesen und aus dem Fenster {geschaut|schauen|1|Regelmäßiges Verb: ge- … -t.}. Die Landschaft war wunderschön: Berge, Seen und kleine Dörfer.

In Zürich {hat|haben|2|abholen bildet das Perfekt mit haben.} mich meine Kusine am Bahnhof abgeholt. Wir {sind|sein|2|gehen bildet das Perfekt mit sein.} zuerst an den See gegangen. Das Wetter war schön, {deshalb/darum/deswegen||3|Folge im Hauptsatz: deshalb + Verb auf Platz 2.} haben wir draußen gegessen. Am Abend {waren|sein|2|Präteritum von sein: wir waren.} wir im Kino. Der Film {hat|haben|1|gefallen bildet das Perfekt mit haben.} mir gut gefallen.

Am Sonntag bin ich wieder nach Hause gefahren. Ich {war|sein|1|Präteritum: ich war.} müde, aber glücklich. Nächstes Jahr {möchte|mögen|3|Wunsch: ich möchte (möchte-Form von mögen).} ich {länger|lang|3|Komparativ mit Umlaut: lang → länger.} bleiben.`},
{id:"a2e",lv:"A2",t:"Ein Geburtstagsfest",x:`Am Samstag {feiert|feiern|1|sie → Endung -t.} meine Freundin Clara ihren dreißigsten Geburtstag. Sie hat {mich|ich|3|Akkusativ von ich: Sie hat mich eingeladen.} und zwanzig andere Leute eingeladen. Ich {weiß|wissen|3|wissen: ich weiß, du weißt, er weiß (unregelmäßig).} noch nicht, was ich {ihr|sie|3|Dativ von sie: Wem schenke ich etwas? – Ihr.} schenken soll. Vielleicht kaufe ich ein Buch, {weil||3|Grund im Nebensatz: weil … Verb am Ende.} sie gern {liest|lesen|2|Im Nebensatz steht das Verb am Ende: weil sie gern liest.}. Oder ich schenke ihr {einen|ein|3|Akkusativ maskulin: der Gutschein → einen Gutschein.} Gutschein für ein Konzert.

Das Fest {findet|stattfinden|3|Trennbares Verb: es findet … statt.} in einem Lokal im ersten Bezirk statt. Es {beginnt|beginnen|1|es → Endung -t.} um sieben Uhr. Ich {muss|müssen|2|Modalverb: ich muss (ohne Endung).} noch ein Kleid kaufen, denn mein altes Kleid ist mir zu {klein||1|Nach „zu“ hat das Adjektiv keine Endung.}.

Nach dem Fest {fahre|fahren|1|ich → Endung -e, kein Vokalwechsel.} ich mit dem Taxi nach Hause, {denn||2|denn: Grund, das Verb bleibt auf Platz 2.} ich {will|wollen|2|Modalverb wollen: ich will.} nicht allein zu Fuß gehen.`},
{id:"b1d",lv:"B1",t:"Leserbrief: Mehr Radwege!",x:`Sehr geehrte Damen und Herren,

mit großem Interesse habe ich Ihren Artikel über den Verkehr in unserer Stadt {gelesen|lesen|1|Partizip II: gelesen.}. Ich fahre seit Jahren mit dem Rad zur Arbeit, {obwohl||3|Gegensatz im Nebensatz: obwohl … Verb am Ende.} es oft gefährlich ist. Viele Autofahrer achten nicht {auf||2|„achten auf“ + Akkusativ.} Radfahrer, und die Radwege {sind|sein|1|Plural → sind.} zu schmal.

Ich bin der Meinung, {dass||2|Meinung im Nebensatz: dass … Verb am Ende.} die Stadt mehr Geld in sichere Radwege investieren {sollte|sollen|3|Konjunktiv II als Rat; im Nebensatz ganz am Ende.}. In {anderen|ander-|3|„in“ + Dativ Plural (wo?): in anderen Städten.} Städten, zum Beispiel in Kopenhagen, {fahren|fahren|1|Plural: viel mehr Menschen fahren.} viel mehr Menschen mit dem Rad.

Wenn es bessere Radwege {gäbe|geben|3|Irreale Bedingung, Konjunktiv II von geben: es gäbe.}, würden auch mehr Kinder allein zur Schule fahren. Außerdem wäre die Luft {sauberer|sauber|3|Komparativ: sauber → sauberer.}.

Ich {würde|werden|2|würde + Infinitiv: höflicher Wunsch.} mich freuen, wenn Sie dieses Thema noch einmal {aufgreifen|aufgreifen|2|Im Nebensatz bleibt das trennbare Verb zusammen am Ende.} würden.

Mit freundlichen {Grüßen|Gruß|3|Feste Formel: „mit“ + Dativ Plural, Endung -en.}`},
{id:"b1e",lv:"B1",t:"Rund um den Bodensee",x:`Der Bodensee liegt {zwischen||2|„zwischen“ + Dativ (wo?): zwischen Deutschland, Österreich und der Schweiz.} Deutschland, Österreich und der Schweiz. Er ist einer der {größten|groß|3|„einer der“ + Superlativ im Genitiv Plural: einer der größten Seen.} Seen Mitteleuropas.

Rund um den See {führt|führen|1|der Radweg → führt.} ein Radweg, {der||3|Relativpronomen, Nominativ maskulin: der Radweg, der …} etwa 260 Kilometer lang ist. Viele Touristen {machen|machen|1|Plural.} die Tour in einer Woche. Unterwegs kommt man an {vielen|viel|3|„an“ + Dativ Plural: an vielen schönen Orten.} schönen Orten vorbei, zum Beispiel an der Insel Mainau. Dort {wachsen|wachsen|1|Plural.} Blumen aus der ganzen Welt.

Wer nicht Rad fahren {will|wollen|2|Nebensatz mit „wer“: Verb am Ende.}, {kann|können|2|Nach dem Nebensatz kommt im Hauptsatz zuerst das Verb.} mit dem Schiff von Land zu Land fahren. Man {braucht|brauchen|1|man → Endung -t.} dafür meistens nur einen Ausweis. In Konstanz zahlt man mit Euro, in der Schweiz mit Franken – das {sollte|sollen|3|Empfehlung mit Konjunktiv II: das sollte man wissen.} man wissen, bevor man {losfährt|losfahren|3|Im Nebensatz bleibt das trennbare Verb zusammen am Ende.}.`},
{id:"b2d",lv:"B2",t:"Digitale Entgiftung",x:`Immer mehr Menschen klagen {darüber||3|„klagen über“ → das Pronominaladverb „darüber“ kündigt den dass-Satz an.}, dass sie ständig erreichbar sein müssen. Viele {merken|merken|1|Plural.} gar nicht, wie oft sie ihr Handy {entsperren|entsperren|1|Indirekte Frage: Verb am Ende.}.

Eine „digitale Entgiftung“ soll helfen: Man verzichtet eine Zeit lang {auf||2|„verzichten auf“ + Akkusativ.} soziale Medien. Wer das {ausprobiert|ausprobieren|3|Verben auf -ieren bilden das Partizip II ohne ge-: ausprobiert.} hat, berichtet oft von besserem Schlaf.

Kritiker {halten|halten|1|Plural: Kritiker halten … für …} solche Trends jedoch für übertrieben. Nicht das Gerät {sei|sein|3|Indirekte Rede, Konjunktiv I: sei.} das Problem, {sondern||3|Nach „nicht A“ folgt „sondern B“.} der Umgang damit. Statt Apps zu löschen, {sollte|sollen|2|Rat mit Konjunktiv II: man sollte …} man lieber feste Zeiten einplanen, {in denen||3|Relativpronomen mit Präposition, Dativ Plural (die Zeiten): in denen.} das Handy in der Schublade bleibt.

Letztlich hängt es {von||2|„abhängen von“ + Dativ.} jedem selbst ab, ob er die Technik beherrscht oder von ihr beherrscht {wird|werden|3|Passiv im Nebensatz: beherrscht wird (werden am Ende).}.`},
{id:"b2e",lv:"B2",t:"Der Wolf kehrt zurück",x:`Nach über hundert Jahren ist der Wolf nach Mitteleuropa {zurückgekehrt|zurückkehren|3|Perfekt mit sein, trennbares Verb: zurück-ge-kehrt.}. Seine Rückkehr wird {von||2|Im Passiv nennt „von“ + Dativ den Handelnden.} Naturschützern gefeiert, {während||3|Gegensatz zweier gleichzeitiger Dinge: während … Verb am Ende.} viele Landwirte um ihre Schafe fürchten. Allein im {vergangenen|vergangen|3|Adjektivendung nach „im“ (Dativ): im vergangenen Jahr.} Jahr wurden in einigen Regionen zahlreiche Nutztiere gerissen.

Die Behörden setzen auf Schutzzäune und Herdenschutzhunde. Diese Maßnahmen gelten als wirksam, {sind|sein|1|Plural (die Maßnahmen).} aber teuer. Viele Bauern fordern deshalb, dass der Staat die Kosten {übernimmt|übernehmen|3|übernehmen ist nicht trennbar: er übernimmt; im Nebensatz am Ende.}.

Umstritten ist auch die Frage, {ob||2|Indirekte Ja/Nein-Frage: ob.} sogenannte Problemwölfe abgeschossen werden {dürfen|dürfen|1|Modalverb im Passiv-Nebensatz ganz am Ende.}. Der Wolf ist in der EU {geschützt|schützen|2|Zustandspassiv: sein + Partizip II.}. Erst wenn ein Tier wiederholt Schutzzäune {überwunden|überwinden|3|Partizip II, nicht trennbar, unregelmäßig: überwunden.} hat, {darf|dürfen|3|Nach dem Nebensatz steht im Hauptsatz das Verb zuerst.} es in der Regel entnommen werden.`},
{id:"c1d",lv:"C1",t:"Die Kunst des Scheiterns",x:`In einer Gesellschaft, {die||2|Relativpronomen, Nominativ feminin: die Gesellschaft, die …} Erfolg über alles stellt, gilt Scheitern {als||2|„gelten als“.} Makel. Dabei {ließe|lassen|3|Konjunktiv II von lassen: es ließe sich argumentieren.} sich argumentieren, dass gerade Misserfolge zu den {wertvollsten|wertvoll|3|Superlativ, Dativ Plural nach „zu den“.} Erfahrungen {zählen|zählen|1|Nebensatz, Plural: Verb am Ende.}.

Im angelsächsischen Raum {wird||3|Unpersönliches Passiv: Es wird … gesprochen – ohne Subjekt, Verb im Singular.} offen über gescheiterte Projekte gesprochen. Hierzulande hingegen herrscht vielerorts noch die Angst, {sich||3|Reflexivpronomen im Infinitivsatz: sich zu blamieren.} zu blamieren. Nicht wenige Gründer verschweigen eine Insolvenz, da sie {befürchten|befürchten|1|Nebensatz, Plural: Verb am Ende.}, künftig keine Kredite mehr {zu bekommen|bekommen|3|Nach „befürchten“: Infinitiv mit zu.}.

{Angesichts||3|Präposition mit Genitiv: angesichts + Genitiv.} {dieser|dies-|3|Genitiv feminin: die Entwicklung → dieser Entwicklung.} Entwicklung fordern Ökonomen eine neue Fehlerkultur. Wer Fehler {eingesteht|eingestehen|3|Trennbares Verb im Nebensatz zusammen: eingesteht.}, so ihr Argument, {lerne|lernen|3|Indirekte Rede („so ihr Argument“), Konjunktiv I: er lerne.} schneller als jemand, der sie {vertuscht|vertuschen|2|Relativsatz: Verb am Ende; vertuschen ist nicht trennbar.}.`},
{id:"c1e",lv:"C1",t:"Mit zwei Sprachen aufwachsen",x:`Lange Zeit {galt|gelten|3|Präteritum von gelten: es galt.} es als ausgemacht, dass Kinder durch zwei Sprachen {überfordert|überfordern|2|Passiv mit würde: überfordert würden.} würden. Inzwischen hat sich diese Annahme als falsch {erwiesen|erweisen|3|Partizip II von erweisen (unregelmäßig): erwiesen.}. Mehrsprachig {aufgewachsene|aufwachsen|3|Partizipialattribut im Plural ohne Artikel: aufgewachsene Kinder.} Kinder schneiden in manchen Aufgaben sogar besser ab, {was||3|„was“ bezieht sich auf den ganzen vorigen Satz.} Forscher auf die ständige Übung im Umschalten {zurückführen|zurückführen|1|Im Relativsatz bleibt das trennbare Verb zusammen am Ende.}.

Entscheidend ist allerdings, {wie||2|Indirekte W-Frage: wie … Verb am Ende.} die Sprachen erworben werden: Je früher und natürlicher der Kontakt, {desto/umso||2|je … desto (umso).} leichter fällt das Lernen.

Eine Sprache, die nur zu Hause gesprochen wird, droht ohne Unterricht {zu verkümmern|verkümmern|3|„drohen“ + Infinitiv mit zu.}. Deshalb plädieren Fachleute {dafür||3|„plädieren für“ → „dafür“ kündigt den Infinitivsatz an.}, Herkunftssprachen {stärker|stark|2|Komparativ als Adverb.} in den Unterricht {einzubeziehen|einbeziehen|3|Trennbares Verb im Infinitiv mit zu: ein-zu-beziehen.}.`},
'''
a = '\n];\nconst LS={lv:null,id:null};'
if s.count(a) != 1: sys.exit("Anker LT")
s = s.replace(a, ',' + NEW.rstrip().rstrip(',') + a)
new = "2026-11-27-lueck"
m = re.search(r'name="app-version" content="([^"]*)"', s)
s = s.replace(m.group(0), 'name="app-version" content="%s"' % new)
open(p, "w", encoding="utf-8").write(s)
open("version.txt", "w").write(new + "\n")
print("OK", new)
