for _ in' '*int(input()):
    n,*a=map(int,input().split());c=0;t=[]
    for i in a:c+=sum(map(i.__lt__,t));t+=[i]
    print(n,c)