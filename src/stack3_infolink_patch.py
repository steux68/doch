# 20.11.2026: Der Link "Info" im Fuss (Titelseite und Seitenende) heisst jetzt "Impressum" und springt zum Balken IMPRESSUM. Idempotent.
import re, sys
s = open('index.html', encoding='utf-8').read()
if 'id="infolink2"' in s:
    print('schon vorhanden'); sys.exit(0)
a = '<script id="info-link-js">'
i = s.index(a); j = s.index('</script>', i) + len('</script>')
JS = '''<script id="infolink2">(function(){var l=document.getElementById('infoLink');if(!l)return;l.textContent='Impressum';
l.onclick=function(e){e.stopPropagation();e.preventDefault();try{var t=secTop(4);SC.scrollTo({top:t,behavior:'smooth'});}catch(x){var c=document.getElementById('cogb');if(c)c.click();}};})();</script>'''
s = s[:j] + JS + s[j:]
s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1) + '2026-11-20h' + m.group(3), s, count=1)
open('index.html', 'w', encoding='utf-8').write(s)
print('ok')
