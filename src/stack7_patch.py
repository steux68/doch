# 20.11.2026: Teaser "mehr Geschichte" steht in STAUNEN direkt unter dem Balken GESCHICHTE (nicht zwischen Zitate und Redewendungen).
import re
s = open('index.html', encoding='utf-8').read()
if 'stack7-css' in s: print('schon live'); raise SystemExit
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (a[:70], s.count(a)); s = s.replace(a, b)
CSS = '''<style id="stack7-css">
html[data-dmode="s"] #hscroll>.capm{order:3;position:relative!important;top:auto!important;bottom:auto!important;flex:none;margin:0!important}
html[data-dmode="s"] #hscroll[data-sec="hist"]>.capm{display:none!important}
</style>
<script id="stack7-js">(function(){if(DMODE!=="s")return;const c=document.querySelector("#hscroll>.capm.p-hist"),b=document.querySelectorAll("#hscroll>.hb")[2];
if(c&&b)c.addEventListener("click",e=>{e.stopImmediatePropagation();e.preventDefault();b.click();},true);})();</script>
'''
rep('<script id="info-link-js">', CSS + '<script id="info-link-js">')
s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1) + '2026-11-20p' + m.group(3), s, count=1)
open('index.html', 'w', encoding='utf-8').write(s); print('ok')
