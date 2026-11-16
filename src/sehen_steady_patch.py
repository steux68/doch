import re, sys
p = "index.html"
s = open(p, encoding="utf-8").read()
if "const setNb=" in s:
    sys.exit("already patched")
def rep(a, b):
    global s
    assert s.count(a) == 1, a[:60]
    s = s.replace(a, b)
A='  const cols=()=>{trk.innerHTML=\'<div class="svp"></div>\'+cfg.chips.map((c,i)=>\'<div class="svcol"><p class="svs">\'+cfg.sent(i,sel)'
rep(A,
    """  const setNb=()=>{const nb=$("svnb");if(!nb||!nb.isConnected)return;const pr=document.createElement("div");pr.className="svnb";pr.style.cssText="position:absolute;left:0;right:0;top:0;visibility:hidden;min-height:0;margin:0";pr.innerHTML='<span class="nv" style="display:block;padding:2px 0"></span><span class="nn" style="display:block;padding:2px 0"></span>';root.appendChild(pr);
    let mx=44;const pl=t=>String(t).replace(/<[^>]*>/g,"");cfg.chips.forEach((c,k)=>{[0,1].forEach(j=>{pr.children[j].innerHTML='<span class="nr">'+esc(c)+'</span><span class="nt">'+esc(pl(cfg.sent(k,sel)))+'</span>';mx=Math.max(mx,pr.children[j].offsetHeight);});});
    root.removeChild(pr);nb.style.minHeight=Math.ceil(mx)+"px";};
"""+A)
rep("marks(cur);};\n  const go=", "marks(cur);setNb();};\n  const go=")
rep("window.addEventListener(\"resize\",line);\n  requestAnimationFrame", "window.addEventListener(\"resize\",()=>{line();setNb();});\n  requestAnimationFrame")
m = re.search(r'name="app-version" content="(\d{4}-\d\d-\d\d)([a-z]?)"', s)
s = s.replace(m.group(0), 'name="app-version" content="%s%s"' % (m.group(1), chr(ord(m.group(2)) + 1)))
open(p, "w", encoding="utf-8").write(s)
