n,c=map(int,input().split())
x=y=z=0
for i in range(n):
    a,b=input().split()
    a=int(a)
    x+=a
    if b=='balcony':z+=a
    if b=='bedroom':y+=a
print(x,y,(x-z/2)*c)