input=open(0).readline
for _ in range(int(input())):
    n=int(input())
    a={*map(int,input().split())}
    m=int(input())
    for i in map(int,input().split()):
        print(+(i in a))