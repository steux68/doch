# DOCH! 25.11.2026: (1) Schalter "Studieren | Staunen" -> "learn | wonder" (nur der Schalter; die Balken behalten ihre deutschen Namen),
# (2) Theorie-Popup: rundes Schliessen-X wie in Geschichte/Zitate statt nacktem "×". Idempotent.
import re, sys
s = open('index.html', encoding='utf-8').read()
if 'id="schliessen-css"' in s: sys.exit('schon angewendet')
R = [
 ('<span class="t1">Studieren</span><span class="pill"><i class="knob"></i></span><span class="t2">Staunen</span>',
  '<span class="t1">learn</span><span class="pill"><i class="knob"></i></span><span class="t2">wonder</span>'),
 ('t.setAttribute("aria-label","Studieren oder Staunen")', 't.setAttribute("aria-label","learn oder wonder")'),
 ('<button id="px" aria-label="Schließen">×</button>',
  '<button id="px" class="tlx" aria-label="Schließen"><svg viewBox="-12 -12 24 24" aria-hidden="true"><circle class="rg" r="9.5"/><path class="xx" d="M-3.6 -3.6L3.6 3.6M3.6 -3.6L-3.6 3.6"/></svg></button>'),
]
for a, b in R:
    assert s.count(a) == 1, a[:50]
    s = s.replace(a, b, 1)
css = '<style id="schliessen-css">#px.tlx{padding:8px;margin:-6px;font-size:inherit;line-height:0;flex:none}</style>'
s = s.replace('</head>', css + '</head>', 1)
if '--noversion' not in sys.argv:
    s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1) + '2026-11-25f' + m.group(3), s, count=1)
open('index.html', 'w', encoding='utf-8').write(s)
print('ok')
