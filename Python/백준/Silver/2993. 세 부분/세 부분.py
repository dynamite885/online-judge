l=len(s:=input())
a=[]
for i in range(1,l-1):
    for j in range(i+1,l):a+=[s[:i][::-1]+s[i:j][::-1]+s[j:][::-1]]
a.sort()
print(a[0])