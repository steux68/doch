#!/usr/bin/env python3
"""DOCH: Fortschritt sichtbar auch bei 0: 'x von y geübt' je Gruppe, sichtbare Leiste, Gesamtzahl im Grammatik-Band."""
import re
p="index.html"; s=open(p,encoding="utf-8").read()
if 'id="fortschritt-css"' in s: raise SystemExit("already patched")
o="""<small>'+g.t.length+(g.t.length===1?' Thema':' Themen')+' · '+lo"""
assert s.count(o)==1
s=s.replace(o,"""<small>'+g.t.filter(t=>score(t)!=null).length+' von '+g.t.length+' geübt · '+lo""")
css='''<style id="fortschritt-css">
.grp .grh .prog{background:#e4e4e2!important}
.hb .hbn{position:absolute;right:12px;top:50%;transform:translateY(-50%);font-size:12px;letter-spacing:0;text-transform:none;font-weight:400;color:#222}
</style>
<script id="fortschritt-js">(function(){
if(typeof renderHome!=="function")return;
var r=renderHome;
renderHome=function(){var x=r.apply(this,arguments);
 try{var all=GROUPS.reduce(function(a,g){return a.concat(g.t)},[]),n=all.filter(function(t){return score(t)!=null}).length;
  var b=document.querySelector("#hscroll>.hb");
  if(b&&/grammatik/i.test(b.textContent.replace(/\\d+\\s*von.*/,""))){var e=b.querySelector(".hbn");if(!e){e=document.createElement("span");e.className="hbn";b.appendChild(e);}e.textContent=n+" von "+all.length+" geübt";}
 }catch(e){}
 return x;};
try{renderHome();}catch(e){}
})();</script>
'''
s=s.rstrip("\n")+"\n"+css
s,c=re.subn(r'(<meta name="app-version" content="2026-11-24)([a-z])(")',lambda m:m.group(1)+chr(ord(m.group(2))+1)+m.group(3),s,count=1); assert c==1
open(p,"w",encoding="utf-8").write(s)
