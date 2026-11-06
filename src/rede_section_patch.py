#!/usr/bin/env python3
"""Redewendungen as a section of its own (Steuart, 6 Nov 2026): seventh bar [05] after Zitate (the last row keeps one empty white half, like PASSAGE),
a pin on the title page (Weimar), five themes of ten idioms, filter chips, origin notes only where a source was checked.
Replaces the first version that sat under the quotes (redewendungen_patch.py). Run from the repo root."""
import re, sys
p = "index.html"
s = open(p, encoding="utf-8").read()
if 'id="p-rede"' in s:
    sys.exit("already patched")

# 1. remove the first version (block under the quotes)
a = s.index("/* ---------- Redewendungen: [Stufe")
b = s.index("function renderQuotes(){")
s = s[:a] + "@@RWDATA@@\n" + s[b:]
s = s.replace("+'</div>'+rwHTML();loadPics($(\"p-quotes\"));rwBind($(\"p-quotes\"));", "+'</div>';loadPics($(\"p-quotes\"));", 1)

# 2. data + rendering
T = [("phil", "Philosophie & Denken"), ("ges", "Gesellschaft & Kultur"), ("his", "Geschichte & Alte Welt"), ("gef", "Gefühle & Lagen"), ("arg", "Argumentieren")]
WP = "https://de.wikipedia.org/wiki/"
DUD = "https://www.duden.de/rechtschreibung/"
R = [
 # [theme, level, phrase, German explanation, English, example, origin note, [url, source name]]
 ["phil","C1","des Pudels Kern","der eigentliche, wesentliche Punkt einer Sache","the heart of the matter","Das also ist des Pudels Kern: Niemand wollte die Verantwortung übernehmen.","Aus Goethes „Faust I“, Studierzimmer (Pudelszene): Der Pudel, der Faust folgt, zeigt sich als Mephisto. Hinter dem Harmlosen steckt der eigentliche Kern.",[WP+"Des_Pudels_Kern","Wikipedia"]],
 ["phil","C1","der Weisheit letzter Schluss","die endgültige, beste Lösung (meist verneint gebraucht)","the final word in wisdom (usually negated)","Mehr Kontrolle ist nicht der Weisheit letzter Schluss.",None,None],
 ["phil","B2","der rote Faden","der Gedanke, der einen Text oder Vortrag zusammenhält","the common thread","In deinem Aufsatz fehlt der rote Faden.",None,None],
 ["phil","C1","das Ei des Kolumbus","eine überraschend einfache Lösung","a brilliantly simple solution","Die Lösung war kein Ei des Kolumbus, aber sie hat funktioniert.","Die Anekdote erzählte Vasari zuerst über den Baumeister Brunelleschi. Auf Kolumbus übertrug sie erst Benzoni 1565, der sie nur vom Hörensagen kannte. Historisch gesichert ist sie nicht.",[WP+"Ei_des_Kolumbus","Wikipedia"]],
 ["phil","C1","die Quadratur des Kreises","eine unlösbare Aufgabe","squaring the circle","Billig, schnell und gut zugleich: Das ist die Quadratur des Kreises.",None,None],
 ["phil","B2","der Stein der Weisen","die ersehnte Lösung, nach der alle suchen","the philosopher’s stone","Einen Stein der Weisen für gutes Lernen gibt es nicht.",None,None],
 ["phil","C1","die Spreu vom Weizen trennen","das Wertlose vom Wertvollen unterscheiden","to separate the wheat from the chaff","Ein guter Test trennt die Spreu vom Weizen.",None,None],
 ["phil","B2","das A und O","das Wichtigste, die Grundlage","the be-all and end-all","Regelmäßige Übung ist das A und O beim Sprachenlernen.",None,None],
 ["phil","C1","zwischen Skylla und Charybdis","zwischen zwei gleich großen Gefahren oder Übeln","between a rock and a hard place","Die Firma steckt zwischen Skylla und Charybdis: sparen oder Schulden machen.",None,None],
 ["phil","C1","den Rubikon überschreiten","eine Entscheidung treffen, die sich nicht mehr rückgängig machen lässt","to cross the Rubicon","Mit der Kündigung hat er den Rubikon überschritten.",None,None],

 ["ges","B2","Tacheles reden","offen und ohne Beschönigung die Wahrheit sagen","to talk straight","Jetzt reden wir Tacheles: So geht es nicht weiter.","Jiddisch „tachles“ heißt „Ziel, Zweck“, dahinter steht ein hebräisches Wort. „Tacheles reden“ hieß zuerst „zur Sache kommen“.",[DUD+"Tacheles","Duden"]],
 ["ges","B1","Hals- und Beinbruch","Glückwunsch vor einer Prüfung oder einem Auftritt","break a leg","Hals- und Beinbruch für deine Prüfung morgen!","Die Herkunft ist umstritten. Manche leiten es vom Jiddischen „hazloche un brocha“ (Erfolg und Segen) ab. Gesichert ist das nicht.",["https://www.duden.de/sprachwissen/sprachratgeber/Hals-und-Beinbruch","Duden"]],
 ["ges","C1","Schmiere stehen","bei einer verbotenen Tat Wache halten","to keep watch for criminals","Er stand Schmiere, während die anderen einbrachen.","„Schmiere“ in der Bedeutung „Wache“ kommt aus der Gaunersprache, über das Jiddische „schmiro“ (Bewachung) aus dem Hebräischen.",[DUD+"Schmiere_Wache","Duden"]],
 ["ges","B2","über den eigenen Schatten springen","etwas tun, das einem sehr schwerfällt","to overcome one’s own reluctance","Ich bin über meinen Schatten gesprungen und habe mich entschuldigt.",None,None],
 ["ges","B2","etwas unter den Teppich kehren","ein Problem verschweigen, statt es zu lösen","to sweep something under the carpet","Man darf die Missstände nicht unter den Teppich kehren.",None,None],
 ["ges","B1","das Kind beim Namen nennen","Dinge offen und ehrlich aussprechen","to call a spade a spade","Nennen wir das Kind beim Namen: Das ist Betrug.",None,None],
 ["ges","B2","jemanden im Regen stehen lassen","jemandem in einer schwierigen Lage nicht helfen","to leave someone in the lurch","Der Partner ließ sie finanziell im Regen stehen.",None,None],
 ["ges","C1","auf großem Fuß leben","viel Geld ausgeben und luxuriös leben","to live in grand style","Die Familie lebte lange auf großem Fuß.",None,None],
 ["ges","B2","auf dem hohen Ross sitzen","überheblich auftreten","to be on one’s high horse","Steig von deinem hohen Ross herunter und hör zu.",None,None],
 ["ges","B1","ein Auge zudrücken","etwas Kleines nicht streng bestrafen","to turn a blind eye","Bei der ersten Verspätung drückt der Chef ein Auge zu.",None,None],

 ["his","C1","eine Lanze für jemanden brechen","sich öffentlich für jemanden einsetzen","to stand up for someone","Sie brach eine Lanze für die Praktikanten.","Das Bild kommt vom ritterlichen Turnier, bei dem man mit der Lanze für jemanden kämpfte.",["https://www.dwds.de/wb/etymwb/Lanze","DWDS"]],
 ["his","B2","jemanden in die Schranken weisen","jemandes Macht oder Verhalten begrenzen","to put someone in their place","Das Gericht wies den Konzern in die Schranken.",None,None],
 ["his","C1","jemandem den Fehdehandschuh hinwerfen","jemanden herausfordern","to throw down the gauntlet","Mit dieser Kritik warf er der Regierung den Fehdehandschuh hin.",None,None],
 ["his","B2","für jemanden die Hand ins Feuer legen","fest für jemanden bürgen","to vouch for someone","Für meinen Bruder lege ich die Hand ins Feuer.",None,None],
 ["his","B1","auf dem Holzweg sein","sich irren, eine falsche Richtung verfolgen","to be barking up the wrong tree","Wenn du glaubst, das klappt ohne Übung, bist du auf dem Holzweg.","Ein Holzweg war ein Weg im Wald, auf dem man Holz abtransportierte. Er führte nirgendwohin. Die übertragene Wendung ist seit dem 15. Jahrhundert belegt, Luther gebrauchte sie, und Heidegger nannte ein Buch „Holzwege“.",[WP+"Auf_dem_Holzweg_sein","Wikipedia"]],
 ["his","B2","mit seinem Latein am Ende sein","nicht mehr weiterwissen","to be at one’s wits’ end","Der Techniker war mit seinem Latein am Ende.",None,None],
 ["his","B2","sich die Sporen verdienen","sich in einer neuen Aufgabe bewähren","to win one’s spurs","Im Verlag verdiente sie sich ihre ersten Sporen.",None,None],
 ["his","B2","die Flinte ins Korn werfen","aufgeben","to throw in the towel","Nach dem ersten Misserfolg warf er die Flinte ins Korn.",None,None],
 ["his","B2","etwas auf die lange Bank schieben","etwas aufschieben","to put something off","Die Steuererklärung schiebe ich immer auf die lange Bank.","Die „lange Bank“ war vermutlich eine Truhe im Gericht, in der weniger dringende Akten lagen, bis sie nach hinten rückten. Das gilt als plausibel, aber nicht als vollständig gesichert.",[WP+"Lange_Bank","Wikipedia"]],
 ["his","C1","unter die Haube kommen","heiraten (veraltend, scherzhaft)","to get married (dated, jokingly)","Früher hieß es, eine Frau müsse mit dreißig unter die Haube kommen.",None,None],

 ["gef","B2","außer sich sein","vor Wut oder Aufregung die Beherrschung verlieren","to be beside oneself","Er war außer sich vor Zorn, als er die Rechnung sah.",None,None],
 ["gef","B1","in der Klemme sitzen","in einer schwierigen Lage sein","to be in a tight spot","Ich sitze in der Klemme: Die Miete ist fällig, aber das Gehalt kommt erst nächste Woche.",None,None],
 ["gef","B1","im siebten Himmel sein","überglücklich sein","to be on cloud nine","Seit der Hochzeit ist sie im siebten Himmel.",None,None],
 ["gef","B1","mit den Nerven am Ende sein","psychisch völlig erschöpft sein","to be at the end of one’s tether","Nach drei Wochen Lärm auf der Baustelle bin ich mit den Nerven am Ende.",None,None],
 ["gef","B1","aus dem Häuschen sein","vor Freude oder Aufregung ganz aufgeregt sein","to be beside oneself with excitement","Die Kinder waren aus dem Häuschen, als der erste Schnee fiel.",None,None],
 ["gef","B2","in der Bredouille sein","in einer unangenehmen Lage sein","to be in a pickle","Ohne Ersatzteil sind wir ganz schön in der Bredouille.",None,None],
 ["gef","B2","im Zwiespalt sein","zwischen zwei Gefühlen oder Entscheidungen hin- und hergerissen sein","to be torn","Ich bin im Zwiespalt: Soll ich bleiben oder gehen?",None,None],
 ["gef","B2","auf der Kippe stehen","unsicher sein, ob etwas gut oder schlecht ausgeht","to hang in the balance","Das Projekt steht auf der Kippe.",None,None],
 ["gef","B2","mit jemandem im Reinen sein","keinen ungelösten Streit mit jemandem haben","to be at peace with someone","Nach dem Gespräch war ich mit ihm wieder im Reinen.",None,None],
 ["gef","B1","am Boden zerstört sein","völlig verzweifelt sein","to be devastated","Nach der Absage war sie am Boden zerstört.",None,None],

 ["arg","C1","außer Frage stehen","nicht bezweifelt werden können","to be beyond question","Dass wir handeln müssen, steht außer Frage.",None,None],
 ["arg","C1","zur Debatte stehen","gerade diskutiert oder entschieden werden","to be up for debate","Zur Debatte steht, ob die Frist verlängert wird.",None,None],
 ["arg","C1","Hand und Fuß haben","gut durchdacht und überzeugend sein (≈ stichhaltig)","to hold water, to be well thought out","Dein Vorschlag hat Hand und Fuß.",None,None],
 ["arg","C1","aus der Luft gegriffen sein","keine Grundlage haben (≈ haltlos)","to be pulled out of thin air","Die Zahlen in dem Bericht sind aus der Luft gegriffen.",None,None],
 ["arg","C1","ins Gewicht fallen","wichtig sein, Bedeutung haben (≈ ausschlaggebend)","to carry weight, to matter","Die Mehrkosten fallen kaum ins Gewicht.",None,None],
 ["arg","C1","einen Einwand erheben","etwas dagegen vorbringen","to raise an objection","Der Betriebsrat erhob Einwände gegen den Plan.",None,None],
 ["arg","C1","unter dem Strich","alles zusammengerechnet; im Ergebnis (≈ Fazit)","all things considered, the bottom line","Unter dem Strich bleibt wenig Gewinn.",None,None],
 ["arg","C1","etwas auf den Punkt bringen","kurz und treffend sagen","to get to the heart of the matter","Sie hat das Problem auf den Punkt gebracht.",None,None],
 ["arg","C1","den Nagel auf den Kopf treffen","genau das Richtige sagen (≈ treffend)","to hit the nail on the head","Mit dieser Analyse hast du den Nagel auf den Kopf getroffen.",None,None],
 ["arg","B2","das Pferd von hinten aufzäumen","eine Sache falsch herum anfangen","to put the cart before the horse","Erst bauen und dann planen? Das heißt, das Pferd von hinten aufzäumen.",None,None],
]
assert len(R) == 50 and all(sum(1 for r in R if r[0] == k) == 10 for k, _ in T)
import json
data = "const RWT=" + json.dumps([[k, n] for k, n in T], ensure_ascii=False) + ";\n" + \
       "/* Redewendungen (Steuart, 6 Nov): [Thema, Stufe, Wendung, Erklärung, English, Beispielsatz, Herkunft, [Link, Quelle]]. Herkunft nur mit geprüfter Quelle. Wording is ours; to be checked by a native speaker. */\n" + \
       "const RW=" + json.dumps(R, ensure_ascii=False, indent=0).replace("\n", "") + ";\n" + r'''
const RS={f:"Alle"};
function rwRow(r,i){const has=!!r[6];
  return '<div class="rwi"><span class="rwt"><b class="rwp">'+esc(r[2])+'</b><span class="rwl">'+r[1]+'</span></span><span class="rwd">'+esc(r[3])+'</span>'+
  '<button class="rwb" type="button" aria-expanded="false" aria-controls="rwe'+i+'">'+(has?'EN · Herkunft':'EN')+'</button>'+
  '<span class="rwe" id="rwe'+i+'" hidden>'+esc(r[4])+'<i>'+esc(r[5])+'</i>'+(has?'<span class="rwo">'+esc(r[6])+(r[7]?' <a class="wk" href="'+r[7][0]+'" target="_blank" rel="noopener" aria-label="Mehr bei '+r[7][1]+'" title="'+r[7][1]+'">mehr ↗</a>':'')+'</span>':'')+'</span></div>';}
function rwHTML(){const items=[];
  RWT.forEach(([k,n])=>{if(RS.f!=="Alle"&&RS.f!==k)return;if(RS.f==="Alle")items.push('<h4 class="qsec">'+esc(n)+'</h4>');
    items.push('<div class="rwlist">'+RW.map((r,i)=>r[0]===k?rwRow(r,i):"").join("")+'</div>');});
  return '<div class="tc df"><h3>Redewendungen</h3><div class="wchips qchips" id="rchips">'+[["Alle","Alle"]].concat(RWT).map(([k,n])=>'<button data-f="'+k+'" aria-pressed="'+(RS.f===k)+'">'+esc(k==="Alle"?"Alle":n.split(" ")[0])+'</button>').join("")+'</div>'+items.join("")+
   '<p class="tline">Stufe rechts: B1 bis C1. „EN“ zeigt Englisch und einen Beispielsatz. Eine Herkunft steht nur da, wo ich sie in Duden, DWDS oder Wikipedia gefunden habe. Erst die Wendung selbst benutzen, dann nachsehen.</p></div>';}
function renderRede(){const P=$("p-rede");P.innerHTML=rwHTML();
  P.querySelectorAll("#rchips button").forEach(b=>b.onclick=()=>{RS.f=b.dataset.f;P.dataset.more="";renderRede();});
  P.querySelectorAll("button.rwb").forEach(b=>b.onclick=()=>{const e=document.getElementById(b.getAttribute("aria-controls")),o=b.getAttribute("aria-expanded")==="true";b.setAttribute("aria-expanded",o?"false":"true");e.hidden=o;});}
'''
s = s.replace("@@RWDATA@@\n", data, 1)

# 3. section element, SECS, render call
s = s.replace('<section class="hp" id="p-quotes"></section>', '<section class="hp" id="p-quotes"></section>\n      <section class="hp" id="p-rede"></section>', 1)
old = '["quotes","Zitate"],["hist","Geschichte"]'
assert old in s
s = s.replace(old, '["quotes","Zitate"],["rede","Redewendungen"],["hist","Geschichte"]', 1)
s = s.replace("\nrenderQuotes();\n", "\nrenderQuotes();renderRede();\n", 1)
assert "renderRede();" in s

# 4. the last left bar has no right-hand partner
oldc = "((ROWS-1-(i>>1))+(i%2?0:1))*HB"
assert oldc in s
s = s.replace(oldc, "((ROWS-1-(i>>1))+(i%2?0:(i+1<SECS.length?1:0)))*HB", 1)

# 5. CSS: background, origin note, link button, pin colours
# #p-rede stays white like Zitate: the theme chips (grey) then show as boxes with white gaps (6 Nov, Steuart)
s = s.replace(".hp .rwi .rwe i{display:block;margin-top:3px;font-style:italic}",
  ".hp .rwi .rwe i{display:block;margin-top:3px;font-style:italic}\n.hp .rwi .rwo{display:block;margin-top:6px;padding-top:6px;border-top:1px dotted #b9bbb4;font-size:14px;color:#3a3c37}\n.hp .rwi a.wk{display:inline-block;padding:1px 8px 2px;font-size:12px;font-weight:700;letter-spacing:.04em;color:#1a5fd0;background:#dfe9fa;text-decoration:none;vertical-align:1px}\n.hp .rwlist+.qsec{margin-top:14px}", 1)
s = s.replace(".tp .pin:nth-of-type(6){--c1:#3a3c37;--c2:#ffd400}", ".tp .pin:nth-of-type(6){--c1:#3a3c37;--c2:#ffd400}.tp .pin:nth-of-type(7){--c1:#ffd400;--c2:#e30613}", 1)

# 6. title page: new pin (Weimar, 11.33 E / 50.98 N on the map: x = 612 + 63.65 (lon-13.40), y = 268 + 100 (52.52-lat)), renumber the later pins
pins = re.findall(r'<button class="pin[^>]*>.*?</button>', s, re.S)
assert len(pins) == 6
hist, sets = pins[4], pins[5]
newhist = hist.replace('style="--k:4"', 'style="--k:5"').replace("[05]", "[06]").replace("<b>05</b>", "<b>06</b>")
newsets = sets.replace('style="--k:5"', 'style="--k:6"').replace("[06]", "[07]").replace("<b>06</b>", "<b>07</b>")
newrede = '<button class="pin r" data-k="rede" data-x="480.2" data-y="422.0" data-row="0.42" style="--k:4" aria-label="Redewendungen [05] – Weimar"><b>05</b><span>Redewendungen</span></button>'
s = s.replace(hist, newrede + newhist, 1).replace(sets, newsets, 1)

s = s.replace('const CAPATOM=".hi,.qt,a,', 'const CAPATOM=".hi,.qt,.rwi,a,', 1)  # a row of idioms is never cut by the section cap

m = re.search(r'name="app-version" content="([^"]*)"', s)
s = s.replace(m.group(0), 'name="app-version" content="2026-11-06z"', 1)
open(p, "w", encoding="utf-8").write(s)
print("ok; version", m.group(1), "-> 2026-11-06z")
