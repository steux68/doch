#!/usr/bin/env python3
"""DOCH: 'Lernen auf Deutsch' Teil 2 - TEKAMOLO und Konnektoren (Karten, Tipp, Warum-Karte). Eigene Formulierung. Idempotent."""
import sys, re
p="index.html"; s=open(p,encoding="utf-8").read()
if "Stelle vier Fragen in dieser Reihenfolge" in s: sys.exit("already patched")
def seg_bounds(k):
    a=s.find("GT.%s={"%k); b=s.find("\nGT.",a+10); assert a>0 and b>a; return a,b
def apply(k,R):
    global s
    a,b=seg_bounds(k); seg=s[a:b]
    for o,n in R:
        assert seg.count(o) in ((2,) if o in MULTI else (1,)),(k,o,seg.count(o))
        seg=seg.replace(o,n)
    s=s[:a]+seg+s[b:]
MULTI={'Two nouns: Dativ before Akkusativ','ob = whether'}
TEK=[
 ("Ask four questions in this order: wann? warum? wie? wo? It is the neutral order, your safe default. New or important information moves towards the end.","Stelle vier Fragen in dieser Reihenfolge: wann? warum? wie? wo? Das ist die neutrale Reihenfolge, dein sicherer Standard. Neues oder Wichtiges rückt nach hinten."),
 ("The usual order of the extra information in the middle of the sentence: <b>when – why – how – where</b>. Each part answers one question.","So stehen die zusätzlichen Angaben meistens in der Satzmitte: <b>wann – warum – wie – wo</b>. Jeder Teil beantwortet eine Frage."),
 ("TEKAMOLO fills the Mittelfeld","TEKAMOLO füllt das Mittelfeld"),
 ("It stands between the two parts of the verb bracket: <b>haben … gearbeitet</b>. Not every sentence uses all four, but the ones you use keep this order.","Es steht zwischen den beiden Teilen der Verbklammer: <b>haben … gearbeitet</b>. Nicht jeder Satz braucht alle vier, aber die, die du brauchst, behalten diese Reihenfolge."),
 ("seit Montag. The time usually comes first.","seit Montag. Die Zeit steht meistens zuerst."),
 ("A reason follows the time.","Ein Grund steht nach der Zeit."),
 ("Manner comes after the reason and before the place.","Die Art und Weise steht nach dem Grund und vor dem Ort."),
 ("Place comes last in the middle field.","Der Ort steht im Mittelfeld zuletzt."),
 ("Pronouns come first","Pronomen stehen zuerst"),
 ("Short pronouns stand right after the verb, before TEKAMOLO. Two pronouns: <b>Akk before Dat</b> – es dir, not dir es.","Kurze Pronomen stehen direkt nach dem Verb, vor TEKAMOLO. Bei zwei Pronomen: <b>Akk vor Dat</b> – es dir, nicht dir es."),
 ("Two nouns: Dativ before Akkusativ","Zwei Nomen: Dativ vor Akkusativ"),
 ("A pronoun comes before a noun: Ich schenke","Ein Pronomen steht vor einem Nomen: Ich schenke"),
 ("Any part can go first","Jeder Teil kann zuerst stehen"),
 ("For emphasis, put one part in position 1. The verb stays second, and the others keep their order: <b>Morgen fahre ich mit dem Zug nach Wien.</b>","Zur Betonung kannst du einen Teil auf Position 1 setzen. Das Verb bleibt an zweiter Stelle, die anderen Teile behalten ihre Reihenfolge: <b>Morgen fahre ich mit dem Zug nach Wien.</b>"),
 ("The new information goes last","Die neue Information steht zuletzt"),
 ("TEKAMOLO is the neutral order. If the means of transport is the point, it can move back: nach Wien <b>mit dem Zug</b>. Learn the default first, then notice how real texts bend it.","TEKAMOLO ist die neutrale Reihenfolge. Wenn das Verkehrsmittel die Hauptsache ist, darf es nach hinten rücken: nach Wien <b>mit dem Zug</b>. Lerne zuerst den Standard und achte dann darauf, wie echte Texte davon abweichen."),
]
KONN=[
 ("Ask first: does the connector push the verb to the end, take the Vorfeld, or stand outside (ADUSO)?","Erst fragen: Schiebt der Konnektor das Verb ans Ende, nimmt er das Vorfeld, oder steht er außerhalb (ADUSO)?"),
 ("They stand outside the clause. The next clause keeps normal word order.","Sie stehen außerhalb des Satzes. Der nächste Satz behält die normale Wortstellung."),
 ("They open a Nebensatz. The conjugated verb goes to the very end.","Sie leiten einen Nebensatz ein. Das konjugierte Verb steht ganz am Ende."),
 ("These are adverbs. They take the Vorfeld, so the verb follows straight away and the subject moves behind it.","Das sind Adverbien. Sie stehen im Vorfeld, deshalb folgt das Verb sofort und das Subjekt rückt dahinter."),
 ("Same meaning, different word order","Gleiche Bedeutung, andere Wortstellung"),
 ("weil sends the verb to the end. denn keeps normal order. In speech you also hear „weil ich bin krank“, but write it with the verb at the end.","weil schickt das Verb ans Ende. denn behält die normale Wortstellung. In der Umgangssprache hörst du auch „weil ich bin krank“, aber schreibe das Verb ans Ende."),
 ("When the Nebensatz comes first, it fills the Vorfeld. So the main verb follows the comma directly.","Steht der Nebensatz zuerst, füllt er das Vorfeld. Das Verb des Hauptsatzes folgt deshalb direkt nach dem Komma."),
 ("als: once, in the past","als: einmal, in der Vergangenheit"),
 ("wenn: present, future, conditions, and every time in the past (immer wenn).","wenn: Gegenwart, Zukunft, Bedingungen und jedes Mal in der Vergangenheit (immer wenn)."),
 ("ob = whether","ob = indirekte Ja/Nein-Frage"),
 ("English says „if“ for both. ob asks a yes/no question indirectly. wenn is a condition.","Im Englischen heißt beides „if“. ob stellt eine Ja/Nein-Frage indirekt. wenn nennt eine Bedingung."),
 ("Two-part connectors","Zweiteilige Konnektoren"),
]
apply("tekamolo",TEK); apply("konn",KONN)
W=[("Is TEKAMOLO a rule?","Ist TEKAMOLO eine Regel?"),
 ("It is a memory aid, not a law. It describes the neutral order, the one you can always use. Native speakers shift things for emphasis: the newer or more important the information, the further back it goes. Learn TEKAMOLO as your safe default, then watch how real texts bend it.","Es ist eine Gedächtnisstütze, kein Gesetz. Es beschreibt die neutrale Reihenfolge, die du immer verwenden kannst. Muttersprachler verschieben Teile zur Betonung: Je neuer oder wichtiger die Information, desto weiter hinten steht sie. Lerne TEKAMOLO als sicheren Standard und beobachte dann, wie echte Texte davon abweichen."),
 ("Why do people say weil with the verb second?","Warum sagen Leute weil mit dem Verb an zweiter Stelle?"),
 ("In speech, weil is drifting towards denn: 'weil ich hab keine Zeit', with a little pause after weil, is now common. It is still wrong in writing and in the exam. The rule to keep: weil, dass, ob, wenn send the verb to the end; und, aber, oder, denn do not.","In der gesprochenen Sprache nähert sich weil dem denn an: „weil ich hab keine Zeit“, mit einer kleinen Pause nach weil, ist heute üblich. In der Schrift und in der Prüfung ist es weiterhin falsch. Die Regel zum Merken: weil, dass, ob, wenn schicken das Verb ans Ende; und, aber, oder, denn nicht.")]
for o,n in W:
    assert s.count(o)==1,("why",o); s=s.replace(o,n)
m=re.search(r'name="app-version" content="(\d{4}-\d\d-\d\d)([a-z]?)"',s)
new=m.group(1)+chr(ord(m.group(2) or "`")+1)
s=s.replace(m.group(0),'name="app-version" content="%s"'%new)
open(p,"w",encoding="utf-8").write(s); print("OK",new)
