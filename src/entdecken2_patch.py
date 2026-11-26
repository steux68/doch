# DOCH! 26.11.2026: Heute-Karten auf ZWEI reduziert, im alten Aussehen (klein, ohne Extrazeilen):
#  1) "Entdecken" (lime, Platz von "Heute ueben"): ein taeglich wechselndes, noch nie geoeffnetes Thema
#  2) rechts die naechste sinnvolle Sache: "Heute wiederholen" (rosa), sonst "Weitermachen" (gelb)
# "Heute ueben 15 Fragen" bleibt unter Tests erreichbar. Ersetzt die schmale Zeile aus entdecken_patch.py. Idempotent.
import re, sys
s = open('index.html', encoding='utf-8').read()
if 'id="entd2-js"' in s: sys.exit('schon angewendet')
# alte Zeile entfernen
s = re.sub(r'<style id="entd-css">.*?</style>', '', s, count=1, flags=re.S)
s = re.sub(r'<script id="entd-js">.*?</script>\n?', '', s, count=1, flags=re.S)
css = ('<style id="entd2-css">'
 '#dayb{display:none!important}#entd{display:none!important}'
 '.rcb .nw{background:#e4f7a0}'
 '</style>')
js = r'''<script id="entd2-js">(function(){
var EX={test:1,links:1,sehen:1,lueck:1,write:1};
function seen(t){try{if(store&&store.seen&&store.seen[t])return true;}catch(e){}try{if(typeof score==="function"&&score(t)!=null)return true;}catch(e){}return false;}
function pick(){var L=(typeof TOPICS!=="undefined"?TOPICS:[]).filter(function(x){return x&&x.t&&!EX[x.t]&&!seen(x.t)});if(!L.length)return null;return L[Math.floor(Date.now()/864e5)%L.length];}
function build(){var rcb=document.querySelector(".rcb");if(!rcb)return;
 var d=document.getElementById("dayb");if(d)d.hidden=true;
 var er=document.getElementById("errc"),rs=document.getElementById("resume");if(er&&rs&&!er.hidden)rs.hidden=true;
 var b=document.getElementById("entd2"),p=pick();
 if(!p){if(b)b.hidden=true;return;}
 if(!b){b=document.createElement("button");b.id="entd2";b.type="button";b.className="dayb nw";rcb.insertBefore(b,rcb.firstChild);b.addEventListener("click",function(){var t=b.dataset.t;if(t&&typeof openTopic==="function")openTopic(t);});}
 b.hidden=false;b.dataset.t=p.t;b.title=p.ds||"";b.innerHTML="<span><small>Entdecken</small><b></b></span>";b.querySelector("b").textContent=p.n;}
var r=window.renderHome;if(typeof r==="function")window.renderHome=function(){var x=r.apply(this,arguments);try{build()}catch(e){}return x;};
try{build()}catch(e){}setTimeout(function(){try{build()}catch(e){}},900);
})();</script>'''
assert '</head>' in s
s = s.replace('</head>', css + '</head>', 1)
s = s.rstrip('\n') + '\n' + js + '\n'
if '--noversion' not in sys.argv:
    s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1) + '2026-11-26x' + m.group(3), s, count=1)
open('index.html', 'w', encoding='utf-8').write(s)
print('ok')
