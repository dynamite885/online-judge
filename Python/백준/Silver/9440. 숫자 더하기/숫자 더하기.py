while'0'<(s:=input()):
 *a,=sorted(s.split()[1:]);k=a.count('0')
 x,y=a[k:k+2];a[k]=a[k+1]='0';a[0],a[1]=x,y
 print(eval(''.join(a[::2])+'+'+''.join(a[1::2])))