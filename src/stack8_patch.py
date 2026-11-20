# 20.11.2026: Kopf-Logo nimmt das gerade "D!" aus dem App-Symbol (icon-512.png, nachgezeichnet) statt des alten Zeichens.
import re
s = open('index.html', encoding='utf-8').read()
if 'class="lm"' in s: print('schon live'); raise SystemExit
D = open('src/icon_mark_path.txt').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (a[:70], s.count(a)); s = s.replace(a, b)
old_start = s.index('<path class="lx" d="M-12 2h24')
old_end = s.index('<text class="ld" x="0" y="25" font-size="22" text-anchor="middle">D</text>') + len('<text class="ld" x="0" y="25" font-size="22" text-anchor="middle">D</text>')
new = '<path class="lx lm" fill-rule="evenodd" transform="translate(0 2) scale(.1429) translate(-256 -62)" d="' + D + '"/>'
s = s[:old_start] + new + s[old_end:]
rep('<text class="ls" x="15.6" y="25" font-size="24">eutsche</text><text class="ls" x="28.0" y="49" font-size="24">Grammatik</text>',
    '<text class="ls" x="16.2" y="30.5" font-size="24">eutsche</text><text class="ls" x="28.0" y="54.5" font-size="24">Grammatik</text>')
s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1) + '2026-11-20q' + m.group(3), s, count=1)
open('index.html', 'w', encoding='utf-8').write(s); print('ok')
