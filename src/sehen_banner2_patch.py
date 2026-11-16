import re, sys
p="index.html"; s=open(p,encoding="utf-8").read()
if "sehk i s[data-i]" in s: sys.exit("already patched")
def rep(a,b):
    global s
    assert s.count(a)==1,a[:60]
    s=s.replace(a,b)
P,N,F="#e6dccb","#e4f7a0","#d3dff2"
def seg(i,bg,t): return '<s data-i="%d" style="background:%s">%s</s>'%(i,bg,t)
zt=''.join([seg(0,P,"PLQ"),seg(1,P,"PRÄT"),seg(2,"linear-gradient(90deg,%s 50%%,%s 50%%)"%(P,N),"PERF"),seg(3,N,"PRÄS"),seg(4,F,"F I"),seg(5,"linear-gradient(90deg,%s 50%%,%s 50%%)"%(F,P),"F II")])
fl=''.join([seg(0,"#e6e6e3","NOM"),seg(1,"#f4dcd8","AKK"),seg(2,"#d3def0","DAT"),seg(3,"#f5efcf","GEN")])
i=s.index('<div class="sehk" role="button" tabindex="0" data-sv="t">'); j=s.index('</div></div>',i)+len('</div></div>')
j=s.index('<div class="sehk"',i); j2=s.index('</div>',s.index('data-sv="k"'))+6
new=('<div class="sehk" role="button" tabindex="0" data-sv="t"><b>Zeiten</b><i>'+zt+'</i></div>'
     '<div class="sehk" role="button" tabindex="0" data-sv="k"><b>Fälle</b><i>'+fl+'</i></div>')
s=s[:i]+new+s[j2:]
rep(".sehg{display:grid;grid-template-columns:1fr 1fr;gap:6px}",".sehg{display:grid;grid-template-columns:3fr 2fr;gap:6px}")
rep(".sehk i{display:flex;gap:2px;height:14px;margin-bottom:4px}.sehk i s{display:block;flex:1;text-decoration:none}",
    ".sehk i{display:flex;gap:2px;height:24px;margin:0}.sehk i s{display:flex;align-items:center;justify-content:center;flex:1;min-width:0;text-decoration:none;font-style:normal;font-size:8.5px;letter-spacing:0;color:#2c2c2a;overflow:hidden;white-space:nowrap}/* sehk i s[data-i] */")
rep('const go=()=>{SV.tab=b.dataset.sv;openTopic("sehen");};','const go=e=>{const sg=e&&e.target&&e.target.closest&&e.target.closest("s");SV.tab=b.dataset.sv;if(sg&&sg.dataset.i!==undefined)SV.cur[SV.tab]=+sg.dataset.i;openTopic("sehen");};')
m=re.search(r'name="app-version" content="(\d{4}-\d\d-\d\d)([a-z]?)"',s)
s=s.replace(m.group(0),'name="app-version" content="%s%s"'%(m.group(1),chr(ord(m.group(2) or "`")+1)))
open(p,"w",encoding="utf-8").write(s); print("ok")
