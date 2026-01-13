n=int(input())
s=input()
t=-1
if n%2:exit(print("NO"))
for c in "PAUL":
    d=s[t+1::2].find(c)
    if d==-1:exit(print("NO"))
    t+=d*2+1
print("YES")