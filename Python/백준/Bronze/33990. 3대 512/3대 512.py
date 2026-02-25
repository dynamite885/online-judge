n=int(input())
ans=-1
for _ in range(n):
    t=eval(input().replace(*" +"))
    if 511<t and (ans==-1 or t<ans):
            ans=t
print(ans)