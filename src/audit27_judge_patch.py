# Audit 27.11., Punkt 6: judge() meldet kein "Fast richtig", wenn eine der falschen Antworten (q.o ohne q.c) getippt wurde; Wrapper in falsch2 reicht den 3. Parameter durch; "gekommen" doppelt -> "gekamen".
import sys
f=sys.argv[1] if len(sys.argv)>1 else "index.html";s=open(f,encoding='utf-8').read()
R=[('function judge(inp,ans){const a=inp.trim().replace(/\\s+/g," "),b=ans;if(!a)return ["no",""];if(a===b)return ["ok",""];',
    'function judge(inp,ans,wrong){const a=inp.trim().replace(/\\s+/g," "),b=ans;if(!a)return ["no",""];if(a===b)return ["ok",""];\n  if(wrong&&wrong.some(w=>w.trim().replace(/\\s+/g," ")===a))return ["no",""]; /* Audit 27.11., Punkt 6: eine der falschen Antworten getippt = Grammatikfehler, kein Tippfehler */'),
   ('[r,why]=judge(inp,q.o[q.c]);','[r,why]=judge(inp,q.o[q.c],q.o.filter((x,k)=>k!==q.c));'),
   ('judge=function(a,b){var r=oj(a,b);','judge=function(a,b,w){var r=oj(a,b,w);'),
   ('"o":["gekommen","gekommt","gekommen"]','"o":["gekommen","gekommt","gekamen"]')]
for a,b in R:s=s.replace(a,b)
open(f,'w',encoding='utf-8').write(s)
