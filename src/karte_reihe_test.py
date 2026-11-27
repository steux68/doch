#!/usr/bin/env python3
"""Titelkarte: Grammatikwoerter [C] von Reihe .30 auf .86 (unten links, neben Redewendungen [D]); Geschichte [B] von .86 auf .56 (neben Zitate [A]). Reihen: A+B, dann C+D;
damit die Linie von Grammatik [01] sie nicht mehr kreuzt.
Aufruf: python3 src/karte_reihe_test.py [live] [datei]  (ohne live -> karte1.html)"""
import os,sys
LIVE='live' in sys.argv[1:]
root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src=os.path.join(root,'index.html')
s=open(src,encoding='utf-8').read()
A='data-k="gram" data-x="363.5" data-y="389.0" data-row="0.30"'
if A not in s: print('already'); raise SystemExit
s=s.replace(A,'data-k="gram" data-x="363.5" data-y="389.0" data-row="0.86"')
B='data-k="hist" data-x="232.7" data-y="825.0" data-row="0.86"'
assert B in s
s=s.replace(B,'data-k="hist" data-x="232.7" data-y="825.0" data-row="0.56"')
s=s+'<style id="karte-reihe-css">@media (max-width:360px){.pin[data-k="gram"] span{display:inline-block;transform:translateX(18px)}}</style>'
out=os.path.join(root,'index.html' if LIVE else 'karte1.html')
open(out,'w',encoding='utf-8').write(s);print('wrote',out)
