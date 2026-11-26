# DOCH! 26.11.2026: (1) Kleine Pfeile in "Heute ueben / Weitermachen / Heute wiederholen" entfernt (wirkten wie Wisch-Hinweis),
# (2) Rundpfeil (wie in den Pop-ups) am Rand des Regals Zeiten/Faelle/Artikel: zeigt "hier wischen", tippbar. Idempotent.
import re, sys
s = open('index.html', encoding='utf-8').read()
if 'id="regal2-css"' in s: sys.exit('schon angewendet')
css = ('<style id="regal2-css">'
 '.rcb button>b:last-child{display:none!important}'
 '#sehb .rgl{position:sticky;flex:none;align-self:flex-start;margin-top:31px;width:26px;height:26px;padding:0;border:0;border-radius:50%;background:rgba(255,255,255,.88);box-shadow:0 0 0 1px rgba(0,0,0,.14);display:flex;align-items:center;justify-content:center;z-index:5;-webkit-tap-highlight-color:transparent;cursor:pointer}'
 '#sehb .rgl::before{content:"";position:absolute;inset:-8px}'
 '#sehb .rgl.r{right:-14px;margin-left:-34px}'
 ''
 '#sehb .rgl .ar{width:24px;height:24px}'
 '#sehb .rgl[hidden]{display:none!important}'
 '</style>')
js = r'''<script id="regal2-js">(function(){var sb=document.getElementById("sehb");if(!sb)return;var ARL='<svg class="ar" viewBox="-12 -12 24 24" aria-hidden="true"><path class="dt" transform="rotate(180)" d="M5.4 0L-4.6 -4.9L-2.2 0L-4.6 4.9Z"/></svg>',ARR='<svg class="ar" viewBox="-12 -12 24 24" aria-hidden="true"><path class="dt" d="M5.4 0L-4.6 -4.9L-2.2 0L-4.6 4.9Z"/></svg>';
function mk(c,svg,lbl,dir){var b=document.createElement("button");b.type="button";b.className="rgl "+c;b.setAttribute("aria-label",lbl);b.innerHTML=svg;b.addEventListener("click",function(e){e.stopPropagation();sb.scrollBy({left:dir*sb.clientWidth*0.66,behavior:"smooth"});});return b;}
var R=mk("r",ARR,"weiter wischen",1);sb.appendChild(R);
function upd(){var m=sb.scrollWidth-sb.clientWidth;R.hidden=m<6||sb.scrollLeft>m-6;}
sb.addEventListener("scroll",upd,{passive:true});window.addEventListener("resize",upd);upd();setTimeout(upd,600);})();</script>'''
assert '</head>' in s
s = s.replace('</head>', css + '</head>', 1)
s = s.rstrip('\n') + '\n' + js + '\n'
if '--noversion' not in sys.argv:
    s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1) + '2026-11-26u' + m.group(3), s, count=1)
open('index.html', 'w', encoding='utf-8').write(s)
print('ok')
