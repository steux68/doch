# Geschichte-Popup: Pfeile mittig auf dem Foto (wie PASSAGE). 25.11.2026
import re
s=open('index.html',encoding='utf-8').read()
if '.tlfig .tlar{top:50%!important}' not in s:
    s=s.replace('.tlpop .tlar svg{width:22px;height:22px}\n','.tlpop .tlar svg{width:22px;height:22px}\n.tlfig .tlar{top:50%!important}\n',1)
    s=re.sub(r'(name="app-version" content=")[^"]*"',r'\g<1>2026-11-25b"',s,count=1)
    open('index.html','w',encoding='utf-8').write(s)
