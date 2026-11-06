# Navigation wieder wie urspruenglich: Leisten unten, wandern beim Scrollen nach oben (Stapel). Die Reiter-Fassung (tabs/nav-bottom/nav-fine) wird entfernt.
# Urheberhinweis: senkrecht auf der Titelseite, ganz am Ende der letzten Seite waagrecht unten. 06.11.2026.
import re, sys
s = open('index.html', encoding='utf-8').read()
if '/* stack-back */' in s:
    print('schon angewendet'); sys.exit(0)
def cut_css(s, marker):
    a = s.index(marker); nxt = s.find('/* ', a + len(marker)); end = s.rindex('</style>')
    b = nxt if 0 < nxt < end else end
    return s[:a] + s[b:]
for m in ('/* tabs-nav */', '/* nav-bottom */', '/* nav-fine */'):
    s = cut_css(s, m)
for sid in ('tabs-js', 'nav-bottom-js', 'credit-corner-js'):
    a = s.index('<script id="%s">' % sid); b = s.index('</script>', a) + 9
    s = s[:a] + s[b:].lstrip('\n')
JS = '''<script id="credit-corner-js">(function(){var f=document.querySelector('#home ~ footer.copy'),h=document.getElementById('hscroll');if(!f||!h)return;
function upd(){var on=h.offsetParent!==null&&h.getBoundingClientRect().height>0,t=h.scrollTop<h.clientHeight*.2,end=h.scrollTop+h.clientHeight>=h.scrollHeight-6&&h.scrollTop>h.clientHeight*.5,m=innerHeight*.5,b=innerHeight;
 [].forEach.call(h.querySelectorAll('.hb'),function(x){var r=x.getBoundingClientRect();if(r.top>m&&r.top<b)b=r.top;});
 f.style.setProperty('--cb',Math.max(60,innerHeight-b+14)+'px');f.style.setProperty('--cbh','10px');
 f.classList.toggle('cv',on&&t);f.classList.toggle('ch',on&&!t&&end);}
upd();h.addEventListener('scroll',upd,{passive:true});addEventListener('resize',upd);setInterval(upd,400);
})();</script>
'''
s = s.rstrip() + '\n' + JS
i = s.rindex('</style>'); s = s[:i] + '\n/* stack-back */\n#hscroll::after{height:36px}\n' + s[i:]
s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1)+'2026-11-06p'+m.group(3), s, count=1)
open('index.html','w',encoding='utf-8').write(s); print('ok')
