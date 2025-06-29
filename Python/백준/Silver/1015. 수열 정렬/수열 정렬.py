n,*a=map(int,open(0).read().split())
b=[i for i in enumerate(a)]
b.sort(key=lambda x:x[1])
p=[0]*n
for i in range(n):p[b[i][0]]=i
print(*p)