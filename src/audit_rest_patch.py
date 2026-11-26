"""Audit Kleinkram (DOCH/PASSAGE): sichtbarer Tastatur-Fokus; DOCH Theorie ohne Leerblock.  Aufruf: audit_rest_patch.py index.html VERSION [--doch]"""
import re,sys
p,V=sys.argv[1],sys.argv[2]; s=open(p,encoding='utf8').read()
css='<style id="audit-rest">:focus-visible{outline:2px solid #1a1a1a;outline-offset:2px}'
if '--doch' in sys.argv: css+='.app[data-mode="theo"] #stagew{display:none}'
css+='</style>'
s=re.sub(r'<style id="audit-rest">.*?</style>','',s,flags=re.S)
s=s.rstrip('\n')+'\n'+css+'\n'
s=re.sub(r'(name="app-version" content=")[^"]*"',r'\g<1>%s"'%V,s,1)
open(p,'w',encoding='utf8').write(s); print('ok')
