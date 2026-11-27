#!/usr/bin/env python3
"""Studieren -> Grammatik: eine schmale Zeile unter den Gruppen fuehrt zu Staunen -> Grammatikwoerter [C].
Aufruf:  python3 src/gram_teaser_test.py          -> schreibt die Testkopie gramm6.html (index.html bleibt unberuehrt)
         python3 src/gram_teaser_test.py live     -> schreibt index.html
Idempotent: bricht ab, wenn id="gwTeaser" schon da ist."""
import os,sys
LIVE=len(sys.argv)>1 and sys.argv[1]=='live'
root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
s=open(os.path.join(root,'index.html'),encoding='utf-8').read()
if 'id="gwTeaser"' in s: print('already'); raise SystemExit
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)

BTN=('<button type="button" class="gwt" id="gwTeaser" aria-label="Grammatikwörter: Woher die Fachwörter kommen. Öffnet Staunen, Leiste C">'
     '<i class="gws" aria-hidden="true"></i>'
     '<span class="gwm"><b>Grammatikwörter</b><small>Woher kommen Dativ, Verb, Ablaut?</small></span>'
     '<span class="gwk">Staunen [C] →</span></button>')
rep('<div id="groups"></div>\n      </section>','<div id="groups"></div>\n        '+BTN+'\n      </section>')

CSS='''<style id="gw-teaser-css">
/* Studieren -> Grammatik: Weg zu den Grammatikwoertern. Teal = Farbe der Leiste C; Text sagt dasselbe (Farbe nie allein) */
#p-home .gwt{order:5;display:flex;align-items:center;gap:10px;width:100%;min-height:48px;margin:6px 0 16px;padding:6px 2px;border:0;border-radius:0;font:inherit;color:#1a1a1a;text-align:left;cursor:pointer;-webkit-tap-highlight-color:transparent;
 background:repeating-linear-gradient(to right,#b8b8b8 0 1px,transparent 1px 3px) left top/100% 1px no-repeat,repeating-linear-gradient(to right,#b8b8b8 0 1px,transparent 1px 3px) left bottom/100% 1px no-repeat,#fff}
#p-home .gwt .gws{flex:none;align-self:stretch;width:8px;background:#bfe4d6;box-shadow:inset 0 0 0 1px #8fcdb6}
#p-home .gwt .gwm{flex:1 1 auto;min-width:0;display:flex;flex-direction:column;line-height:1.25}
#p-home .gwt .gwm b{font-size:14px;font-weight:700}
#p-home .gwt .gwm small{font-size:12px;color:#6b6b67}
#p-home .gwt .gwk{flex:none;font-size:12px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--red,#e30613);white-space:nowrap}
#p-home .gwt:active{background-color:#e8f4ef}
#p-home .gwt:focus-visible{outline:2px solid #1a5fd0;outline-offset:2px}
</style>'''
JS='''<script id="gw-teaser-js">(function(){var b=document.getElementById("gwTeaser");if(!b)return;
b.addEventListener("click",function(){try{sessionStorage.setItem("dochMode","s");sessionStorage.setItem("dochSwitched","1");sessionStorage.setItem("dochTarget","2");}catch(e){}location.reload();});})();</script>'''
s=s+CSS+JS  # Datei hat kein </body>; Skripte stehen am Ende

out=os.path.join(root,'index.html' if LIVE else 'gramm6.html')
open(out,'w',encoding='utf-8').write(s); print('wrote',out)
