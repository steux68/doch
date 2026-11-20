/* ---------- Sehen neu (2026-11-21): der Satz ist der Regler [sehen-neu] ---------- */
const SNEW=(function(){
const st={p:0,zl:0,v:0,fl:0,fm:"bsp",rat:false,ans:null,r:"B",vb:0,g:0,pk:[{i:0,pl:0},{i:0,pl:0},{i:0,pl:0}],opts:[]};
const PR=["ich","du","er","wir","ihr","sie"],CAP=s=>s.charAt(0).toUpperCase()+s.slice(1);
const HAB=["habe","hast","hat","haben","habt","haben"],HATT=["hatte","hattest","hatte","hatten","hattet","hatten"],WERD=["werde","wirst","wird","werden","werdet","werden"],WILL=["will","willst","will","wollen","wollt","wollen"],SEIN=["bin","bist","ist","sind","seid","sind"],WAR=["war","warst","war","waren","wart","waren"];
const PE=["e","st","t","en","t","en"];
const VZ=[
 {inf:"lernen",s:"lern",ps:"lern",pte:["te","test","te","ten","tet","ten"],pp:"gelernt",a:HAB,a0:HATT,fi:"haben",ns:"die Prüfung bestehen",nv:WILL},
 {inf:"gehen",s:"geh",ps:"ging",pte:["","st","","en","t","en"],pp:"gegangen",a:SEIN,a0:WAR,fi:"sein",ns:"müde",nv:SEIN}];
const G=x=>'<span class="g">'+x+'</span>',Y=x=>'<span class="y">'+x+'</span>';
const BLANK='<span class="g" style="padding:0 22px">&nbsp;</span>';
const ARL='<svg class="ar" viewBox="-12 -12 24 24" aria-hidden="true"><path class="dt" transform="rotate(180)" d="M5.4 0L-4.6 -4.9L-2.2 0L-4.6 4.9Z"/></svg>',ARR='<svg class="ar" viewBox="-12 -12 24 24" aria-hidden="true"><path class="dt" d="M5.4 0L-4.6 -4.9L-2.2 0L-4.6 4.9Z"/></svg>';
/* ----- Zeiten ----- */
function form(v,t,p){
 if(t==3)return{st:v.s,en:PE[p],rest:""};
 if(t==1)return{st:v.ps,en:v.pte[p],rest:""};
 if(t==0)return{fin:v.a0[p],rest:v.pp};
 if(t==2)return{fin:v.a[p],rest:v.pp};
 if(t==4)return{fin:WERD[p],rest:v.inf};
 return{fin:WERD[p],rest:v.pp+" "+v.fi};}
const plain=f=>(f.st!==undefined?f.st+f.en:f.fin)+(f.rest&&f.st===undefined?" "+f.rest:"");
function finH(f,cap){let a=f.st!==undefined?f.st:f.fin;if(cap)a=CAP(a);return f.st!==undefined?a+(f.en?'<span class="end">'+f.en+'</span>':''):a;}
function zSent(t,p,hide){
 const v=VZ[st.v],f=form(v,t,p),L=st.zl;let main,ns="";
 if(L==2){main=(hide?BLANK:G(finH(f,true))+(f.st===undefined?"":""))+' '+PR[p]+(!hide&&f.st===undefined?' '+Y(f.rest):'')+'?';}
 else{const vg=hide?BLANK:(f.st!==undefined?G(finH(f,false)):G(f.fin)+' '+Y(f.rest));main=CAP(PR[p])+' '+vg+(L==1?',':'.');}
 if(L==1)ns='weil '+PR[p]+' '+v.ns+' <span class="vf">'+v.nv[p]+'</span>.';
 return{main,ns};}
const FILL=()=>SVCFG.t.fills;
const mix=a=>a.map(x=>[Math.random(),x]).sort((a,b)=>a[0]-b[0]).map(x=>x[1]);
function newOpts(){
 if(SV.tab==="t"){const v=VZ[st.v],t=SV.cur.t,c=plain(form(v,t,st.p));const o=[0,1,2,3,4,5].filter(k=>k!=t).map(k=>plain(form(v,k,st.p))).filter(x=>x!=c);st.opts=mix([c,...mix([...new Set(o)]).slice(0,2)]);}
 else{const c=SVA[0][SV.cur.k][st.g],o=[...new Set(SVA[0].map(r=>r[st.g]))].filter(x=>x!=c);st.opts=mix([c,...mix(o).slice(0,2)]);}
 st.ans=null;}
/* ----- Fälle ----- */
const CN=["NOM","AKK","DAT","GEN"],CNn=["Nom.","Akk.","Dat.","Gen."],GN=["M","N","F","PL"],GL=["der Mann","das Kind","die Frau","Plural"];
const CC=()=>SVCFG.k.fills;
const ART=[["der","das","die","die"],["den","das","die","die"],["dem","dem","der","den"],["des","des","der","der"]];
const NO=[["Mann","Mann","Mann","Mannes"],["Kind","Kind","Kind","Kindes"],["Frau","Frau","Frau","Frau"],["Kinder","Kinder","Kindern","Kinder"]];
const GRP=[[1,2,3,3],[4,2,3,3],[5,5,6,7],[8,8,6,6]];
const LAB={1:[0,0,1,1],2:[0,1,2,1],3:[0,2,2,2],4:[1,0,1,1],5:[2,0,1,2],6:[3,2,1,2],7:[2,3,1,1],8:[3,0,1,2]};
const QW=["wer / was?","wen / was?","wem?","wessen?"];
function fSent(c,g,hide){
 const A=ART[c][g],Nn=NO[g][c],a=hide?"____":(c==0?CAP(A):A);
 const np='<span class="np" style="background:'+CC()[c]+'">'+a+' '+Nn+'</span>';
 const pl=g==3,main=[np+' '+(pl?'schlafen':'schläft'),'Ich sehe '+np,'Ich helfe '+np,'Das ist das Auto '+np][c];
 const ns=[ 'weil '+['er','es','sie','sie'][g]+' müde <span class="vf">'+(pl?'sind':'ist')+'</span>.','obwohl es dunkel <span class="vf">ist</span>.','weil es <span class="vf">regnet</span>.','das ich gestern gesehen <span class="vf">habe</span>.'][c];
 return st.fl?{main:main+',',ns}:{main:main+'.',ns:""};}
/* ----- Satz bauen: Nomen und Verben (eigene Formulierung, bitte prüfen) ----- */
const NN={
 mann:{g:0,s:"Mann",p:"Männer",d:"Männern"},lehrer:{g:0,s:"Lehrer",p:"Lehrer",d:"Lehrern"},frau:{g:2,s:"Frau",p:"Frauen",d:"Frauen"},freundin:{g:2,s:"Freundin",p:"Freundinnen",d:"Freundinnen"},kind:{g:1,s:"Kind",p:"Kinder",d:"Kindern"},mädchen:{g:1,s:"Mädchen",p:"Mädchen",d:"Mädchen"},
 apfel:{g:0,s:"Apfel",p:"Äpfel",d:"Äpfeln"},hund:{g:0,s:"Hund",p:"Hunde",d:"Hunden"},tasche:{g:2,s:"Tasche",p:"Taschen",d:"Taschen"},katze:{g:2,s:"Katze",p:"Katzen",d:"Katzen"},buch:{g:1,s:"Buch",p:"Bücher",d:"Büchern"},auto:{g:1,s:"Auto",p:"Autos",d:"Autos"},
 haus:{g:1,s:"Haus",p:"Häuser",d:"Häusern"},stadt:{g:2,s:"Stadt",p:"Städte",d:"Städten"},garten:{g:0,s:"Garten",p:"Gärten",d:"Gärten"},schule:{g:2,s:"Schule",p:"Schulen",d:"Schulen"},
 tisch:{g:0,s:"Tisch",p:"Tische",d:"Tischen"},stuhl:{g:0,s:"Stuhl",p:"Stühle",d:"Stühlen"},bett:{g:1,s:"Bett",p:"Betten",d:"Betten"},bank:{g:2,s:"Bank",p:"Bänke",d:"Bänken"}};
const PERS=["mann","lehrer","frau","freundin","kind","mädchen"],THING=["apfel","hund","tasche","katze","buch","auto"],PORT=["apfel","tasche","buch"],GIFT=["apfel","tasche","buch","auto"],LOC=["haus","stadt","garten","schule"],SURF=["tisch","stuhl","bett","bank"],ALL=PERS.concat(THING);
const who={c:0,p:PERS,w:"the one who does it"};
const VB=[
 {n:"sehen",gr:"Akkusativ",f:["sieht","sehen"],sl:[who,{c:1,p:ALL,w:"sehen takes Akkusativ"}],tip:"sehen, kaufen, finden: what is seen, bought or found is Akkusativ."},
 {n:"kaufen",gr:"Akkusativ",f:["kauft","kaufen"],sl:[who,{c:1,p:THING,w:"kaufen takes Akkusativ"}],tip:"What gets bought is always Akkusativ."},
 {n:"finden",gr:"Akkusativ",f:["findet","finden"],sl:[who,{c:1,p:ALL,w:"finden takes Akkusativ"}],tip:"Akkusativ: the thing or person that is found."},
 {n:"helfen",gr:"Dativ",f:["hilft","helfen"],sl:[who,{c:2,p:PERS,w:"helfen always takes Dativ"}],tip:"Dativ verbs to learn as a group: helfen, danken, antworten, gehören, gefallen."},
 {n:"danken",gr:"Dativ",f:["dankt","danken"],sl:[who,{c:2,p:PERS,w:"danken always takes Dativ"}],tip:"You thank someone: Dativ, never Akkusativ."},
 {n:"antworten",gr:"Dativ",f:["antwortet","antworten"],sl:[who,{c:2,p:PERS,w:"antworten takes Dativ"}],tip:"You answer someone: Dativ."},
 {n:"gehören",gr:"Dativ",f:["gehört","gehören"],sl:[{c:0,p:THING,w:"the thing that belongs"},{c:2,p:PERS,w:"gehören takes Dativ"}],tip:"Belonging to someone: the owner is Dativ."},
 {n:"gefallen",gr:"Dativ",f:["gefällt","gefallen"],sl:[{c:0,p:THING,w:"the thing that pleases"},{c:2,p:PERS,w:"gefallen takes Dativ"}],tip:"The thing is the subject, the person who likes it is Dativ."},
 {n:"geben",gr:"Dativ + Akkusativ",f:["gibt","geben"],sl:[who,{c:2,p:PERS,w:"the one who receives → Dativ"},{c:1,p:GIFT,w:"the thing given → Akkusativ"}],tip:"Two objects: person = Dativ, thing = Akkusativ. The person comes first."},
 {n:"zeigen",gr:"Dativ + Akkusativ",f:["zeigt","zeigen"],sl:[who,{c:2,p:PERS,w:"the one who is shown → Dativ"},{c:1,p:GIFT,w:"the thing shown → Akkusativ"}],tip:"Same pattern as geben."},
 {n:"schenken",gr:"Dativ + Akkusativ",f:["schenkt","schenken"],sl:[who,{c:2,p:PERS,w:"the one who gets the gift → Dativ"},{c:1,p:GIFT,w:"the gift → Akkusativ"}],tip:"Same pattern as geben."},
 {n:"legen",gr:"Wechsel: Wohin? (Akk)",f:["legt","legen"],sl:[who,{c:1,p:PORT,w:"the thing that is laid down → Akkusativ"},{c:1,p:SURF,pre:"auf",w:"auf + movement (Wohin?) → Akkusativ"}],tip:"legen = put down flat: Wohin? So Akkusativ."},
 {n:"stellen",gr:"Wechsel: Wohin? (Akk)",f:["stellt","stellen"],sl:[who,{c:1,p:PORT,w:"the thing that is put upright → Akkusativ"},{c:1,p:SURF,pre:"auf",w:"auf + movement (Wohin?) → Akkusativ"}],tip:"stellen = put upright: Wohin? So Akkusativ."},
 {n:"liegen",gr:"Wechsel: Wo? (Dat)",f:["liegt","liegen"],sl:[{c:0,p:PORT,w:"the thing that lies"},{c:2,p:SURF,pre:"auf",w:"auf + place (Wo?) → Dativ"}],tip:"liegen = lies there: Wo? So Dativ. Compare legen."},
 {n:"stehen",gr:"Wechsel: Wo? (Dat)",f:["steht","stehen"],sl:[{c:0,p:PORT,w:"the thing that stands"},{c:2,p:SURF,pre:"auf",w:"auf + place (Wo?) → Dativ"}],tip:"stehen = stands there: Wo? So Dativ. Compare stellen."},
 {n:"wohnen",gr:"Ort und Richtung",f:["wohnt","wohnen"],sl:[who,{c:2,p:LOC,pre:"in",w:"in + place (Wo?) → Dativ"}],tip:"No movement, just being somewhere: Dativ."},
 {n:"gehen",gr:"Ort und Richtung",f:["geht","gehen"],sl:[who,{c:1,p:LOC,pre:"in",w:"in + movement (Wohin?) → Akkusativ"}],tip:"Movement towards a place: Akkusativ."},
 {n:"warten",gr:"Feste Präposition",f:["wartet","warten"],sl:[who,{c:1,p:PERS,pre:"auf",w:"warten auf + Akkusativ"}],tip:"warten auf is a fixed pair, always with Akkusativ."},
 {n:"denken",gr:"Feste Präposition",f:["denkt","denken"],sl:[who,{c:1,p:PERS,pre:"an",w:"denken an + Akkusativ"}],tip:"denken an is a fixed pair, always with Akkusativ."},
 {n:"sprechen",gr:"Feste Präposition",f:["spricht","sprechen"],sl:[who,{c:2,p:PERS,pre:"mit",w:"mit always takes Dativ"}],tip:"mit is always Dativ, whatever the verb."},
 {n:"sein",gr:"Nominativ",f:["ist","sind"],sl:[who,{c:0,p:PERS,w:"after sein → Nominativ (not Akkusativ!)"}],tip:"sein, werden, bleiben: the same case before and after the verb."}];
function phrase(sl,k){
 const n=NN[sl.p[k.i]],g=k.pl?3:n.g,w=k.pl?(sl.c==2?n.d:n.p):n.s,a=ART[sl.c][g];
 if(sl.pre=="in"){
  if(sl.c==2)return{pre:"",txt:(g<2)?"im "+w:"in "+a+" "+w,g};
  return{pre:"",txt:(g==1)?"ins "+w:"in "+a+" "+w,g};}
 if(sl.pre)return{pre:sl.pre+" ",txt:a+" "+w,g};
 return{pre:"",txt:a+" "+w,g};}
const nomLabel=k=>ART[0][NN[k].g]+" "+NN[k].s;
function build(){
 const v=VB[st.vb],pl=!!st.pk[0].pl;let html="",rows=[];
 v.sl.forEach((sl,i)=>{const ph=phrase(sl,st.pk[i]);let t=ph.txt;if(i==0)t=CAP(t);
  const span=ph.pre+'<span class="np" style="background:'+CC()[sl.c]+'">'+t+'</span>';
  if(i==0)html+=span+' '+G(v.f[pl?1:0]);else html+=' '+span;
  rows.push({c:sl.c,g:ph.g,t:ph.pre+ph.txt,w:sl.w});});
 return{html:html+".",rows};}
/* ----- Bausteine ----- */
const seg=(labels,cur,key,fills)=>'<div class="svg" style="--n:'+labels.length+'">'+labels.map((l,i)=>'<span role="button" tabindex="0" class="svb svo fr'+(cur==i?' on':'')+'" data-a="'+key+':'+i+'"'+(cur==i&&fills?' style="background:'+fills[i]+'"':'')+'>'+l+'</span>').join('')+'</div>';
function hero(sent,off,canL,canR){
 return '<div class="snh"><span role="button" tabindex="0" class="svar l" data-a="st:-1" aria-label="Zurück"'+(canL?'':' data-off')+'>'+ARL+'</span><div class="sns">'+sent.main+'</div>'
  +(sent.ns?'<div class="snn">'+sent.ns+'</div><div class="snl">Nebensatz · Verb ans Ende</div>':'')
  +'<span role="button" tabindex="0" class="svar r" data-a="st:1" aria-label="Weiter"'+(canR?'':' data-off')+'>'+ARR+'</span></div>';}
function optsH(c){
 if(!st.rat)return"";
 return '<div class="svg" style="--n:3">'+st.opts.map(o=>{let cl="svb svo fr sno";if(st.ans!=null){if(o==c)cl+=" ok";else if(o==st.ans)cl+=" bad";}
  return '<span role="button" tabindex="0" class="'+cl+'" data-a="o:'+o+'">'+(st.ans!=null&&o==c?"✓ ":"")+(st.ans!=null&&o==st.ans&&o!=c?"✗ ":"")+o+'</span>';}).join('')+'</div>';}
function foot(){return '<div class="svg" style="--n:3;margin-top:6px"><span role="button" tabindex="0" class="svb svo fr'+(st.rat?' on':'')+'" data-a="rat"'+(st.rat?' style="background:#cdff3e"':'')+'>Raten</span><span class="svb" style="grid-column:span 2;text-transform:none;letter-spacing:0;color:#999">Satz wischen oder Pfeil</span></div>';}
function acc(x){
 const rows=[["B","Bildung",x.f],["G","Gebrauch",x.u],["S","Signale",x.s],["A","Achtung",x.a]];
 return rows.map(r=>'<div role="button" tabindex="0" class="svr" data-a="r:'+r[0]+'"><span>'+r[1]+'</span><span>'+(st.r==r[0]?esc(r[2]):'<span style="color:#aaa">+</span>')+'</span></div>').join('');}
function table(c,g){
 const ag=GRP[c][g];let h='<div class="snt"><span></span>'+GN.map((x,i)=>'<span class="tn'+(g==i?' on':'')+'">'+x+'</span>').join("");
 for(let r=0;r<4;r++){
  h+='<span class="tn'+(c==r?' on':'')+'" style="'+(c==r?'background:'+CC()[r]+';':'')+'">'+CN[r]+'</span>';
  for(let k=0;k<4;k++){
   const q=GRP[r][k],ln=[];
   if(r==0)ln.push("var(--df) left top/100% 1px no-repeat");if(k==0)ln.push("var(--dfv) left top/1px 100% no-repeat");
   if(k==3||GRP[r][k+1]!=q)ln.push("var(--dfv) right top/1px 100% no-repeat");
   if(r==3||GRP[r+1][k]!=q)ln.push("var(--df) left bottom/100% 1px no-repeat");
   const L=LAB[q];let lab="";
   if(L[0]==r&&L[1]==k)lab='<span class="tl" style="width:'+(L[3]*100)+'%;height:'+(L[2]*100)+'%">'+ART[r][k]+'</span>';
   h+='<span role="button" tabindex="0" class="tc'+(q==ag?(r==c&&k==g?' sel':' grp'):'')+'" data-a="cell:'+r+':'+k+'">'+lab+'<i style="background:'+ln.join(",")+'"></i></span>';}}
 return h+'</div>';}
/* ----- Seiten ----- */
function zH(){
 const t=SV.cur.t,hide=st.rat&&st.ans==null,s=zSent(t,st.p,hide),x=SVT[t],f=FILL();
 let h=seg(PR,st.p,"p");
 h+='<div class="svg svbd" style="--n:6">'+SVCFG.t.bands.map(b=>'<span class="svb" style="grid-column:span '+b[1]+';background:'+b[2]+'">'+b[0]+'</span>').join("")+'</div>';
 h+='<div class="svg" style="--n:6">'+SVCFG.t.chips.map((c,i)=>'<span role="button" tabindex="0" class="svb svk fr'+(t==i?' on':'')+'" data-a="t:'+i+'"'+(t==i?' style="background:'+f[i]+'"':'')+'>'+c+'</span>').join("")+'</div>';
 h+='<div style="height:6px"></div>';
 h+=seg(["kurz","+ Nebensatz","Frage"],st.zl,"zl");
 h+=seg(["lernen (haben)","gehen (sein)"],st.v,"v");
 h+=hero(s,0,t>0,t<5)+optsH(plain(form(VZ[st.v],t,st.p)));
 h+='<div class="svb svti" style="background:'+f[t]+'">'+esc(x.n)+'</div>'+acc(x)+foot();
 return h;}
function fH(){
 let h=svSub();
 h+='<div style="height:6px"></div>'+seg(["Beispiele","Satz bauen"],st.fm=="bsp"?0:1,"fm");
 if(st.fm=="bsp"){
  const c=SV.cur.k,g=st.g,hide=st.rat&&st.ans==null,x=SVKC[c];
  h+=seg(CNn,c,"c",CC())+seg(GL,g,"g",["#e4f7a0","#e4f7a0","#e4f7a0","#e4f7a0"]);
  h+=seg(["kurz","+ Nebensatz"],st.fl,"fl");
  h+=hero(fSent(c,g,hide),0,c>0,c<3)+optsH(ART[c][g]);
  h+='<div class="svb svti" style="background:'+CC()[c]+'">'+esc(x.n+" · "+x.q)+'</div>'+acc(x);
  h+=table(c,g)+foot();return h;}
 const v=VB[st.vb],b=build(),gr=[];
 VB.forEach((y,i)=>{let q=gr.find(z=>z.n==y.gr);if(!q){q={n:y.gr,it:[]};gr.push(q);}q.it.push([y.n,i]);});
 h+='<div class="snb snsel"><select id="snv" aria-label="Verb">'+gr.map(q=>'<optgroup label="'+q.n+'">'+q.it.map(y=>'<option value="'+y[1]+'"'+(y[1]==st.vb?' selected':'')+'>'+y[0]+'</option>').join("")+'</optgroup>').join("")+'</select></div>';
 v.sl.forEach((sl,i)=>{h+='<div class="snrow"><span class="svb snch" style="background:'+CC()[sl.c]+'">'+(sl.pre?sl.pre+' ':'')+CN[sl.c]+'</span><div class="snb snsel"><select data-sel="'+i+'" aria-label="'+CN[sl.c]+'">'+sl.p.map((k,j)=>'<option value="'+j+'"'+(st.pk[i].i==j?' selected':'')+'>'+nomLabel(k)+'</option>').join("")+'</select></div><span role="button" tabindex="0" class="snb snpl'+(st.pk[i].pl?' on':'')+'" data-a="pl:'+i+'">Pl</span></div>';});
 h+='<div class="sncard">'+b.html+'</div><div class="snm"><span class="snl2">Merke</span> '+esc(v.tip)+'</div>';
 const c=SV.cur.k;
 h+=table(c,st.g);
 h+=b.rows.map(r=>'<div role="button" tabindex="0" class="snr" data-a="np:'+r.c+':'+r.g+'"><div><span class="svb snch" style="background:'+CC()[r.c]+'">'+CN[r.c]+'</span> <b>'+r.t+'</b> <span class="snq">· '+QW[r.c]+'</span></div><div class="snw">'+esc(r.w)+'</div></div>').join("");
 return h+'<p class="svh">Every sentence is built from checked rules, so it is always correct.</p>';}
function step(d){
 if(SV.tab==="t")SV.cur.t=Math.max(0,Math.min(5,SV.cur.t+d));else SV.cur.k=Math.max(0,Math.min(3,SV.cur.k+d));
 newOpts();render();}
function render(){
 const th=$("theo");
 const top='<div class="svg" style="--n:2"><span role="button" tabindex="0" class="svb svo fr'+(SV.tab==="t"?' on':'')+'" data-tab="t">Zeiten</span><span role="button" tabindex="0" class="svb svo fr'+(SV.tab==="k"?' on':'')+'" data-tab="k">Fälle</span></div>';
 th.innerHTML='<div class="sv sn" id="sv">'+top+(SV.tab==="t"?'<div style="height:6px"></div>'+zH():fH())+'</div>';
 const root=$("sv");svGlue();requestAnimationFrame(svGlue);
 let x0=null;
 root.addEventListener("click",e=>{const b=e.target.closest("[role=button]");if(!b||!root.contains(b))return;
  if(b.dataset.tab){SV.tab=b.dataset.tab;SV.kp="s";st.rat=false;newOpts();render();return;}
  if(b.dataset.kp){SV.kp=b.dataset.kp;renderSehen();return;}
  const a=b.dataset.a;if(!a)return;
  if(a.startsWith("st:"))step(+a.slice(3));
  else if(a.startsWith("p:")){st.p=+a.slice(2);newOpts();render();}
  else if(a.startsWith("t:")){SV.cur.t=+a.slice(2);newOpts();render();}
  else if(a.startsWith("zl:")){st.zl=+a.slice(3);render();}
  else if(a.startsWith("v:")){st.v=+a.slice(2);newOpts();render();}
  else if(a.startsWith("fl:")){st.fl=+a.slice(3);render();}
  else if(a.startsWith("fm:")){st.fm=a.slice(3)=="0"?"bsp":"bau";st.rat=false;newOpts();render();}
  else if(a.startsWith("c:")){SV.cur.k=+a.slice(2);newOpts();render();}
  else if(a.startsWith("g:")){st.g=+a.slice(2);newOpts();render();}
  else if(a.startsWith("cell:")){const q=a.split(":");SV.cur.k=+q[1];st.g=+q[2];newOpts();render();}
  else if(a.startsWith("np:")){const q=a.split(":");SV.cur.k=+q[1];st.g=+q[2];render();}
  else if(a.startsWith("pl:")){const i=+a.slice(3);st.pk[i].pl=st.pk[i].pl?0:1;const sl=VB[st.vb].sl[i];SV.cur.k=sl.c;st.g=phrase(sl,st.pk[i]).g;render();}
  else if(a.startsWith("r:")){st.r=a[2];render();}
  else if(a=="rat"){st.rat=!st.rat;newOpts();render();}
  else if(a.startsWith("o:")){if(st.ans==null){st.ans=a.slice(2);render();}}});
 root.addEventListener("change",e=>{const t=e.target;
  if(t.id=="snv"){st.vb=+t.value;st.pk=[{i:0,pl:0},{i:0,pl:0},{i:0,pl:0}];const v=VB[st.vb],k=v.sl.length-1,sl=v.sl[k];SV.cur.k=sl.c;st.g=phrase(sl,st.pk[k]).g;render();}
  else if(t.dataset.sel!==undefined){const i=+t.dataset.sel;st.pk[i].i=+t.value;const sl=VB[st.vb].sl[i];SV.cur.k=sl.c;st.g=phrase(sl,st.pk[i]).g;render();}});
 root.addEventListener("keydown",e=>{if((e.key==="Enter"||e.key===" ")&&e.target.getAttribute("role")==="button"){e.preventDefault();e.target.click();}});
 root.addEventListener("pointerdown",e=>{if(e.target.closest(".snh")&&!e.target.closest(".svar"))x0=e.clientX;});
 root.addEventListener("pointerup",e=>{if(x0!=null){const d=e.clientX-x0;x0=null;if(Math.abs(d)>40)step(d<0?1:-1);}});}
function open(){if(!st.opts.length)newOpts();if(SV.tab==="k"&&(!st.g&&st.g!==0))st.g=0;render();}
return{render:open};})();
function renderSehen(){if(SV.tab==="k"&&SV.kp&&SV.kp!=="s")return renderSehenX();return SNEW.render();}
