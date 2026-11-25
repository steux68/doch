# Zitate-Popup: Pfeile mittig auf dem Foto (wie Geschichte). 25.11.2026
import re
s=open('index.html',encoding='utf-8').read()
if 'zitate-pfeile-css' in s: raise SystemExit('schon angewendet')
a='<span class="qvc"><button type="button" class="qva" id="qw" aria-label="Zurück">\'+W+\'</button><span class="count" id="qc"></span><button type="button" class="qva" id="qe" aria-label="Weiter">\'+EE+\'</button></span>'
assert a in s
s=s.replace(a,'<span class="qvc"><span class="count" id="qc"></span></span>',1)
b='qv.classList.remove("has");qv.innerHTML=\'<i>\'+E(g(".pic i"))+\'</i>\'+(wimg?\'<img alt="" data-w="\'+E(wimg)+\'">\':\'\');'
assert b in s
s=s.replace(b,b+'qv.insertAdjacentHTML("beforeend",\'<button type="button" class="tlar pw" id="qw" aria-label="Zurück">\'+W+\'</button><button type="button" class="tlar pe" id="qe" aria-label="Weiter">\'+EE+\'</button>\');$("qw").onclick=()=>show(QO.i-1);$("qe").onclick=()=>show(QO.i+1);',1)
s=s.replace('$("qw").onclick=()=>show(QO.i-1);$("qe").onclick=()=>show(QO.i+1);\nwindow.addEventListener("popstate"','window.addEventListener("popstate"',1)
css='<style id="zitate-pfeile-css">\n.qvimg .tlar{top:50%!important;z-index:2}\n.qvimg.has .tlar,.qvimg .tlar{opacity:1!important}\n</style>\n'
i=s.rindex('</head>'); s=s[:i]+css+s[i:]
s=re.sub(r'(name="app-version" content=")[^"]*"',r'\g<1>2026-11-25c"',s,count=1)
open('index.html','w',encoding='utf-8').write(s)
