r,c=map(int,input().split())
a=[[*map(int,input().split())]for _ in' '*r]
t=int(input())
z=0
for i in range(r-2):
 for j in range(c-2):
  z+=t<=sorted(a[i+x][j+y]for x in range(3)for y in range(3))[4]
print(z)