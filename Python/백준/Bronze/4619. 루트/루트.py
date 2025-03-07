while'0 0'<(s:=input()):
 b,n=map(int,s.split())
 k=b;i=0
 while 1:
  if k<abs(b-i**n):print(i-1);break
  k=abs(b-i**n);i+=1