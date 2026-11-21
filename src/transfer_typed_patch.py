#!/usr/bin/env python3
"""2026-11-21z: (1) typed (Ergaenzen) answers show the wrong-option explanation when the typed word is one of the options;
(2) Einstellungen: progress backup code (copy / paste) to move progress between devices. Idempotent."""
import os,re
root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
p=os.path.join(root,"index.html");s=open(p,encoding="utf-8").read()
if 'id="typ-wx-js"' in s: print("already patched");raise SystemExit
blk='''
<style id="xfer-css">#xfer{margin:14px 0 4px;padding-top:12px;border-top:1px dotted #bdb8a8}#xfer b{display:block;font-size:13px;margin-bottom:4px}#xfer small{display:block;color:#5d5f58;font-size:12px;line-height:1.35;margin-bottom:8px}#xfer button{font:inherit;font-size:13px;padding:7px 12px;margin:0 6px 6px 0;border:1px solid #1c1c1a;background:#fff;color:#1c1c1a;border-radius:0;cursor:pointer}#xfer textarea{display:block;width:100%;box-sizing:border-box;height:64px;font:11px/1.3 monospace;margin:4px 0 8px;border:1px solid #bdb8a8;padding:6px}#xfer .xm{font-size:12px;min-height:16px;color:#1c1c1a}</style>
<script id="typ-wx-js">(function(){var iv=setInterval(function(){if(typeof mcTyped!=="function"||typeof MC==="undefined"||mcTyped.__tw)return;var o=mcTyped;
mcTyped=function(){var q=MC&&MC.list&&MC.list[MC.i],was=MC&&MC.done;o.apply(this,arguments);if(was||!q||!window.WX)return;
var a=document.getElementById("ans"),inp=((a&&a.value)||"").trim().replace(/\\s+/g," ");if(!inp||inp===String(q.o[q.c]))return;
var i=q.o.findIndex(function(x){return String(x).toLowerCase()===inp.toLowerCase()});if(i<0||i===q.c)return;var r=WX[q.s+"|"+q.o[i]];if(!r)return;
var res=document.getElementById("res");if(!res)return;var d=document.createElement("p");d.className="nr";d.textContent="Nicht „"+q.o[i]+"“. "+r;res.appendChild(d);};
mcTyped.__tw=1;clearInterval(iv)},300)})();</script>
<script id="xfer-js">(function(){function go(){var sb=document.getElementById("setb");if(!sb||document.getElementById("xfer"))return !!document.getElementById("xfer");
var d=document.createElement("div");d.id="xfer";d.innerHTML='<b>Fortschritt übertragen</b><small>Dein Fortschritt liegt nur auf diesem Gerät. Code kopieren, auf dem anderen Gerät hier einfügen.</small><button type="button" id="xc">Code kopieren</button><button type="button" id="xi">Code einfügen</button><textarea id="xt" hidden placeholder="Code hier einfügen" spellcheck="false"></textarea><button type="button" id="xg" hidden>Übernehmen</button><div class="xm" id="xm"></div>';sb.appendChild(d);
var m=function(t){document.getElementById("xm").textContent=t};
function enc(){var o={v:1,s:JSON.parse(localStorage.getItem("deutsch.v1")||"{}"),b:localStorage.getItem("doch-best")||""};return "DOCH1:"+btoa(unescape(encodeURIComponent(JSON.stringify(o))))}
document.getElementById("xc").onclick=function(){var c;try{c=enc()}catch(e){m("Kein Fortschritt gefunden.");return}
var t=document.getElementById("xt");t.hidden=false;t.value=c;t.focus();t.select();var ok=false;try{ok=document.execCommand("copy")}catch(e){}if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(c).then(function(){m("Code kopiert.")},function(){m(ok?"Code kopiert.":"Code markiert: bitte selbst kopieren.")})}else m(ok?"Code kopiert.":"Code markiert: bitte selbst kopieren.")};
document.getElementById("xi").onclick=function(){var t=document.getElementById("xt");t.hidden=false;t.value="";document.getElementById("xg").hidden=false;m("Code einfügen und Übernehmen tippen. Der Fortschritt auf diesem Gerät wird ersetzt.");t.focus()};
var armed=false;document.getElementById("xg").onclick=function(){var v=document.getElementById("xt").value.trim();if(v.indexOf("DOCH1:")!==0){m("Das ist kein DOCH-Code.");return}
var o;try{o=JSON.parse(decodeURIComponent(escape(atob(v.slice(6)))))}catch(e){m("Code beschädigt.");return}if(!o||o.v!==1||typeof o.s!=="object"){m("Code beschädigt.");return}
if(!armed){armed=true;m("Nochmal tippen: Fortschritt auf diesem Gerät wird ersetzt.");return}
try{localStorage.setItem("deutsch.v1",JSON.stringify(o.s));if(o.b)localStorage.setItem("doch-best",o.b)}catch(e){m("Speichern nicht möglich.");return}m("Übernommen. Die Seite lädt neu.");setTimeout(function(){location.reload()},700)};
return true}
if(!go()){var n=0,iv=setInterval(function(){if(go()||++n>40)clearInterval(iv)},500)}})();</script>
'''
s=s.rstrip("\n")+"\n"+blk
s=re.sub(r'<meta name="app-version" content="[^"]+">','<meta name="app-version" content="2026-11-21z">',s,count=1)
open(p,"w",encoding="utf-8").write(s);print("ok")
