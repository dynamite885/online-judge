for _ in' '*int(input()):
    n=int(input())
    s=sum(map(int,input().split()))
    i=1
    while s<=n:s*=4;i+=1
    print(i)