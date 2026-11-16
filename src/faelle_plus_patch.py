import re, sys
p = "index.html"
s = open(p, encoding="utf-8").read()
if "function renderSehenX" in s:
    sys.exit("already patched")

def rep(a, b):
    global s
    assert s.count(a) == 1, a[:70]
    s = s.replace(a, b)

# ---- state ----
rep('const SV={tab:"t",sel:{t:[0,0],k:[0,0]},cur:{t:3,k:0}};',
    'const SV={tab:"t",sel:{t:[0,0],k:[0,0]},cur:{t:3,k:0},kp:"s",at:0,aw:"der",pp:{g:"W",w:"an"},rl:{g:"W",i:0,wo:0}};')

# ---- hooks into the existing renderSehen ----
rep('function renderSehen(){const th=$("theo"),',
    'function renderSehen(){if(SV.tab==="k"&&SV.kp&&SV.kp!=="s")return renderSehenX();const th=$("theo"),')
rep('data-tab="k">Fälle</span></div><div style="height:6px"></div>\';',
    'data-tab="k">Fälle</span></div\'+(SV.tab==="k"?svSub():"")+\'<div style="height:6px"></div>\';')
rep('if(b.dataset.tab){SV.tab=b.dataset.tab;renderSehen();return;}',
    'if(b.dataset.kp){SV.kp=b.dataset.kp;renderSehen();return;}if(b.dataset.tab){SV.tab=b.dataset.tab;renderSehen();return;}')
rep('SV.tab=b.dataset.sv;if(sg', 'SV.tab=b.dataset.sv;SV.kp="s";if(sg')

# ---- CSS ----
css = '''
.sag{position:relative;display:grid;grid-template-columns:40px repeat(4,minmax(0,1fr));grid-template-rows:26px repeat(4,46px);margin:0 4px 6px}
.sag::after{content:"";position:absolute;inset:0;pointer-events:none;background:var(--df) left top/100% 1px no-repeat,var(--df) left bottom/100% 1px no-repeat,var(--dfv) left top/1px 100% no-repeat,var(--dfv) right top/1px 100% no-repeat}
.sag .svb{height:auto}
.svl.cc{justify-content:center}
.sat{display:flex;align-items:center;justify-content:center;box-sizing:border-box;font-size:16px;font-weight:600;letter-spacing:.04em;text-transform:uppercase;color:#1a1a1a;cursor:pointer;-webkit-tap-highlight-color:transparent;user-select:none}
.sat.on{background-color:#e4f7a0!important}
.sat.nn{color:#aaa;cursor:default}
.sat.lg{font-size:13px;letter-spacing:.02em}
.svbn{color:var(--red);font-weight:700;letter-spacing:.12em}
.svw{text-transform:none;font-size:12px;letter-spacing:0;height:24px}
.spc{align-items:start}
.spcol{display:flex;flex-direction:column;gap:2px}
.svx{margin:8px 4px 0}
.svq{padding:6px 6px 0}
.svq>span{display:block;font-size:10px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--red);margin-top:6px}
.svq .svs{font-size:17px;margin:2px 0 4px}
'''
rep('.svln{position:absolute;left:0;top:0;width:100%;height:100%;pointer-events:none;overflow:visible}',
    '.svln{position:absolute;left:0;top:0;width:100%;height:100%;pointer-events:none;overflow:visible}' + css)

# ---- JS ----
js = r'''
/* ---------- Sehen · Fälle: Artikel, Präpositionen, Roller ---------- */
const SVA=[
[["der","das","die","die"],["den","das","die","die"],["dem","dem","der","den"],["des","des","der","der"]],
[["ein","ein","eine","–"],["einen","ein","eine","–"],["einem","einem","einer","–"],["eines","eines","einer","–"]],
[["kein","kein","keine","keine"],["keinen","kein","keine","keine"],["keinem","keinem","keiner","keinen"],["keines","keines","keiner","keiner"]]];
const SVAN=["der","ein","kein · mein"];
const SVAI=[
[["Merke","Only masculine changes: der → den"],["Trick","Plural = feminine, except DAT: den"],["Achtung","der = NOM m · DAT f · GEN f + pl"]],
[["Merke","Endings: -en, -em, -er, -es"],["Trick","Neuter NOM = AKK: ein Kind"],["Achtung","No plural: say keine / no article"]],
[["Merke","kein, mein, dein: same as ein"],["Trick","Plural too: keine, meine, deine"],["Achtung","DAT plural: keinen Kindern (+n)"]]];
const SVQ={
A:{n:"Akkusativ",c:"#f4dcd8",l:["bis","durch","für","gegen","ohne","um"],
 s:{bis:["Ich bleibe {bis} [nächsten Montag]."],durch:["Wir gehen {durch} [den Park]."],"für":["Ich kaufe Blumen {für} [meine Mutter]."],gegen:["Er läuft {gegen} [die Wand]."],ohne:["Sie geht {ohne} [ihren Hund]."],um:["Wir sitzen {um} [den Tisch]."]},
 i:[["Merke","Only masculine changes: den"],["Trick","FUDGEBO: für um durch gegen bis ohne"],["Achtung","entlang follows: den Fluss entlang"]]},
D:{n:"Dativ",c:"#d3def0",l:["ab","aus","außer","bei","gegenüber","mit","nach","seit","von","zu"],
 s:{ab:["{Ab} [dem ersten Mai] ist geschlossen."],aus:["Er kommt {aus} [dem Haus]."],"außer":["Alle kommen {außer} [dem Chef]."],bei:["Ich wohne {bei} [meiner Tante]."],"gegenüber":["Das Café liegt {gegenüber} [dem Bahnhof]."],mit:["Ich fahre {mit} [dem Bus]."],nach:["{Nach} [der Arbeit] gehe ich heim."],seit:["Ich lerne {seit} [einem Jahr] Deutsch."],von:["Das Buch ist {von} [der Lehrerin]."],zu:["Wir fahren {zu} [meinen Eltern]."]},
 i:[["Merke","aus bei mit nach seit von zu = DAT"],["Trick","Plural noun gets -n: mit den Kindern"],["Achtung","zu + dem = zum · bei + dem = beim"]]},
W:{n:"Wechsel",c:"linear-gradient(90deg,#f4dcd8 50%,#d3def0 50%)",l:["an","auf","hinter","in","neben","über","unter","vor","zwischen"],
 s:{an:["Das Bild hängt {an} [der Wand].","Ich hänge das Bild {an} [die Wand]."],auf:["Das Buch liegt {auf} [dem Tisch].","Ich lege das Buch {auf} [den Tisch]."],hinter:["Das Auto steht {hinter} [dem Haus].","Ich fahre das Auto {hinter} [das Haus]."],in:["Ich bin {in} [der Küche].","Ich gehe {in} [die Küche]."],neben:["Die Lampe steht {neben} [dem Sofa].","Ich stelle die Lampe {neben} [das Sofa]."],"über":["Die Lampe hängt {über} [dem Tisch].","Ich hänge die Lampe {über} [den Tisch]."],unter:["Die Katze liegt {unter} [dem Bett].","Die Katze kriecht {unter} [das Bett]."],vor:["Der Wagen steht {vor} [der Tür].","Ich stelle den Wagen {vor} [die Tür]."],zwischen:["Der Stuhl steht {zwischen} [den Fenstern].","Ich stelle den Stuhl {zwischen} [die Fenster]."]},
 i:[["Merke","Wo? → DAT · Wohin? → AKK"],["Trick","stehen, liegen, sitzen → Wo?"],["Achtung","stellen, legen, setzen → Wohin?"]]},
G:{n:"Genitiv",c:"#f5efcf",l:["anstatt","außerhalb","diesseits","innerhalb","jenseits","oberhalb","trotz","unterhalb","während","wegen"],
 s:{anstatt:["{Anstatt} [des Autos] nehme ich das Rad."],"außerhalb":["Er wohnt {außerhalb} [der Stadt]."],diesseits:["{Diesseits} [des Flusses] liegt das Dorf."],innerhalb:["{Innerhalb} [einer Woche] ist es fertig."],jenseits:["{Jenseits} [der Grenze] beginnt Ungarn."],oberhalb:["{Oberhalb} [des Dorfes] steht eine Kirche."],trotz:["{Trotz} [des Regens] gehen wir spazieren."],unterhalb:["{Unterhalb} [der Brücke] liegt ein Café."],"während":["{Während} [des Films] schläft er ein."],wegen:["{Wegen} [des Wetters] bleiben wir zu Hause."]},
 i:[["Merke","Formal and written: needs the Genitiv"],["Trick","Speech: wegen dem Wetter (DAT)"],["Achtung","masc. / neut. noun takes -(e)s"]]}};
function svSub(){return '<div class="svg" style="--n:4;margin-top:4px">'+[["s","Sätze"],["a","Artikel"],["p","Präp."],["r","Roller"]].map(x=>'<span role="button" tabindex="0" class="svb svo fr'+(SV.kp===x[0]?' on':'')+'" data-kp="'+x[0]+'">'+x[1]+'</span>').join('')+'</div>';}
function svFmt(t){return t.replace(/\{([^}]+)\}/g,(m,a)=>SVG_(a)).replace(/\[([^\]]+)\]/g,(m,a)=>SVY_(a));}
function svInfoH(t,fill,rows){return '<div class="svb svti" style="background:'+fill+'">'+esc(t)+'</div>'+rows.map(r=>'<div class="svr"><span>'+r[0]+'</span><span>'+esc(r[1])+'</span></div>').join('');}
function svTiles(g){const used=g.map(r=>r.map(()=>0)),T=[];
  for(let r=0;r<4;r++)for(let c=0;c<4;c++){if(used[r][c])continue;const w=g[r][c];let c2=c,r2=r;
    while(c2+1<4&&!used[r][c2+1]&&g[r][c2+1]===w)c2++;
    outer:while(r2+1<4){for(let k=c;k<=c2;k++)if(used[r2+1][k]||g[r2+1][k]!==w)break outer;r2++;}
    for(let i=r;i<=r2;i++)for(let k=c;k<=c2;k++)used[i][k]=1;T.push({w,r,c,r2,c2,a:(r2-r+1)*(c2-c+1)});}
  return T;}
function svAdj(a,b){const ro=a.r<=b.r2&&b.r<=a.r2,co=a.c<=b.c2&&b.c<=a.c2;return (ro&&(a.c2+1===b.c||b.c2+1===a.c))||(co&&(a.r2+1===b.r||b.r2+1===a.r));}
function svArtH(){const t=SV.at,g=SVA[t],tl=svTiles(g),fl=SVCFG.k.fills,cs=["NOM","AKK","DAT","GEN"];
  let h='<div class="svg" style="--n:3">'+SVAN.map((n,i)=>'<span role="button" tabindex="0" class="svb svo fr'+(t===i?' on':'')+'" data-at="'+i+'">'+n+'</span>').join('')+'</div><div style="height:6px"></div><div class="sag">';
  h+=["MASK","NEUT","FEM","PLUR"].map((x,c)=>'<span class="svb svl cc" style="grid-row:1;grid-column:'+(c+2)+'">'+x+'</span>').join('');
  h+=cs.map((x,r)=>'<span class="svb svl" style="grid-row:'+(r+2)+';grid-column:1;background:'+fl[r]+'">'+x+'</span>').join('');
  tl.forEach((q,i)=>{let top=q.r===0,left=q.c===0;
    if(q.r>0)for(let k=q.c;k<=q.c2;k++)if(g[q.r-1][k]!==q.w)top=true;
    if(q.c>0)for(let k=q.r;k<=q.r2;k++)if(g[k][q.c-1]!==q.w)left=true;
    const lay=[];if(top)lay.push("var(--df) left top/100% 1px no-repeat");if(left)lay.push("var(--dfv) left top/1px 100% no-repeat");
    const lab=!tl.some((u,j)=>j!==i&&u.w===q.w&&svAdj(q,u)&&(u.a>q.a||(u.a===q.a&&j<i))),dash=q.w==="–";
    h+='<span'+(dash?' class="sat nn"':' role="button" tabindex="0" class="sat'+(q.w.length>5?' lg':'')+(q.w===SV.aw?' on':'')+'" data-w="'+q.w+'"')+' style="grid-row:'+(q.r+2)+'/span '+(q.r2-q.r+1)+';grid-column:'+(q.c+2)+'/span '+(q.c2-q.c+1)+';background:'+(lay.join(",")||"none")+'">'+(lab?q.w:"")+'</span>';});
  return h+'</div><div class="svi" id="svi">'+svInfoH(["Bestimmter Artikel","Unbestimmter Artikel","kein · mein · dein"][t],"#e6e6e3",SVAI[t])+'</div>';}
function svPrepH(){const chip=(k,w)=>'<span role="button" tabindex="0" class="svb svk fr svw" data-g="'+k+'" data-w="'+w+'">'+w+'</span>';
  let h='<div class="svg" style="--n:3">'+[["A","Akkusativ"],["W","Wechsel"],["D","Dativ"]].map(x=>'<span class="svb svbn" style="background:'+SVQ[x[0]].c+'">'+x[1]+'</span>').join('')+'</div><div class="svg spc" style="--n:3;margin-top:3px">';
  ["A","W","D"].forEach(k=>{h+='<div class="spcol">'+SVQ[k].l.map(w=>chip(k,w)).join('')+'</div>';});
  return h+'</div><div class="svg" style="--n:1;margin-top:8px"><span class="svb svbn" style="background:'+SVQ.G.c+'">Genitiv</span></div><div class="svg" style="--n:4;margin-top:3px">'+SVQ.G.l.map(w=>chip("G",w)).join('')+'</div><div class="svx" id="svx"></div>';}
function svRollH(){const R=SV.rl,q=SVQ[R.g];
  let h='<div class="svg" style="--n:4">'+[["A","AKK"],["D","DAT"],["W","Wechsel"],["G","GEN"]].map(x=>'<span role="button" tabindex="0" class="svb svo fr'+(R.g===x[0]?' on':'')+'" data-rg="'+x[0]+'"'+(R.g===x[0]?' style="background:'+SVQ[x[0]].c+'"':'')+'>'+x[1]+'</span>').join('')+'</div>';
  h+=R.g==="W"?'<div class="svg" id="svrw" style="--n:2;margin-top:3px">'+["Wo? · Dativ","Wohin? · Akkusativ"].map((x,i)=>'<span role="button" tabindex="0" class="svb svo fr'+(R.wo===i?' on':'')+'" data-rw="'+i+'"'+(R.wo===i?' style="background:'+(i?"#f4dcd8":"#d3def0")+'"':'')+'>'+x+'</span>').join('')+'</div>'
    :'<div class="svg" style="--n:1;margin-top:3px"><span class="svb svbn" style="background:'+q.c+'">immer '+q.n+'</span></div>';
  h+='<div class="svg" id="svc" style="--n:5;margin-top:8px">'+q.l.map((w,i)=>'<span role="button" tabindex="0" class="svb svk fr svw" data-i="'+i+'">'+w+'</span>').join('')+'</div>';
  return h+'<div class="svt" id="svt"></div><div class="svi" id="svi"></div>';}
function renderSehenX(){const th=$("theo"),kp=SV.kp;
  let h='<div class="sv" id="sv"><div class="svg" style="--n:2"><span role="button" tabindex="0" class="svb svo fr" data-tab="t">Zeiten</span><span role="button" tabindex="0" class="svb svo fr on" data-tab="k">Fälle</span></div>'+svSub()+'<div style="height:6px"></div>';
  h+=kp==="a"?svArtH():kp==="p"?svPrepH():svRollH();
  h+='<p class="svh">'+(kp==="a"?"Wort antippen · gleiche Formen leuchten":kp==="p"?"Wort antippen":"wischen · Wort antippen")+'</p></div>';
  th.innerHTML=h;const root=$("sv");let pg=()=>false;
  if(kp==="a"){pg=b=>{if(b.dataset.at!==undefined){SV.at=+b.dataset.at;const g=SVA[SV.at];if(!g.some(r=>r.includes(SV.aw)))SV.aw=g[0][0];renderSehenX();return true;}
    if(b.dataset.w){SV.aw=b.dataset.w;root.querySelectorAll(".sat").forEach(x=>x.classList.toggle("on",x.dataset.w===SV.aw));return true;}return false;};}
  if(kp==="p"){const fill=()=>{const P=SV.pp,q=SVQ[P.g],s=q.s[P.w];let x='<div class="svb svti" style="background:'+q.c+'">'+esc(P.w)+' + '+q.n+'</div><div class="svq">';
      x+=P.g==="W"?'<span>Wo? · Dativ</span><p class="svs">'+svFmt(s[0])+'</p><span>Wohin? · Akkusativ</span><p class="svs">'+svFmt(s[1])+'</p>':'<p class="svs">'+svFmt(s[0])+'</p>';
      $("svx").innerHTML=x+'</div>';
      root.querySelectorAll(".svw").forEach(c=>{const on=c.dataset.g===P.g&&c.dataset.w===P.w;c.classList.toggle("on",on);c.style.background=on?SVQ[c.dataset.g].c:"";});};
    fill();pg=b=>{if(b.dataset.w&&b.dataset.g){SV.pp={g:b.dataset.g,w:b.dataset.w};fill();return true;}return false;};}
  if(kp==="r"){const R=SV.rl,q=SVQ[R.g],L=q.l,trk=$("svt"),chips=$("svc"),info=$("svi");if(R.i>=L.length)R.i=0;
    const cw=()=>{const c=trk.querySelector(".svcol");return c?c.offsetWidth:1;};
    const sent=w=>svFmt(R.g==="W"?q.s[w][R.wo]:q.s[w][0]);
    const marks=i=>{R.i=i;trk.querySelectorAll(".svcol").forEach((c,k)=>c.classList.toggle("on",k===i));
      const fill=R.g==="W"?(R.wo?"#f4dcd8":"#d3def0"):q.c,cn=R.g==="W"?(R.wo?"Akkusativ":"Dativ"):q.n;
      chips.querySelectorAll(".svk").forEach(c=>{const on=+c.dataset.i===i;c.classList.toggle("on",on);c.style.background=on?fill:"";});
      info.innerHTML=svInfoH(L[i]+" + "+cn,fill,q.i);};
    const cols=()=>{trk.innerHTML='<div class="svp"></div>'+L.map(w=>'<div class="svcol"><p class="svs">'+sent(w)+'</p></div>').join('')+'<div class="svp"></div>';marks(R.i);};
    const go=(i,sm)=>trk.scrollTo({left:i*cw(),behavior:sm?"smooth":"auto"});
    cols();let raf=0;
    trk.addEventListener("scroll",()=>{cancelAnimationFrame(raf);raf=requestAnimationFrame(()=>{const i=Math.max(0,Math.min(L.length-1,Math.round(trk.scrollLeft/cw())));if(i!==R.i)marks(i);});});
    pg=b=>{if(b.dataset.rg){R.g=b.dataset.rg;R.i=0;renderSehenX();return true;}
      if(b.dataset.rw!==undefined){R.wo=+b.dataset.rw;root.querySelectorAll("[data-rw]").forEach(x=>{const on=+x.dataset.rw===R.wo;x.classList.toggle("on",on);x.style.background=on?(+x.dataset.rw?"#f4dcd8":"#d3def0"):"";});cols();go(R.i,false);return true;}
      if(b.dataset.i!==undefined){const i=+b.dataset.i;marks(i);go(i,true);return true;}return false;};
    requestAnimationFrame(()=>requestAnimationFrame(()=>go(R.i,false)));}
  root.addEventListener("click",e=>{const b=e.target.closest("[role=button]");if(!b||!root.contains(b))return;
    if(b.dataset.kp){SV.kp=b.dataset.kp;renderSehen();return;}
    if(b.dataset.tab){SV.tab=b.dataset.tab;renderSehen();return;}
    pg(b);});
  root.addEventListener("keydown",e=>{if((e.key==="Enter"||e.key===" ")&&e.target.getAttribute("role")==="button"){e.preventDefault();e.target.click();}});}
'''
rep('document.querySelectorAll("#sehb .sehk")', js + 'document.querySelectorAll("#sehb .sehk")')

# ---- version ----
m = re.search(r'name="app-version" content="(\d{4}-\d\d-\d\d)([a-z]?)"', s)
s = s.replace(m.group(0), 'name="app-version" content="%s%s"' % (m.group(1), chr(ord(m.group(2) or "`") + 1)))
open(p, "w", encoding="utf-8").write(s)
print("ok")
