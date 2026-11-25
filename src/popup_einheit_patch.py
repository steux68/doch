# Popups auf die Masse der PASSAGE-Popups (Anatomie): Kopfzeile, Schliessen, Seitenrand, Titel 16 px, Text 14 px. 25.11.2026
import re,sys
s=open('index.html',encoding='utf-8').read()
if 'popup-einheit-css' in s: sys.exit('schon angewendet')
CSS='''<style id="popup-einheit-css">
.tlpop:not(.full) .tltop{padding:4px 4px 3px;min-height:0}
.tlpop .tlx{padding:4px;margin:-4px}
.tlpop .tlx svg{width:22px;height:22px}
.tlpop:not(.full) .tlcard .tlbody{padding-left:4px;padding-right:4px}
.tlpop .tlar svg{width:22px;height:22px}
#pt,#theo:has(#ltx) .tc>h3,#theo:has(#wprompt) .tc>h3{font-size:16px!important;line-height:1.15!important}
#pb p:not([class]){font-size:14px!important;line-height:1.4!important}
.qv2 .qq,#qpop .tlbody p{font-size:14px}
</style>
'''
i=s.rindex('</head>'); s=s[:i]+CSS+s[i:]
s=re.sub(r'(name="app-version" content=")[^"]*"',r'\g<1>2026-11-25a"',s,count=1)
open('index.html','w',encoding='utf-8').write(s)
