# Zusätzliche Sicherung: DOCH! beginnt immer ganz oben (Startseite), bis die Person selbst wischt oder tippt. Idempotent.
import re
P="index.html";s=open(P,encoding="utf-8").read()
J=('<script id="top-lock">(function(){var SC=document.getElementById("hscroll"),u=false;'
'["touchstart","wheel","keydown","mousedown"].forEach(function(e){addEventListener(e,function(){u=true},{once:true,passive:true})});'
'function z(){if(!u&&SC&&SC.scrollTop>0)SC.scrollTo({top:0,behavior:"auto"})}'
'[0,150,400,900,1800,3500].forEach(function(t){setTimeout(z,t)});addEventListener("load",z);addEventListener("pageshow",z);})();</script>')
s=re.sub(r'<script id="top-lock">.*?</script>','',s,flags=re.S)
s=s.replace('</body>',J+'</body>',1)
s=re.sub(r'(<meta name="app-version" content=")[^"]*(")',lambda m:m.group(1)+'2026-11-01b'+m.group(2),s,count=1)
open(P,"w",encoding="utf-8").write(s)
