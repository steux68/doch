# 20.11.2026: blaues "EN" wieder rechts neben der Stufe; Hinweiszeilen unter Zitate und Redewendungen weg; die Liste fuellt in STAUNEN die Seite bis zum unteren Balken.
import re
s = open('index.html', encoding='utf-8').read()
if 'stack6-css' in s: print('schon live'); raise SystemExit
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (a[:70], s.count(a)); s = s.replace(a, b)
rep("""+'<p class="tline">Antippen öffnet das Zitat, dort steht der Link zur Quelle. Bilder: Wikipedia / Wikimedia Commons.</p>';}""", ";}")
rep("""+
   '<p class="tline">Stufe rechts: B1 bis C1. Antippen zeigt Englisch und einen Beispielsatz. Eine Herkunft steht nur da, wo ich sie in Duden, DWDS oder Wikipedia gefunden habe. Erst die Wendung selbst benutzen, dann nachsehen.</p></div>';}""", "+'</div>';}")
rep("""<span class="rwl">'+r[1]+'</span></span>""", """<span class="rwr"><span class="rwl">'+r[1]+'</span><button type="button" class="rwb" aria-expanded="false" aria-controls="rwe'+i+'" aria-label="English">EN</button></span></span>""")
rep('b.setAttribute("aria-expanded",o?"false":"true");e.hidden=o;};b.onclick=tg;b.onkeydown=ev=>{',
    'b.setAttribute("aria-expanded",o?"false":"true");const bt=b.querySelector(".rwb");if(bt)bt.setAttribute("aria-expanded",o?"false":"true");e.hidden=o;};b.onclick=tg;b.onkeydown=ev=>{if(ev.target.closest&&ev.target.closest(".rwb"))return;')
CSS = '''<style id="stack6-css">
.hp .rwi .rwr{display:flex;align-items:baseline;gap:8px;flex:none}
.hp .rwi .rwt button.rwb{position:relative;margin:0;padding:1px 7px 2px;font-size:11.5px;line-height:1.2}
.hp .rwi .rwt button.rwb::before{content:"";position:absolute;inset:-12px -8px}
html[data-dmode="s"] #hscroll[data-sec="quotes"] #p-quotes,html[data-dmode="s"] #hscroll[data-sec="rede"] #p-rede{display:flex!important;flex-direction:column;overflow:hidden!important}
html[data-dmode="s"] #p-quotes>.tc,html[data-dmode="s"] #p-rede>.tc{flex:1 1 0;min-height:0;display:flex;flex-direction:column}
html[data-dmode="s"] #p-quotes .qbw,html[data-dmode="s"] #p-rede .qbw{flex:1 1 0;min-height:0}
html[data-dmode="s"] #p-quotes .qbs,html[data-dmode="s"] #p-rede .qbs{height:100%}
</style>
'''
rep('<script id="stack4-js">', CSS + '<script id="stack4-js">')
s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1) + '2026-11-20o' + m.group(3), s, count=1)
open('index.html', 'w', encoding='utf-8').write(s); print('ok')
