for _ in' '*int(input()):
    s=input()
    p,q,r=map(int,s.split())
    flag=1
    for B in range(int(max(*s))+1,17):
        P,Q,R=p,q,r
        a=b=c=0
        t=1
        while P:
            a+=P%10*t
            P//=10
            t*=B
        t=1
        while Q:
            b+=Q%10*t
            Q//=10
            t*=B
        t=1
        while R:
            c+=R%10*t
            R//=10
            t*=B
        if a*b==c:print(B);flag=0;break
    if flag:print(0)