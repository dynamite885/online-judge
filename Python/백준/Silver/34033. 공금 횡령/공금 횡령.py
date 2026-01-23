x,*y=open(0)
n,m=map(int,x.split())
p={}
for a,b in map(str.split,y[:n]):
    p[a]=int(b)
cnt=0
for c,d in map(str.split,y[n:]):
    if p[c]*1.05<int(d):cnt+=1
print(cnt)