n,*a=map(int,open(0).read().split())
s=t=0
for i in a:t+=[-1,1][i];s+=t
print(s)