#!/usr/bin/env python3
"""Theorie in drei Stufen, zweite Runde (2026-11-21p): Genitiv, Plural, Komparation, Pronomen, Reflexiv, Praeteritum & Futur, Zeitformen, Praesens, Zeitangaben. Eigene Formulierung. Idempotent."""
import os,re
root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
p=os.path.join(root,"index.html");s=open(p,encoding="utf-8").read()
if "TH3B-MARK" in s: print("already patched");raise SystemExit
def rows(L): return '<div class="rows">'+''.join('<div><span>%s</span><span>%s</span></div>'%(a,b) for a,b in L)+'</div>'
def three(rule,tl1,steps,exc,lv):
    a,b,c=lv
    return ('<div class="tc df"><h3>1 · Die einfache Regel <small>%s</small></h3><p class="memo">%s</p><p class="tline">%s</p></div>\n'%(a,rule,tl1)+
            '<div class="tc df"><h3>2 · Schritt für Schritt <small>%s</small></h3>%s</div>\n'%(b,rows(steps))+
            '<div class="tc df"><h3>3 · Ausnahmen &amp; mehr <small>%s</small></h3>%s</div>\n'%(c,rows(exc)))
T={}
T['gen']=three('The Genitiv shows who owns something. The article becomes <b>des</b> (masculine, neuter) or <b>der</b> (feminine, plural). Masculine and neuter nouns add <b>-s</b> or <b>-es</b>.','das Haus des Mannes · die Tür der Wohnung',
 [("1 Owner","der Mann → masculine"),("2 Article","des"),("3 Noun ending","Mannes (add -es)"),("4 Feminine or plural","der, and the noun stays: die Tür <b>der</b> Wohnung")],
 [("Names","Annas Pferd · no apostrophe"),("n-Deklination","des Studenten, des Kollegen"),("Adjective","des neu<b>en</b> Plans"),("Spoken","das Auto von meinem Bruder (von + Dativ)"),("With prepositions","wegen des Regens · trotz des Wetters")],('B1','B1','B2–C1'))
T['plural']=three('The plural cannot be predicted from the singular, so learn it <b>with</b> the noun. The plural article is always <b>die</b>.','das Kind – die Kinder',
 [("1 Ending -ung, -heit, -keit, -schaft","add -en: die Zeitung → die Zeitungen"),("2 Ending -in","-innen: die Ärztin → die Ärztinnen"),("3 Feminine -e","add -n: die Lampe → die Lampen"),("4 Not sure","learn singular and plural together: der Hund, die Hunde")],
 [("Foreign words","-s: das Auto → die Autos"),("Umlaut","der Stuhl → die Stühle · das Haus → die Häuser"),("No change","der Lehrer → die Lehrer"),("n-Deklination","der Student → die Studenten"),("Only plural","die Eltern · die Leute"),("Dativ plural","an the end: mit den Kinder<b>n</b>")],('A2','A1–A2','B1–C1'))
T['komp']=three('Add <b>-er</b> for the comparative and <b>am … -sten</b> for the superlative. Compare equal things with <b>wie</b>, unequal things with <b>als</b>.','schnell · schneller · am schnellsten',
 [("1 Equal","Ich bin so schnell <b>wie</b> du."),("2 Higher","Ich bin schneller <b>als</b> du."),("3 Highest","Ich bin <b>am</b> schnellsten."),("4 Before a noun","der schnellste Läufer (with an adjective ending)")],
 [("Umlaut","alt → älter → am ältesten · groß → größer → am größten"),("Irregular","gut → besser → am besten · viel → mehr → am meisten · gern → lieber → am liebsten"),("-d, -t, -s, -z, -ß","with -e-: am ältesten, am heißesten, am kürzesten"),("je … desto","Je mehr ich übe, desto besser spreche ich."),("Elativ","höchst interessant · bestens informiert")],('A2','A2','B1–C1'))
T['pron']=three('Pronouns replace nouns and change with the case: <b>ich – mich – mir</b>. Ask the verb which case it needs.','Ich sehe ihn. · Ich helfe ihm.',
 [("1 The verb","geben → who gets what?"),("2 The questions","Wem? → Dativ · Was? → Akkusativ"),("3 The pronouns","er → ihm (Dativ) · das Buch → es (Akkusativ)"),("4 Write it","Ich gebe <b>es ihm</b>.")],
 [("sie","she, they, or formal Sie: check the verb ending"),("es","can be empty: Es regnet. Es gibt einen Park."),("Order","pronoun Akkusativ before pronoun Dativ: Ich gebe es ihm."),("uns · euch","the same in Akkusativ and Dativ"),("das","das is used for a whole idea: Das stimmt.")],('A1','A1–A2','B1–C1'))
T['refl']=three('A reflexive pronoun points back to the subject: <b>Ich wasche mich.</b> Only the third person has its own form: <b>sich</b>.','ich mich · du dich · er sich · wir uns · ihr euch · sie sich',
 [("1 Subject","ich"),("2 Pronoun","mich (Akkusativ)"),("3 Another object?","then Dativ: Ich wasche <b>mir</b> die Hände."),("4 Third person","Sie freut <b>sich</b>.")],
 [("With preposition","sich freuen auf (coming) · über (already here)"),("Each other","Wir sehen uns morgen. = we see each other"),("selbst","Er hilft sich selbst. = he helps himself, for emphasis"),("sich lassen","Das lässt sich lösen. = can be solved"),("Nebensatz","…, weil ich mich freue.")],('A2','A2','B1–C1'))
T['praet']=three('The Präteritum is the written past. Regular verbs add <b>-te</b>, strong verbs change their vowel. In speech use the Perfekt, except for <b>war, hatte, konnte, musste</b>.','Ich lernte. · Ich ging. · Ich war müde.',
 [("1 Stem","lern-"),("2 Add -te","lernte"),("3 Endings","ich lernte · du lerntest · wir lernten"),("4 Strong verbs","gehen → ging: no -te, a vowel change")],
 [("Mixed verbs","denken → dachte · bringen → brachte · wissen → wusste"),("Modal verbs","musste, konnte, wollte, durfte, sollte (no Umlaut)"),("Plusquamperfekt","hatte / war + Partizip II: Ich hatte gelernt."),("Futur","werde + Infinitiv: Er wird wohl krank sein. = I suppose he is ill")],('B1','A2–B1','B1–C1'))
T['perf']=three('The Perfekt is the spoken past: <b>haben</b> or <b>sein</b> + Partizip II at the end of the sentence.','Ich habe gelernt. · Ich bin gegangen.',
 [("1 Auxiliary","haben (most verbs) · sein (movement, change of state)"),("2 Partizip II","ge-…-t (machen → gemacht) · ge-…-en (schreiben → geschrieben)"),("3 Position","Ich habe gestern gelernt.")],
 [("sein","bleiben, sein, passieren: ist geblieben, ist gewesen, ist passiert"),("No ge-","studieren → studiert · verstehen → verstanden · besuchen → besucht"),("Separable","aufstehen → aufgestanden · anrufen → angerufen"),("Austria","ich bin gesessen, ich bin gestanden (south of Germany too)"),("With a modal","…, weil er hat arbeiten müssen.")],('A2','A2','B1–C1'))
T['praes']=three('Present tense: verb stem + ending. <b>ich -e · du -st · er -t · wir -en · ihr -t · sie -en</b>. The verb is in second place.','Ich mache. · Du machst. · Heute mache ich Pause.',
 [("1 Infinitive","machen"),("2 Stem","mach-"),("3 Ending","ich mache · du machst · er macht"),("4 Position","Heute <b>mache</b> ich Pause.")],
 [("Vowel change","du gibst, er gibt (e → i) · du fährst, er fährt (a → ä)"),("Stem on -t, -d","du arbeitest, er arbeitet (extra -e-)"),("Stem on -s, -ß, -z","du heißt, du reist"),("sein · haben","ich bin, du bist, er ist · ich habe, du hast, er hat"),("Future","Morgen fahre ich nach Graz. = the present can mean the future")],('A1','A1','A2–B1'))
T['zeit']=three('Use <b>am</b> for days and parts of the day, <b>um</b> for clock times, <b>im</b> for months, seasons and years.','am Montag · um acht Uhr · im Mai',
 [("1 Day or date","am Montag · am 3. Mai"),("2 Clock time","um acht Uhr · um Mitternacht"),("3 Month or season","im Mai · im Winter"),("4 Since or ago","seit drei Jahren (still going) · vor drei Jahren (over)")],
 [("Night","in der Nacht · nachts (not am Nacht)"),("Year","im Jahr 2020 or just 2020"),("From now","in zwei Wochen = two weeks from now"),("Festivals","an Weihnachten · zu Ostern"),("Vague","gegen Abend · um die Mittagszeit")],('A2','A1–A2','B1–C1'))
def const_ins(name,text):
    global s
    a='const %s=`'%name
    assert s.count(a)==1,name
    s=s.replace(a,a+"\n"+text)
const_ins('TH_GEN',T['gen']);const_ins('TH_PRON',T['pron'])
for k in ['plural','komp','refl','praes','zeit','praet','perf']:
    i=s.index('GT.%s='%k);j=s.index('th:`',i)+4
    if s.startswith("${tpxHTML('t')}",j): j=s.index('}',j)+1
    else: assert s[j:j+14]=='<div class="tc',(k,s[j:j+40])
    s=s[:j]+T[k]+s[j:]
s=re.sub(r'<meta name="app-version" content="[^"]+">','<meta name="app-version" content="2026-11-21p">',s,count=1)
s+='\n<!-- TH3B-MARK -->'
open(p,"w",encoding="utf-8").write(s);print("ok")
