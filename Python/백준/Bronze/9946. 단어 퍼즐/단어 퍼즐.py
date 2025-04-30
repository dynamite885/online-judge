*a,=open(t:=0).read().split()
for i,j in zip(a[::2],a[1:-1:2]):
    a=sorted(i)
    b=sorted(j)
    t+=1
    print(f'Case {t}:', ''.join(a) == ''.join(b) and 'same' or 'different')