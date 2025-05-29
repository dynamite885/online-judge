m,*a=open(0)
m,n=map(int,m.split())
i=c=0
d={}
for s in a:
    if i<m:
        x,y=s.split()
        y=int(y)
        d[x]=y
    else:
        if s.strip()=='.':print(c);c=0
        else:
            *b,=s.split()
            for w in b:
                c+=d.get(w,0)
    i+=1