#!/usr/bin/env python3
"""DOCH: Grautöne vereinheitlichen - Rahmen/Linien #999 #bbb #bfbfbf -> #b8b8b8; Textgrau #999 -> #8a8a86."""
import re
p="index.html"; s=open(p,encoding="utf-8").read()
n0=len(re.findall(r"#999\b|#bbb\b|#bfbfbf\b",s))
if n0==0: raise SystemExit("already patched")
s=re.sub(r"(border[a-z-]*:[^;{}]*?)#(?:999|bbb)\b",r"\1#b8b8b8",s)   # Rahmen
s=s.replace("#bfbfbf","#b8b8b8")                                    # Pins, Linien
s=re.sub(r"(?<![0-9a-fA-F])#999\b","#8a8a86",s)                     # Textgrau
s=re.sub(r"(?<![0-9a-fA-F])#bbb\b","#b8b8b8",s)
s,c=re.subn(r'(<meta name="app-version" content="2026-11-24)([a-z])(")',lambda m:m.group(1)+chr(ord(m.group(2))+1)+m.group(3),s,count=1); assert c==1
open(p,"w",encoding="utf-8").write(s); print("ok",n0,"->",len(re.findall(r"#999\b|#bbb\b|#bfbfbf\b",s)))
