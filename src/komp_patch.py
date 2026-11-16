#!/usr/bin/env python3
"""DOCH: Thema 'Komparation' (komp), eigene Formulierung."""
from _gt_common import *
C=[
 card("Drei Stufen",R("Positiv · Komparativ · Superlativ",["schnell – schneller – am schnellsten","klein – kleiner – am kleinsten","teuer – teurer – am teuersten","dunkel – dunkler – am dunkelsten","bunt – bunter – am buntesten","heiß – heißer – am heißesten"]),"Add -er, then am + -(e)sten","Comparative = stem + -er. Superlative = am + stem + -sten. After -t, -d, -s, -ß, -z or -sch the Superlativ takes -esten: am buntesten, am heißesten. With -el and -er the e often drops: dunkler, teurer."),
 card("Umlaut",R("Many short adjectives",["alt – älter – am ältesten","jung – jünger – am jüngsten","kalt – kälter – am kältesten","warm – wärmer – am wärmsten","lang – länger – am längsten","stark – stärker – am stärksten","groß – größer – am größten"]),"a, o, u often become ä, ö, ü","Many one-syllable adjectives take an umlaut, but not all: klar – klarer, bunt – bunter, froh – froher. Note groß: am größten, without an extra e."),
 card("Unregelmäßig",R("Learn these by heart",["gut – besser – am besten","viel – mehr – am meisten","gern – lieber – am liebsten","hoch – höher – am höchsten","nah – näher – am nächsten","wenig – weniger – am wenigsten"]),"A few common words change completely","The c of hoch disappears before an ending: ein hoher Berg, but höher and am höchsten. Gern is an adverb: Ich trinke gern Tee. Ich trinke lieber Kaffee."),
 card("so … wie · als",R("Equal or different",["Er ist so groß wie ich.","Er ist größer als ich.","Er ist nicht so groß wie ich.","Es ist genauso teuer wie vorher.","Das Haus ist doppelt so groß wie das alte."]),"Same → so … wie. Different → Komparativ + als","Use wie with so or genauso and the basic form. Use als after a Komparativ. Komparativ + wie is spoken and not correct in standard German."),
 card("je … desto",R("The more … the more …",["Je länger ich lerne, desto besser verstehe ich.","Je früher du kommst, desto mehr Zeit haben wir.","Je älter, desto klüger."]),"Two Komparative, two clauses","The je-part is a Nebensatz, so the verb stands last. In the second part desto (or umso) + Komparativ comes first and the verb is second."),
 card("am -sten oder der -ste",R("Two Superlativ forms",["Anna läuft am schnellsten.","Anna ist am schnellsten.","Anna ist die schnellste Läuferin.","Das ist der höchste Berg.","Das ist das beste Essen."]),"No noun → am. With a noun → article + -ste","Use am + -sten with verbs and in the predicate, when no noun follows. Before a noun use the adjective with the article and an ending: der höchste Berg."),
 card("Endungen",R("Endings still apply",["ein größeres Haus","der schnellere Zug","mit besseren Noten","ein teureres Auto","mehr Zeit","weniger Geld"]),"A Komparativ before a noun takes an ending","Put the normal adjective ending after -er: ein größeres Haus. The words mehr and weniger never take an ending: mehr Zeit, weniger Geld."),
 card("immer + Komparativ",R("Getting more and more",["Es wird immer kälter.","Er spricht immer besser.","Die Tage werden immer länger.","Das Leben wird immer teurer."]),"immer + Komparativ = more and more","It describes a change over time. It is common with werden."),
 card("Elativ",R("Very, without comparing",["Das ist höchst interessant.","Sie ist äußerst höflich.","Ich bin bestens informiert.","Wir danken Ihnen aufs Herzlichste."]),"A Superlativ form that only means very","The Elativ does not compare with others. It is typical for written and formal German and shows polite emphasis."),
]
QS=[
 Q("Mein Bruder ist ___ als ich. (alt)",["älter","alter","ältere"],"alt → älter, with an umlaut.","A2"),
 Q("Der Zug ist ___ als der Bus. (schnell)",["schneller","schnellere","schnell"],"Komparativ: schneller. No ending in the predicate.","A2"),
 Q("Ich bin so groß ___ mein Vater.",["wie","als","denn"],"Equal comparison: so … wie.","A2"),
 Q("Mein Vater ist größer ___ ich.",["als","wie","so"],"After a Komparativ use als.","A2"),
 Q("Das Wetter ist heute ___ als gestern. (gut)",["besser","gutter","besten"],"gut – besser – am besten.","A2"),
 Q("Im Sommer ist es ___ als im Winter. (warm)",["wärmer","warmer","wärmere"],"warm → wärmer, with an umlaut.","A2"),
 Q("Ich trinke ___ Tee als Kaffee. (gern)",["lieber","gerner","liebe"],"gern – lieber – am liebsten.","A2"),
 Q("Das ist der ___ Film des Jahres. (gut)",["beste","besste","bester"],"gut → beste, with the ending -e after der.","A2"),
 Q("Sie hat ___ Geld als ich. (viel)",["mehr","vieler","mehrer"],"viel – mehr – am meisten. mehr takes no ending.","A2"),
 Q("Welcher Berg ist ___? (hoch)",["am höchsten","am hochsten","höchste"],"hoch – höher – am höchsten.","B1"),
 Q("Je mehr ich übe, ___ besser spreche ich.",["desto","als","wie"],"je … desto + Komparativ.","B1"),
 Q("Das Auto ist ___ als das Fahrrad. (teuer)",["teurer","teuerer","teuer"],"teuer → teurer. The e before r drops.","B1"),
 Q("Dieser Raum ist ___ als der andere. (dunkel)",["dunkler","dunkeler","dunklerer"],"dunkel → dunkler. The e before l drops.","B1"),
 Q("Das ist der ___ Tag des Jahres. (kurz)",["kürzeste","kurzeste","kürzte"],"kurz → kürzer → der kürzeste.","B1"),
 Q("Er hat ein ___ Auto als ich. (groß)",["größeres","größer","größte"],"Komparativ before a noun: ein größeres Auto.","B1"),
 Q("Von allen Läufern läuft Anna ___. (schnell)",["am schnellsten","schnellste","der schnellste"],"After a verb with no noun: am + -sten.","B1"),
 Q("Im Winter wird es ___ kälter.",["immer","mehr","desto"],"immer + Komparativ: more and more.","B1"),
 Q("Komm bitte so ___ wie möglich. (schnell)",["schnell","schneller","am schnellsten"],"so … wie takes the basic form: so schnell wie möglich.","B2"),
 Q("Das Haus ist doppelt so ___ wie das alte. (groß)",["groß","größer","größte"],"doppelt so groß wie: basic form after so.","B2"),
 Q("Das war das ___ Essen, das ich je hatte. (gut)",["beste","bessere","gute"],"Superlativ with je: das beste Essen.","B2"),
 Q("Er wohnt im ___ Haus der Stadt. (hoch)",["höchsten","hochsten","höheren"],"hoch – höher – am höchsten. Dativ after im: im höchsten Haus.","B2"),
 Q("Das ist ___ unwahrscheinlich.",["höchst","höchste","am höchsten"],"höchst = extremely. This is an Elativ.","B2"),
 Q("Ich bin über alles ___ informiert.",["bestens","beste","am besten"],"bestens is an Elativ: very well.","C1"),
 Q("Wir danken Ihnen aufs ___.",["Herzlichste","Herzlichen","Herzlicher"],"aufs Herzlichste is a formal Elativ.","C1"),
]
TH=[
 tc("Stufen",[("schnell","schneller · am schnellsten"),("alt","älter · am ältesten"),("groß","größer · am größten"),("gut","besser · am besten"),("viel","mehr · am meisten"),("gern","lieber · am liebsten"),("hoch","höher · am höchsten"),("nah","näher · am nächsten")],"Unregelmäßig: gut, viel, gern, hoch, nah."),
 tc("Vergleichen",[("gleich","so groß wie"),("ungleich","größer als"),("je … desto","Je mehr, desto besser"),("immer","immer kälter"),("doppelt","doppelt so groß wie")],"Nach dem Komparativ steht als, nicht wie."),
 tc("Superlativ",[("ohne Nomen","am schnellsten"),("mit Nomen","der schnellste Läufer"),("Elativ","höchst interessant"),("Elativ","bestens informiert")],"Elativ: sehr, ohne Vergleich."),
]
apply("komp","Komparation","Adjektiv","Add -er, then am + -sten. Als after the Komparativ, wie after so.",
 '<span><b class="wt k lgk">-er</b> Komparativ</span><span><b class="wt v lgk">am -sten</b> Superlativ</span>',
 C,QS,TH,"adj",
 ' {t:"komp",n:"Komparation",tag:"schnell · schneller · am schnellsten",ds:"Steigerung, Umlaut, unregelmäßig, so … wie, als, je … desto, Elativ · A2–C1"},',
 '{n:"Adjektiv",t:["adj"],soon:"Vergleichen"}',
 '{n:"Adjektiv",t:["adj","komp"]}',
 "Steigerungsform oder Vergleichswort")
