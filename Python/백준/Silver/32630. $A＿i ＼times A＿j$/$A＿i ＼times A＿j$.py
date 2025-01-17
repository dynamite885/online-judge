n,*a=map(int,open(0).read().split())
s=sum(a)
a.sort()
x,y,*b=a
s=max(s,x*y*2+sum(b))
*b,x,y=a
s=max(s,x*y*2+sum(b))
print(s)