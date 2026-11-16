import re, sys
p = "index.html"
s = open(p, encoding="utf-8").read()
if "svGridHTML" in s:
    sys.exit("already patched")
def rep(a, b):
    global s
    assert s.count(a) == 1, a[:70]
    s = s.replace(a, b)

# CSS
rep(".svsw{position:relative;",
    ".sgq{width:min(100%,304px);margin:14px auto 6px}.sgq .sgl{color:#e30613;font-weight:700;letter-spacing:.12em;text-transform:uppercase;font-size:11px;margin:0 0 6px}"
    ".sgw{display:grid;grid-template-columns:34px 1fr}.sgh{display:grid;grid-template-columns:repeat(4,1fr);height:22px}"
    ".sgr{display:grid;grid-template-rows:repeat(4,1fr)}.sgt{display:grid;grid-template-columns:repeat(4,1fr);grid-template-rows:repeat(4,1fr);aspect-ratio:1/1}"
    ".sgh span,.sgr span{font-size:10px;letter-spacing:.08em;text-transform:uppercase;color:#777;display:flex;align-items:center}.sgh span{justify-content:center;padding-bottom:3px}"
    ".sgh span.on,.sgr span.on{color:#222;font-weight:700}"
    ".sgt div{border:1px dotted #b8b8b8;display:flex;align-items:center;justify-content:center;font-size:20px;color:#9a9a96;background:#fff}"
    ".sgt div.ln{background:#f2fbd0;color:#333}.sgt div.hit{background:#cdff3e;color:#111;border:1px solid #222;font-weight:500}"
    ".svsw{position:relative;")

# engine: grid builder, placed before renderSehen
rep("function renderSehen(){",
    """const SGT=[["der",1,1,1,1],["den",2,2,1,1],["das",1,2,2,2],["die",1,2,3,4],["dem",3,3,1,2],["des",4,4,1,2],["der",3,3,3,3],["den",3,3,4,4],["der",4,4,3,4]];
function svGridHTML(row,col){const R=["Nom.","Akk.","Dat.","Gen."],C=["Mask.","Neut.","Fem.","Plur."],F=SVCFG.k.fills;
  return '<p class="sgl">Artikel</p><div class="sgw"><div></div><div class="sgh">'+C.map((c,i)=>'<span class="'+(i+1===col?"on":"")+'">'+c+'</span>').join('')+'</div>'
   +'<div class="sgr">'+R.map((r,i)=>'<span class="'+(i+1===row?"on":"")+'" style="background:'+F[i]+';padding-left:3px">'+r+'</span>').join('')+'</div>'
   +'<div class="sgt">'+SGT.map(t=>{const a=row>=t[1]&&row<=t[2],b=col>=t[3]&&col<=t[4];return '<div class="'+(a&&b?"hit":(a||b?"ln":""))+'" style="grid-row:'+t[1]+'/'+(t[2]+1)+';grid-column:'+t[3]+'/'+(t[4]+1)+'">'+t[0]+'</div>';}).join('')+'</div></div>';}
function renderSehen(){""")

# container under the info band (only Fälle)
rep("""<div class="svi" id="svi"></div><p class="svh">""",
    """<div class="svi" id="svi"></div>'+(SV.tab==="k"?'<div class="sgq" id="sgq"></div>':'')+'<p class="svh">""")

# refresh inside marks()
rep("""    const x=cfg.info(i);info.innerHTML=""",
    """    const gq=$("sgq");if(gq)gq.innerHTML=svGridHTML(i+1,[1,3,2,4][sel[1]]);
    const x=cfg.info(i);info.innerHTML=""")

m = re.search(r'name="app-version" content="(\d{4}-\d\d-\d\d)([a-z]?)"', s)
s = s.replace(m.group(0), 'name="app-version" content="%s%s"' % (m.group(1), chr(ord(m.group(2)) + 1)))
open(p, "w", encoding="utf-8").write(s)
