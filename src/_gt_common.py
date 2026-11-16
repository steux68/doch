"""Gemeinsame Helfer für die Overnight-Patches (plural, komp, zeit, indef)."""
import re, sys
def J(l): return "["+",".join('"%s"'%x for x in l)+"]"
def Q(sent,o,why,lv): return ' {s:"%s",o:%s,why:"%s",lv:"%s"}'%(sent,J(o),why,lv)
def rows(items): return '<div class="rows">'+"".join('<div><span>%s</span><span>%s</span></div>'%(a,b) for a,b in items)+'</div>'
def tc(h,items,note): return '<div class="tc df"><h3>%s</h3>%s<p class="tline">%s</p></div>'%(h,rows(items),note)
def card(b,st,tx,gt): return ' {b:"%s",st:%s,tx:"%s",gt:"%s"}'%(b,st,tx,gt)
def R(h,l): return 'ruleSt("%s",%s)'%(h,J(l))

def apply(key,name,badge,tip,lg,C,QS,TH,after_t,topic_line,grp_old,grp_new,lab):
    p="index.html"; s=open(p,encoding="utf-8").read()
    if "GT.%s="%key in s: sys.exit("already patched")
    assert len(QS)==24, len(QS)
    assert 7<=len(C)<=9, len(C)
    BL=('GT.%s={name:"%s",badge:"%s",tip:"%s",src:["duden","grammis","lingolia"],\n lg:\'%s\',\n cards:[\n'%(key,name,badge,tip,lg)
        +",\n".join(C)+'],\n q:[\n'+",\n".join(QS)+'],\n th:`'+"".join(TH)+'`};\n')
    a='/* ---------- topics + home ---------- */'
    if s.count(a)!=1: sys.exit("Anker topics")
    s=s.replace(a,"/* %s */\n"%key+BL+a)
    a=' {t:"%s",'%after_t
    i=s.find(a); assert i>0
    j=s.index("\n",i)+1
    s=s[:j]+topic_line+"\n"+s[j:]
    if s.count(grp_old)!=1: sys.exit("Anker Gruppe")
    s=s.replace(grp_old,grp_new)
    a='if(k==="praet")return'
    if s.count(a)!=1: sys.exit("Anker lab")
    s=s.replace(a,'if(k==="%s")return "%s";'%(key,lab)+a)
    m=re.search(r'name="app-version" content="(\d{4}-\d\d-\d\d)([a-z]?)"',s)
    s=s.replace(m.group(0),'name="app-version" content="%s%s"'%(m.group(1),chr(ord(m.group(2) or "`")+1)))
    open(p,"w",encoding="utf-8").write(s); print("OK",key)
