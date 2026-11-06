# Navigation wieder unten wie bei den anderen Apps: zwei Spalten, schlanke Leisten, Farbpuls auf der Titelseite, aktiv = Neongelb. 06.11.2026.
import re, sys
s = open('index.html', encoding='utf-8').read()
if '/* nav-bottom */' in s:
    print('schon angewendet'); sys.exit(0)
CSS = '''
/* nav-bottom */
#hscroll{height:calc(100% - 76px)!important}
#hnav{position:absolute!important;left:0;right:0;bottom:0;margin:0!important;display:grid!important;grid-template-columns:1fr 1fr!important;gap:0!important;background:#fff;z-index:15;
 border-top:1px dotted #b8b8b8}
#hnav .hnb{height:25px;padding:0 10px!important;display:flex;align-items:center;justify-content:flex-start;text-align:left!important;font-size:12px!important;font-weight:700!important;color:#000!important;
 background:#f2f2f2!important;border-bottom:1px dotted #b8b8b8!important;box-sizing:border-box}
#hnav .hnb:nth-child(odd){border-right:1px dotted #b8b8b8!important}
#hnav .hnb[aria-pressed="true"]{background:#cdff3e!important}
body.introOn #hnav .hnb:not([aria-pressed="true"]){animation:hbp 3.4s ease-in-out infinite}
#hnav .hnb[data-pc="0"]{--pc:#fbe0e3}#hnav .hnb[data-pc="1"]{--pc:#e6f4c8;animation-delay:-.7s!important}
#hnav .hnb[data-pc="2"]{--pc:#dfe9fb;animation-delay:-1.4s!important}#hnav .hnb[data-pc="3"]{--pc:#fdf0c2;animation-delay:-2.1s!important}
#hnav .hnb[data-pc="4"]{--pc:#ece2f8;animation-delay:-2.8s!important}
@media (prefers-reduced-motion:reduce){body.introOn #hnav .hnb{animation:none!important}}
'''
JS = '<script id="nav-bottom-js">(function(){var n=document.getElementById("hnav");if(!n)return;[].forEach.call(n.children,function(b,k){b.setAttribute("data-pc",k%5);});})();</script>\n'
i = s.rindex('</style>'); s = s[:i] + CSS + s[i:]
s = s.rstrip() + '\n' + JS
s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1)+'2026-11-06m'+m.group(3), s, count=1)
open('index.html','w',encoding='utf-8').write(s); print('ok')
