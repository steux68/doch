#!/usr/bin/env python3
"""Rueckmeldung 2 (2026-11-21h): Adjektivendungen erklaert ('-e = ...'), 'Regel →'-Link zur Lernen-Ansicht bei falscher Wahl,
und beim Tippen gilt 'zu dem' fuer 'zum' usw. als richtig. Ersetzt den Block wx-js. Idempotent."""
import os,re
root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
p=os.path.join(root,"index.html");s=open(p,encoding="utf-8").read()
if 'id="wx2-js"' in s: print("already patched");raise SystemExit
i=s.index('<script id="wx-js">');j=s.index('</script>',i)+len('</script>')
js=r'''<style id="wx2-css">#nf .wxl{all:unset;cursor:pointer;color:#e30613;font-weight:700;border-bottom:1px dotted #e30613;position:relative}#nf .wxl::before{content:"";position:absolute;inset:-12px -8px}</style>
<script id="wx2-js">(function(){
var F={"der":"Nom. m. · Dat. f. · Gen. f./pl.","die":"Nom./Akk. f. · Nom./Akk. pl.","das":"Nom./Akk. n.","den":"Akk. m. · Dat. pl.","dem":"Dat. m./n.","des":"Gen. m./n.",
"ein":"Nom. m./n. · Akk. n.","eine":"Nom./Akk. f.","einen":"Akk. m.","einem":"Dat. m./n.","einer":"Dat./Gen. f.","eines":"Gen. m./n.",
"mein":"Nom. m./n. · Akk. n.","meine":"Nom./Akk. f./pl.","meinen":"Akk. m. · Dat. pl.","meinem":"Dat. m./n.","meiner":"Dat./Gen. f.",
"sein":"Nom. m./n. · Akk. n.","seine":"Nom./Akk. f./pl.","seinen":"Akk. m. · Dat. pl.","seinem":"Dat. m./n.","seiner":"Dat./Gen. f.",
"im":"in + dem · Dat. m./n.","ins":"in + das · Akk. n.","am":"an + dem · Dat. m./n.","ans":"an + das · Akk. n.","zum":"zu + dem · Dat. m./n.","zur":"zu + der · Dat. f.","beim":"bei + dem · Dat. m./n.","vom":"von + dem · Dat. m./n.","aufs":"auf + das · Akk. n.",
"ihm":"Dat. er/es","ihn":"Akk. er","ihr":"Dat. sie (f.)","mir":"Dat. ich","mich":"Akk. ich","dir":"Dat. du","dich":"Akk. du","ihnen":"Dat. sie (pl.)","uns":"Akk./Dat. wir"};
var A={"e":"Nom. m. (der) · Nom./Akk. f. · Nom./Akk. n. (das) · pl. ohne Artikel","en":"nach Artikel: Akk. m., Dat., Gen., pl. · ohne Artikel: Akk. m., Gen. m./n., Dat. pl.","er":"Nom. m. nach ein- · Dat./Gen. f. ohne Artikel","es":"Nom./Akk. n. nach ein- oder ohne Artikel","em":"Dat. m./n. ohne Artikel"};
var CT={"im":"in dem","ins":"in das","am":"an dem","ans":"an das","zum":"zu dem","zur":"zu der","beim":"bei dem","vom":"von dem","aufs":"auf das"};
function hook(){if(typeof mcAnswer==="function"&&!mcAnswer.__wx){var o=mcAnswer;
 mcAnswer=function(i){var r=o.apply(this,arguments);try{
  var q=MC&&MC.list&&MC.list[MC.i];if(!q||i==null||i<0||i===q.c||!q.o||q.o[i]==null)return r;
  var w=String(q.o[i]),g=document.getElementById("gt");
  if(g&&/^Nicht ganz\. /.test(g.textContent))g.textContent="Nicht „"+w+"“. "+g.textContent.slice(12);
  var nf=document.getElementById("nf");if(!nf)return r;
  var k=q.t==="adj"?A[w.replace(/^-/,"").toLowerCase()]:F[w.toLowerCase()];
  var h=nf.innerHTML.trim();
  if(!h&&k)h="<b>"+(q.t==="adj"?"-"+w.replace(/^-/,""):w)+"</b> = "+k;
  if(!nf.querySelector(".wxl"))h+=(h?" · ":"")+'<button type="button" class="wxl">Regel →</button>';
  nf.innerHTML=h;
 }catch(e){}return r;};mcAnswer.__wx=1;}
 if(typeof judge==="function"&&!judge.__wx){var oj=judge;
  judge=function(a,b){var r=oj(a,b);if(r[0]!=="ok"&&CT[b]&&String(a).trim().replace(/\s+/g," ").toLowerCase()===CT[b])return["ok",""];return r;};judge.__wx=1;}}
document.addEventListener("click",function(e){var b=e.target.closest&&e.target.closest("#nf .wxl");if(b&&typeof setMode==="function"){e.preventDefault();setMode("learn");}});
hook();setInterval(hook,500);
})();</script>'''
s=s[:i]+js+s[j:]
s=re.sub(r'<meta name="app-version" content="[^"]+">','<meta name="app-version" content="2026-11-21h">',s,count=1)
open(p,"w",encoding="utf-8").write(s);print("ok")
