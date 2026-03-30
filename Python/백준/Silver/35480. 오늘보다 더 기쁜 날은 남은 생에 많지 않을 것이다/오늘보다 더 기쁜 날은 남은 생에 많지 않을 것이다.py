date=[31,28,31,30,31,30,31,31,30,31,30,31]

y0,m0,d0=map(int,input().split())
y1,m1,d1=map(int,input().split())
n=int(input())
a=dict()
for _ in range(n):
    y,m,d=map(int,input().split())
    a[(m,d)]=y

t=y0-a[(m0,d0)]
cnt = 0

for y in range(y0,y1+1):
    for m in range(1,13):
        for d in range(1,date[m-1]+1):
            if not (y0*10000+m0*100+d0<=y*10000+m*100+d<=y1*10000+m1*100+d1):continue
            x=(m,d)
            if x in a and t<y-a[x]:
                    cnt+=1

print(cnt)