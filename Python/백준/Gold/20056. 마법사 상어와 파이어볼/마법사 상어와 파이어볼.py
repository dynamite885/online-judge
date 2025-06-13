N,M,K=map(int,input().split())
a=[[[] for _ in range(N)] for _ in range(N)]
b=[[[] for _ in range(N)] for _ in range(N)]
dx=[0,1,1,1,0,-1,-1,-1]
dy=[-1,-1,0,1,1,1,0,-1]

for _ in range(M):
    r,c,m,s,d=map(int,input().split())
    a[r-1][c-1]+=[[m,s,d]]

for _ in range(K):
    for i in range(N):
        for j in range(N):
            if a[i][j]:
                for m,s,d in a[i][j]:
                    ni=(i+s*dy[d])%N
                    nj=(j+s*dx[d])%N
                    b[ni][nj]+=[[m,s,d]]
            a[i][j]=[]
    for i in range(N):
        for j in range(N):
            if len(b[i][j])<2:
                a[i][j]=b[i][j]
                b[i][j]=[]
                continue
            mSum,sSum=0,0
            odd=even=0
            for m,s,d in b[i][j]:
                mSum+=m
                sSum+=s
                odd+=d%2
                even+=d%2==0
            if mSum//5==0:
                b[i][j]=[]
                continue
            if odd*even:
                for nd in[1,3,5,7]:
                    a[i][j]+=[[mSum//5,sSum//len(b[i][j]),nd]]
            else:
                for nd in[0,2,4,6]:
                    a[i][j]+=[[mSum//5,sSum//len(b[i][j]),nd]]
            b[i][j]=[]

total=0
for i in range(N):
    for j in range(N):
        for m,s,d in a[i][j]:
            total+=m
print(total)