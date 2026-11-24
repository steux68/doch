#!/usr/bin/env python3
"""DOCH: Abstaende vereinheitlichen. In margin/padding/gap (nur <style>-Bloecke, nur positive px):
6,7,9,10,11 -> 8 ; 14 -> 12. Alles andere bleibt. Idempotent (Marker-Style)."""
import re, sys
p="index.html"; s=open(p,encoding="utf-8").read()
if 'id="abstand-marker"' in s: sys.exit("already patched")
MAP={"6":"8","7":"8","9":"8","10":"8","11":"8","14":"12"}
n=[0]
def fix_decl(m):
    def px(v):
        k=v.group(2)
        if v.group(1)=="-" or k not in MAP: return v.group(0)
        n[0]+=1; return MAP[k]+"px"
    val=re.sub(r'(?<![\w.])(-?)(\d+)px',px,m.group(3))
    return m.group(1)+val
pat=re.compile(r'((?<![-\w])(?:margin|padding|gap|row-gap|column-gap)(?:-(?:top|bottom|left|right))?\s*:\s*)([^;}{]*)')
def fix_decl2(m):
    pre,val=m.group(1),m.group(2)
    def px(v):
        if v.group(1)=="-" or v.group(2) not in MAP: return v.group(0)
        n[0]+=1; return MAP[v.group(2)]+"px"
    return pre+re.sub(r'(?<![\w.])(-?)(\d+)px',px,val)
def style(m): return m.group(1)+pat.sub(fix_decl2,m.group(2))+m.group(3)
s=re.sub(r'(<style[^>]*>)(.*?)(</style>)',style,s,flags=re.S)
i=s.rfind('</style>'); j=s.index('\n',i)+1
s=s[:j]+'<style id="abstand-marker">/* Abstaende: 6,7,9,10,11 -> 8; 14 -> 12 */</style>\n'+s[j:]
m=re.search(r'name="app-version" content="(\d{4}-\d\d-\d\d)([a-z]?)"',s)
new=m.group(1)+chr(ord(m.group(2) or "`")+1)
s=s.replace(m.group(0),'name="app-version" content="%s"'%new)
open(p,"w",encoding="utf-8").write(s); print("OK",new,"changed",n[0])
