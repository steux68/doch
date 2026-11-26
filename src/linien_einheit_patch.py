# DOCH! 26.11.2026: Linienfarben vereinheitlicht (#b9b9b5 -> #b8b8b8). Idempotent (Text-Ersetzung).
import re, sys
s = open('index.html', encoding='utf-8').read()
n = s.count('#b9b9b5')
s = s.replace('#b9b9b5', '#b8b8b8')
if '--noversion' not in sys.argv and n:
    s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1) + '2026-11-26zt' + m.group(3), s, count=1)
open('index.html', 'w', encoding='utf-8').write(s); print('ok', n)
