#!/usr/bin/env python3
"""Lernstand pro Thema (2026-11-21i): neu · gesehen · geübt · sicher. Text statt nur Prozent (auch farbenblind-sicher).
gesehen = Lernen-Ansicht geoeffnet; geuebt = mind. eine Spielrunde; sicher = Bestwert >= 80 % und keine offenen Fehler im Thema. Idempotent."""
import os,re
root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
p=os.path.join(root,"index.html");s=open(p,encoding="utf-8").read()
if 'id="st-js"' in s: print("already patched");raise SystemExit
js=r'''<style id="st-css">.tt .prog em{font-style:normal}.tt .prog em .stb{font-weight:700;color:#3a3c37;font-size:inherit}.tt .prog em .stw{color:#8a8a8a}</style>
<script id="st-js">(function(){
function status(t){var b=score(t),M=typeof mistakes==="function"?mistakes():{},open=Object.keys(M).some(function(k){return M[k]&&M[k].t===t});
 if(b!=null&&b>=0.8&&!open)return ["sicher",1];if(b!=null)return ["geübt",0];if(store.seen&&store.seen[t])return ["gesehen",0];return ["neu",0];}
function deco(){try{document.querySelectorAll(".tt[data-t]").forEach(function(btn){var t=btn.dataset.t,em=btn.querySelector("em");if(!em)return;
  var s=status(t),pct=Math.round((score(t)||0)*100);em.innerHTML=(s[1]?'<span class="stb">'+s[0]+"</span>":'<span class="stw">'+s[0]+"</span>")+(s[0]==="neu"||s[0]==="gesehen"?"":" · "+pct+" %");});}catch(e){}}
if(typeof renderHome==="function"){var r=renderHome;renderHome=function(){var x=r.apply(this,arguments);deco();return x;};}
if(typeof setMode==="function"){var m=setMode;setMode=function(md){var x=m.apply(this,arguments);try{if(md==="learn"&&typeof T!=="undefined"&&T&&store){(store.seen||(store.seen={}))[T]=1;save();}}catch(e){}return x;};}
deco();})();</script>'''
s=s+js
s=re.sub(r'<meta name="app-version" content="[^"]+">','<meta name="app-version" content="2026-11-21i">',s,count=1)
open(p,"w",encoding="utf-8").write(s);print("ok")
