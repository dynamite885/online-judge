for _ in range(int(input())):
    l,r=map(int,input().split())
    print(r-l+(max(l,r)==1))