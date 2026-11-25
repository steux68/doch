# DOCH! 25.11.2026: ein Neon-Gelb (#cdff3e) fuer aktive Knoepfe: Modus-Reiter Lernen/Spiel/Theorie, "Pruefen", Weiter-/Start-Knoepfe (.dgo, .hbar .t).
# Grammatik-Markierungen (.rgsn .e, .svo.on ...) und Marker-Punkte bleiben unveraendert. Idempotent.
import re, sys
s = open('index.html', encoding='utf-8').read()
if 'id="farbe-done"' in s: sys.exit('schon angewendet')
R = [
 ('.seg #mLearn[aria-pressed="true"],.seg #mGame[aria-pressed="true"],.seg #mTheo[aria-pressed="true"]{background:var(--hl),#e4f7a0;color:#222}',
  '.seg #mLearn[aria-pressed="true"],.seg #mGame[aria-pressed="true"],.seg #mTheo[aria-pressed="true"]{background:var(--hl),#cdff3e;color:#222}'),
 ('.dgo{background:var(--yellow);', '.dgo{background:var(--lime);'),
 ('.hbar .t{background:var(--yellow);', '.hbar .t{background:var(--lime);'),
 ('.tst[data-l="mix"]{background:var(--yellow)}', '.tst[data-l="mix"]{background:var(--lime)}'),
 ('font-size:15px;font-weight:500;background:#ffd400;color:#222;border:0;border-radius:0}', 'font-size:15px;font-weight:500;background:#cdff3e;color:#222;border:0;border-radius:0}'),
]
for a, b in R:
    assert s.count(a) == 1, a[:50]
    s = s.replace(a, b, 1)
s = s.replace('</head>', '<meta id="farbe-done" name="farbe" content="1"></head>', 1)
if '--noversion' not in sys.argv:
    s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1) + '2026-11-25d' + m.group(3), s, count=1)
open('index.html', 'w', encoding='utf-8').write(s)
print('ok')
