T=int(input())
n=int(input())
A=[0,*map(int, input().split())]
m=int(input())
B=[0,*map(int, input().split())]

for i in range(n):
    A[i+1]+=A[i]
for i in range(m):
    B[i+1]+=B[i]

Asubs=[]
Bsubs=[]

for i in range(n):
    for j in range(i+1, n+1):
        Asubs+=[A[j]-A[i]]
for i in range(m):
    for j in range(i+1, m+1):
        Bsubs+=[B[j]-B[i]]

Asubs.sort()
Bsubs.sort()

a=len(Asubs)
b=len(Bsubs)
p=0
q=b-1
cnt=0

while p<a and q>=0:
    if Asubs[p]+Bsubs[q]==T:
        pCnt=qCnt=0
        aTmp=Asubs[p]
        bTmp=Bsubs[q]
        while p<a and Asubs[p]==aTmp:
            p+=1
            pCnt+=1
        while q>=0 and Bsubs[q]==bTmp:
            q-=1
            qCnt+=1
        cnt+=pCnt*qCnt

    elif Asubs[p]+Bsubs[q]<T:
        p+=1
    else:
        q-=1

print(cnt)