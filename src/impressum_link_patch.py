#!/usr/bin/env python3
"""DOCH Titelseite: kleiner Link '§ impressum' unten links; öffnet Info & Einstellungen beim Impressum."""
import re, sys
p="index.html"; s=open(p,encoding="utf-8").read()
if "/* impressum-link */" in s: sys.exit("already patched")
a='<i class="lt"></i>eine von mehreren / regional</p>'
if s.count(a)!=1: sys.exit("Anker")
s=s.replace(a,a+'<button type="button" class="timp" id="timp">§ impressum</button>')
CSS="""/* impressum-link */
.timp{position:absolute;left:4px;bottom:1px;z-index:5;padding:2px 4px;border:0;background:none;font:inherit;font-size:12px;letter-spacing:.06em;color:#8a8a86;cursor:pointer;-webkit-tap-highlight-color:transparent}
.timp:active{color:var(--red)}
"""
k=s.rindex("</style>"); s=s[:k]+CSS+s[k:]
JS="""<script id="imp-link-js">(function(){var b=document.getElementById('timp'),c=document.getElementById('cogb');if(!b)return;
b.onclick=function(e){e.stopPropagation();if(c)c.click();setTimeout(function(){var B=document.getElementById('setb'),t=[].filter.call(B.querySelectorAll('p'),function(x){return /^Impressum:/.test(x.textContent);})[0];if(t&&B){B.scrollTop=Math.max(0,t.offsetTop-B.offsetTop-12);}},60);};})();</script>
"""
k=s.rindex("</html>") if "</html>" in s else len(s); s=s[:k]+JS+s[k:]
m=re.search(r'name="app-version" content="(\d{4}-\d\d-\d\d)([a-z]?)"',s)
s=s.replace(m.group(0),'name="app-version" content="%s%s"'%(m.group(1),chr(ord(m.group(2) or "`")+1)))
open(p,"w",encoding="utf-8").write(s); print("OK")
