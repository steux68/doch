#!/usr/bin/env python3
"""DOCH: zwei neue Themen 'Reflexiv' (refl) und 'Nebensätze' (nebs), eigene Formulierung."""
import re, sys
p="index.html"; s=open(p,encoding="utf-8").read()
if "GT.refl=" in s: sys.exit("already patched")
def J(l): return "["+",".join('"%s"'%x for x in l)+"]"
def Q(sent,o,why,lv): return ' {s:"%s",o:%s,why:"%s",lv:"%s"}'%(sent,J(o),why,lv)
def rows(items): return '<div class="rows">'+"".join('<div><span>%s</span><span>%s</span></div>'%(a,b) for a,b in items)+'</div>'
def tc(h,items,note): return '<div class="tc df"><h3>%s</h3>%s<p class="tline">%s</p></div>'%(h,rows(items),note)
def cards(C): return ",\n".join(' {b:"%s",st:%s,tx:"%s",gt:"%s"}'%c for c in C)

# ---------------- Reflexiv ----------------
RF_CARDS=[
 ('Formen','ruleSt("Das Reflexivpronomen",["ich → mich","du → dich","er, sie, es, man → sich","wir → uns","ihr → euch","sie, Sie → sich"])','Only the third person has its own form: sich','The other persons look like the normal Akkusativ pronouns. The pronoun points back to the subject: Ich wasche mich.'),
 ('Echt','ruleSt("Always reflexive",["Ich beeile mich.","Wir erholen uns im Urlaub.","Sie bedankt sich bei dir.","Er weigert sich zu gehen."])','These verbs need sich','Also: sich verabschieden, sich entschließen, sich befinden, sich ereignen, sich irren. Learn the verb together with sich.'),
 ('Unecht','ruleSt("Both ways",["Ich wasche das Auto. / Ich wasche mich.","Er ärgert den Hund. / Er ärgert sich.","Sie zieht das Kind an. / Sie zieht sich an."])','The verb also works with another object','Without sich the action goes to someone else. With sich it points back to the subject.'),
 ('mich · mir','ruleSt("Akkusativ or Dativ?",["Ich wasche mich.","Ich wasche mir die Hände.","Ich kaufe mir ein Buch.","Du merkst dir die Nummer."])','Dativ only when there is another Akkusativ object','Only ich and du differ: mich / mir, dich / dir. In the third person sich is both: Sie kauft sich ein Buch.'),
 ('Präposition','ruleSt("sich + Präposition",["Ich freue mich auf den Urlaub. (kommt noch)","Ich freue mich über das Geschenk. (ist da)","Wir interessieren uns für Musik.","Sie kümmert sich um die Kinder.","Er erinnert sich an den Tag."])','The preposition belongs to the verb','Also: sich ärgern über, sich verlassen auf, sich entscheiden für, sich bewerben um. All of these take the Akkusativ.'),
 ('Stellung','ruleSt("Where does sich go?",["Ich freue mich.","Heute freue ich mich.","Ich glaube, dass er sich freut.","Ich glaube, dass sich der Chef freut.","Beeil dich! Setzen Sie sich!"])','Right behind the verb, or behind a pronoun subject','After a pronoun subject: er sich. Before a noun subject: sich der Chef is usual. In the imperative it stands behind the verb.'),
 ('Besonders','ruleSt("Two special uses",["Wir sehen uns morgen. (einander)","Sie lieben sich. (einander)","Das lässt sich lösen. (kann gelöst werden)","Das Buch verkauft sich gut."])','Each other, and a passive meaning','sich + lassen + Infinitiv says that something is possible. With uns, euch, sich the pronoun can also mean each other.'),
]
RF_Q=[
 Q("Ich dusche ___ jeden Morgen.",["mich","mir","sich"],"No other object: Akkusativ, mich.","A1"),
 Q("Wir treffen ___ um acht Uhr.",["uns","wir","unser"],"sich treffen: reflexive pronoun wir → uns.","A2"),
 Q("Sie beeilt ___.",["sich","sie","ihr"],"sich beeilen: third person → sich.","A2"),
 Q("Ich freue ___ auf das Wochenende.",["mich","mir","sich"],"sich freuen + Akkusativ: mich.","A2"),
 Q("Sie setzt ___ auf den Stuhl.",["sich","ihr","sie"],"sich setzen: third person → sich.","A2"),
 Q("Beeil ___, wir sind spät dran!",["dich","dir","sich"],"Imperative du: Beeil dich!","A2"),
 Q("Ich kaufe ___ ein neues Handy.",["mir","mich","sich"],"The Handy is the Akkusativ object, so the pronoun is Dativ: mir.","A2"),
 Q("Ich putze ___ die Zähne.",["mir","mich","sich"],"die Zähne is the Akkusativ object, so the pronoun is Dativ: mir.","A2"),
 Q("Hast du ___ die Hände gewaschen?",["dir","dich","sich"],"Another Akkusativ object is present: Dativ, dir.","B1"),
 Q("Setzen Sie ___ bitte.",["sich","Sie","Ihnen"],"Imperative with Sie: Setzen Sie sich.","B1"),
 Q("Er ärgert ___ über den Lärm.",["sich","ihn","ihm"],"sich ärgern über: third person → sich.","B1"),
 Q("Wir interessieren uns ___ Architektur.",["für","an","über"],"sich interessieren für + Akkusativ.","B1"),
 Q("Ich erinnere ___ an meine Kindheit.",["mich","mir","sich"],"sich erinnern an + Akkusativ: mich.","B1"),
 Q("Ich freue mich ___ deinen Besuch nächste Woche.",["auf","über","an"],"Something in the future: sich freuen auf.","B1"),
 Q("Ich freue mich ___ dein Geschenk von gestern.",["über","auf","für"],"Something that is already here: sich freuen über.","B1"),
 Q("Wer kümmert sich ___ die Kinder?",["um","für","auf"],"sich kümmern um + Akkusativ.","B1"),
 Q("Die Schüler bereiten ___ auf die Prüfung vor.",["sich","sie","ihnen"],"sich vorbereiten auf: third person plural → sich.","B1"),
 Q("Wir haben ___ lange nicht gesehen.",["uns","wir","unser"],"Each other: wir → uns.","B1"),
 Q("Das muss ich ___ noch überlegen.",["mir","mich","sich"],"sich (Dativ) etwas überlegen: ich → mir.","B2"),
 Q("Ich kann ___ das gar nicht vorstellen.",["mir","mich","sich"],"sich (Dativ) etwas vorstellen: ich → mir.","B2"),
 Q("Sie nahm ___ vor, früher aufzustehen.",["sich","ihr","sie"],"sich (Dativ) etwas vornehmen: third person → sich.","B2"),
 Q("Es handelt ___ hier um einen Irrtum.",["sich","es","ihn"],"es handelt sich um + Akkusativ: a fixed phrase.","B2"),
 Q("Das Problem lässt ___ leicht lösen.",["sich","es","ihm"],"sich lassen + Infinitiv = it can be done.","C1"),
 Q("Das Buch verkauft ___ sehr gut.",["sich","es","ihm"],"Reflexive with a passive meaning: it sells well.","C1"),
]
RF_TH=''.join([
 tc("Die Formen",[("ich","mich · mir"),("du","dich · dir"),("er, sie, es, man","sich"),("wir","uns"),("ihr","euch"),("sie, Sie","sich")],"Only ich and du change between Akkusativ and Dativ."),
 tc("Akkusativ oder Dativ",[("kein anderes Objekt","Akkusativ: Ich wasche mich."),("noch ein Akkusativ","Dativ: Ich wasche mir die Hände.")],"Also Dativ: sich etwas merken, vorstellen, überlegen, vornehmen."),
 tc("Mit Präposition",[("sich freuen","auf (kommt) · über (ist da)"),("sich interessieren","für"),("sich kümmern","um"),("sich erinnern","an"),("sich ärgern","über"),("sich verlassen","auf")],"All take the Akkusativ. Learn the preposition with the verb."),
])
RF=('GT.refl={name:"Reflexiv",badge:"Reflexiv",tip:"Ask: is there already an Akkusativ object? Then the pronoun is Dativ (mir, dir).",src:["duden","grammis","lingolia"],\n'
 ' lg:\'<span class="lgc akk">Akk</span><span class="lgc dat">Dat</span>\',\n cards:[\n'+cards(RF_CARDS)+'],\n q:[\n'+",\n".join(RF_Q)+'],\n th:`'+RF_TH+'`};\n')

# ---------------- Nebensätze ----------------
NS_CARDS=[
 ('Verb am Ende','D("Ich weiß,|dass~k|er|morgen|kommt~v|.~p","1-4a:Verb ans Ende")','Nebensatz: the conjugated verb goes last','A comma always separates the Nebensatz from the main clause. The conjunction (dass, weil, ob, wenn …) opens it.'),
 ('Mehrteilig','ruleSt("The conjugated verb is last",["…, dass er morgen kommen kann.","…, weil ich gestern gearbeitet habe.","…, dass das Haus gebaut wird.","…, ob sie gekommen ist."])','Infinitive or participle first, then the conjugated verb','This holds for modal verbs, Perfekt, Passiv and Futur alike. The verb that carries the person and tense is always the last word.'),
 ('dass · ob · W-Frage','ruleSt("Indirect speech and questions",["Ich glaube, dass er recht hat.","Ich weiß nicht, ob er kommt.","Sie fragt, wann der Zug fährt.","Er will wissen, wo ich wohne."])','dass = statement · ob = yes/no · W-word = question word','A question word becomes the conjunction. The verb goes to the end: Wann fährt der Zug? → Sie fragt, wann der Zug fährt.'),
 ('Zeit','ruleSt("Time",["Als ich ein Kind war, …","Wenn ich Zeit habe, …","Bevor ich gehe, rufe ich an.","Nachdem ich gegessen hatte, ging ich los.","Sobald du kommst, fangen wir an.","Seit ich in Wien wohne, …","Bis du kommst, warte ich."])','als · wenn · bevor · nachdem · sobald · seit · bis · während','nachdem: the action in the Nebensatz happens first, so it uses the earlier tense (Plusquamperfekt or Perfekt).'),
 ('Grund · Gegensatz','ruleSt("Reason and contrast",["Ich bleibe, weil ich krank bin.","Da es regnet, bleiben wir zu Hause.","Obwohl es regnet, gehen wir spazieren.","Er arbeitet, während sie schläft."])','weil · da · obwohl · während','weil gives the reason, obwohl names something that does not stop the action. da usually stands at the start of the sentence.'),
 ('Zweck · Folge · Mittel','ruleSt("Purpose, result, means",["Ich lerne, damit ich die Prüfung bestehe.","Es war so kalt, dass wir froren.","Er spart Geld, indem er selbst kocht.","Sie ging, ohne dass er etwas sagen konnte."])','damit · so … dass · indem · ohne dass','damit says what for. indem says how. ohne dass says that something did not happen at the same time.'),
 ('Bedingung','ruleSt("Condition",["Wenn du willst, komme ich mit.","Falls du Fragen hast, melde dich.","Sofern es möglich ist, helfen wir.","Wenn ich das gewusst hätte, wäre ich nicht gekommen."])','wenn · falls · sofern','falls and sofern are a little more formal. With a Konjunktiv II condition the sentence is unreal: Wenn ich das gewusst hätte …'),
 ('Nebensatz zuerst','D("Weil~k|er|krank|ist~v|,~p|bleibt~v|er~s|zu Hause|.~p","0-3a:Ende;3-5b:Verb, Verb@g")','Komma, then the verb of the main clause','The Nebensatz fills the first place. So the main clause begins with its verb: Weil er krank ist, bleibt er zu Hause.'),
 ('Modal im Perfekt','ruleSt("hat before the double infinitive",["…, weil er hat arbeiten müssen.","…, dass sie nicht hat kommen können.","…, wenn ich das hätte machen können."])','Perfekt or Konjunktiv II with a modal verb (C1)','The conjugated verb (hat, hätte) stands before the two infinitives. Spoken regional variants differ. For exams use this standard order.'),
]
NS_Q=[
 Q("Ich bleibe zu Hause, ___ ich krank bin.",["weil","denn","deshalb"],"The verb bin is at the end, so the conjunction is weil.","A2"),
 Q("Ich glaube, dass ___.",["er recht hat","hat er recht","er hat recht"],"After dass the conjugated verb goes last.","A2"),
 Q("Ich möchte wissen, ___ du Hunger hast. (Frage: Hast du Hunger?)",["ob","dass","wann"],"A yes/no question becomes a Nebensatz with ob.","A2"),
 Q("___ ich ein Kind war, wohnten wir in Linz.",["Als","Wenn","Wann"],"One event in the past: als.","A2"),
 Q("___ ich Zeit habe, rufe ich dich an.",["Wenn","Als","Weil"],"Present or future: wenn.","A2"),
 Q("Weil es regnet, ___ zu Hause.",["bleiben wir","wir bleiben","wir bleiben nicht"],"After a Nebensatz at the start, the main verb comes first: bleiben wir.","A2"),
 Q("Ich lerne Deutsch, ___ ich in Wien arbeiten kann.",["damit","um","dass"],"damit + Nebensatz gives the purpose when there is a subject: ich … kann.","B1"),
 Q("Es ist so laut, ___ ich nicht schlafen kann.",["dass","damit","weil"],"so … dass gives the result.","B1"),
 Q("___ es regnet, gehen wir spazieren.",["Obwohl","Weil","Damit"],"The rain does not stop us: obwohl.","B1"),
 Q("Ich bin müde, ___ ich schlecht geschlafen habe.",["weil","obwohl","damit"],"Bad sleep is the reason: weil.","B1"),
 Q("Nachdem ich gegessen ___, ging ich spazieren.",["hatte","habe","war"],"nachdem + Plusquamperfekt before the Präteritum: gegessen hatte.","B1"),
 Q("Er ruft an, ___ er nach Hause kommt.",["sobald","damit","obwohl"],"As soon as: sobald.","B1"),
 Q("Ich weiß, dass er gestern nicht ___.",["gekommen ist","ist gekommen","gekommen hat"],"Participle first, then the conjugated verb. kommen forms the Perfekt with sein.","B1"),
 Q("Ich glaube, dass er morgen ___.",["kommen kann","kann kommen","kann kommen können"],"Infinitive first, then the conjugated modal verb.","B1"),
 Q("Falls du Fragen ___, melde dich bitte.",["hast","hat","habe"],"The verb stands at the end and agrees with du: hast.","B1"),
 Q("Seit ich in Wien ___, besuche ich oft Museen.",["wohne","wohnt","wohnen"],"The verb is last and agrees with ich: wohne.","B1"),
 Q("Ich hoffe, dass das Haus bald ___.",["gebaut wird","wird gebaut","gebaut werden"],"Participle first, then the conjugated werden: gebaut wird.","B2"),
 Q("Er spart Geld, ___ er selbst kocht.",["indem","damit","obwohl"],"indem says how: by cooking himself.","B2"),
 Q("Sie ging, ___ er etwas sagen konnte.",["ohne dass","damit","indem"],"ohne dass: she left and he could not say anything.","B2"),
 Q("Sie wollte wissen, ___ er die Wahrheit gesagt hat. (Hat er sie gesagt?)",["ob","dass","wenn"],"A yes/no question becomes a Nebensatz with ob.","B2"),
 Q("Er ist nicht gekommen, weil er ___.",["hat arbeiten müssen","arbeiten müssen hat","hat müssen arbeiten"],"Perfekt with a modal: hat comes before the double infinitive.","C1"),
 Q("Ich wüsste es, wenn ich das ___.",["hätte machen können","machen können hätte","hätte können machen"],"Konjunktiv II with a modal: hätte before the double infinitive.","C1"),
 Q("Wenn ich das gewusst ___, wäre ich nicht gekommen.",["hätte","habe","würde"],"An unreal past condition: Wenn ich das gewusst hätte.","C1"),
 Q("Nachdem sie angekommen ___, rief sie ihre Mutter an.",["war","hatte","wurde"],"ankommen forms the Perfekt with sein: war angekommen.","B2"),
]
NS_TH=''.join([
 tc("Das Verb am Ende",[("einfach","…, dass er kommt."),("mit Modalverb","…, dass er kommen kann."),("Perfekt","…, dass er gekommen ist."),("Passiv","…, dass es gebaut wird.")],"The conjugated verb is always the last word of the Nebensatz."),
 tc("Konjunktionen nach Art",[("Zeit","als · wenn · bevor · nachdem · sobald · seit · bis · während"),("Grund","weil · da"),("Gegensatz","obwohl · während"),("Zweck","damit"),("Folge","so … dass"),("Mittel","indem"),("Bedingung","wenn · falls · sofern"),("Inhalt","dass · ob · W-Wort")],"Choose the conjunction by meaning first, then send the verb to the end."),
 tc("Nebensatz zuerst",[("Nebensatz","Weil er krank ist,"),("Hauptsatz","bleibt er zu Hause.")],"Komma, then the verb: the Nebensatz fills the first place."),
])
NS=('GT.nebs={name:"Nebensätze",badge:"Nebensatz",tip:"Choose the conjunction by meaning, then send the conjugated verb to the very end.",src:["duden","grammis","lingolia"],\n'
 ' lg:\'<span><b class="wt k lgk">weil</b> Konjunktion</span><span><b class="wt v lgk">Verb</b> am Ende</span>\',\n cards:[\n'+cards(NS_CARDS)+'],\n q:[\n'+",\n".join(NS_Q)+'],\n th:`'+NS_TH+'`};\n')

a='/* ---------- topics + home ---------- */'
if s.count(a)!=1: sys.exit("Anker topics")
s=s.replace(a,"/* refl-nebs */\n"+RF+NS+a)
a=' {t:"zuinf",'
i=s.find(a); assert i>0
j=s.index("\n",i)+1
s=s[:j]+' {t:"nebs",n:"Nebensätze",tag:"weil · dass · obwohl",ds:"Verb am Ende, Konjunktionen nach Art, Nebensatz zuerst · A2–C1"},\n'+s[j:]
a=' {t:"k1",'
i=s.find(a); assert i>0
j=s.index("\n",i)+1
s=s[:j]+' {t:"refl",n:"Reflexiv",tag:"ich freue mich",ds:"mich oder mir, sich + Präposition, Stellung · A1–C1"},\n'+s[j:]
a='{n:"Satz",t:["satz","tekamolo","neg","konn","rel","zuinf"],soon:"Nebensätze"}'
if s.count(a)!=1: sys.exit("Anker Satz")
s=s.replace(a,'{n:"Satz",t:["satz","tekamolo","neg","konn","nebs","rel","zuinf"]}')
a='{n:"Verb",t:["praes","modal","perf","pass","k2","k1"],soon:"Reflexiv"}'
if s.count(a)!=1: sys.exit("Anker Verb")
s=s.replace(a,'{n:"Verb",t:["praes","refl","modal","perf","pass","k2","k1"],soon:"Präteritum · Futur"}')
a='if(k==="art")return "Artikel";'
if s.count(a)!=1: sys.exit("Anker lab")
s=s.replace(a,a+'if(k==="refl")return "Reflexivpronomen oder Präposition";if(k==="nebs")return "Konjunktion, Verb oder Satzstellung";')
m=re.search(r'name="app-version" content="(\d{4}-\d\d-\d\d)([a-z]?)"',s)
new="2026-11-16a" if m.group(1)!="2026-11-16" else "2026-11-16"+chr(ord(m.group(2) or "`")+1)
s=s.replace(m.group(0),'name="app-version" content="%s"'%new)
open(p,"w",encoding="utf-8").write(s); print("OK",new)
