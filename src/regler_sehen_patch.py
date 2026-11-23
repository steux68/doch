#!/usr/bin/env python3
"""Regler-Karte (Fälle & Pronomen, Zeitformen: Lernen + Theorie) im Sehen-Look (2026-11-23i). Marker [regler-sehen]. Idempotent."""
import sys
P="index.html"
s=open(P,encoding="utf-8").read()
if "[regler-sehen]" in s:
    print("schon angewendet"); sys.exit(0)
def rep(a,b):
    global s
    assert s.count(a)==1,("Treffer != 1:",s.count(a),a[:80])
    s=s.replace(a,b)
i=s.index("window.tpxHTML=function(k){"); j=s.index("function step(r,x){")
new=r'''/* [regler-sehen] */
var RGF={k:["#ededeb","#f0be83","#c3ccfc","#c4a6ee"],t:["#e6dccb","#e6dccb","#e6dccb","#e4f7a0","#a9d3f0","#a9d3f0"]};
var RGB=["#e6dccb","#e4f7a0","#a9d3f0"];
var RGA='<svg class="ar" viewBox="-12 -12 24 24" aria-hidden="true"><path class="dt" transform="rotate(180)" d="M5.4 0L-4.6 -4.9L-2.2 0L-4.6 4.9Z"/></svg>',RGR='<svg class="ar" viewBox="-12 -12 24 24" aria-hidden="true"><path class="dt" d="M5.4 0L-4.6 -4.9L-2.2 0L-4.6 4.9Z"/></svg>';
function rgSel(key,label,opts,cur,flex,rich){
 return '<div class="snc1'+(rich?' rich':'')+'" style="flex:'+flex+'"><span class="snl3">'+label+'</span>'+(rich?'<div class="disp">'+opts.map(function(o,i){return i==cur?'<b>'+o+'</b>':o}).join('<i>/</i>')+'</div>':'')
  +'<select data-key="'+key+'" aria-label="'+label+'">'+opts.map(function(o,i){return '<option value="'+i+'"'+(i==cur?' selected':'')+'>'+o+'</option>'}).join('')+'</select></div>';}
window.tpxHTML=function(k){k=k||"t";var d=D[k],n=d.ab.length;
 var bd=(k=="t"?[["Vergangenheit",3],["Jetzt",1],["Zukunft",2]]:d.bands.map(function(b){return [b[0],1]})).map(function(b,q){return '<span class="svb" style="grid-column:span '+b[1]+';background:'+(k=="t"?RGB[q]:RGF.k[q])+'">'+b[0]+'</span>'}).join("");
 var chips=d.ab.map(function(a,j){return '<button type="button" class="svb svk fr" data-s="='+j+'" aria-label="'+d.nm[j]+'">'+a+'</button>'}).join("");
 return '<div class="rgc sv sn" data-k="'+k+'" data-i="'+d.i0+'" data-v="0" data-l="0"><div class="svg svbd" style="--n:'+n+'">'+bd+'</div><div class="svg" style="--n:'+n+'">'+chips+'</div>'
 +'<div class="snhw"><div class="snh"><span role="button" tabindex="0" class="svar l" data-s="-1" aria-label="zurück">'+RGA+'</span><div class="sns rgsn"></div><span role="button" tabindex="0" class="svar r" data-s="1" aria-label="weiter">'+RGR+'</span></div></div>'
 +'<div class="snctl">'+rgSel("v",k=="t"?"Verb":"Nomen",d.o1,0,1.2,false)+rgSel("l","Form",["Kurz","+ Nebensatz"],0,1.3,true)+'</div>'
 +'<div class="rgh"><b></b><small></small></div><div class="rgi"></div><svg class="svln" aria-hidden="true"><path class="rgp" fill="none" stroke="#b8b8b8" stroke-width="1.2" stroke-linecap="round" stroke-dasharray="0.5 2.5"/></svg></div>';};
function rgLine(r){var pa=r.querySelector(".rgp"),on=r.querySelector(".svk.on"),w=r.querySelector(".rgsn .n0,.rgsn .n1,.rgsn .n2,.rgsn .n3,.rgsn .v");if(!pa)return;if(!on||!w){pa.setAttribute("d","");return;}
 var W=r.getBoundingClientRect(),c=on.getBoundingClientRect(),q=w.getBoundingClientRect(),x1=c.left+c.width/2-W.left,y1=c.bottom-W.top+2,x2=q.left+q.width/2-W.left,y2=q.top-W.top-3,ym=y1+Math.min(14,(y2-y1)/2);
 pa.setAttribute("d","M"+x1+" "+y1+" V"+ym+" H"+x2+" V"+y2);}
function draw(r){var k=r.dataset.k,d=D[k],i=+r.dataset.i,v=+r.dataset.v,l=+r.dataset.l,fill=RGF[k][i];
 var sn=r.querySelector(".rgsn");r.querySelector(".snhw").style.setProperty("--hl",fill);
 sn.innerHTML=parts(k,i,v,l).map(function(x){return '<span class="'+x[1]+(/^[,.]\s*$/.test(x[0])?' p':'')+'">'+x[0].trim()+'</span>'}).join(" ").replace(/ <span class="t p">/g,'<span class="t p">');
 r.querySelectorAll(".svk").forEach(function(b,j){var on=j==i;b.classList.toggle("on",on);b.style.background=on?RGF[k][j]:"";});
 r.querySelectorAll(".svar").forEach(function(a){var q=i+ +a.dataset.s;if(q<0||q>=d.nm.length)a.setAttribute("data-off","");else a.removeAttribute("data-off");});
 r.querySelector(".rgh b").textContent=d.nm[i];r.querySelector(".rgh small").textContent=d.st[i];
 r.querySelector(".rgi").innerHTML=k==="t"?d.I[i].map(function(t,j){return '<div><span>'+d.L[j]+'</span><span>'+t+'</span></div>'}).join(""):d.nm.map(function(n,j){return '<div'+(j==i?' class="on"':'')+'><span>'+n+'</span><span>'+d.F[v][j]+'</span></div>'}).join("")+'<div><span></span><span style="color:var(--muted);font-weight:400">'+d.I[i]+'</span></div>';
 fit(sn);rgLine(r);requestAnimationFrame(function(){rgLine(r)});setTimeout(function(){rgLine(r)},250);}
'''
s=s[:i]+new+s[j:]
rep("""document.addEventListener("click",function(e){var b=e.target.closest&&e.target.closest(".rgc button");if(!b)return;var r=b.closest(".rgc");
 if(b.dataset.s!==undefined)step(r,b.dataset.s);else if(b.dataset.o){var o=b.dataset.o;r.dataset[o[0]]=o.slice(1);draw(r);}});""",
"""document.addEventListener("click",function(e){var b=e.target.closest&&e.target.closest(".rgc [data-s]");if(!b)return;var r=b.closest(".rgc");step(r,b.dataset.s);});
document.addEventListener("change",function(e){var t=e.target;if(!t||!t.dataset||!t.dataset.key)return;var r=t.closest&&t.closest(".rgc");if(!r)return;r.dataset[t.dataset.key]=t.value;var q=t.closest(".snc1"),dp=q&&q.querySelector(".disp");if(dp)dp.innerHTML=[].map.call(t.options,function(o,j){return j==t.selectedIndex?'<b>'+o.text+'</b>':o.text}).join('<i>/</i>');draw(r);});""")
rep("""var s=e.target.closest&&e.target.closest(".rgs");X0=""","""var s=e.target.closest&&e.target.closest(".rgc .snh");X0=""")
rep("window.addEventListener(\"resize\",function(){document.querySelectorAll(\".rgsn\").forEach(fit)});","window.addEventListener(\"resize\",function(){document.querySelectorAll(\".rgsn\").forEach(fit);document.querySelectorAll(\".rgc\").forEach(rgLine)});")
css="""/* [regler-sehen] */
.rgc.sv{padding:0 0 8px;box-shadow:none;margin:0;gap:0}
.rgc .svb{cursor:pointer;font-family:inherit}
.rgc .snhw{position:relative}
.rgc .rgsn{white-space:nowrap;overflow:hidden;color:#1a1a1a}
.rgc button.svb{font-size:10px;letter-spacing:.06em;color:#2c2c2a;font-family:inherit}
.rgc .rgsn.wr{white-space:normal}
.rgc .rgsn .t{color:#1a1a1a}
.rgc .rgsn span{padding:0 3px;margin:0 -1px}.rgc .rgsn span.p{padding:0;margin:0}
.rgc .rgsn .n0{background:#ededeb}.rgc .rgsn .n1{background:#f0be83}.rgc .rgsn .n2{background:#c3ccfc}.rgc .rgsn .n3{background:#c4a6ee}
.rgc .rgsn .v,.rgc .rgsn .e{background:var(--hl,#e4f7a0);font-weight:700}
.rgc .rgsn .n0,.rgc .rgsn .n1,.rgc .rgsn .n2,.rgc .rgsn .n3{font-weight:700}
.rgc .rgh{padding:8px 10px 0}
.rgc .rgi>div{padding:6px 10px}
.rgc .rgi>div.on{background-color:#f4f4f1}
.rgc .svln{z-index:2}
"""
rep("/* [sehen-verben] */\n","/* [sehen-verben] */\n"+css)
rep('app-version" content="2026-11-23h"','app-version" content="2026-11-23i"')
open(P,"w",encoding="utf-8").write(s)
print("ok")
