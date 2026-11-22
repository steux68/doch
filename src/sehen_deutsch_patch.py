#!/usr/bin/env python3
"""2026-11-22j Sehen: alle Erklärtexte (Bildung, Gebrauch, Signale, Achtung, Merke, Trick, Satz bauen, Präpositionen) auf Deutsch.
Eigene Formulierungen, Entwurf. Idempotent: bei bereits ersetzten Texten passiert nichts."""
import os, re, sys
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
p = os.path.join(root, "index.html")
s = open(p, encoding="utf-8").read()

T = [
# Zeiten
("Before another past event.", "Vor einem anderen vergangenen Ereignis."),
("Stamm + -te (or Ablaut)", "Stamm + -te (oder Ablaut)"),
("Written past, narration.", "Schriftliche Vergangenheit, Erzählung."),
("Spoken: mostly sein, haben, Modalverben.", "Gesprochen: fast nur sein, haben, Modalverben."),
("Spoken past, result counts now.", "Gesprochene Vergangenheit; das Ergebnis zählt jetzt."),
("bin with movement or change.", "bin bei Bewegung oder Veränderung."),
("Now, always, planned.", "Jetzt, immer, geplant."),
("Also the future with a time word.", "Auch für die Zukunft, mit einer Zeitangabe."),
("Plans, promises, guesses.", "Pläne, Versprechen, Vermutungen."),
("Präsens + morgen is more common.", "Präsens + morgen ist häufiger."),
("Done by a future point; or a guess.", "Bis zu einem Zeitpunkt in der Zukunft fertig; oder eine Vermutung."),
# Fälle
("the dictionary form", "die Grundform"),
("Subject; after sein, werden.", "Subjekt; nach sein, werden."),
("Ask: who does it?", "Frage: Wer macht es?"),
("only masculine: der → den", "nur Maskulinum: der → den"),
("Object; für, durch, gegen, ohne.", "Objekt; für, durch, gegen, ohne."),
("die, das, die stay the same.", "die, das, die bleiben gleich."),
("Indirect object; mit, bei, nach, von.", "Indirektes Objekt; mit, bei, nach, von."),
("Plural noun gets -n: den Kindern.", "Das Nomen im Plural bekommt -n: den Kindern."),
("Possession; wegen, trotz, während.", "Besitz; wegen, trotz, während."),
("masc. / neut. noun takes -(e)s.", "Maskulinum / Neutrum: Nomen bekommt -(e)s."),
# Satz bauen
("the one who does it", "wer etwas tut"),
("sehen takes Akkusativ", "sehen verlangt den Akkusativ"),
("kaufen takes Akkusativ", "kaufen verlangt den Akkusativ"),
("finden takes Akkusativ", "finden verlangt den Akkusativ"),
("helfen always takes Dativ", "helfen verlangt immer den Dativ"),
("danken always takes Dativ", "danken verlangt immer den Dativ"),
("antworten takes Dativ", "antworten verlangt den Dativ"),
("the thing that belongs", "was jemandem gehört"),
("gehören takes Dativ", "gehören verlangt den Dativ"),
("the thing that pleases", "was gefällt"),
("gefallen takes Dativ", "gefallen verlangt den Dativ"),
("the one who receives → Dativ", "wer etwas bekommt → Dativ"),
("the thing given → Akkusativ", "was man gibt → Akkusativ"),
("the one who is shown → Dativ", "wem man etwas zeigt → Dativ"),
("the thing shown → Akkusativ", "was man zeigt → Akkusativ"),
("the thing that is put upright → Akkusativ", "was man hinstellt → Akkusativ"),
("auf + movement (Wohin?) → Akkusativ", "auf + Bewegung (Wohin?) → Akkusativ"),
("the thing that lies", "was liegt"),
("auf + place (Wo?) → Dativ", "auf + Ort (Wo?) → Dativ"),
("the thing that stands", "was steht"),
("in + place (Wo?) → Dativ", "in + Ort (Wo?) → Dativ"),
("in + movement (Wohin?) → Akkusativ", "in + Bewegung (Wohin?) → Akkusativ"),
("mit always takes Dativ", "mit verlangt immer den Dativ"),
("after sein → Nominativ (not Akkusativ!)", "nach sein → Nominativ (nicht Akkusativ!)"),
("sehen, kaufen, finden: what is seen, bought or found is Akkusativ.", "sehen, kaufen, finden: Was man sieht, kauft oder findet, steht im Akkusativ."),
("What gets bought is always Akkusativ.", "Was man kauft, steht immer im Akkusativ."),
("Akkusativ: the thing or person that is found.", "Akkusativ: die Sache oder Person, die man findet."),
("Dativ verbs to learn as a group: helfen, danken, antworten, gehören, gefallen.", "Diese Dativ-Verben lernt man als Gruppe: helfen, danken, antworten, gehören, gefallen."),
("You thank someone: Dativ, never Akkusativ.", "Man dankt jemandem: Dativ, nie Akkusativ."),
("You answer someone: Dativ.", "Man antwortet jemandem: Dativ."),
("Belonging to someone: the owner is Dativ.", "Etwas gehört jemandem: Der Besitzer steht im Dativ."),
("The thing is the subject, the person who likes it is Dativ.", "Die Sache ist das Subjekt, die Person, der sie gefällt, steht im Dativ."),
("Two objects: person = Dativ, thing = Akkusativ. The person comes first.", "Zwei Objekte: Person = Dativ, Sache = Akkusativ. Die Person steht zuerst."),
("Same pattern as geben.", "Gleiches Muster wie bei geben."),
("stellen = put upright: Wohin? So Akkusativ.", "stellen = irgendwohin stellen: Wohin? Also Akkusativ."),
("liegen = lies there: Wo? So Dativ. Compare legen.", "liegen = irgendwo liegen: Wo? Also Dativ. Vergleiche legen."),
("stehen = stands there: Wo? So Dativ. Compare stellen.", "stehen = irgendwo stehen: Wo? Also Dativ. Vergleiche stellen."),
("No movement, just being somewhere: Dativ.", "Keine Bewegung, man ist nur irgendwo: Dativ."),
("Movement towards a place: Akkusativ.", "Bewegung zu einem Ort: Akkusativ."),
("warten auf is a fixed pair, always with Akkusativ.", "warten auf ist ein festes Paar, immer mit Akkusativ."),
("denken an is a fixed pair, always with Akkusativ.", "denken an ist ein festes Paar, immer mit Akkusativ."),
("mit is always Dativ, whatever the verb.", "mit steht immer mit Dativ, egal welches Verb."),
("sein, werden, bleiben: the same case before and after the verb.", "sein, werden, bleiben: derselbe Fall vor und nach dem Verb."),
# Artikel und Präpositionen
("Only masculine changes: der → den", "Nur das Maskulinum ändert sich: der → den"),
("Plural = feminine, except DAT: den", "Plural = wie Femininum, außer im Dativ: den"),
("der = NOM m · DAT f · GEN f + pl", "der = NOM m · DAT f · GEN f + Pl."),
("Endings: -en, -em, -er, -es", "Endungen: -en, -em, -er, -es"),
("Neuter NOM = AKK: ein Kind", "Neutrum: NOM = AKK: ein Kind"),
("No plural: say keine / no article", "Kein Plural: man sagt keine / ohne Artikel"),
("kein, mein, dein: same as ein", "kein, mein, dein: wie ein"),
("Plural too: keine, meine, deine", "Auch im Plural: keine, meine, deine"),
("DAT plural: keinen Kindern (+n)", "Dativ Plural: keinen Kindern (+n)"),
("Only masculine changes: den", "Nur das Maskulinum ändert sich: den"),
("entlang follows: den Fluss entlang", "entlang steht nach dem Nomen: den Fluss entlang"),
("Plural noun gets -n: mit den Kindern", "Das Nomen im Plural bekommt -n: mit den Kindern"),
("Formal and written: needs the Genitiv", "Formell und schriftlich: verlangt den Genitiv"),
("Speech: wegen dem Wetter (DAT)", "Gesprochen: wegen dem Wetter (DAT)"),
("für, durch, gegen, ohne, um, bis: always Akkusativ. Only the masculine changes.", "für, durch, gegen, ohne, um, bis: immer Akkusativ. Nur das Maskulinum ändert sich."),
("aus, bei, mit, nach, seit, von, zu: always Dativ. The plural noun gets -n.", "aus, bei, mit, nach, seit, von, zu: immer Dativ. Das Nomen im Plural bekommt -n."),
("Wo? → Dativ · Wohin? → Akkusativ. Nine prepositions: an, auf, in, …", "Wo? → Dativ · Wohin? → Akkusativ. Neun Präpositionen: an, auf, in, …"),
("wegen, trotz, während: formal and written. A masc. / neut. noun takes -(e)s.", "wegen, trotz, während: formell und schriftlich. Maskulinum / Neutrum: Nomen bekommt -(e)s."),
]
done = 0; missing = []
for old, new in T:
    q = '"' + old + '"'
    n = s.count(q)
    if n:
        s = s.replace(q, '"' + new + '"'); done += 1
    elif ('"' + new + '"') not in s:
        missing.append(old)
a = "Every sentence is built from checked rules, so it is always correct."
if a in s:
    s = s.replace(a, "Jeder Satz wird aus geprüften Regeln gebaut, deshalb ist er immer richtig."); done += 1
if missing:
    print("NICHT GEFUNDEN:", missing)
if not done:
    print("nichts zu tun"); sys.exit()
s = re.sub(r'<meta name="app-version" content="[^"]+">', '<meta name="app-version" content="2026-11-22j">', s, count=1)
open(p, "w", encoding="utf-8").write(s); print("ersetzt:", done)
