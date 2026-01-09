p=[0,0]+[1]*10001
for i in range(2,101):
    if p[i]:
        for j in range(i*i,10002,i):
            p[j]=0
for _ in range(int(input())):
    n=int(input())
    if p[n+1]:
        print(1)
        print(1,n+1)
    else:
        print(0)