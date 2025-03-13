n,*a=map(int,open(t:=0).read().split())
b=[]
for _ in' '*n:b.insert(a[t],t:=t+1)
print(*b[::-1])