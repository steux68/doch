#!/usr/bin/env python3
"""Karte "Satz korrigieren" bei Verben mit Präpositionen (Steuart, 13 Nov 2026).
Vier typische Lernerfehler, Antippen zeigt Lösung + Begründung. Nutzt die CSS-Klasse .kzk aus
korrigieren_wechselpraep_patch.py (wird bei Bedarf mit eingefügt). Zählt app-version hoch.
Aufruf im Repo-Hauptordner: python3 src/korrigieren_vprep_patch.py"""
import re, sys
p = "index.html"
s = open(p, encoding="utf-8").read()
if 'kzk vp' in s:
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
    return ('<details><summary>' + wrong.replace(bad, '<s>' + bad + '</s>') + '</summary>'
            '<p class="lsg">' + fix + '<small>' + why + '</small></p></details>')

HTML = ('<div class="tc df kzk vp"><h3>Satz korrigieren <small>A2–B2</small></h3>\n'
 + item("Ich warte für den Bus.", "für",
        'Ich warte <b>auf</b> den Bus.', "warten auf: Verb und Präposition gehören fest zusammen.") + "\n"
 + item("Wofür wartest du? Auf meinen Freund.", "Wofür",
        '<b>Auf wen</b> wartest du? Auf meinen Freund.', "Bei Personen bleibt die Präposition: auf wen, nicht wo-.") + "\n"
 + item("Ich denke über dich.", "über",
        'Ich denke <b>an</b> dich.', "denken an. (nachdenken über ist ein anderes Verb.)") + "\n"
 + item("Ich interessiere mich an Architektur.", "an",
        'Ich interessiere mich <b>für</b> Architektur.', "sich interessieren für: die Präposition ist nicht übersetzbar, lerne sie mit dem Verb.") + "\n"
 + '<p class="tline">Verb und Präposition immer als Block lernen.</p></div>\n')

anchor = '<div class="tc df"><h3>Gleiches Verb, andere Bedeutung</h3>'
if s.count(anchor) != 1:
    sys.exit("HTML-Anker nicht eindeutig")
s = s.replace(anchor, HTML + anchor, 1)

m = re.search(r'name="app-version" content="(\d{4}-\d\d-\d\d)([a-z]?)"', s)
if m:
    nxt = chr(ord(m.group(2) or "`") + 1)
    s = s.replace(m.group(0), 'name="app-version" content="%s%s"' % (m.group(1), nxt), 1)
open(p, "w", encoding="utf-8").write(s)
print("OK – app-version erhöht, Karte eingefügt")
