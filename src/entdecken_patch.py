# DOCH! 26.11.2026: "Entdecken" - eine schmale Zeile unter den Heute-Karten holt taeglich ein noch NIE geoeffnetes Thema nach oben
# (Name aus TOPICS, Auswahl nach Datum, wechselt pro Tag; verschwindet, wenn alles gesehen ist). Kein Pfeil, kein Menue. Idempotent.
import re, sys
s = open('index.html', encoding='utf-8').read()
if 'id="entd-css"' in s: sys.exit('schon angewendet')
css = ('<style id="entd-css">'
 '#entd{order:2!important;display:flex;align-items:baseline;gap:10px;width:100%;margin:0 0 8px;padding:7px 10px;background:#f6f6f4;color:#1a1a1a;text-align:left;min-height:34px;line-height:1.25;overflow:hidden;white-space:nowrap}'
 '#entd[hidden]{display:none!important}'
 '#entd small{flex:none;font-size:12px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--red,#e30613)}'
 '#entd b{font-size:14px;overflow:hidden;text-overflow:ellipsis;min-width:0}'
 '#entd:active{background:#cdff3e}'
 '</style>')
js = r'''<script id="entd-js">(function(){
var EX={test:1,links:1,sehen:1,lueck:1,write:1};
function seen(t){try{if(store&&store.seen&&store.seen[t])return true;}catch(e){}try{if(typeof score==="function"&&score(t)!=null)return true;}catch(e){}return false;}
function pick(){var L=(typeof TOPICS!=="undefined"?TOPICS:[]).filter(function(x){return x&&x.t&&!EX[x.t]&&!seen(x.t)});if(!L.length)return null;var d=Math.floor(Date.now()/864e5);return L[d%L.length];}
function build(){var rcb=document.querySelector(".rcb");if(!rcb)return;var b=document.getElementById("entd");var p=pick();
 if(!p){if(b)b.hidden=true;return;}
 if(!b){b=document.createElement("button");b.id="entd";b.type="button";rcb.insertAdjacentElement("afterend",b);b.addEventListener("click",function(){var t=b.dataset.t;if(t&&typeof openTopic==="function")openTopic(t);});}
 b.hidden=false;b.dataset.t=p.t;b.title=p.ds||"";b.innerHTML="<small>Entdecken</small><b></b>";b.lastChild.textContent=p.n;}
var r=window.renderHome;if(typeof r==="function")window.renderHome=function(){var x=r.apply(this,arguments);try{build()}catch(e){}return x;};
try{build()}catch(e){}setTimeout(function(){try{build()}catch(e){}},900);
})();</script>'''
assert '</head>' in s
s = s.replace('</head>', css + '</head>', 1)
s = s.rstrip('\n') + '\n' + js + '\n'
if '--noversion' not in sys.argv:
    s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1) + '2026-11-26w' + m.group(3), s, count=1)
open('index.html', 'w', encoding='utf-8').write(s)
print('ok')
