n,e,*d=map(int,open(0).read().split())
t,*a=sorted(d)
for i in a:n-=i-t<e;t=i
print(n)