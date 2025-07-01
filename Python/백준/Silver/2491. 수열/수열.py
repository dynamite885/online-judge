n,t,*a=map(int,open(0).read().split())
u=d=U=D=1
for i in a:
    if t<i:
        u+=1
        d=1
    elif i<t:
        d+=1
        u=1
    else:
        d+=1
        u+=1
    U=max(U,u)
    D=max(D,d)
    t=i
print(max(U,D))