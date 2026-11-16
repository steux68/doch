import re, sys
p = "index.html"
s = open(p, encoding="utf-8").read()
if "sgsmall" in s:
    sys.exit("already patched")
# 1) replace the whole CSS block of the first grid patch
a = s.index(".sgq{width:min(100%,304px)")
b = s.index(".svsw{position:relative;")
css = (".sgq{margin:2px auto 0;display:flex;justify-content:center}"
 ".sgw{display:grid;grid-template-columns:26px 104px;/*sgsmall*/}.sgh{display:grid;grid-template-columns:repeat(4,1fr);height:15px}"
 ".sgr{display:grid;grid-template-rows:repeat(4,1fr)}.sgt{display:grid;grid-template-columns:repeat(4,1fr);grid-template-rows:repeat(4,1fr);width:104px;height:104px}"
 ".sgh span,.sgr span{font-size:9px;letter-spacing:.04em;text-transform:uppercase;color:#777;display:flex;align-items:center;justify-content:center}"
 ".sgh span.on{background:#cdff3e;color:#111;font-weight:700}.sgr span.on{color:#111;font-weight:700;box-shadow:inset 0 0 0 1px #222}"
 ".sgt div{border:1px dotted #b8b8b8;display:flex;align-items:center;justify-content:center;font-size:12px;color:#222;background:#fff}"
 ".sgt div.hit{background:#cdff3e;border:1px solid #222;font-weight:700}")
s = s[:a] + css + s[b:]
# 2) builder without label line, tidy markup
a = s.index("function svGridHTML(row,col){")
b = s.index("function renderSehen(){")
fn = '''function svGridHTML(row,col){const R=["Nom","Akk","Dat","Gen"],C=["M","N","F","Pl"],F=SVCFG.k.fills;
  return '<div class="sgw"><div></div><div class="sgh">'+C.map((c,i)=>'<span class="'+(i+1===col?"on":"")+'">'+c+'</span>').join('')+'</div>'
   +'<div class="sgr">'+R.map((r,i)=>'<span class="'+(i+1===row?"on":"")+'" style="background:'+(i+1===row?F[i]:"#fff")+'">'+r+'</span>').join('')+'</div>'
   +'<div class="sgt">'+SGT.map(t=>{const a=row>=t[1]&&row<=t[2],b=col>=t[3]&&col<=t[4];return '<div class="'+(a&&b?"hit":"")+'" style="grid-row:'+t[1]+'/'+(t[2]+1)+';grid-column:'+t[3]+'/'+(t[4]+1)+'">'+t[0]+'</div>';}).join('')+'</div></div>';}
'''
s = s[:a] + fn + s[b:]
# 3) hide the swipe hint on Fälle->Sätze (the diagram takes its place)
s = s.replace('<p class="svh">wischen · Kasten antippen</p>', '<p class="svh"'+"'+(SV.tab===\"k\"?' style=\"display:none\"':'')+'"+'>wischen · Kasten antippen</p>',1) if 'class="svh">wischen' in s else s
m = re.search(r'name="app-version" content="(\d{4}-\d\d-\d\d)([a-z]?)"', s)
s = s.replace(m.group(0), 'name="app-version" content="%s%s"' % (m.group(1), (m.group(2)+'a' if m.group(2)=='z' else chr(ord(m.group(2)) + 1))))
open(p, "w", encoding="utf-8").write(s)
print("ok")
