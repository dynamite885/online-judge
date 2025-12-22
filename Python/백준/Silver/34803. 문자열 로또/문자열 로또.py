l,n=map(int,input().split())
a=[input()for _ in range(n)]
k=int(input())
d={}
for s in a:
    for i in range(l-k+1):
        t=s[i:i+k]
        d[t]=d.get(t,0)+1
print(max(d.values()))