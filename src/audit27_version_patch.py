# Audit 27.11., Punkt 2: Versions-Check über version.txt statt ganzer index.html; zweites Prüfskript (PASSAGE) entfernt. Danach src/version_sync.py. sw.js: version.txt nie cachen, alte ?t=-Kopien löschen.
import sys,re
NEW=('<script id="upd-js">/* Update-Prüfung (Audit 27.11., Punkt 2): beim Öffnen und beim Zurückkehren in die App wird nur die kleine version.txt ohne Zwischenspeicher geholt (eine Zeile statt der ganzen Seite); steht dort eine andere Version, lädt die App einmal neu. version.txt muss zur meta app-version passen: nach jeder Versionsänderung python3 src/version_sync.py */\n'
 '(function(){var cur=(document.querySelector(\'meta[name="app-version"]\')||{}).content;if(!cur||!window.fetch)return;\n'
 'function check(){fetch("version.txt?t="+Date.now(),{cache:"no-store"}).then(function(r){return r.ok?r.text():"";}).then(function(t){var v=(t||"").trim();if(!v||v.length>40||v===cur)return;\n'
 'try{if(sessionStorage.getItem("app-upd")===v)return;sessionStorage.setItem("app-upd",v);}catch(e){}\n'
 'var q=new URLSearchParams(location.search);q.set("v",v);location.replace(location.pathname+"?"+q.toString()+location.hash);}).catch(function(){});}\n'
 'addEventListener("load",function(){setTimeout(check,1500);});document.addEventListener("visibilitychange",function(){if(document.visibilityState==="visible")check();});})();</script>')
for f in sys.argv[1:]:
    s=open(f,encoding='utf-8').read()
    m=re.search(r'<script id="upd-js">.*?</script>',s,re.S);assert m,f
    s=s[:m.start()]+NEW+s[m.end():]
    # PASSAGE: zweites, älteres Prüf-Skript streichen
    old=re.search(r"/\* Neue Version vorhanden\? Dann einmal neu laden.*?location\.reload\(\)\}\)\.catch\(\(\)=>\{\}\)\}catch\(e\)\{\}\}\)\(\);\n",s,re.S)
    if old: s=s[:old.start()]+s[old.end():];print(f,"altes Skript entfernt")
    open(f,'w',encoding='utf-8').write(s)
    v=re.search(r'name="app-version" content="([^"]+)"',s).group(1)
    print(f,"no-store:",s.count("no-store"),"Version",v)
