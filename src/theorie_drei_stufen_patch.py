#!/usr/bin/env python3
"""Theorie in drei Stufen (Regel, Schritt fuer Schritt, Ausnahmen) fuer k1, nvv, vkas, indef, dopp, konn2, mpart, neg, tekamolo, modal, zuinf. Eigene Formulierung. Idempotent."""
import os,re
root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
p=os.path.join(root,"index.html");s=open(p,encoding="utf-8").read()
if "TH3C-MARK" in s: print("already");raise SystemExit
def rows(L): return '<div class="rows">'+''.join('<div><span>%s</span><span>%s</span></div>'%(a,b) for a,b in L)+'</div>'
def three(rule,tl1,steps,tl2,exc,lv):
    a,b,c=lv
    return ('<div class="tc df"><h3>1 · Die einfache Regel <small>%s</small></h3><p class="memo">%s</p><p class="tline">%s</p></div>\n'%(a,rule,tl1)+
            '<div class="tc df"><h3>2 · Schritt für Schritt <small>%s</small></h3>%s%s</div>\n'%(b,rows(steps),('<p class="tline">%s</p>'%tl2) if tl2 else '')+
            '<div class="tc df"><h3>3 · Ausnahmen &amp; mehr <small>%s</small></h3>%s</div>\n'%(c,rows(exc)))
T={}
T['k1']=three('Mit <b>Konjunktiv I</b> gibst du wieder, was jemand anderes gesagt hat, ohne es selbst zu behaupten. Du brauchst fast nur die <b>3. Person</b>: er <b>sei</b>, sie <b>habe</b>, er <b>komme</b>.','Sie sagt, er sei krank.',
 [("1 Wer sagt es?","Der Minister sagt: „Wir haben keine Zeit.“"),("2 Person umstellen","wir → sie"),("3 Verb in den Konjunktiv I","haben → habe"),("4 Ergebnis","Der Minister sagt, sie <b>hätten</b> keine Zeit. (siehe Ausnahme)")],'',
 [("Gleiche Form","Ist der Konjunktiv I gleich dem Indikativ (sie haben), nimmst du den Konjunktiv II: sie hätten."),("sein","Nur sein ist ganz regelmäßig: ich sei, du seist, er sei, wir seien."),("Gegenwart","Er sagt, er komme. (er komme = kommt oder kommen wird)"),("Vergangenheit","Er sagte, er sei krank gewesen. · sie habe gearbeitet."),("Zeitung","Der Konjunktiv I steht oft in Nachrichten und Berichten.")],('B2','B2','C1'))
T['nvv']=three('Eine <b>Nomen-Verb-Verbindung</b> besteht aus einem Nomen und einem Verb, das nur wenig Bedeutung hat. Die Bedeutung steckt im Nomen: <b>eine Entscheidung treffen</b> heißt entscheiden.','eine Entscheidung treffen = entscheiden',
 [("1 Nomen","die Entscheidung"),("2 Verb","treffen"),("3 Als Block lernen","eine Entscheidung treffen"),("4 Passendes Verb","nicht „machen“: eine Entscheidung machen ist falsch")],'',
 [("Artikel","Meist ohne oder mit festem Artikel: in Kauf nehmen · zur Verfügung stellen."),("Passiv","Die Entscheidung wurde getroffen."),("Stil","Nomen-Verb-Verbindungen klingen formeller als das einfache Verb."),("Nicht tauschen","Das Verb lässt sich nicht beliebig ersetzen: Rücksicht nehmen (nicht „Rücksicht machen“).")],('B2','B2','C1'))
T['vkas']=three('Das <b>Verb</b> bestimmt den Fall des Objekts. Die meisten Verben haben ein Objekt im <b>Akkusativ</b> (wen? was?). Nur einige verlangen den <b>Dativ</b> (wem?).','Ich sehe den Mann. · Ich helfe dem Mann.',
 [("1 Verb","helfen"),("2 Frage","Wem helfe ich?"),("3 Fall","dem Mann → Dativ"),("4 Merken","Fall mit dem Verb lernen: helfen + Dativ")],'',
 [("Nur Dativ","helfen, danken, gefallen, gehören, folgen, antworten, zuhören"),("Zwei Objekte","Ich gebe dem Kind (Dativ) einen Apfel (Akkusativ)."),("Genitiv","sich bedienen, gedenken (formell, selten)"),("Wie im Englischen?","Nicht übertragen: jemandem helfen, nicht „jemanden helfen“.")],('A2','B1','B2'))
T['indef']=three('<b>man</b> ist ein Pronomen für „irgendjemand“ oder „die Leute“. Es steht immer im <b>Nominativ</b>, und das Verb steht in der 3. Person Singular: <b>man kann</b>.','Man spricht hier Deutsch.',
 [("1 Allgemein","Man darf hier nicht rauchen."),("2 Mit Modalverb","Man muss das nicht wissen."),("3 Wiederholung","Nach man bleibt es bei man (nicht er)."),("4 Mengen","alle · viele · einige · wenige · manche (siehe Mengen)")],'',
 [("Akkusativ","Das kann einen stören. (einen = man im Akkusativ)"),("Dativ","Das kann einem passieren."),("jemand · niemand","jemand = irgendeine Person · niemand = keine Person"),("etwas · nichts","Ich habe nichts gehört. · Hast du etwas gesehen?")],('A2','B1','B2'))
T['dopp']=three('Zweiteilige Konnektoren bestehen aus <b>zwei</b> Teilen, die zusammengehören: <b>sowohl … als auch</b>, <b>entweder … oder</b>, <b>weder … noch</b>. Sie verbinden gleichwertige Teile.','Ich mag sowohl Tee als auch Kaffee.',
 [("1 Paar wählen","sowohl … als auch (beides)"),("2 Beide Teile setzen","Ich mag <b>sowohl</b> Tee <b>als auch</b> Kaffee."),("3 Verb prüfen","Das Verb richtet sich nach dem Subjekt: Sowohl er als auch sie sind da."),("4 Komma","vor dem zweiten Teil steht kein Komma, wenn nur Wörter verbunden werden.")],'',
 [("nicht nur … sondern auch","Er ist nicht nur freundlich, sondern auch hilfsbereit."),("je … desto","Je mehr ich lerne, desto besser verstehe ich."),("zwar … aber","Er ist zwar klein, aber stark."),("weder … noch","Sie hat weder Zeit noch Lust.")],('B1','B2','C1'))
T['konn2']=three('Formelle Konnektoren verbinden Sätze in <b>Schrift und Vortrag</b>. Sie sind länger und genauer als und, aber und weil: <b>jedoch</b>, <b>außerdem</b>, <b>folglich</b>, <b>dennoch</b>.','Es regnet. Dennoch gehen wir spazieren.',
 [("1 Bedeutung","Gegensatz: jedoch, dennoch · Folge: folglich, daher · Zusatz: außerdem"),("2 Position","Das Verb steht direkt nach dem Konnektor."),("3 Satz bauen","Er ist krank. Folglich <b>bleibt</b> er zu Hause."),("4 Tipp","Nicht überall verwenden: gesprochen reichen oft aber und deshalb.")],'',
 [("Nebensatz-Konnektoren","indem, sodass, während, sofern: das Verb steht am Ende."),("Gegensatz","Er ist reich. Er ist jedoch unglücklich."),("Folge","Das Wetter war schlecht, sodass wir blieben."),("Bedingung","Sofern es Zeit gibt, treffen wir uns.")],('B2','B2','C1'))
T['mpart']=three('<b>Modalpartikeln</b> verändern den Ton eines Satzes, nicht den Inhalt. Sie stehen im <b>Mittelfeld</b> und werden <b>nicht betont</b>: <b>doch, ja, mal, denn, eben, halt, schon, wohl</b>.','Komm doch mal vorbei!',
 [("1 Satz ohne Partikel","Komm vorbei!"),("2 Ton wählen","freundlich, eine Einladung"),("3 Partikel einsetzen","Komm <b>doch</b> vorbei!"),("4 Betonung","Die Partikel bleibt unbetont.")],'',
 [("Nur gesprochen","Modalpartikeln gehören vor allem in die Alltagssprache."),("Nicht übersetzbar","Es gibt oft kein genaues englisches Wort."),("Betontes doch","Als Widerspruch ist DOCH betont: Du kommst nicht? – Doch!"),("Satzart","denn passt zu Fragen, ja zu Aussagen, mal zu Bitten.")],('B1','B2','C1'))
T['neg']=three('<b>kein</b> verneint ein Nomen mit unbestimmtem Artikel oder ohne Artikel. <b>nicht</b> verneint alles andere: Verben, Adjektive, bestimmte Nomen.','Ich habe kein Auto. · Ich arbeite nicht.',
 [("1 Nomen mit ein-/ohne Artikel","Ich habe ein Auto → Ich habe <b>kein</b> Auto."),("2 Mit der/die/das","Ich kenne den Mann → Ich kenne den Mann <b>nicht</b>."),("3 Verb","Ich schlafe <b>nicht</b>."),("4 Adjektiv","Er ist <b>nicht</b> müde.")],'',
 [("Position von nicht","Am Satzende, wenn es das Verb verneint; sonst vor dem Teil, den du verneinen willst."),("sondern","Nicht heute, sondern morgen."),("weder … noch","Ich habe weder Zeit noch Geld."),("nie · niemand · nichts","Er sagt nichts. · Ich sehe niemanden.")],('A1','A2','B1'))
T['tekamolo']=three('Im Mittelfeld stehen die Angaben meist in dieser Reihenfolge: <b>Te</b>mporal (wann), <b>Ka</b>usal (warum), <b>Mo</b>dal (wie), <b>Lo</b>kal (wo).','Ich fahre morgen wegen der Arbeit mit dem Zug nach Wien.',
 [("1 Te (wann)","morgen"),("2 Ka (warum)","wegen der Arbeit"),("3 Mo (wie)","mit dem Zug"),("4 Lo (wo/wohin)","nach Wien")],'',
 [("Pronomen zuerst","Ich gebe es ihm morgen. (Pronomen vor den Angaben)"),("Betonung","Das Wichtige kann nach vorn: Morgen fahre ich mit dem Zug nach Wien."),("Nicht streng","Die Reihenfolge ist eine Tendenz, keine feste Regel."),("Mehrere Angaben","Meist reichen zwei oder drei Angaben im Satz.")],('B1','B1','B2'))
T['modal']=three('Modalverben (<b>können, müssen, dürfen, sollen, wollen, mögen</b>) stehen an Position 2. Das zweite Verb steht als <b>Infinitiv am Ende</b>.','Ich kann schwimmen.',
 [("1 Modalverb","kann (Position 2)"),("2 Rest des Satzes","Ich kann gut"),("3 Infinitiv ans Ende","Ich kann gut <b>schwimmen</b>.")],'',
 [("ich/er","ich kann · er kann (ohne -t)"),("nicht müssen","Du musst nicht kommen = Du brauchst nicht zu kommen."),("Nebensatz","…, weil ich schwimmen können will (Modalverb ganz am Ende)."),("Perfekt","Ich habe schwimmen können. oder: Ich konnte schwimmen.")],('A1','A2','B1'))
T['zuinf']=three('Nach vielen Verben und Ausdrücken steht der Infinitiv <b>mit zu</b>: <b>Ich versuche, früh aufzustehen.</b> Nach Modalverben steht er <b>ohne zu</b>.','Ich habe vergessen, dich anzurufen.',
 [("1 Hauptsatz","Ich habe vergessen,"),("2 Komma","Komma vor dem zu-Satz (meist)"),("3 zu + Infinitiv","dich anzurufen"),("4 Trennbar","zu steht zwischen Vorsilbe und Verb: an<b>zu</b>rufen")],'',
 [("um … zu","Ich lerne, um die Prüfung zu bestehen (Zweck)."),("ohne … zu","Er geht, ohne zu grüßen."),("statt … zu","Sie liest, statt zu schlafen."),("Ohne zu","nach Modalverben, lassen, gehen, bleiben, sehen und hören: Ich muss gehen.")],('B1','B1','B2'))
for k,v in T.items():
    i=s.index('GT.%s='%k);j=s.index('th:`',i)+4
    assert s[j:j+14]=='<div class="tc',(k,s[j:j+40])
    s=s[:j]+v+s[j:]
s=s.rstrip('\n')+'\n<!--TH3C-MARK-->\n'
open(p,'w',encoding='utf-8').write(s)
print('ok',len(T))
