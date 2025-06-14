xs,ys,xe,ye,dx,dy=map(int,open(0).read().split())
wx=xs-xe
wy=ys-ye
vv=dx*dx+dy*dy
if vv==0:exit(print(xe,ye))
t=(wx*dx+wy*dy)/vv
if t<0:
    x,y=xe,ye
else:
    x=xe+t*dx
    y=ye+t*dy
print(round(x),round(y))