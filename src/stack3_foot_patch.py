# 20.11.2026: Das Ende beider Modi (STUDIEREN und STAUNEN) zeigt Urheber-Zeile, Info-Knopf und Impressum
# (vorher war der Abschnitt hinter dem letzten Balken leer). Idempotent.
import re, sys
s = open('index.html', encoding='utf-8').read()
if 'id="stack3-foot"' in s:
    print('schon vorhanden'); sys.exit(0)
CSS = '''<style id="stack3-foot-css">
.endblk{padding:20px 0 56px}
.endblk .ucr{margin:0 0 14px}
.endblk .endinfo{display:block;width:100%;height:25px;margin:0 0 14px;padding:0;border:0;background:#f2f2f2;color:#222;font:inherit;font-size:12px;letter-spacing:1.6px;text-transform:uppercase;text-align:left;position:relative}
.endblk .endinfo::after{content:"";position:absolute;inset:0;pointer-events:none;background:repeating-linear-gradient(to right,#b8b8b8 0 1px,transparent 1px 3px) left top/100% 1px no-repeat,repeating-linear-gradient(to right,#b8b8b8 0 1px,transparent 1px 3px) left bottom/100% 1px no-repeat}
</style>
'''
JS = '''<script id="stack3-foot">(function(){const $=id=>document.getElementById(id),sb=$("setb");if(!sb)return;
const cr=sb.querySelector(".ucr"),imp=$("impH");
function mk(sec){if(!sec)return;const w=document.createElement("div");w.className="endblk";
 if(cr)w.appendChild(cr.cloneNode(true));
 const b=document.createElement("button");b.type="button";b.className="endinfo";b.textContent="Info & Einstellungen";b.onclick=()=>{const c=$("cogb");if(c)c.click();};w.appendChild(b);
 if(imp){const h=imp.cloneNode(true);h.removeAttribute("id");w.appendChild(h);const t=imp.nextElementSibling;if(t)w.appendChild(t.cloneNode(true));}
 sec.appendChild(w);}
mk($("p-wow"));mk($("p-study"));})();</script>
'''
a = '<script id="info-link-js">'
assert s.count(a) == 1
s = s.replace(a, CSS + JS + a)
s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1) + '2026-11-20f' + m.group(3), s, count=1)
open('index.html', 'w', encoding='utf-8').write(s)
print('ok')
