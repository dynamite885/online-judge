d={}
for i in[*open(0)][1:]:
    p,s=i.split()
    if'-'!=s:d.setdefault(s,d.get(s)or[]);d[s]+=[p]
cnt=0
ans=''
for i in d.keys():
    if len(d[i])==2:cnt+=1;ans+=d[i][0]+' '+d[i][1]+'\n'
print(cnt)
print(ans)