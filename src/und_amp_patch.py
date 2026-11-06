# "und" in Knopf- und Kachelbeschriftungen durch "&" ersetzen (HTML-Stellen als &amp;). Idempotent. 06.11.2026
import re, sys
s = open('index.html', encoding='utf-8').read()
HTML = ['<h3>Aktiv und Passiv</h3>', '<h3>Objekte und Pronomen <small>', '<h3>Partizip I und II</h3>', '<h3>da- und wo-</h3>',
        '>Text kopieren und LanguageTool öffnen</button>']
TXT = ['Personalpronomen im Akkusativ und Dativ', 'Präpositionen mit Dativ und Akkusativ', 'Regeln nach Endung und ein schnelles Spiel',
       'Verb an Position 2 und die Satzklammer', 'formelles Deutsch für Briefe und Vorträge', 'Wortschatz und Grammatik je Stufe',
       'Häufigkeit von Wörtern und typische Nachbarn', 'Modellsätze und Infos A1–C2']
n = 0
for t in HTML:
    n += s.count(t); s = s.replace(t, t.replace(' und ', ' &amp; '))
for t in TXT:
    n += s.count(t); s = s.replace(t, t.replace(' und ', ' & '))
print('ersetzt:', n)
if '--noversion' not in sys.argv:
    s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1) + '2026-11-06c' + m.group(3), s, count=1)
open('index.html', 'w', encoding='utf-8').write(s)
