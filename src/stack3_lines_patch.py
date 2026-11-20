# 20.11.2026: Jeder Menuebalken bekommt seine gepunktete Linie oben (::before), damit sie zwischen den Balken nicht vom naechsten Balken verdeckt wird. Idempotent.
import re, sys
s = open('index.html', encoding='utf-8').read()
if 'id="stack3-lines-css"' in s:
    print('schon vorhanden'); sys.exit(0)
CSS = '''<style id="stack3-lines-css">
html body .hb::before{content:"";position:absolute;left:0;right:0;top:0;height:1px;z-index:2;pointer-events:none;background:repeating-linear-gradient(to right,#b8b8b8 0 1px,transparent 1px 3px)!important}
</style>
'''
a = '<script id="info-link-js">'
assert s.count(a) == 1
s = s.replace(a, CSS + a)
s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1) + '2026-11-20l' + m.group(3), s, count=1)
open('index.html', 'w', encoding='utf-8').write(s)
print('ok')
