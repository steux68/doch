#!/usr/bin/env python3
"""2026-11-21ad: Staunen -> 'Heute' card (quote of the day + Redewendung of the day) at the top of Zitate. Idempotent."""
import os,re
root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
p=os.path.join(root,"index.html");s=open(p,encoding="utf-8").read()
if 'id="heute-js"' in s: print("already");raise SystemExit
blk=r'''
<style id="heute-css">
.hte{margin:0 0 10px;border:1px dotted #bbb;background:#fffbe0;padding:8px 10px;flex:none}
.hte .hth{font-size:10px;letter-spacing:.14em;text-transform:uppercase;color:var(--red);font-weight:700;margin-bottom:4px}
.hte a.htq{display:block;color:inherit;text-decoration:none;position:relative}
.hte q{display:block;font-size:15px;line-height:1.35;color:#1a1a1a;quotes:"„" "“"}
.hte .htw{display:block;font-size:12px;color:#666;margin-top:2px}
.hte .htr{display:block;margin-top:7px;padding-top:6px;border-top:1px dotted #c9c27a;cursor:pointer;min-height:36px}
.hte .htr b{font-size:15px;color:#1a1a1a}.hte .htr span{display:block;font-size:13px;line-height:1.3;color:#444}
</style>
<script id="heute-js">(function(){
function ok(){return typeof renderQuotes==="function"&&typeof QUOTES!=="undefined"&&typeof RW!=="undefined"&&document.getElementById("p-quotes")}
function go(){if(!ok()){setTimeout(go,300);return}
 var o=renderQuotes;
 function e(t){return String(t).replace(/[&<>"]/g,function(c){return{"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]})}
 renderQuotes=function(){o.apply(this,arguments);
  var P=document.getElementById("p-quotes"),tc=P&&P.querySelector(".tc");if(!tc||tc.querySelector(".hte"))return;
  var d=Math.floor((Date.now()-new Date(new Date().getFullYear(),0,0))/864e5),qs=QUOTES.filter(function(x){return !x.sec&&x.q}),q=qs[d%qs.length],r=RW[(d*7)%RW.length];
  var h=document.createElement("div");h.className="hte";
  h.innerHTML='<div class="hth">Heute</div><a class="htq" href="'+e(q.u)+'" target="_blank" rel="noopener"><q>'+e(q.q)+'</q><span class="htw">'+e(q.who)+' · '+e(q.when)+'</span></a>'+
   '<div class="htr" role="button" tabindex="0"><b>'+e(r[2])+'</b><span>'+e(r[3])+'</span></div>';
  var rb=h.querySelector(".htr"),jump=function(){var b=document.querySelectorAll("#hscroll>.hb")[1];if(b)b.click()};rb.onclick=jump;rb.onkeydown=function(ev){if(ev.key==="Enter"||ev.key===" "){ev.preventDefault();jump()}};
  tc.insertBefore(h,tc.firstChild)};
 renderQuotes();}
go();})();</script>
'''
s=s.rstrip("\n")+"\n"+blk
s=re.sub(r'<meta name="app-version" content="[^"]+">','<meta name="app-version" content="2026-11-21ad">',s,count=1)
open(p,"w",encoding="utf-8").write(s);print("ok")
