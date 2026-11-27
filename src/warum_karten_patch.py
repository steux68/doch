#!/usr/bin/env python3
"""'Warum?'-Karten: je eine Erklaerungskarte am Ende der Theorie fuer Faelle, Nebensaetze, Zeitformen, Praesens, Konjunktiv II, Verneinung, Plural, Wortbildung, Verben & Faelle, Komparation. Eigene Formulierung, keine unbelegten Herkunftsbehauptungen. Idempotent."""
import os
root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
p=os.path.join(root,"index.html");s=open(p,encoding="utf-8").read()
if "WARUM-MARK" in s: print("already");raise SystemExit
def card(t,memo,line,lv): return '<div class="tc df"><h3>Warum? %s <small>%s</small></h3><p class="memo">%s</p><p class="tline">%s</p></div>'%(t,lv,memo,line)
C={
'fall':card('der → den','Im Deutschen zeigt der <b>Artikel</b> den Fall an, denn am Nomen selbst sieht man ihn kaum noch. Nur beim <b>Maskulinum</b> ändert sich der Artikel im Akkusativ: <b>der</b> Mann → <b>den</b> Mann. Bei die, das und der Mehrzahl (die) bleibt der Akkusativ gleich.','Ich sehe den Mann · die Frau · das Kind · die Kinder.','A1'),
'nebs':card('steht das Verb am Ende','Denke an eine <b>Klammer</b>. Im Hauptsatz steht das Verb an Platz 2. Im Nebensatz öffnet die Konjunktion (weil, dass, wenn) die Klammer, und das Verb <b>schließt</b> sie am Ende. So erkennt man beim Hören sofort: Der Nebensatz ist erst zu Ende, wenn das Verb kommt.','Ich bleibe zu Hause, weil ich müde <b>bin</b>.','A2'),
'perf':card('steht das Partizip am Ende','Auch hier gibt es eine <b>Klammer</b>: Das Hilfsverb (haben oder sein) steht an Platz 2, das <b>Partizip II</b> schließt den Satz. Dazwischen steht alles Übrige. Darum wartet man im Deutschen oft bis zum Schluss auf das Wichtigste.','Ich <b>habe</b> gestern lange mit Anna telefoniert<b>.</b>','A2'),
'praes':card('trennt sich die Vorsilbe','Trennbare Vorsilben werden <b>betont</b> und verhalten sich wie ein eigenes Wort. Sie bilden mit dem Verb eine Klammer: Das Verb steht an Platz 2, die Vorsilbe geht ans Ende. Bei untrennbaren Verben liegt die Betonung auf dem Verb, und nichts trennt sich.','Ich <b>rufe</b> dich morgen <b>an</b>. (ánrufen) · Ich verstehe dich. (verstéhen)','A2'),
'k2':card('würde + Infinitiv','Bei vielen Verben sieht der Konjunktiv II genauso aus wie das Präteritum (ich arbeitete, ich machte). Man hört dann nicht, ob etwas <b>wirklich</b> oder nur <b>gedacht</b> ist. Mit <b>würde + Infinitiv</b> wird es eindeutig. Nur bei häufigen Verben (sein, haben, können) benutzt man die eigene Form.','Wenn ich Zeit hätte, <b>würde</b> ich mehr <b>reisen</b>.','B1'),
'neg':card('kein statt nicht','<b>kein</b> ist die Verneinung von <b>ein</b>. Wo man „ein“ sagen könnte oder gar keinen Artikel hat, sagt man „kein“. Alles andere (Verben, Adjektive, bestimmte Artikel) verneint man mit <b>nicht</b>.','ein Auto → kein Auto · das Auto → nicht das Auto','A1'),
'plural':card('ist das Mädchen sächlich','Das grammatische Geschlecht folgt oft der <b>Endung</b>, nicht dem natürlichen Geschlecht. Verkleinerungen auf <b>-chen</b> und <b>-lein</b> sind immer sächlich: das Mädchen, das Fräulein, das Brötchen. Darum heißt es „das Mädchen“, auch wenn es ein Mädchen ist.','das Mädchen · das Häuschen · das Büchlein','A2'),
'wortb':card('werden Nomen großgeschrieben','Im Deutschen schreibt man <b>alle Nomen</b> groß, auch Abstraktes (die Freiheit) und Wörter, die zu Nomen werden: <b>das</b> Essen, <b>beim</b> Laufen, <b>im</b> Ganzen. So erkennt man Satzbausteine beim Lesen schneller. Merke: Steht davor ein Artikel oder eine Präposition mit Artikel, ist es meist ein Nomen.','Das Lesen fällt mir leicht. · Beim Kochen höre ich Musik.','A2'),
'vkas':card('helfen + Dativ','Eine strenge Regel gibt es nicht: Das <b>Verb</b> bestimmt den Fall. Als Merkhilfe: Beim Dativ geht es oft um eine <b>Person, der etwas nützt oder gefällt</b> – helfen, danken, gefallen, gehören, antworten. Am besten lernt man das Verb mit dem Fall zusammen.','Ich helfe <b>dir</b>. · Das Buch gehört <b>mir</b>.','B1'),
'komp':card('gut – besser – am besten','Sehr häufige Wörter behalten oft alte, unregelmäßige Formen. Man benutzt sie so oft, dass sie sich nicht an die Regel anpassen: gut – besser – am besten, viel – mehr – am meisten, gern – lieber – am liebsten. Lerne diese Reihen als Block.','gut → besser → am besten','A2'),
}
for k,v in C.items():
    if k=='fall':
        i=s.index('const TH_FALL=`');j=s.index('`;',i)
        s=s[:j]+'\n'+v+s[j:]
    else:
        i=s.index('GT.%s='%k);a=s.index(' th:`',i);j=s.index('`',a+5)
        s=s[:j]+'\n'+v+s[j:]
s=s.rstrip('\n')+'\n<!--WARUM-MARK-->\n'
open(p,'w',encoding='utf-8').write(s);print('ok',len(C))
