N,*A=open(0)
N=int(N)
A=[[*map(int,i.split())]for i in A]
A.sort(key=lambda x:x[0])
L=R=ans=0
for a,d in A:
    if d==1:R+=1
    elif d==0:ans+=R*2
    else:ans+=R
for a,d in A[::-1]:
    if d==-1:L+=1
    elif d==0:ans+=L*2
print(ans)