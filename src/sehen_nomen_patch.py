#!/usr/bin/env python3
"""Sehen/Fälle: 10 Nomen, je 10 Verben/Satzrahmen pro Fall (2026-11-23f). Marker [sehen-nomen]. Idempotent."""
import sys
P="index.html"
s=open(P,encoding="utf-8").read()
if "[sehen-nomen]" in s:
    print("schon angewendet"); sys.exit(0)
def rep(a,b):
    global s
    assert s.count(a)==1,("Treffer != 1:",s.count(a),a[:80])
    s=s.replace(a,b)
i=s.index("const FRM=["); j=s.index("]];",i)+3
s=s[:i]+'''/* [sehen-nomen] Satzrahmen je Fall (Name, Satz, optional Nebensatz). Bitte Deutsch prüfen. */
const VN=(l,a,b,r)=>[l,(n,pl)=>n+" "+(pl?b:a)+(r?" "+r:"")];
const VA=(l,f)=>[l,n=>"Ich "+f+" "+n];
const FRM=[
 [VN("schlafen","schläft","schlafen"),VN("ist hier","ist","sind","hier"),VN("kommt","kommt","kommen","heute"),VN("lachen","lacht","lachen"),VN("warten","wartet","warten","hier"),VN("wohnen","wohnt","wohnen","hier"),VN("arbeiten","arbeitet","arbeiten","heute"),VN("spielen","spielt","spielen","draußen"),VN("bleiben","bleibt","bleiben","zu Hause"),VN("lernen","lernt","lernen","viel")],
 [VA("sehen","sehe"),VA("kennen","kenne"),VA("besuchen","besuche"),VA("treffen","treffe"),VA("finden","finde"),VA("suchen","suche"),VA("brauchen","brauche"),VA("mögen","mag"),VA("fragen","frage"),VA("rufen","rufe")],
 [VA("helfen","helfe"),VA("danken","danke"),VA("antworten","antworte"),["gehören",n=>"Das Buch gehört "+n],["gefallen",n=>"Das Buch gefällt "+n],VA("glauben","glaube"),VA("folgen","folge"),["zuhören",n=>"Ich höre "+n+" zu"],VA("vertrauen","vertraue"),VA("gratulieren","gratuliere")],
 [["das Auto",n=>"Das ist das Auto "+n,"das ich gestern gesehen <span class=\\"vf\\">habe</span>."],["das Fahrrad",n=>"Das ist das Fahrrad "+n,"das ich gestern gesehen <span class=\\"vf\\">habe</span>."],["der Garten",n=>"Das ist der Garten "+n,"den ich gestern gesehen <span class=\\"vf\\">habe</span>."],["das Buch",n=>"Das ist das Buch "+n,"das ich gestern gelesen <span class=\\"vf\\">habe</span>."],["die Tasche",n=>"Das ist die Tasche "+n,"die ich gestern gesehen <span class=\\"vf\\">habe</span>."],["das Zimmer",n=>"Das ist das Zimmer "+n,"das ich gestern gesehen <span class=\\"vf\\">habe</span>."],["der Name",n=>"Das ist der Name "+n,"den ich gestern gehört <span class=\\"vf\\">habe</span>."],["die Meinung",n=>"Das ist die Meinung "+n,"die ich gestern gehört <span class=\\"vf\\">habe</span>."],["wegen",n=>"Wegen "+n+" bleibe ich hier","weil es <span class=\\"vf\\">regnet</span>."],["trotz",n=>"Trotz "+n+" gehe ich raus","obwohl es dunkel <span class=\\"vf\\">ist</span>."]]];
/* Nomen: g = Spalte der Tabelle (0 M, 1 N, 2 F, 3 Pl); f = Nom, Akk, Dat, Gen */
const NL=[
 {g:0,f:["Mann","Mann","Mann","Mannes"]},{g:0,f:["Hund","Hund","Hund","Hundes"]},{g:0,f:["Student","Studenten","Studenten","Studenten"],n:1},{g:0,f:["Lehrer","Lehrer","Lehrer","Lehrers"]},
 {g:1,f:["Kind","Kind","Kind","Kindes"]},{g:1,f:["Mädchen","Mädchen","Mädchen","Mädchens"]},
 {g:2,f:["Frau","Frau","Frau","Frau"]},{g:2,f:["Katze","Katze","Katze","Katze"]},
 {g:3,f:["Kinder","Kinder","Kindern","Kinder"]},{g:3,f:["Freunde","Freunde","Freunden","Freunde"]}];
'''+s[j:]
# Zustand
rep("const st={fv:0,fvc:-1,","const st={nn:0,fv:0,fvc:-1,")
# nounH
rep("""const A=ART[c][g],Nn=NO[g][c],B=NO[g][0],a=hide?"____":(first?CAP(A):A);""","""const A=ART[c][g],nz=NL[st.nn],Nn=nz.f[c],B=nz.f[0],a=hide?"____":(first?CAP(A):A);""")
# Nebensatz je Rahmen
rep("""return st.fl?{main:main+',',ns}:{main:main+'.',ns:""};}""","""const nsx=(c==3&&fr[2])?fr[2]:ns;
 return st.fl?{main:main+',',ns:nsx}:{main:main+'.',ns:""};}""")
rep("""const base=ART[0][g]+" "+NO[g][0],x=SVKC[c];""","""const base=ART[0][g]+" "+NL[st.nn].f[0],x=SVKC[c];""")
# Nomenliste
rep("""const NSEL=["der Mann","das Kind","die Frau","die Kinder"];""","""const NSEL=NL.map(n=>ART[0][n.g]+" "+n.f[0]);""")
rep("""const c=SV.cur.k,g=st.g,hide=st.rat&&st.ans==null,x=SVKC[c],f=CC();""","""if(NL[st.nn].g!==st.g)st.nn=NL.findIndex(n=>n.g==st.g);
  const c=SV.cur.k,g=st.g,hide=st.rat&&st.ans==null,f=CC(),x0=SVKC[c],x=(NL[st.nn].n&&c>0)?Object.assign({},x0,{a:"n-Deklination: "+NL[st.nn].f[0]+" → -en in allen Fällen außer Nom."}):x0;""")
rep("""sel1("snfn","Nomen",NSEL,g,1.1)""","""sel1("snfn","Nomen",NSEL,st.nn,1.1)""")
rep("""else if(t.id=="snfn"){st.g=+t.value;newOpts();render();}""","""else if(t.id=="snfn"){st.nn=+t.value;st.g=NL[st.nn].g;newOpts();render();}""")
rep('app-version" content="2026-11-23e"','app-version" content="2026-11-23f"')
open(P,"w",encoding="utf-8").write(s)
print("ok")
