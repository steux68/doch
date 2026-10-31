"""Einheitliche „mehr“-Leiste in der Deutsch-App (Vorlage: .cvb/.more aus dasein-design, in P a–x als .zmore):
zwei gepunktete Linien, roter Kreis mit Kreuz und pulsierenden Limetten-Ringen, „mehr“ dünn + rotes Stichwort, „weniger“ mit Minus.
Betrifft die Zeile „mehr Zitate“ (#qmore) und die Kapitel-Kürzungen (.mrow.capm). Die Hinweise, was verborgen ist, wandern in aria-label.
Aufruf im Repo-Hauptordner: python3 src/more_patch.py  (idempotent)"""
import re,sys
f='deutsch/index.html'; s=open(f,encoding='utf8').read()
if 'mrp{' in s: sys.exit('schon angewendet')
def cut(rule):
    global s
    assert s.count(rule)==1,rule; s=s.replace(rule,'',1)
OLD=['.mrow b{color:var(--red)}','.mrow small{font-size:.75rem;color:var(--muted)}',
 '.mrow .pl{flex:none;width:26px;height:26px;overflow:visible;border-radius:50%;box-shadow:0 0 0 4px #e6f7a8}',
 '.mrow .pl circle{fill:#fff;stroke:var(--red);stroke-width:1.2}','.mrow .pl path{fill:none;stroke:var(--red);stroke-width:1.4;stroke-linecap:round}',
 '.mrow.capm{margin:0;align-items:flex-start;padding-top:9px;background:var(--df) left top/100% 1px no-repeat,#fff}',
 '.mrow.capm:is(.p-links,.p-hist,.p-home){background:var(--df) left top/100% 1px no-repeat,#f4f4f2}',
 '.mrow:active{background:var(--df) left top/100% 1px no-repeat,var(--lime)}']
for r in OLD: cut(r)
first='.mrow{display:flex;align-items:center;gap:12px;width:100%;min-height:44px;margin:-1px 0 0;padding:6px 10px;border:0;border-radius:0;background:var(--df) left top/100% 1px no-repeat;font:inherit;font-size:1rem;font-weight:400;color:#000;text-align:left;-webkit-tap-highlight-color:transparent}'
assert s.count(first)==1
L2='var(--df) left top/100% 1px no-repeat,var(--df) left 29px/100% 1px no-repeat'
NEW=('.mrow{display:flex;align-items:center;gap:7px;width:100%;height:30px;margin:8px 0 0;padding:0 2px;border:0;border-radius:0;font:inherit;font-size:14px;font-weight:400;letter-spacing:.04em;color:inherit;text-align:left;cursor:pointer;-webkit-tap-highlight-color:transparent;'
 'background:var(--df) left top/100% 1px no-repeat,var(--df) left bottom/100% 1px no-repeat}'
 '.mrow>span{line-height:20px}.mrow b{color:var(--red);font-weight:700;font-size:15px;margin-left:-3px}.mrow .cvt{color:#000;font-weight:300;font-size:13px}'
 '.mrow .pl{flex:none;width:20px;height:20px;overflow:visible}.mrow .pl .c{fill:#fff;stroke:var(--red);stroke-width:1.5}.mrow .pl path{fill:none;stroke:var(--red);stroke-width:1.6;stroke-linecap:round}'
 '.mrow .pl .r1,.mrow .pl .r2{fill:none;stroke:#cdff3e;stroke-width:2.2;transform-box:fill-box;transform-origin:center;animation:mrp 1.8s ease-out infinite}.mrow .pl .r2{animation-delay:.9s}'
 '@keyframes mrp{0%{transform:scale(1);opacity:.95}100%{transform:scale(1.9);opacity:0}}@media (prefers-reduced-motion:reduce){.mrow .pl .r1,.mrow .pl .r2{animation:none}}'
 '.mrow.capm{height:auto;min-height:30px;margin:0;align-items:flex-start;padding-top:5px;background:'+L2+',#fff}'
 '.mrow.capm:is(.p-links,.p-hist,.p-home){background:'+L2+',#f4f4f2}')
s=s.replace(first,NEW,1)
# Symbole
a='const PLUS=\'<svg class="pl" viewBox="-12 -12 24 24" aria-hidden="true"><circle r="10.5"/><path d="M-5.5 0H5.5M0 -5.5V5.5"/></svg>\';'
b='const MINUS=\'<svg class="pl" viewBox="-12 -12 24 24" aria-hidden="true"><circle r="10.5"/><path d="M-5.5 0H5.5"/></svg>\';'
assert s.count(a)==1 and s.count(b)==1
s=s.replace(a,'const PLUS=\'<svg class="pl" viewBox="-12 -12 24 24" aria-hidden="true"><circle class="r1" r="8"/><circle class="r2" r="8"/><circle class="c" r="8"/><path d="M0 -4.2V4.2"/><path d="M-4.2 0H4.2"/></svg>\';',1)
s=s.replace(b,'const MINUS=\'<svg class="pl" viewBox="-12 -12 24 24" aria-hidden="true"><circle class="c" r="8"/><path d="M-4.2 0H4.2"/></svg>\';',1)
# Texte
a="<span>mehr <b>Zitate</b> <small>(+'+hid+')</small></span></button>"
assert s.count(a)==1; s=s.replace(a,"<span class=\"cvt\">mehr</span><b>Zitate</b></button>",1)
a="""m.innerHTML=PLUS+'<span>mehr <b>'+esc(name)+'</b> <small>'+(hid.length?esc(hid.slice(0,3).join(" · "))+(hid.length>3?" …":""):rows?"(+"+rows+")":"")+'</small></span>';}"""
assert s.count(a)==1
s=s.replace(a,"""const hint=hid.length?hid.slice(0,3).join(" · ")+(hid.length>3?" …":""):rows?"+"+rows:"";m.setAttribute("aria-label","Mehr "+name+(hint?": "+hint:""));m.innerHTML=PLUS+'<span class="cvt">mehr</span><b>'+esc(name)+'</b>';}""",1)
a="""m.innerHTML=MINUS+'<span>weniger <b>'+esc(name)+'</b></span>';return;"""
assert s.count(a)==1
s=s.replace(a,"""m.setAttribute("aria-label","Weniger "+name);m.innerHTML=MINUS+'<span class="cvt">weniger</span><b>'+esc(name)+'</b>';return;""",1)
# Version
mm=re.search(r'(<meta name="app-version" content=")(\d{4}-\d{2}-\d{2})([a-z]+)(">)',s); assert mm
nv=mm.group(3)[:-1]+chr(ord(mm.group(3)[-1])+1)
s=s.replace(mm.group(0),mm.group(1)+mm.group(2)+nv+mm.group(4),1)
open(f,'w',encoding='utf8').write(s); print('ok',mm.group(2)+mm.group(3),'->',mm.group(2)+nv)
