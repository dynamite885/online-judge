input=open(0).readline
n,k=map(int,input().split())
a=[[*map(int,input().split())]for _ in range(n)]
b=[[max(t),0][1<t.count(max(t))]for t in zip(*a)]

for i in range(n):
    for j in range(k):
        if a[i][j]!=b[j]:
            a[i][j]=0
cnt=0
for t in a:
    cnt+=0<sum(t)
print(cnt)