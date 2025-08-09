t=[0]*101
table=0,*map(int,input().split())
for _ in'   ':
    p,q=map(int,input().split())
    for i in range(p,q):t[i]+=1
cost=0
for i in t:
    cost+=table[i]*i
print(cost)