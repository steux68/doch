import re, sys
p = "index.html"
s = open(p, encoding="utf-8").read()
if "svar" in s:
    sys.exit("already patched")

def rep(a, b):
    global s
    assert s.count(a) == 1, a[:70]
    s = s.replace(a, b)

rep(".svnb{display:grid;",
    ".svsw{position:relative;padding-top:24px}.svsw .svt{margin-top:0}"
    ".svar{position:absolute;top:36px;width:30px;height:30px;display:flex;align-items:center;justify-content:center;cursor:pointer;z-index:2;-webkit-tap-highlight-color:transparent}"
    ".svar.l{left:0}.svar.r{right:0}.svar svg{width:26px;height:26px}.svar[data-off]{opacity:0;pointer-events:none}"
    ".svt1 .svcol{opacity:0!important;min-height:50px}.svt1 .svcol.on{opacity:1!important}"
    ".svnb{display:grid;")

AR = ("'<span role=\"button\" tabindex=\"0\" class=\"svar %s\" data-st=\"%d\" aria-label=\"%s\">'"
      "+'<svg class=\"ar\" viewBox=\"-12 -12 24 24\" aria-hidden=\"true\"><path class=\"rg\" d=\"%s\"/>"
      "<path class=\"dt\" transform=\"rotate(%d)\" d=\"M5.4 0L-4.6 -4.9L-2.2 0L-4.6 4.9Z\"/></svg></span>'")
L = AR % ("l", -1, "Zurück", "M-7.88 -5.31A9.5 9.5 0 1 1 -7.88 5.31", 180)
R = AR % ("r", 1, "Weiter", "M7.88 5.31A9.5 9.5 0 1 1 7.88 -5.31", 0)

rep("""h+='<div class="svt" id="svt"></div><div class="svnb" id="svnb"></div>""",
    """h+='<div class="svsw">'+""" + L + """+'<div class="svt svt1" id="svt"></div>'+""" + R + """+'</div><div class="svnb" id="svnb"></div>""")

rep("""const nb=$("svnb");""",
    """root.querySelectorAll(".svar").forEach(a=>{const k=i+(+a.dataset.st);if(k<0||k>=cfg.chips.length)a.setAttribute("data-off","");else a.removeAttribute("data-off");});
    const nb=$("svnb");""")

rep("""if(b.classList.contains("svk")||b.closest("#svnb")){""",
    """if(b.dataset.st){const i=cur+(+b.dataset.st);if(i>=0&&i<cfg.chips.length){marks(i);go(i,true);}return;}
    if(b.classList.contains("svk")||b.closest("#svnb")){""")

# svnb arrows ‹ › removed (arrows now do that job)
rep("""(ar<0?"‹ ":"")+esc(cfg.chips[k])+(ar>0?" ›":"")""", """esc(cfg.chips[k])""")

m = re.search(r'name="app-version" content="(\d{4}-\d\d-\d\d)([a-z]?)"', s)
s = s.replace(m.group(0), 'name="app-version" content="%s%s"' % (m.group(1), chr(ord(m.group(2) or "`") + 1)))
open(p, "w", encoding="utf-8").write(s)
print("patched")
