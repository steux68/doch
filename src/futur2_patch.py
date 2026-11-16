import re,sys
sys.path.insert(0,"src")
from _gt_common import Q,card,R,tc
p="index.html"; s=open(p,encoding="utf-8").read()
i=s.index("GT.praet="); j=s.index("\n/* ",i); b=s[i:j]
if "Futur II" in b and 'b:"Futur II"' in b: sys.exit("already patched")
c1=card("Futur II",R("werden + Partizip II + haben/sein",["Bis morgen werde ich es gelernt haben.","Er wird den Zug verpasst haben. (guess)","Sie wird schon angekommen sein. (guess)","Bis Montag wird er gegangen sein."]),"Finished by a point in the future, or a guess about the past","Two uses: something will be finished by a future time, or a guess about something that already happened. Gehen, ankommen take sein; most others take haben. It is rare in speech.")
c2=card("Keine Verlaufsform",R("No -ing form",["Ich lese gerade ein Buch.","Er schläft noch.","Sie telefoniert immer noch.","Ich bin am Lesen. (spoken, informal)"]),"English I am reading → just the Präsens","German has no continuous tense. Add gerade, noch or immer noch if you want to stress that it is happening now. The Perfekt is not a continuous form either.")
qs=[
Q("Bis morgen ___ ich den Text gelesen haben.",["werde","habe","wurde"],"Futur II: werden + Partizip II + haben.","C1"),
Q("Bis Montag wird er schon nach Wien ___ sein. (fahren)",["gefahren","fahren","gefahrt"],"Futur II with sein: gefahren sein.","C1"),
Q("Sie ist nicht da. Sie wird den Zug verpasst ___.",["haben","sein","werden"],"A guess about the past: werden + Partizip II + haben.","C1"),
Q("Er wird schon ___ sein. (ankommen)",["angekommen","ankommen","kommt an"],"Futur II: the Partizip II is angekommen, with sein.","C1"),
Q("Englisch: I am reading a book. Deutsch: Ich lese ___ ein Buch.",["gerade","am","lesend"],"There is no -ing form. Gerade shows that it is happening now.","B1"),
Q("Was machst du? – Ich ___ gerade.",["koche","bin kochen","werde kochen"],"The Präsens with gerade. No continuous form.","A2"),
Q("Er schläft ___. (still)",["noch","gerade","bald"],"noch = still, as before.","A2"),
Q("Sie ___ immer noch am Telefon.",["ist","wird","hat"],"sein + am Telefon, with immer noch for emphasis.","B1")]
assert len(set(q.split("o:")[1][:30] for q in qs))==8
b=b.replace('"}],\n q:[','"},\n'+c1+',\n'+c2+'],\n q:[',1)
b=b.replace('],\n th:`',',\n'+",\n".join(qs)+'],\n th:`',1) if False else b
k=b.index("],\n th:`"); b=b[:k]+",\n"+",\n".join(qs)+b[k:]
tafel=('<div class="tc df"><h3>Zeitachse</h3><div class="rows"><div><span>Plusquamperfekt</span><span>Ich hatte gelernt.</span></div><div><span>Präteritum</span><span>Ich lernte.</span></div><div><span>Perfekt</span><span>Ich habe gelernt.</span></div><div><span>Präsens</span><span>Ich lerne.</span></div><div><span>Futur I</span><span>Ich werde lernen.</span></div><div><span>Futur II</span><span>Ich werde gelernt haben.</span></div></div><p class="tline">Von früher nach später, von oben nach unten.</p></div>')
b=b[:-3]+tafel+"`};" if b.endswith("`};") else sys.exit("th-Ende")
s=s[:i]+b+s[j:]
m=re.search(r'name="app-version" content="(\d{4}-\d\d-\d\d)([a-z]?)"',s)
s=s.replace(m.group(0),'name="app-version" content="%s%s"'%(m.group(1),chr(ord(m.group(2))+1)))
open(p,"w",encoding="utf-8").write(s); print("OK")
