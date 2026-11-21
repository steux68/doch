#!/usr/bin/env python3
"""W-Fragen: Praeposition + wem/wen und Mass-Fragen; Possessivartikel-Karte in Faelle (2026-11-21l). Eigene Formulierung. Idempotent."""
import os,re
root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
p=os.path.join(root,"index.html");s=open(p,encoding="utf-8").read()
if "mein · dein · sein" in s: print("already patched");raise SystemExit
def rep(a,b):
    global s
    assert s.count(a)==1,a[:60]
    s=s.replace(a,b)
a='<div><span class="g">Welcher?</span><span>wie der</span>'
rep(a,'''<div><span class="g">Mit wem?</span><span>DAT</span><span><b>Mit wem</b> gehst du ins Kino? <b>Von wem</b> ist das Geschenk? <b>Bei wem</b> wohnst du?</span></div>
<div><span class="g">Für wen?</span><span>AKK</span><span><b>Für wen</b> ist das? <b>Gegen wen</b> spielt ihr? <b>Um wen</b> geht es?</span></div>
<div><span class="g">Wie viel?</span><span>Maß</span><span><b>Wie viel</b> kostet das? <b>Wie viele</b> Zimmer? <b>Wie oft</b>? <b>Wie spät</b> ist es?</span></div>
'''+a)
b='<div class="tc df"><h3>Verben mit Dativ <small>A2</small></h3>'
rep(b,'''<div class="tc df"><h3>mein · dein · sein <small>A2</small></h3><div class="rows">
<div><span>Who owns?</span><span>ich mein · du dein · er, es sein · sie ihr · wir unser · ihr euer · Sie Ihr</span></div>
<div><span>What is owned?</span><span>The noun decides the ending, as with ein: mein Plan · meine Lampe · meinen Plan · meinem Freund</span></div>
<div><span>Example</span><span>Er repariert <b>sein</b> Fahrrad. Sie liest <b>ihre</b> Zeitung. Sie liest <b>ihr</b> Buch.</span></div>
<div><span>euer · unser</span><span>euer drops the e before an ending: euer Zimmer, euren Plan, eure Lampe</span></div></div>
<p class="tline">The owner chooses the stem (sein or ihr), the thing owned chooses the ending. The formal Sie becomes Ihr, with a capital letter.</p></div>
'''+b)
s=re.sub(r'<meta name="app-version" content="[^"]+">','<meta name="app-version" content="2026-11-21l">',s,count=1)
open(p,"w",encoding="utf-8").write(s);print("ok")
