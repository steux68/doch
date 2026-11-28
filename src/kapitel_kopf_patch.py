# 28.11.2026: Kapitel-Kopf wie in PASSAGE (von Steuart freigegeben, Mock-up mockup_nav2).
# In einem Thema: oben kleiner grauer Link „← Grammatik“ (bzw. Tests, Hilfsmittel, Staunen = der Abschnitt, aus dem man kam),
# darunter Titelleiste in der Farbe dieses Abschnitts, schwarzer Strich links, so breit und hoch (32 px) wie die Reiter.
# Zurück (Link und Handy) führt eine Ebene hinauf: zur Startseite an die Stelle, von der aus das Thema geöffnet wurde,
# nicht mehr zur Titelseite mit der Karte. Ein Tipp auf die Titelleiste führt nicht mehr zurück (nur der Link).
# Unterer Weiter-Knopf (tNext): am Ende steht der Abschnittsname (z. B. „Grammatik“) statt „Start“.
# Aufruf: python3 src/kapitel_kopf_patch.py NEUE_VERSION   danach: python3 src/version_sync.py
import sys,re
VER=sys.argv[1]
f='index.html'
s=open(f,encoding='utf-8').read()
OLD='setTimeout(()=>{$("hscroll").scrollTop=0;typeof enterMap==="function"&&enterMap();},90);};'
NEW='setTimeout(()=>{if(window.chBack)chBack();else{$("hscroll").scrollTop=0;typeof enterMap==="function"&&enterMap();}},90);};'
if OLD in s: s=s.replace(OLD,NEW,1)
assert NEW in s
CSS='''<style id="kapitel-css">/* 28.11.: Kapitel-Kopf: kleiner grauer Zurück-Link, darunter Titelleiste in der Abschnittsfarbe, so breit und hoch wie die Reiter */
#topic .titlebar.titlebar{height:auto!important;flex-wrap:wrap!important;gap:0!important;padding:0 0 4px!important;align-items:stretch!important;justify-content:flex-start!important;cursor:default!important}
#topic .titlebar .spacer{display:none!important}
#topic #back{flex:0 0 100%!important;height:28px!important;min-height:0!important;margin:0!important;padding:0!important;background:none!important;box-shadow:none!important;border:0!important;justify-content:flex-start!important;align-items:center!important;gap:0!important;min-width:0!important;font-size:12px!important;font-weight:700!important;letter-spacing:.12em!important;text-transform:uppercase!important;color:#777!important;white-space:nowrap;cursor:pointer}
#topic #back svg{display:none!important}
#topic .titlebar #ttl#ttl{flex:0 0 100%!important;box-sizing:border-box!important;height:32px!important;min-height:0!important;margin:0!important;padding:0 10px!important;display:flex!important;flex-direction:row!important;align-items:center!important;justify-content:flex-start!important;background:var(--chc,#cfe2f9)!important;border-left:4px solid #1a1a1a!important;font-size:14px!important;font-weight:700!important;letter-spacing:.12em!important;text-transform:uppercase!important;color:#1a1a1a!important;line-height:1!important;white-space:nowrap!important;overflow:hidden!important;text-overflow:ellipsis!important;text-align:left!important}
</style>'''
JS='''<script id="kapitel-js">/* 28.11.: Kapitel-Kopf. Merkt beim Öffnen eines Themas Abschnitt und Scrollstelle; Zurück kehrt genau dorthin zurück */
(function(){const $=id=>document.getElementById(id),S=$('hscroll'),bk=$('back'),tt=$('ttl');if(!S||!bk||!tt)return;
 const SEC={'p-home':['Grammatik','#cfe2f9'],'p-test':['Tests','#f2e2b0'],'p-links':['Hilfsmittel','#8db5e8']};
 const ST=['Staunen','#f2c14e'];
 let pos=0,sec=null,dl=0;const top=id=>{const P=$(id);return P?P.offsetTop-parseFloat(getComputedStyle(P).scrollMarginTop||0):0;};
 S.addEventListener('click',e=>{const p=e.target.closest&&e.target.closest('#hscroll > section');pos=S.scrollTop;sec=p?p.id:null;dl=sec?pos-top(sec):0;},true);
 const cur=()=>SEC[sec]||(sec&&sec!=='p-title'?ST:['Start','#e8e8e8']);window.chName=()=>cur()[0];
 function label(){const v=cur();
  const txt=bk.lastChild;if(txt&&txt.nodeType===3)txt.textContent='\\u2190\\u2002'+v[0];else bk.append('\\u2190\\u2002'+v[0]);
  bk.setAttribute('aria-label','Zurück zu '+v[0]);$('topic').style.setProperty('--chc',v[1]);}
 new MutationObserver(()=>{if(!$('topic').hidden)label();}).observe($('topic'),{attributes:true,attributeFilter:['hidden']});
 window.chBack=function(){if(!sec||sec==='p-title'){S.scrollTop=0;if(typeof enterMap==='function')enterMap();return;}
  /* zuletzt von knapp darunter herauf setzen: das Einrasten der Startseite sieht dann „rückwärts“ und schiebt nicht zum nächsten Abschnitt weiter */
  const go=()=>{if($('home').hidden)return;const y=Math.max(0,top(sec)+dl);S.scrollTop=y+6;requestAnimationFrame(()=>{S.scrollTop=y;});};[0,120,400].forEach(t=>setTimeout(go,t));};
 /* Tipp auf die Titelleiste führt nicht mehr zurück, nur der Link */
 tt.addEventListener('click',e=>e.stopPropagation());
 label();
})();</script>'''
for tag,blk in (('style id="kapitel-css"',CSS),('script id="kapitel-js"',JS)):
    nm=tag.split()[0];pat=r'<%s>.*?</%s>'%(re.escape(tag),nm)
    if re.search(pat,s,flags=re.S): s=re.sub(pat,lambda m:blk,s,flags=re.S)
    else: s=s.rstrip('\n')+'\n'+blk+'\n'
OLD2='$("tnw").textContent=nx||"Start";b.setAttribute("aria-label",nx?"weiter zu "+nx:"zur Titelseite");'
NEW2='$("tnw").textContent=nx||(window.chName?chName():"Start");b.setAttribute("aria-label",nx?"weiter zu "+nx:"zurück zu "+(window.chName?chName():"Start"));'
if OLD2 in s: s=s.replace(OLD2,NEW2,1)
assert NEW2 in s
s=re.sub(r'(<meta name="app-version" content=")[^"]+(")',lambda m:m.group(1)+VER+m.group(2),s,count=1)
open(f,'w',encoding='utf-8').write(s);print(f,'ok',VER)
