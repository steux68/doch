#!/usr/bin/env python3
"""Aufgabenzeile 'Ergänze: …' fragenweise nach Wortart (Steuart, 15 Nov 2026). Ersetzt das Skript aufgabe-js. Nach spiel_aufgabe_patch.py."""
import re, sys
p = "index.html"
s = open(p, encoding="utf-8").read()
if 'id="aufgabe2-js"' in s: sys.exit("already patched")
m = re.search(r'<script id="aufgabe-js">.*?</script>', s, re.S)
if not m: sys.exit("aufgabe-js fehlt")
JS = r"""<script id="aufgabe2-js">(function(){
var AUX=/^(sind|bin|ist|habe|hat|haben|hatte|hatten|werde|wurde|wird|war|waren|wären|hätte|hätten)$/;
function lab(q){var a=String(q.o[q.c]||""),k=q.t,sx=q.s||"",hasInf=/\(\w+\)\s*$/.test(sx);
if(k==="vprep"||k==="prep")return "Präposition";
if(k==="art")return "Artikel";
if(k==="rel")return "Relativpronomen";
if(k==="praes"){if(/^(an|auf|aus|ein|ab|um|zu|vor|mit|nach)$/.test(a))return "Vorsilbe des trennbaren Verbs";return "Verb in der richtigen Form";}
if(k==="modal")return "Modalverb in der richtigen Form";
if(k==="perf")return AUX.test(a)?"Hilfsverb":"Partizip oder Verbform";
if(k==="pass"){if(/^(von|durch|mit)$/.test(a))return "Präposition";if(a==="zu")return "Wort vor dem Infinitiv";return "Form von werden / Verbform";}
if(k==="k1"||k==="k2")return "Verb im Konjunktiv";
if(k==="konn")return hasInf?"Hilfsverb":"Bindewort";
if(k==="neg"){if(/^(nicht|kein\w*)$/.test(a))return "nicht oder kein (richtige Form)";if(/^(sondern|noch)$/.test(a))return "Bindewort";if(a==="nichts")return "Verneinungswort";if(a==="Doch")return "Antwortwort";return "Verneinung";}
if(k==="zuinf"){if(/^(um|damit|ohne|statt|darauf)$/i.test(a))return "Wort vor dem Infinitiv";return "Infinitiv (mit oder ohne zu)";}
if(k==="nom"){if(/^(Wegen|Trotz|Während|Bei)$/.test(a))return "Präposition";if(/^[A-ZÄÖÜ]/.test(a))return "Nomen";return "Partizip als Adjektiv (mit Endung)";}
if(k==="nvv")return /^[A-ZÄÖÜ]/.test(a)?"Nomen":"Verb in der richtigen Form";
return "fehlendes Wort";}
setInterval(function(){var a=document.getElementById("ans");if(!a)return;var w=a.closest(".answer")||a.parentNode,t=document.getElementById("task"),q;try{q=MC.list[MC.i];}catch(e){}var txt="fehlendes Wort";try{if(q)txt=lab(q);}catch(e){}var h="Ergänze: <b>"+txt+"</b>";if(!t){t=document.createElement("div");t.id="task";w.parentNode.insertBefore(t,w);}if(t.innerHTML!==h)t.innerHTML=h;},150);})();</script>"""
s = s[:m.start()] + JS + s[m.end():]
mm = re.search(r'name="app-version" content="(\d{4}-\d\d-\d\d)([a-z]?)"', s)
if mm: s = s.replace(mm.group(0), 'name="app-version" content="%s%s"' % (mm.group(1), chr(ord(mm.group(2) or "`") + 1)))
open(p, "w", encoding="utf-8").write(s); print("OK")
