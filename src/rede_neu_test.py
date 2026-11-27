#!/usr/bin/env python3
"""Staunen -> Redewendungen: die 50 Redewendungen (frueher Philosophie, Gesellschaft, Geschichte, Gefuehle, Argumentieren)
werden durch 50 gelaeufige ersetzt. Grundlage: Hallsteinsdottir/Sajankova/Quasthoff, "Phraseologisches Optimum fuer DaF",
Linguistik online 27, 2/2006 (Korpusfrequenz + Befragung von 101 Muttersprachlern), dazu 8 Lieblinge vieler Lernseiten.
Die Wort-Filter (Woerter mit Geschichte, Lehnwoerter, Scheinenglisch, Wortfamilien) bleiben unveraendert.
Herkunft nur, wo DWDS, Duden, Wikipedia (oder Wiktionary, markiert) sie stuetzen; sonst None. Geprueft 27.11.2026.
Aufruf:  python3 src/rede_neu_test.py        -> Testkopie rede6.html
         python3 src/rede_neu_test.py live   -> index.html
Idempotent: bricht ab, wenn der Schluessel "hilf" schon in RWT steht."""
import os,sys,json
LIVE=len(sys.argv)>1 and sys.argv[1]=='live'
root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
s=open(os.path.join(root,'index.html'),encoding='utf-8').read()
if '["hilf", ' in s: print('already'); raise SystemExit

N=None
W=lambda t:"https://de.wikipedia.org/wiki/"+t
NEW_T=[["hilf","Helfen & Zusammenhalten"],["gef","Gefühle & Nerven"],["erf","Erfolg & Pech"],["plan","Planen & Entscheiden"],["vers","Verstehen & Argumentieren"],["tric","Tricks & Fettnäpfchen"]]
NEW=[
# Helfen & Zusammenhalten
["hilf","B1","jemandem unter die Arme greifen","jemandem in einer schwierigen Lage helfen, oft mit Geld","to help someone out","Als ich arbeitslos war, haben mir meine Eltern unter die Arme gegriffen.",N,N],
["hilf","B2","an einem Strang ziehen","gemeinsam dasselbe Ziel verfolgen","to pull together","Wenn wir alle an einem Strang ziehen, schaffen wir das.","Der Strang ist hier die Zugleine im Geschirr eines Pferdes. Ziehen alle Tiere am selben Strang, kommt der Wagen voran. Belegt seit dem 18. Jahrhundert.",["https://www.dwds.de/wb/Strang","DWDS"]],
["hilf","B1","jemanden im Stich lassen","jemandem in einer Notlage nicht helfen, ihn allein lassen","to leave someone in the lurch","Mein Kollege hat mich mit der ganzen Arbeit im Stich gelassen.","Wohl aus dem Ritterturnier: Wer einen Kampfgefährten verließ, ließ ihn „im Stich“ des Gegners zurück. Belegt seit dem 15. Jahrhundert.",["https://www.dwds.de/wb/Stich","DWDS"]],
["hilf","A2","jemandem die Daumen drücken","jemandem Glück und Erfolg wünschen","to keep one’s fingers crossed for someone","Morgen ist meine Prüfung – drück mir die Daumen!","Wer bei einem Wettkampf mitfiebert, ballt unwillkürlich die Hände – so erklärt man die Geste. Wo man anderswo die Finger kreuzt, drückt man im Deutschen den Daumen.",[W("Daumen_dr%C3%BCcken"),"Wikipedia"]],
None, # Hals- und Beinbruch (bisheriger Eintrag)
["hilf","B2","in jemandes Fußstapfen treten","denselben Weg gehen wie ein Vorbild, oft wie die Eltern","to follow in someone’s footsteps","Sie ist Ärztin geworden und in die Fußstapfen ihrer Mutter getreten.",N,N],
["hilf","B2","sich ins Zeug legen","sich sehr anstrengen","to put one’s back into it","Für die Prüfung hat er sich richtig ins Zeug gelegt.","„Zeug“ ist hier das Geschirr von Zugpferden und Ochsen. Bei schwerer Last legen sich die Tiere mit ihrem ganzen Gewicht hinein.",["https://www.duden.de/sprachwissen/sprachratgeber/Das-Wort-%E2%80%9EZeug%E2%80%9C","Duden"]],
["hilf","B1","alle Hände voll zu tun haben","sehr viel Arbeit haben","to have one’s hands full","Vor Weihnachten haben wir im Geschäft alle Hände voll zu tun.",N,N],
# Gefuehle & Nerven
None, # aus dem Haeuschen sein
["gef","B1","die Nase voll haben","von etwas genug haben, es nicht mehr ertragen","to be fed up","Ich habe die Nase voll von diesem Regen.",N,N],
["gef","A2","jemandem auf die Nerven gehen","jemanden stören, ärgern","to get on someone’s nerves","Das ständige Hupen geht mir auf die Nerven.",N,N],
["gef","B2","jemandem ein Dorn im Auge sein","jemanden ständig stören, ein Ärgernis sein","to be a thorn in someone’s side","Die neue Baustelle ist den Anwohnern ein Dorn im Auge.","Aus der Bibel (4. Mose 33,55): Feinde, die man nicht vertreibt, werden einem zu „Dornen in den Augen“.",["https://www.duden.de/rechtschreibung/Dorn","Duden"]],
["gef","B2","sich in die Haare geraten","heftig miteinander streiten","to get into an argument","Die Geschwister geraten sich wegen jeder Kleinigkeit in die Haare.",N,N],
["gef","B1","das ist mir Wurst","das ist mir egal","I couldn’t care less","Ob wir Pizza oder Pasta essen, ist mir Wurst.","Aus der Studentensprache, Anfang 19. Jahrhundert. Eine Erklärung: Eine Wurst hat zwei gleiche Enden – egal, wo man anfängt.",["https://www.dwds.de/wb/etymwb/Wurst","DWDS"]],
["gef","B2","aus heiterem Himmel","völlig unerwartet, plötzlich","out of the blue","Aus heiterem Himmel hat er gekündigt.","Kurz für „wie ein Blitz aus heiterem Himmel“: ein Blitz, obwohl keine Wolke zu sehen ist.",["https://www.dwds.de/wb/aus%20heiterem%20Himmel","DWDS"]],
# Erfolg & Pech
["erf","B1","Schwein haben","Glück haben","to be lucky","Wir haben Schwein gehabt: Der Zug hatte auch Verspätung.","Oft erklärt mit einem alten Brauch: Bei Wettkämpfen bekam der Verlierer ein Schwein als Trostpreis. Ganz sicher ist die Herkunft nicht.",[W("Schwein_haben"),"Wikipedia"]],
["erf","B2","das Handtuch werfen","aufgeben","to throw in the towel","Nach drei Jahren Streit mit der Firma hat sie das Handtuch geworfen.","Aus dem Boxen (20. Jahrhundert): Der Trainer wirft ein Handtuch in den Ring und gibt den Kampf damit auf.",["https://www.dwds.de/wb/etymwb/Handtuch","DWDS"]],
["erf","B1","in die Hose gehen","misslingen, schiefgehen","to go wrong","Der erste Versuch ist leider in die Hose gegangen.",N,N],
["erf","B2","den Kürzeren ziehen","verlieren, im Nachteil sein","to draw the short straw","Im Streit mit der Versicherung hat er den Kürzeren gezogen.","Vom Losen mit Hölzchen oder Halmen: Wer das kürzere zieht, hat verloren. Belegt seit dem 16. Jahrhundert.",["https://www.dwds.de/wb/K%C3%BCrze","DWDS"]],
["erf","B2","ins Schwarze treffen","genau das Richtige sagen oder tun","to hit the bull’s-eye","Mit deiner Vermutung hast du ins Schwarze getroffen.","Aus dem Schießsport: Die Mitte der Zielscheibe ist schwarz.",[W("Schwarz"),"Wikipedia"]],
["erf","C1","sich auf seinen Lorbeeren ausruhen","nach einem Erfolg nichts mehr tun","to rest on one’s laurels","Nach dem Sieg darf sich die Mannschaft nicht auf ihren Lorbeeren ausruhen.","Mit einem Lorbeerkranz wurden früher Sieger und Dichter geehrt.",["https://www.dwds.de/wb/Lorbeer","DWDS"]],
["erf","B2","über die Runden kommen","mit wenig Geld gerade auskommen; eine schwere Zeit überstehen","to make ends meet","Mit seinem kleinen Gehalt kommt er kaum über die Runden.","Wohl aus dem Boxen: Wer angeschlagen ist, will nur noch bis zum Ende der letzten Runde durchhalten.",["https://de.wiktionary.org/wiki/%C3%BCber_die_Runden_kommen","Wiktionary"]],
["erf","B2","jemandem einen Strich durch die Rechnung machen","jemandes Plan zunichtemachen","to thwart someone’s plans","Das Wetter hat uns einen Strich durch die Rechnung gemacht.","Eine Rechnung, durch die man einen Strich zieht, gilt nicht mehr – und mit ihr der Plan.",["https://www.dwds.de/wb/dwb/rechnung","DWDS (Grimm)"]],
["erf","B1","jemandem einen Korb geben","jemanden abweisen, besonders bei einer Einladung oder in der Liebe","to turn someone down","Er wollte mit ihr tanzen, aber sie hat ihm einen Korb gegeben.","Früher sollen Frauen einen Verehrer in einem Korb zum Fenster hochgezogen haben. War er nicht willkommen, bekam er einen Korb mit brüchigem Boden – und fiel durch.",[W("Einen_Korb_geben"),"Wikipedia"]],
["erf","B1","etwas in den Griff bekommen","ein Problem unter Kontrolle bringen","to get a grip on something","Die Stadt hat das Verkehrsproblem endlich in den Griff bekommen.",N,N],
# Planen & Entscheiden
["plan","B2","etwas auf Eis legen","ein Vorhaben vorläufig stoppen","to put something on hold","Das Bauprojekt wurde aus Geldmangel auf Eis gelegt.",N,N],
["plan","B2","etwas über den Haufen werfen","einen Plan plötzlich aufgeben oder ganz ändern","to scrap something","Der Regen hat alle unsere Pläne über den Haufen geworfen.",N,N],
["plan","B1","grünes Licht geben","etwas erlauben, freigeben","to give the green light","Die Chefin hat grünes Licht für das neue Projekt gegeben.",N,N],
None, # auf der Kippe stehen
["plan","B2","in den Sternen stehen","noch völlig ungewiss sein","to be up in the air","Ob das Konzert stattfindet, steht noch in den Sternen.",N,N],
["plan","B2","auf dem Spiel stehen","in Gefahr sein, verloren gehen zu können","to be at stake","Bei dieser Entscheidung steht viel Geld auf dem Spiel.",N,N],
["plan","B1","sich etwas durch den Kopf gehen lassen","über etwas in Ruhe nachdenken","to mull something over","Ich lasse mir dein Angebot noch einmal durch den Kopf gehen.",N,N],
["plan","B2","alles unter einen Hut bringen","verschiedene Dinge oder Interessen miteinander vereinbaren","to juggle everything","Beruf, Kinder und Hobby unter einen Hut zu bringen, ist nicht leicht.",N,N],
["plan","B2","auf eigene Faust","selbstständig, ohne Hilfe oder Erlaubnis","on one’s own","Wir haben die Stadt auf eigene Faust erkundet.",N,N],
["plan","B2","in der Luft liegen","kurz bevorstehen, schon spürbar sein","to be in the air","Ein Streit lag schon den ganzen Abend in der Luft.",N,N],
# Verstehen & Argumentieren
["vers","A2","nur Bahnhof verstehen","gar nichts verstehen","it’s all Greek to me","Bei seinem Vortrag über Steuern habe ich nur Bahnhof verstanden.","Herkunft nicht sicher. Vielleicht von Soldaten am Ende des Ersten Weltkriegs, die nur noch an den Bahnhof dachten – an die Heimfahrt.",["https://www.duden.de/rechtschreibung/Bahnhof","Duden"]],
["vers","B1","Tomaten auf den Augen haben","etwas Offensichtliches nicht sehen","to be blind to the obvious","Hast du Tomaten auf den Augen? Die Ampel war rot!",N,N],
["vers","B2","im Dunkeln tappen","etwas nicht wissen, keine Anhaltspunkte haben","to be in the dark","Die Polizei tappt bei dem Einbruch noch im Dunkeln.",N,N],
["vers","B1","hinter dem Mond leben","nicht wissen, was in der Welt passiert","to live under a rock","Du kennst kein Smartphone? Du lebst wohl hinter dem Mond!",N,N],
["vers","B2","zwischen den Zeilen lesen","auch verstehen, was nur angedeutet ist","to read between the lines","Wer zwischen den Zeilen liest, merkt, dass sie unzufrieden ist.",N,N],
["vers","B2","auf der Hand liegen","ganz offensichtlich sein","to be obvious","Die Lösung liegt doch auf der Hand.",N,N],
None, # aus der Luft gegriffen sein
None, # ins Gewicht fallen
None, # etwas auf den Punkt bringen
["vers","C1","gang und gäbe sein","allgemein üblich sein","to be common practice","Homeoffice ist heute in vielen Firmen gang und gäbe.","Schon mittelhochdeutsch „genge und gæbe“. Gemeint waren Münzen und Waren, die gut „gehen“ und sich leicht „geben“ lassen – also im Umlauf sind.",["https://www.duden.de/rechtschreibung/gang","Duden"]],
# Tricks & Fettnaepfchen
["tric","B2","jemanden an der Nase herumführen","jemanden täuschen, hinhalten","to lead someone up the garden path","Der Verkäufer hat uns wochenlang an der Nase herumgeführt.","Nach dem Bild eines Tieres, das man an einem Nasenring führt.",["https://www.duden.de/rechtschreibung/Nase","Duden"]],
["tric","B2","jemanden über den Tisch ziehen","jemanden bei einem Geschäft betrügen","to rip someone off","Beim Autokauf hat man ihn ordentlich über den Tisch gezogen.","Vom Fingerhakeln, einem alten Kraftsport in Bayern und Österreich: Zwei sitzen am Tisch und ziehen einander am Finger herüber.",[W("Fingerhakeln"),"Wikipedia"]],
["tric","B2","jemandem etwas in die Schuhe schieben","jemandem die Schuld für etwas geben, das er nicht getan hat","to pin the blame on someone","Er hat den Fehler einfach seinem Kollegen in die Schuhe geschoben.",N,N],
["tric","B2","ins Fettnäpfchen treten","mit einer ungeschickten Bemerkung jemanden verärgern","to put one’s foot in it","Mit der Frage nach seiner Ex-Frau bin ich voll ins Fettnäpfchen getreten.","Belegt seit dem 19. Jahrhundert. Früher stand wohl ein Napf mit Stiefelfett am Herd. Wer hineintrat, machte Flecken – und sich unbeliebt.",[W("Ins_Fettn%C3%A4pfchen_treten"),"Wikipedia"]],
["tric","B1","aus der Reihe tanzen","sich anders verhalten als die anderen","to step out of line","In jeder Gruppe tanzt einer aus der Reihe.",N,N],
]
KEEP=dict(zip([i for i,r in enumerate(NEW) if r is None],[("Hals- und Beinbruch","hilf"),("aus dem Häuschen sein","gef"),("auf der Kippe stehen","plan"),
      ("aus der Luft gegriffen sein","vers"),("ins Gewicht fallen","vers"),("etwas auf den Punkt bringen","vers")]))

# alte Listen lesen
def arr(name):
    i=s.index('const '+name+'=')+len('const '+name+'=');d=0
    for k in range(i,len(s)):
        c=s[k]
        if c=='[':d+=1
        elif c==']':
            d-=1
            if d==0:return i,k+1
RWi,RWj=arr('RW'); RW=json.loads(s[RWi:RWj])
Ti,Tj=arr('RWT'); RWT=json.loads(s[Ti:Tj])
OLD={"phil","ges","his","gef","arg"}
byp={r[2]:r for r in RW}
for idx,(ph,g) in KEEP.items():
    assert NEW[idx] is None,(idx,ph); r=list(byp[ph]); r[0]=g; NEW[idx]=r
assert all(NEW) and len(NEW)==50,len(NEW)
assert len({r[2] for r in NEW})==50
RW2=NEW+[r for r in RW if r[0] not in OLD]
RWT2=NEW_T+[t for t in RWT if t[0] not in OLD]
assert len(RW2)==len(RW), (len(RW2),len(RW))
dump=lambda x:json.dumps(x,ensure_ascii=False)
s=s[:Ti]+dump(RWT2)+s[Tj:]
RWi,RWj=arr('RW')
s=s[:RWi]+dump(RW2)+s[RWj:]
out=os.path.join(root,'index.html' if LIVE else 'rede6.html')
open(out,'w',encoding='utf-8').write(s); print('wrote',out,len(RW2),'entries')
