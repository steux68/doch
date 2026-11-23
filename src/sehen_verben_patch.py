#!/usr/bin/env python3
"""Sehen: 10 Verben (Zeiten) + Raten neben dem Satz (2026-11-23b). Marker [sehen-verben]. Idempotent."""
import re,sys
P="index.html"
s=open(P,encoding="utf-8").read()
if "[sehen-verben]" in s:
    print("schon angewendet"); sys.exit(0)
def rep(a,b):
    global s
    assert s.count(a)==1,("Treffer != 1:",s.count(a),a[:80])
    s=s.replace(a,b)

# 1. zehn Verben (nach Muster gewählt)
i=s.index("const VZ=["); j=s.index("nv:SEIN}];",i)+len("nv:SEIN}];")
TE='["te","test","te","ten","tet","ten"]'; ST='["","st","","en","t","en"]'
s=s[:i]+'''/* [sehen-verben] regelmäßig: lernen, machen, arbeiten · Stammvokal: sehen, geben · mit sein: gehen, kommen, bleiben · Hilfsverben: sein, haben. o = Ergänzung, pr = unregelmäßige Präsensformen (Text = ganzes Wort, [Stamm,Endung] = Endung) */
const VZ=[
 {inf:"lernen",s:"lern",ps:"lern",pte:'''+TE+''',pp:"gelernt",a:HAB,a0:HATT,fi:"haben",ns:"die Prüfung bestehen",nv:WILL},
 {inf:"machen",s:"mach",ps:"mach",pte:'''+TE+''',pp:"gemacht",a:HAB,a0:HATT,fi:"haben",ns:"die Prüfung bestehen",nv:WILL,o:"Hausaufgaben"},
 {inf:"arbeiten",s:"arbeit",ps:"arbeit",pte:["ete","etest","ete","eten","etet","eten"],pp:"gearbeitet",a:HAB,a0:HATT,fi:"haben",ns:"Geld verdienen",nv:WILL,pr:[null,["arbeit","est"],["arbeit","et"],null,["arbeit","et"],null]},
 {inf:"sehen",s:"seh",ps:"sah",pte:'''+ST+''',pp:"gesehen",a:HAB,a0:HATT,fi:"haben",ns:"neugierig",nv:SEIN,o:"den Film",pr:[null,"siehst","sieht",null,null,null]},
 {inf:"geben",s:"geb",ps:"gab",pte:'''+ST+''',pp:"gegeben",a:HAB,a0:HATT,fi:"haben",ns:"ihm helfen",nv:WILL,o:"ihm das Buch",pr:[null,"gibst","gibt",null,null,null]},
 {inf:"gehen",s:"geh",ps:"ging",pte:'''+ST+''',pp:"gegangen",a:SEIN,a0:WAR,fi:"sein",ns:"müde",nv:SEIN},
 {inf:"kommen",s:"komm",ps:"kam",pte:'''+ST+''',pp:"gekommen",a:SEIN,a0:WAR,fi:"sein",ns:"Zeit",nv:HAB},
 {inf:"bleiben",s:"bleib",ps:"blieb",pte:'''+ST+''',pp:"geblieben",a:SEIN,a0:WAR,fi:"sein",ns:"krank",nv:SEIN},
 {inf:"sein",s:"",ps:"war",pte:'''+ST+''',pp:"gewesen",a:SEIN,a0:WAR,fi:"sein",ns:"lange gearbeitet",nv:HAB,o:"müde",pr:["bin","bist","ist","sind","seid","sind"]},
 {inf:"haben",s:"hab",ps:"hat",pte:'''+TE+''',pp:"gehabt",a:HAB,a0:HATT,fi:"haben",ns:"frei",nv:SEIN,o:"Zeit",pr:[null,"hast","hat",null,null,null]}];'''+s[j:]

# 2. Präsens: unregelmäßige Formen
rep('if(t==3)return{st:v.s,en:PE[p],rest:""};','if(t==3){const r=v.pr&&v.pr[p];if(r)return typeof r=="string"?{fin:r,rest:"",irr:1}:{st:r[0],en:r[1],rest:""};return{st:v.s,en:PE[p],rest:""};}')

# 3. zSent mit Ergänzung
i=s.index("function zSent(t,p,hide){"); j=s.index("\nconst FILL=",i)
s=s[:i]+'''function zSent(t,p,hide){
 const v=VZ[st.v],f=form(v,t,p),L=st.zl,o=v.o?' '+v.o:'',yr=(f.rest&&f.st===undefined)?' '+Y(f.rest):'';let main,ns="";
 if(L==2){main=(hide?BLANK:G(finH(f,true)))+' '+PR[p]+o+(hide?'':yr)+'?';}
 else{const vg=hide?BLANK+o:(f.st!==undefined?G(finH(f,false))+o:G(f.fin)+o+yr);main=CAP(PR[p])+' '+vg+(L==1?',':'.');}
 if(L==1)ns='weil '+PR[p]+' '+v.ns+' <span class="vf">'+v.nv[p]+'</span>.';
 return{main,ns};}'''+s[j:]

# 4. Bildung-Zeile: Raten-Knopf rechts oben, unregelmäßige Formen
rep('''function bildH(label,html){return '<div class="snbl"><span class="snc">Bildung · '+esc(label)+'</span><span class="snf">'+html+'</span></div>';}''',
    '''function bildH(label,html){return '<div class="snbl"><div class="snbh"><span class="snc">Bildung · '+esc(label)+'</span><span role="button" tabindex="0" class="snrat'+(st.rat?' on':'')+'" data-a="rat">Raten</span></div><span class="snf">'+html+'</span></div>';}''')
rep("col=SOL(t),x=SVT[t];let fo;","col=SOL(t),x=SVT[t];let fo,lab=x.f;")
rep(''' else if(t==3)fo=f.st+" + "+MK(f.en,col);
 else if(t==1){const e=f.en;
  if(e.indexOf("te")==0)fo=f.st+" + "+MK("te",col)+(e.length>2?" + "+MK(e.slice(2),col):"");
  else fo=MK(f.st,col)+(e?" + "+MK(e,col):"");}''',
''' else if(t==3){
  if(f.fin!==undefined){lab="unregelmäßig";fo=v.inf+" → "+MK(f.fin,col);}
  else fo=f.st+" + "+MK(f.en,col);}
 else if(t==1){const e=f.en,m=/^e?te/.exec(e);
  if(m)fo=f.st+" + "+MK(m[0],col)+(e.length>m[0].length?" + "+MK(e.slice(m[0].length),col):"");
  else fo=MK(f.st,col)+(e?" + "+MK(e,col):"");}''')
rep("return bildH(x.f,fo);}","return bildH(lab,fo);}")

# 5. Verb-Auswahl aus VZ; Raten-Zeile unten entfällt
rep('sel1("snzv","Verb",["lernen","gehen"],st.v,1)','sel1("snzv","Verb",VZ.map(v=>v.inf),st.v,1)')
rep(" h+=acc(x)+foot();\n return h;}"," h+=acc(x);\n return h;}")
rep("+table(c,g)+foot();return h;}","+table(c,g);return h;}")

# 6. CSS
rep("</style>\n<style id=\"acc-offen-css\">",""".sn .snbh{display:flex;align-items:flex-start;justify-content:space-between;gap:8px;margin-bottom:6px}
.sn .snbh .snc{flex:1;min-width:0;line-height:1.4;margin:5px 0 0}
.sn .snrat{position:relative;flex:0 0 auto;height:24px;padding:0 12px;display:flex;align-items:center;font-size:11px;letter-spacing:.09em;text-transform:uppercase;color:#222;cursor:pointer;-webkit-tap-highlight-color:transparent;background:var(--df) left top/100% 1px no-repeat,var(--df) left bottom/100% 1px no-repeat,var(--dfv) left top/1px 100% no-repeat,var(--dfv) right top/1px 100% no-repeat}
.sn .snrat::before{content:"";position:absolute;inset:-8px}
.sn .snrat.on{background-color:#cdff3e;font-weight:700}
/* [sehen-verben] */
</style>
<style id="acc-offen-css">""")

m=re.search(r'<meta name="app-version" content="([^"]*)">',s); assert m
rep(m.group(0),'<meta name="app-version" content="2026-11-23b">')
open(P,"w",encoding="utf-8").write(s)
print("ok")
