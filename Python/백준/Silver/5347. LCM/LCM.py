for _ in' '*int(input()):
    a,b=map(int,input().split())
    x,y=sorted([a,b])
    while x:x,y=y%x,x
    print(a//y*b)