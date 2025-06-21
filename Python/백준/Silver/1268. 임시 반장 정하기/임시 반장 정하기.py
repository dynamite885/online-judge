n,*a=open(0)
n=int(n)
s=[set()for _ in range(n)]
t=[0]*n
for g in zip(*[[*map(int,j.split())]for j in a]):
    for x in range(n):
        for y in range(n):
            if g[x]==g[y]:
                s[x]|={y}
for i in range(n):
    t[i]=len(s[i])
m=max(t)
print(t.index(m)+1)