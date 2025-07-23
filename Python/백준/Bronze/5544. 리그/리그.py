N,*X=open(0)
N=int(N)
K=[[i,0]for i in range(N+1)]
for i in X:
    A,B,C,D=map(int,i.split())
    if C>D:K[A][1]+=3
    elif C<D:K[B][1]+=3
    else:K[A][1]+=1;K[B][1]+=1

K.sort(key=lambda x:-x[1])
t=-1
r=0
for i in range(N+1):
    r+=1
    K[i]+=[r]
    if 0<i and K[i][1]==K[i-1][1]:
        K[i][2]=K[i-1][2]

K.sort(key=lambda x:x[0])
for i in K[1:]:
    print(i[2])