# Schriftgroessen auf wenige Stufen vereinheitlichen: 12 / 14 / 16 px (kleine Marken <9.5px und Titel ab 19px bleiben). Idempotent.
import re, sys
s = open('index.html', encoding='utf-8').read()
if '<!--type-scale-->' in s:
    print('schon angewendet'); sys.exit(0)
n = 0
def snap(px):
    if px < 9.5 or px >= 19: return None
    return 12 if px < 13 else 14 if px < 15.5 else 16
def f(m):
    global n
    v = float(m.group(1)); px = v * 16 if m.group(2) == 'rem' else v
    t = snap(px)
    if t is None or t == px: return m.group(0)
    n += 1
    return 'font-size:%dpx' % t
s = re.sub(r'font-size:(\d*\.?\d+)(rem|px)(?![\w.%])', f, s)
print('ersetzt', n)
s = s.replace('</head>', '<!--type-scale--></head>', 1)
if '--noversion' not in sys.argv:
    s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1) + m.group(2) + 't' + m.group(3), s, count=1)
open('index.html', 'w', encoding='utf-8').write(s)
