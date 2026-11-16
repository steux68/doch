import re, sys
p = "index.html"
s = open(p, encoding="utf-8").read()
if "margin:6px -4px" in s:
    sys.exit("already patched")
def rep(a, b):
    global s
    assert s.count(a) == 1, a[:60]
    s = s.replace(a, b)
rep(".sv{position:relative;margin:6px 8px;padding:14px 8px 8px;", ".sv{position:relative;margin:6px -4px;padding:14px 6px 8px;")
rep(".svar svg{width:26px;height:26px}", ".svar{border-radius:50%;background:rgba(60,62,56,.09)}.svar svg{width:30px;height:30px}.svar .rg{display:none}.svar .dt{fill:#8c918a;stroke:none}")
m = re.search(r'name="app-version" content="(\d{4}-\d\d-\d\d)([a-z]?)"', s)
s = s.replace(m.group(0), 'name="app-version" content="%s%s"' % (m.group(1), chr(ord(m.group(2)) + 1)))
open(p, "w", encoding="utf-8").write(s)
