# DOCH! 26.11.2026: Finger-Weg Schritt "Thema": nach dem Tipp auf Knoten 01 zeigt ein Punkt neben "Satzbau" + Etikett "Tippe ein Thema."
# Zaehler doch-fw: 1 = Punkt getippt, 2 = Thema getippt, 3 = Pfeil gesehen. Baut auf finger_weg_patch.py auf. Idempotent.
import re, sys
s = open('index.html', encoding='utf-8').read()
if 'function showTile' in s: sys.exit('schon angewendet')
def rep(a, b):
    global s
    assert s.count(a) == 1, a
    s = s.replace(a, b)
rep('var K="doch-fw",els=[],tm=0;', 'var K="doch-fw",els=[],tm=0,mode=0;')
rep('lab("Tippe einen Punkt.",st.left,y-14-8-26,"l",0);arm();}', 'lab("Tippe einen Punkt.",st.left,y-14-8-26,"l",0);mode=1;arm();}')
rep('function show2(){clear();if(get()>=2)return;', 'function show2(){clear();if(get()>=3)return;')
rep('lab("weiter",cx,r.bottom+42,"c",r.right);arm();}', 'lab("weiter",cx,r.bottom+42,"c",r.right);mode=3;arm();}')
tile = ('function showTile(){clear();if(get()>=2||get()<1)return;var h=$("home"),t=document.getElementById("t-satz");if(!h||h.hidden||!t)return;var r=t.getBoundingClientRect();if(r.width<10||r.top<110||r.bottom>window.innerHeight-60)return;'
        'var bb=t.querySelector("b"),br=bb?bb.getBoundingClientRect().right:r.left+60,x=br+(r.right-br)*0.3,y=r.top+17;dot(x,y,0,-5);lab("Tippe ein Thema.",Math.max(x-8,104),r.top-60,"l",0);mode=2;arm();}\n')
rep('document.addEventListener("pointerdown"', tile + 'document.addEventListener("pointerdown"')
m = re.search(r'document\.addEventListener\("pointerdown",function\(e\)\{.*?\},true\);', s, re.S)
assert m
new = ('document.addEventListener("pointerdown",function(e){if(!els.length)return;var t=e.target,c=t.closest?t:null,m=mode;clear();'
       'if(m===1){if(c&&c.closest("#tstage .pin")){put(1);setTimeout(showTile,1300);}return;}'
       'if(m===2){put(2);return;}if(m===3)put(3);},true);')
s = s[:m.start()] + new + s[m.end():]
if '--noversion' not in sys.argv:
    s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda mm: mm.group(1) + '2026-11-26s' + mm.group(3), s, count=1)
open('index.html', 'w', encoding='utf-8').write(s)
print('ok')
