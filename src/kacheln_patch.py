#!/usr/bin/env python3
"""2026-11-23r: drei Kacheln (Heute ueben / Weitermachen / Fehler ueben): Beschriftung einzeilig, Pfeil rechts unten
ausserhalb des Textes, damit Themenname nicht vom Pfeil abgeschnitten wird."""
import sys
F='/home/claude/doch/index.html'
s=open(F,encoding='utf-8').read()
if '[kacheln]' in s: print('already');sys.exit()
css='''/* [kacheln] */
.rcb .resume,.rcb .errc,.rcb .dayb{position:relative;display:block;padding:8px 8px 8px 10px;min-height:52px;text-align:left}
.rcb .resume small,.rcb .errc small,.rcb .dayb small{display:block;font-size:10px;letter-spacing:.07em;white-space:nowrap;margin:0 0 3px}
.rcb span>b,.rcb .dayb span>b{display:block;font-size:13px;line-height:1.2;padding-right:14px}
.rcb button>b:last-child{position:absolute;right:7px;bottom:8px;font-size:13px;line-height:1;padding:0}
</style>
<style id="acc-offen-css">'''
a='</style>\n<style id="acc-offen-css">'
assert s.count(a)==1
s=s.replace(a,css,1)
s=s.replace('content="2026-11-23q"','content="2026-11-23r"')
open(F,'w',encoding='utf-8').write(s);print('ok')
