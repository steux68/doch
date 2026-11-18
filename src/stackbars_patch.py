# 18.11.2026: Startseite - sechs Balken in voller Breite (je eine Zeile, 25 px, Grossbuchstaben), gepunktete Linien und Farben bleiben.
# Der Balken des aktuellen Abschnitts klebt oben, die folgenden warten unten (wie bisher). Idempotent.
import re, sys
s = open('index.html', encoding='utf-8').read()
if 'id="stack-css"' in s:
    print('schon vorhanden'); sys.exit(0)
H = 25; HB = H - 1
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (a, s.count(a)); s = s.replace(a, b)
rep('const HB=22,ROWS=Math.ceil(SECS.length/2),', 'const HB=%d,ROWS=SECS.length,' % HB)
rep('const r=i>>1,b=document.createElement("div")', 'const r=i,b=document.createElement("div")')
rep('secEl(k).style.scrollMarginTop=(r*HB+22)+"px"', 'secEl(k).style.scrollMarginTop=(r*HB+%d)+"px"' % HB)
rep('PAGES[i].offsetTop-((i>>1)*HB+22)', 'PAGES[i].offsetTop-(i*HB+%d)' % HB)
rep('SC.clientHeight-((i>>1)*HB+22)-((ROWS-1-(i>>1))+(i%2?0:(i+1<SECS.length?1:0)))*HB', 'SC.clientHeight-(i*HB+%d)-(SECS.length-1-i)*HB' % HB)
css = '''<style id="stack-css">
.hb{--hv:linear-gradient(transparent,transparent)!important;height:%dpx!important;font-size:13px!important;padding:0 12px!important}
.hb b{text-transform:uppercase;letter-spacing:1.6px;font-size:12.5px}
.hb small{font-size:9.5px!important;margin-left:6px!important;letter-spacing:.5px}
.hb.hl,.hb.hr{margin:%dpx 0 -1px 0!important}
.hb.first{margin-top:14px!important}
</style>
</head>''' % (H, HB)
rep('</head>', css)
s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1) + '2026-11-18a' + m.group(3), s, count=1)
open('index.html', 'w', encoding='utf-8').write(s)
print('ok')
