# DOCH!-Kopflogo, Fassung 3: DOCH etwas kleiner, Schrift rechts etwas groesser, D mittig im "!", Umlaut-Punkte im O (DOCH + DÖCH = D-Ö-CH, Deutschland-Österreich-Schweiz).
import re
P="deutsch/index.html"
s=open(P,encoding="utf-8").read()
FS=51      # DOCH
T=24       # Deutsche / Grammatik
OX,OY,DR,DG=48.5,30.5,3.1,4.7   # Mitte des O-Innenraums, Punktradius, halber Punktabstand
SX=0    # Mitte des Strichs
GX=28.0    # x des "u"
svg=('<h1 class="logo" role="img" aria-label="DOCH! Deutsche Grammatik">'
f'<svg viewBox="0 0 289 62" aria-hidden="true">'
f'<text class="lb" x="0" y="52" font-size="{FS}">DOCH</text>'
f'<circle class="lu" cx="{OX-DG}" cy="{OY}" r="{DR}"/><circle class="lu" cx="{OX+DG}" cy="{OY}" r="{DR}"/>'
'<g transform="translate(150 0)"><path class="lx" d="M-12 2h24a3.4 3.4 0 0 1 3.4 3.8l-2.8 29.6a3.4 3.4 0 0 1-3.4 3H-4.6a3.4 3.4 0 0 1-3.4-3L-14.8 5.8A3.4 3.4 0 0 1-12 2z" transform="translate(0 0)"/>'
'<circle class="lx" cx="0" cy="48" r="8.6"/>'
f'<text class="ld" x="0" y="25" font-size="{T-2}" text-anchor="middle">D</text>'
f'<text class="ls" x="18.4" y="25" font-size="{T}">eutsche</text>'
f'<text class="ls" x="{GX}" y="49" font-size="{T}">Grammatik</text></g>'
'</svg></h1>')
s=re.sub(r'<h1 class="logo".*?</h1>(?=<button class="markb on")',lambda m:svg,s,count=1,flags=re.S)
if '.lu{' not in s:
    s=s.replace('.home h1.logo .lx{fill:var(--red)}','.home h1.logo .lx{fill:var(--red)}.home h1.logo .lu{fill:var(--red);stroke:#fff;stroke-width:1.5}',1)
s=re.sub(r'(<meta name="app-version" content=")[^"]*(")',lambda m:m.group(1)+'2026-10-31p'+m.group(2),s,count=1)
open(P,"w",encoding="utf-8").write(s)
