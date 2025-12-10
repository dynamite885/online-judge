x,y=map(int,input().split())
for _ in range(int(input())):
    a,b=map(int,input().split())
    print(+(x!=a and y!=b))