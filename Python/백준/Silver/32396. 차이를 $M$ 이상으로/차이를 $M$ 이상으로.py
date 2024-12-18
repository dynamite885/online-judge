n,m,t,*a=map(int,open(c:=0).read().split())
for i in a:
 if abs(i-t)<m:t=-m;c+=1
 else:t=i
print(c)