import re, sys
p = "index.html"
s = open(p, encoding="utf-8").read()
if "svglue" in s:
    sys.exit("already patched")
def rep(a, b, cnt=1):
    global s
    assert s.count(a) == cnt, (s.count(a), a[:70])
    s = s.replace(a, b)

# ---- CSS: one shared thin dotted line (1px dots every 3px, #b8b8b8 = var(--df)/--dfv), no gaps, no black frames
rep(".svg{display:grid;grid-template-columns:repeat(var(--n),minmax(0,1fr));gap:2px;margin:0 0 3px}",
    ".svg{display:grid;grid-template-columns:repeat(var(--n),minmax(0,1fr));gap:0;margin:0}")
rep(".fr::after{content:\"\";position:absolute;inset:0;pointer-events:none;background:var(--df) left top/100% 1px no-repeat,var(--df) left bottom/100% 1px no-repeat,var(--dfv) left top/1px 100% no-repeat,var(--dfv) right top/1px 100% no-repeat}",
    ".fr::after{content:\"\";position:absolute;inset:0;pointer-events:none;background:var(--df) left bottom/100% 1px no-repeat,var(--dfv) right top/1px 100% no-repeat}"
    ".fr.fnr::after{background:var(--df) left bottom/100% 1px no-repeat}"
    ".fr::before{content:\"\";position:absolute;inset:0;pointer-events:none}"
    ".fr.ft::before{background:var(--df) left top/100% 1px no-repeat}.fr.fl::before{background:var(--dfv) left top/1px 100% no-repeat}"
    ".fr.ft.fl::before{background:var(--df) left top/100% 1px no-repeat,var(--dfv) left top/1px 100% no-repeat}/*svglue*/")
rep(".fr.on::after{display:none}", "")
rep(".svb.on{border-color:#000;color:#2c2c2a}", ".svb.on{color:#2c2c2a;font-weight:700}")
rep(".svti{justify-content:flex-start;padding:0 8px;margin-bottom:3px;font-weight:700;letter-spacing:.12em;border-color:#000}",
    ".svti{justify-content:flex-start;padding:0 8px;margin-bottom:0;font-weight:700;letter-spacing:.12em}"
    ".svti::after{content:\"\";position:absolute;inset:0;pointer-events:none;background:var(--df) left top/100% 1px no-repeat,var(--df) left bottom/100% 1px no-repeat,var(--dfv) left top/1px 100% no-repeat,var(--dfv) right top/1px 100% no-repeat}")
# the small article diagram: same lines, fill instead of black outline
a = s.index(".sgt{border-top:1px dotted")
b = s.index(".sgt div.hit.sgL:not(.nb){")
b = s.index("}", b) + 1
s = s[:a] + (
    ".sgt{background:var(--df) left top/100% 1px no-repeat,var(--dfv) left top/1px 100% no-repeat}"
    ".sgt div{border:0;position:relative;display:flex;align-items:center;justify-content:center;font-size:13px;color:#222;background:var(--dfv) right top/1px 100% no-repeat,var(--df) left bottom/100% 1px no-repeat #fff}"
    ".sgt div.nb{background:var(--dfv) right top/1px 100% no-repeat #fff}"
    ".sgt div.hit{background-color:#cdff3e;font-weight:700}") + s[b:]
rep(".sgh span.on{background:#cdff3e;color:#111;font-weight:700}.sgr span.on{color:#111;font-weight:700;box-shadow:inset 0 0 0 1px #222}",
    ".sgh span.on{background:#cdff3e;color:#111;font-weight:700}.sgr span.on{color:#111;font-weight:700}")

# ---- JS: draw each shared line once (top/left only where no chip lies above/left; none at the frame edges)
rep("function renderSehen(){",
    """function svGlue(){const sv=document.getElementById("sv");if(!sv)return;const S=sv.getBoundingClientRect(),cs=[...sv.querySelectorAll(".fr")];
  const R=cs.map(c=>c.getBoundingClientRect()),ov=(a,b,c,d)=>Math.min(b,d)-Math.max(a,c)>1;
  cs.forEach((c,i)=>{const r=R[i];let up=false,lf=false;R.forEach((q,j)=>{if(i===j)return;if(Math.abs(q.bottom-r.top)<1.6&&ov(q.left,q.right,r.left,r.right))up=true;if(Math.abs(q.right-r.left)<1.6&&ov(q.top,q.bottom,r.top,r.bottom))lf=true;});
   c.classList.toggle("ft",!up);c.classList.toggle("fl",!lf&&r.left>S.left+2);c.classList.toggle("fnr",r.right>=S.right-2);});}
function renderSehen(){""")
m = re.search(r'name="app-version" content="(\d{4}-\d\d-\d\d)([a-z]+)"', s)
s = s.replace(m.group(0), 'name="app-version" content="%s%s"' % (m.group(1), m.group(2)[:-1] + chr(ord(m.group(2)[-1]) + 1)))
open(p, "w", encoding="utf-8").write(s)
print("ok")
