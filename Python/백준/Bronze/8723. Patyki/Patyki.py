a,b,c=sorted(map(int,input().split()))
if a*a+b*b==c*c:print(1)
elif a==b==c:print(2)
else:print(0)