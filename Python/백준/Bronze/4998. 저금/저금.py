for i in open(0):
    y=0
    N,B,M=map(float,i.split())
    while N<M:
        y+=1
        N+=N*B/100
    print(y)