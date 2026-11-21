#!/usr/bin/env python3
"""Faelle & Pronomen und Praepositionen & Fall: Theorie in drei Stufen (2026-11-21n). Eigene Formulierung. Idempotent."""
import os,re
root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
p=os.path.join(root,"index.html");s=open(p,encoding="utf-8").read()
if "Find the preposition" in s: print("already patched");raise SystemExit
def rep(a,b):
    global s
    assert s.count(a)==1,a[:70]
    s=s.replace(a,b)
FALL='''<div class="tc df"><h3>1 · Die einfache Regel <small>A1</small></h3><p class="memo">Every noun plays a role. <b>Nominativ</b> does it, <b>Akkusativ</b> receives it, <b>Dativ</b> gets something from it, <b>Genitiv</b> owns it. The role shows in the article: der → den → dem → des.</p><p class="tline">Der Mann sieht den Hund. Only the masculine changes between Nominativ and Akkusativ.</p></div>
<div class="tc df"><h3>2 · Schritt für Schritt <small>A2–B1</small></h3><div class="rows">
<div><span>Wer zeigt?</span><span>NOM · <b>der Architekt</b></span></div>
<div><span>Wem?</span><span>DAT · <b>dem Kunden</b> (masc. → dem)</span></div>
<div><span>Was?</span><span>AKK · <b>den Plan</b> (masc. → den)</span></div></div><p class="tline">Der Architekt zeigt dem Kunden den Plan. Ask the verb: Wer? Wem? Was? Then pick the article by gender.</p></div>
<div class="tc df"><h3>3 · Ausnahmen &amp; mehr <small>B2–C1</small></h3><div class="rows">
<div><span>n-Deklination</span><span>der Student → den, dem, des <b>Studenten</b></span></div>
<div><span>Dativ Plural</span><span>mit den Kinder<b>n</b> · von den Kollegen</span></div>
<div><span>Genitiv</span><span>masculine and neuter nouns add -s or -es: des Hauses, des Mannes</span></div>
<div><span>sein · werden</span><span>Nominativ again: Er ist ein guter Lehrer. Er wird Arzt.</span></div>
<div><span>Zeit</span><span>Akkusativ: jeden Tag, letzten Montag</span></div>
<div><span>es gibt</span><span>always Akkusativ: Es gibt einen Park.</span></div>
<div><span>Verb entscheidet</span><span>helfen + Dativ, but fragen + Akkusativ: Ich helfe ihm. Ich frage ihn.</span></div></div></div>
'''
rep('<div class="tc df"><h3>Alle Artikel <small>A1</small></h3>',FALL+'<div class="tc df"><h3>Alle Artikel <small>A1</small></h3>')
PF='''th:`<div class="tc df"><h3>1 · Die einfache Regel <small>A2</small></h3><p class="memo">Learn each preposition with its case. <b>Akkusativ:</b> für, durch, gegen, ohne, um. <b>Dativ:</b> mit, nach, aus, bei, von, zu, seit. Nine are two-way: position = Dativ, movement = Akkusativ.</p><p class="tline">mit <b>dem</b> Bus · für <b>den</b> Bus</p></div><div class="tc df"><h3>2 · Schritt für Schritt <small>A2–B1</small></h3><div class="rows"><div><span>1 Find the preposition</span><span>mit</span></div><div><span>2 Look up its case</span><span>always Dativ</span></div><div><span>3 Gender of the noun</span><span>der Bus → dem</span></div><div><span>4 Write it</span><span>mit <b>dem</b> Bus</span></div><div><span>Two-way: in</span><span>Wo? in <b>der</b> Schule (Dativ) · Wohin? in <b>die</b> Schule (Akkusativ)</span></div></div></div><div class="tc df"><h3>3 · Ausnahmen &amp; mehr <small>B2–C1</small></h3><div class="rows"><div><span>zu · nach</span><span>movement, but Dativ: Ich gehe zur Schule, nach Hause. At home: zu Hause.</span></div><div><span>Verb entscheidet</span><span>warten auf + Akkusativ, teilnehmen an + Dativ. The verb fixes the case, not the movement.</span></div><div><span>bis</span><span>usually with another preposition: bis zum Bahnhof, bis nach Wien.</span></div><div><span>nachgestellt</span><span>den Fluss entlang · dem Bahnhof gegenüber (gegenüber can also come first)</span></div><div><span>Genitiv</span><span>wegen des Regens. Spoken German often uses Dativ: wegen dem Regen.</span></div></div></div>'''
rep('th:`<div class="tc df"><h3>Nur Akkusativ</h3>',PF+'<div class="tc df"><h3>Nur Akkusativ</h3>')
s=re.sub(r'<meta name="app-version" content="[^"]+">','<meta name="app-version" content="2026-11-21n">',s,count=1)
open(p,"w",encoding="utf-8").write(s);print("ok")
