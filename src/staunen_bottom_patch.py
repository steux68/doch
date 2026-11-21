#!/usr/bin/env python3
"""2026-11-21ad: Staunen – Zitate/Redewendungen/Geschichte bars at the bottom (above the Studieren bar); content fills the space above and slides up on switch. Idempotent."""
import os,re
root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
p=os.path.join(root,"index.html");s=open(p,encoding="utf-8").read()
if 'id="stn-bottom-css"' in s: print("already");raise SystemExit
blk='''
<style id="stn-bottom-css">
html[data-dmode="s"] #hscroll>.hb[data-i="0"]{order:11}
html[data-dmode="s"] #hscroll>.hb[data-i="1"]{order:12}
html[data-dmode="s"] #hscroll>.hb[data-i="2"]{order:13}
html[data-dmode="s"] #hscroll>.hb[data-i="3"]{order:20;margin-top:12px!important}
html[data-dmode="s"] #hscroll>.capm{order:9!important}
html[data-dmode="s"] #hscroll>.hb{margin:0 0 -1px 0!important}
@keyframes stnUp{from{opacity:0;transform:translateY(18px)}to{opacity:1;transform:none}}
html[data-dmode="s"] #hscroll.stn-go #p-quotes>.tc,html[data-dmode="s"] #hscroll.stn-go #p-rede>.tc,html[data-dmode="s"] #hscroll.stn-go #p-hist>.tc{animation:stnUp .32s ease-out}
@media (prefers-reduced-motion:reduce){html[data-dmode="s"] #hscroll.stn-go .tc{animation:none!important}}
</style>
<script id="stn-bottom-js">(function(){if(typeof DMODE==="undefined"||DMODE!=="s")return;var sc=document.getElementById("hscroll");if(!sc)return;
document.querySelectorAll("#hscroll>.hb").forEach(function(b){b.addEventListener("click",function(){sc.classList.remove("stn-go");void sc.offsetWidth;sc.classList.add("stn-go")})});})();</script>
'''
s=s.rstrip("\n")+"\n"+blk
s=re.sub(r'<meta name="app-version" content="[^"]+">','<meta name="app-version" content="2026-11-21ad">',s,count=1)
open(p,"w",encoding="utf-8").write(s);print("ok")
