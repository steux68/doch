#!/usr/bin/env python3
"""DOCH: Österreichisch um Café-/Stadt-Wörter erweitern (2 Karten, 8 Fragen)."""
import re, sys
p="index.html"; s=open(p,encoding="utf-8").read()
if 'b:"Café"' in s: sys.exit("already patched")
i=s.index("GT.oest="); j=s.index("\nGT.",i+5)
blk=s[i:j]
C=(' {b:"Café",st:ruleSt("Café und Gasthaus",["Melange (Milchkaffee)","Seidl (kleines Bier, 0,3 l)","Spritzer (Weißweinschorle)","Beisl (einfaches Wirtshaus)"]),tx:"Drinks and places in Vienna",gt:"A Melange is coffee with a lot of hot milk. A Seidl is a small beer. In a Beisl you eat simple Austrian food."},\n'
   ' {b:"Stadt",st:ruleSt("Stadt und Wohnung",["Bankomat (Geldautomat)","Anrainer (Anwohner)","Fenstertag (Brückentag)","Eiskasten (Kühlschrank)"]),tx:"Words on signs and in conversation",gt:"Anrainer frei means residents only. A Fenstertag is a working day between a holiday and the weekend."},\n')
a=' {b:"Amt",'
assert blk.count(a)==1
blk=blk.replace(a,C+a)
def Q(s_,o,w,lv): return ' {s:"%s",o:[%s],why:"%s",lv:"%s"}'%(s_,",".join('"%s"'%x for x in o),w,lv)
N=",\n".join([
 Q("Der Kühlschrank heißt in Österreich oft ___.",["Eiskasten","Kasten","Kassa"],"Eiskasten = Kühlschrank.","B1"),
 Q("Der Geldautomat heißt in Österreich ___.",["Bankomat","Trafik","Kassa"],"Bankomat = Geldautomat.","B1"),
 Q("Ein Arbeitstag zwischen Feiertag und Wochenende heißt ___.",["Fenstertag","Feiertag","Jausentag"],"Fenstertag = Brückentag.","B1"),
 Q("Die Anwohner nennt man in Österreich ___.",["Anrainer","Fleischhauer","Tischler"],"Anrainer = Anwohner.","B2"),
 Q("Ein Milchkaffee heißt in Wien ___.",["Melange","Spritzer","Seidl"],"Melange = Milchkaffee.","B1"),
 Q("Ein kleines Bier (0,3 l) heißt in Österreich ___.",["Seidl","Spritzer","Melange"],"Seidl = kleines Bier.","B1"),
 Q("Weißweinschorle heißt in Österreich ___.",["Spritzer","Seidl","Melange"],"Spritzer = Weißweinschorle.","B1"),
 Q("Ein einfaches Wirtshaus nennt man in Wien ___.",["Beisl","Trafik","Spital"],"Beisl = einfaches Wirtshaus.","B1"),
])
k=blk.index("],\n th:`")
blk=blk[:k].rstrip()+",\n"+N+blk[k:]
s=s[:i]+blk+s[j:]
m=re.search(r'name="app-version" content="(\d{4}-\d\d-\d\d)([a-z]?)"',s)
s=s.replace(m.group(0),'name="app-version" content="%s%s"'%(m.group(1),chr(ord(m.group(2) or "`")+1)))
open(p,"w",encoding="utf-8").write(s); print("OK")
