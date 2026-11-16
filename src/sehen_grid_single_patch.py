import re, sys
p = "index.html"
s = open(p, encoding="utf-8").read()
if "sgsingle" in s:
    sys.exit("already patched")
def rep(a, b):
    global s
    assert s.count(a) == 1, a[:70]
    s = s.replace(a, b)
# one single dotted line between tiles: container draws top+left, every tile right+bottom
rep(".sgt div{border:1px dotted #b8b8b8;display:flex;align-items:center;justify-content:center;font-size:12px;color:#222;background:#fff}",
    ".sgt{border-top:1px dotted #b8b8b8;border-left:1px dotted #b8b8b8;box-sizing:content-box/*sgsingle*/}"
    ".sgt div{border:0;border-right:1px dotted #b8b8b8;border-bottom:1px dotted #b8b8b8;position:relative;display:flex;align-items:center;justify-content:center;font-size:13px;color:#222;background:#fff}"
    ".sgt div.nb{border-bottom:0}")
rep(".sgt div.hit{background:#cdff3e;border:1px solid #222;font-weight:700}",
    ".sgt div.hit{background:#cdff3e;font-weight:700;z-index:1;box-shadow:inset 0 0 0 1px #222}")
# bigger: 112 px (about 3 cm)
rep("grid-template-columns:26px 104px;", "grid-template-columns:26px 112px;")
rep("width:104px;height:104px}", "width:112px;height:112px}")
rep(".svk2 .sgw{grid-template-columns:24px 96px}.svk2 .sgt{width:96px;height:96px}",
    ".svk2 .sgw{grid-template-columns:24px 112px}.svk2 .sgt{width:112px;height:112px}")
# L-shaped der: no line between the two parts, one label
rep("""const SGT=[["der",1,1,1,1],""", """const SGT=[["der",1,1,1,1],""")
rep("""["der",3,3,3,3],["den",3,3,4,4],["der",4,4,3,4]];""", """["",3,3,3,3,"nb"],["den",3,3,4,4],["der",4,4,3,4]];""")
rep("""'<div class="'+(a&&b?"hit":"")+'" style=""", """'<div class="'+(a&&b?"hit":"")+(t[5]?" "+t[5]:"")+'" style=""")
m = re.search(r'name="app-version" content="(\d{4}-\d\d-\d\d)([a-z]+)"', s)
s = s.replace(m.group(0), 'name="app-version" content="%s%s"' % (m.group(1), m.group(2)[:-1] + chr(ord(m.group(2)[-1]) + 1)))
open(p, "w", encoding="utf-8").write(s)
print("ok")
