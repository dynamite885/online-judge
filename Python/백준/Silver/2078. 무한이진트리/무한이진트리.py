a,b=map(int,input().split())
l=r=0
while 1<min(a,b):
    if a>b:l+=a//b;a%=b
    else:r+=b//a;b%=a
print(l+a-1,r+b-1)