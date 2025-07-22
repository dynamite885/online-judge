M,N=map(int,open(0))
prime=[0]*(N+1)
for i in range(2,N+1):
    if prime[i]==0:
        for j in range(i*2,N+1,i):
            prime[j]=1

prime[0:2]=[1,1]
pSum=[]
for i in range(M,N+1):
    if prime[i]==0:
        pSum.append(i)
if pSum:
    print(sum(pSum))
    print(min(pSum))
else:print(-1)