import re, sys
p = "index.html"
s = open(p, encoding="utf-8").read()
if "const SVWN=" in s:
    sys.exit("already patched")

def rep(a, b):
    global s
    assert s.count(a) == 1, a[:70]
    s = s.replace(a, b)

rep('rl:{g:"W",i:0,wo:0}}', 'rl:{g:"W",i:0,wo:0,n:0}}')

data = r'''
/* Wechsel-Roller: pro Präposition Rahmensatz (Wo?/Wohin?) und vier Nomen m / f / n / Plural */
const SVWN={
an:["Das Bild hängt {an} [NP].","Ich hänge das Bild {an} [NP].",["Schrank","Wand","Fenster","Wände"]],
auf:["Das Buch liegt {auf} [NP].","Ich lege das Buch {auf} [NP].",["Tisch","Bank","Sofa","Stühle"]],
hinter:["Das Auto steht {hinter} [NP].","Ich fahre das Auto {hinter} [NP].",["Baum","Garage","Haus","Bäume"]],
in:["Ich bin {in} [NP].","Ich gehe {in} [NP].",["Garten","Küche","Zimmer","Räume"]],
neben:["Die Lampe steht {neben} [NP].","Ich stelle die Lampe {neben} [NP].",["Schrank","Tür","Sofa","Stühle"]],
"über":["Die Lampe hängt {über} [NP].","Ich hänge die Lampe {über} [NP].",["Tisch","Couch","Bett","Tische"]],
unter:["Die Katze liegt {unter} [NP].","Die Katze kriecht {unter} [NP].",["Tisch","Bank","Bett","Stühle"]],
vor:["Der Wagen steht {vor} [NP].","Ich stelle den Wagen {vor} [NP].",["Baum","Tür","Haus","Bäume"]],
zwischen:["Der Stuhl steht {zwischen} [NP] und der Tür.","Ich stelle den Stuhl {zwischen} [NP] und die Tür.",["Tisch","Wand","Sofa","Tische"]]};
function svWS(w,wo,n){const d=SVWN[w];let no=d[2][n];if(!wo&&n===3&&!/[ns]$/.test(no))no+="n";return d[wo?1:0].replace("[NP]","["+SVW[n][wo?1:2]+" "+no+"]");}
'''
rep('function svSub(){', data + 'function svSub(){')

# Wort row for Wechsel
rep("""+'</div>'
    :'<div class="svg" style="--n:1;margin-top:3px"><span class="svb svbn" style="background:'+q.c+'">immer '+q.n+'</span></div>';""",
    """+'</div><div class="svg" id="svrn" style="--n:4;margin-top:3px">'+["der","die","das","Plural"].map((x,i)=>'<span role="button" tabindex="0" class="svb svo fr'+(R.n===i?' on':'')+'" data-rn="'+i+'">'+x+'</span>').join('')+'</div>'
    :'<div class="svg" style="--n:1;margin-top:3px"><span class="svb svbn" style="background:'+q.c+'">immer '+q.n+'</span></div>';""")
rep('const sent=w=>svFmt(R.g==="W"?q.s[w][R.wo]:q.s[w][0]);',
    'const sent=w=>R.g==="W"?svFmt(svWS(w,R.wo,R.n)):svFmt(q.s[w][0]);')
rep('if(b.dataset.i!==undefined){const i=+b.dataset.i;marks(i);go(i,true);return true;}return false;};',
    'if(b.dataset.rn!==undefined){R.n=+b.dataset.rn;root.querySelectorAll("[data-rn]").forEach(x=>x.classList.toggle("on",+x.dataset.rn===R.n));cols();go(R.i,false);return true;}\n      if(b.dataset.i!==undefined){const i=+b.dataset.i;marks(i);go(i,true);return true;}return false;};')
m = re.search(r'name="app-version" content="(\d{4}-\d\d-\d\d)([a-z]?)"', s)
s = s.replace(m.group(0), 'name="app-version" content="%s%s"' % (m.group(1), chr(ord(m.group(2) or "`") + 1)))
open(p, "w", encoding="utf-8").write(s)
print("ok")
