for s in[*open(0)][1:]:
    a,b,n=map(int,s.split())
    t=n//2*(a+b)
    print(t*t+n%2*(t*a+t*b+a*b))