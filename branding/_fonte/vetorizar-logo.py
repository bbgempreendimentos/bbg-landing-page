import sys, numpy as np, potrace
from PIL import Image, ImageFilter
im = Image.open(sys.argv[1]).convert('RGB')
im = im.resize((im.width*4, im.height*4), Image.LANCZOS).filter(ImageFilter.GaussianBlur(2))
a = np.asarray(im).astype(int)
mask = (a[:,:,1] - a[:,:,0]) > 90
# sample colours
px = np.asarray(Image.open(sys.argv[1]).convert('RGB')).reshape(-1,3)
g = px[(px[:,1]-px[:,0])>120]
print('green min/mean/max', g.min(0), g.mean(0).astype(int), g.max(0), file=sys.stderr)
ys,xs=np.where(mask); print('bbox', xs.min()/4, ys.min()/4, xs.max()/4, ys.max()/4, file=sys.stderr)
bm = potrace.Bitmap(~mask)
path = bm.trace(turdsize=20, alphamax=1.0, opticurve=True, opttolerance=0.2)
d=[]
f=lambda p:f"{p.x/4:.2f} {p.y/4:.2f}"
for c in path:
    d.append("M"+f(c.start_point))
    for s in c.segments:
        if s.is_corner: d.append("L"+f(s.c)+" L"+f(s.end_point))
        else: d.append("C"+f(s.c1)+" "+f(s.c2)+" "+f(s.end_point))
    d.append("Z")
print(" ".join(d))
