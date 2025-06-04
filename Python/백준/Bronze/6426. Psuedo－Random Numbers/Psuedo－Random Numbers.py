for s in[*open(t:=0)][:-1]:
    t+=1
    Z,I,M,L=map(int,s.split())
    z,i,m,l=Z,I,M,L
    c1=set()
    while 1:
        if l in c1:break
        c1.add(l)
        l=(z*l+i)%m
    c2=set()
    while 1:
        if l in c2:break
        c2.add(l)
        l=(z*l+i)%m
    print(f'Case {t}:',len(c2))