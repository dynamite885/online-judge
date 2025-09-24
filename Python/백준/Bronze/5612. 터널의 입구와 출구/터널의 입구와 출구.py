n=int(input())
m=int(input())
t=m
for _ in range(n):
    a,b=map(int,input().split())
    m+=a-b
    t=max(t,m)
    if m<0:exit(print(0))
print(t)