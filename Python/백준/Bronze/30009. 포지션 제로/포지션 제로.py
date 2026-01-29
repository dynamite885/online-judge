n,x,y,r,*t=map(int,open(0).read().split())
a=b=0
for i in t:
    a+=x-r<i<x+r
    b+=i==x-r
    b+=i==x+r
print(a,b)