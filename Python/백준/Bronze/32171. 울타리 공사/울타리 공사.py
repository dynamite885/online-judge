f=max
x=y=X=Y=-10
for i in[*open(0)][1:]:a,b,c,d=map(int,i.split());x,y,X,Y=f(x,-a),f(y,-b),f(X,c),f(Y,d);print(X+x+Y+y<<1)