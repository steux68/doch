# DOCH! 26.11.2026: "Einfuehrung - Hinweise noch einmal zeigen" in Info & Einstellungen: setzt den Zaehler doch-fw zurueck,
# schliesst das Fenster und zeigt die Hinweise der Reihe nach wieder (Start -> Thema -> weiter). Idempotent.
import re, sys
s = open('index.html', encoding='utf-8').read()
if 'id="fwr-js"' in s: sys.exit('schon angewendet')
a = '<div class="timer"><span>Artikel-Hilfe <small class="n">Grundform vor der Antwort zeigen</small></span><button id="ahp" aria-pressed="false">aus</button></div>'
assert s.count(a) == 1
s = s.replace(a, a + '<div class="timer"><span>Einführung <small class="n">Hinweise noch einmal zeigen</small></span><button type="button" data-fwr="1">zeigen</button></div>')
js = ('<script id="fwr-js">(function(){document.addEventListener("click",function(e){var b=e.target.closest&&e.target.closest("[data-fwr]");if(!b)return;'
      'try{localStorage.setItem("doch-fw","0")}catch(x){}'
      'try{var sp=document.getElementById("setpop"),sx=document.getElementById("setx");if(sp&&!sp.hidden&&sx)sx.click();}catch(x){}'
      'setTimeout(function(){try{if(typeof goHome==="function")goHome();var h=document.getElementById("hscroll");if(h)h.scrollTop=0;if(typeof enterMap==="function")enterMap();}catch(x){}},400);});})();</script>')
s = s.rstrip('\n') + '\n' + js + '\n'
if '--noversion' not in sys.argv:
    s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1) + '2026-11-26zb' + m.group(3), s, count=1)
open('index.html', 'w', encoding='utf-8').write(s)
print('ok')
