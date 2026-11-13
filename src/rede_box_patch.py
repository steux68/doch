#!/usr/bin/env python3
"""Redewendungen: Liste wie bisher, aber in der Box mit rotem Schieber (wie Zitate). Idempotent. Aus dem Repo-Stamm ausfuehren."""
f="index.html"
s=open(f,encoding="utf8").read()
if 'aria-label="Redewendungen"' in s:
    print("already patched"); raise SystemExit
def rep(old,new):
    global s
    assert s.count(old)==1,(s.count(old),old[:70])
    s=s.replace(old,new)
rep("""+'</div>'+items.join("")+
   '<p class="tline">Stufe rechts""","""+'</div><div class="qbw"><div class="qbs" tabindex="0" role="region" aria-label="Redewendungen">'+items.join("")+'</div><div class="qsl" aria-hidden="true"><i></i></div></div>'+
   '<p class="tline">Stufe rechts""")
old_js=s[s.index('<script id="qbox-js">'):s.index('</script>',s.index('<script id="qbox-js">'))+len('</script>')]
new_js='''<script id="qbox-js">(function(){if(!window.qSlider)return;["p-quotes","p-rede"].forEach(function(id){var root=document.getElementById(id);if(!root)return;
function setup(){var sc=root.querySelector(".qbs"),sl=root.querySelector(".qbw>.qsl");if(!sc||!sl||sc._q)return;sc._q=1;window.qSlider(sc,sl);}
new MutationObserver(setup).observe(root,{childList:true});setup();});})();</script>'''
s=s.replace(old_js,new_js)
rep('content="2026-11-13b"','content="2026-11-13c"')
open(f,"w",encoding="utf8").write(s)
print("patched")
