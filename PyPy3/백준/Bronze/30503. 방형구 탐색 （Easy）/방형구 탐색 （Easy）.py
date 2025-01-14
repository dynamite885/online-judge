n=int(input())
*a,=map(int,input().split())
q=int(input())
for i in range(q):
    e,l,r,*k=map(int,input().split())
    if e==1:
        print(a[l-1:r].count(k[0]))
    else:
        for j in range(l-1,r):a[j]=0