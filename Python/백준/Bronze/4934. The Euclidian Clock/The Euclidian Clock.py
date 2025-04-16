import math
for i in range(int(input())):
    t1=0
    H,M,S,U=map(int,input().split())
    t1=U+S*100+M*6000+H*360000
    t2=0
    H,M,S,U=map(int,input().split())
    t2=U+S*100+M*6000+H*360000
    r=float(input())
    t=abs(t1-t2)
    print(f"{i+1}. {math.pi*r*r*t/4320000:.3f}")