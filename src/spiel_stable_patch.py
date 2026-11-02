# DOCH!: Spiel/Test springt nicht mehr und hat keinen Leerraum zwischen Titel und Frage. Idempotent. 02.11.2026
# 1) Fehler: classList.toggle("typ",undefined) schaltet um statt zu setzen -> Panel sprang zwischen 226 und 316 px.
# 2) Buehne nur so hoch wie ihr Inhalt (pro Runde gemessen), Frage direkt darunter, Datenzeile unten.
# 3) Pro Runde werden die Hoehen von Legende, Frage (auch mit eingesetzter Loesung) und Antworten (auch mit Haekchen)
#    vorab gemessen und reserviert. Die Erklaerung darf wachsen, weil die Datenzeile unten verankert ist.
# 4) "Neu starten" und "Ergaenzen" stehen in einer Zeile; der E-Pfeil bleibt auch beim letzten Schritt ("Ergebnis").
# 5) Reicht der Platz nicht, wird der Inhalt der Buehne verkleinert (nicht unter 70 %).
import re,sys
s=open('index.html',encoding='utf-8').read()

a='classList.toggle("typ",typed)'
if a in s:
    assert s.count(a)==1
    s=s.replace(a,'classList.toggle("typ",!!typed)',1)

r='/^Weiter/.test(w.textContent)'
if r in s:
    assert s.count(r)==1
    s=s.replace(r,'/^(Weiter|Ergebnis)/.test(w.textContent)',1)

if 'id="spiel-css"' not in s:
    css='''<style id="spiel-css">
/* Spiel: Buehne so hoch wie ihr Inhalt, Frage direkt darunter, nichts springt */
.app[data-mode="game"] .stagew{flex:0 0 auto;min-height:0}
.app[data-mode="game"] .stage{flex:none;height:var(--sh,150px);min-height:84px;gap:8px}
.app[data-mode="game"] .stage.meas{height:auto;min-height:0}
.app[data-mode="game"] .stage>*{zoom:var(--sk,1)}
.app[data-mode="game"] .stage>.pict{padding:0 48px}
.app[data-mode="game"] .stage>:not(.pict){padding-right:48px;box-sizing:border-box}
.app[data-mode="game"] .stage .noun .star{right:52px}
.app[data-mode="game"] .panel,.app[data-mode="game"].typ .panel{flex:1 1 auto;height:auto;min-height:0;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:minmax(0,1fr) auto;gap:6px}
.app[data-mode="game"] .panel>.card{grid-column:1/-1;min-height:0}
.app[data-mode="game"] .panel>.btns{display:contents}
.app[data-mode="game"] .lg{min-height:var(--hl,0)}
.app[data-mode="game"] #panel #tx{min-height:var(--hx,0)}
.app[data-mode="game"] #panel .opts{min-height:var(--ho,0)}
.app[data-mode="game"] #panel .card.df #cardbody{padding-bottom:8px}
.app[data-mode="game"] #panel .card.df .top{margin-top:auto}
</style>
'''
    assert s.count('</head>')==1
    s=s.replace('</head>',css+'</head>',1)

if 'id="spiel-js"' not in s:
    js='''<script id="spiel-js">/* Spiel: misst pro Runde alle Hoehen vorab und reserviert sie, damit nichts springt */
(function(){const $=id=>document.getElementById(id),app=document.querySelector(".app");
if(typeof mcRender!=="function"||!app)return;
const base=mcRender,VARS=["--hx","--ho","--hl","--sh","--sk"],H=e=>e.getBoundingClientRect().height,P=(k,v)=>app.style.setProperty(k,v);
function lock(){const st=$("stage"),cb=$("cardbody"),tx=$("tx"),gt=$("gt"),nf=$("nf"),lg=$("lg"),card=document.querySelector("#panel .card"),top=card&&card.querySelector(".top");
 if(!MC||!MC.list||!st||!cb||!tx||!gt||!nf||!lg||!card)return;
 const cur=MC.list[MC.i];if(!cur)return;MC.lw=innerWidth;VARS.forEach(v=>app.style.removeProperty(v));
 const sTx=tx.innerHTML,sGt=gt.textContent,sNf=nf.innerHTML,sLg=lg.innerHTML;let hx=0,ho=0,hg=0,hn=0,hl=0,hs=0;st.classList.add("meas");
 try{MC.list.forEach(q=>{
  const t0=esc(q.s).replace(/\\[(.+?)\\]/,'<mark class="fm">$1</mark>');
  tx.innerHTML=t0.replace("___",'<span class="gap">&nbsp;</span>');hx=Math.max(hx,H(tx));
  tx.innerHTML=t0.replace("___",'<span class="gap">'+esc(q.o[q.c])+'</span>');hx=Math.max(hx,H(tx));
  if(!canType(q)){const t=document.createElement("div");t.className="opts"+(q.o.some(w=>w.length>12)?" long":q.o.length===3?" three":"");t.style.visibility="hidden";
   t.innerHTML=q.o.map(w=>'<button class="opt ok">'+esc(w)+'</button>').join("");cb.appendChild(t);ho=Math.max(ho,H(t));cb.removeChild(t);}
  gt.textContent="Nicht ganz. "+q.why;hg=Math.max(hg,H(gt));
  if(baseOf(q)&&q.t!=="art"){nf.innerHTML="Grundform: <b>x</b>";hn=Math.max(hn,H(nf));}
  if(q.t==="prep")prLegend(false);else lg.innerHTML=LG[q.t]||(GT[q.t]&&GT[q.t].lg)||"";hl=Math.max(hl,H(lg));
  [false,true].forEach(rev=>{try{(STAGE[q.t]||gStage)(q,rev);hs=Math.max(hs,H(st));}catch(e){}});});}catch(e){}
 tx.innerHTML=sTx;gt.textContent=sGt;nf.innerHTML=sNf;
 if(cur.t==="prep")prLegend(false);else lg.innerHTML=sLg;
 try{(STAGE[cur.t]||gStage)(cur,false);if(MC.done)(STAGE[cur.t]||gStage)(cur,true);}catch(e){}
 st.classList.remove("meas");
 const cap=Math.max(150,Math.round(innerHeight*.4));hs=Math.max(84,Math.min(Math.ceil(hs)+4,cap));
 [["--hx",hx],["--ho",ho],["--hl",hl]].forEach(a=>P(a[0],(Math.ceil(a[1]*100)/100)+"px"));P("--sh",hs+"px");P("--sk","1");
 /* Platz fuer die Erklaerung (hoechstens drei Zeilen) und Grundform: sonst wird der Inhalt der Buehne verkleinert */
 const need=Math.min(hg+hn,76),sh0=hs;
 for(let n=0;n<3;n++){const used=H(cb)+(top?H(top):0)+16,free=card.clientHeight-used+(sGt?0:0)-H(gt)-H(nf),d=need-free;
  if(d<=1)break;const nh=Math.max(Math.round(sh0*.7),hs-Math.ceil(d));if(nh>=hs)break;hs=nh;P("--sh",hs+"px");P("--sk",(hs/sh0).toFixed(3));}}
mcRender=function(){base.apply(this,arguments);try{if(MC&&MC.lw!==innerWidth)lock();}catch(e){}};
let rt=0;addEventListener("resize",()=>{clearTimeout(rt);rt=setTimeout(()=>{try{if(MC&&app.dataset.mode==="game"&&MC.lw!==innerWidth)lock();}catch(e){}},200);});})();
</script>
'''
    k='<script id="upd-js">'
    assert s.count(k)==1
    s=s.replace(k,js+k,1)

if '--noversion' not in sys.argv:
    s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda mm:mm.group(1)+'2026-11-02c'+mm.group(3),s,count=1)
open('index.html','w',encoding='utf-8').write(s)
