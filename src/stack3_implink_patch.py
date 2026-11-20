# 20.11.2026: Balken IMPRESSUM entfaellt (beide Modi); stattdessen ein roter Link "Impressum" unten rechts unter den Linien,
# er oeffnet das Info-Fenster beim Impressum. Der Link im Fuss (Titelseite) macht dasselbe. Idempotent.
import re, sys
s = open('index.html', encoding='utf-8').read()
if 'id="implink"' in s:
    print('schon vorhanden'); sys.exit(0)
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (a[:70], s.count(a)); s = s.replace(a, b)
rep(',["imp","Impressum"]', '', 2)
rep('<section class="hp" id="p-imp"></section>', '')
i = s.index('/* IMPRESSUM */'); j = s.index('/* Einstieg')
s = s[:i] + s[j:]
rep('const ib=document.querySelectorAll("#hscroll>.hb");if(ib[4]){const sm=ib[4].querySelector("small");if(sm)sm.textContent="";}', '')
# neuer Link-Code: Info-Fenster, gescrollt zum Impressum
i = s.index('<script id="infolink2">'); j = s.index('</script>', i) + len('</script>')
JS = '''<script id="infolink2">(function(){var l=document.getElementById('infoLink');
function open(e){if(e){e.stopPropagation();e.preventDefault();}var c=document.getElementById('cogb');if(c)c.click();
 requestAnimationFrame(function(){var b=document.getElementById('setb'),h=document.getElementById('impH');if(b&&h)b.scrollTop=h.getBoundingClientRect().top-b.getBoundingClientRect().top+b.scrollTop-8;});}
if(l){l.textContent='Impressum';l.onclick=open;}
var r=document.getElementById('implink');if(r)r.onclick=open;})();</script>'''
s = s[:i] + JS + s[j:]
rep('  </section>\n\n  <!-- TOPIC -->', '  <div class="implink"><button type="button" id="implink">Impressum</button></div>\n  </section>\n\n  <!-- TOPIC -->')
rep('.endblk.enter{padding:8px 0 24px}', '.endblk.enter{padding:8px 0 24px}\n.implink{flex:none;display:flex;justify-content:flex-end;padding:5px 0 3px;background:#fff}\n#implink{border:0;background:none;padding:2px 0;font:inherit;font-size:11px;letter-spacing:1.4px;text-transform:uppercase;color:var(--red,#e30613);cursor:pointer;position:relative}\n#implink::before{content:"";position:absolute;left:-12px;right:-6px;top:-8px;bottom:-8px}')
s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1) + '2026-11-20i' + m.group(3), s, count=1)
open('index.html', 'w', encoding='utf-8').write(s)
print('ok')
