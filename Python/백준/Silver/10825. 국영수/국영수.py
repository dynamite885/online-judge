a=[]
for i in[*open(0)][1:]:
 s,*b=i.split()
 b=map(int,b)
 a+=[[s,*b]]
a.sort(key=lambda x:(-x[1],x[2],-x[3],x[0]))
for i in a:print(i[0])