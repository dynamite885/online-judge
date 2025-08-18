*a,=eval('""'+'+input()'*4)
_,*b=sorted(a)
c=0
for i in range(15):t=a.index(b[i]);c+=abs(i//4-t//4)+abs(i%4-t%4)
print(c)