r,c=map(int,input().split())
a=[input()for _ in' '*r]
x=[0]*5
for i in range(r-1):
    for j in range(c-1):
        s=a[i][j:j+2]+a[i+1][j:j+2]
        if'#'not in s:x[s.count('X')]+=1
print(*x)