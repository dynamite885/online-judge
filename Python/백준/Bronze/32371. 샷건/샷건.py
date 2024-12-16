*a,s=[input()for _ in' '*5]
b=[10*[0]for _ in' '*4]
for i in range(4):
    for j in range(10):
        if a[i][j]in s:b[i][j]=1
c=0
for i in range(4):
    for j in range(10):
        c+=b[i][j]
        if c==5:exit(print(a[i][j]))