#!/usr/bin/env python3
"""Zitate: Liste unveraendert, aber in einer Box (ca. 3,5 Zitate hoch) mit rotem Schieber im Rand rechts;
Zitat-Popup im Stil der dasein-design-Projekt-Popups: W Zaehler E oben, grosses Bild, Text mit eigenem Schieber.
Idempotent. Aus dem Repo-Stamm: python3 src/qbox_patch.py"""
f="index.html"
s=open(f,encoding="utf8").read()
if "qbox-css" in s:
    print("already patched"); raise SystemExit
def rep(old,new,n=1):
    global s
    assert s.count(old)==n,(s.count(old),old[:80])
    s=s.replace(old,new)
# 1) list in a box with slider
rep("""'<div class="qlist">'+items.join("")+'</div>'""",
    """'<div class="qbw"><div class="qbs" tabindex="0" role="region" aria-label="Zitate"><div class="qlist">'+items.join("")+'</div></div><div class="qsl" aria-hidden="true"><i></i></div></div>'""")
# 2) popup structure
rep("""p.innerHTML='<div class="tlcard"><div class="tltop"><span class="tlk" id="qk">Zitat</span><button type="button" class="tlx" id="qx" aria-label="Schließen">'+X+'</button></div><div class="tlbody" id="qb"></div><div class="qnav"><button type="button" class="rnd" id="qw" aria-label="Zurück">'+W+'</button><span class="count" id="qc"></span><button type="button" class="rnd" id="qe" aria-label="Weiter">'+EE+'</button></div></div>';""",
    """p.innerHTML='<div class="tlcard qv2"><div class="tltop"><span class="qvc"><button type="button" class="qva" id="qw" aria-label="Zurück">'+W+'</button><span class="count" id="qc"></span><button type="button" class="qva" id="qe" aria-label="Weiter">'+EE+'</button></span><button type="button" class="tlx" id="qx" aria-label="Schließen">'+X+'</button></div><span class="qsr" id="qk">Zitat</span><div class="qvimg" id="qv" aria-hidden="true"></div><div class="qvw"><div class="tlbody" id="qb"></div><div class="qsl" id="qvsl" aria-hidden="true"><i></i></div></div></div>';""")
rep("document.body.appendChild(p);\nconst items","document.body.appendChild(p);QO.upd=window.qSlider?window.qSlider($(\"qb\"),$(\"qvsl\")):null;\nconst items")
# 3) popup content
old_start=""" const im=a.querySelector("img[data-w]"),wimg=im?im.dataset.w:"";
 $("qb").innerHTML="""
assert s.count(old_start)==1
i0=s.index(old_start)
i1=s.index("""$("qb").scrollTop=0;}""",i0)+len("""$("qb").scrollTop=0;}""")
new_block=""" const im=a.querySelector("img[data-w]"),wimg=im?im.dataset.w:"",qv=$("qv");
 qv.classList.remove("has");qv.innerHTML='<i>'+E(g(".pic i"))+'</i>'+(wimg?'<img alt="" data-w="'+E(wimg)+'">':'');
 $("qb").innerHTML='<h4>'+E(g(".who"))+'</h4><p class="qq">„'+E(g("q"))+'“</p><p class="qen2">'+E(g(".qen"))+'</p><dl class="qd"><dt>Quelle</dt><dd>'+E(g("small"))+' <a class="wk" href="'+E(a.href)+'" target="_blank" rel="noopener" aria-label="Quelle öffnen: '+E(g(".who"))+'">mehr ↗</a></dd>'+(sec?'<dt>Thema</dt><dd>'+E(sec)+'</dd>':'')+'<dt>Bild</dt><dd>Wikipedia / Wikimedia Commons</dd></dl>';
 if(typeof loadPics==="function")loadPics(qv);
 $("qc").innerHTML='Zitate <b>'+(i+1)+'</b> / '+n;$("qb").scrollTop=0;if(QO.upd)QO.upd();}"""
s=s[:i0]+new_block+s[i1:]
# 4) swipe on the whole pop-up
rep("""const tb=$("qb");tb.addEventListener("touchstart",""","""const tb=p;tb.addEventListener("touchstart",""")
# 5) slider helper (global) before the qpop script
helper='''<script id="qslider-js">/* roter Schieber: duenne gepunktete Spur, roter Balken; ziehen oder antippen */
window.qSlider=function(sc,sl){var th=sl.querySelector("i"),dr=false,tH=0;
 function upd(){var h=sc.clientHeight,t=sc.scrollHeight;if(!h||t<=h+2){sl.style.visibility="hidden";return;}sl.style.visibility="visible";var H=sl.clientHeight;tH=Math.max(28,h/t*H);th.style.height=tH+"px";th.style.top=(sc.scrollTop/(t-h))*(H-tH)+"px";}
 function mv(e){var r=sl.getBoundingClientRect(),H=sl.clientHeight,t=sc.scrollHeight,h=sc.clientHeight,k=(e.clientY-r.top-tH/2)/Math.max(1,H-tH);k=Math.max(0,Math.min(1,k));sc.scrollTop=k*(t-h);}
 sl.addEventListener("pointerdown",function(e){dr=true;try{sl.setPointerCapture(e.pointerId);}catch(x){}mv(e);e.preventDefault();});
 sl.addEventListener("pointermove",function(e){if(dr)mv(e);});
 sl.addEventListener("pointerup",function(){dr=false;});sl.addEventListener("pointercancel",function(){dr=false;});
 sc.addEventListener("scroll",upd,{passive:true});window.addEventListener("resize",upd);
 if(window.ResizeObserver){var ro=new ResizeObserver(upd);ro.observe(sc);if(sc.firstElementChild)ro.observe(sc.firstElementChild);}
 upd();return upd;};
</script>
'''
css='''<style id="qbox-css">
.qbw{position:relative}
.qbs{height:min(372px,58svh);overflow-y:auto;scrollbar-width:none;overscroll-behavior-y:auto}
.qbs::-webkit-scrollbar{display:none}
.qbs:focus-visible{outline:2px solid var(--red);outline-offset:2px}
.qsl{position:absolute;top:0;bottom:0;width:14px;touch-action:none;cursor:pointer;z-index:3}
.qsl::before{content:"";position:absolute;left:6px;top:0;bottom:0;width:1px;background:repeating-linear-gradient(to bottom,#b8b8b8 0 1px,transparent 1px 3px)}
.qsl i{position:absolute;left:4px;top:0;width:5px;min-height:28px;background:var(--red)}
.qbw>.qsl{right:0;width:10px}.qbw>.qsl::before{left:7px}.qbw>.qsl i{left:5px}
.qv2 .qvc{grid-column:2;display:flex;align-items:center;gap:10px}
.qv2 .qvc .count{font-size:14px;color:#555;letter-spacing:.06em;font-variant-numeric:tabular-nums}.qv2 .qvc .count b{color:var(--red);font-weight:400}
.qv2 .qva{border:0;background:none;padding:6px;margin:-6px 0;display:flex;min-height:0;-webkit-tap-highlight-color:transparent}
.qsr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}
.qvimg{flex:none;position:relative;aspect-ratio:1/1;width:min(calc(100% - 24px),34svh);margin:0 auto 10px;background:#f4f4f2;outline:1px dotted #b8b8b8;outline-offset:-1px;display:grid;place-items:center;font-size:34px;font-weight:700;color:var(--ink);overflow:hidden}
.qvimg i{font-style:normal}
.qvimg img{position:absolute;inset:0;width:100%;height:100%;object-fit:contain;opacity:0;filter:grayscale(1)}
.qvimg.has img{opacity:1}.qvimg.has i{visibility:hidden}
.qvw{position:relative;flex:1 1 auto;min-height:0;display:flex}
.qvw .tlbody{flex:1;padding-right:24px;scrollbar-width:none}
.qvw .tlbody::-webkit-scrollbar{display:none}
.qvw>.qsl{right:6px}
.tlbody dl.qd{margin:6px 0 0;padding-top:8px;display:grid;grid-template-columns:auto 1fr;gap:3px 10px;font-size:12px;line-height:1.35;background:repeating-linear-gradient(to right,#b8b8b8 0 1px,transparent 1px 3px) left top/100% 1px no-repeat}
.tlbody dl.qd dt{color:#8a8a86}.tlbody dl.qd dd{margin:0;color:#222}
</style>
<script id="qbox-js">(function(){var root=document.getElementById("p-quotes");if(!root||!window.qSlider)return;
function setup(){var sc=root.querySelector(".qbs"),sl=root.querySelector(".qbw>.qsl");if(!sc||!sl||sc._q)return;sc._q=1;window.qSlider(sc,sl);}
new MutationObserver(setup).observe(root,{childList:true});setup();})();</script>
'''
# remove the earlier photo css (replaced)
a=s.index('<style id="qpic-css">');b=s.index('</style>',a)+len('</style>\n')
s=s[:a]+s[b:]
marker='<script id="qpop-js">'
assert s.count(marker)==1
# order: slider helper first, then pop-up, then css + box script
s=s.replace(marker,helper+marker)
end='</script>\n<script id="spiel-js">'
assert s.count(end)==1
s=s.replace(end,'</script>\n'+css+'<script id="spiel-js">')
rep('content="2026-11-13a"','content="2026-11-13b"')
open(f,"w",encoding="utf8").write(s)
print("patched")
