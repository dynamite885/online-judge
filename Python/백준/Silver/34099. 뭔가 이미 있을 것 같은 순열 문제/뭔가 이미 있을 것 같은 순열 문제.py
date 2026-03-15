for s in[*open(0)][1:]:
    n,k=map(int,s.split())
    if k==1:
        if n<4:print(-1)
        else:print(*range(2,n+1,2),*range(1,n+1,2))
    else:
        print(*range(1,n+1))