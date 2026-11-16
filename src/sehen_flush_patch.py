import re, sys
p = "index.html"
s = open(p, encoding="utf-8").read()
if "#theo:has(#sv){overflow-x:hidden}" in s:
    sys.exit("already patched")
def rep(a, b):
    global s
    assert s.count(a) == 1, a[:60]
    s = s.replace(a, b)
rep(".svg{display:grid;grid-template-columns:repeat(var(--n),minmax(0,1fr));gap:2px;margin:0 4px 3px}",
    ".svg{display:grid;grid-template-columns:repeat(var(--n),minmax(0,1fr));gap:2px;margin:0 0 3px}")
rep(".svi{margin:4px 4px 0}", ".svi{margin:4px 0 0}")
rep(".svar.l{left:0}.svar.r{right:0}", ".svar.l{left:6px}.svar.r{right:6px}#theo:has(#sv){overflow-x:hidden}.sv{overflow-x:clip}")
m = re.search(r'name="app-version" content="(\d{4}-\d\d-\d\d)([a-z]?)"', s)
s = s.replace(m.group(0), 'name="app-version" content="%s%s"' % (m.group(1), chr(ord(m.group(2)) + 1)))
open(p, "w", encoding="utf-8").write(s)
