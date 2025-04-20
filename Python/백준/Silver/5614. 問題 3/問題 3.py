d={}
for i in[*open(0)][1:]:
    k,v=i.split()
    v=int(v)
    if k in d:
        d[k]+=v
    else:
        d[k]=v
for k,v in sorted(d.items(),key=lambda x:(len(x[0]),x[0])):
    print(k,v)