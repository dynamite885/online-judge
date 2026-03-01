input=open(0).readline
I=lambda:map(int,input().split())
n,m=I()
a=[[*I()]for _ in range(n)]
b=[[*I()]for _ in range(n)]
*c,=I()
d=[0]*n

for i in range(n):
    for j in range(n):
        d[j]=max(d[j],abs(a[i][j]-b[i][j]))

print(sum(d[i-1]for i in c))