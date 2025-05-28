N,B,H,W=map(int,input().split())
m=10**9
for _ in range(H):
    p=int(input())
    *a,=map(int,input().split())
    for i in a:
        if i>=N:
            t=p*N
            if t<=B:m=min(m,t)
if m==10**9:print("stay home")
else:print(m)