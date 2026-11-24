#!/usr/bin/env python3
"""DOCH: letzte CSS-dotted-Rahmen -> Gradient-Rezept, gelbe Auswahl -> Lime, Linienfarbe #b8b8b8. Idempotent."""
import re, sys
p="index.html"; s=open(p,encoding="utf-8").read()
if 'id="linien-css"' in s: sys.exit("already patched")
D='repeating-linear-gradient(to right,#b8b8b8 0 1px,transparent 1px 3px)'
V='repeating-linear-gradient(to bottom,#b8b8b8 0 1px,transparent 1px 3px)'
def frame(fill): return ('border:0!important;background:'+D+' top/100% 1px no-repeat,'+D+' bottom/100% 1px no-repeat,'+V+' left/1px 100% no-repeat,'+V+' right/1px 100% no-repeat,'+fill+'!important')
def top(c=D): return 'border-top:0!important;background-image:'+c+'!important;background-size:100% 1px!important;background-position:left top!important;background-repeat:no-repeat!important'
def bot(c=D): return 'border-bottom:0!important;background-image:'+c+'!important;background-size:100% 1px!important;background-position:left bottom!important;background-repeat:no-repeat!important'
G='.app[data-mode="game"] '; T='.app[data-mode="theo"] '
R=[
 ('.qmq.n',top()),
 (G+'#panel #ans,'+G+'#panel .opt',frame('#fff')),
 (G+'#panel #chk',frame('#cdff3e')+';font-weight:700!important'),
 (G+'#panel .gap','border-bottom:0!important;background-image:repeating-linear-gradient(to right,#555 0 1px,transparent 1px 3px)!important;background-size:100% 1px!important;background-position:left bottom!important;background-repeat:no-repeat!important'),
 (T+'.tc:has(#llv),'+T+'.tc:has(#ltx),'+T+'.tc:has(#wlv),'+T+'.tc:has(#wtx),'+T+'#lres .tc,'+T+'#wres .tc',frame('rgba(255,255,255,.94)')),
 (T+'#llv button,'+T+'#wlv button',frame('#f2f2f2')),
 (T+'#llv button[aria-pressed="true"],'+T+'#wlv button[aria-pressed="true"]',frame('#cdff3e')+';font-weight:700!important'),
 (T+'#ltask,'+T+'#wtask,'+T+'#wtx',frame('#fff')),
 (T+'.lg.fld','border-bottom:0!important;background-image:repeating-linear-gradient(to right,#555 0 1px,transparent 1px 3px)!important;background-size:100% 1px!important;background-position:left bottom!important;background-repeat:no-repeat!important'),
 (T+'.lbtn button.primary,'+T+'.wrow button.primary',frame('#cdff3e')+';font-weight:700!important'),
 (G+'#gqpop',top()),
 ('#nf .wxl','border-bottom:0!important;background-image:repeating-linear-gradient(to right,#e30613 0 1px,transparent 1px 3px)!important;background-size:100% 1px!important;background-position:left bottom!important;background-repeat:repeat-x!important'),
 ('#xfer',top()),
 ('#stnT',frame('transparent')),
]
css='<style id="linien-css">\n'+"\n".join(sel+'{'+body+'}' for sel,body in R)+'\n</style>\n'
i=s.rfind('</style>'); assert i>0
j=s.index('\n',i)+1
s=s[:j]+css+s[j:]
m=re.search(r'name="app-version" content="(\d{4}-\d\d-\d\d)([a-z]?)"',s)
new=m.group(1)+chr(ord(m.group(2) or "`")+1)
s=s.replace(m.group(0),'name="app-version" content="%s"'%new)
open(p,"w",encoding="utf-8").write(s); print("OK",new)
