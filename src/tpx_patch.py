import re,sys
p="index.html"; s=open(p,encoding="utf-8").read()
if "function tpxHTML" in s: sys.exit("already patched")
css=""".tpx .vb{display:flex;gap:6px}.tpx .vb button{flex:1;padding:7px 4px;border:1px solid var(--line);background:transparent;color:var(--muted);font:inherit;font-size:15px}
.tpx .vb button[aria-pressed="true"]{background:var(--pale);color:var(--fg);font-weight:700;border-color:var(--ink)}
.tpx .sn{min-height:70px;display:flex;flex-wrap:wrap;gap:6px;align-items:center;font-size:21px;line-height:1.3}
.tpx .sn span{padding:1px 7px}.tpx .sn .t{color:var(--muted)}.tpx .sn .v{background:var(--lime);font-weight:700}.tpx .sn .e{background:var(--yellow);font-weight:700}
.tpx input[type=range]{width:100%;margin:4px 0 0;accent-color:var(--red);height:28px}
.tpx .tk{display:flex;justify-content:space-between;font-size:12px;color:var(--muted)}.tpx .tk b{font-weight:400;width:16.6%;text-align:center}.tpx .tk b.on{color:var(--fg);font-weight:700}
.tpx .hd{display:flex;align-items:baseline;gap:8px;flex-wrap:wrap}.tpx .hd b{font-size:1.25rem}.tpx .hd small{font-size:13px;color:var(--muted)}
.tpx .inf>div{display:flex;gap:10px;padding:4px 0;font-size:16px;line-height:1.35;border-top:1px solid transparent;background:var(--df) left top/100% 1px no-repeat}
.tpx .inf>div span:first-child{width:70px;flex:none;color:var(--muted)}
"""
js=r'''function tpxHTML(){
return '<div class="tc df tpx"><h3>Regler: Zeitformen <small>schiebe von früher nach später</small></h3><div class="vb"><button type="button" data-v="0" aria-pressed="true">lernen</button><button type="button" data-v="1" aria-pressed="false">gehen</button></div><div class="sn"></div><input type="range" min="0" max="5" step="1" value="3" aria-label="Zeitform wählen"><div class="tk"><b>Plusq.</b><b>Prät.</b><b>Perf.</b><b class="on">Präs.</b><b>Fut I</b><b>Fut II</b></div><div class="hd"><b></b><small></small></div><div class="inf"></div><p class="tline">Gelb: der Rest des Verbs am Satzende. Grün: das Verb an Position 2.</p></div>';}
(function(){
var N=["Plusquamperfekt","Präteritum","Perfekt","Präsens","Futur I","Futur II"],ST=["Vorvergangenheit","Vergangenheit","Vergangenheit","Gegenwart","Zukunft","Zukunft"];
var S=[[[["Davor","t"],["hatte","v"],["ich","t"],["gelernt","e"]],[["Davor","t"],["war","v"],["ich","t"],["gegangen","e"]]],
[[["Damals","t"],["lernte","v"],["ich","t"]],[["Damals","t"],["ging","v"],["ich","t"]]],
[[["Gestern","t"],["habe","v"],["ich","t"],["gelernt","e"]],[["Gestern","t"],["bin","v"],["ich","t"],["gegangen","e"]]],
[[["Jetzt","t"],["lerne","v"],["ich","t"]],[["Jetzt","t"],["gehe","v"],["ich","t"]]],
[[["Morgen","t"],["werde","v"],["ich","t"],["lernen","e"]],[["Morgen","t"],["werde","v"],["ich","t"],["gehen","e"]]],
[[["Bis Montag","t"],["werde","v"],["ich","t"],["gelernt haben","e"]],[["Bis Montag","t"],["werde","v"],["ich","t"],["gegangen sein","e"]]]];
var I=[["hatte / war + Partizip II","Before another past event","nachdem, bevor, bereits"],["Stem + -te, or a new vowel","Stories, reports; war, hatte, konnte","damals, früher, 1995"],["habe / bin + Partizip II","Spoken past, letters, emails","gestern, schon, gerade"],["Stem + ending","Now, always, planned future","jetzt, heute, immer"],["werde + Infinitiv","Plans, forecasts, a guess about now","bald, wohl"],["werde + Partizip II + haben / sein","Finished by a future time; a guess about the past","bis morgen, sicher"]];
var L=["Bildung","Gebrauch","Signale"];
function draw(r){var i=+r.querySelector("input").value,v=+r.dataset.v||0;
r.querySelector(".sn").innerHTML=S[i][v].map(function(p){return '<span class="'+p[1]+'">'+p[0]+'</span>'}).join("");
r.querySelector(".hd b").textContent=N[i];r.querySelector(".hd small").textContent=ST[i];
r.querySelectorAll(".tk b").forEach(function(b,k){b.className=k==i?"on":""});
r.querySelector(".inf").innerHTML=I[i].map(function(t,j){return '<div><span>'+L[j]+'</span><span>'+t+'</span></div>'}).join("");}
function all(){document.querySelectorAll(".tpx").forEach(function(r){if(!r.dataset.d){r.dataset.d=1;draw(r)}});}
document.addEventListener("input",function(e){var r=e.target.closest&&e.target.closest(".tpx");if(r)draw(r)});
document.addEventListener("click",function(e){var b=e.target.closest&&e.target.closest(".tpx [data-v]");if(!b)return;var r=b.closest(".tpx");r.dataset.v=b.dataset.v;r.querySelectorAll("[data-v]").forEach(function(x){x.setAttribute("aria-pressed",x===b)});draw(r)});
new MutationObserver(all).observe(document.documentElement,{childList:true,subtree:true});
})();
'''
a="GT.perf={"
assert s.count(a)==1
s=s.replace(a,js+a)
a=".theo{flex:1 1 auto"
assert s.count(a)==1
s=s.replace(a,css+a)
i=s.index("GT.perf="); k=s.index(" th:`",i)+len(" th:`"); s=s[:k]+"${tpxHTML()}"+s[k:]
i=s.index("GT.praet="); k=s.index(" th:`",i)+len(" th:`"); s=s[:k]+"${tpxHTML()}"+s[k:]
m=re.search(r'name="app-version" content="(\d{4}-\d\d-\d\d)([a-z]?)"',s)
s=s.replace(m.group(0),'name="app-version" content="%s%s"'%(m.group(1),chr(ord(m.group(2))+1)))
open(p,"w",encoding="utf-8").write(s);print("OK")
