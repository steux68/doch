# Filterboxen einheitlich wie PASSAGE "Pferdewissen" (grau, fett, 14 px, 32 px, 2 px Abstand, aktiv lime)
# + Redewendungen: kompakte Zeilen grau/weiss im Wechsel, Antippen klappt auf (kein EN-Knopf). 19.11.2026.
import re, sys
VER = sys.argv[1]
s = open('index.html', encoding='utf-8').read()
if '/* fbx */' in s:
    print('schon angewendet'); sys.exit(0)

# 1) Redewendungen: Zeile antippbar
a = s.index('function rwRow(r,i){')
b = s.index('function rwHTML(){')
NEWROW = '''function rwRow(r,i){const has=!!r[6];
  return '<div class="rwi" role="button" tabindex="0" aria-expanded="false" aria-controls="rwe'+i+'"><span class="rwt"><b class="rwp">'+esc(r[2])+'</b><span class="rwl">'+r[1]+'</span></span><span class="rwd">'+esc(r[3])+'</span>'+
  '<span class="rwe" id="rwe'+i+'" hidden><span class="rwen">EN</span> '+esc(r[4])+'<i>'+esc(r[5])+'</i>'+(has?'<span class="rwo">'+esc(r[6])+(r[7]?' <a class="wk" href="'+r[7][0]+'" target="_blank" rel="noopener" aria-label="Mehr bei '+r[7][1]+'" title="'+r[7][1]+'">mehr ↗</a>':'')+'</span>':'')+'</span></div>';}
'''
s = s[:a] + NEWROW + s[b:]
old = '''P.querySelectorAll("button.rwb").forEach(b=>{b.onclick=()=>{const e=document.getElementById(b.getAttribute("aria-controls")),o=b.getAttribute("aria-expanded")==="true";b.setAttribute("aria-expanded",o?"false":"true");e.hidden=o;};});'''
old = '''P.querySelectorAll("button.rwb").forEach(b=>b.onclick=()=>{const e=document.getElementById(b.getAttribute("aria-controls")),o=b.getAttribute("aria-expanded")==="true";b.setAttribute("aria-expanded",o?"false":"true");e.hidden=o;});'''
assert old in s
new = '''P.querySelectorAll(".rwi").forEach(b=>{const tg=ev=>{if(ev.target.closest&&ev.target.closest("a"))return;const e=document.getElementById(b.getAttribute("aria-controls")),o=b.getAttribute("aria-expanded")==="true";b.setAttribute("aria-expanded",o?"false":"true");e.hidden=o;};b.onclick=tg;b.onkeydown=ev=>{if(ev.key==="Enter"||ev.key===" "){ev.preventDefault();tg(ev);}};});'''
s = s.replace(old, new)
s = s.replace('Stufe rechts: B1 bis C1. „EN“ zeigt Englisch und einen Beispielsatz.', 'Stufe rechts: B1 bis C1. Antippen zeigt Englisch und einen Beispielsatz.')

# 2) CSS
CSS = '''
/* fbx */
.wchips,.qchips{display:grid!important;grid-template-columns:repeat(3,minmax(0,1fr));gap:2px!important;padding:2px 0 8px;margin:0}
#llv,#wlv,#lvs,#lvs2,.tlen2{display:grid!important;grid-auto-flow:column;grid-auto-columns:minmax(0,1fr);grid-template-columns:none;gap:2px!important;height:auto!important;width:100%}
.wchips button,.lvb,.tlen2 button{background:#ebebeb!important;color:#222;padding:6px 8px!important;min-height:32px!important;font-size:14px!important;font-weight:700!important;line-height:1.2;text-align:left;border:0!important;border-radius:0!important;box-shadow:none!important;min-width:0}
.wchips button[aria-pressed="true"],.lvb[aria-pressed="true"],.tlen2 button[aria-pressed="true"]{background:#cdff3e!important}
/* Redewendungen: kompakte Zeilen, grau/weiss im Wechsel, Text buendig mit dem Text der Filterboxen (8 px) */
.hp .rwlist{display:flex;flex-direction:column}
.hp .rwi{padding:6px 8px 7px!important;line-height:1.25;cursor:pointer;background:transparent!important}
.hp .rwlist .rwi:nth-child(odd){background:#fff!important}
.hp .rwi .rwp{font-size:16px}
.hp .rwi .rwd{font-size:14px;margin-top:1px}
.hp .rwi .rwe{margin-top:5px;padding-top:5px;font-size:14px}
.hp .rwi .rwen{font-size:11px;font-weight:700;letter-spacing:.08em;color:#e30613;margin-right:2px}
'''
i = s.rindex('</style>'); s = s[:i] + CSS + s[i:]
s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1)+VER+m.group(3), s, count=1)
open('index.html','w',encoding='utf-8').write(s); print('ok')
