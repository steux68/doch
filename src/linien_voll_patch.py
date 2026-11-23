#!/usr/bin/env python3
"""2026-11-23q: fehlende Punktlinien (Reiter Lernen/Spiel/Theorie oben+unten, Verb/Form oben in der Regler-Karte)
und die leere alte Karte "Regler" unter der Regler-Karte entfernt (zwei Zusatzlinien + Wort "Regler")."""
import sys
F='/home/claude/doch/index.html'
s=open(F,encoding='utf-8').read()
if '[linien-voll]' in s: print('already');sys.exit()
css='''/* [linien-voll] */
.seg button:not([aria-pressed="true"]){background:var(--df) left top/100% 1px no-repeat,var(--df) left bottom/100% 1px no-repeat,repeating-linear-gradient(to bottom,#b8b8b8 0 1px,transparent 1px 3px) left top/1px 100% no-repeat,#f2f2f2}
.seg button:first-child:not([aria-pressed="true"]){background:var(--df) left top/100% 1px no-repeat,var(--df) left bottom/100% 1px no-repeat,#f2f2f2}
.seg button:active:not([aria-pressed="true"]){background:var(--hl),var(--lime)}
.rgc .snctl{background:var(--df) left top/100% 1px no-repeat,var(--dfv) left top/1px 100% no-repeat}
#gqpop:has(#stage .rgc) #panel{display:none}
</style>
<style id="acc-offen-css">'''
a='</style>\n<style id="acc-offen-css">'
assert s.count(a)==1
s=s.replace(a,css,1)
s=s.replace('<meta name="app-version" content="2026-11-23p">','<meta name="app-version" content="2026-11-23q">')
open(F,'w',encoding='utf-8').write(s);print('ok')
