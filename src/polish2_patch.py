# DOCH!: Themenkarten buendig, Einstellungen linksbuendig, Footer an Kanten, Zitat-Fotos buendig, Tests-Raster wie ueberall gepunktet. 06.11.2026.
import re, sys
s = open('index.html', encoding='utf-8').read()
if '/* polish2 */' in s:
    print('schon angewendet'); sys.exit(0)
CSS='''
/* polish2 */
.gl{padding:0 0 8px 0!important;gap:6px!important;grid-template-columns:repeat(2,minmax(0,1fr))!important}
#p-sets p.tline{text-align:left!important}
footer.copy.ch{right:18px!important;width:calc(100vw - 36px)!important}
body:has(footer.copy.ch) #toTop{display:none!important}
#toTop{right:18px!important}
.qt,.hp .qt.alt{padding:0!important;grid-template-columns:92px minmax(0,1fr)!important;align-items:start!important;min-height:92px;gap:10px!important}
.qt .pic{width:92px!important;height:92px!important;border:0!important;align-self:start!important}
.qt .qb{padding:8px 8px 8px 0}
.tests{border:0!important;background:var(--df) left top/100% 1px no-repeat,var(--dfv) left top/1px 100% no-repeat!important}
.tests .tst{border:0!important;background:var(--df) left bottom/100% 1px no-repeat,var(--dfv) right top/1px 100% no-repeat,#f6f6f6!important}
.tests .tst[data-l="mix"],.tests .tst:active{background:var(--df) left bottom/100% 1px no-repeat,var(--dfv) right top/1px 100% no-repeat,#cdff3e!important}
'''
i=s.rindex('</style>'); s=s[:i]+CSS+s[i:]
s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-11-06u'+m.group(3),s,count=1)
open('index.html','w',encoding='utf-8').write(s); print('ok')
