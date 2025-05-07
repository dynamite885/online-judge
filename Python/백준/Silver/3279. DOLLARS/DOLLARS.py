n,t,*a=map(int,open(0))
d=100
m=0
for i in a:
    if t>i:
        m+=d/100*t
        d=0
    elif t<i:
        d+=m*100/t
        m=0
    t=i
d+=m*100/t
print("%.2f"%d)