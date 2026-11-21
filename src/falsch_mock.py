#!/usr/bin/env python3
"""Mock-up falsch.html: bessere Rueckmeldung bei falscher Wahl. Testkopie, index.html unveraendert.
1) 'Nicht ganz.' -> 'Nicht „den“.'  (gleich lang, kein Hoehensprung)
2) bei Artikel-/Pronomenformen steht in der Zeile darunter, was die gewaehlte Form tatsaechlich ist (feste Tabelle, kein Parser)."""
import os
root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
s=open(os.path.join(root,"index.html"),encoding="utf-8").read()
js="""<script id="wx-js">(function(){
var F={"der":"Nom. m. · Dat. f. · Gen. f./pl.","die":"Nom./Akk. f. · Nom./Akk. pl.","das":"Nom./Akk. n.","den":"Akk. m. · Dat. pl.","dem":"Dat. m./n.","des":"Gen. m./n.",
"ein":"Nom. m./n. · Akk. n.","eine":"Nom./Akk. f.","einen":"Akk. m.","einem":"Dat. m./n.","einer":"Dat./Gen. f.","eines":"Gen. m./n.",
"mein":"Nom. m./n. · Akk. n.","meine":"Nom./Akk. f./pl.","meinen":"Akk. m. · Dat. pl.","meinem":"Dat. m./n.","meiner":"Dat./Gen. f.",
"sein":"Nom. m./n. · Akk. n.","seine":"Nom./Akk. f./pl.","seinen":"Akk. m. · Dat. pl.","seinem":"Dat. m./n.","seiner":"Dat./Gen. f.",
"im":"in + dem · Dat. m./n.","ins":"in + das · Akk. n.","am":"an + dem · Dat. m./n.","ans":"an + das · Akk. n.","zum":"zu + dem · Dat. m./n.","zur":"zu + der · Dat. f.","beim":"bei + dem · Dat. m./n.","vom":"von + dem · Dat. m./n.","aufs":"auf + das · Akk. n.",
"ihm":"Dat. er/es","ihn":"Akk. er","ihr":"Dat. sie (f.)","mir":"Dat. ich","mich":"Akk. ich","dir":"Dat. du","dich":"Akk. du","ihnen":"Dat. sie (pl.)","uns":"Akk./Dat. wir"};
function hook(){if(typeof mcAnswer!=="function"||mcAnswer.__wx)return;var o=mcAnswer;
 mcAnswer=function(i){var r=o.apply(this,arguments);try{
  var q=MC&&MC.list&&MC.list[MC.i];if(!q||i==null||i<0||i===q.c||!q.o||q.o[i]==null)return r;
  var w=q.o[i],g=document.getElementById("gt");
  if(g&&/^Nicht ganz\\. /.test(g.textContent))g.textContent="Nicht „"+w+"“. "+g.textContent.slice(12);
  var nf=document.getElementById("nf"),k=F[String(w).toLowerCase()];
  if(nf&&k&&!nf.textContent.trim())nf.innerHTML="<b>"+w+"</b> = "+k;
 }catch(e){}return r;};mcAnswer.__wx=1;}
hook();setInterval(hook,500);
})();</script>"""
s=s+js
open(os.path.join(root,"falsch.html"),"w",encoding="utf-8").write(s);print("ok")
