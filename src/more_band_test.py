# Testkopie band5.html: "mehr"-Zeilen (.mrow) als Leiste in der blassen Farbe des Abschnitts, mit rundem pulsierendem Chevron-Knopf. index.html bleibt unberuehrt. 27.11.2026
s=open('index.html',encoding='utf-8').read()
CH_D='<path d="M-3.6 -1.4L0 2.2L3.6 -1.4"/>'; CH_U='<path d="M-3.6 1.4L0 -2.2L3.6 1.4"/>'
a='<path d="M0 -4.2V4.2"/><path d="M-4.2 0H4.2"/></svg>\';'
assert s.count(a)==1; s=s.replace(a,CH_D+'</svg>\';')
b='<circle class="c" r="8"/><path d="M-4.2 0H4.2"/></svg>\';'
assert s.count(b)==1; s=s.replace(b,'<circle class="c" r="8"/>'+CH_U+'</svg>\';')
CSS='''<style id="bandtest">
/* Leiste statt kleinem (+): ganze Breite, blasse Farbe des Abschnitts, Text mittig, Knopf links */
.mrow.capm,.mrow#qmore{position:relative;justify-content:center;flex-wrap:wrap;height:auto;min-height:40px;margin:8px 0 14px;padding:7px 44px;text-align:center;text-transform:uppercase;letter-spacing:.14em;font-size:12px;font-weight:700;color:#222;
 background:var(--df) left top/100% 1px no-repeat,var(--bt,#f2f2f0)!important;margin:8px 0 14px!important;align-items:center}
html body .mrow.capm,html body .mrow.capm.nl,html body .mrow.capm.nl:is(.p-links,.p-hist,.p-home){background:var(--df) left top/100% 1px no-repeat,var(--bt,#f2f2f0)!important}
.mrow.capm .cvt,.mrow#qmore .cvt{font-weight:700;font-size:12px}
.mrow.capm b,.mrow#qmore b{margin-left:0;font-size:12px;color:#222}
.mrow.capm small,.mrow#qmore small{flex:0 0 100%;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;font-size:12px!important;margin:2px 0 0;text-transform:none;letter-spacing:.02em;font-weight:400;font-size:13px;color:#555}
.mrow.capm .pl,.mrow#qmore .pl{position:absolute;left:12px;top:10px}
.mrow.p-test,.mrow.p-rede{--bt:#f8f0d2}.mrow.p-links,.mrow.p-quotes,.mrow.p-hist,.mrow.p-study,.mrow#qmore{--bt:#dfe9fb}
</style>'''
i=s.rindex('</head>') if '</head>' in s else s.rindex('</style>')+8
s=s[:i]+CSS+s[i:]
s=s.replace('<title>','<title>[Test Leiste] ',1)
open('band5.html','w',encoding='utf-8').write(s); print('ok')
