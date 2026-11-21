#!/usr/bin/env python3
"""Mock-up voraus.html: 'Zuerst'-Zeile (Voraussetzungen) unter den Tabs jedes Themas. Nur Testkopie, index.html bleibt unveraendert."""
import os
root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
s=open(os.path.join(root,"index.html"),encoding="utf-8").read()
css="""<style id="pre-css">
#pre{display:flex;align-items:center;gap:0;height:23px;margin:0;padding:0 12px;overflow:hidden;white-space:nowrap;font-size:12.5px;color:#6b6b6b;position:relative}
#pre[hidden]{display:none}
#pre::after{content:"";position:absolute;left:0;right:0;bottom:0;height:1px;background:repeating-linear-gradient(to right,#b8b8b8 0 1px,transparent 1px 3px)}
#pre .pl{color:#e30613;font-weight:700;font-size:10.5px;letter-spacing:.12em;margin-right:8px;text-transform:uppercase}
#pre button{all:unset;cursor:pointer;color:#3a3c37;padding:0 0;position:relative}
#pre button::before{content:"";position:absolute;inset:-10px -4px}
#pre button+button::before{left:-10px}
#pre .ps{margin:0 6px;color:#b8b8b8}
</style>"""
js="""<script id="pre-js">(function(){
var PRE={adj:["art","fall"],nebs:["satz","konn"],rel:["fall","nebs"],gen:["art","fall"],prep:["art","fall"],pfall:["fall"],vkas:["fall","pron"],komp:["adj"],zuinf:["modal","satz"],perf:["praes"],praet:["perf"],pron:["fall"],fall:["art"],konn:["satz"],tekamolo:["satz"]};
var tb=document.querySelector("#topic .seg");if(!tb||typeof openTopic!=="function")return;
var el=document.createElement("div");el.id="pre";el.hidden=true;document.getElementById("seg").after(el);
function nm(t){var x=TOPICS.find(function(y){return y.t===t});return x?x.n:null}
function upd(){var t=typeof T!=="undefined"?T:null,l=(PRE[t]||[]).filter(nm);
 var show=l.length&&!document.getElementById("topic").hidden;
 el.hidden=!show;if(!show){el.innerHTML="";return}
 var h='<span class="pl">Zuerst</span>';
 l.forEach(function(x,i){h+=(i?'<span class="ps">·</span>':'')+'<button type="button" data-t="'+x+'">'+nm(x)+'</button>'});
 if(el.dataset.k!==t){el.innerHTML=h;el.dataset.k=t}}
el.addEventListener("click",function(e){var b=e.target.closest("button");if(b){el.dataset.k="";openTopic(b.dataset.t)}});
setInterval(upd,300);
})();</script>"""
k=len(s)
s=s[:k]+css+js+s[k:]
open(os.path.join(root,"voraus.html"),"w",encoding="utf-8").write(s);print("ok")
