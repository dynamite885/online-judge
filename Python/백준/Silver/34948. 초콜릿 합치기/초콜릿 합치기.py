I=lambda:[*map(int,input().split())]
n=int(input())
x=y=0
for i,j in sorted([*zip(I(),I())])[::-1]:
    x+=j
    y=max(y,i*x)
print(y)