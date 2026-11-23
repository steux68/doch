#!/usr/bin/env python3
"""Sehen neu 2 (2026-11-23): neues Layout für Zeiten und Fälle (Beispiele).
Streifen oben, Satz gross, Bildung-Zeile, Auswahlzeile mit Pull-downs (Satz/Form zeigt alle Möglichkeiten),
Gebrauch/Signale/Achtung offen, quadratische Artikel-Tabelle (38 px), Raten unten.
Satz bauen, Artikel, Präp. und Roller sind über das Pull-down "Ansicht" erreichbar.
Idempotent: Marker [sehen-neu2]."""
import re,sys
P="index.html"
s=open(P,encoding="utf-8").read()
if "[sehen-neu2]" in s:
    print("schon angewendet"); sys.exit(0)

def rep(a,b):
    global s
    assert s.count(a)==1,("Treffer != 1:",s.count(a),a[:80])
    s=s.replace(a,b)

# --- 1. Zustand
rep('const st={p:0,zl:0,v:0,fl:0,fm:"bsp"','const st={fv:0,fvc:-1,p:0,zl:0,v:0,fl:0,fm:"bsp"')

# --- 2. fSent: nur Artikel/Endung markiert, Verb-Auswahl je Fall
i=s.index("function fSent(c,g,hide){"); j=s.index("/* ----- Satz bauen",i)
s=s[:i]+'''const FRM=[
 [["schlafen",(n,pl)=>n+" "+(pl?"schlafen":"schläft")],["ist hier",(n,pl)=>n+" "+(pl?"sind":"ist")+" hier"],["kommt",(n,pl)=>n+" "+(pl?"kommen":"kommt")+" heute"]],
 [["sehen",n=>"Ich sehe "+n],["kennen",n=>"Ich kenne "+n],["besuchen",n=>"Ich besuche "+n]],
 [["helfen",n=>"Ich helfe "+n],["danken",n=>"Ich danke "+n],["antworten",n=>"Ich antworte "+n]],
 [["das Auto",n=>"Das ist das Auto "+n],["das Haus",n=>"Das ist das Haus "+n]]];
function nounH(c,g,col,hide,first){
 const A=ART[c][g],Nn=NO[g][c],B=NO[g][0],a=hide?"____":(first?CAP(A):A);
 const suf=(Nn.length>B.length&&Nn.indexOf(B)==0)?Nn.slice(B.length):"";
 return '<span class="np" style="background:'+col+'">'+a+'</span> '+(suf?B+'<span class="np" style="background:'+col+'">'+suf+'</span>':Nn);}
function fSent(c,g,hide){
 if(st.fvc!==c){st.fv=0;st.fvc=c;}
 const np=nounH(c,g,CC()[c],hide,c==0);
 const pl=g==3,fr=FRM[c][Math.min(st.fv,FRM[c].length-1)],main=fr[1](np,pl);
 const ns=[ 'weil '+['er','es','sie','sie'][g]+' müde <span class="vf">'+(pl?'sind':'ist')+'</span>.','obwohl es dunkel <span class="vf">ist</span>.','weil es <span class="vf">regnet</span>.','das ich gestern gesehen <span class="vf">habe</span>.'][c];
 return st.fl?{main:main+',',ns}:{main:main+'.',ns:""};}
'''+s[j:]

# --- 3. acc ohne Bildung (Bildung steht jetzt über der Auswahlzeile)
rep('const rows=[["B","Bildung",x.f],["G","Gebrauch",x.u],["S","Signale",x.s],["A","Achtung",x.a]];','const rows=[["G","Gebrauch",x.u],["S","Signale",x.s],["A","Achtung",x.a]];')

# --- 4. Tabelle: Beschriftungen antippbar, keine Hintergrundfarbe am Zeilenlabel, Farbe per --cc
rep("""let h='<div class="snt"><span></span>'+GN.map((x,i)=>'<span class="tn'+(g==i?' on':'')+'">'+x+'</span>').join("");""",
    """let h='<div class="snt" style="--cc:'+CC()[c]+'"><span></span>'+GN.map((x,i)=>'<span role="button" tabindex="0" class="tn'+(g==i?' on':'')+'" data-a="gc:'+i+'">'+x+'</span>').join("");""")
rep("""h+='<span class="tn'+(c==r?' on':'')+'" style="'+(c==r?'background:'+CC()[r]+';':'')+'">'+CN[r]+'</span>';""",
    """h+='<span role="button" tabindex="0" class="tn'+(c==r?' on':'')+'" data-a="cr:'+r+'">'+CN[r]+'</span>';""")

# --- 5. neue Bausteine + zH + fH(Beispiele)
i=s.index("function zH(){"); j=s.index("\n const v=VB[st.vb],b=build()",i)
new='''const SOL=t=>SVCFG.t.bands[t<3?0:t==3?1:2][2];
const MK=(x,col)=>'<span class="hl" style="background:'+col+'">'+x+'</span>';
function bildH(label,html){return '<div class="snbl"><span class="snc">Bildung · '+esc(label)+'</span><span class="snf">'+html+'</span></div>';}
function bildT(t,hide){
 const v=VZ[st.v],p=st.p,f=form(v,t,p),col=SOL(t),x=SVT[t];let fo;
 if(hide)fo="…";
 else if(t==3)fo=f.st+" + "+MK(f.en,col);
 else if(t==1){const e=f.en;
  if(e.indexOf("te")==0)fo=f.st+" + "+MK("te",col)+(e.length>2?" + "+MK(e.slice(2),col):"");
  else fo=MK(f.st,col)+(e?" + "+MK(e,col):"");}
 else if(t==0||t==2||t==4)fo=MK(f.fin,col)+" + "+MK(f.rest,col);
 else{const q=f.rest.split(" ");fo=MK(f.fin,col)+" + "+MK(q[0],col)+" + "+MK(q[1],col);}
 return bildH(x.f,fo);}
function bildF(c,g,hide){
 const base=ART[0][g]+" "+NO[g][0],x=SVKC[c];
 if(hide)return bildH(x.f,"…");
 return bildH(x.f,c==0?base:base+" → "+nounH(c,g,CC()[c],false,false));}
const NSEL=["der Mann","das Kind","die Frau","die Kinder"];
function sel1(id,label,opts,cur,flex){return '<div class="snc1" style="flex:'+flex+'"><label class="snl3" for="'+id+'">'+label+'</label><select id="'+id+'">'+opts.map((o,i)=>'<option value="'+i+'"'+(i==cur?' selected':'')+'>'+o+'</option>').join("")+'</select></div>';}
function selR(id,label,opts,cur,flex){return '<div class="snc1 rich" style="flex:'+flex+'"><label class="snl3" for="'+id+'">'+label+'</label><div class="disp">'+opts.map((o,i)=>i==cur?'<b>'+o+'</b>':o).join('<i>/</i>')+'</div><select id="'+id+'">'+opts.map((o,i)=>'<option value="'+i+'"'+(i==cur?' selected':'')+'>'+o+'</option>').join("")+'</select></div>';}
function zH(){
 const t=SV.cur.t,hide=st.rat&&st.ans==null,s=zSent(t,st.p,hide),x=SVT[t],f=FILL();
 let h='<div class="svg svbd" style="--n:6">'+SVCFG.t.bands.map(b=>'<span class="svb" style="grid-column:span '+b[1]+';background:'+b[2]+'">'+b[0]+'</span>').join("")+'</div>';
 h+='<div class="svg" style="--n:6">'+SVCFG.t.chips.map((c,i)=>'<span role="button" tabindex="0" class="svb svk fr'+(t==i?' on':'')+'" data-a="t:'+i+'"'+(t==i?' style="background:'+f[i]+'"':'')+'>'+c+'</span>').join("")+'</div>';
 h+='<div class="snhw" style="--hl:'+SOL(t)+'">'+hero(s,0,t>0,t<5)+'</div>'+optsH(plain(form(VZ[st.v],t,st.p)));
 h+=bildT(t,hide);
 h+='<div class="snctl">'+sel1("snzp","Person",PR,st.p,.7)+sel1("snzv","Verb",["lernen","gehen"],st.v,1)+selR("snzl","Satz",["Kurz","+ Nebensatz","Frage"],st.zl,2.3)+'</div>';
 h+=acc(x)+foot();
 return h;}
function fH(){
 let h=svSub();
 if(st.fm=="bsp"){
  const c=SV.cur.k,g=st.g,hide=st.rat&&st.ans==null,x=SVKC[c],f=CC();
  h+='<div class="svg svbd" style="--n:4">'+QW.map((q,i)=>'<span class="svb" style="background:'+f[i]+'">'+q+'</span>').join("")+'</div>';
  h+='<div class="svg" style="--n:4">'+CNn.map((n,i)=>'<span role="button" tabindex="0" class="svb svk fr'+(c==i?' on':'')+'" data-a="c:'+i+'"'+(c==i?' style="background:'+f[i]+'"':'')+'>'+n+'</span>').join("")+'</div>';
  h+='<div class="snhw">'+hero(fSent(c,g,hide),0,c>0,c<3)+'</div>'+optsH(ART[c][g]);
  h+=bildF(c,g,hide);
  h+='<div class="snctl">'+sel1("snfn","Nomen",NSEL,g,1.1)+sel1("snfv","Satz",FRM[c].map(y=>y[0]),Math.min(st.fv,FRM[c].length-1),1.1)+selR("snff","Form",["Kurz","+ Nebensatz"],st.fl,1.3)+'</div>';
  h+=acc(x)+'<div class="snc" style="display:block;padding:8px 8px 0">Artikel · antippen</div>'+table(c,g)+foot();return h;}'''
s=s[:i]+new+s[j:]

# --- 6. render: ohne Abstand, Linie auch in Fälle
rep("""(SV.tab==="t"?'<div style="height:6px"></div>'+zH()+'<svg class="svln" aria-hidden="true"><path id="svpath" fill="none" stroke="#b8b8b8" stroke-width="1.2" stroke-linecap="round" stroke-dasharray="0.5 2.5"/></svg>':fH())+'</div>';""",
    """(SV.tab==="t"?zH():fH())+'<svg class="svln" aria-hidden="true"><path id="svpath" fill="none" stroke="#b8b8b8" stroke-width="1.2" stroke-linecap="round" stroke-dasharray="0.5 2.5"/></svg></div>';""")

# --- 7. Klick- und Change-Aktionen
rep('  else if(a.startsWith("fl:")){st.fl=+a.slice(3);render();}',
    '  else if(a.startsWith("cr:")){SV.cur.k=+a.slice(3);newOpts();render();}\n  else if(a.startsWith("gc:")){st.g=+a.slice(3);newOpts();render();}\n  else if(a.startsWith("fl:")){st.fl=+a.slice(3);render();}')
rep('  if(t.id=="snv"){',
    '  if(t.id=="snzp"){st.p=+t.value;newOpts();render();}\n  else if(t.id=="snzv"){st.v=+t.value;newOpts();render();}\n  else if(t.id=="snzl"){st.zl=+t.value;render();}\n  else if(t.id=="snfn"){st.g=+t.value;newOpts();render();}\n  else if(t.id=="snfv"){st.fv=+t.value;render();}\n  else if(t.id=="snff"){st.fl=+t.value;render();}\n  else if(t.id=="snv"){')

# --- 8. setView / view
rep('return{render:open,U:{seg,hero,table,ART,CC,CAP,G,mix}};})();',
    'function setView(v){SV.tab="k";if(v=="bsp"||v=="bau"){SV.kp="s";st.fm=v;st.rat=false;newOpts();}else SV.kp=v;renderSehen();}\nconst view=()=>(SV.kp&&SV.kp!=="s")?SV.kp:(st.fm=="bau"?"bau":"bsp");\nreturn{render:open,setView,view,U:{seg,hero,table,ART,CC,CAP,G,mix}};})();')

# --- 9. Ansicht-Auswahl statt der zwei Knopfreihen
i=s.index("function svSub(){"); j=s.index("\n",i)
s=s[:i]+'''function svSub(){const V=[["bsp","Sätze"],["bau","Satz bauen"],["a","Artikel"],["p","Präp."],["r","Roller"]],cur=SNEW.view();
 return '<div class="snctl snans"><div class="snc1 rich" style="flex:1"><label class="snl3" for="snans">Ansicht</label><div class="disp">'+V.map(x=>x[0]==cur?'<b>'+x[1]+'</b>':x[1]).join('<i>/</i>')+'</div><select id="snans">'+V.map(x=>'<option value="'+x[0]+'"'+(x[0]==cur?' selected':'')+'>'+x[1]+'</option>').join('')+'</select></div></div>';}
document.addEventListener("change",e=>{if(e.target&&e.target.id==="snans")SNEW.setView(e.target.value);});'''+s[j:]

# --- 10. Linie: Ziel = Endung, sonst Verb, sonst Artikel
rep('w=sv.querySelector(".sns .g");if(!on||!w)','w=sv.querySelector(".sns .end")||sv.querySelector(".sns .g")||sv.querySelector(".sns .np");if(!on||!w)')

# --- 11. CSS
css='''<style id="sehen-neu2-css">/* [sehen-neu2] */
.sn .svbd{margin-top:0}
.sn .snhw{position:relative}
.sn .snhw .g,.sn .snhw .y{background:var(--hl,#c8f23c);color:#1a1a1a;font-weight:700;padding:0 3px;margin:0 -1px}
.sn .snhw .g:has(.end){background:none;padding:0;margin:0}
.sn .snhw .end{background:var(--hl,#c8f23c);border-bottom:0;font-weight:700;padding:0 3px;margin:0 -1px}
.sn .np{font-weight:700;margin:0 -1px}
.sn .snbl{position:relative;padding:9px 10px 10px;background:var(--df) left bottom/100% 1px no-repeat}
.sn .snc,.sn .snl3{display:block;font-size:9px;letter-spacing:.09em;text-transform:uppercase;color:var(--red);font-weight:700;line-height:1}
.sn .snbl .snc{margin-bottom:5px}
.sn .snf{display:block;font-size:18px;line-height:1.35;color:#1a1a1a}
.sn .snf .hl{font-weight:700;padding:0 3px;margin:0 -1px}
.sn .snctl{display:flex;position:relative;background:var(--df) left top/100% 1px no-repeat,var(--dfv) left top/1px 100% no-repeat}
.sn .snc1{position:relative;min-width:0;padding:6px 8px 4px;background:var(--df) left bottom/100% 1px no-repeat,var(--dfv) right top/1px 100% no-repeat}
.sn .snl3{margin-bottom:3px}
.sn .snc1 select{appearance:none;-webkit-appearance:none;display:block;border:0;border-radius:0;background:transparent url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='10' height='6'%3E%3Cpolyline points='1,1 5,5 9,1' fill='none' stroke='%23222' stroke-width='1.4'/%3E%3C/svg%3E") right 1px center no-repeat;font:inherit;font-weight:700;font-size:15px;color:#222;width:100%;height:30px;padding:0 14px 0 0;margin:0;text-overflow:ellipsis}
.sn .snc1.rich select{position:absolute;left:0;top:0;width:100%;height:100%;opacity:0;font-size:16px;cursor:pointer}
.sn .snc1 .disp{font-size:11.5px;color:#8a8a8a;white-space:nowrap;height:30px;line-height:30px;padding-right:14px;background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='10' height='6'%3E%3Cpolyline points='1,1 5,5 9,1' fill='none' stroke='%23222' stroke-width='1.4'/%3E%3C/svg%3E") right 1px center no-repeat}
.sn .snc1 .disp b{font-weight:700;color:#1a1a1a;font-size:13px}
.sn .snc1 .disp i{font-style:normal;margin:0 2px;color:#bbb}
.sn .snans .snc1{display:flex;align-items:center;gap:8px;padding:0 8px;min-height:30px}
.sn .snans .snl3{margin:0;flex:0 0 auto}
.sn .snans .disp{flex:1;min-width:0;overflow:hidden}
.snt{--cs:38px;grid-template-columns:36px repeat(4,var(--cs));grid-template-rows:18px repeat(4,var(--cs))}
.snt .tn{font-size:9px;font-weight:700;letter-spacing:.06em;color:var(--red);cursor:pointer;-webkit-tap-highlight-color:transparent}
.snt .tn.on{color:#111}
.snt .tq{font-size:17px}
.snt .tq.grp,.snt .tq.sel{background:var(--cc,#e4f7a0)}
.snt .tq.grp .tz,.snt .tq.sel .tz{font-weight:700}
</style>
'''
rep('<style id="acc-offen-css">',css+'<style id="acc-offen-css">')

# --- 12. Version
m=re.search(r'<meta name="app-version" content="([^"]*)">',s)
assert m
rep(m.group(0),'<meta name="app-version" content="2026-11-23a">')
open(P,"w",encoding="utf-8").write(s)
print("ok")
