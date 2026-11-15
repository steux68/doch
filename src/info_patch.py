#!/usr/bin/env python3
"""DOCH: Einstellungen werden zu 'Info & Einstellungen': Anleitung, Credit-Kasten, update-/home-Knopf (wie PASSAGE/dasein-design)."""
import re, sys
p="index.html"; s=open(p,encoding="utf-8").read()
if "/* info-credit */" in s: sys.exit("already patched")
def rep(old,new,cnt=1):
    global s
    if s.count(old)!=cnt: sys.exit("Anker fehlt/mehrfach: "+old[:60])
    s=s.replace(old,new)
# 1 old update row out (button is created in JS below)
rep('      <div class="timer"><span>Neueste Version <small class="n">App neu laden, Lernstand bleibt</small></span><button id="updbtn">laden</button></div>\n','')
# 2 titles
rep('<b id="setpt">Einstellungen</b>','<b id="setpt">Info &amp; Einstellungen</b>')
rep('Einstellungen</b><small>Timer · Artikel-Hilfe · neueste Version</small>','Info &amp; Einstellungen</b><small>Anleitung · Timer · neueste Version</small>')
rep('aria-label="Einstellungen"','aria-label="Info und Einstellungen"',s.count('aria-label="Einstellungen"'))
# 3 css
G='repeating-linear-gradient(to right,#b8b8b8 0 1px,transparent 1px 3px)'; V='repeating-linear-gradient(to bottom,#b8b8b8 0 1px,transparent 1px 3px)'
box=f"background-color:#fff!important;background-image:{G},{G},{V},{V}!important;background-position:left top,left bottom,left top,right top!important;background-size:100% 1px,100% 1px,1px 100%,1px 100%!important;background-repeat:no-repeat!important;background-origin:border-box!important"
CSS=f"""/* info-credit */
.ih{{margin:16px 0 4px!important;font-size:12px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--red)}}
.ih.first{{margin-top:2px!important}}
#setb .tline b{{color:var(--fg)}}
.utl{{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin:12px 0 4px}}
.utl button{{display:flex;align-items:center;justify-content:center;gap:6px;height:36px;padding:0 10px;font:inherit;font-size:14px;color:#222;cursor:pointer;border:1px solid transparent;border-radius:0;{box}}}
.utl button svg{{width:16px;height:16px;fill:none;stroke:currentColor;stroke-width:1.6;stroke-linecap:round;stroke-linejoin:round}}
.utl button:active{{background-color:#f4f4f4!important}}
.ucr{{display:flex;flex-direction:column;align-items:center;gap:4px;margin:14px auto 0;max-width:200px;font-size:12px;color:#777;text-align:center;line-height:1.2}}
.ucr .bx{{width:100%;height:46px;display:grid;place-items:center;padding:3px 6px;border:1px solid transparent;box-sizing:border-box;{box}}}
.ucr .bx img{{max-height:38px;max-width:100%;display:block}}
"""
k=s.rindex("</style>"); s=s[:k]+CSS+s[k:]
# 4 js: info block first, credit + buttons before impressum
rep('(()=>{const st=$("sets"),B=$("setb");st.hidden=false;B.appendChild(st);',
r'''(()=>{const st=$("sets"),B=$("setb");st.hidden=false;
  const ih=document.createElement("div");ih.innerHTML='<p class="ih first">Info &amp; Anleitung</p><p class="tline"><b>Als App auf den Startbildschirm</b><br><b>iPhone (Safari):</b> Teilen-Symbol → „Zum Home-Bildschirm“<br><b>Android (Chrome):</b> Menü ⋮ → „Zum Startbildschirm hinzufügen“</p><p class="ih">So lernst du</p><p class="tline"><b>Grammatik:</b> Thema antippen. <b>Lernen</b> zeigt die Regel Karte für Karte, <b>Spiel</b> stellt Fragen mit Punkten und Serie, <b>Theorie</b> fasst alles zusammen.<br><b>Tests:</b> Fragen aus allen Themen, wahlweise für eine Stufe (A1–C1) oder gemischt. Dazu <b>Lückentext</b> und <b>Text prüfen</b> (mit LanguageTool).<br><b>Ergänzen:</b> im Spiel selbst tippen statt wählen, mit „Ergänzen: an“.<br><b>Hilfsmittel:</b> Wörterbücher, Zitate, Redewendungen und Geschichte der deutschen Sprache.</p><p class="ih">Einstellungen</p>';
  B.appendChild(ih);B.appendChild(st);''')
rep('  const im=document.createElement("p");im.className="tline";im.innerHTML="<b>Impressum:</b>',
r'''  const lg=document.querySelector("footer.copy img"),cr=document.createElement("div");
  cr.innerHTML='<div class="ucr"><div class="bx">'+(lg?'<img src="'+lg.getAttribute("src")+'" alt="steux">':'steux')+'</div><span>App, Gestaltung und Inhalte © Steuart JM HARRISON (steux)</span></div><div class="utl"><button type="button" id="updbtn"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20 12a8 8 0 1 1-2.6-5.9"/><path d="M20 4v5h-5"/></svg>update</button><button type="button" id="homebtn"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 11l8-7 8 7"/><path d="M6 10v10h12V10"/></svg>home</button></div><p class="tline" style="margin-top:0">update lädt die neueste Version, der Lernstand bleibt.</p>';
  B.appendChild(cr);
  $("homebtn").onclick=function(){location.replace(location.pathname);};
  const im=document.createElement("p");im.className="tline";im.innerHTML="<b>Impressum:</b>''')
# 5 inpop footer clone no longer needed (credit box replaces it)
rep('const f=document.querySelector("footer.copy");if(f){const c=f.cloneNode(true);c.classList.add("inpop");B.appendChild(c);}','')
m=re.search(r'name="app-version" content="(\d{4}-\d\d-\d\d)([a-z]?)"',s)
s=s.replace(m.group(0),'name="app-version" content="%s%s"'%(m.group(1),chr(ord(m.group(2) or "`")+1)))
open(p,"w",encoding="utf-8").write(s); print("OK",m.group(0))
