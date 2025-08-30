x=0
for i in[*open(0)][1:]:
    t=0
    a,b,c,d=sorted(map(int,i.split()))
    if a==b==c==d:
        x=max(x,50000+a*5000)
    elif a==b==c or b==c==d:
        x=max(x,10000+b*1000)
    elif a==b and c==d:
        x=max(x,2000+a*500+c*500)
    elif a!=b!=c!=d:
        x=max(x,max(a,b,c,d)*100)
    else:
        if a==b or b==c:
            x=max(x,1000+b*100)
        else:
            x=max(x,1000+d*100)
print(x)