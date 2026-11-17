import re
p='index.html';s=open(p,encoding='utf8').read()
# 1) markup: percentage + track in topic tiles
a='<span class="prog"><i style="width:\'+Math.round((s||0)*100)+\'%"></i></span></button>\';}).join("")'
assert s.count(a)==1
s=s.replace(a,'<span class="prog"><span class="pk"><i style="width:\'+Math.round((s||0)*100)+\'%"></i></span><em>\'+Math.round((s||0)*100)+\' %</em></span></button>\';}).join("")')
# 2) css: replace slim block
m=re.search(r'<style id="tt-slim-css">.*?</style>\n',s,re.S);assert m
css='''<style id="cards-css">
.grp.open{background:rgba(205,255,62,.45)!important}
.grp.open .gl{gap:0!important;padding:0 0 0 0!important}
.gl .tt{background:#fff!important;min-height:52px!important;gap:6px!important;padding:8px 10px 7px!important;justify-content:space-between!important;position:relative}
.gl .tt::after{display:block!important;content:"";position:absolute;inset:0;pointer-events:none;background:repeating-linear-gradient(to right,#b8b8b8 0 1px,transparent 1px 3px) left bottom/100% 1px no-repeat,repeating-linear-gradient(to bottom,#b8b8b8 0 1px,transparent 1px 3px) right top/1px 100% no-repeat}
.gl .tt:nth-child(2n)::after{background:repeating-linear-gradient(to right,#b8b8b8 0 1px,transparent 1px 3px) left bottom/100% 1px no-repeat}
.tt .prog{display:flex;align-items:center;gap:8px;height:auto;background:none!important}
.tt .pk{flex:1;height:2px;background:#d6d6d3;position:relative}
.tt .pk i{position:absolute;left:0;top:-2px;height:6px;background:#e30613;max-width:100%}
.tt .pk i[style="width:0%"]{display:none}
.tt .prog em{font-style:normal;font-size:12px;color:#333;min-width:34px;text-align:right}
.tt .pk:has(i[style="width:0%"])+em{color:#8c918a}
</style>
'''
s=s[:m.start()]+css+s[m.end():]
s=s.replace('<meta name="app-version" content="2026-11-17s">','<meta name="app-version" content="2026-11-17t">')
open(p,'w',encoding='utf8').write(s)
