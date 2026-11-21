/* ---------- Präpositionen neu (Testfassung praep2.html): Satz als Regler [praep-neu] ---------- */
const PNEW=(function(){
const U=SNEW.U,ART=U.ART,CC=U.CC,CAP=U.CAP,G=U.G,mix=U.mix;
const GN=["M","N","F","PL"];
const PG=[
 {n:"Akkusativ",c:1,fill:"#f0be83",m:"für, durch, gegen, ohne, um, bis: always Akkusativ. Only the masculine changes.",p:[
  {w:"für",f:["Das Geschenk ist [für] [NP]."],n:["Lehrer","Kind","Freundin","Kinder"]},
  {w:"durch",f:["Wir gehen [durch] [NP]."],n:["Park","Dorf","Stadt","Straßen"]},
  {w:"ohne",f:["Er geht [ohne] [NP] aus dem Haus."],n:["Hund","Kind","Tasche","Schlüssel"]}]},
 {n:"Dativ",c:2,fill:"#c3ccfc",m:"aus, bei, mit, nach, seit, von, zu: always Dativ. The plural noun gets -n.",p:[
  {w:"mit",f:["Ich fahre [mit] [NP]."],n:["Bus","Auto","Bahn","Freunde"]},
  {w:"bei",f:["Ich bin [bei] [NP]."],n:["Arzt","Kind","Tante","Eltern"]},
  {w:"zu",f:["Wir gehen [zu] [NP]."],n:["Arzt","Haus","Schule","Freunde"]}]},
 {n:"Wechsel",c:-1,fill:"linear-gradient(90deg,#f0be83 50%,#c3ccfc 50%)",m:"Wo? → Dativ · Wohin? → Akkusativ. Nine prepositions: an, auf, in, …",p:[
  {w:"in",f:["Er ist [in] [NP].","Er geht [in] [NP]."],n:["Garten","Haus","Stadt","Räume"]},
  {w:"auf",f:["Das Buch liegt [auf] [NP].","Ich lege das Buch [auf] [NP]."],n:["Tisch","Sofa","Bank","Stühle"]},
  {w:"an",f:["Das Bild hängt [an] [NP].","Ich hänge das Bild [an] [NP]."],n:["Schrank","Fenster","Wand","Wände"]}]},
 {n:"Genitiv",c:3,fill:"#c4a6ee",m:"wegen, trotz, während: formal and written. A masc. / neut. noun takes -(e)s.",p:[
  {w:"wegen",f:["[Wegen] [NP] bleiben wir zu Hause."],n:["Regens","Wetters","Krankheit","Kinder"]},
  {w:"trotz",f:["[Trotz] [NP] gehen wir spazieren."],n:["Lärms","Wetters","Kälte","Probleme"]},
  {w:"während",f:["[Während] [NP] schläft er ein."],n:["Films","Spiels","Sitzung","Ferien"]}]}];
const P={g:1,i:0,gd:0,wo:0,rat:false,ans:null,opts:[]};
const dpl=w=>/[ns]$/.test(w)?w:w+"n";
const cur=()=>{const g=PG[P.g],pr=g.p[P.i],c=g.c<0?(P.wo?1:2):g.c;return{g,pr,c};};
function np(c,gd,hide){const {pr}=cur();let w=pr.n[gd];if(c==2&&gd==3)w=dpl(w);const a=hide?"____":ART[c][gd];return{art:ART[c][gd],txt:a+" "+w};}
function sent(hide){const {g,pr,c}=cur(),f=pr.f[g.c<0?(P.wo?1:0):0],n=np(c,P.gd,hide);
 return f.replace(/\[NP\]/,'<span class="np" style="background:'+CC()[c]+'">'+n.txt+'</span>').replace(/\[([^\]]+)\]/,(m,a)=>G(a));}
function newOpts(){const {c}=cur(),k=ART[c][P.gd],o=[...new Set(ART.map(r=>r[P.gd]))].filter(x=>x!=k);P.opts=mix([k,...mix(o).slice(0,2)]);P.ans=null;}
function optsH(){if(!P.rat)return"";const {c}=cur(),k=ART[c][P.gd];
 return '<div class="svg" style="--n:3">'+P.opts.map(o=>{let cl="svb svo fr sno";if(P.ans!=null){if(o==k)cl+=" ok";else if(o==P.ans)cl+=" bad";}
  return '<span role="button" tabindex="0" class="'+cl+'" data-a="o:'+o+'">'+(P.ans!=null&&o==k?"✓ ":"")+(P.ans!=null&&o==P.ans&&o!=k?"✗ ":"")+o+'</span>';}).join("")+'</div>';}
function html(){
 const {g,pr,c}=cur(),hide=P.rat&&P.ans==null;
 let h='<div class="svg" style="--n:4">'+PG.map((x,i)=>'<span role="button" tabindex="0" class="svb svo fr'+(P.g==i?' on':'')+'" data-a="g:'+i+'"'+(P.g==i?' style="background:'+x.fill+'"':'')+'>'+x.n+'</span>').join("")+'</div>';
 h+='<div class="svg" style="--n:3">'+g.p.map((x,i)=>'<span role="button" tabindex="0" class="svb svk fr'+(P.i==i?' on':'')+'" data-a="i:'+i+'"'+(P.i==i?' style="background:'+g.fill+'"':'')+'>'+x.w+'</span>').join("")+'</div>';
 if(g.c<0)h+='<div class="svg" style="--n:2"><span role="button" tabindex="0" class="svb svo fr'+(!P.wo?' on':'')+'" data-a="w:0"'+(!P.wo?' style="background:#c3ccfc"':'')+'>Wo? · Dativ</span><span role="button" tabindex="0" class="svb svo fr'+(P.wo?' on':'')+'" data-a="w:1"'+(P.wo?' style="background:#f0be83"':'')+'>Wohin? · Akkusativ</span></div>';
 h+=U.hero({main:sent(hide),ns:""},0,true,true)+optsH();
 h+='<div class="snm"><span class="snl2">Merke</span> '+g.m+'</div>';
 h+=U.table(c,P.gd);
 h+='<div class="svg" style="--n:3;margin-top:6px"><span role="button" tabindex="0" class="svb svo fr'+(P.rat?' on':'')+'" data-a="rat"'+(P.rat?' style="background:#cdff3e"':'')+'>Raten</span><span class="svb" style="grid-column:span 2;text-transform:none;letter-spacing:0;color:#999">Satz wischen: M · N · F · PL</span></div>';
 return '<div class="sv sn" id="sv">'+h+'</div>';}
function step(d){P.gd=(P.gd+d+4)%4;newOpts();draw();}
function draw(){const old=document.getElementById("sv"),box=document.createElement("div");box.innerHTML=html();const el=box.firstChild;
 if(old)old.replaceWith(el);else $("theo").prepend(el);
 svGlue();requestAnimationFrame(svGlue);let x0=null;
 el.addEventListener("click",e=>{const b=e.target.closest("[role=button]");if(!b||!el.contains(b))return;const a=b.dataset.a;if(!a)return;
  if(a.startsWith("st:"))step(+a.slice(3));
  else if(a.startsWith("g:")){P.g=+a.slice(2);P.i=0;newOpts();draw();}
  else if(a.startsWith("i:")){P.i=+a.slice(2);newOpts();draw();}
  else if(a.startsWith("w:")){P.wo=+a.slice(2);newOpts();draw();}
  else if(a.startsWith("cell:")){P.gd=+a.split(":")[2];newOpts();draw();}
  else if(a=="rat"){P.rat=!P.rat;newOpts();draw();}
  else if(a.startsWith("o:")){if(P.ans==null){P.ans=a.slice(2);draw();}}});
 el.addEventListener("keydown",e=>{if((e.key==="Enter"||e.key===" ")&&e.target.getAttribute("role")==="button"){e.preventDefault();e.target.click();}});
 el.addEventListener("pointerdown",e=>{if(e.target.closest(".snh")&&!e.target.closest(".svar"))x0=e.clientX;});
 el.addEventListener("pointerup",e=>{if(x0!=null){const d=e.clientX-x0;x0=null;if(Math.abs(d)>40)step(d<0?1:-1);}});}
function mount(){if(!P.opts.length)newOpts();draw();}
return{mount};})();
const _tgP=theoGallery;theoGallery=function(){_tgP();if(T==="pfall")PNEW.mount();};
