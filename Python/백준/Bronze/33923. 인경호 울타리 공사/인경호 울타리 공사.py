a,b=map(int,input().split())
t=a==b
print((min(a,b)+~t)**2+t)