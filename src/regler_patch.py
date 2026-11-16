import re,sys
p="index.html"; s=open(p,encoding="utf-8").read()
if "function tpxCard" in s: sys.exit("already patched")
# 1. alten Regler entfernen
i=s.index(".tpx .tpvb{"); j=s.index(".theo{flex:1 1 auto"); s=s[:i]+s[j:]
i=s.index("function tpxHTML"); j=s.index("GT.perf={"); s=s[:i]+s[j:]
s=s.replace("${tpxHTML()}","${tpxHTML('t')}")
css=r'''.rgc{width:100%;box-sizing:border-box;position:relative;background:#fff;box-shadow:0 2px 18px rgba(0,0,0,.14);padding:10px 12px 10px;display:flex;flex-direction:column;gap:8px;color:var(--fg);text-align:left}
.rgc::after{content:"";position:absolute;inset:0;pointer-events:none;background:var(--df) left top/100% 1px no-repeat,var(--df) left bottom/100% 1px no-repeat,var(--dfv) left top/1px 100% no-repeat,var(--dfv) right top/1px 100% no-repeat}
.rgc button{font:inherit;cursor:pointer;background:transparent;border:0;color:inherit;padding:0}
.rgt{display:flex;justify-content:center;align-items:center;height:30px;margin-top:-4px}
.rgo2{display:flex;justify-content:space-between;gap:8px;flex-wrap:wrap}
.rgn{font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
.rgo{display:inline-flex}.rgo button{padding:4px 9px;font-size:14px;color:var(--muted);border:1px solid var(--line);margin-left:-1px}
.rgo button[aria-pressed="true"]{background:var(--ink);color:#fff;border-color:var(--ink);font-weight:700}
.rgbd{display:flex;margin:0 38px;font-size:11px;letter-spacing:.06em;text-transform:uppercase;color:var(--ink)}
.rgbd span{padding:3px 0;text-align:center;border-left:1px solid #fff}
.rgrow{display:flex;align-items:flex-start;gap:4px}
.rga{flex:none;width:34px;height:44px;font-size:26px;line-height:1;color:var(--ink)}
.rgdots{flex:1;display:flex;position:relative}
.rgdots::before{content:"";position:absolute;left:8%;right:8%;top:11px;height:2px;background:var(--ink)}
.rgdot{flex:1;position:relative;display:flex;flex-direction:column;align-items:center;gap:4px;font-size:12px;color:var(--muted);min-width:0}
.rgdot i{width:22px;height:22px;border-radius:50%;background:#fff;border:2px solid var(--ink);box-sizing:border-box}
.rgdot[aria-pressed="true"]{color:var(--fg);font-weight:700}.rgdot[aria-pressed="true"] i{background:var(--red);border-color:var(--red);transform:scale(1.25)}
.rgs{background:var(--pale);padding:12px 8px;touch-action:pan-y;user-select:none;min-height:3.2em;display:flex;align-items:center}
.rgsn{width:100%;white-space:nowrap;overflow:hidden;line-height:1.5;font-size:22px}
.stagew:has(.rgc){flex:0 0 auto}
.stage:has(.rgc){overflow-y:auto;justify-content:flex-start}
.rgsn.wr{white-space:normal}
.rgsn span{padding:1px 3px}.rgsn span.p{padding:1px 0}.rgsn .t{color:var(--muted)}.rgsn .v{background:var(--lime);font-weight:700}.rgsn .e{background:var(--yellow);font-weight:700}
.rgsn .n0{background:var(--mnom);font-weight:700}.rgsn .n1{background:var(--makk2);font-weight:700}.rgsn .n2{background:var(--mdat);font-weight:700}.rgsn .n3{background:var(--mgen);font-weight:700}
.rgh{display:flex;align-items:baseline;gap:8px;flex-wrap:wrap}.rgh b{font-size:1.25rem}.rgh small{font-size:13px;color:var(--muted)}
.rgi>div{display:flex;gap:10px;padding:4px 0;font-size:15px;line-height:1.35;background:var(--df) left top/100% 1px no-repeat}
.rgi>div>span:first-child{width:78px;flex:none;color:var(--muted)}
.rgi>div.on{font-weight:700;background-color:var(--pale)}
'''
js=r'''(function(){
var TL=["#e3d8c8","#d3def0","#eaffae","#fffbd6"];
var D={
t:{n:"Zeitformen",o1:["lernen","gehen"],ab:["Plusq.","Prät.","Perf.","Präs.","Fut I","Fut II"],i0:3,
 bands:[["Vergangenheit",3,"#e3d8c8"],["Jetzt",1,"#eaffae"],["Zukunft",2,"#d3def0"]],
 nm:["Plusquamperfekt","Präteritum","Perfekt","Präsens","Futur I","Futur II"],
 st:["Vorvergangenheit","Vergangenheit","Vergangenheit","Gegenwart","Zukunft","Zukunft"],
 S:[
 [[[["Davor","t"],["hatte","v"],["ich","t"],["gelernt","e"]],[["Nachdem ich","t"],["gelernt","e"],["hatte","v"],[", ","t"],["ging","v"],["ich spazieren.","t"]]],
  [[["Davor","t"],["war","v"],["ich","t"],["gegangen","e"]],[["Nachdem sie","t"],["gegangen","e"],["war","v"],[", ","t"],["war","v"],["es still.","t"]]]],
 [[[["Damals","t"],["lernte","v"],["ich","t"]],[["Als ich jung","t"],["war","v"],[", ","t"],["lernte","v"],["ich jeden Abend.","t"]]],
  [[["Damals","t"],["ging","v"],["ich","t"]],[["Als es dunkel","t"],["wurde","v"],[", ","t"],["ging","v"],["ich nach Hause.","t"]]]],
 [[[["Gestern","t"],["habe","v"],["ich","t"],["gelernt","e"]],[["Obwohl ich müde","t"],["war","v"],[", ","t"],["habe","v"],["ich gestern lange","t"],["gelernt","e"],[".","t"]]],
  [[["Gestern","t"],["bin","v"],["ich","t"],["gegangen","e"]],[["Weil es","t"],["regnete","v"],[", ","t"],["bin","v"],["ich früh nach Hause","t"],["gegangen","e"],[".","t"]]]],
 [[[["Jetzt","t"],["lerne","v"],["ich","t"]],[["Weil morgen die Prüfung","t"],["ist","v"],[", ","t"],["lerne","v"],["ich jetzt.","t"]]],
  [[["Jetzt","t"],["gehe","v"],["ich","t"]],[["Wenn es","t"],["regnet","v"],[", ","t"],["gehe","v"],["ich nicht spazieren.","t"]]]],
 [[[["Morgen","t"],["werde","v"],["ich","t"],["lernen","e"]],[["Wenn ich Zeit","t"],["habe","v"],[", ","t"],["werde","v"],["ich morgen","t"],["lernen","e"],[".","t"]]],
  [[["Morgen","t"],["werde","v"],["ich","t"],["gehen","e"]],[["Wenn du","t"],["willst","v"],[", ","t"],["werde","v"],["ich mit dir","t"],["gehen","e"],[".","t"]]]],
 [[[["Bis Montag","t"],["werde","v"],["ich","t"],["gelernt haben","e"]],[["Bis die Prüfung","t"],["beginnt","v"],[", ","t"],["werde","v"],["ich alles","t"],["gelernt haben","e"],[".","t"]]],
  [[["Bis Montag","t"],["werde","v"],["ich","t"],["gegangen sein","e"]],[["Bis du","t"],["ankommst","v"],[", ","t"],["werde","v"],["ich schon","t"],["gegangen sein","e"],[".","t"]]]]],
 I:[["hatte / war + Partizip II","Before another past event","nachdem, bevor, bereits"],["Stem + -te, or a new vowel","Stories, reports; war, hatte, konnte","damals, früher, als"],["habe / bin + Partizip II","Spoken past, letters, emails","gestern, schon, gerade"],["Stem + ending","Now, always, planned future","jetzt, heute, immer"],["werde + Infinitiv","Plans, forecasts, a guess about now","bald, wohl"],["werde + Partizip II + haben / sein","Finished by a future time; a guess about the past","bis morgen, sicher"]],
 L:["Bildung","Gebrauch","Signale"],leg:"Grün: konjugiertes Verb · Gelb: Rest des Verbs"},
k:{n:"Fälle",o1:["der Mann","die Frau","das Kind","die Kinder","der Student"],ab:["Nom","Akk","Dat","Gen"],i0:1,
 bands:[["Wer?",1,"#e6e6e3"],["Wen?",1,"#f4dcd8"],["Wem?",1,"#d3def0"],["Wessen?",1,"#f5efcf"]],
 nm:["Nominativ","Akkusativ","Dativ","Genitiv"],st:["Wer oder was?","Wen oder was?","Wem?","Wessen?"],
 F:[["der Mann","den Mann","dem Mann","des Mannes"],["die Frau","die Frau","der Frau","der Frau"],["das Kind","das Kind","dem Kind","des Kindes"],["die Kinder","die Kinder","den Kindern","der Kinder"],["der Student","den Studenten","dem Studenten","des Studenten"]],
 I:["Subject: who does it. Also after sein.","Direct object: sehen, finden, kaufen. Also after für, durch, ohne.","Indirect object: helfen, danken, gehören. Also after mit, bei, nach.","Belonging: das Auto des Mannes. Also after wegen, trotz, während."],
 leg:"Der Artikel (und das Nomen) ändert sich mit dem Fall."}};
function cap(x){return x.charAt(0).toUpperCase()+x.slice(1)}
function parts(k,i,v,l){
 if(k==="t")return D.t.S[i][v][l];
 var f=D.k.F[v][i],pl=v==3;
 if(!l){if(i==0)return [[cap(f),"n0"],[pl?"kommen.":"kommt.","t"]];if(i==1)return [["Ich sehe","t"],[f,"n1"],[".","t"]];if(i==2)return [["Ich helfe","t"],[f,"n2"],[".","t"]];return [["Das ist das Auto","t"],[f,"n3"],[".","t"]];}
 if(i==0)return [["Ich weiß, dass","t"],[f,"n0"],[pl?"kommen.":"kommt.","t"]];
 if(i==1)return [["Ich weiß, dass er","t"],[f,"n1"],["sieht.","t"]];
 if(i==2)return [["Ich weiß, dass er","t"],[f,"n2"],["hilft.","t"]];
 return [["Ich weiß, dass das Auto","t"],[f,"n3"],["kaputt ist.","t"]];}
function fit(el){el.classList.remove("wr");el.style.fontSize="22px";var fs=22;while(el.scrollWidth>el.clientWidth+1&&fs>14){fs--;el.style.fontSize=fs+"px"}if(el.scrollWidth>el.clientWidth+1)el.classList.add("wr");}
window.tpxHTML=function(k){k=k||"t";var d=D[k];
 var o1=d.o1.map(function(x,j){return '<button type="button" data-o="v'+j+'" aria-pressed="'+(j==0)+'">'+x+'</button>'}).join("");
 var bd=d.bands.map(function(b){return '<span style="flex:'+b[1]+';background:'+b[2]+'">'+b[0]+'</span>'}).join("");
 var dots=d.ab.map(function(a,j){return '<button type="button" class="rgdot" data-s="='+j+'" aria-pressed="false" aria-label="'+d.nm[j]+'"><i></i>'+a+'</button>'}).join("");
 return '<div class="rgc" data-k="'+k+'" data-i="'+d.i0+'" data-v="0" data-l="0"><div class="rgt"><span class="rgn">'+d.n+'</span></div><div class="rgo2"><span class="rgo">'+o1+'</span><span class="rgo"><button type="button" data-o="l0" aria-pressed="true">kurz</button><button type="button" data-o="l1" aria-pressed="false">+ Nebensatz</button></span></div>'
 +'<div class="rgbd">'+bd+'</div><div class="rgrow"><button type="button" class="rga" data-s="-1" aria-label="zurück">‹</button><div class="rgdots">'+dots+'</div><button type="button" class="rga" data-s="1" aria-label="weiter">›</button></div>'
 +'<div class="rgs"><div class="rgsn"></div></div><div class="rgh"><b></b><small></small></div><div class="rgi"></div></div>';};
function draw(r){var k=r.dataset.k,d=D[k],i=+r.dataset.i,v=+r.dataset.v,l=+r.dataset.l;
 var sn=r.querySelector(".rgsn");sn.innerHTML=parts(k,i,v,l).map(function(x){return '<span class="'+x[1]+(/^[,.]\s*$/.test(x[0])?' p':'')+'">'+x[0].trim()+'</span>'}).join(" ").replace(/ <span class="t p">/g,'<span class="t p">');
 r.querySelectorAll(".rgdot").forEach(function(b,j){b.setAttribute("aria-pressed",j==i)});
 r.querySelectorAll("[data-o]").forEach(function(b){var o=b.dataset.o;b.setAttribute("aria-pressed",o===("v"+v)||o===("l"+l))});
 r.querySelector(".rgh b").textContent=d.nm[i];r.querySelector(".rgh small").textContent=d.st[i];
 r.querySelector(".rgi").innerHTML=k==="t"?d.I[i].map(function(t,j){return '<div><span>'+d.L[j]+'</span><span>'+t+'</span></div>'}).join(""):d.nm.map(function(n,j){return '<div'+(j==i?' class="on"':'')+'><span>'+n+'</span><span>'+d.F[v][j]+'</span></div>'}).join("")+'<div><span></span><span style="color:var(--muted);font-weight:400">'+d.I[i]+'</span></div>';
 fit(sn);}
function step(r,x){var d=D[r.dataset.k],n=d.nm.length,i=+r.dataset.i;if(x[0]==="=")i=+x.slice(1);else i=Math.max(0,Math.min(n-1,i+ +x));r.dataset.i=i;draw(r);}
function all(){document.querySelectorAll(".rgc").forEach(function(r){if(!r.dataset.d){r.dataset.d=1;draw(r)}});}
document.addEventListener("click",function(e){var b=e.target.closest&&e.target.closest(".rgc button");if(!b)return;var r=b.closest(".rgc");
 if(b.dataset.s!==undefined)step(r,b.dataset.s);else if(b.dataset.o){var o=b.dataset.o;r.dataset[o[0]]=o.slice(1);draw(r);}});
var X0=null;
document.addEventListener("touchstart",function(e){var s=e.target.closest&&e.target.closest(".rgs");X0=s?e.touches[0].clientX:null;},{passive:true});
document.addEventListener("touchend",function(e){if(X0===null)return;var s=e.target.closest&&e.target.closest(".rgc");var dx=e.changedTouches[0].clientX-X0;X0=null;if(s&&Math.abs(dx)>40)step(s,dx<0?"1":"-1");},{passive:true});
document.addEventListener("keydown",function(e){var r=document.querySelector(".rgc");if(!r||!(e.key==="ArrowLeft"||e.key==="ArrowRight")||document.activeElement.closest(".rgc")===null)return;step(r,e.key==="ArrowRight"?"1":"-1");});
window.tpxCard=function(k){return {b:"Regler",st:tpxHTML(k),tx:"",gt:"",say:""};};
new MutationObserver(all).observe(document.documentElement,{childList:true,subtree:true});
window.addEventListener("resize",function(){document.querySelectorAll(".rgsn").forEach(fit)});
})();
'''
a="GT.perf={"; assert s.count(a)==1; s=s.replace(a,js+a)
a=".theo{flex:1 1 auto"; assert s.count(a)==1; s=s.replace(a,css+a)
a="Object.keys(GT).forEach(k=>{SRC[k]=GT[k].src;TH[k]=()=>GT[k].th+srcCard(k);});"
assert s.count(a)==1
s=s.replace(a,a+"\nGT.perf.cards.unshift(tpxCard('t'));GT.praet.cards.unshift(tpxCard('t'));FALL_CARDS.unshift(tpxCard('k'));")
m=re.search(r'name="app-version" content="(\d{4}-\d\d-\d\d)([a-z]?)"',s)
s=s.replace(m.group(0),'name="app-version" content="%s%s"'%(m.group(1),chr(ord(m.group(2))+1)))
open(p,"w",encoding="utf-8").write(s);print("OK")
