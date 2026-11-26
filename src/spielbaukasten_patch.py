# DOCH! 26.11.2026: Spiel-Steuerung im Stil des Test-Starts: rote Beschriftungen links (FRAGEN, STAND), gleich hohe Chips 10/20/50,
# Stand "Punkte · Serie · Beste" in einer Zeile, rechts runder Knopf "Neu" (duenner gepunkteter Kreis). Die alte Fragen-Leiste (#artNbar) bleibt unsichtbar bestehen
# (ihr Klick-Handler wird per click() benutzt), sichtbar ist nur #srow. Idempotent.
import re, sys
s = open('index.html', encoding='utf-8').read()
if 'id="spielbk-css"' in s: sys.exit('schon angewendet')
old = """row.innerHTML='<span>Punkte <b>'+MC.score+'</b> / '+n+'</span><span>Serie <b>'+streak+'</b></span><span>Beste <b>'+best+'</b></span><button type="button">\\u21ba Neu</button>';
 row.querySelector("button").onclick=()=>{const r=$("bR");if(r)r.click();};}"""
assert s.count(old) == 1, s.count(old)
new = """const nb=$("artNbar"),has=nb&&!nb.hidden&&nb.querySelector("button[data-n]"),cur=(typeof ARTN==="function"?ARTN():20);
 let h="";if(has)h+='<span class="gl">Fragen</span>'+[10,20,50].map((k,i)=>'<button type="button" class="gc" data-n="'+k+'" style="grid-column:'+(i+2)+'" aria-pressed="'+(cur===k)+'">'+k+'</button>').join("");
 h+='<span class="gl" style="grid-row:'+(has?2:1)+'">Stand</span><span class="gs">Punkte <b>'+MC.score+'</b> / '+n+' \\u00b7 Serie <b>'+streak+'</b> \\u00b7 Beste <b>'+best+'</b></span><button type="button" class="gn">Neu</button>';
 row.className=has?"two":"one";row.innerHTML=h;
 row.querySelector(".gn").onclick=()=>{const r=$("bR");if(r)r.click();};
 row.querySelectorAll(".gc").forEach(b=>b.onclick=()=>{const x=document.querySelector('#artNbar button[data-n="'+b.dataset.n+'"]');if(x)x.click();});}"""
s = s.replace(old, new)
css = ('<style id="spielbk-css">'
 '.app[data-mode="game"] #artNbar{display:none!important}'
 'body .app[data-mode="game"] #srow{display:grid;grid-template-columns:60px repeat(6,1fr);gap:4px;align-items:center;justify-content:normal;margin:8px 0 10px;height:auto;padding:0}'
 '#srow .gl{grid-column:1;font-size:12px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--red,#e30613)}'
 '#srow .gc{grid-row:1;height:32px;padding:0;font:inherit;font-size:14px;border:0;border-radius:0;background:#ececea;color:#1a1a1a;cursor:pointer}'
 '#srow .gc[aria-pressed="true"]{background:#cdff3e;font-weight:700}'
 '#srow .gs{grid-column:2/6;white-space:nowrap;font-size:14px;color:#555;font-variant-numeric:tabular-nums}#srow .gs b{color:#1a1a1a;font-weight:700}'
 '#srow.two .gs{grid-row:2}#srow.one .gs{grid-row:1}'
 '#srow .gn{grid-column:6/8;justify-self:center;align-self:center;width:56px;height:56px;border-radius:50%;border:1px dotted #1a1a1a;padding:0;background:#f4f4f2;color:#1a1a1a;font:inherit;font-size:14px;font-weight:800;cursor:pointer;-webkit-tap-highlight-color:transparent}'
 '.app #srow:empty{display:none!important}#srow.two .gn{grid-row:1/3}#srow.one .gn{grid-row:1}#srow .gn:active{background:#e8ecd6}'
 '@media(max-width:380px){#srow.two .gn{grid-row:1;width:48px;height:48px}#srow.two .gs{grid-column:2/8}}'
 '</style>')
s = s.replace('</head>', css + '</head>', 1)
if '--noversion' not in sys.argv:
    s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1) + '2026-11-26zg' + m.group(3), s, count=1)
open('index.html', 'w', encoding='utf-8').write(s); print('ok')
