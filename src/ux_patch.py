#!/usr/bin/env python3
"""2026-11-21ab: (1) bigger hit areas for small links; (2) Sehen: variant rows behind one 'mehr' button + larger sentence;
(3) 'Heute üben' button (5 open mistakes + questions from the 3 weakest topics, 15 in all). Idempotent."""
import os,re
root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
p=os.path.join(root,"index.html");s=open(p,encoding="utf-8").read()
if 'id="ux-js"' in s: print("already patched");raise SystemExit
blk=r'''
<style id="ux-css">
a[href^="http"]{position:relative}
a[href^="http"]::after{content:"";position:absolute;left:-6px;right:-6px;top:-9px;bottom:-9px}
#theo .sv .xmore{margin-top:4px}
#theo .sv .xmore .svb{font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:#555;cursor:pointer;min-height:30px;display:flex;align-items:center;justify-content:center}
#theo .sv .xh{display:none!important}
.sns{font-size:23px;line-height:1.3}.snn{font-size:16px}.snh{height:118px}
.rcb .dayb{display:flex;justify-content:space-between;align-items:center;gap:10px;text-align:left;background:#e4f7a0;color:#1a1a1a;padding:9px 12px;flex:none;border:0;font:inherit;cursor:pointer;min-height:44px}
.rcb .dayb small{display:block;font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:#4a5a12}.rcb .dayb b{font-size:16px}
</style>
<script id="ux-js">(function(){
/* ---- Sehen: variant rows behind "mehr" ---- */
var openMore=false,pend=0;
function fix(){pend=0;var th=document.getElementById("theo");if(!th)return;var root=th.querySelector("#sv");if(!root||root.querySelector(".xmore"))return;
 var rows=[].slice.call(root.children).filter(function(c){return c.classList.contains("svg")});
 var sec=rows.filter(function(r){var t=(r.innerText||"").trim().toUpperCase();return /^KURZ(\s|$)/.test(t)||/^LERNEN \(HABEN\)/.test(t)});
 if(!sec.length)return;
 var need=sec.some(function(r){var on=r.querySelector(".svo.on"),f=r.querySelector(".svo");return on&&f&&on!==f});
 var open=need||openMore;
 var t=document.createElement("div");t.className="svg xmore";t.style.setProperty("--n","1");
 var b=document.createElement("span");b.setAttribute("role","button");b.tabIndex=0;b.className="svb svo fr";t.appendChild(b);
 function paint(){sec.forEach(function(r){r.classList.toggle("xh",!open)});b.textContent=open?"weniger ▴":"mehr: Nebensatz · Frage · gehen ▾"}
 function tog(){open=!open;openMore=open;paint()}
 b.onclick=tog;b.onkeydown=function(e){if(e.key==="Enter"||e.key===" "){e.preventDefault();tog()}};
 sec[0].parentNode.insertBefore(t,sec[0]);paint();}
function sched(){if(!pend){pend=1;requestAnimationFrame(fix)}}
function boot(){var th=document.getElementById("theo");if(!th){setTimeout(boot,300);return}new MutationObserver(sched).observe(th,{childList:true,subtree:true});sched()}
boot();
/* ---- Heute üben ---- */
function ready(){return typeof openTopic==="function"&&typeof mcStart==="function"&&typeof fullPool==="function"&&typeof ALLT==="function"&&typeof mistQs==="function"&&typeof mix==="function"&&typeof qKey==="function"&&typeof store!=="undefined"}
function inst(){if(!ready()){setTimeout(inst,300);return}
 var oT=openTopic;openTopic=function(t){window.__daily=!!window.__dArm;window.__dArm=0;return oT.apply(this,arguments)};
 var oS=mcStart;mcStart=function(t){if(!window.__daily||ERRMODE)return oS.apply(this,arguments);
  var seen={},list=[],mq=mistQs("err").slice(0,5);mq.forEach(function(q){seen[qKey(q)]=1;list.push(q)});
  var best=store.best||{},tops=ALLT().filter(function(x){try{return fullPool(x).length>3}catch(e){return false}}).map(function(x){var b=best[x];return {t:x,s:(b==null?0.4:b)+Math.random()*0.05}}).sort(function(a,b){return a.s-b.s}).slice(0,3);
  var need=15-list.length,per=Math.ceil(need/tops.length);
  tops.forEach(function(tp){var pool=fullPool(tp.t).filter(function(q){return q.k!=="c"&&!seen[qKey(q)]}),k=0;shuffle(pool);pool.forEach(function(q){if(k<per&&list.length<15){seen[qKey(q)]=1;list.push(q);k++}})});
  shuffle(list);MC={t:t,list:list.map(mix),i:0,score:0,done:false,per:{},old:mq.length};};
 var rcb=document.querySelector(".rcb");if(rcb&&!document.getElementById("dayb")){var b=document.createElement("button");b.id="dayb";b.className="dayb";b.type="button";
  b.innerHTML='<span><small>Heute üben</small><b>15 Fragen</b></span><b>→</b>';
  b.onclick=function(){window.__dArm=1;ERRMODE=false;openTopic("test");var tt=document.getElementById("ttl");if(tt)tt.textContent="Heute üben";setMode("game")};rcb.insertBefore(b,rcb.firstChild)}}
inst();})();</script>
'''
s=s.rstrip("\n")+"\n"+blk
s=re.sub(r'<meta name="app-version" content="[^"]+">','<meta name="app-version" content="2026-11-21ab">',s,count=1)
open(p,"w",encoding="utf-8").write(s);print("ok")
