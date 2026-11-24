#!/usr/bin/env python3
"""DOCH: 'Lernen auf Deutsch' Teil 3 - refl, nebs, modal, zuinf, dopp, konn2 (Karten + Tipp). Eigene Formulierung. Idempotent."""
import sys, re
p="index.html"; s=open(p,encoding="utf-8").read()
if "Erst fragen: Gibt es schon ein Akkusativobjekt" in s: sys.exit("already patched")
miss=[]
def apply(k,R):
    global s
    a=s.find("GT.%s={"%k); b=s.find("\nGT.",a+10)
    if b<0: b=s.find("/* ---------- topics",a)
    assert a>0 and b>a,k
    seg=s[a:b]
    for o,n in R:
        if seg.count(o)<1: miss.append((k,o[:60])); continue
        seg=seg.replace(o,n)
    s=s[:a]+seg+s[b:]
REFL=[
("Ask: is there already an Akkusativ object? Then the pronoun is Dativ (mir, dir).","Erst fragen: Gibt es schon ein Akkusativobjekt? Dann steht das Pronomen im Dativ (mir, dir)."),
("Only the third person has its own form: sich","Nur die dritte Person hat eine eigene Form: sich"),
("The other persons look like the normal Akkusativ pronouns. The pronoun points back to the subject: Ich wasche mich.","Die anderen Personen sehen aus wie die normalen Akkusativpronomen. Das Pronomen verweist auf das Subjekt zurück: Ich wasche mich."),
("These verbs need sich","Diese Verben brauchen sich"),
("Also: sich verabschieden, sich entschließen, sich befinden, sich ereignen, sich irren. Learn the verb together with sich.","Außerdem: sich verabschieden, sich entschließen, sich befinden, sich ereignen, sich irren. Lerne das Verb zusammen mit sich."),
("The verb also works with another object","Das Verb funktioniert auch mit einem anderen Objekt"),
("Without sich the action goes to someone else. With sich it points back to the subject.","Ohne sich geht die Handlung auf jemand anderen. Mit sich verweist sie auf das Subjekt zurück."),
("Dativ only when there is another Akkusativ object","Dativ nur bei einem weiteren Akkusativobjekt"),
("Only ich and du differ: mich / mir, dich / dir. In the third person sich is both: Sie kauft sich ein Buch.","Nur ich und du unterscheiden sich: mich / mir, dich / dir. In der dritten Person ist sich beides: Sie kauft sich ein Buch."),
("The preposition belongs to the verb","Die Präposition gehört zum Verb"),
("Also: sich ärgern über, sich verlassen auf, sich entscheiden für, sich bewerben um. All of these take the Akkusativ.","Außerdem: sich ärgern über, sich verlassen auf, sich entscheiden für, sich bewerben um. Alle haben den Akkusativ."),
("Right behind the verb, or behind a pronoun subject","Direkt hinter dem Verb oder hinter einem Pronomen als Subjekt"),
("After a pronoun subject: er sich. Before a noun subject: sich der Chef is usual. In the imperative it stands behind the verb.","Nach einem Pronomen als Subjekt: er sich. Vor einem Nomen als Subjekt ist sich der Chef üblich. Im Imperativ steht es hinter dem Verb."),
("Each other, and a passive meaning","Einander und passive Bedeutung"),
("sich + lassen + Infinitiv says that something is possible. With uns, euch, sich the pronoun can also mean each other.","sich + lassen + Infinitiv sagt, dass etwas möglich ist. Bei uns, euch, sich kann das Pronomen auch einander bedeuten."),
]
NEBS=[
("Choose the conjunction by meaning, then send the conjugated verb to the very end.","Wähle die Konjunktion nach der Bedeutung und schicke dann das konjugierte Verb ganz ans Ende."),
("Nebensatz: the conjugated verb goes last","Nebensatz: Das konjugierte Verb steht zuletzt"),
("A comma always separates the Nebensatz from the main clause. The conjunction (dass, weil, ob, wenn …) opens it.","Ein Komma trennt den Nebensatz immer vom Hauptsatz. Die Konjunktion (dass, weil, ob, wenn …) leitet ihn ein."),
("Infinitive or participle first, then the conjugated verb","Erst Infinitiv oder Partizip, dann das konjugierte Verb"),
("This holds for modal verbs, Perfekt, Passiv and Futur alike. The verb that carries the person and tense is always the last word.","Das gilt für Modalverben, Perfekt, Passiv und Futur gleichermaßen. Das Verb mit Person und Zeit ist immer das letzte Wort."),
("dass = statement · ob = yes/no · W-word = question word","dass = Aussage · ob = Ja/Nein · W-Wort = Fragewort"),
("A question word becomes the conjunction. The verb goes to the end:","Ein Fragewort wird zur Konjunktion. Das Verb geht ans Ende:"),
("nachdem: the action in the Nebensatz happens first, so it uses the earlier tense (Plusquamperfekt or Perfekt).","nachdem: Die Handlung im Nebensatz passiert zuerst, deshalb steht die frühere Zeit (Plusquamperfekt oder Perfekt)."),
("weil gives the reason, obwohl names something that does not stop the action. da usually stands at the start of the sentence.","weil nennt den Grund, obwohl nennt etwas, das die Handlung nicht aufhält. da steht meistens am Satzanfang."),
("damit says what for. indem says how. ohne dass says that something did not happen at the same time.","damit sagt wozu. indem sagt wie. ohne dass sagt, dass etwas nicht gleichzeitig passiert ist."),
("falls and sofern are a little more formal. With a Konjunktiv II condition the sentence is unreal:","falls und sofern sind etwas förmlicher. Mit einer Konjunktiv-II-Bedingung ist der Satz irreal:"),
("Komma, then the verb of the main clause","Komma, dann das Verb des Hauptsatzes"),
("The Nebensatz fills the first place. So the main clause begins with its verb:","Der Nebensatz füllt die erste Position. Deshalb beginnt der Hauptsatz mit seinem Verb:"),
("Perfekt or Konjunktiv II with a modal verb (C1)","Perfekt oder Konjunktiv II mit Modalverb (C1)"),
("The conjugated verb (hat, hätte) stands before the two infinitives. Spoken regional variants differ. For exams use this standard order.","Das konjugierte Verb (hat, hätte) steht vor den beiden Infinitiven. Gesprochene regionale Varianten unterscheiden sich. Für Prüfungen gilt diese Standardreihenfolge."),
]
MODAL=[
("Modalverb in position 2, infinitive at the end – without zu. ich and er have the same form: ich kann, er kann.","Modalverb an Position 2, Infinitiv am Ende – ohne zu. ich und er haben dieselbe Form: ich kann, er kann."),
("Modalverb in position 2, infinitive at the end","Modalverb an Position 2, Infinitiv am Ende"),
("The modal verb is conjugated; the main verb waits at the end as a plain infinitive, <b>without zu</b>:","Das Modalverb wird konjugiert; das Vollverb wartet am Ende als einfacher Infinitiv, <b>ohne zu</b>:"),
("ich kann · er kann – no ending","ich kann · er kann – keine Endung"),
("ich and er/sie/es look the same and have no ending. Most change the vowel in the singular:","ich und er/sie/es haben dieselbe Form und keine Endung. Die meisten wechseln den Vokal im Singular:"),
("Only sollen keeps its o.","Nur sollen behält sein o."),
("<b>Du musst nicht</b> = you don't have to. <b>Du darfst nicht</b> = you mustn't. The classic trap for English speakers. Instead of nicht müssen you can say <b>nicht brauchen zu</b>:","<b>Du musst nicht</b> = du brauchst nicht. <b>Du darfst nicht</b> = es ist dir verboten. Die klassische Falle für Englischsprachige. Statt nicht müssen kannst du <b>nicht brauchen zu</b> sagen:"),
("möchte = polite want","möchte = höflicher Wunsch"),
("<b>möchte</b> is the Konjunktiv II of mögen, used as a polite present: Ich möchte zahlen. ich mag = I like. A modal verb can stand without an infinitive when the meaning is clear:","<b>möchte</b> ist der Konjunktiv II von mögen und wird als höfliches Präsens benutzt: Ich möchte zahlen. ich mag = etwas gern haben. Ein Modalverb kann ohne Infinitiv stehen, wenn die Bedeutung klar ist:"),
("In a Nebensatz the modal verb goes last","Im Nebensatz steht das Modalverb zuletzt"),
("infinitive first, then the conjugated modal verb.","erst der Infinitiv, dann das konjugierte Modalverb."),
("Ersatzinfinitiv: müssen, not gemusst","Ersatzinfinitiv: müssen, nicht gemusst"),
("With a second verb, the Perfekt uses the infinitive of the modal: Ich habe arbeiten <b>müssen</b>. Without one, the Partizip: Das habe ich nicht <b>gewollt</b>. In speech the Präteritum is usual:","Mit einem zweiten Verb steht im Perfekt der Infinitiv des Modalverbs: Ich habe arbeiten <b>müssen</b>. Ohne zweites Verb steht das Partizip: Das habe ich nicht <b>gewollt</b>. In der gesprochenen Sprache ist das Präteritum üblich:"),
("The one exception to „verb last“: with two infinitives, <b>hat</b> jumps in front of them.","Die einzige Ausnahme von „Verb am Ende“: Bei zwei Infinitiven springt <b>hat</b> vor sie."),
("How sure am I?","Wie sicher bin ich?"),
("Modals also show how certain the speaker is: <b>muss</b> = almost certain, <b>dürfte</b> = probably, <b>kann / könnte</b> = possibly, <b>kann nicht</b> = impossible. Past:","Modalverben zeigen auch, wie sicher sich der Sprecher ist: <b>muss</b> = fast sicher, <b>dürfte</b> = wahrscheinlich, <b>kann / könnte</b> = möglich, <b>kann nicht</b> = unmöglich. Vergangenheit:"),
("soll = people say · will = he claims","soll = man sagt · will = er behauptet"),
("<b>Er soll reich sein</b>: that is what people say. <b>Er will nichts gewusst haben</b>: that is what he claims – and I doubt it. Typical of newspapers and C1 texts.","<b>Er soll reich sein</b>: Das sagen die Leute. <b>Er will nichts gewusst haben</b>: Das behauptet er – und ich zweifle daran. Typisch für Zeitungen und C1-Texte."),
]
ZUINF=[
("After modal verbs, werden, lassen and sehen / hören: no zu. Separable verbs take zu in the middle: anzurufen.","Nach Modalverben, werden, lassen und sehen / hören: kein zu. Trennbare Verben nehmen zu in der Mitte: anzurufen."),
("zu + infinitive goes to the end","zu + Infinitiv steht am Ende"),
("After many nouns (Zeit, Lust, Angst), adjectives (es ist schwer) and verbs (versuchen, vergessen, anfangen): <b>zu</b> + infinitive at the end of its clause.","Nach vielen Nomen (Zeit, Lust, Angst), Adjektiven (es ist schwer) und Verben (versuchen, vergessen, anfangen): <b>zu</b> + Infinitiv am Ende des Satzes."),
("zu goes inside a separable verb","zu steht im trennbaren Verb"),
("Written as one word.","In einem Wort geschrieben."),
("No zu after modal verbs, werden, lassen, bleiben, gehen and verbs of perception:","Kein zu nach Modalverben, werden, lassen, bleiben, gehen und Verben der Wahrnehmung:"),
("No zu after modal verbs","Kein zu nach Modalverben"),
("um … zu = in order to","um … zu = Zweck"),
("Purpose, same subject in both clauses. Different subjects → <b>damit</b>:","Zweck, gleiches Subjekt in beiden Sätzen. Verschiedene Subjekte → <b>damit</b>:"),
("<b>ohne … zu</b> = without doing. <b>(an)statt … zu</b> = instead of doing. English uses -ing; German uses zu + infinitive.","<b>ohne … zu</b> = ohne dass man etwas tut. <b>(an)statt … zu</b> = anstelle einer Handlung. Wo das Englische -ing benutzt, steht im Deutschen zu + Infinitiv."),
("sein zu = must / can be done","sein zu = muss / kann getan werden"),
("<b>Ich habe zu arbeiten</b> = I have to work. <b>Das ist zu bezahlen</b> = it must be paid (passive). <b>Das ist leicht zu lösen</b> = it can be solved easily. Typical of forms and official letters.","<b>Ich habe zu arbeiten</b> = ich muss arbeiten. <b>Das ist zu bezahlen</b> = es muss bezahlt werden (Passiv). <b>Das ist leicht zu lösen</b> = es lässt sich leicht lösen. Typisch für Formulare und amtliche Briefe."),
("When the action lies before the main verb: Partizip II + <b>zu haben / zu sein</b>. Passive:","Liegt die Handlung vor dem Hauptverb: Partizip II + <b>zu haben / zu sein</b>. Passiv:"),
("<b>Sie scheint müde zu sein</b> = she seems to be tired. Also: Er pflegt früh aufzustehen (he tends to), Das verspricht spannend zu werden.","<b>Sie scheint müde zu sein</b> = sie wirkt müde. Außerdem: Er pflegt früh aufzustehen (er tut das gewöhnlich), Das verspricht spannend zu werden."),
]
DOPP=[
("The first part announces the second. Learn the pair, then check comma and verb.","Der erste Teil kündigt den zweiten an. Lerne das Paar, dann prüfe Komma und Verb."),
("Both A and B","Beides: A und B"),
("Joins two equal parts. No comma. With two subjects the verb is plural:","Verbindet zwei gleichwertige Teile. Kein Komma. Bei zwei Subjekten steht das Verb im Plural:"),
("Not only A but also B","Nicht nur A, sondern auch B"),
("The comma before sondern is always there. With two subjects the verb agrees with the nearer one:","Das Komma vor sondern steht immer. Bei zwei Subjekten richtet sich das Verb nach dem näheren:"),
("Either A or B","Entweder A oder B"),
("One of the two, never both. Between two clauses it works two ways:","Eines von beiden, nie beides. Zwischen zwei Sätzen geht es auf zwei Arten:"),
("Neither A nor B","Weder A noch B"),
("The negation is already inside. Add no nicht and no kein. Between two clauses the verb moves up after noch:","Die Verneinung steckt schon drin. Kein nicht und kein kein dazu. Zwischen zwei Sätzen rückt das Verb nach noch nach vorn:"),
("It is true that A, but B","Zwar A, aber B wiegt schwerer"),
("A is granted, B weighs more. Comma before aber. aber stands outside, so the verb stays in second place:","A wird zugestanden, B wiegt schwerer. Komma vor aber. aber steht außerhalb, das Verb bleibt also an zweiter Stelle:"),
("The more A, the more B","Je mehr A, desto mehr B"),
("je opens a Nebensatz (verb last). desto + comparative opens the main clause, and the verb follows at once. umso works like desto.","je leitet einen Nebensatz ein (Verb am Ende). desto + Komparativ leitet den Hauptsatz ein, das Verb folgt sofort. umso funktioniert wie desto."),
("On the one hand … on the other hand","Einerseits … andererseits: zwei Seiten"),
("Two views of one thing, each a main clause. Comma before andererseits. Often followed by aber auch.","Zwei Sichtweisen auf eine Sache, jede ein Hauptsatz. Komma vor andererseits. Oft folgt aber auch."),
("Partly … partly · sometimes … sometimes","teils … teils · mal … mal: wechselnd"),
("Both parts are the same kind of word. mal … mal is common in speech, teils … teils in writing.","Beide Teile sind dieselbe Wortart. mal … mal ist in der Umgangssprache üblich, teils … teils in der Schrift."),
('ruleSt("Alternating"','ruleSt("Wechselnd"'),
("Whether … or · be it … or be it","ob … oder · sei es … sei es: Alternativen"),
("Formal and rhythmic. Ob … oder opens a Nebensatz when it has a verb. sei es … sei es is written style.","Förmlich und rhythmisch. Ob … oder leitet einen Nebensatz ein, wenn er ein Verb hat. sei es … sei es ist Schriftstil."),
('ruleSt("Alternatives (B2–C1)"','ruleSt("Alternativen (B2–C1)"'),
]
KONN2=[
("Ask: Vorfeld (verb right after), inside the clause, or Nebensatz (verb last)?","Frage: Vorfeld (Verb sofort danach), mitten im Satz oder Nebensatz (Verb am Ende)?"),
("Adverbs of result. They take the Vorfeld, the verb follows at once. As a Nebensatz: sodass (one word, verb last).","Adverbien des Ergebnisses. Sie stehen im Vorfeld, das Verb folgt sofort. Als Nebensatz: sodass (ein Wort, Verb am Ende)."),
("Contrast against what you expect. In the Vorfeld, or inside the clause: Er ist jedoch sehr erfahren. As a Nebensatz: wohingegen.","Gegensatz zu dem, was man erwartet. Im Vorfeld oder im Satz: Er ist jedoch sehr erfahren. Als Nebensatz: wohingegen."),
("Adds a further point. Vorfeld, verb second. darüber hinaus is a longer, more formal form.","Fügt einen weiteren Punkt hinzu. Vorfeld, Verb an zweiter Stelle. darüber hinaus ist die längere, förmlichere Form."),
('ruleSt("Otherwise · unless"','ruleSt("Sonst · außer wenn"'),
("sonst and andernfalls take the Vorfeld. es sei denn is followed by a clause. sofern sends the verb to the end.","sonst und andernfalls stehen im Vorfeld. Nach es sei denn folgt ein Satz. sofern schickt das Verb ans Ende."),
('ruleSt("How? By doing what?"','ruleSt("Wie? Wodurch?"'),
("All three open a Nebensatz. indem says by which means.","Alle drei leiten einen Nebensatz ein. indem sagt, mit welchem Mittel."),
("Grund formell","Grund formell"),
('ruleSt("Reason, written style"','ruleSt("Grund, Schriftstil"'),
("zumal opens a Nebensatz and adds an extra reason. nämlich never stands first: it sits inside the clause.","zumal leitet einen Nebensatz ein und nennt einen zusätzlichen Grund. nämlich steht nie am Anfang, sondern im Satz."),
("Several of these may stand after the verb. The sentence stays a normal main clause. Only the Vorfeld position changes the order.","Mehrere dieser Wörter können nach dem Verb stehen. Der Satz bleibt ein normaler Hauptsatz. Nur das Vorfeld ändert die Wortstellung."),
('ruleSt("Limits"','ruleSt("Grenzen"'),
("Careful, formal. soweit opens a Nebensatz and gives the limit of what you know.","Vorsicht, förmlich. soweit leitet einen Nebensatz ein und nennt die Grenze dessen, was man weiß."),
]
for k,R in [("refl",REFL),("nebs",NEBS),("modal",MODAL),("zuinf",ZUINF),("dopp",DOPP),("konn2",KONN2)]: apply(k,R)
if miss:
    for m in miss: print("MISS",m)
    sys.exit("not written")
m=re.search(r'name="app-version" content="(\d{4}-\d\d-\d\d)([a-z]?)"',s)
new=m.group(1)+chr(ord(m.group(2) or "`")+1)
s=s.replace(m.group(0),'name="app-version" content="%s"'%new)
open(p,"w",encoding="utf-8").write(s); print("OK",new)
