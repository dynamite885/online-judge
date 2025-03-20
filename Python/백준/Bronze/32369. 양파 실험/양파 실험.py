n,a,b=map(int,input().split())
x=y=1
while n:
 n-=1;x+=a;y+=b
 if x<y:x,y=y,x
 if x==y:y-=1
print(x,y)