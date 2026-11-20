import sys,re
app,path=sys.argv[1],sys.argv[2]
COMMON='html{-webkit-text-size-adjust:100%;text-size-adjust:100%}\n:root{--red:#d1000f}\n'
CSS={
'doch':COMMON+'''a.wk::before{content:"";position:absolute;left:-4px;right:-4px;top:-8px;bottom:-8px}
button.markb::before,.tls button::before{content:"";position:absolute;left:0;right:0;top:-7px;bottom:-7px}
#hscroll>.hb.stt[data-i="1"]::before{content:"";position:absolute;left:0;right:0;top:1px;height:1px;background:repeating-linear-gradient(to right,#b8b8b8 0 1px,transparent 1px 3px);pointer-events:none}
.gl{background:#fff!important}
''',
'passage':COMMON+'''.wsw::before,.ilink::before,.tls button::before,.tipbar button::before{content:"";position:absolute;left:-4px;right:-4px;top:-9px;bottom:-9px}
.tlar::after{content:"";position:absolute;inset:-9px}
''',
'phone':COMMON+'''.cvb::before{content:"";position:absolute;left:0;right:0;top:-7px;bottom:-7px}
.wsw::after{content:"";position:absolute;left:-4px;right:-4px;top:-10px;bottom:-10px}
'''}[app]
s=open(path).read()
if 'id="safe-ui"' in s: print('already');sys.exit()
s=s.replace('</head>','<style id="safe-ui">\n/* safe-ui: unsichtbare Verbesserungen (Tippflaechen, Textgroesse, Kontrast) */\n'+CSS+'</style>\n</head>',1)
open(path,'w').write(s)
print('patched',app)
