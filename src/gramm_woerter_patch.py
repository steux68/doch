#!/usr/bin/env python3
"""Redewendungen: neuer Filter "Grammatikwoerter" (10 Fachwoerter mit Herkunft, alle nach DWDS geprueft am 27.11.2026). Umlaut entfaellt: DWDS hat dort keine Etymologie. Idempotent."""
import os,json,re
from urllib.parse import quote
root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
p=os.path.join(root,"index.html");s=open(p,encoding="utf-8").read()
if '["gram","A1","die Grammatik"' in s: print("already");raise SystemExit
def row(k,l,w,e,en,x,h,slug):
    for t in (w,e,en,x,h): assert '"' not in t and "'" not in t,t
    return '["%s","%s","%s","%s","%s","%s",%s,%s]'%(k,l,w,e,en,x,json.dumps(h,ensure_ascii=False),json.dumps(["https://www.dwds.de/wb/"+quote(slug),"DWDS"],ensure_ascii=False))
R=[
("gram","A1","die Grammatik","die Lehre vom Bau einer Sprache und ihren Regeln","grammar","Ohne Grammatik versteht man den Satz nicht richtig.","Aus griechisch grammatikḗ (téchnē), „Kunst der Buchstaben“, zu grámma, „Buchstabe, Geschriebenes“ (gráphein, ritzen, schreiben). Über das Lateinische kam das Wort ins Althochdeutsche (grammatih um 1000); die heutige Form Grammatik gibt es seit dem 16. Jahrhundert.","Grammatik"),
("gram","A1","das Verb","das Wort für eine Handlung oder einen Zustand","verb","Im Satz steht das Verb an zweiter Stelle.","Aus lateinisch verbum, „Wort“. Im 15. Jahrhundert kam es als Fachwort in die deutschen Grammatiken. Daneben gab es Namen wie Zeitwort, Sagwort und Tätigkeitswort. Die Form Verb ist seit der ersten Hälfte des 18. Jahrhunderts belegt, wurde aber erst Ende des 19. Jahrhunderts üblich.","Verb"),
("gram","A1","der Artikel","das kleine Wort vor dem Nomen: der, die, das","article (the little word before a noun)","Der Artikel verrät das Geschlecht des Nomens.","Aus lateinisch articulus, „kleines Gelenk, Glied“ (zu artus, Glied). 1291 ist es zuerst als Abschnitt eines Vertrags belegt. Als Grammatikwort, gleichsam ein „Gelenk“ im Satz, wurde es im 16. Jahrhundert entlehnt und ist seit dem 17. Jahrhundert der übliche Name für der, die, das. Der Zeitungsartikel kommt erst im 18. Jahrhundert.","Artikel"),
("gram","A2","der Nominativ","der Fall des Subjekts: wer oder was?","nominative case","Der Hund schläft im Garten.","Aus lateinisch cāsus nōminātīvus, „Fall des Nennens“ (zu nōmināre, nennen). Als deutsches Wort zuerst 1691 bei Kaspar von Stieler. Daneben standen Nennendung und später bei Gottsched Nennfall.","Nominativ"),
("gram","A2","der Akkusativ","der Fall des direkten Objekts: wen oder was?","accusative case (a translation mistake)","Ich sehe den Hund.","Aus lateinisch cāsus accūsātīvus, „Fall der Anklage“ (zu accūsāre, anklagen). Das ist ein Übersetzungsfehler: Das griechische Vorbild aitiatikḗ meinte den Fall, den das Verb bewirkt, und kommt von aition, „Ursache“. Deutsche Namen wie Klagendung (1641) und Klagefall (Lessing 1759) setzten sich nicht durch; im 19. Jahrhundert wurde Akkusativ üblich.","Akkusativ"),
("gram","A2","der Dativ","der Fall des Empfängers: wem?","dative case (the giving case)","Ich gebe dem Kind einen Apfel.","Aus lateinisch cāsus datīvus, „Fall des Gebens“, nach griechisch dotikḗ ptōsis. Beide gehören zu „geben“ (dare, didónai). Frühe deutsche Übersetzungen waren Drittfall (frühes 17. Jahrhundert) und Gebendung (spätes 17. Jahrhundert), etwa gleichzeitig kommt Dativ als deutsches Wort auf.","Dativ"),
("gram","B1","der Genitiv","der Fall des Besitzes: wessen?","genitive case","Das ist das Auto meines Vaters.","Aus lateinisch cāsus genitīvus, nach griechisch genikḗ ptōsis, dem „allgemeinen Fall“ (zur Gattung gehörig). Lateinische Grammatiker brachten es fälschlich mit „zeugen“ zusammen; darum hieß der Fall im Deutschen auch Zeugefall. Andere Versuche: Besitzfall (1619). Genitiv oder Genetiv setzt sich Mitte des 18. Jahrhunderts durch.","Genitiv"),
("gram","B1","die Präposition","das Wort vor einem Nomen, das den Fall bestimmt: in, auf, mit","preposition","Ich warte auf den Bus.","Aus lateinisch praepositio, „das Voranstellen“ (zu praepōnere, voranstellen). Mitte des 17. Jahrhunderts als Fachwort entlehnt. Deutsche Namen waren Vorwort (Schottelius 1641) und Vorsetzwort; seit 1801 setzte Campe Verhältniswort dagegen, und das wurde die deutsche Entsprechung.","Präposition"),
("gram","B2","der Konjunktiv","die Verbform für Wunsch, Möglichkeit und indirekte Rede","subjunctive mood","Wenn ich Zeit hätte, käme ich mit.","Aus spätlateinisch (modus) coniūnctīvus, „verbindende Form“, zu coniungere, verbinden. Dasselbe Verb steckt in Konjunktion. Im 17. Jahrhundert ins Deutsche übernommen; bis ins 19. Jahrhundert schrieb man oft noch Conjunctivus.","Konjunktiv"),
("gram","C1","der Ablaut","der feste Vokalwechsel in verwandten Wörtern: singen, sang, gesungen","ablaut (vowel gradation)","Der Ablaut zeigt sich bei starken Verben wie singen, sang, gesungen.","Als Fachwort prägte es Jacob Grimm 1819 für den vererbten Vokalwechsel in verwandten Wörtern. Vorher kam das Wort im 17. und 18. Jahrhundert nur gelegentlich vor, locker für einen schiefen, unreinen Klang. Es setzt sich aus ab und Laut zusammen.","Ablaut"),
]
rows=''.join(','+row(*r) for r in R)
j=s.index('];',s.index('"fam","B1","der Unfall"'))
s=s[:j]+rows+s[j:]
a='["fam", "Wortfamilien"]];'
assert s.count(a)==1
s=s.replace(a,'["fam", "Wortfamilien"], ["gram", "Grammatikwörter"]];')
m=re.search(r'(<meta name="app-version" content=")([^"]*)(")',s); s=s.replace(m.group(0),m.group(1)+'2026-11-27-gramm'+m.group(3),1)
open(p,'w',encoding='utf-8').write(s);print('ok',len(R))
