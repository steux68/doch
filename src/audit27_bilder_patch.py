# Audit 27.11., Punkt 1: Netzfehler sperren Bilder nicht mehr dauerhaft (-1 nur bei sicherem "kein Bild"/404). Aufruf: python3 src/audit27_bilder_patch.py index.html [weitere .js]
import sys,re
for f in sys.argv[1:]:
    s=open(f,encoding='utf-8').read();o=s
    s=s.replace("if(cache[key]===0)return;","if(cache[key]===-1)return;")
    for sv in ("save()","saveC()"):
        s=s.replace("const next=i=>{if(i>=list.length){cache[key]=0;%s;return;}"%sv,
                    "const next=(i,bad)=>{if(i>=list.length){if(!bad){cache[key]=-1;%s;}return;}"%sv)
    s=s.replace(".then(r=>r.ok?r.json():null).then(j=>{const u=j&&(j.thumbnail&&j.thumbnail.source||j.originalimage&&j.originalimage.source);if(u){cache[key]=u;save();show(u);}else next(i+1);}).catch(()=>next(i+1));",
                ".then(r=>r.ok?r.json():r.status===404?null:Promise.reject(r.status)).then(j=>{const u=j&&(j.thumbnail&&j.thumbnail.source||j.originalimage&&j.originalimage.source);if(u){cache[key]=u;save();show(u);}else next(i+1,bad);},()=>next(i+1,1));")
    s=s.replace(".then(r=>r.ok?r.json():null).then(j=>{const u=j&&(j.thumbnail&&j.thumbnail.source||j.originalimage&&j.originalimage.source);if(u){cache[key]=u;saveC();show(u);}else next(i+1);}).catch(()=>next(i+1));",
                ".then(r=>r.ok?r.json():r.status===404?null:Promise.reject(r.status)).then(j=>{const u=j&&(j.thumbnail&&j.thumbnail.source||j.originalimage&&j.originalimage.source);if(u){cache[key]=u;saveC();show(u);}else next(i+1,bad);},()=>next(i+1,1));")
    n=s.count("next(i+1,1)");print(f,"ersetzt:",n,"rest0:",s.count("cache[key]=0"))
    open(f,'w',encoding='utf-8').write(s)
# Nachtrag: -1 ist in JS "wahr", daher vor der Cache-Prüfung abfragen; PASSAGE: saveC führt zusammen statt zu überschreiben (drei Kopien teilen zl_pics)
for f in sys.argv[1:]:
    s=open(f,encoding='utf-8').read()
    s=s.replace("if(cache[key]){show(cache[key]);return;}if(cache[key]===-1)return;","if(cache[key]===-1)return;if(cache[key]){show(cache[key]);return;}")
    s=s.replace("const saveC=()=>{try{localStorage.setItem('zl_pics',JSON.stringify(cache))}catch(e){}};","const saveC=()=>{try{const o=JSON.parse(localStorage.getItem('zl_pics')||'{}');for(const k in cache)o[k]=cache[k];for(const k in o)if(!(k in cache))cache[k]=o[k];localStorage.setItem('zl_pics',JSON.stringify(o))}catch(e){}}; /* Audit 27.11.: drei Kopien teilen sich zl_pics – zusammenführen statt überschreiben */")
    open(f,'w',encoding='utf-8').write(s)
