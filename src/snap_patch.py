#!/usr/bin/env python3
"""Einrasten beruhigen (2026-11-21c): rastet nur noch ein, wenn man auf einen Balken ZU scrollt (nie dagegen),
und nach dem Einrasten bleibt der Balken 'gesperrt', bis man >60% Bildschirmhoehe weg ist. CSS-Proximity-Snap aus. Idempotent."""
import os
root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
p=os.path.join(root,"index.html");s=open(p,encoding="utf-8").read()
if "snap-lock" in s: print("already patched");raise SystemExit
a="#hscroll{scroll-snap-type:y proximity!important}"
assert s.count(a)==1
s=s.replace(a,"#hscroll{scroll-snap-type:none!important}")
b="var last=SC.scrollTop,dir=0,timer=0,touching=false,busy=0;"
assert s.count(b)==1
s=s.replace(b,b+"var lock=null;/*snap-lock*/")
c="P.forEach(function(p){if(p>max+2)return;var d=p-y,a=Math.abs(d);if(a<3)return;var lim=d>0?(dir>=0?.45:.18):(dir<=0?.45:.18);if(a<lim*V&&a<bd){bd=a;best=p;}});\n if(best===null)return;busy="
assert s.count(c)==1
s=s.replace(c,"P.forEach(function(p){if(p>max+2)return;var d=p-y,a=Math.abs(d);if(a<3){lock=p;return;}if(p===lock&&a<.6*V)return;var lim=d>0?(dir>0?.45:0):(dir<0?.45:0);if(a<lim*V&&a<bd){bd=a;best=p;}});\n if(best===null)return;lock=best;busy=")
d="SC.addEventListener(\"scroll\",function(){var y=SC.scrollTop;"
assert s.count(d)==1
s=s.replace(d,d+"if(lock!==null&&Math.abs(y-lock)>.6*SC.clientHeight)lock=null;")
import re
s=re.sub(r'<meta name="app-version" content="[^"]+">','<meta name="app-version" content="2026-11-21c">',s,count=1)
open(p,"w",encoding="utf-8").write(s);print("ok")
