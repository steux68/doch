#!/usr/bin/env python3
"""DOCH: eight more Modalpartikeln questions (24 → 32), 27 Nov 2026. Own wording."""
import re, sys
p = "index.html"; s = open(p, encoding="utf-8").read()
if "/* mpart-mehr */" in s: sys.exit("already patched")
QS = [
 ("Wo warst du ___ so lange? (neugierig)", ["denn","doch","halt"], "In Fragen zeigt denn Interesse.", "B1"),
 ("Das kann ___ nicht wahr sein! (empört)", ["doch","denn","mal"], "doch drückt hier Empörung aus.", "B2"),
 ("Setz dich ___ hin, ich bringe dir einen Tee.", ["doch","denn","wohl"], "Freundliche Aufforderung: doch.", "B1"),
 ("Du hast ___ recht, aber trotzdem sehe ich es anders. (Zugeständnis)", ["schon","denn","mal"], "schon räumt etwas ein, bevor ein Aber kommt.", "B2"),
 ("Was ist ___ passiert? (neugierig)", ["denn","halt","mal"], "In Fragen zeigt denn Interesse.", "B1"),
 ("Schau ___, wer da ist!", ["mal","denn","wohl"], "mal macht die Aufforderung leicht.", "A2"),
 ("Wir müssen ___ damit leben. (Resignation)", ["halt","denn","aber"], "halt: Es ist nicht zu ändern.", "B1"),
 ("Es ist ___ so: Man kann nicht alles haben.", ["eben","denn","mal"], "eben: So ist es nun einmal.", "B2"),
]
def J(l): return "[" + ",".join('"%s"' % x for x in l) + "]"
def Q(t): return ' {s:"%s",o:%s,why:"%s",lv:"%s"}' % (t[0], J(t[1]), t[2], t[3])
st = s.find("GT.mpart={"); q = s.find(" q:[", st); end = s.find("}],\n th:`", q)
if st < 0 or q < 0 or end < 0: sys.exit("Anker mpart")
have = set(re.findall(r'\{s:"([^"]*)"', s[q:end]))
for t in QS:
    if t[0] in have: sys.exit("duplicate " + t[0])
s = s[:end] + "},\n" + ",\n".join(Q(t) for t in QS) + s[end + 1:]
s = s.replace("/* ---------- topics + home ---------- */", "/* mpart-mehr */\n/* ---------- topics + home ---------- */", 1)
new = "2026-11-27-fragen2"
m = re.search(r'name="app-version" content="([^"]*)"', s)
s = s.replace(m.group(0), 'name="app-version" content="%s"' % new)
open(p, "w", encoding="utf-8").write(s); open("version.txt", "w").write(new + "\n")
print("OK", new)
