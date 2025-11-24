a,b,n,k=map(int,input().split())
for i in range(a):
    for j in range(b):
        k-=n
        if k<=0:exit(print(i+1,j+1))