# 20.11.2026: Schalter oben 20 % groesser; Pins 04-06 auf der Karte heissen A B C und wechseln bei Bedarf den Modus;
# der senkrechte Link im Fuss entfaellt (es bleibt der rote Impressum-Link unten); Impressum normal geschrieben;
# Pfeil am Wechselbalken. Idempotent.
import re, sys
s = open('index.html', encoding='utf-8').read()
if 'id="stack3-pins"' in s:
    print('schon vorhanden'); sys.exit(0)
CSS = '''<style id="stack3-pins-css">
#dsw{width:79px}
#dsw>button[data-m]{height:13px;font-size:10.2px;letter-spacing:1px}
#dsw .markb{height:19px;margin:2px 0}
#dsw .mark{width:55px;height:19px}
#infoLink{display:none!important}
#implink{font-size:11px;text-transform:none;letter-spacing:.4px}
</style>
'''
JS = '''<script id="stack3-pins">(function(){
const M={home:["d",0],test:["d",1],links:["d",2],quotes:["s",0],rede:["s",1],hist:["s",2]},L={quotes:"A",rede:"B",hist:"C"};
document.querySelectorAll("#tstage .pin").forEach(b=>{const k=b.dataset.k,m=M[k];if(!m)return;
 if(L[k]){const n=b.querySelector("b");if(n)n.textContent=L[k];b.setAttribute("aria-label",(b.getAttribute("aria-label")||"").replace(/\\[0\\d\\]/,"["+L[k]+"]"));}
 if(m[0]!==DMODE)b.addEventListener("click",e=>{e.stopImmediatePropagation();try{sessionStorage.setItem("dochMode",m[0]);sessionStorage.setItem("dochSwitched","1");sessionStorage.setItem("dochTarget",String(m[1]));}catch(x){}location.reload();},true);});
const lb=document.querySelectorAll("#hscroll>.hb")[3];if(lb){const t=lb.querySelector("b");if(t)t.textContent+=" \\u2192";}
})();</script>
'''
a = '<script id="info-link-js">'
assert s.count(a) == 1
s = s.replace(a, CSS + JS + a)
s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1) + '2026-11-20k' + m.group(3), s, count=1)
open('index.html', 'w', encoding='utf-8').write(s)
print('ok')
