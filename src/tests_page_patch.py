p='index.html';s=open(p,encoding='utf8').read()
# 1) new renderTest markup (same boxes/strip/rows as Grammatik)
a=s.index('function renderTest(){')
b=s.index('$("p-links").innerHTML=TH_LINKS;')
new='''function renderTest(){
  const L=store.level||"all",ne=Object.keys(mistakes()).length;
  $("p-test").innerHTML='<div class="tc tpg">'+
   '<div class="sehb"><div class="sehg"><div class="sehk tkx"><b>Länge</b><div class="tlen2">'+[15,30,45].map(k=>'<button data-n="'+k+'" aria-pressed="'+(TLEN()===k)+'">'+k+'</button>').join("")+'</i></div>'+
   '<div class="sehk tkx" id="tErr"'+(ne?'':' hidden')+'><b>Fehler üben</b><span class="tern">'+ne+(ne===1?' Frage':' Fragen')+' →</span></div></div></div>'+
   '<div class="lvsel" role="group" aria-label="Niveau"><div id="lvs2">'+["all"].concat(LVLS.slice(0,5)).map(l=>'<button class="lvb" data-l="'+l+'" aria-pressed="'+(L===l)+'">'+(l==="all"?"Alle":l)+'</button>').join("")+'</div></div>'+
   '<div class="rcb"><button class="resume" id="goTest"><span><small>Test starten</small><b>'+TLEN()+' Fragen · '+(L==="all"?"alle Stufen":L)+'</b></span><b>→</b></button></div>'+
   '<div class="tests rows2"><button class="tst wide" id="goLueck"><b>Lückentext</b><small>ganze Texte · A1–C1 · mit Korrektur</small></button><button class="tst wide" id="goWrite"><b>Text prüfen</b><small>Schreiben A1–C1 · mit LanguageTool</small></button><button class="tst wide" id="goSet"><b class="setb"><span class="cogi" aria-hidden="true"></span>Info &amp; Einstellungen</b><small>Anleitung · Timer · neueste Version</small></button></div></div>';
  $("p-test").querySelectorAll(".tlen2 button").forEach(x=>x.onclick=()=>{store.tlen=+x.dataset.n;save();renderTest();});
  $("p-test").querySelectorAll("#lvs2 .lvb").forEach(x=>x.onclick=()=>{store.level=x.dataset.l;save();renderHome();renderTest();});
  $("goTest").onclick=()=>{TESTLV=(store.level&&store.level!=="all")?store.level:"all";openTopic("test");};
  $("tErr").onclick=()=>{ERRMODE=true;openTopic("test");$("ttl").textContent="Deine Fehler";setMode("game");};
  $("goWrite").onclick=()=>openTopic("write");$("goSet").onclick=()=>{const c=$("cogb");if(c)c.click();};$("goLueck").onclick=()=>openTopic("lueck");}
'''
s=s[:a]+new+s[b:]
# 2) level handler on Grammatik also refreshes Tests
h='document.querySelectorAll(".lvb").forEach(b=>b.onclick=()=>{store.level=b.dataset.l;save();renderHome();});'
assert s.count(h)==1
s=s.replace(h,'document.querySelectorAll("#lvs .lvb").forEach(b=>b.onclick=()=>{store.level=b.dataset.l;save();renderHome();if(typeof renderTest==="function"&&$("p-test").firstChild)renderTest();});')
# 3) css
css='''<style id="tests-page-css">
.tpg .sehb{margin:0 0 12px}
.tpg .lvsel{margin:0 0 12px}
.tkx[hidden]{display:none}
.sehg:has(#tErr[hidden]){grid-template-columns:1fr}
.tlen2{display:flex!important;gap:2px;height:24px}
.tlen2 button{flex:1;min-width:0;background:#ebebe9;font-size:13px;padding:0;box-shadow:none!important}
.tlen2 button[aria-pressed="true"]{background:#cdff3e!important;font-weight:700}
.tern{display:block;height:24px;line-height:24px;background:#fadfdc;padding:0 8px;font-size:13px;font-weight:700}
.tpg .rcb{margin:0 0 12px}
.tpg .rcb .resume{padding:9px 12px}
.tpg .rcb .resume b{font-size:16px}
.tests.rows2{display:grid!important;grid-template-columns:1fr!important;gap:4px!important}
.tests.rows2 .tst{background:var(--df) left top/100% 1px no-repeat,var(--df) left bottom/100% 1px no-repeat,var(--dfv) left top/1px 100% no-repeat,var(--dfv) right top/1px 100% no-repeat,#fff!important;min-height:52px;padding:8px 12px}
.tests.rows2 .tst b{font-size:1.1rem}
.hb.on{background-color:#3c403d!important;color:#fff}
.hb.on small{color:#cfd2cd}
</style>
'''
k=s.index('<script id="info-link-js">')
assert 'tests-page-css' not in s
s=s[:k]+css+s[k:]
s=s.replace('<meta name="app-version" content="2026-11-17u">','<meta name="app-version" content="2026-11-17v">')
open(p,'w',encoding='utf8').write(s)
