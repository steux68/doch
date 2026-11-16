import re, sys
p="index.html"; s=open(p,encoding="utf-8").read()
a='<h3>Sehen</h3><p>Zeiten und Fälle auf einen Blick: wischen statt lesen.</p>'
if a not in s: sys.exit("already patched")
s=s.replace(a,'')
for x,y in [('.sehb{margin:0 0 14px;padding:10px 10px 12px;position:relative;background:#fff}','.sehb{margin:0 0 12px;padding:0;position:relative}'),
            ('.sehb::after,.sv::after{','.sv::after{')]:
    assert s.count(x)==1,x
    s=s.replace(x,y)
m=re.search(r'name="app-version" content="(\d{4}-\d\d-\d\d)([a-z]?)"',s)
s=s.replace(m.group(0),'name="app-version" content="%s%s"'%(m.group(1),chr(ord(m.group(2) or "`")+1)))
open(p,"w",encoding="utf-8").write(s); print("ok")
