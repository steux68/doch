import re, sys
p="index.html"; s=open(p,encoding="utf-8").read()
if ".rcb{" in s: sys.exit("already patched")
def rep(a,b):
    global s
    assert s.count(a)==1,a[:70]
    s=s.replace(a,b)
# 1. angedockte Leisten: ab der zweiten Reihe bekommen sie oben wieder eine Punktlinie (die Leiste darüber blendet ihre untere aus)
D="repeating-linear-gradient(to right,#b8b8b8 0 1px,transparent 1px 3px)"
NF=':not([data-i="0"]):not([data-i="1"])'
a='.hb.stt.hr{background:var(--bl) left bottom/100% 1px no-repeat,var(--hv) left top/1px 100% no-repeat,#fff}'
rep(a,a+'\n.hb.stt.hl%s{background:%s left top/100%% 1px no-repeat,var(--bl) left bottom/100%% 1px no-repeat,var(--hv) right top/1px 100%% no-repeat,#fff}'%(NF,D)
      +'\n.hb.stt.hr%s{background:%s left top/100%% 1px no-repeat,var(--bl) left bottom/100%% 1px no-repeat,var(--hv) left top/1px 100%% no-repeat,#fff}'%(NF,D))
# 2. Weitermachen + Fehler: eine kleine Zeile mit zwei Feldern
rep('<button class="resume" id="resume" hidden></button>\n        <button class="errc" id="errc" hidden></button>',
    '<div class="rcb"><button class="resume" id="resume" hidden></button><button class="errc" id="errc" hidden></button></div>')
css='''
.rcb{display:grid;grid-auto-flow:column;grid-auto-columns:minmax(0,1fr);gap:4px;margin:0 0 6px}
.rcb:not(:has(button:not([hidden]))){display:none}
.rcb .resume,.rcb .errc{min-height:0;padding:6px 10px;gap:6px;min-width:0}
.rcb small{font-size:10px;letter-spacing:.1em}
.rcb b{font-size:14px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.rcb span{min-width:0;overflow:hidden}.rcb button>b:last-child{flex:none}
'''
rep('.hb.first{margin-top:14px}','.hb.first{margin-top:14px}'+css)
rep("""+(s!=null?Math.round(s*100)+' % ':'')+'→</b>'""","""+'→</b>'""")
rep("""' zum Wiederholen</b></span><b>üben →</b>'""","""'</b></span><b>→</b>'""")
rep("<small>Deine Fehler</small>","<small>Fehler üben</small>")
m=re.search(r'name="app-version" content="(\d{4}-\d\d-\d\d)([a-z]?)"',s)
s=s.replace(m.group(0),'name="app-version" content="%s%s"'%(m.group(1),chr(ord(m.group(2) or "`")+1)))
open(p,"w",encoding="utf-8").write(s); print("ok")
