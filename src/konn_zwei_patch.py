#!/usr/bin/env python3
"""DOCH: zwei neue Themen 'Zweiteilige Konnektoren' (dopp) und 'Konnektoren formell' (konn2).
Eigene Formulierung, Beispielsätze selbst geschrieben. Idempotent."""
import re, sys
p = "index.html"
s = open(p, encoding="utf-8").read()
if "GT.dopp=" in s:
    sys.exit("already patched")

def J(l): return "[" + ",".join('"%s"' % x for x in l) + "]"
def Q(sent, o, why, lv): return ' {s:"%s",o:%s,why:"%s",lv:"%s"}' % (sent, J(o), why, lv)
def rows(items): return '<div class="rows">' + "".join('<div><span>%s</span><span>%s</span></div>' % (a, b) for a, b in items) + '</div>'
def tc(h, items, note=""):
    n = '<p class="tline">%s</p>' % note if note else ""
    return '<div class="tc df"><h3>%s</h3>%s%s</div>' % (h, rows(items), n)
def cards(C): return ",\n".join(' {b:"%s",st:%s,tx:"%s",gt:"%s"}' % c for c in C)

# ================= Zweiteilige Konnektoren =================
DP_CARDS = [
 ('sowohl … als auch', 'D("Ich|spreche|sowohl~k|Deutsch|als auch~k|Englisch|.~p","")',
  'Both A and B', 'Joins two equal parts. No comma. With two subjects the verb is plural: Sowohl Anna als auch Tom sind müde.'),
 ('nicht nur … sondern auch', 'D("Sie|spricht|nicht nur~k|Deutsch|,~p|sondern auch~k|Englisch|.~p","")',
  'Not only A but also B', 'The comma before sondern is always there. With two subjects the verb agrees with the nearer one: Nicht nur die Kinder, sondern auch der Vater kommt mit.'),
 ('entweder … oder', 'D("Wir|fahren|entweder~k|nach Graz|oder~k|nach Linz|.~p","")',
  'Either A or B', 'One of the two, never both. Between two clauses it works two ways: Entweder du kommst heute, oder du kommst morgen. · Entweder kommst du heute, oder …'),
 ('weder … noch', 'D("Ich|trinke|weder~k|Kaffee|noch~k|Tee|.~p","")',
  'Neither A nor B', 'The negation is already inside. Add no nicht and no kein. Between two clauses the verb moves up after noch: Weder hat er angerufen, noch hat er geschrieben.'),
 ('zwar … aber', 'D("Das Haus|ist|zwar~k|alt|,~p|aber~k|es|ist~v|schön|.~p","")',
  'It is true that A, but B', 'A is granted, B weighs more. Comma before aber. aber stands outside, so the verb stays in second place: Zwar ist das Haus alt, aber es ist schön.'),
 ('je … desto', 'D("Je~k|länger|ich|warte~v|,~p|desto~k|nervöser|werde~v|ich|.~p","0-3a:Ende;5-8a:desto + Verb")',
  'The more A, the more B', 'je opens a Nebensatz (verb last). desto + comparative opens the main clause, and the verb follows at once. umso works like desto.'),
 ('einerseits … andererseits', 'D("Einerseits~k|möchte~v|ich|schlafen|,~p|andererseits~k|muss~v|ich|arbeiten|.~p","")',
  'On the one hand … on the other hand', 'Two views of one thing, each a main clause. Comma before andererseits. Often followed by aber auch.'),
 ('teils … teils · mal … mal', 'ruleSt("Alternating",["Das Wetter war teils sonnig, teils regnerisch.","Mal regnet es, mal scheint die Sonne.","Er ist mal freundlich, mal ganz still."])',
  'Partly … partly · sometimes … sometimes', 'Both parts are the same kind of word. mal … mal is common in speech, teils … teils in writing.'),
 ('ob … oder · sei es … sei es', 'ruleSt("Alternatives (B2–C1)",["Ob du willst oder nicht, wir gehen jetzt.","Sei es aus Neugier, sei es aus Pflichtgefühl: Er kam jeden Tag.","Ob früh oder spät, sie ist immer da."])',
  'Whether … or · be it … or be it', 'Formal and rhythmic. Ob … oder opens a Nebensatz when it has a verb. sei es … sei es is written style.'),
]
DP_Q = [
 Q("Ich spreche sowohl Deutsch ___ Englisch.", ["als auch", "noch", "sondern"], "Fixed pair: sowohl … als auch.", "B1"),
 Q("Er ist nicht nur freundlich, ___ auch hilfsbereit.", ["sondern", "aber", "noch"], "Fixed pair: nicht nur … sondern auch.", "B1"),
 Q("Wir fahren entweder nach Graz ___ nach Linz.", ["oder", "noch", "als auch"], "One of two: entweder … oder.", "B1"),
 Q("Ich trinke ___ Kaffee noch Tee.", ["weder", "entweder", "sowohl"], "Neither: weder … noch.", "B1"),
 Q("Ich habe weder Zeit ___ Lust.", ["noch", "oder", "und"], "weder is answered by noch.", "B1"),
 Q("Er hat weder angerufen ___ geschrieben.", ["noch", "sondern", "als auch"], "weder … noch: no nicht needed.", "B1"),
 Q("Das Haus ist zwar alt, ___ es ist sehr schön.", ["aber", "sondern", "denn"], "zwar … aber: A is granted, B counts more.", "B1"),
 Q("Zwar ist das Haus alt, aber ___.", ["es ist schön", "ist es schön", "es schön ist"], "aber stands outside the clause: normal word order.", "B1"),
 Q("Je früher du kommst, ___ mehr Zeit haben wir.", ["desto", "so", "als"], "je … desto: the more A, the more B.", "B1"),
 Q("Je länger ich warte, desto ___ werde ich.", ["nervöser", "nervös", "am nervösesten"], "After desto comes a comparative.", "B1"),
 Q("Je mehr ich übe, ___.", ["desto besser spreche ich", "desto besser ich spreche", "desto ich besser spreche"], "The verb follows desto + comparative at once.", "B1"),
 Q("Je mehr ich übe, desto besser ___ ich.", ["spreche", "sprechen", "gesprochen"], "The main clause: verb in second place after desto besser.", "B1"),
 Q("Sowohl Anna als auch Tom ___ müde.", ["sind", "ist", "bist"], "Two subjects joined by sowohl … als auch take the plural.", "B2"),
 Q("Nicht nur meine Eltern, sondern auch meine Schwester ___ mit.", ["kommt", "kommen", "kommst"], "The verb agrees with the nearer subject: meine Schwester.", "B2"),
 Q("Einerseits möchte ich schlafen, ___ muss ich arbeiten.", ["andererseits", "zwar", "entweder"], "einerseits … andererseits: two views of one thing.", "B2"),
 Q("Das Wetter war ___ sonnig, teils regnerisch.", ["teils", "mal", "zwar"], "teils … teils: the same word twice.", "B2"),
 Q("___ regnet es, mal scheint die Sonne.", ["Mal", "Teils", "Weder"], "mal … mal: sometimes … sometimes.", "B2"),
 Q("Ob du willst ___ nicht, wir gehen jetzt.", ["oder", "noch", "aber"], "ob … oder: whether … or.", "B2"),
 Q("Nicht nur ___ müde, sondern er war auch hungrig.", ["war er", "er war", "er müde war"], "nicht nur at the front: the verb moves up, like after any first element.", "C1"),
 Q("___ im Beruf, sei es in der Freizeit: Er ist immer pünktlich.", ["Sei es", "Ob es", "Weder"], "Written style: sei es … sei es.", "C1"),
]
DP_TH = ''.join([
 tc("Die Paare", [("A und B", "sowohl … als auch · nicht nur … sondern auch"), ("A oder B", "entweder … oder"), ("weder A noch B", "weder … noch"),
                  ("A, aber B", "zwar … aber"), ("je mehr, desto mehr", "je … desto · je … umso"), ("zwei Seiten", "einerseits … andererseits"),
                  ("wechselnd", "teils … teils · mal … mal")], "Learn them as pairs. The first part announces the second."),
 tc("Verb und Komma", [("sowohl … als auch", "no comma"), ("nicht nur … sondern auch", "comma before sondern"), ("entweder … oder", "comma only between two clauses"),
                       ("weder … noch", "comma only between two clauses"), ("zwar … aber", "comma before aber"),
                       ("je … desto", "comma always, verb last after je, verb right after desto + comparative"),
                       ("einerseits … andererseits", "comma before andererseits")], "Two main clauses: the first part may take the Vorfeld, then the verb is second."),
 tc("Typische Fehler", [("weder … nicht", "Ich trinke weder Kaffee noch Tee. (no nicht)"), ("je … so", "wrong: Je mehr ich übe, desto besser. (not so)"),
                        ("sowohl … oder", "wrong: sowohl is answered by als auch"), ("zwar … sondern", "wrong: zwar is answered by aber")]),
])
DP = ('GT.dopp={name:"Zweiteilige Konnektoren",badge:"Doppelkonnektor",tip:"The first part announces the second. Learn the pair, then check comma and verb.",src:["duden","grammis","lingolia"],\n'
      ' lg:\'<span><b class="wt k lgk">sowohl</b> Konnektor</span><span><b class="wt v lgk">Verb</b> Verbposition</span>\',\n cards:[\n'
      + cards(DP_CARDS) + '],\n q:[\n' + ",\n".join(DP_Q) + '],\n th:`' + DP_TH + '`};\n')

# ================= Konnektoren formell =================
K2_CARDS = [
 ('Folge', 'D("Das Budget ist knapp.|Folglich~k|müssen~v|wir~s|sparen|.~p","1-2a:Verb direkt danach")',
  'folglich · somit · demnach · infolgedessen', 'Adverbs of result. They take the Vorfeld, the verb follows at once. As a Nebensatz: sodass (one word, verb last).'),
 ('Gegensatz', 'D("Der Plan ist gut.|Dennoch~k|fehlt~v|das Geld|.~p","1-2a:Verb direkt danach")',
  'dennoch · jedoch · allerdings · hingegen', 'Contrast against what you expect. In the Vorfeld, or inside the clause: Er ist jedoch sehr erfahren. As a Nebensatz: wohingegen.'),
 ('Zusatz', 'D("Das Haus ist günstig.|Zudem~k|liegt~v|es~s|zentral|.~p","1-2a:Verb direkt danach")',
  'zudem · außerdem · darüber hinaus · ferner', 'Adds a further point. Vorfeld, verb second. darüber hinaus is a longer, more formal form.'),
 ('Ausnahme', 'ruleSt("Otherwise · unless",["Komm früher, sonst verpasst du den Zug.","Komm früher, andernfalls verpasst du den Zug.","Wir fahren morgen, es sei denn, es schneit.","Sofern es möglich ist, helfen wir."])',
  'sonst · andernfalls · es sei denn · sofern', 'sonst and andernfalls take the Vorfeld. es sei denn is followed by a clause. sofern sends the verb to the end.'),
 ('Mittel', 'ruleSt("How? By doing what?",["Er löste das Problem, indem er den Computer neu startete.","Sie ging, ohne dass jemand es bemerkte.","Anstatt dass er hilft, sieht er zu."])',
  'indem · ohne dass · anstatt dass', 'All three open a Nebensatz. indem says by which means.'),
 ('Grund formell', 'ruleSt("Reason, written style",["Wir sollten warten, zumal das Wetter schlecht ist.","Er kommt nicht. Er ist nämlich krank.","Da es spät ist, gehen wir."])',
  'zumal · nämlich · da', 'zumal opens a Nebensatz and adds an extra reason. nämlich never stands first: it sits inside the clause.'),
 ('Mitten im Satz', 'D("Er|ist|jedoch~k|sehr erfahren|.~p","")',
  'jedoch · allerdings · hingegen · nämlich · zudem', 'Several of these may stand after the verb. The sentence stays a normal main clause. Only the Vorfeld position changes the order.'),
 ('Einschränkung', 'ruleSt("Limits",["Soweit ich weiß, kommt er morgen.","Das stimmt insofern, als es nur für Kinder gilt.","Er kann nicht schwimmen, geschweige denn tauchen."])',
  'soweit · insofern als · geschweige denn', 'Careful, formal. soweit opens a Nebensatz and gives the limit of what you know.'),
]
K2_Q = [
 Q("Das Budget ist knapp. ___ müssen wir sparen.", ["Folglich", "Sodass", "Obwohl"], "An adverb of result in the Vorfeld: folglich, verb right after.", "B2"),
 Q("Es regnete stark, sodass ___.", ["das Fest ausfiel", "fiel das Fest aus", "das Fest fiel aus"], "sodass opens a Nebensatz: the verb goes last.", "B2"),
 Q("Der Plan ist gut. ___ fehlt das Geld.", ["Dennoch", "Obwohl", "Sodass"], "Contrast, verb right after: dennoch.", "B2"),
 Q("Er liebt die Stadt, ___ sie das Land bevorzugt.", ["wohingegen", "dennoch", "folglich"], "Contrast with the verb at the end: wohingegen.", "C1"),
 Q("Das Haus ist günstig. ___ liegt es zentral.", ["Zudem", "Dennoch", "Folglich"], "A further point: zudem.", "B2"),
 Q("Wir fahren morgen, ___, es schneit.", ["es sei denn", "es sei dass", "sonst"], "Fixed phrase for an exception: es sei denn.", "C1"),
 Q("Komm früher, ___ verpasst du den Zug.", ["sonst", "weil", "damit"], "Otherwise: sonst, verb right after.", "B1"),
 Q("Er löste das Problem, ___ er den Computer neu startete.", ["indem", "damit", "sodass"], "How he did it: indem.", "B2"),
 Q("Wir sollten warten, ___ das Wetter schlecht ist.", ["zumal", "dennoch", "folglich"], "An extra reason with the verb last: zumal.", "C1"),
 Q("Er kommt nicht. Er ist ___ krank.", ["nämlich", "jedoch", "sodass"], "nämlich gives the reason and stands inside the clause.", "B2"),
 Q("___ ich weiß, kommt er morgen.", ["Soweit", "Sobald", "Sowie"], "The limit of what I know: soweit.", "C1"),
 Q("Das ist richtig. Allerdings ___.", ["kostet es mehr", "es kostet mehr", "es mehr kostet"], "allerdings in the Vorfeld: the verb follows at once.", "B2"),
 Q("Er ist jung, ___ sehr erfahren.", ["jedoch", "sodass", "indem"], "A contrast: jedoch.", "B2"),
 Q("Der Chef ist streng, seine Mitarbeiter ___ sind freundlich.", ["hingegen", "wohingegen", "sodass"], "hingegen sits inside the main clause. wohingegen would send the verb to the end.", "C1"),
 Q("Der Zug fällt aus. ___ nehmen wir ein Taxi.", ["Infolgedessen", "Indem", "Sodass"], "Result in the Vorfeld: infolgedessen.", "C1"),
 Q("Sie ist freundlich. Außerdem ___ sie sehr klug.", ["ist", "sie", "sind"], "außerdem is in the Vorfeld, so the verb is second.", "B1"),
]
K2_TH = ''.join([
 tc("Nach Bedeutung", [("Folge", "folglich · somit · demnach · infolgedessen · sodass"), ("Gegensatz", "dennoch · jedoch · allerdings · hingegen · wohingegen"),
                       ("Zusatz", "zudem · außerdem · darüber hinaus · ferner"), ("Ausnahme", "sonst · andernfalls · es sei denn · sofern"),
                       ("Mittel", "indem · ohne dass · anstatt dass"), ("Grund", "zumal · nämlich · da"), ("Grenze", "soweit · insofern als")]),
 tc("Wo steht das Verb?", [("Vorfeld, Verb sofort", "folglich · somit · demnach · dennoch · zudem · außerdem · sonst · andernfalls"),
                           ("auch mitten im Satz", "jedoch · allerdings · hingegen · zudem"), ("nur mitten im Satz", "nämlich"),
                           ("Nebensatz, Verb am Ende", "sodass · wohingegen · indem · zumal · sofern · soweit · ohne dass")]),
 tc("Gesprochen und geschrieben", [("weil · also · aber", "speech and everyday text"), ("folglich · jedoch · dennoch", "reports, essays, exam texts"),
                                   ("zumal · es sei denn", "careful written style, rare in speech")], "At C1 you choose by register: the meaning stays the same."),
])
K2 = ('GT.konn2={name:"Konnektoren formell",badge:"Konnektor",tip:"Ask: Vorfeld (verb right after), inside the clause, or Nebensatz (verb last)?",src:["duden","grammis","lingolia"],\n'
      ' lg:\'<span><b class="wt k lgk">dennoch</b> Konnektor</span><span><b class="wt v lgk">Verb</b> Verbposition</span>\',\n cards:[\n'
      + cards(K2_CARDS) + '],\n q:[\n' + ",\n".join(K2_Q) + '],\n th:`' + K2_TH + '`};\n')

# ================= Einbau =================
a = '/* ---------- topics + home ---------- */'
if s.count(a) != 1: sys.exit("Anker topics")
s = s.replace(a, "/* konn-zwei */\n" + DP + K2 + a)

a = ' {t:"konn",n:"Konnektoren",tag:"weil · denn · deshalb",ds:"Wohin geht das Verb? · A2–B2"},'
if s.count(a) != 1: sys.exit("Anker TOPICS konn")
s = s.replace(a, a + '\n {t:"dopp",n:"Zweiteilige Konnektoren",tag:"sowohl … als auch",ds:"entweder … oder, weder … noch, je … desto · B1–C1"},'
                     '\n {t:"konn2",n:"Konnektoren formell",tag:"dennoch · folglich · indem",ds:"Vorfeld, Mittelfeld, Nebensatz · B2–C1"},')

a = '{n:"Satz",t:["satz","tekamolo","neg","konn","nebs","rel","zuinf"]}'
if s.count(a) != 1: sys.exit("Anker Satz")
s = s.replace(a, '{n:"Satz",t:["satz","tekamolo","neg","konn","dopp","konn2","nebs","rel","zuinf"]}')

a = 'if(k==="art")return "Artikel";'
if s.count(a) != 1: sys.exit("Anker lab")
s = s.replace(a, a + 'if(k==="dopp")return "Bindewort oder Verb";if(k==="konn2")return "Konnektor oder Verbstellung";')

a = 'konn:["satz"],tekamolo:["satz"]};'
if s.count(a) != 1: sys.exit("Anker PRE")
s = s.replace(a, 'konn:["satz"],dopp:["konn"],konn2:["konn"],tekamolo:["satz"]};')

m = re.search(r'name="app-version" content="(\d{4}-\d\d-\d\d)([a-z]?)"', s)
new = m.group(1) + chr(ord(m.group(2) or "`") + 1)
s = s.replace(m.group(0), 'name="app-version" content="%s"' % new)
open(p, "w", encoding="utf-8").write(s)
print("OK", new)
