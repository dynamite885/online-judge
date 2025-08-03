n,*a=map(int,open(0).read().split())
b=[[i,v]for i,v in enumerate(a)]
ans=[]
idx=0
while b:
    n-=1
    i,v=b.pop(idx)
    if n==0:ans+=[i+1];break
    idx=(v+n*1000-(0<v)+idx)%n
    ans+=[i+1]
print(*ans)