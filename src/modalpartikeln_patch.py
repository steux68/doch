#!/usr/bin/env python3
"""DOCH: neues Thema 'Modalpartikeln' (mpart), eigene Formulierung, Texte auf Deutsch (27 Nov 2026)."""
import re, sys
p = "index.html"; s = open(p, encoding="utf-8").read()
if "GT.mpart=" in s: sys.exit("already patched")
def J(l): return "[" + ",".join('"%s"' % x for x in l) + "]"
def Q(sent, o, why, lv): return ' {s:"%s",o:%s,why:"%s",lv:"%s"}' % (sent, J(o), why, lv)
def rows(items): return '<div class="rows">' + "".join('<div><span>%s</span><span>%s</span></div>' % (a, b) for a, b in items) + '</div>'
def tc(h, items, note): return '<div class="tc df"><h3>%s</h3>%s<p class="tline">%s</p></div>' % (h, rows(items), note)
def cards(C): return ",\n".join(' {b:"%s",st:%s,tx:"%s",gt:"%s"}' % c for c in C)

C = [
 ('Was sie tun', 'ruleSt("Ohne und mit Partikel",["Komm mit. (neutral, fast ein Befehl)","Komm doch mit! (freundlich, einladend)","Wo wohnst du? (neutral)","Wo wohnst du denn? (interessiert, weich)"])',
  'Modalpartikeln färben den Satz',
  'Sie ändern nicht den Inhalt, sondern den Ton: freundlich, erstaunt, ungeduldig oder beruhigend. Wörtlich übersetzen kann man sie kaum. Im Englischen übernimmt oft die Satzmelodie diese Aufgabe.'),
 ('doch', 'ruleSt("doch – vier Gesichter",["Kommst du nicht? – Doch! (Widerspruch)","Komm doch mit! (freundliche Aufforderung)","Das weißt du doch! (Erinnerung)","Wenn er doch käme! (Wunsch)"])',
  'Das Wort, nach dem die App heißt',
  'Als Antwort auf eine verneinte Frage heißt Doch: ja, im Gegenteil. Als Partikel macht doch Bitten weich und erinnert an etwas, das der andere schon weiß.'),
 ('ja', 'ruleSt("ja – erstaunt oder bekannt",["Das ist ja toll! (Erstaunen)","Du weißt ja, wie er ist. (bekannt)","Mach das ja nicht! (Warnung, betont)"])',
  'ja: Das überrascht mich, oder: Das wissen wir beide',
  'Unbetont drückt ja Erstaunen aus oder erinnert an Gemeinsames. Betont wird es zur Warnung.'),
 ('mal', 'ruleSt("mal macht Bitten leicht",["Komm mal her.","Kannst du mal kurz helfen?","Hör mal!"])',
  'mal kommt von einmal',
  'Die Bitte klingt klein und schnell erledigt. In der gesprochenen Sprache hört man mal ständig.'),
 ('denn', 'ruleSt("denn – nur in Fragen",["Wie heißt du denn?","Was ist denn los?","Bist du denn schon fertig?"])',
  'denn zeigt Interesse',
  'Die Frage wird weicher und persönlicher. Nicht verwechseln mit der Konjunktion denn (= weil) am Anfang eines Hauptsatzes.'),
 ('eben · halt', 'ruleSt("Nicht zu ändern",["Das ist eben so.","Dann nehmen wir halt den Bus.","Er ist halt müde."])',
  'So ist es, da kann man nichts machen',
  'eben und halt bedeuten fast dasselbe. halt hört man vor allem in Österreich und im Süden Deutschlands, eben eher im Norden.'),
 ('schon · wohl', 'ruleSt("Beruhigen und vermuten",["Das klappt schon. (beruhigt)","Er ist wohl krank. (vermutlich)","Das wird wohl stimmen."])',
  'schon nimmt die Sorge, wohl zeigt Unsicherheit',
  'Mit schon sagt man: Keine Angst, es geht gut. Mit wohl sagt man: Ich glaube es, bin mir aber nicht ganz sicher.'),
 ('eigentlich · bloß · aber', 'ruleSt("Noch drei häufige",["Wie alt bist du eigentlich? (neues Thema)","Was soll ich bloß tun? (ratlos)","Mach bloß keinen Fehler! (Warnung)","Du bist aber groß geworden! (Erstaunen)"])',
  'Themenwechsel, Ratlosigkeit, Staunen',
  'eigentlich öffnet in Fragen ein neues Thema. bloß und nur machen Fragen ratlos und Befehle zur Warnung. aber staunt über ein Ausmaß.'),
 ('Stellung', 'ruleSt("Immer im Mittelfeld",["Komm doch mal vorbei!","Das ist ja eigentlich ganz einfach.","Er hat halt keine Zeit.","Falsch: Doch komm mal vorbei."])',
  'Nach dem Verb, nie auf Platz 1, immer unbetont',
  'Stehen mehrere Partikeln zusammen, gilt meist diese Reihenfolge: ja · denn · doch · eben/halt · mal.'),
]
QQ = [
 Q("Hast du keinen Hunger? – ___! Ich habe großen Hunger.", ["Doch", "Ja", "Nein"], "Antwort auf eine verneinte Frage, die widerspricht: Doch.", "A1"),
 Q("Ist er nicht da? – ___, er ist im Garten.", ["Doch", "Ja", "Nein"], "Die Frage ist verneint, die Antwort widerspricht: Doch.", "A1"),
 Q("Komm ___ her! (freundliche Bitte)", ["mal", "bloß", "wohl"], "mal macht eine Bitte leicht und freundlich.", "A2"),
 Q("Gib mir ___ das Salz, bitte.", ["mal", "denn", "ja"], "Eine kleine Bitte: mal.", "A2"),
 Q("Komm ___ mit, das wird lustig!", ["doch", "denn", "wohl"], "Freundliche Aufforderung: doch. denn steht nur in Fragen.", "A2"),
 Q("Ruf ___ an, wenn du ankommst.", ["mal", "denn", "wohl"], "Eine kleine Bitte: mal.", "A2"),
 Q("Wie heißt du ___?", ["denn", "doch", "halt"], "In Fragen zeigt denn Interesse.", "B1"),
 Q("Was machst du ___ hier? (überrascht)", ["denn", "mal", "schon"], "Überraschte Frage: denn.", "B1"),
 Q("Das ist ___ toll! (Ich bin überrascht.)", ["ja", "denn", "mal"], "Erstaunen in einer Aussage: ja.", "B1"),
 Q("Das weißt du ___, das habe ich dir gestern gesagt.", ["doch", "denn", "mal"], "Erinnerung an Bekanntes: doch.", "B1"),
 Q("Ich hab ___ gesagt, dass es regnet!", ["doch", "denn", "wohl"], "Ein kleiner Vorwurf: Ich habe es schon gesagt – doch.", "B1"),
 Q("Der Zug ist weg. Das ist ___ so, da kann man nichts machen.", ["halt", "denn", "mal"], "Nicht zu ändern: halt (oder eben).", "B1"),
 Q("Er antwortet nicht. Er ist ___ krank. (Vermutung)", ["wohl", "mal", "denn"], "Vermutung: wohl.", "B2"),
 Q("Er wird ___ noch im Büro sein. (Vermutung)", ["wohl", "mal", "denn"], "Vermutung mit werden: wohl.", "B2"),
 Q("Mach dir keine Sorgen, das klappt ___.", ["schon", "denn", "mal"], "Beruhigung: schon.", "B2"),
 Q("Wie alt bist du ___? (neues Thema)", ["eigentlich", "mal", "halt"], "Themenwechsel in einer Frage: eigentlich.", "B2"),
 Q("Wenn ich ___ mehr Zeit hätte!", ["nur", "denn", "halt"], "Wunsch im Konjunktiv II: nur (oder doch, bloß).", "B2"),
 Q("Fass das ___ nicht an! (Warnung)", ["bloß", "mal", "denn"], "Warnung: bloß (oder ja, betont).", "B2"),
 Q("Du bist ___ groß geworden! (Erstaunen)", ["aber", "denn", "mal"], "Staunen über ein Ausmaß: aber.", "B2"),
 Q("Du kommst ___ morgen, oder? (Ich erwarte ein Ja.)", ["doch", "denn", "mal"], "doch erinnert an etwas Vereinbartes.", "B2"),
 Q("Na gut, dann probier es ___!", ["halt", "denn", "wohl"], "Etwas resigniert: halt (oder eben).", "B2"),
 Q("Modalpartikeln stehen im ___.", ["Mittelfeld", "Vorfeld", "Nachfeld"], "Nach dem Verb, nie auf Platz 1.", "B2"),
 Q("Richtig ist: ___", ["Komm doch mal vorbei!", "Komm mal doch vorbei!", "Doch komm mal vorbei!"], "Reihenfolge: doch vor mal, und nie auf Platz 1.", "C1"),
 Q("Wer war das ___? (ratlose Frage)", ["bloß", "mal", "halt"], "Ratlose Frage: bloß (oder nur, denn).", "C1"),
]
TH = ''.join([
 tc("Die Partikeln", [("doch", "freundlich, erinnernd · Aufforderung, Aussage"), ("ja", "erstaunt, bekannt · Aussage"), ("mal", "leicht · Bitte"), ("denn", "interessiert · Frage"), ("eben · halt", "nicht zu ändern · Aussage"), ("schon", "beruhigend · Aussage"), ("wohl", "vermutend · Aussage"), ("eigentlich", "neues Thema · Frage"), ("bloß · nur", "ratlos, warnend · Frage, Befehl"), ("aber", "erstaunt · Ausruf")], "Sie ändern den Ton, nicht den Inhalt."),
 tc("Doch als Antwort", [("Kommst du?", "Ja. / Nein."), ("Kommst du nicht?", "Doch! (ich komme) / Nein.")], "Doch widerspricht einer verneinten Frage oder Aussage."),
 tc("Stellung", [("Mittelfeld", "Komm doch mal vorbei!"), ("Reihenfolge", "ja · denn · doch · eben/halt · mal"), ("Betonung", "unbetont, sonst ändert sich die Bedeutung")], "Nie auf Platz 1 im Satz."),
])
MP = ('GT.mpart={name:"Modalpartikeln",badge:"Partikel",tip:"Frag dich: Welchen Ton soll der Satz haben? Freundlich, erstaunt, beruhigend oder ungeduldig?",src:["duden","grammis","lingolia"],\n'
      ' lg:\'<span><b class="wt k lgk">doch</b> Partikel</span>\',\n cards:[\n' + cards(C) + '],\n q:[\n' + ",\n".join(QQ) + '],\n th:`' + TH + '`};\n')

a = '/* ---------- topics + home ---------- */'
if s.count(a) != 1: sys.exit("Anker topics")
s = s.replace(a, "/* mpart */\n" + MP + a)

a = ' {t:"neg",n:"Verneinung",tag:"nicht · kein",ds:"nicht oder kein, und wo nicht steht · A1–B1"},'
if s.count(a) != 1: sys.exit("Anker TOPICS neg")
s = s.replace(a, a + '\n {t:"mpart",n:"Modalpartikeln",tag:"doch · ja · mal",ds:"Ton statt Inhalt: doch, ja, mal, denn, halt, schon · A1–C1"},')

a = '{n:"Satz",t:["satz","tekamolo","neg","konn",'
if s.count(a) != 1: sys.exit("Anker Satz")
s = s.replace(a, '{n:"Satz",t:["satz","tekamolo","neg","mpart","konn",')

a = 'if(k==="art")return "Artikel";'
if s.count(a) != 1: sys.exit("Anker lab")
s = s.replace(a, a + 'if(k==="mpart")return "Modalpartikel";')

a = 'konn:["satz"],'
if s.count(a) != 1: sys.exit("Anker PRE")
s = s.replace(a, 'konn:["satz"],mpart:["satz"],')

m = re.search(r'name="app-version" content="([^"]*)"', s)
new = "2026-11-27-mpart"
s = s.replace(m.group(0), 'name="app-version" content="%s"' % new)
open(p, "w", encoding="utf-8").write(s)
open("version.txt", "w").write(new + "\n")
print("OK", new)
