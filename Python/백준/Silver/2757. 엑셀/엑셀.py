for i in[*open(0)][:-1]:
    n,m=map(int,i[1:].split("C"))
    if n==0 and m==0:
        break
    s=""
    while m>0:
        m-=1
        s+=chr(65+m%26)
        m//=26
    print(s[::-1]+str(n))