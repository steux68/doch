#!/usr/bin/env python3
"""DOCH: zwei neue Themen aus den PDFs: 'Verben & Fälle' (vkas) und 'Präpositionen & Fall' (pfall), eigene Formulierung."""
import re, sys
p="index.html"; s=open(p,encoding="utf-8").read()
if "GT.vkas=" in s: sys.exit("already patched")
def J(l): return "["+",".join('"%s"'%x for x in l)+"]"
def Q(sent,o,why,lv): return ' {s:"%s",o:%s,why:"%s",lv:"%s"}'%(sent,J(o),why,lv)
def rows(items): return '<div class="rows">'+"".join('<div><span>%s</span><span>%s</span></div>'%(a,b) for a,b in items)+'</div>'
def tc(h,items,note): return '<div class="tc df"><h3>%s</h3>%s<p class="tline">%s</p></div>'%(h,rows(items),note)

VK_CARDS=[
 ('Akkusativ','ruleSt("Most verbs: + Akkusativ",["Ich sehe den Hengst.","Wir brauchen einen Plan.","Sie besucht ihre Tante.","Er kauft das Buch."])','Direct object: Wen oder was?','sehen, brauchen, besuchen, kaufen, haben, machen, lesen, suchen, finden …'),
 ('Dativ','ruleSt("helfen · danken · gehören · gefallen",["Ich helfe dem Nachbarn.","Das Pferd gehört mir.","Der Entwurf gefällt der Kundin.","Wir danken Ihnen."])','A small group takes only the Dativ','Also: antworten, folgen, passen, schmecken, fehlen, zuhören, glauben (a person), begegnen.'),
 ('Dat + Akk','ruleSt("geben · zeigen · schenken · schicken",["Ich gebe dem Bauherrn den Plan.","Sie zeigt mir das Zimmer.","Er schenkt seiner Mutter einen Ring.","Wir schicken Ihnen die Rechnung."])','Two objects: person Dativ, thing Akkusativ','Also: bringen, erklären, empfehlen, leihen, schreiben, sagen. Two nouns: Dativ first. Two pronouns: Akkusativ first.'),
 ('Nominativ','ruleSt("sein · werden · bleiben",["Er ist Architekt.","Sie wird Ärztin.","Das bleibt ein Geheimnis."])','The noun after these verbs stays Nominativ','There is no object here. The noun says the same as the subject. Also: heißen, scheinen.'),
 ('Fallen','ruleSt("Same meaning, different case",["helfen + Dativ, but unterstützen + Akkusativ","folgen + Dativ, but begleiten + Akkusativ","antworten + Dativ, but fragen + Akkusativ"])','Check each new verb in a dictionary','Ich helfe ihm, but Ich unterstütze ihn. English does not show the difference, so learn the case with the verb.'),
 ('Reflexiv','ruleSt("mich or mir?",["Ich wasche mich. (Akkusativ)","Ich wasche mir die Hände. (Dativ)","Ich kaufe mir ein Buch. (Dativ)"])','With another object, mich becomes mir','If the sentence already has an Akkusativ object, the reflexive pronoun is Dativ.'),
 ('Genitiv','ruleSt("bedürfen · gedenken",["Das bedarf einer Erklärung.","Wir gedenken der Opfer."])','Very few verbs, formal (C1)','Rare in everyday speech. You will meet them in speeches, laws and written reports.'),
]
VK_Q=[
 Q("Ich helfe ___ Nachbarn.",["dem","den","der"],"helfen + Dativ: dem Nachbarn.","A2"),
 Q("Wir besuchen ___ Großeltern.",["die","den","der"],"besuchen + Akkusativ: die Großeltern.","A1"),
 Q("Das Pferd gehört ___.",["mir","mich","ich"],"gehören + Dativ: mir.","A2"),
 Q("Der Entwurf gefällt ___ Kundin.",["der","die","den"],"gefallen + Dativ; feminine → der Kundin.","A2"),
 Q("Ich brauche ___ neuen Plan.",["einen","einem","ein"],"brauchen + Akkusativ; masculine → einen.","A1"),
 Q("Kannst du ___ bitte helfen? (ich)",["mir","mich","ich"],"helfen + Dativ: mir.","A2"),
 Q("Ich danke ___ für die Einladung. (Sie)",["Ihnen","Sie","Ihr"],"danken + Dativ: Ihnen.","A2"),
 Q("Er schenkt ___ Mutter einen Ring.",["seiner","seine","seinem"],"schenken: the person is Dativ; feminine → seiner.","A2"),
 Q("Sie zeigt ___ das Zimmer. (wir)",["uns","wir","unser"],"zeigen: the person is Dativ: uns.","A2"),
 Q("Ich frage ___ Lehrer.",["den","dem","der"],"fragen + Akkusativ: den Lehrer.","A2"),
 Q("Ich antworte ___ Lehrerin.",["der","die","den"],"antworten + Dativ; feminine → der Lehrerin.","B1"),
 Q("Wir folgen ___ Weg.",["dem","den","der"],"folgen + Dativ: dem Weg.","B1"),
 Q("Ich unterstütze ___ Kollegen.",["den","dem","der"],"unterstützen + Akkusativ: den Kollegen.","B1"),
 Q("Das Kleid passt ___ sehr gut. (sie)",["ihr","sie","ihrer"],"passen + Dativ: ihr.","B1"),
 Q("Das Essen schmeckt ___ nicht. (er)",["ihm","ihn","er"],"schmecken + Dativ: ihm.","A2"),
 Q("Mir fehlt ___ Stift.",["ein","einen","einem"],"fehlen + Dativ for the person; the missing thing is the subject, so Nominativ: ein Stift.","B1"),
 Q("Ich wasche ___ die Hände. (ich)",["mir","mich","ich"],"Another Akkusativ object (die Hände) is present, so the pronoun is Dativ: mir.","B1"),
 Q("Ich wasche ___. (ich)",["mich","mir","ich"],"No other object: the pronoun is Akkusativ: mich.","B1"),
 Q("Er ist ___ Architekt.",["ein","einen","einem"],"After sein the noun stays Nominativ: ein Architekt.","A2"),
 Q("Ich glaube ___ nicht. (er)",["ihm","ihn","er"],"glauben + Dativ when you believe a person: ihm.","B1"),
 Q("Der Lehrer erklärt ___ Schülern die Regel.",["den","die","dem"],"erklären: the person is Dativ; plural → den Schülern.","B1"),
 Q("Ich leihe ___ mein Fahrrad. (du)",["dir","dich","du"],"leihen: the person is Dativ: dir.","B1"),
 Q("Wir gedenken ___ Opfer.",["der","die","den"],"gedenken + Genitiv (C1); plural → der.","C1"),
 Q("Das Projekt bedarf ___ Genehmigung.",["einer","eine","einem"],"bedürfen + Genitiv (C1); feminine → einer.","C1"),
]
VK_TH=''.join([
 tc("Welcher Fall?",[("Wen oder was?","Akkusativ: Ich sehe den Plan."),("Wem?","Dativ: Ich helfe dem Nachbarn."),("Wer oder was?","Nominativ: Der Plan ist neu.")],"Ask the question after the verb. The answer tells you the case."),
 tc("Nur Dativ",[("helfen","Ich helfe dir."),("danken","Wir danken Ihnen."),("gehören","Das gehört mir."),("gefallen","Es gefällt ihr."),("antworten","Er antwortet dem Chef."),("folgen","Sie folgt dem Weg.")],"Also: passen, schmecken, fehlen, zuhören, begegnen."),
 tc("Zwei Objekte",[("Person","Dativ: Ich gebe dem Kind"),("Sache","Akkusativ: einen Apfel.")],"geben, zeigen, schenken, schicken, bringen, erklären, empfehlen, leihen."),
])
VK=('GT.vkas={name:"Verben & Fälle",badge:"Verb",tip:"Learn the case together with the verb: helfen + Dativ, brauchen + Akkusativ.",src:["duden","grammis","lingolia"],\n'
 ' lg:\'<span class="lgc akk">Akk</span><span class="lgc dat">Dat</span><span class="lgc nom">Nom</span><span class="lgc gen">Gen</span>\',\n cards:[\n'
 +",\n".join(' {b:"%s",st:%s,tx:"%s",gt:"%s"}'%(b,st,tx,gt) for b,st,tx,gt in VK_CARDS)+'],\n q:[\n'+",\n".join(VK_Q)+'],\n th:`'+VK_TH+'`};\n')

PF_CARDS=[
 ('Akkusativ','ruleSt("bis · durch · entlang · für · gegen · ohne · um",["durch den Park","für meinen Bruder","gegen die Wand","ohne einen Plan"])','Always Akkusativ','entlang usually follows its noun: den Fluss entlang. um + Akkusativ: um den See.'),
 ('Dativ','ruleSt("aus · außer · bei · gegenüber · mit · nach · seit · von · zu",["aus dem Haus","mit meinem Kollegen","seit einem Jahr","zu der Besprechung"])','Always Dativ','gegenüber can follow a pronoun: mir gegenüber. nach is used for cities and countries: nach Wien.'),
 ('Wechsel','ruleSt("an · auf · hinter · in · neben · über · unter · vor · zwischen",["Wo? → Dativ: im Stall","Wohin? → Akkusativ: in den Stall"])','Nine two-way prepositions','Position (Wo?) takes the Dativ, movement (Wohin?) takes the Akkusativ. Practise in Wo oder wohin?'),
 ('Kurzform','ruleSt("am · im · zum · zur · vom · beim · ins · ans",["am Montag (an dem)","zum Arzt (zu dem)","zur Schule (zu der)","ins Kino (in das)"])','Short forms with the article','Use the long form to stress the article: Ich gehe zu dem Arzt, den du empfohlen hast.'),
 ('Genitiv','ruleSt("wegen · trotz · während · statt",["wegen des Regens","trotz der Kälte","während der Sitzung"])','Written and formal: Genitiv','See the Genitiv topic for the full list.'),
 ('Merken','ruleSt("Learn them inside sentences",["Ich fahre mit dem Zug zu meiner Tante.","Ich gehe ohne meinen Schirm durch den Regen."])','One short sentence beats a list','Say the sentence aloud and change the noun: mit dem Bus, mit der Bahn, mit dem Auto.'),
]
PF_Q=[
 Q("Wir gehen durch ___ Park.",["den","dem","der"],"durch + Akkusativ; masculine → den.","A1"),
 Q("Das Geschenk ist für ___ Mutter.",["meine","meiner","meinen"],"für + Akkusativ; feminine stays meine.","A1"),
 Q("Er fährt ohne ___ Auto.",["sein","seinem","seines"],"ohne + Akkusativ; neuter stays sein.","A2"),
 Q("Wir spielen gegen ___ Mannschaft aus Graz.",["die","der","den"],"gegen + Akkusativ; feminine stays die.","A2"),
 Q("Sie läuft um ___ See.",["den","dem","der"],"um + Akkusativ; masculine → den.","A2"),
 Q("Sie kommt aus ___ Schule.",["der","die","dem"],"aus + Dativ; feminine → der.","A1"),
 Q("Ich wohne bei ___ Eltern.",["meinen","meine","meinem"],"bei + Dativ; plural → meinen.","A2"),
 Q("Ich fahre mit ___ Zug.",["dem","den","der"],"mit + Dativ; masculine → dem.","A1"),
 Q("Nach ___ Arbeit gehe ich heim.",["der","die","dem"],"nach + Dativ; feminine → der.","A1"),
 Q("Seit ___ Woche bin ich krank.",["einer","eine","einem"],"seit + Dativ; feminine → einer.","A2"),
 Q("Das ist ein Brief von ___ Kollegen.",["einem","einen","einer"],"von + Dativ; masculine → einem.","A2"),
 Q("Wir gehen zu ___ Besprechung.",["der","die","dem"],"zu + Dativ; feminine → der.","A2"),
 Q("Außer ___ Hund ist niemand zu Hause.",["dem","den","der"],"außer + Dativ; masculine → dem.","B1"),
 Q("Das Hotel liegt gegenüber ___ Bahnhof.",["dem","den","der"],"gegenüber + Dativ; masculine → dem.","B1"),
 Q("Ich gehe ___ Arzt.",["zum","zu den","zur"],"zu + dem = zum (masculine).","A1"),
 Q("Wir treffen uns ___ Bahnhof.",["am","im","zum"],"an + dem = am: at the station.","A1"),
 Q("Ich gehe ___ Kino.",["ins","im","zum"],"in + das = ins (movement, Akkusativ).","A1"),
 Q("Wir fahren ___ Schule.",["zur","zum","im"],"zu + der = zur (feminine).","A1"),
 Q("Ohne ___ Hilfe schaffe ich das nicht. (du)",["deine","deiner","deinen"],"ohne + Akkusativ; feminine stays deine.","A2"),
 Q("Für ___ ist das Geschenk? (wer)",["wen","wem","wer"],"für + Akkusativ: wen?","A2"),
 Q("Mit ___ fährst du? (wer)",["wem","wen","wer"],"mit + Dativ: wem?","A2"),
 Q("Er arbeitet bei ___ Firma.",["einer","eine","einem"],"bei + Dativ; feminine → einer.","A2"),
 Q("Wir sind gegen ___ Idee.",["die","der","den"],"gegen + Akkusativ; feminine stays die.","A2"),
 Q("Aus ___ Fenster sieht man den Hof.",["dem","das","den"],"aus + Dativ; neuter → dem.","A2"),
]
PF_TH=''.join([
 tc("Nur Akkusativ",[("bis","bis morgen · bis Wien"),("durch","durch den Park"),("entlang","den Fluss entlang"),("für","für meinen Bruder"),("gegen","gegen die Wand"),("ohne","ohne einen Plan"),("um","um den See")],"These seven never change their case."),
 tc("Nur Dativ",[("aus","aus dem Haus"),("außer","außer dem Hund"),("bei","bei meinen Eltern"),("gegenüber","dem Bahnhof gegenüber"),("mit","mit dem Zug"),("nach","nach der Arbeit"),("seit","seit einer Woche"),("von","von einem Kollegen"),("zu","zu der Besprechung")],"These nine never change their case."),
 tc("Wechsel & Genitiv",[("an auf hinter in neben über unter vor zwischen","Wo? Dativ · Wohin? Akkusativ"),("wegen trotz während statt","Genitiv: wegen des Regens")],"See Wo oder wohin? and Genitiv for practice."),
])
PF=('GT.pfall={name:"Präpositionen & Fall",badge:"Präposition",tip:"Sort prepositions into groups: always Akkusativ, always Dativ, two-way, Genitiv.",src:["duden","grammis","lingolia"],\n'
 ' lg:\'<span class="lgc akk">Akk</span><span class="lgc dat">Dat</span><span class="lgc gen">Gen</span>\',\n cards:[\n'
 +",\n".join(' {b:"%s",st:%s,tx:"%s",gt:"%s"}'%(b,st,tx,gt) for b,st,tx,gt in PF_CARDS)+'],\n q:[\n'+",\n".join(PF_Q)+'],\n th:`'+PF_TH+'`};\n')

a='/* ---------- topics + home ---------- */'
if s.count(a)!=1: sys.exit("Anker topics")
s=s.replace(a,"/* verben-faelle */\n"+VK+PF+a)
a=' {t:"vprep",n:"Verben mit Präpositionen",tag:"warten auf",ds:"feste Präposition, darauf, woran · A2–B2"},\n'
if s.count(a)!=1: sys.exit("Anker vprep")
s=s.replace(a,a+' {t:"vkas",n:"Verben & Fälle",tag:"helfen + Dativ",ds:"welcher Fall nach welchem Verb, zwei Objekte, mich oder mir · A1–C1"},\n {t:"pfall",n:"Präpositionen & Fall",tag:"mit + Dativ",ds:"immer Akkusativ, immer Dativ, Kurzformen · A1–B2"},\n')
a='{n:"Präpositionen",t:["prep","vprep"],soon:"Zeitangaben"}'
if s.count(a)!=1: sys.exit("Anker Gruppe")
s=s.replace(a,'{n:"Präpositionen",t:["prep","pfall","vprep"],soon:"Zeitangaben"}')
a='{n:"Nomen & Fälle",t:["art","fall","gen"]'
if s.count(a)!=1: sys.exit("Anker Gruppe2")
s=s.replace(a,'{n:"Nomen & Fälle",t:["art","fall","vkas","gen"]')
a='if(k==="vprep"||k==="prep")return "Präposition";'
if s.count(a)!=1: sys.exit("Anker lab")
s=s.replace(a,a+'if(k==="pfall")return "Präposition oder Artikel";if(k==="vkas")return "Artikel oder Pronomen im richtigen Fall";')
m=re.search(r'name="app-version" content="(\d{4}-\d\d-\d\d)([a-z]?)"',s)
s=s.replace(m.group(0),'name="app-version" content="%s%s"'%(m.group(1),chr(ord(m.group(2) or "`")+1)))
open(p,"w",encoding="utf-8").write(s); print("OK")
