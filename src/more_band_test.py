# Testkopie band5.html (27.11.2026, v2): "mehr"-Zeilen (.mrow) = schlanke Zeile mit grossem limettengruenem, pulsierendem Pfeil-Kreis;
# darunter dicht der kleine Hinweis. Und in "Staunen": Geschichte vor Redewendungen. index.html bleibt unberuehrt.
s=open('index.html',encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:60],s.count(a)); s=s.replace(a,b)
# Chevron statt Plus / Minus
CH_D='<path d="M-3.8 -1.6L0 2.4L3.8 -1.6"/>'; CH_U='<path d="M-3.8 1.6L0 -2.4L3.8 1.6"/>'
rep('<path d="M0 -4.2V4.2"/><path d="M-4.2 0H4.2"/></svg>\';',CH_D+'</svg>\';')
rep('<circle class="c" r="8"/><path d="M-4.2 0H4.2"/></svg>\';','<circle class="c" r="8"/>'+CH_U+'</svg>\';')
# Text in zwei dichte Zeilen: "MEHR HILFSMITTEL" + kleiner Hinweis
rep("""m.innerHTML=MINUS+'<span class="cvt">weniger</span><b>'+esc(name)+'</b>';""","""m.innerHTML=MINUS+'<span class="mt"><span class="l1"><span class="cvt">weniger</span> <b>'+esc(name)+'</b></span></span>';""")
rep("""m.innerHTML=PLUS+'<span class="cvt">mehr</span><b>'+esc(name)+'</b>'+(hint?'<small>'+esc(hint)+'</small>':'');""","""m.innerHTML=PLUS+'<span class="mt"><span class="l1"><span class="cvt">mehr</span> <b>'+esc(name)+'</b></span>'+(hint?'<small>'+esc(hint)+'</small>':'')+'</span>';""")
rep("""'+PLUS+'<span class="cvt">mehr</span><b>Zitate</b><small>+'+hid+' weitere</small></button>'""","""'+PLUS+'<span class="mt"><span class="l1"><span class="cvt">mehr</span> <b>Zitate</b></span><small>+'+hid+' weitere</small></span></button>'""")
# Reihenfolge Staunen: Zitate, Geschichte, Redewendungen
rep('[["quotes","Zitate"],["rede","Redewendungen"],["hist","Geschichte"],["study","Studieren"]]','[["quotes","Zitate"],["hist","Geschichte"],["rede","Redewendungen"],["study","Studieren"]]')
rep('sec=["quotes","rede","hist"]','sec=["quotes","hist","rede"]')
rep('PN=["p-quotes","p-rede","p-hist"]','PN=["p-quotes","p-hist","p-rede"]')
rep('quotes:["s",0],rede:["s",1],hist:["s",2]},L={quotes:"A",rede:"B",hist:"C"}','quotes:["s",0],hist:["s",1],rede:["s",2]},L={quotes:"A",hist:"B",rede:"C"}')
rep('b=document.querySelectorAll("#hscroll>.hb")[2];\nif(c&&b)','b=document.querySelectorAll("#hscroll>.hb")[1];\nif(c&&b)')
# die Leisten sitzen vor ihrem Abschnitt im DOM: Abschnitt p-hist vor p-rede legen, dann stimmen alle Reihenfolgen (Leisten, Buchstaben A B C)
rep('<section class="hp" id="p-rede"></section>','')
rep('<section class="hp" id="p-hist"></section>','<section class="hp" id="p-hist"></section><section class="hp" id="p-rede"></section>')
CSS='''<style id="bandtest">
/* schlanke "mehr"-Zeile: grosser limettengruener Pfeil-Kreis (pulsiert), dicht daneben Text + kleiner Hinweis */
html body .mrow.capm,html body .mrow#qmore{display:flex;align-items:center;justify-content:flex-start;gap:10px;width:100%;height:auto;min-height:44px;margin:8px 0 12px!important;padding:6px 2px;text-align:left;text-transform:none;
 background:var(--df) left top/100% 1px no-repeat,var(--df) left bottom/100% 1px no-repeat,var(--bg,#fff)!important}
.mrow.p-links,.mrow.p-hist,.mrow.p-home,.mrow#qmore{--bg:#f4f4f2}
.mrow .pl{width:30px!important;height:30px!important}
.mrow .pl .c{fill:#cdff3e!important;stroke:var(--red);stroke-width:1.5}
.mrow .pl path{stroke:var(--red)!important;stroke-width:1.9!important}
.mrow .mt{display:flex;flex-direction:column;min-width:0;line-height:1.2}
.mrow .l1{display:block;white-space:nowrap}
.mrow .cvt{font-size:13px!important;font-weight:400!important;letter-spacing:.08em}
.mrow .mt b{font-size:13px;letter-spacing:.08em;margin-left:0}
.mrow .mt small{display:block;flex:none;margin:1px 0 0;font-size:12px;line-height:1.2;color:var(--muted);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
</style>'''
i=s.rindex('</head>') if '</head>' in s else s.rindex('</style>')+8
s=s[:i]+CSS+s[i:]
s=s.replace('<title>','<title>[Test Leiste] ',1)
open('band5.html','w',encoding='utf-8').write(s); print('ok')
