while 1:
    n,m,k=map(int,input().split())
    if n+m+k==0:exit()
    *a,=map(int,input().split())
    arr=[]
    idx=0
    while len(arr)<m:
        arr+=[n]
        n+=a[idx%k]
        idx+=1
    print(sum(arr))