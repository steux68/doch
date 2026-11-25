# DOCH! 25.11.2026: Im Modus "wonder" fuehrt ein Tipp aufs Logo zurueck in den Modus "learn" und zur Titelseite
# (wie bei PASSAGE und dasein-design). Vorher blieb man in "wonder". Idempotent.
import re, sys
s = open('index.html', encoding='utf-8').read()
if 'id="wunder-logo-js"' in s: sys.exit('schon angewendet')
js = ('<script id="wunder-logo-js">(function(){document.addEventListener("click",function(e){'
      'if(!e.target.closest||!e.target.closest("#home h1.logo,#markb,#markL"))return;'
      'if(!document.querySelector(\'button[data-m="s"][aria-pressed="true"]\'))return;'
      'var d=document.querySelector(\'button[data-m="d"]\');if(d)d.click();},true);})();</script>')
s = s.rstrip('\n') + '\n' + js + '\n'
if '--noversion' not in sys.argv:
    s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1) + '2026-11-26p' + m.group(3), s, count=1)
open('index.html', 'w', encoding='utf-8').write(s)
print('ok')
