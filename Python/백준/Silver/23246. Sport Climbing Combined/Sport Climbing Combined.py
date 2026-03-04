n=int(input())
a=[[*map(int,input().split())]for _ in range(n)]
a.sort(key=lambda x:(x[1]*x[2]*x[3],x[1]+x[2]+x[3],x[0]))
print(*[t[0] for t in a[:3]])