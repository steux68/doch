# 18.11.2026: Zugaenglichkeit, unsichtbar: Pfeil-Knoepfe der Lernen-Leiste bekommen Namen (zurueck/weiter), Textlinks (Hilfsmittel, Wikipedia)
# und die "EN"-Chips bekommen eine groessere Beruehrungsflaeche, .app ist role="main". Aussehen unveraendert. Idempotent.
# Zurueck: git revert <dieser Commit> oder git checkout restore-2026-11-18b -- index.html
import re, sys
s = open('index.html', encoding='utf-8').read()
if 'id="a11y-css"' in s:
    print('schon vorhanden'); sys.exit(0)
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (a, s.count(a)); s = s.replace(a, b)
rep('b.disabled=!!d;if(fn)b.onclick=fn;return b;}', 'b.disabled=!!d;if(fn)b.onclick=fn;if(c==="ob-a")b.setAttribute("aria-label",/rotate\\(180\\)/.test(h)?"zurück":"weiter");return b;}')
css = '''<style id="a11y-css">
.hp .rows a,.hp a.wk{position:relative}
.hp .rows a::after,.hp a.wk::after{content:"";position:absolute;left:-6px;right:-6px;top:50%;height:44px;transform:translateY(-50%)}
.hp .rwi button.rwb{--hh:44px}
</style>
</head>'''
rep('</head>', css)
s = s.rstrip('\n') + '\n<script id="a11y-js">(function(){var a=document.querySelector(".app");if(a&&!a.getAttribute("role"))a.setAttribute("role","main");})();</script>\n'
s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1) + '2026-11-18c' + m.group(3), s, count=1)
open('index.html', 'w', encoding='utf-8').write(s)
print('ok')
