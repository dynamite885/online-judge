n,c,*a=map(int,open(0).read().split())
r=range(c+1)
t=[0]*-~c
for i in a:
 for j in r[::int(i)]:t[j]=1
print(sum(t)-1)