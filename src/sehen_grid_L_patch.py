import re, sys
p = "index.html"
s = open(p, encoding="utf-8").read()
if "sgL" in s:
    sys.exit("already patched")
def rep(a, b):
    global s
    assert s.count(a) == 1, a[:70]
    s = s.replace(a, b)
rep("""["",3,3,3,3,"nb"],["den",3,3,4,4],["der",4,4,3,4]];""", """["",3,3,3,3,"nb","sgL"],["den",3,3,4,4],["der",4,4,3,4,"","sgL"]];""")
rep("""SGT.map(t=>{const a=row>=t[1]&&row<=t[2],b=col>=t[3]&&col<=t[4];return '<div class="'+(a&&b?"hit":"")""",
    """SGT.map((t,i)=>{const g=t[6]||("i"+i),on=SGT.some((u,j)=>(u[6]||("i"+j))===g&&row>=u[1]&&row<=u[2]&&col>=u[3]&&col<=u[4]);return '<div class="'+(on?"hit":"")""")
m = re.search(r'name="app-version" content="(\d{4}-\d\d-\d\d)([a-z]+)"', s)
s = s.replace(m.group(0), 'name="app-version" content="%s%s"' % (m.group(1), m.group(2)[:-1] + chr(ord(m.group(2)[-1]) + 1)))
open(p, "w", encoding="utf-8").write(s)
print("ok")
