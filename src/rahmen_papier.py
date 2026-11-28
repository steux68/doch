# Papier hinter dem Goldrahmen exakt in der Form der Rahmenöffnung (statt Rechteck) -> keine weißen Lücken
import numpy as np
from PIL import Image
from scipy import ndimage as ndi
im=Image.open('img/rahmen-gold.webp').convert('RGBA');a=np.array(im)[:,:,3]
op=a<60
lab,n=ndi.label(op);outer=set(lab[0,:])|set(lab[-1,:])|set(lab[:,0])|set(lab[:,-1]);outer.discard(0)
inner=op&~np.isin(lab,list(outer))
# nur die große Öffnung behalten
l2,n2=ndi.label(inner);sz=ndi.sum(inner,l2,range(1,n2+1));inner=l2==(1+int(np.argmax(sz)))
inner=ndi.binary_dilation(inner,iterations=4)   # etwas unter den Rahmen schieben
f=ndi.gaussian_filter(inner.astype(float),9)     # weicher Rand für Innenschatten
sh=np.clip(1-f*1.0,0,1)**1.6*0.30
base=np.array([251,247,234],float)
rgb=base[None,None,:]*(1-sh[:,:,None])
rgba=np.dstack([rgb,ndi.gaussian_filter(inner.astype(float),.8)*255]).clip(0,255).astype(np.uint8)
out=Image.fromarray(rgba,'RGBA').resize((350,528),Image.LANCZOS)
out.save('img/rahmen-papier.webp',quality=82,method=6);print(out.size)
