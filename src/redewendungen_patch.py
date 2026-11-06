#!/usr/bin/env python3
"""Redewendungen block (Steuart, 6 Nov 2026): two lines per idiom (German phrase + short German explanation),
an "EN" button opens the English and a German example sentence. Block sits under the quotes (section Zitate).
Run from the repo root: python3 src/redewendungen_patch.py"""
import re, sys
p = "index.html"
s = open(p, encoding="utf-8").read()
if "const RW=[" in s:
    sys.exit("already patched")

CSS = """
/* Redewendungen (6 Nov): grey/white rows, German first, English behind a small EN button */
.rwlist{display:flex;flex-direction:column}
.hp .rwi{padding:9px 10px 10px;background:#fff;font-size:16px;line-height:1.3}
.hp .rwi:nth-child(odd){background:#f4f4f2}
.hp .rwi .rwt{display:flex;align-items:baseline;justify-content:space-between;gap:8px}
.hp .rwi .rwp{font-weight:700;overflow-wrap:anywhere}
.hp .rwi .rwl{flex:none;font-size:11px;font-weight:700;letter-spacing:.06em;color:#3a3c37}
.hp .rwi .rwd{display:block;margin-top:2px;overflow-wrap:anywhere;hyphens:auto}
.hp .rwi button.rwb{margin:6px 0 0;padding:1px 8px 2px;border:0;border-radius:0;font:inherit;font-size:12px;font-weight:700;letter-spacing:.04em;color:#1a5fd0;background:#dfe9fa;cursor:pointer}
.hp .rwi button.rwb[aria-expanded="true"]{color:#fff;background:#1a5fd0}
.hp .rwi .rwe{display:block;margin-top:6px;padding-top:6px;border-top:1px dotted #b9bbb4;font-size:15px;overflow-wrap:anywhere}
.hp .rwi .rwe[hidden]{display:none}
.hp .rwi .rwe i{display:block;margin-top:3px;font-style:italic}
"""
s = s.replace("\n.hlist{display:flex;flex-direction:column}", CSS + "\n.hlist{display:flex;flex-direction:column}", 1)

DATA = r'''
/* ---------- Redewendungen: [Stufe, Wendung, Erklärung auf Deutsch, English, Beispielsatz] (own wording, to be checked by a native speaker) ---------- */
const RW=[
 ["B1","auf dem Holzweg sein","sich irren; eine falsche Richtung verfolgen","to be barking up the wrong tree","Wenn du glaubst, das klappt ohne Übung, bist du auf dem Holzweg."],
 ["B1","im Eimer sein","kaputt oder misslungen sein (umgangssprachlich)","to be ruined, down the drain (colloquial)","Der Urlaub ist im Eimer – mein Flug wurde gestrichen."],
 ["B1","in der Klemme sitzen","in einer schwierigen Lage sein","to be in a tight spot","Ich sitze in der Klemme: Die Miete ist fällig, aber das Gehalt kommt erst nächste Woche."],
 ["B1","auf Zack sein","aufmerksam sein und schnell reagieren","to be on the ball","Um acht Uhr morgens ist er schon richtig auf Zack."],
 ["B1","am Ball bleiben","dranbleiben und nicht aufgeben","to keep at it","Bleib am Ball, dann schaffst du die Prüfung."],
 ["B1","ein Herz und eine Seele sein","sich außerordentlich gut verstehen","to be inseparable, as thick as thieves","Die beiden Schwestern sind ein Herz und eine Seele."],
 ["B1","auf einer Wellenlänge sein","ähnlich denken und sich gut verstehen","to be on the same wavelength","Mit meiner Chefin bin ich völlig auf einer Wellenlänge."],
 ["B1","aus dem Häuschen sein","vor Freude oder Aufregung ganz aufgeregt sein","to be beside oneself with excitement","Die Kinder waren aus dem Häuschen, als der erste Schnee fiel."],
 ["B1","im siebten Himmel sein","überglücklich sein","to be on cloud nine","Seit der Hochzeit ist sie im siebten Himmel."],
 ["B1","mit den Nerven am Ende sein","psychisch völlig erschöpft sein","to be at the end of one’s tether","Nach drei Wochen Lärm auf der Baustelle bin ich mit den Nerven am Ende."],
 ["B2","außer sich sein","vor Wut oder Aufregung die Beherrschung verlieren","to be beside oneself","Er war außer sich vor Zorn, als er die Rechnung sah."],
 ["B2","in der Bredouille sein","in einer unangenehmen Lage sein","to be in a pickle","Ohne Ersatzteil sind wir ganz schön in der Bredouille."],
 ["B2","mit seinem Latein am Ende sein","nicht mehr weiterwissen","to be at one’s wits’ end","Der Techniker war mit seinem Latein am Ende."],
 ["B2","auf Kriegsfuß stehen","mit jemandem oder etwas Schwierigkeiten haben","to be at odds with, to be on bad terms","Mit der Rechtschreibung stehe ich auf Kriegsfuß."],
 ["B2","mit jemandem im Reinen sein","keinen ungelösten Streit mit jemandem haben","to be at peace with someone","Nach dem Gespräch war ich mit ihm wieder im Reinen."],
 ["B2","im Begriff sein, etwas zu tun","kurz davor sein, etwas zu tun","to be about to do something","Ich war gerade im Begriff zu gehen, da klingelte das Telefon."],
 ["B2","im Gespräch sein","als Möglichkeit erwogen werden","to be under consideration","Ein neuer Standort ist im Gespräch."],
 ["B2","auf der Kippe stehen","unsicher sein, ob etwas gut oder schlecht ausgeht","to hang in the balance","Das Projekt steht auf der Kippe."],
 ["C1","außer Frage stehen","nicht bezweifelt werden können","to be beyond question","Dass wir handeln müssen, steht außer Frage."],
 ["C1","zur Debatte stehen","gerade diskutiert oder entschieden werden","to be up for debate","Zur Debatte steht, ob die Frist verlängert wird."],
 ["C1","Hand und Fuß haben","gut durchdacht und überzeugend sein (≈ stichhaltig)","to hold water, to be well thought out","Dein Vorschlag hat Hand und Fuß."],
 ["C1","aus der Luft gegriffen sein","keine Grundlage haben (≈ haltlos)","to be pulled out of thin air","Die Zahlen in dem Bericht sind aus der Luft gegriffen."],
 ["C1","ins Gewicht fallen","wichtig sein, Bedeutung haben (≈ ausschlaggebend)","to carry weight, to matter","Die Mehrkosten fallen kaum ins Gewicht."],
 ["C1","einen Einwand erheben","etwas dagegen vorbringen","to raise an objection","Der Betriebsrat erhob Einwände gegen den Plan."],
 ["C1","unter dem Strich","alles zusammengerechnet; im Ergebnis (≈ Fazit)","all things considered, the bottom line","Unter dem Strich bleibt wenig Gewinn."],
 ["C1","etwas auf den Punkt bringen","kurz und treffend sagen","to get to the heart of the matter","Sie hat das Problem auf den Punkt gebracht."],
 ["C1","den Nagel auf den Kopf treffen","genau das Richtige sagen (≈ treffend)","to hit the nail on the head","Mit dieser Analyse hast du den Nagel auf den Kopf getroffen."]
];
function rwHTML(){return '<div class="tc df"><h3>Redewendungen</h3><div class="rwlist">'+RW.map((r,i)=>
  '<div class="rwi"><span class="rwt"><b class="rwp">'+esc(r[1])+'</b><span class="rwl">'+r[0]+'</span></span><span class="rwd">'+esc(r[2])+'</span>'+
  '<button class="rwb" type="button" aria-expanded="false" aria-controls="rwe'+i+'">EN</button>'+
  '<span class="rwe" id="rwe'+i+'" hidden>'+esc(r[3])+'<i>'+esc(r[4])+'</i></span></div>').join("")+'</div>'+
  '<p class="tline">Stufe rechts: B1 bis C1. „EN“ zeigt Englisch und einen Beispielsatz. Erst die Wendung selbst benutzen, dann nachsehen.</p></div>';}
function rwBind(root){root.querySelectorAll("button.rwb").forEach(b=>b.onclick=()=>{const e=document.getElementById(b.getAttribute("aria-controls")),o=b.getAttribute("aria-expanded")==="true";b.setAttribute("aria-expanded",o?"false":"true");e.hidden=o;});}
'''
anchor = "function renderQuotes(){"
assert anchor in s
s = s.replace(anchor, DATA.lstrip("\n") + anchor, 1)

old = """$("p-quotes").innerHTML='<div class="tc df"><h3>Über die deutsche Sprache</h3>'+quotesHTML()+'</div>';loadPics($("p-quotes"));"""
new = """$("p-quotes").innerHTML='<div class="tc df"><h3>Über die deutsche Sprache</h3>'+quotesHTML()+'</div>'+rwHTML();loadPics($("p-quotes"));rwBind($("p-quotes"));"""
assert old in s
s = s.replace(old, new, 1)

m = re.search(r'name="app-version" content="([^"]*)"', s)
s = s.replace(m.group(0), 'name="app-version" content="2026-11-06y"', 1)
open(p, "w", encoding="utf-8").write(s)
print("ok; version", m.group(1), "->", "2026-11-06y")
