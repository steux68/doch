#!/usr/bin/env python3
"""Wrong-option explanations (2026-11-21r+). Reads src/wx/*.json, resolves questions through the live app, writes <script id="wx-data"> and hooks the feedback.
Entry format per file: {"topic": "k2", "items": [[index, "first 14 chars of the stem", {"wrong option": "reason", ...}], ...]}
topic is a GT key or one of PQ, PRON_Q, GEN_Q, FALL_Q, ADJ_Q. Idempotent: rebuilds the data block every run."""
import os,re,json,glob,sys
from playwright.sync_api import sync_playwright
root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
p=os.path.join(root,"index.html");s=open(p,encoding="utf-8").read()
BLOCK='''  var h=nf.innerHTML.trim();
  var CN={nom:"Nominativ",akk:"Akkusativ",dat:"Dativ",gen:"Genitiv"},cs=(q.cs&&k&&q.t!=="adj")?" · hier: <b>"+(CN[String(q.cs).toLowerCase()]||q.cs)+"</b>":"";
  if(k&&h.indexOf(" = ")<0)h="<b>"+(q.t==="adj"?"-"+w.replace(/^-/,""):w)+"</b> = "+k+cs+(h?" · "+h:"");
  if(q.t==="art"&&q.noun){var G={"der":"maskulin","die":"feminin (oder Plural)","das":"neutral"},c0=q.o[q.c];if(G[w]&&G[c0])h="<b>"+w+"</b> = "+G[w]+" · <b>"+q.noun+"</b> ist "+G[c0].replace(" (oder Plural)","")+": <b>"+c0+"</b>";}
  var wr=window.WX&&WX[q.s+"|"+w];if(wr)h='<span class="wxr">'+wr+"</span>"+(h?"<br>"+h:"");
'''
m=re.search(r'  var h=nf\.innerHTML\.trim\(\);\n.*?(?=  if\(!nf\.querySelector\("\.wxl"\)\))',s,re.S)
assert m,"hook region not found"
s=s[:m.start()]+BLOCK+s[m.end():]
if "#nf .wxr" not in s:
    a='<script id="wx2-js">'
    assert s.count(a)==1
    s=s.replace(a,'<style id="wx3-css">#nf .wxr{color:#3a3c37}</style>\n'+a)
# resolve questions
items=[]
for f in sorted(glob.glob(os.path.join(root,"src","wx","*.json"))):
    d=json.load(open(f,encoding="utf-8"))
    for it in d["items"]: items.append((d["topic"],it))
with sync_playwright() as pw:
    b=pw.chromium.launch();pg=b.new_page()
    pg.route("**/*",lambda r:r.continue_() if r.request.url.startswith("file:") else r.abort())
    pg.goto("file://"+p);pg.wait_for_timeout(600)
    src=pg.evaluate("""()=>{const m={};for(const k of Object.keys(GT))m[k]=GT[k].q.map(q=>({s:q.s,o:q.o,c:q.c||0}));m.PQ=PQ.map(q=>({s:q.s,o:q.o,c:q.c||0}));m.PRON_Q=PRON_Q.map(q=>({s:q.s,o:q.o,c:q.c||0}));m.GEN_Q=GEN_Q.map(q=>({s:q.s,o:q.o,c:q.c||0}));m.FALL_Q=FALL_Q.map(q=>({s:q.s,o:q.o,c:q.c||0}));m.ADJ_Q=ADJ_Q.map(q=>({s:q.s,o:q.o,c:q.c||0}));return m}""")
    b.close()
WX={};bad=0;n=0
for t,(i,st,x) in items:
    q=src[t][i]
    if not q["s"].startswith(st): print("MISMATCH",t,i,st,"|",q["s"][:30]);bad+=1;continue
    for opt,why in x.items():
        if opt not in q["o"]: print("NO OPTION",t,i,opt);bad+=1;continue
        if q["o"].index(opt)==q["c"]: print("CORRECT OPTION",t,i,opt);bad+=1;continue
        WX[q["s"]+"|"+opt]=why;n+=1
if bad: sys.exit("fix errors first")
blk='<script id="wx-data">window.WX='+json.dumps(WX,ensure_ascii=False,separators=(",",":"))+';</script>'
if '<script id="wx-data">' in s: s=re.sub(r'<script id="wx-data">.*?</script>',lambda m:blk,s,count=1,flags=re.S)
else:
    a='<style id="wx3-css">'; s=s.replace(a,blk+"\n"+a,1)
ver=sys.argv[1] if len(sys.argv)>1 else None
if ver: s=re.sub(r'<meta name="app-version" content="[^"]+">','<meta name="app-version" content="%s">'%ver,s,count=1)
open(p,"w",encoding="utf-8").write(s);print("ok",n,"explanations")
