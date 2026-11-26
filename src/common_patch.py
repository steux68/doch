# Audit 27.11., Punkte 7 & 8: gemeinsame common.js (AppBack = Zurück-Taste, AppSwipe = Wischen), gleich in DOCH, PASSAGE & dasein-design.
# DOCH: altes Verlaufs-Schema ("never leave the app") raus, Ebenen bei AppBack anmelden, Wischen auf der Lernkarte.
# Aufruf: python3 src/common_patch.py index.html NEUE_VERSION   danach: python3 src/version_sync.py
import sys,re
f,VER=sys.argv[1],sys.argv[2]
s=open(f,encoding='utf-8').read()
def rep(old,new,n=1):
    global s
    c=s.count(old);assert c==n,(old[:70],c);s=s.replace(old,new)

# 1. common.js früh laden (vor allen App-Skripten, damit sein popstate-Handler zuerst dran ist)
if 'src="common.js' not in s:
    m=re.search(r'<meta name="app-version" content="[^"]+">',s);assert m
    s=s[:m.end()]+'<script src="common.js?v=%s"></script>'%VER+s[m.end():]

# 2. altes Schema: Verlauf nicht mehr selbst führen (navPush/navState bleiben als leere Hüllen, damit alte Aufrufe direkt schließen)
rep('/* phone back button: pop-up → topic → start page, and never leave the app */\n'
    'function navState(){try{return history.state&&history.state.dg;}catch(e){return null;}}\n'
    'function navPush(v){try{history.pushState({dg:v},"");}catch(e){}}\n'
    'try{history.replaceState({dg:"base"},"");history.pushState({dg:"home"},"");}catch(e){}\n'
    'window.addEventListener("popstate",e=>{const st=e.state&&e.state.dg;\n'
    '  if(!$("setpop").hidden){closeSetPop();if(st==="home"||st==="topic")return;}\n'
    '  if(GP.open){closePop();if(st==="topic")return;}\n'
    '  if(!$("topic").hidden&&st!=="topic"){goHome();}\n'
    '  if(st==="base"||!st){navPush("home");}});\n',
    '/* Zurück-Taste: seit Audit 27.11. über common.js (AppBack, Skript common-wire am Ende). Pop-up → Thema → Titelseite → App verlassen. */\n'
    'function navState(){return null;}\n'
    'function navPush(v){}\n')
rep('  window.addEventListener("popstate",()=>{if(TLO.open)tlClose();});\n','')
rep('window.addEventListener("popstate",()=>{if(QO.open)close();});\n','')

# 3. Ebenen anmelden & Wischen
WIRE='''<script id="common-wire">/* Audit 27.11., Punkte 7 & 8: Ebenen für die Zurück-Taste (oberste zuerst) und Wischen auf der Lernkarte (common.js) */
(function(){if(!window.AppBack||!window.AppSwipe)return;const $=id=>document.getElementById(id),open=id=>{const e=$(id);return !!e&&!e.hidden;},P=AppCommon.press;
 const SC=$("hscroll"),app=document.querySelector(".app");let toTop=false,quiet=0;
 AppBack
  .add({open:()=>open("bkov"),close:()=>{$("bkov").hidden=true;}})
  .add({open:()=>open("setpop"),close:()=>{if(!P("setx"))window.closeSetPop&&closeSetPop();}})
  .add({open:()=>open("qpop"),close:()=>{if(!P("qx"))$("qpop").hidden=true;}})
  .add({open:()=>open("tlpop"),close:()=>{if(!P("tlx"))typeof tlClose==="function"&&tlClose();}})
  .add({open:()=>typeof GP!=="undefined"&&!!GP.open,close:()=>{if(!P("px"))closePop();}})
  .add({open:()=>open("topic"),close:()=>{quiet=Date.now()+500;P("back");}})
  /* Titelseite: weiter unten gescrollt → zuerst nach oben (wie PASSAGE) */
  .add({open:()=>{if(!SC||open("topic")||Date.now()<quiet)return false;if(toTop){if(SC.scrollTop<60)toTop=false;return false;}return SC.scrollTop>=60;},
        close:()=>{toTop=true;SC.scrollTo({top:0,behavior:matchMedia("(prefers-reduced-motion: reduce)").matches?"auto":"smooth"});}})
  .init();
 if(SC)SC.addEventListener("scroll",()=>{if(toTop&&SC.scrollTop<60)toTop=false;},{passive:true});
 /* Lernkarte (01 / 30): waagrecht wischen = Pfeil links/rechts; senkrecht scrollt weiter */
 AppSwipe($("topic"),{when:()=>app&&app.dataset.mode==="learn"&&!(typeof GP!=="undefined"&&GP.open),
  prev:()=>P("bZ"),next:()=>P("bW"),ignore:"#seg,.snh,.svar,.svt,#sehb"});
})();</script>'''
if 'id="common-wire"' in s:
    s=re.sub(r'<script id="common-wire">.*?</script>',lambda m:WIRE,s,flags=re.S)
else:
    s=s.rstrip('\n')+'\n'+WIRE+'\n'
s=re.sub(r'(<meta name="app-version" content=")[^"]+(")',lambda m:m.group(1)+VER+m.group(2),s,count=1)
open(f,'w',encoding='utf-8').write(s)
print(f,'ok',VER,'common.js-Tags:',s.count('src="common.js'),'popstate:',s.count('popstate'))
