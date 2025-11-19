for i in range(int(input())):
    r=a=0
    while s:=input():
        a+=len(s)
        r+=s.count('#')
    print(f'Efficiency ratio is {(a-r)/a*100:.1f}%.'.replace('.0',''))