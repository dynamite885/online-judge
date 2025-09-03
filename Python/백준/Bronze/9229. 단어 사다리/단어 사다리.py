*a,_=open(0).read().split()
c=1
t=''
for s in a:
    if s=='#':
        print(['Incorrect','Correct'][c])
        c=1
        t=''
        continue
    if t=='':
        t=s
        continue
    c*=(sum(i!=j for i,j in zip(t,s))==1)*(len(s)==len(t))
    t=s