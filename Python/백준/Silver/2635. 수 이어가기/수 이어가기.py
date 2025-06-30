n=int(input())
x=n+1
ans=0
arr=[]
while x:
    a,b=n,x
    c=a-b
    cnt=2
    tmp=[a,b]
    while 0<=c:
        tmp+=[c]
        cnt+=1
        a,b=b,c
        c=a-b
    if ans<cnt:
        ans=cnt
        arr=tmp[:]
    x-=1

print(ans)
print(*arr)