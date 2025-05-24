for i in[*open(t:=0)][1:]:
 *a,=map(int,i.split())
 x=max(a)
 y=max(a,key=a.count)
 t=max(t,[x,10+y,100+y*10][int(sum(map(a.count,a))**.5)-1]*100)
print(t)