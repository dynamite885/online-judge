m,n=map(int,input().split())
d=*map(str,range(10)),*'ABCDEF'
r=''
while m:r+=d[m%n];m//=n
print(r[::-1]or'0')