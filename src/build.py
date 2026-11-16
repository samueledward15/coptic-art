import base64,re,sys
import os
D=os.path.dirname(os.path.abspath(__file__))
T=os.path.join(D,'theme')+'/'
def uri(p): return 'data:image/svg+xml;base64,'+base64.b64encode(open(p,'rb').read()).decode()
h=open(os.path.join(D,'template.html'),encoding='utf-8').read()
m={'PAPYRUS':'papyrus.svg','ORN':'orn.svg','BRAID':'braid-tile.svg','RULE':'rule.svg','LOGO_ANIM':'logo-mark-anim.svg','LOGO_ICON':'logo-icon.svg'}
for k,v in m.items(): h=h.replace('{{%s}}'%k,uri(T+v))
for k in set(re.findall(r'\{\{EL_(\w+)\}\}',h)): h=h.replace('{{EL_%s}}'%k,uri(T+'el/'+k+'.svg'))
h=h.replace('{{IMGS}}',open(os.path.join(D,'imgs.json')).read())
assert '{{' not in h, re.findall(r'\{\{\w+\}\}',h)
open(os.path.join(D,'..','index.html'),'w',encoding='utf-8').write(h); print(len(h))
