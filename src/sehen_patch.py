import re, sys
p = "index.html"
s = open(p, encoding="utf-8").read()
if "function renderSehen" in s:
    sys.exit("already patched")

# ---------- CSS ----------
css = r'''
/* ---- Sehen: Zeiten und Fälle als Wischleiste (dasein look: dotted frames, red capitals) ---- */
.sehb{margin:0 0 14px;padding:10px 10px 12px;position:relative;background:#fff}
.sehb::after,.sv::after{content:"";position:absolute;inset:0;pointer-events:none;background:var(--df) left top/100% 1px no-repeat,var(--df) left bottom/100% 1px no-repeat,var(--dfv) left top/1px 100% no-repeat,var(--dfv) right top/1px 100% no-repeat}
.sehb h3{margin:0 0 2px;font-size:12px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--red)}
.sehb p{margin:0 0 8px;font-size:14px;line-height:1.35;color:var(--muted)}
.sehg{display:grid;grid-template-columns:1fr 1fr;gap:6px}
.sehk{position:relative;cursor:pointer;-webkit-tap-highlight-color:transparent;padding:6px 6px 8px;background:#fff}
.sehk::after{content:"";position:absolute;inset:0;pointer-events:none;background:var(--df) left top/100% 1px no-repeat,var(--df) left bottom/100% 1px no-repeat,var(--dfv) left top/1px 100% no-repeat,var(--dfv) right top/1px 100% no-repeat}
.sehk:active{background:var(--lime)}
.sehk b{display:block;font-size:11px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--red);margin-bottom:5px}
.sehk i{display:flex;gap:2px;height:14px;margin-bottom:4px}.sehk i s{display:block;flex:1;text-decoration:none}
.sehk small{font-size:12px;color:var(--muted)}
.sv{position:relative;margin:6px 8px;padding:14px 8px 8px;background:#fff;color:#2c2c2a}
.svg{display:grid;grid-template-columns:repeat(var(--n),minmax(0,1fr));gap:2px;margin:0 4px 3px}
.svb{position:relative;display:flex;align-items:center;justify-content:center;height:26px;box-sizing:border-box;border:.5px solid transparent;font-size:10px;font-weight:400;line-height:1;letter-spacing:.06em;text-transform:uppercase;white-space:nowrap;overflow:hidden;color:#2c2c2a;user-select:none;-webkit-tap-highlight-color:transparent}
.svb[role=button]{cursor:pointer;color:#555}
.svl,.svbd .svb{color:var(--red);font-weight:700;letter-spacing:.12em}
.svl{justify-content:flex-start}
.svbd{margin-top:10px}
.fr::after{content:"";position:absolute;inset:0;pointer-events:none;background:var(--df) left top/100% 1px no-repeat,var(--df) left bottom/100% 1px no-repeat,var(--dfv) left top/1px 100% no-repeat,var(--dfv) right top/1px 100% no-repeat}
.fr.on::after{display:none}
.svb.on{border-color:#000;color:#2c2c2a}
.svo.on{background:#e4f7a0}
.app[data-mode="theo"] #topic .theo:has(.sv){justify-content:flex-start;flex:1000 1 auto;margin-top:0;padding-top:8px}
.svt{display:flex;overflow-x:auto;scroll-snap-type:x mandatory;scrollbar-width:none;margin-top:24px}
.svt::-webkit-scrollbar{display:none}
.svp{flex:0 0 11%}
.svcol{flex:0 0 78%;scroll-snap-align:center;box-sizing:border-box;padding:14px 14px 0;opacity:.25;transition:opacity .2s;min-height:84px}
.svcol.on{opacity:1}
.svs{font-size:19px;line-height:1.4;margin:0;color:#1a1a1a}
.svs .g{background:#c8f23c;color:#1d2a00;padding:0 3px;border-radius:2px}
.svs .y{background:#fbe48a;color:#3a2c00;padding:0 3px;border-radius:2px}
.svi{margin:4px 4px 0}
.svti{justify-content:flex-start;padding:0 8px;margin-bottom:3px;font-weight:700;letter-spacing:.12em;border-color:#000}
.svr{display:flex;gap:10px;height:28px;align-items:center;box-sizing:border-box;padding:0 2px;white-space:nowrap;overflow:hidden;font-size:12px;color:var(--muted);background:var(--df) left bottom/100% 1px no-repeat}
.svr:first-of-type{background:var(--df) left top/100% 1px no-repeat,var(--df) left bottom/100% 1px no-repeat}
.svr span:first-child{flex:0 0 66px;font-size:10px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--red)}
.svh{margin:10px 0 0;text-align:center;font-size:11px;color:#999}
.svln{position:absolute;left:0;top:0;width:100%;height:100%;pointer-events:none;overflow:visible}
'''
a = ".hb.first{margin-top:14px}"
assert s.count(a) == 1
s = s.replace(a, a + css)

# ---------- banner on the Grammatik section (first thing after the title page) ----------
a = '<div class="lvsel" role="group" aria-label="Niveau">'
assert s.count(a) == 1
banner = ('<div class="sehb" id="sehb"><h3>Sehen</h3><p>Zeiten und Fälle auf einen Blick: wischen statt lesen.</p>'
          '<div class="sehg">'
          '<div class="sehk" role="button" tabindex="0" data-sv="t"><b>Zeiten</b><i><s style="background:#e6dccb;flex:3"></s><s style="background:#e4f7a0"></s><s style="background:#d3dff2;flex:2"></s></i><small>sechs Zeitformen</small></div>'
          '<div class="sehk" role="button" tabindex="0" data-sv="k"><b>Fälle</b><i><s style="background:#e6e6e3"></s><s style="background:#f4dcd8"></s><s style="background:#d3def0"></s><s style="background:#f5efcf"></s></i><small>vier Fälle</small></div>'
          '</div></div>')
s = s.replace(a, banner + a)

# ---------- topic wiring ----------
a = ' {t:"write",n:"Text prüfen"'
assert s.count(a) == 1
i = s.index(a)
j = s.index("\n", i) + 1
s = s[:j] + ' {t:"sehen",n:"Sehen",tag:"Zeiten · Fälle",ds:"Zeiten und Fälle als Wischleiste mit Beispielsätzen"},\n' + s[j:]

old = '$("seg").hidden=t==="test"||t==="links"||t==="write"||t==="lueck";setMode(t==="test"?"game":(t==="links"||t==="write"||t==="lueck")?"theo":"learn");'
assert s.count(old) == 1
s = s.replace(old, '$("seg").hidden=t==="test"||t==="links"||t==="write"||t==="lueck"||t==="sehen";setMode(t==="test"?"game":(t==="links"||t==="write"||t==="lueck"||t==="sehen")?"theo":"learn");')
old = 'T!=="links"&&T!=="write"&&T!=="lueck"){store.last'
assert s.count(old) == 1
s = s.replace(old, 'T!=="links"&&T!=="write"&&T!=="lueck"&&T!=="sehen"){store.last')
old = 'function score(t){if(t==="links"||t==="write"||t==="lueck")return null;'
assert s.count(old) == 1
s = s.replace(old, 'function score(t){if(t==="links"||t==="write"||t==="lueck"||t==="sehen")return null;')
old = 'if(T==="lueck"){renderLueck();$("theo").scrollTop=0;return;}theoGallery();'
assert s.count(old) == 1
s = s.replace(old, 'if(T==="lueck"){renderLueck();$("theo").scrollTop=0;return;}if(T==="sehen"){renderSehen();$("theo").scrollTop=0;return;}theoGallery();')

# ---------- JS ----------
js = r'''/* ---------- Sehen: Zeiten und Fälle ---------- */
const SVP="#e6dccb",SVN="#e4f7a0",SVF="#d3dff2";
const SVG_=x=>'<span class="g">'+x+'</span>',SVY_=x=>'<span class="y">'+x+'</span>';
const SV={tab:"t",sel:{t:[0,0],k:[0,0]},cur:{t:3,k:0}};
const SVT=[
{n:"Plusquamperfekt",f:"hatte / war + Partizip II",u:"Before another past event.",s:"nachdem, bevor, schon, vorher",a:"Nebensatz: gelernt hatte."},
{n:"Präteritum",f:"Stamm + -te (or Ablaut)",u:"Written past, narration.",s:"damals, als, einst",a:"Spoken: mostly sein, haben, Modalverben."},
{n:"Perfekt",f:"habe / bin + Partizip II",u:"Spoken past, result counts now.",s:"schon, heute, gestern",a:"bin with movement or change."},
{n:"Präsens",f:"Stamm + Endung",u:"Now, always, planned.",s:"jetzt, immer, morgen",a:"Also the future with a time word."},
{n:"Futur I",f:"werden + Infinitiv",u:"Plans, promises, guesses.",s:"bald, wohl, sicher",a:"Präsens + morgen is more common."},
{n:"Futur II",f:"werden + Partizip II + haben/sein",u:"Done by a future point; or a guess.",s:"bis dann, bis Freitag",a:"Er wird schon gegangen sein."}];
const G=SVG_,Y=SVY_;
const SVS=[[
[G('Hatte')+' ich '+Y('gelernt')+'.','Nachdem ich '+Y('gelernt')+' '+G('hatte')+', ging ich heim.',G('Hattest')+' du schon '+Y('gelernt')+'?'],
['Ich '+G('lernte')+'.','Ich '+G('lernte')+', während sie kochte.','Warum '+G('lerntest')+' du nie?'],
['Ich '+G('habe')+' '+Y('gelernt')+'.','Ich weiß, dass ich viel '+Y('gelernt')+' '+G('habe')+'.',G('Hast')+' du heute '+Y('gelernt')+'?'],
['Ich '+G('lerne')+'.','Ich '+G('lerne')+', weil ich C1 will.',G('Lernst')+' du heute Abend?'],
['Ich '+G('werde')+' '+Y('lernen')+'.','Ich glaube, dass ich morgen '+Y('lernen')+' '+G('werde')+'.',G('Wirst')+' du '+Y('lernen')+'?'],
['Ich '+G('werde')+' '+Y('gelernt haben')+'.','Bis Freitag '+G('werde')+' ich alles '+Y('gelernt haben')+'.',G('Wirst')+' du es dann '+Y('gelernt haben')+'?']
],[
['Ich '+G('war')+' '+Y('gegangen')+'.','Nachdem er '+Y('gegangen')+' '+G('war')+', wurde es still.',G('Warst')+' du schon '+Y('gegangen')+'?'],
['Ich '+G('ging')+'.','Ich '+G('ging')+', als es regnete.','Wohin '+G('gingst')+' du?'],
['Ich '+G('bin')+' '+Y('gegangen')+'.','Ich weiß, dass sie '+Y('gegangen')+' '+G('ist')+'.',G('Bist')+' du schon '+Y('gegangen')+'?'],
['Ich '+G('gehe')+'.','Ich '+G('gehe')+', weil es spät ist.',G('Gehst')+' du mit?'],
['Ich '+G('werde')+' '+Y('gehen')+'.','Ich denke, dass wir morgen '+Y('gehen')+' '+G('werden')+'.',G('Wirst')+' du '+Y('gehen')+'?'],
['Ich '+G('werde')+' '+Y('gegangen sein')+'.','Bis du kommst, '+G('werde')+' ich '+Y('gegangen sein')+'.',G('Wird')+' er schon '+Y('gegangen sein')+'?']
]];
const SVKC=[
{n:"Nominativ",q:"wer / was?",f:"the dictionary form",u:"Subject; after sein, werden.",s:"sein, werden, bleiben",a:"Ask: who does it?"},
{n:"Akkusativ",q:"wen / was?",f:"only masculine: der → den",u:"Object; für, durch, gegen, ohne.",s:"sehen, haben, kaufen · für, ohne",a:"die, das, die stay the same."},
{n:"Dativ",q:"wem?",f:"dem / der / dem / den",u:"Indirect object; mit, bei, nach, von.",s:"helfen, danken, gehören · mit, bei",a:"Plural noun gets -n: den Kindern."},
{n:"Genitiv",q:"wessen?",f:"des / der / des / der",u:"Possession; wegen, trotz, während.",s:"wegen, trotz, während · Besitz",a:"masc. / neut. noun takes -(e)s."}];
const SVK=[
[['Der Mann '+'schläft.','Ich sehe, dass der Mann schläft.'],['Ich sehe den Mann.','Ich weiß, dass sie den Mann kennt.'],['Ich helfe dem Mann.','Ich glaube, dass sie dem Mann hilft.'],['Das ist das Auto des Mannes.','Sie fragt, wo das Auto des Mannes steht.']],
[['Die Frau schläft.','Ich sehe, dass die Frau schläft.'],['Ich sehe die Frau.','Ich weiß, dass er die Frau kennt.'],['Ich helfe der Frau.','Ich glaube, dass er der Frau hilft.'],['Das ist das Auto der Frau.','Sie fragt, wo das Auto der Frau steht.']],
[['Das Kind schläft.','Ich sehe, dass das Kind schläft.'],['Ich sehe das Kind.','Ich weiß, dass er das Kind kennt.'],['Ich helfe dem Kind.','Ich glaube, dass er dem Kind hilft.'],['Das ist das Auto des Kindes.','Sie fragt, wo das Auto des Kindes steht.']],
[['Die Kinder schlafen.','Ich sehe, dass die Kinder schlafen.'],['Ich sehe die Kinder.','Ich weiß, dass er die Kinder kennt.'],['Ich helfe den Kindern.','Ich glaube, dass er den Kindern hilft.'],['Das ist das Auto der Kinder.','Sie fragt, wo das Auto der Kinder steht.']]];
/* article green, noun yellow: marked in the sentence by the nouns/articles of each Wort */
const SVW=[["der","den","dem","des"],["die","die","der","der"],["das","das","dem","des"],["die","die","den","der"]];
const SVN_=[["Mann","Mann","Mann","Mannes"],["Frau","Frau","Frau","Frau"],["Kind","Kind","Kind","Kindes"],["Kinder","Kinder","Kindern","Kinder"]];
function svMark(w,c,txt){const art=SVW[w][c],no=SVN_[w][c],re=new RegExp('\\b('+art+'|'+art.charAt(0).toUpperCase()+art.slice(1)+') ('+no+')\\b');
  return txt.replace(re,(m,a,n)=>SVG_(a)+' '+SVY_(n));}
const SVCFG={
t:{N:6,L:1,rows:[{l:"Satz",o:[["kurz",2],["+ Nebensatz",2],["Frage",1]]},{l:"Verb",o:[["lernen (haben)",3],["gehen (sein)",2]]}],
 bands:[["Vergangenheit",3,SVP],["Jetzt",1,SVN],["Zukunft",2,SVF]],chips:["Plusq.","Prät.","Perf.","Präs.","Fut. I","Fut. II"],cs:1,
 fills:[SVP,SVP,"linear-gradient(90deg,"+SVP+" 50%,"+SVN+" 50%)",SVN,SVF,"linear-gradient(90deg,"+SVF+" 50%,"+SVP+" 50%)"],
 sent:(i,sel)=>SVS[sel[1]][i][sel[0]],info:i=>SVT[i],title:i=>SVT[i].n},
k:{N:20,L:4,rows:[{l:"Satz",o:[["kurz",8],["+ Nebensatz",8]]},{l:"Wort",o:[["der Mann",4],["die Frau",4],["das Kind",4],["Plural",4]]}],
 bands:[["Subjekt",5,"#e6e6e3"],["Objekt",10,"linear-gradient(90deg,#f4dcd8 50%,#d3def0 50%)"],["Besitz",5,"#f5efcf"]],chips:["Nom.","Akk.","Dat.","Gen."],cs:5,
 fills:["#e6e6e3","#f4dcd8","#d3def0","#f5efcf"],
 sent:(i,sel)=>svMark(sel[1],i,SVK[sel[1]][i][sel[0]]),info:i=>SVKC[i],title:i=>SVKC[i].n+" · "+SVKC[i].q}};
function renderSehen(){const th=$("theo"),cfg=SVCFG[SV.tab],sel=SV.sel[SV.tab];let cur=SV.cur[SV.tab];
  let h='<div class="sv" id="sv"><div class="svg" style="--n:2"><span role="button" tabindex="0" class="svb svo fr'+(SV.tab==="t"?' on':'')+'" data-tab="t">Zeiten</span><span role="button" tabindex="0" class="svb svo fr'+(SV.tab==="k"?' on':'')+'" data-tab="k">Fälle</span></div><div style="height:6px"></div>';
  cfg.rows.forEach((r,ri)=>{h+='<div class="svg" style="--n:'+cfg.N+'"><span class="svb svl" style="grid-column:span '+cfg.L+'">'+r.l+'</span>'+r.o.map((o,oi)=>'<span role="button" tabindex="0" class="svb svo fr'+(sel[ri]===oi?' on':'')+'" data-r="'+ri+'" data-o="'+oi+'" style="grid-column:span '+o[1]+'">'+o[0]+'</span>').join('')+'</div>';});
  h+='<div class="svg svbd" style="--n:'+cfg.N+'">'+cfg.bands.map(b=>'<span class="svb" style="grid-column:span '+b[1]+';background:'+b[2]+'">'+b[0]+'</span>').join('')+'</div>';
  h+='<div class="svg" id="svc" style="--n:'+cfg.N+'">'+cfg.chips.map((c,i)=>'<span role="button" tabindex="0" class="svb svk fr" data-i="'+i+'" style="grid-column:span '+cfg.cs+'">'+c+'</span>').join('')+'</div>';
  h+='<div class="svt" id="svt"></div><div class="svi" id="svi"></div><p class="svh">wischen · Kasten antippen</p><svg class="svln" aria-hidden="true"><path id="svpath" fill="none" stroke="#b8b8b8" stroke-width="1.2" stroke-linecap="round" stroke-dasharray="0.5 2.5"/></svg></div>';
  th.innerHTML=h;
  const root=$("sv"),trk=$("svt"),chips=$("svc"),info=$("svi");
  const cw=()=>{const c=trk.querySelector(".svcol");return c?c.offsetWidth:1;};
  const line=()=>{const on=chips.querySelector(".svk.on");if(!on||!trk.isConnected)return;const W=root.getBoundingClientRect(),c=on.getBoundingClientRect(),r=trk.getBoundingClientRect();
    const x1=c.left+c.width/2-W.left,y1=c.bottom-W.top+3,x2=r.left+r.width*.11+18-W.left,y2=r.top-W.top+16,ym=y1+(y2-y1)/2;$("svpath").setAttribute("d","M"+x1+" "+y1+" V"+ym+" H"+x2+" V"+y2);};
  const marks=i=>{cur=SV.cur[SV.tab]=i;
    trk.querySelectorAll(".svcol").forEach((c,k)=>c.classList.toggle("on",k===i));
    chips.querySelectorAll(".svk").forEach(c=>{const on=+c.dataset.i===i;c.classList.toggle("on",on);c.style.background=on?cfg.fills[i]:"";});
    const x=cfg.info(i);info.innerHTML='<div class="svb svti" style="background:'+cfg.fills[i]+'">'+esc(cfg.title(i))+'</div><div class="svr"><span>Bildung</span><span>'+esc(x.f)+'</span></div><div class="svr"><span>Gebrauch</span><span>'+esc(x.u)+'</span></div><div class="svr"><span>Signale</span><span>'+esc(x.s)+'</span></div><div class="svr"><span>Achtung</span><span>'+esc(x.a)+'</span></div>';line();};
  const cols=()=>{trk.innerHTML='<div class="svp"></div>'+cfg.chips.map((c,i)=>'<div class="svcol"><p class="svs">'+cfg.sent(i,sel)+'</p></div>').join('')+'<div class="svp"></div>';marks(cur);};
  const go=(i,sm)=>trk.scrollTo({left:i*cw(),behavior:sm?"smooth":"auto"});
  cols();
  let raf=0;trk.addEventListener("scroll",()=>{cancelAnimationFrame(raf);raf=requestAnimationFrame(()=>{const i=Math.max(0,Math.min(cfg.chips.length-1,Math.round(trk.scrollLeft/cw())));if(i!==cur)marks(i);});});
  root.addEventListener("click",e=>{const b=e.target.closest("[role=button]");if(!b||!root.contains(b))return;
    if(b.dataset.tab){SV.tab=b.dataset.tab;renderSehen();return;}
    if(b.classList.contains("svk")){const i=+b.dataset.i;marks(i);go(i,true);return;}
    if(b.dataset.r!==undefined){sel[+b.dataset.r]=+b.dataset.o;root.querySelectorAll('.svo[data-r="'+b.dataset.r+'"]').forEach(x=>x.classList.toggle("on",x===b));cols();go(cur,false);}});
  root.addEventListener("keydown",e=>{if((e.key==="Enter"||e.key===" ")&&e.target.getAttribute("role")==="button"){e.preventDefault();e.target.click();}});
  window.addEventListener("resize",line);
  requestAnimationFrame(()=>requestAnimationFrame(()=>{go(cur,false);line();}));}
document.querySelectorAll("#sehb .sehk").forEach(b=>{const go=()=>{SV.tab=b.dataset.sv;openTopic("sehen");};b.addEventListener("click",go);b.addEventListener("keydown",e=>{if(e.key==="Enter"||e.key===" "){e.preventDefault();go();}});});
'''
a = "/* ---------- navigation ---------- */"
assert s.count(a) == 1
s = s.replace(a, js + a)

# ---------- version ----------
m = re.search(r'name="app-version" content="(\d{4}-\d\d-\d\d)([a-z]?)"', s)
s = s.replace(m.group(0), 'name="app-version" content="%s%s"' % (m.group(1), chr(ord(m.group(2) or "`") + 1)))
open(p, "w", encoding="utf-8").write(s)
print("ok", re.search(r'name="app-version" content="([^"]+)"', s).group(1))
