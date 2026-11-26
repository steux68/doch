# DOCH! 26.11.2026: Baukasten weiter verdichtet: Karte "Test starten" entfernt; Bereich-Knopf nur bis B1 (4 Spalten);
# rechts daneben ein gelber Rundknopf "Start" ueber die Zeilen Fragen+Bereich. Ersetzt CSS/JS aus test_baukasten_patch.py. Idempotent.
import re, sys
s = open('index.html', encoding='utf-8').read()
if 'id="bk2-js"' in s: sys.exit('schon angewendet')
assert 'id="bk-js"' in s and 'id="bk-css"' in s
css = ('<style id="bk-css">'
 '#p-test .sehb{display:none!important}'
 '#p-test .rcb{display:none!important}'
 '#p-test .bk{display:grid;grid-template-columns:60px repeat(6,1fr);gap:4px;padding:2px 0 0;margin:0 0 10px;align-items:center}'
 '#p-test .bk .bkl{grid-column:1;font-size:12px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--red,#e30613)}'
 '#p-test .bk .lvsel,#p-test .bk #lvs2{display:contents!important;margin:0!important}'
 '#p-test .bk button:not(.bks){height:32px;min-height:32px!important;padding:0;font:inherit;font-size:14px;border:0;border-radius:0;background:#ececea!important;color:#1a1a1a;cursor:pointer}'
 '#p-test .bk .lvb{grid-row:1}'
 '#p-test .bk button[aria-pressed="true"]{background:#cdff3e!important;font-weight:700}'
 '#p-test .bk .bkb{grid-row:3;grid-column:2/6;display:flex;align-items:center;justify-content:space-between;padding:0 10px;text-align:left}'
 '#p-test .bk .bkb span:last-child{font-size:12px}'
 '#p-test .bk .bks{grid-row:2/4;grid-column:6/8;justify-self:center;align-self:center;width:56px;height:56px;border-radius:50%;border:0;padding:0;background:#f4f4f2;box-shadow:inset 0 0 0 6px #cdff3e;color:#1a1a1a;font:inherit;font-size:14px;font-weight:800;letter-spacing:.01em;cursor:pointer;-webkit-tap-highlight-color:transparent}'
 '#p-test .bk .bks:active{background:#e8ecd6}'
 '#bkov{position:fixed;inset:0;z-index:99995;background:rgba(0,0,0,.35);display:flex;align-items:center;justify-content:center;padding:24px}'
 '#bkov[hidden]{display:none}'
 '#bkov .bkp{background:#fff;width:100%;max-width:420px;max-height:80vh;display:flex;flex-direction:column;box-shadow:0 0 0 1px #bbb}'
 '#bkov .bkh{display:flex;justify-content:space-between;align-items:center;padding:10px 14px;border-bottom:1px dotted #aaa;font-size:12px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--red,#e30613)}'
 '#bkov .bkh button{background:transparent;font-size:20px;padding:0 4px;line-height:1;color:#1a1a1a}'
 '#bkov .bkl2{overflow-y:auto;padding:8px 10px;display:grid;gap:4px}'
 '#bkov .bkl2 button{text-align:left;padding:8px 12px;font-size:14px;background:#f3f3f1;border:0;border-radius:0;color:#1a1a1a}'
 '#bkov .bkl2 button.on{background:#cdff3e;font-weight:700}'
 '</style>')
old = re.search(r'<script id="bk-js">.*?</script>', s, re.S).group(0)
js = old.replace('<script id="bk-js">', '<script id="bk2-js">')
a = js.index('function decorate()'); b = js.index('var r=window.renderTest')
new_dec = r'''function decorate(){var pt=document.getElementById("p-test"),tpg=pt&&pt.querySelector(".tpg");if(!tpg||tpg.querySelector(".bk"))return;
 var lv=tpg.querySelector(".lvsel"),gt=document.getElementById("goTest");if(!lv||!gt)return;
 var n=TLEN(),ar=store.tarea||"";if(ar&&!nameOf(ar)){ar="";store.tarea="";}
 var bk=mk("bk",""),L=function(t,r){var d=document.createElement("span");d.className="bkl";d.textContent=t;d.style.gridRow=r;return d;};
 bk.appendChild(L("Niveau",1));bk.appendChild(lv);bk.appendChild(L("Fragen",2));bk.appendChild(L("Bereich",3));
 [10,20,50].forEach(function(k,i){var b=document.createElement("button");b.type="button";b.textContent=k;b.style.gridRow="2";b.style.gridColumn=String(i+2);b.setAttribute("aria-pressed",n===k);b.onclick=function(){store.tlen=k;store.artn=k;save();renderTest();};bk.appendChild(b);});
 var bb=document.createElement("button");bb.type="button";bb.className="bkb";bb.innerHTML="<span></span><span>▾</span>";bb.firstChild.textContent=ar?nameOf(ar):"Alle Bereiche";bb.onclick=openArea;bk.appendChild(bb);
 var st=document.createElement("button");st.type="button";st.className="bks";st.textContent="Start";st.setAttribute("aria-label","Test starten");st.onclick=function(){gt.click();};bk.appendChild(st);
 tpg.insertBefore(bk,tpg.firstChild);
 gt.onclick=function(){TESTLV=(store.level&&store.level!=="all")?store.level:"all";store.artn=TLEN();if(ar){openTopic(ar);setMode("game");}else openTopic("test");};}
'''
js = js[:a] + new_dec + js[b:]
s = s.replace(old, js)
s = re.sub(r'<style id="bk-css">.*?</style>', lambda m: css, s, count=1, flags=re.S)
if '--noversion' not in sys.argv:
    s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1) + '2026-11-26z' + m.group(3), s, count=1)
open('index.html', 'w', encoding='utf-8').write(s)
print('ok')
