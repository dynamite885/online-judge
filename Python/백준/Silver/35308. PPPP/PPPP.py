for s in[*open(0)][1:]:
    n,k=map(int,s.split())
    if n==1 or k==2:
        print(*range(2,n+1),1)
    else:
        print(-1)