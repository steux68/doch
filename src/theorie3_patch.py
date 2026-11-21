#!/usr/bin/env python3
"""Theorie in drei Stufen fuer Artikel, Konnektoren, Relativsaetze, Verben mit Praepositionen, Konjunktiv II, Passiv (2026-11-21o). Eigene Formulierung. Idempotent."""
import os,re
root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
p=os.path.join(root,"index.html");s=open(p,encoding="utf-8").read()
if "TH3-MARK" in s: print("already patched");raise SystemExit
def rows(L): return '<div class="rows">'+''.join('<div><span>%s</span><span>%s</span></div>'%(a,b) for a,b in L)+'</div>'
def three(rule,tl1,steps,tl2,exc,lv):
    a,b,c=lv
    return ('<div class="tc df"><h3>1 · Die einfache Regel <small>%s</small></h3><p class="memo">%s</p><p class="tline">%s</p></div>\n'%(a,rule,tl1)+
            '<div class="tc df"><h3>2 · Schritt für Schritt <small>%s</small></h3>%s%s</div>\n'%(b,rows(steps),('<p class="tline">%s</p>'%tl2) if tl2 else '')+
            '<div class="tc df"><h3>3 · Ausnahmen &amp; mehr <small>%s</small></h3>%s</div>\n'%(c,rows(exc)))
T={}
T['art']=three('Every noun has a gender. Learn the noun <b>with</b> its article, as one word. The plural is always <b>die</b>.','der Tisch · die Lampe · das Buch · die Bücher',
 [("1 Ending","-ung, -heit, -keit → die · -chen, -lein → das · -ling, -ismus → der"),("2 Meaning","days, months, seasons → der · metals, colours, young animals → das"),("3 Compound","the last word decides: die Haustür"),("4 Not sure","look it up and learn article + noun as one word")],'',
 [("Two meanings","der See (lake) · die See (sea) · das Steuer (wheel) · die Steuer (tax) · der Tor (fool) · das Tor (gate)"),("Austria","das E-Mail in Austria, die E-Mail in Germany"),("Verb as noun","always das: das Lernen, das Reiten"),("Adjective as noun","der Deutsche · die Deutsche · das Gute")],('A1','A1–A2','B1–C1'))
T['konn']=three('Connectors join clauses. Ask first: where does the verb go? <b>Position 0</b> (und, aber, oder, denn, sondern): normal order. <b>Verb at the end</b> (weil, dass, wenn, obwohl). <b>First place</b> (deshalb, trotzdem, dann): the verb follows at once.','Merkhilfe for position 0: ADUSO',
 [("1 Meaning","reason → weil, denn · contrast → aber, obwohl · result → deshalb"),("2 Position","weil: verb at the end · denn: verb in second place · deshalb: verb right after it"),("3 Write it","Ich bleibe zu Hause, <b>weil</b> ich krank <b>bin</b>. · …, <b>denn</b> ich <b>bin</b> krank. · <b>Deshalb bleibe</b> ich zu Hause.")],'',
 [("aber · sondern","sondern follows a negative: Ich komme nicht heute, sondern morgen."),("obwohl · trotzdem","Obwohl es regnet, gehen wir. · Es regnet. Trotzdem gehen wir."),("weil · da","da usually starts the sentence: Da es regnet, bleiben wir hier."),("wenn · falls","falls is more formal and always means a real possibility."),("gesprochen","You hear „weil ich bin müde“ in speech. Write the verb at the end.")],('A2','A2–B1','B1–C1'))
T['rel']=three('A relative clause describes a noun. It begins with der, die or das. <b>Gender and number</b> come from the noun, the <b>case</b> from the job in the relative clause. The verb goes to the end.','der Mann, der dort wohnt',
 [("1 The noun","die Frau → feminine"),("2 The job","ich helfe ihr → Dativ"),("3 The pronoun","feminine + Dativ → der"),("4 Write it","die Frau, <b>der</b> ich helfe")],'',
 [("Preposition","das Haus, in dem ich wohne · die Firma, für die ich arbeite"),("Dativ plural","die Kinder, denen ich helfe"),("Genitiv","der Kollege, dessen Büro … · die Kollegin, deren Entwurf …"),("was","alles, was ich weiß · nichts, was ich sagen kann"),("Partizip","die gebaute Brücke = die Brücke, die gebaut wurde")],('A2–B1','B1','B2–C1'))
T['vprep']=three('Many verbs come with a fixed preposition. Learn <b>verb + preposition + case</b> as one block.','warten auf den Bus',
 [("1 The block","warten + auf"),("2 The case","with auf, über, für, um, gegen: Akkusativ · with mit, von, nach, zu, bei: Dativ"),("3 Question","Worauf wartest du? (thing) · Auf wen wartest du? (person)"),("4 Answer","Ich warte <b>darauf</b>. · Ich warte <b>auf ihn</b>.")],'',
 [("Dativ with an · auf","teilnehmen an, zweifeln an, bestehen auf (Dativ)"),("Same verb, new meaning","sich freuen auf (coming) · sich freuen über (already here)"),("With dass or zu","Ich freue mich <b>darauf</b>, dich zu sehen."),("halten von","Was hältst du <b>davon</b>? Von takes Dativ.")],('A2','A2–B1','B1–C1'))
T['k2']=three('Konjunktiv II is for wishes, unreal situations and polite requests. Mostly use <b>würde + Infinitiv</b>. With sein, haben and the modal verbs use their own forms: <b>wäre, hätte, könnte</b>.','Wenn ich Zeit hätte, würde ich kommen.',
 [("Wunsch","Ich hätte gern einen Kaffee."),("Unreal","Wenn ich reich wäre, würde ich reisen."),("Höflich","Könnten Sie mir bitte helfen?"),("Vergangenheit","hätte / wäre + Partizip II: Wenn ich Zeit gehabt hätte, wäre ich gekommen.")],'',
 [("Regular verbs","arbeitete looks like the Präteritum, so use würde arbeiten"),("Strong verbs","käme, ginge, wüsste – common in writing"),("Without wenn","Hätte ich Zeit, käme ich mit."),("als ob","Er tut so, als ob er nichts wüsste."),("Modal in the past","Ich hätte kommen können.")],('B1','B1','B2–C1'))
T['pass']=three('The passive puts the action first, not the doer. <b>werden + Partizip II</b>. The Akkusativ object of the active sentence becomes the subject.','Das Auto wird repariert.',
 [("Aktiv","Der Mechaniker repariert das Auto."),("1 Object → subject","das Auto"),("2 werden","wird"),("3 Partizip II at the end","repariert"),("4 Doer (optional)","von + Dativ: Das Auto wird <b>vom Mechaniker</b> repariert.")],'',
 [("Perfekt","Das Haus ist gebaut <b>worden</b>. (not geworden)"),("With a modal","Das Haus muss gebaut werden."),("Dativ stays","Dem Mann wird geholfen."),("Zustand","Die Tür ist geschlossen. = the result, with sein"),("man","Man baut das Haus. = active, doer unnamed")],('B1','B1','B2–C1'))
def ins(anchor,text):
    global s
    assert s.count(anchor)==1,anchor
    s=s.replace(anchor,anchor+text)
ins('const TH_ART=`\n',T['art'])
for k in ['konn','rel','vprep','k2','pass']:
    i=s.index('GT.%s='%k);j=s.index('th:`',i)+4
    assert s[j:j+14]=='<div class="tc',(k,s[j:j+40])
    s=s[:j]+T[k]+s[j:]
s=re.sub(r'<meta name="app-version" content="[^"]+">','<meta name="app-version" content="2026-11-21o">',s,count=1)
s+='\n<!-- TH3-MARK -->'
open(p,"w",encoding="utf-8").write(s);print("ok")
