a,b,c,d=map(int,open(0).read().split())
m=t=i=0
while i<4:
    if m<a/c+b/d:
        t=i
        m=a/c+b/d
    i+=1
    a,b,c,d=c,a,d,b
print(t)