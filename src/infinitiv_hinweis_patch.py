#!/usr/bin/env python3
"""Infinitiv in Klammern bei Verb-Lücken (Steuart, 15 Nov 2026), z. B. 'Wir ___ nach Graz gefahren. (fahren)'.
Gilt für Perfekt, Passiv, Konjunktiv I/II, Modalverben, Präsens, Konnektoren (1 Satz). Nicht bei Wortschatz-Kollokationen (nvv)."""
import re, sys
p = "index.html"
s = open(p, encoding="utf-8").read()
if "/* inf-hinweis */" in s: sys.exit("already patched")
M = {
 "Wir ___ nach Graz gefahren.":"fahren","Ich ___ den Plan gezeichnet.":"zeichnen","Er ___ um sieben aufgestanden.":"aufstehen",
 "Das Fohlen ___ schnell gewachsen.":"wachsen","Wir ___ den ganzen Tag im Büro geblieben.":"bleiben",
 "Ich habe die Rechnung ___.":"bezahlen","Wir haben das Zimmer ___.":"aufräumen","Sie hat Architektur ___.":"studieren",
 "Hast du den Brief schon ___?":"schreiben","Ich habe dich nicht ___.":"verstehen","Gestern ___ ich keine Zeit.":"haben",
 "Als Kind ___ ich in Glasgow.":"wohnen","Nachdem er gegessen ___, ging er in den Stall.":"haben",
 "Morgen ___ ich den Plan abgeben.":"werden","Wann ___ der Unfall passiert?":"passieren","Ich bin lange im Café ___.":"sitzen",
 "Bis Freitag ___ ich den Bericht geschrieben haben.":"werden",
 "Das Auto ___ in der Werkstatt repariert.":"werden","Das Haus ___ 1912 gebaut.":"werden","Das Paket ist heute früh geliefert ___.":"werden",
 "Die Rechnung muss bis Freitag bezahlt ___.":"werden","Die Ergebnisse ___ morgen veröffentlicht.":"werden",
 "Dem Patienten ___ sofort geholfen.":"werden","Hier ___ nicht geraucht.":"werden","Ich weiß, dass hier viel gearbeitet ___.":"werden",
 "Wir warten, weil die Unterlagen noch unterschrieben werden ___.":"müssen","Das Problem lässt sich leicht ___.":"lösen",
 "Hier ___ ein neues Haus gebaut.":"werden","Die Fenster ___ gestern geputzt.":"werden","Das Gebäude war damals schon renoviert ___.":"werden",
 "Wenn ich Zeit ___, würde ich mehr zeichnen.":"haben","Wenn ich du ___, würde ich das Angebot annehmen.":"sein",
 "___ Sie mir bitte kurz helfen?":"können","Ich ___ gern einen Kaffee.":"haben","An deiner Stelle ___ ich früher losfahren.":"werden",
 "Wenn ich das gewusst ___, wäre ich gekommen.":"haben","Wenn der Zug pünktlich gewesen wäre, ___ wir den Termin geschafft.":"haben",
 "Er tut so, als ___ er nichts.":"wissen","Ich hätte früher kommen ___.":"sollen","Ich wünschte, ich ___ mehr Zeit.":"haben",
 "Wenn es nicht regnen ___, könnten wir ausreiten.":"werden","Es ___ schön, wenn du mitkommst.":"sein",
 "___ ich mehr Geld, würde ich ein Pferd kaufen.":"haben","___ es möglich, den Termin zu verschieben?":"sein",
 "Wenn er doch nur endlich ___!":"kommen","Ohne deine Hilfe ___ ich das nie geschafft.":"haben","Das ___ nicht nötig gewesen.":"sein",
 "Ich ___ gern gekommen, aber ich war krank.":"sein","Es wäre besser gewesen, wenn du früher gefragt ___.":"haben",
 "Fast ___ ich den Zug verpasst.":"haben","Sie ist zu müde, als dass sie noch arbeiten ___.":"können",
 "Der Minister sagt, er ___ zufrieden.":"sein","Er behauptet, er ___ keine Zeit.":"haben","Sie sagen, sie ___ keine Zeit.":"haben",
 "Laut Bericht ___ das Projekt teurer werden.":"werden","Er sagte, er ___ gestern in Graz gewesen.":"sein",
 "Sie erzählte, sie ___ den Plan abgegeben.":"haben","Der Arzt meint, ich ___ mehr schlafen.":"sollen",
 "Sie sagt: „Ich bin müde.“ → Sie sagt, sie ___ müde.":"sein","Die Firma teilt mit, man ___ die Preise erhöhen.":"werden",
 "Die Nachbarn sagen, sie ___ nichts gehört.":"haben",
 "Ich ___ gut schwimmen.":"können","Er ___ heute lange arbeiten.":"müssen","___ du mir bitte helfen?":"können","Ich ___ einen Kaffee, bitte.":"mögen",
 "Hier ___ man nicht rauchen.":"dürfen","Wir ___ morgen ins Kino gehen.":"wollen","Wenn du keine Zeit hast, ___ du nicht kommen.":"müssen",
 "Im Museum ___ man nicht fotografieren. Es ist verboten.":"dürfen","Ich ___ keinen Fisch.":"mögen","Der Arzt sagt, ich ___ mehr Wasser trinken.":"sollen",
 "Gestern ___ ich nicht kommen, ich war krank.":"können","Als Kind ___ er Pilot werden.":"wollen","Wenn du willst, ___ du gern mitkommen.":"können",
 "Ich gehe früh schlafen, weil ich morgen um fünf aufstehen ___.":"müssen","Ich weiß nicht, ob er morgen kommen ___.":"können",
 "Gestern habe ich länger arbeiten ___.":"müssen","___ Sie bitte das Fenster schließen?":"können","Du ___ mehr schlafen. Du siehst müde aus.":"sollen",
 "Du ___ nicht zu warten, ich komme allein.":"brauchen","Das neue Museum ___ im Juni eröffnet werden.":"sollen",
 "„Wolltest du das?“ – „Nein, das habe ich nicht ___.“":"wollen","Wir haben das Haus nicht verkaufen ___.":"wollen",
 "Er ist nicht im Büro. Er ___ krank sein – er fehlt nie.":"müssen","Bis Linz ___ es etwa zwei Stunden sein – genau weiß ich es nicht.":"dürfen",
 "Laut Zeitung ___ der Minister von dem Vertrag gewusst haben.":"sollen","Er ___ den Unfall nicht gesehen haben – das behauptet er jedenfalls.":"wollen",
 "Er muss den Termin vergessen ___.":"haben","Sie soll schon gestern abgereist ___.":"sein",
 "Er war die ganze Zeit hier. Er ___ den Brief nicht geschrieben haben.":"können","Er hätte den Fehler früher bemerken ___.":"müssen",
 "___ er auch reich sein – glücklich ist er nicht.":"mögen",
 "Ich ___ seit zehn Jahren in Wien.":"wohnen","Morgen ___ ich nach Salzburg.":"fahren","Kaum ___ er angekommen, klingelte das Telefon.":"sein",
}
n = 0; miss = []
for sent, inf in M.items():
    key = '{s:"' + sent + '"'
    c = s.count(key)
    if c == 0:
        # Teilsatz am Ende (Beispiele mit längerem Satzanfang)
        m = re.findall(r'\{s:"([^"]*' + re.escape(sent) + r')"', s)
        if len(m) == 1: key = '{s:"' + m[0] + '"'; sent = m[0]; c = 1
    if c != 1: miss.append((sent, c)); continue
    s = s.replace(key, '{s:"' + sent + ' (' + inf + ')"'); n += 1
if miss: sys.exit("nicht eindeutig: %r" % miss)
s = s.replace("</style>", "/* inf-hinweis */</style>", 1)
m = re.search(r'name="app-version" content="(\d{4}-\d\d-\d\d)([a-z]?)"', s)
if m: s = s.replace(m.group(0), 'name="app-version" content="%s%s"' % (m.group(1), chr(ord(m.group(2) or "`") + 1)))
open(p, "w", encoding="utf-8").write(s); print("OK", n)
