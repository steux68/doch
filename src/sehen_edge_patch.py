import re, sys
p = "index.html"
s = open(p, encoding="utf-8").read()
if "margin:6px 0;padding:14px 0 8px;background:rgba(255,255,255,.82)" in s:
    sys.exit("already patched")
def rep(a, b):
    global s
    assert s.count(a) == 1, a[:60]
    s = s.replace(a, b)
rep(".sv{position:relative;margin:6px -4px;padding:14px 6px 8px;background:#fff;",
    ".sv{position:relative;margin:6px 0;padding:14px 0 8px;background:rgba(255,255,255,.82);-webkit-backdrop-filter:blur(3px);backdrop-filter:blur(3px);")
rep(".svar{border-radius:50%;background:rgba(60,62,56,.09)}",
    ".svar{border-radius:50%;background:rgba(255,255,255,.82)}")
rep(".svnb{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:2px 4px 16px;",
    ".svnb{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:2px 0 16px;")
m = re.search(r'name="app-version" content="(\d{4}-\d\d-\d\d)([a-z]?)"', s)
s = s.replace(m.group(0), 'name="app-version" content="%s%s"' % (m.group(1), chr(ord(m.group(2)) + 1)))
open(p, "w", encoding="utf-8").write(s)
