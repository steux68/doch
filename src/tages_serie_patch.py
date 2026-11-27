#!/usr/bin/env python3
"""DOCH: 'Heute üben' gets a quiet day streak (27 Nov 2026).
A finished daily round marks the day; days in a row are shown on the button
as text plus seven small circles (lime = done). Missing a day starts again at 1."""
import sys
p = "index.html"; s = open(p, encoding="utf-8").read()
if 'id="serie-js"' in s: sys.exit("already patched")
CSS = '''<style id="serie-css">
.dayb .ser{display:flex;gap:3px;margin-top:4px}
.dayb .ser i{width:7px;height:7px;border-radius:50%;border:1px solid #b8b8b8;background:#fff}
.dayb .ser i.on{background:#cdff3e;border-color:#9fbf2a}
.dayb small .ok{color:#1a1a1a;font-weight:700}
</style>'''
JS = '''<script id="serie-js">(function(){
function T(){return typeof today==="function"?today():new Date().toISOString().slice(0,10)}
function Y(){return new Date(Date.now()-864e5).toISOString().slice(0,10)}
function S(){return store.dser||(store.dser={last:null,n:0})}
function cur(){var d=S();return (d.last===T()||d.last===Y())?d.n:0}
function paint(){var b=document.getElementById("dayb");if(!b)return;var d=S(),n=cur(),done=d.last===T(),k=n%7||(n?7:0),c="";
 for(var i=0;i<7;i++)c+='<i class="'+(i<k?"on":"")+'"></i>';
 b.innerHTML='<span><small>Heute üben'+(n?' · '+n+(n===1?' Tag':' Tage')+' in Folge':'')+(done?' · <span class="ok">✓ erledigt</span>':'')+'</small><b>15 Fragen</b><span class="ser" aria-hidden="true">'+c+'</span></span><b>→</b>';}
function mark(){var d=S(),t=T();if(d.last===t)return;d.n=(d.last===Y())?d.n+1:1;d.last=t;save();paint()}
function watch(){var bd=document.getElementById("bd");if(!bd||!document.getElementById("dayb")){setTimeout(watch,400);return}
 paint();
 new MutationObserver(function(){if(window.__daily&&/^Ergebnis/.test(bd.textContent||""))mark()}).observe(bd,{childList:true,characterData:true,subtree:true});
 var h=document.getElementById("home");if(h)new MutationObserver(function(){if(!h.hidden)paint()}).observe(h,{attributes:true,attributeFilter:["hidden"]});}
watch();})();</script>'''
a = '</body>'
i = s.rfind(a)
s = (s[:i] + CSS + JS + s[i:]) if i >= 0 else (s + "\n" + CSS + JS + "\n")
new = "2026-11-27-serie"
import re
m = re.search(r'name="app-version" content="([^"]*)"', s)
s = s.replace(m.group(0), 'name="app-version" content="%s"' % new)
open(p, "w", encoding="utf-8").write(s)
open("version.txt", "w").write(new + "\n")
print("OK", new)
