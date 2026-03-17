n,x,m,*a=map(int,open(0).read().split())
t=sum(i<x for i in a)
print(min(m-t,t))