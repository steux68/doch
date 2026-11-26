# DOCH! 26.11.2026: Tests als kompakter Baukasten: Niveau / Fragen (10-20-50) / Bereich (Popup mit allen Themen) + "Test starten".
# Laenge und "Heute wiederholen" aus der Tests-Seite entfernt; "Heute wiederholen" heisst jetzt "Fehler wiederholen". Idempotent.
import re, sys
s = open('index.html', encoding='utf-8').read()
if 'id="bk-js"' in s: sys.exit('schon angewendet')
a = 'const TLEN=()=>[15,30,45].includes(store.tlen)?store.tlen:15;'
assert s.count(a) == 1
s = s.replace(a, 'const TLEN=()=>[10,20,50].includes(store.tlen)?store.tlen:20;')
s = s.replace('Heute wiederholen', 'Fehler wiederholen')
css = ('<style id="bk-css">'
 '#p-test .sehb{display:none!important}'
 '#p-test .bk{padding:2px 0 0}'
 '#p-test .bkr{display:flex;align-items:center;gap:8px;margin:0 0 4px}'
 '#p-test .bkl{flex:none;width:60px;font-size:12px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--red,#e30613)}'
 '#p-test .bkc{flex:1;min-width:0;display:grid;grid-template-columns:repeat(6,1fr);gap:4px}'
 '#p-test .bkc>button,#p-test .bkc .lvb{height:32px;min-height:32px!important;padding:0;font:inherit;font-size:14px;border:0;border-radius:0;background:#ececea!important;color:#1a1a1a;cursor:pointer}'
 '#p-test .bkc>button[aria-pressed="true"],#p-test .bkc .lvb[aria-pressed="true"]{background:#cdff3e!important;font-weight:700}'
 '#p-test .bkc .lvsel,#p-test .bkc #lvs2{display:contents!important;margin:0!important}'
 '#p-test .bkc .bkb{grid-column:1/-1;display:flex;align-items:center;justify-content:space-between;padding:0 10px;text-align:left}'
 '#p-test .bkc .bkb span:last-child{font-size:12px}'
 '#p-test .rcb{margin:8px 0 8px!important}'
 '#p-test #goTest{min-height:44px!important;padding:8px 12px!important}'
 '#p-test #goTest>b:last-child{display:none!important}'
 '#bkov{position:fixed;inset:0;z-index:99995;background:rgba(0,0,0,.35);display:flex;align-items:center;justify-content:center;padding:24px}'
 '#bkov[hidden]{display:none}'
 '#bkov .bkp{background:#fff;width:100%;max-width:420px;max-height:80vh;display:flex;flex-direction:column;box-shadow:0 0 0 1px #bbb}'
 '#bkov .bkh{display:flex;justify-content:space-between;align-items:center;padding:10px 14px;border-bottom:1px dotted #aaa;font-size:12px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--red,#e30613)}'
 '#bkov .bkh button{background:transparent;font-size:20px;padding:0 4px;line-height:1;color:#1a1a1a}'
 '#bkov .bkl2{overflow-y:auto;padding:8px 10px;display:grid;gap:4px}'
 '#bkov .bkl2 button{text-align:left;padding:8px 12px;font-size:14px;background:#f3f3f1;border:0;border-radius:0;color:#1a1a1a}'
 '#bkov .bkl2 button.on{background:#cdff3e;font-weight:700}'
 '</style>')
js = r'''<script id="bk-js">(function(){
var EX={test:1,links:1,sehen:1,lueck:1,write:1};
function areas(){var o=[];try{TOPICS.forEach(function(x){if(!x||!x.t||EX[x.t])return;try{if(bank(x.t).length>0)o.push(x)}catch(e){}})}catch(e){}return o;}
function nameOf(t){var l=areas();for(var i=0;i<l.length;i++)if(l[i].t===t)return l[i].n;return "";}
function ov(){var o=document.getElementById("bkov");if(!o){o=document.createElement("div");o.id="bkov";o.hidden=true;document.body.appendChild(o);o.addEventListener("click",function(e){if(e.target===o)o.hidden=true;});}return o;}
function openArea(){var o=ov(),cur=store.tarea||"";var h='<div class="bkp"><div class="bkh"><span>Bereich</span><button type="button" aria-label="Schließen" id="bkx">✕</button></div><div class="bkl2"><button type="button" data-t=""'+(cur?'':' class="on"')+'>Alle Bereiche</button>';
 areas().forEach(function(x){h+='<button type="button" data-t="'+x.t+'"'+(cur===x.t?' class="on"':'')+'></button>';});h+='</div></div>';o.innerHTML=h;
 var bs=o.querySelectorAll(".bkl2 button"),l=areas();for(var i=1;i<bs.length;i++)bs[i].textContent=l[i-1].n;
 o.querySelector("#bkx").onclick=function(){o.hidden=true};
 bs.forEach(function(b){b.onclick=function(){store.tarea=b.dataset.t||"";save();o.hidden=true;renderTest();};});o.hidden=false;}
function mk(cls,html){var d=document.createElement("div");d.className=cls;d.innerHTML=html;return d;}
function decorate(){var pt=document.getElementById("p-test"),tpg=pt&&pt.querySelector(".tpg");if(!tpg||tpg.querySelector(".bk"))return;
 var lv=tpg.querySelector(".lvsel"),gt=document.getElementById("goTest");if(!lv||!gt)return;
 var n=TLEN(),L=store.level||"all",ar=store.tarea||"";if(ar&&!nameOf(ar)){ar="";store.tarea="";}
 var bk=mk("bk",""),r1=mk("bkr",'<span class="bkl">Niveau</span>'),c1=mk("bkc",""),r2=mk("bkr",'<span class="bkl">Fragen</span>'),c2=mk("bkc",""),r3=mk("bkr",'<span class="bkl">Bereich</span>'),c3=mk("bkc","");
 c1.appendChild(lv);r1.appendChild(c1);
 [10,20,50].forEach(function(k){var b=document.createElement("button");b.type="button";b.textContent=k;b.setAttribute("aria-pressed",n===k);b.onclick=function(){store.tlen=k;store.artn=k;save();renderTest();};c2.appendChild(b);});r2.appendChild(c2);
 var bb=document.createElement("button");bb.type="button";bb.className="bkb";bb.innerHTML="<span></span><span>▾</span>";bb.firstChild.textContent=ar?nameOf(ar):"Alle Bereiche";bb.onclick=openArea;c3.appendChild(bb);r3.appendChild(c3);
 bk.appendChild(r1);bk.appendChild(r2);bk.appendChild(r3);tpg.insertBefore(bk,tpg.firstChild);
 var rc=gt.closest(".rcb");if(rc)bk.after(rc);
 gt.innerHTML="<span><small>Test starten</small><b></b></span>";gt.querySelector("b").textContent=n+" Fragen · "+(L==="all"?"alle Stufen":L)+" · "+(ar?nameOf(ar):"alle Bereiche");
 gt.onclick=function(){TESTLV=(store.level&&store.level!=="all")?store.level:"all";store.artn=TLEN();if(ar){openTopic(ar);setMode("game");}else openTopic("test");};}
var r=window.renderTest;if(typeof r==="function")window.renderTest=function(){var x=r.apply(this,arguments);try{decorate()}catch(e){}return x;};
try{if(document.getElementById("p-test").firstChild)renderTest();}catch(e){}
})();</script>'''
assert '</head>' in s
s = s.replace('</head>', css + '</head>', 1)
s = s.rstrip('\n') + '\n' + js + '\n'
if '--noversion' not in sys.argv:
    s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1) + '2026-11-26y' + m.group(3), s, count=1)
open('index.html', 'w', encoding='utf-8').write(s)
print('ok')
