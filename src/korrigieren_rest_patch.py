#!/usr/bin/env python3
"""Drei Karten "Satz korrigieren" (Steuart, 13 Nov 2026): Konnektoren (Verb am Ende), TEKAMOLO und Pronomen,
Artikel und Endungen. Antippen zeigt Lösung + Begründung (details/summary, kein JS). Zählt app-version hoch.
Aufruf im Repo-Hauptordner: python3 src/korrigieren_rest_patch.py"""
import re, sys
p = "index.html"
s = open(p, encoding="utf-8").read()
if "kzk rest" in s:
    sys.exit("already patched")

CSS = """
/* Satz korrigieren (13 Nov): kompakte Zeilen, Lösung per Antippen */
.kzk details{padding:6px 0;background:var(--df) left bottom/100% 1px no-repeat}
.kzk summary{cursor:pointer;list-style:none;font-size:16px;line-height:1.35}
.kzk summary::-webkit-details-marker{display:none}
.kzk summary s{color:var(--akk);text-decoration-thickness:2px}
.kzk summary:after{content:"  ▸";color:var(--muted);font-size:13px}
.kzk details[open] summary:after{content:"  ▾"}
.kzk .lsg{margin:4px 0 2px;font-size:15px}
.kzk .lsg small{display:block;color:var(--muted);font-size:14px}
"""
if ".kzk summary{" not in s:
    a = "\nmark.d{color:var(--dat)} mark.a{color:var(--akk)}"
    if a not in s:
        sys.exit("CSS-Anker nicht gefunden")
    s = s.replace(a, CSS + a, 1)

def item(wrong, bad, fix, why):
    assert bad in wrong, wrong
    return ('<details><summary>' + wrong.replace(bad, '<s>' + bad + '</s>') + '</summary>'
            '<p class="lsg">' + fix + '<small>' + why + '</small></p></details>')

def card(level, items, tip):
    return ('<div class="tc df kzk rest"><h3>Satz korrigieren <small>' + level + '</small></h3>\n'
            + "\n".join(item(*i) for i in items) + '\n<p class="tline">' + tip + '</p></div>\n')

KONN = card("B1", [
 ("Ich lerne Deutsch, weil ich wohne in Wien.", "ich wohne in Wien",
  "Ich lerne Deutsch, weil ich in Wien <b>wohne</b>.", "Nach weil geht das Verb ans Ende."),
 ("Ich weiß, dass er kommt heute.", "er kommt heute",
  "Ich weiß, dass er heute <b>kommt</b>.", "Nach dass steht das Verb am Ende."),
 ("Weil es regnet, wir bleiben zu Hause.", "wir bleiben zu Hause",
  "Weil es regnet, <b>bleiben wir</b> zu Hause.", "Nebensatz zuerst: Nach dem Komma folgt sofort das Verb."),
 ("Ich rufe dich an, wenn ich habe Zeit.", "ich habe Zeit",
  "Ich rufe dich an, wenn ich Zeit <b>habe</b>.", "wenn ist ein Nebensatz-Konnektor: Verb am Ende."),
], "Erst fragen: Ist es ein Nebensatz? Dann steht das Verb am Ende.")

TEKA = card("B1", [
 ("Ich gebe das Buch ihr.", "das Buch ihr",
  "Ich gebe <b>ihr das Buch</b>.", "Pronomen zuerst."),
 ("Ich gebe dir es.", "dir es",
  "Ich gebe <b>es dir</b>.", "Zwei Pronomen: erst Akkusativ, dann Dativ."),
 ("Ich fahre nach Wien morgen mit dem Zug.", "nach Wien morgen mit dem Zug",
  "Ich fahre <b>morgen mit dem Zug nach Wien</b>.", "Normalfall: Te – Ka – Mo – Lo."),
 ("Ich schenke einen Ring meiner Mutter.", "einen Ring meiner Mutter",
  "Ich schenke <b>meiner Mutter einen Ring</b>.", "Zwei Nomen: erst Dativ, dann Akkusativ."),
], "TEKAMOLO ist der sichere Normalfall, kein Gesetz.")

ART = card("A1–B1", [
 ("Das Wohnung ist hell.", "Das",
  "<b>Die</b> Wohnung ist hell.", "-ung → immer die."),
 ("Die Mädchen ist neun Jahre alt.", "Die",
  "<b>Das</b> Mädchen ist neun Jahre alt.", "-chen → immer das, auch bei Mädchen."),
 ("Der Fenster ist offen.", "Der",
  "<b>Das</b> Fenster ist offen.", "-er-Falle: das Fenster, das Zimmer."),
 ("Der Haustür ist offen.", "Der",
  "<b>Die</b> Haustür ist offen.", "Das letzte Wort entscheidet: die Tür → die Haustür."),
], "Nomen immer mit Artikel lernen, als ein Wort.")

for name, anchor, html in [
 ("Konnektoren", '<div class="tc df"><h3>Paare, die man verwechselt</h3>', KONN),
 ("TEKAMOLO", '<div class="tc df"><h3>Wann gilt es nicht? <small>B1</small></h3>', TEKA),
 ("Artikel", '<div class="tc df"><h3>Komposita</h3>', ART)]:
    if s.count(anchor) != 1:
        sys.exit("HTML-Anker nicht eindeutig: " + name)
    s = s.replace(anchor, html + anchor, 1)

m = re.search(r'name="app-version" content="(\d{4}-\d\d-\d\d)([a-z]?)"', s)
if m:
    nxt = chr(ord(m.group(2) or "`") + 1)
    s = s.replace(m.group(0), 'name="app-version" content="%s%s"' % (m.group(1), nxt), 1)
open(p, "w", encoding="utf-8").write(s)
print("OK – app-version erhöht, drei Karten eingefügt")
