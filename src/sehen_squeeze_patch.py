import re, sys
p = "index.html"
s = open(p, encoding="utf-8").read()
if "svk2" in s:
    sys.exit("already patched")
def rep(a, b):
    global s
    assert s.count(a) == 1, a[:70]
    s = s.replace(a, b)
rep("""let h='<div class="sv" id="sv"><div class="svg" style="--n:2"><span role="button" tabindex="0" class="svb svo fr'+(SV.tab==="t"?' on':'')""",
    """let h='<div class="sv'+(SV.tab==="k"?' svk2':'')+'" id="sv"><div class="svg" style="--n:2"><span role="button" tabindex="0" class="svb svo fr'+(SV.tab==="t"?' on':'')""")
rep(".svsw{position:relative;",
    ".svk2 .svb{height:24px}.svk2 .svr{height:25px}.svk2 .svsw{padding-top:12px}.svk2 .svar{top:24px}.svk2 .svnb{margin-bottom:4px;gap:8px}"
    ".svk2 .svnb .nt{font-size:12.5px;line-height:1.25;margin-top:1px}.svk2 .svnb .nr{font-size:10px}"
    ".svk2 .sgw{grid-template-columns:24px 96px}.svk2 .sgt{width:96px;height:96px}.svk2 .sgh{height:13px}.svk2 .sgq{margin-top:0}"
    ".svsw{position:relative;")
m = re.search(r'name="app-version" content="(\d{4}-\d\d-\d\d)([a-z]+)"', s)
s = s.replace(m.group(0), 'name="app-version" content="%s%s"' % (m.group(1), m.group(2)[:-1] + chr(ord(m.group(2)[-1]) + 1)))
open(p, "w", encoding="utf-8").write(s)
print("ok")
