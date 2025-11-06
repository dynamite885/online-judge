a,b=map(int,input().split())
s=(b>0)-(b<0)
a*=s
x,y=divmod(a,b)
print(x*s,y*s)