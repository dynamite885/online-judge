*a,=open(0)
b=[]
for i in a:
 t=0
 for j in i.split():b+=[0]*(len(b)<=t);b[t]=max(b[t],len(j));t+=1
for i in a:
 r=''
 for j,k in zip(i.split(),b):r+=j+' '*(k-len(j)+1)
 print(r.strip())