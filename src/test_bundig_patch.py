# DOCH! 26.11.2026: (1) Tests: Bereich-Feld buendig am unteren Rand des Blocks (kein Puffer darunter), Start-Knopf 50 px;
# (2) Pfeil im Bereich-Feld grosser Chevron (Schaltflaeche erkennbar); (3) PDF-Symbol (dasein-design) an jedem Link auf eine PDF-Datei. Idempotent.
import re, sys
s = open('index.html', encoding='utf-8').read()
if 'id="bundig-css"' in s: sys.exit('schon angewendet')
chev = "url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M4 8l8 8 8-8' fill='none' stroke='%231a1a1a' stroke-width='2.4' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E\")"
css = ('<style id="bundig-css">#p-test .tc.tpg,#p-test .tpg{padding-bottom:0!important}#p-test{margin-bottom:12px}'
       '#p-test .tc.tpg{gap:0!important}#p-test .tpg>.sehb,#p-test .tpg>.rcb{margin:0!important}'
       '#p-test .tests.rows2{padding-top:0!important}'
       '.bks{width:50px!important;height:50px!important}'
       '.bkb span:last-child{font-size:0!important;flex:none;width:22px;height:22px;background:' + chev + ' center/22px 22px no-repeat}'
       '.pdfi{display:inline-block;vertical-align:-4px;margin-left:6px}'
       '</style>')
svg = ('<svg class="pdfi" viewBox="58 0 342 428" width="16" height="20" aria-hidden="true" focusable="false"><g fill="none" stroke="#4d4d4d" stroke-width="22" stroke-linejoin="round">'
       '<path d="M140 11H298L381 94V356Q381 384 353 384H140Q112 384 112 356V39Q112 11 140 11Z"/><path d="M298 11V70Q298 94 322 94H381"/></g>'
       '<rect x="68" y="80" width="202" height="84" fill="#e2401c"/><text x="169" y="148" fill="#fff" font-family="inherit" font-weight="700" font-size="74" text-anchor="middle" letter-spacing="2">PDF</text>'
       '<path d="M251 236H325V331H358L288 422L218 331H251Z" fill="#e2401c"/></svg>')
js = ('<script id="bundig-js">(function(){var SV=' + repr(svg) + ';function f(){try{document.querySelectorAll(\'a[href*=".pdf"]\').forEach(function(a){if(a.getAttribute("data-pdfi"))return;a.setAttribute("data-pdfi","1");a.insertAdjacentHTML("beforeend",SV);});}catch(e){}}'
      'f();try{new MutationObserver(f).observe(document.body,{childList:true,subtree:true});}catch(e){}})();</script>')
s = s.rstrip('\n') + '\n' + css + '\n' + js + '\n'
if '--noversion' not in sys.argv:
    s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1) + '2026-11-26zp' + m.group(3), s, count=1)
open('index.html', 'w', encoding='utf-8').write(s); print('ok')
