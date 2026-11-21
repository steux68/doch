#!/usr/bin/env python3
"""Adjektivendungen: Theorie in drei Stufen (2026-11-21j): 1 einfache Regel, 2 Schritt fuer Schritt, 3 Ausnahmen. Neue Karten vor den Tabellen. Idempotent."""
import os,re
root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
p=os.path.join(root,"index.html");s=open(p,encoding="utf-8").read()
if "1 · Die einfache Regel" in s: print("already patched");raise SystemExit
a='const TH_ADJ=`\n<div class="tc df"><h3>Nach der · die · das</h3>'
assert s.count(a)==1
new='''const TH_ADJ=`
<div class="tc df"><h3>1 · Die einfache Regel <small>A2</small></h3><p class="memo">Look at the word before the adjective. If it already shows the case (der, den, dem, diesem …), the adjective ends in <b>-e</b> or <b>-en</b>. If nothing shows the case, the adjective shows it.</p><p class="tline">Most endings are -en. der neu<b>e</b> Plan · mit dem neu<b>en</b> Plan · mit frisch<b>em</b> Brot</p></div>
<div class="tc df"><h3>2 · Schritt für Schritt <small>A2–B1</small></h3><div class="rows">
<div><span>Nom. m.</span><span>der neu<b>e</b> Plan: der shows the case → -e</span></div>
<div><span>Akk. m.</span><span>Ich sehe den neu<b>en</b> Plan: den shows it → -en</span></div>
<div><span>Nom. m.</span><span>ein neu<b>er</b> Plan: ein shows nothing → the adjective does: -er</span></div>
<div><span>Dat. n.</span><span>mit frisch<b>em</b> Brot: no article → -em</span></div></div><p class="tline">Ask in this order: gender, case, does the article show it?</p></div>
<div class="tc df"><h3>3 · Ausnahmen &amp; mehr <small>B2–C1</small></h3><div class="rows">
<div><span>alle · diese · keine</span><span>plural: -en. alle neu<b>en</b> Pläne</span></div>
<div><span>viele · einige · wenige</span><span>like without article: viele neu<b>e</b> Pläne</span></div>
<div><span>-el · -er · -en · hoch</span><span>the e drops: ein dunkl<b>es</b> Zimmer · ein teur<b>es</b> Auto · ein hoh<b>es</b> Haus</span></div>
<div><span>two adjectives</span><span>same ending: ein groß<b>er</b>, neu<b>er</b> Plan</span></div>
<div><span>as a noun</span><span>der Deutsch<b>e</b> · ein Deutsch<b>er</b> · das Gut<b>e</b></span></div>
<div><span>unchanged</span><span>ein rosa Kleid · lila</span></div></div></div>
<div class="tc df"><h3>Nach der · die · das</h3>'''
s=s.replace(a,new)
s=re.sub(r'<meta name="app-version" content="[^"]+">','<meta name="app-version" content="2026-11-21j">',s,count=1)
open(p,"w",encoding="utf-8").write(s);print("ok")
