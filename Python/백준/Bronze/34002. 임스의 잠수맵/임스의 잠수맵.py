a,b,c=map(int,input().split())
s,v=map(lambda x:int(x)*30,input().split())
l=int(input())
t=(250-l)*100
ans=0
while 0<t:
    if v:
        v-=1
        t-=c
    elif s:
        s-=1
        t-=b
    else:
        t-=a
    ans+=1

print(ans)