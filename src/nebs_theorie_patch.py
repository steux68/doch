#!/usr/bin/env python3
"""Nebensaetze: Theorie in drei Stufen (2026-11-21m): 1 einfache Regel, 2 Schritt fuer Schritt, 3 Ausnahmen. Eigene Formulierung. Idempotent."""
import os,re
root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
p=os.path.join(root,"index.html");s=open(p,encoding="utf-8").read()
if "1 · Die einfache Regel <small>A2</small></h3><p class=\"memo\">A Nebensatz" in s: print("already patched");raise SystemExit
a='<div class="tc df"><h3>Das Verb am Ende</h3>'
assert s.count(a)==1
new='''<div class="tc df"><h3>1 · Die einfache Regel <small>A2</small></h3><p class="memo">A Nebensatz starts with a conjunction (weil, dass, wenn, obwohl …). The conjugated verb goes to the <b>end</b>. A comma separates it from the main clause.</p><p class="tline">Ich bleibe zu Hause, weil ich krank <b>bin</b>.</p></div>
<div class="tc df"><h3>2 · Schritt für Schritt <small>A2–B1</small></h3><div class="rows">
<div><span>1 Hauptsatz</span><span>Ich bleibe zu Hause.</span></div>
<div><span>2 Konjunktion</span><span>Add weil: …, weil ich krank … The verb must move.</span></div>
<div><span>3 Verb ans Ende</span><span>…, weil ich krank <b>bin</b>.</span></div>
<div><span>Nebensatz zuerst</span><span>Weil ich krank bin, <b>bleibe</b> ich zu Hause.</span></div></div><p class="tline">After the comma the main clause starts with its verb. The sentence ends with a full stop after the last clause, not with a comma.</p></div>
<div class="tc df"><h3>3 · Ausnahmen &amp; mehr <small>B2–C1</small></h3><div class="rows">
<div><span>trennbar</span><span>The verb stays in one piece: …, weil ich früh <b>aufstehe</b>.</span></div>
<div><span>um … zu</span><span>Same subject: Ich lerne, <b>um</b> die Prüfung <b>zu</b> bestehen. Different subject: …, <b>damit</b> du die Prüfung bestehst.</span></div>
<div><span>dass weglassen</span><span>Ich glaube, er kommt. Without dass the verb is in second place again.</span></div>
<div><span>ohne wenn</span><span>Hätte ich Zeit, käme ich mit. = Wenn ich Zeit hätte, …</span></div>
<div><span>Modal im Perfekt</span><span>…, weil er hat arbeiten müssen.</span></div>
<div><span>gesprochen</span><span>You hear „weil ich bin krank“ in speech. In writing and exams: the verb goes to the end.</span></div></div></div>
'''
s=s.replace(a,new+a)
s=re.sub(r'<meta name="app-version" content="[^"]+">','<meta name="app-version" content="2026-11-21m">',s,count=1)
open(p,"w",encoding="utf-8").write(s);print("ok")
