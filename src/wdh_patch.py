p='index.html';s=open(p,encoding='utf8').read()
a='$("bd").textContent="Dein Fehler · "+$("bd").textContent'
assert s.count(a)==1
s=s.replace(a,'$("bd").textContent="↻ Wiederholung · "+$("bd").textContent')
s=s.replace('<meta name="app-version" content="2026-11-17o">','<meta name="app-version" content="2026-11-17p">')
open(p,'w',encoding='utf8').write(s)
