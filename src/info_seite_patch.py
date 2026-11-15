#!/usr/bin/env python3
"""DOCH: '§ impressum'-Link entfällt; stattdessen 'Info' im senkrechten Credit wie bei PASSAGE; Impressum mit eigener Überschrift."""
import re, sys
p="index.html"; s=open(p,encoding="utf-8").read()
if "/* info-seite */" in s: sys.exit("already patched")
def rep(old,new):
    global s
    if s.count(old)!=1: sys.exit("Anker: "+old[:60])
    s=s.replace(old,new)
rep('<button type="button" class="timp" id="timp">§ impressum</button>','')
i=s.index('<script id="imp-link-js">'); j=s.index('</script>',i)+9; s=s[:i]+s[j:]
rep('<span>© Steuart JM HARRISON (steux)</span>','<span>© Steuart JM HARRISON (steux)</span><button type="button" class="ilink" id="infoLink">Info</button>')
CSS="""/* info-seite */
.ilink{margin:0;padding:2px 4px;font:inherit;font-size:12px;color:var(--muted);text-decoration:underline;background:none;border:0;cursor:pointer;-webkit-tap-highlight-color:transparent}
footer.copy .ilink{pointer-events:auto}
"""
k=s.rindex("</style>"); s=s[:k]+CSS+s[k:]
rep('const im=document.createElement("p");im.className="tline";im.innerHTML="<b>Impressum:</b> Medieninhaber',
    'const ih2=document.createElement("p");ih2.className="ih";ih2.id="impH";ih2.textContent="Impressum";B.appendChild(ih2);const im=document.createElement("p");im.className="tline";im.innerHTML="Medieninhaber')
JS="""<script id="info-link-js">(function(){var l=document.getElementById('infoLink'),c=document.getElementById('cogb');if(l)l.onclick=function(e){e.stopPropagation();if(c)c.click();};})();</script>
"""
k=s.rindex("</html>") if "</html>" in s else len(s); s=s[:k]+JS+s[k:]
m=re.search(r'name="app-version" content="(\d{4}-\d\d-\d\d)([a-z]?)"',s)
s=s.replace(m.group(0),'name="app-version" content="%s%s"'%(m.group(1),chr(ord(m.group(2) or "`")+1)))
open(p,"w",encoding="utf-8").write(s); print("OK")
