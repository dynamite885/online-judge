for i in[*open(0)][:-1]:
    a,b,c=i.split()
    a=int(a)
    c=int(c)
    if b=='D':
        print(a+c)
        continue
    if -200 <= a-c:
        print(a-c)
    else:
        print('Not allowed')