import re, sys
p = "index.html"
s = open(p, encoding="utf-8").read()
if "svnb" in s:
    sys.exit("already patched")

def rep(a, b):
    global s
    assert s.count(a) == 1, a[:70]
    s = s.replace(a, b)

# CSS
rep(".svh{margin:10px 0 0;",
    ".svnb{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:2px 4px 16px;min-height:44px}"
    ".svnb [role=button]{display:block;color:#a3a3a0;cursor:pointer;padding:2px 0}"
    ".svnb .nr{display:block;font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:#e30613;opacity:.55;font-weight:700}"
    ".svnb .nt{display:block;font-size:14px;line-height:1.35;margin-top:2px}"
    ".svnb .nn{text-align:right}"
    ".svh{margin:10px 0 0;")

# markup: neighbour row directly under the track
rep("""h+='<div class="svt" id="svt"></div><div class="svi" id="svi"></div>""",
    """h+='<div class="svt" id="svt"></div><div class="svnb" id="svnb"></div><div class="svi" id="svi"></div>""")

# fill it in marks()
rep("""const x=cfg.info(i);info.innerHTML=""",
    """const nb=$("svnb");if(nb){const pl=t=>String(t).replace(/<[^>]*>/g,"");const one=(k,cls,ar)=>k<0||k>=cfg.chips.length?'<span></span>':'<span role="button" tabindex="0" class="'+cls+'" data-i="'+k+'"><span class="nr">'+(ar<0?"‹ ":"")+esc(cfg.chips[k])+(ar>0?" ›":"")+'</span><span class="nt">'+esc(pl(cfg.sent(k,sel)))+'</span></span>';nb.innerHTML=one(i-1,"nv",-1)+one(i+1,"nn",1);}
    const x=cfg.info(i);info.innerHTML=""")

# tap on a neighbour = same as chip (data-i, handled by the existing branch only for .svk) 
rep("""if(b.classList.contains("svk")){const i=+b.dataset.i;""",
    """if(b.classList.contains("svk")||b.closest("#svnb")){const i=+b.dataset.i;""")

m = re.search(r'name="app-version" content="(\d{4}-\d\d-\d\d)([a-z]?)"', s)
s = s.replace(m.group(0), 'name="app-version" content="%s%s"' % (m.group(1), chr(ord(m.group(2) or "`") + 1)))
open(p, "w", encoding="utf-8").write(s)
print("patched")
