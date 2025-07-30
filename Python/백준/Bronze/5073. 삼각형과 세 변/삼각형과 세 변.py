for i in[*open(0)][:-1]:
    a,b,c=sorted(map(int,i.split()))
    if a+b<=c:print('Invalid');continue
    print(['Equilateral','Isosceles','Scalene'][len({a,b,c})-1])