#!/usr/bin/env python3
"""7 Nov 2026: Einstellungen bar removed (six bars again); small cog + vertical "Einstellungen" in the right margin
opens a settings pop-up (Timer, Artikel-Hilfe, Neueste Version, picture credits, Impressum, version).
Start page also gets a small white strip at the bottom (like PASSAGE) so the Android nav buttons are not hit by mistake.
Run from repo root: python3 src/cog_settings_patch.py"""
import re, sys
p="index.html"; s=open(p,encoding="utf-8").read()
if 'id="setpop"' in s: sys.exit("already patched")
def rep(a,b,c=1):
    global s
    assert s.count(a)>=1,("missing",a[:60])
    s=s.replace(a,b,c)
# 1. bars / sections
rep(',["hist","Geschichte"],["sets","Einstellungen"]];',',["hist","Geschichte"]];')
rep('      <section class="hp" id="p-sets"></section>\n','')
s=re.sub(r'<button class="pin l" data-k="sets"[^>]*>.*?</button>','',s,count=1,flags=re.S)
assert 'data-k="sets"' not in s
# 2. IIFE that built p-sets -> builds the pop-up body
i=s.index('(()=>{const st=$("sets");$("p-sets")'); j=s.index('/* which page are we in')
NEW='''(()=>{const st=$("sets"),B=$("setb");st.hidden=false;B.appendChild(st);
  const nt=document.createElement("p");nt.className="tline";nt.textContent="Bilder: Wikipedia / Wikimedia Commons, freie Lizenzen, Quelle jeweils verlinkt. Alle Links öffnen in einem neuen Fenster.";B.appendChild(nt);
  const im=document.createElement("p");im.className="tline";im.innerHTML="<b>Impressum:</b> Medieninhaber, Herausgeber und Verantwortlicher: Steuart JM Harrison, Wien. Privates, nicht kommerzielles Lernangebot ohne Werbung. Keine Cookies; Lernstand und Einstellungen bleiben auf dem Gerät. Bilder werden direkt von Wikipedia / Wikimedia Commons geladen, dabei sieht Wikimedia die IP-Adresse. Beim Prüfen eines Textes wird er an LanguageTool gesendet (siehe dort).";B.appendChild(im);
  const vm=document.querySelector('meta[name="app-version"]');if(vm){const v=document.createElement("p");v.className="tline";v.textContent="Version "+vm.content;B.appendChild(v);}
  const f=document.querySelector("footer.copy");if(f){const c=f.cloneNode(true);c.classList.add("inpop");B.appendChild(c);}
  function open(){if($("setpop").hidden){navPush("sets");$("setpop").hidden=false;$("setb").scrollTop=0;}}
  function close(){$("setpop").hidden=true;}
  $("cogb").onclick=open;
  $("setx").onclick=()=>{if(navState()==="sets")history.back();else close();};
  window.closeSetPop=close;
  document.addEventListener("keydown",e=>{if(e.key==="Escape"&&!$("setpop").hidden)$("setx").click();});})();
'''
s=s[:i]+NEW+s[j:]
# 3. popstate
rep('window.addEventListener("popstate",e=>{const st=e.state&&e.state.dg;\n','window.addEventListener("popstate",e=>{const st=e.state&&e.state.dg;\n  if(!$("setpop").hidden){closeSetPop();if(st==="home"||st==="topic")return;}\n')
# 4. markup: pop-up + cog (after the main pop)
MARK='''  <div class="pop" id="setpop" hidden role="dialog" aria-modal="true" aria-labelledby="setpt">
    <div class="pbar"><b id="setpt">Einstellungen</b><button id="setx" aria-label="Schließen">×</button></div>
    <div class="pbody" id="setb"></div>
  </div>
  <button class="cogb" id="cogb" type="button" aria-label="Einstellungen"><svg viewBox="-12 -12 24 24" width="20" height="20" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round" d="M-1.9-9.2h3.8l.6 2.5 1.6.7 2.2-1.4 2.7 2.7-1.4 2.2.7 1.6 2.5.6v3.8l-2.5.6-.7 1.6 1.4 2.2-2.7 2.7-2.2-1.4-1.6.7-.6 2.5h-3.8l-.6-2.5-1.6-.7-2.2 1.4-2.7-2.7 1.4-2.2-.7-1.6-2.5-.6v-3.8l2.5-.6.7-1.6-1.4-2.2 2.7-2.7 2.2 1.4 1.6-.7z"/><circle r="3.2" fill="none" stroke="currentColor" stroke-width="1.6"/></svg><span>Einstellungen</span></button>
'''
rep('  <div class="pop" id="pop" hidden',MARK+'  <div class="pop" id="pop" hidden')
# 5. CSS
CSS='''
/* 7 Nov: Einstellungen live in a pop-up opened by a small cog in the right margin (like PASSAGE's vertical Info) */
.cogb{position:fixed;right:5px;bottom:var(--cogb,330px);z-index:46;display:flex;flex-direction:column;align-items:center;gap:5px;width:24px;padding:0;border:0;border-radius:0;background:none;color:#3a3c37;font:inherit;cursor:pointer;opacity:0;pointer-events:none;transition:opacity .35s}
.cogb.cv{opacity:1;pointer-events:auto}
.cogb span{writing-mode:vertical-rl;transform:rotate(180deg);font-size:12px;letter-spacing:.04em;white-space:nowrap}
.cogb:active{color:#000}
#setb .tline{text-align:left}
#setb footer.copy.inpop{position:static;transform:none;opacity:1;pointer-events:auto;width:auto;right:auto;bottom:auto;height:auto;margin-top:8px;border:0;display:flex;justify-content:flex-start;flex-wrap:wrap;background:none}
.app:has(#home:not([hidden])){padding-bottom:max(12px,env(safe-area-inset-bottom,0px))}
'''
rep('.app:has(#home:not([hidden])){padding-bottom:0}\n',CSS)
s=s.replace('#p-sets footer.copy{display:none!important}\n','').replace('#p-sets p.tline{text-align:left!important}\n','')
# 6. credit-corner-js: place cog above the vertical credit, show with it
rep("f.classList.toggle('cv',on&&t);","f.classList.toggle('cv',on&&t);var cg=document.getElementById('cogb');if(cg){cg.style.setProperty('--cogb',(Math.max(60,innerHeight-b+14)+f.offsetWidth+10)+'px');cg.classList.toggle('cv',on&&t);}")
# version
m=re.search(r'name="app-version" content="([^"]*)"',s)
s=s.replace(m.group(0),'name="app-version" content="2026-11-07a"',1)
open(p,"w",encoding="utf-8").write(s); print("ok",m.group(1),"->2026-11-07a")
