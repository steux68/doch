import re, sys
p = "index.html"
s = open(p, encoding="utf-8").read()
if "const fitGrid=" in s:
    sys.exit("already patched")
def rep(a, b):
    global s
    assert s.count(a) == 1, a[:70]
    s = s.replace(a, b)
rep("  const setNb=()=>{",
    """  const fitGrid=()=>{const g=$("sgq"),t=$("theo");if(!g||!t)return;g.style.display="";if(t.scrollHeight>t.clientHeight+1)g.style.display="none";};
  const setNb=()=>{""")
rep("""root.removeChild(pr);nb.style.minHeight=Math.ceil(mx)+"px";};""",
    """root.removeChild(pr);nb.style.minHeight=Math.ceil(mx)+"px";fitGrid();};""")
rep("""requestAnimationFrame(()=>requestAnimationFrame(()=>{go(cur,false);line();}));}""",
    """requestAnimationFrame(()=>requestAnimationFrame(()=>{go(cur,false);line();fitGrid();}));}""")
m = re.search(r'name="app-version" content="(\d{4}-\d\d-\d\d)([a-z]+)"', s)
s = s.replace(m.group(0), 'name="app-version" content="%s%s"' % (m.group(1), m.group(2)[:-1] + chr(ord(m.group(2)[-1]) + 1)))
open(p, "w", encoding="utf-8").write(s)
print("ok")
