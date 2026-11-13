#!/usr/bin/env python3
"""Karte "Satz korrigieren" (Steuart, 13 Nov 2026): kompakte Übung unter "Das Verb verrät den Fall".
Vier falsche Sätze, Antippen zeigt Lösung + Begründung (details/summary, kein JS). Zählt app-version hoch.
Aufruf im Repo-Hauptordner: python3 src/korrigieren_wechselpraep_patch.py"""
import re, sys
p = "index.html"
s = open(p, encoding="utf-8").read()
if "kzk wp" in s:
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
anchor_css = "\nmark.d{color:var(--dat)} mark.a{color:var(--akk)}"
if ".kzk summary{" not in s:
    if anchor_css not in s:
        sys.exit("CSS-Anker nicht gefunden")
    s = s.replace(anchor_css, CSS + anchor_css, 1)

def item(wrong, bad, fix, why):
    return ('<details><summary>' + wrong.replace(bad, '<s>' + bad + '</s>') + '</summary>'
            '<p class="lsg">' + fix + '<small>' + why + '</small></p></details>')

HTML = ('<div class="tc df kzk wp"><h3>Satz korrigieren <small>A2–B1</small></h3>\n'
 + item("Ich lege das Buch auf dem Tisch.", "auf dem",
        'Ich lege das Buch auf <mark class="a">den</mark> Tisch.', "Wohin? Bewegung → Akkusativ.") + "\n"
 + item("Das Bild hängt an die Wand.", "an die",
        'Das Bild hängt an <mark class="d">der</mark> Wand.', "Wo? Es hängt schon dort → Dativ.") + "\n"
 + item("Er setzt sich auf dem Stuhl.", "auf dem",
        'Er setzt sich auf <mark class="a">den</mark> Stuhl.', "Wohin? setzen = Bewegung → Akkusativ.") + "\n"
 + item("Die Vase steht auf das Regal.", "auf das",
        'Die Vase steht auf <mark class="d">dem</mark> Regal.', "Wo? stehen = Position → Dativ.") + "\n"
 + '<p class="tline">Erst fragen: Wo? oder Wohin? Dann den Artikel wählen.</p></div>\n\n')

anchor = '<div class="tc df"><h3>Wo · Wohin · Woher <small>B1–B2</small></h3>'
if s.count(anchor) != 1:
    sys.exit("HTML-Anker nicht eindeutig")
s = s.replace(anchor, HTML + anchor, 1)

m = re.search(r'name="app-version" content="(\d{4}-\d\d-\d\d)([a-z]?)"', s)
if m:
    nxt = chr(ord(m.group(2) or "`") + 1)
    s = s.replace(m.group(0), 'name="app-version" content="%s%s"' % (m.group(1), nxt), 1)
open(p, "w", encoding="utf-8").write(s)
print("OK – app-version erhöht, Karte eingefügt")
