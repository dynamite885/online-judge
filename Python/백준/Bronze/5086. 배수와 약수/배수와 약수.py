for i in[*open(0)][:-1]:
    a,b=map(int,i.split())
    if b%a<1:print("factor")
    if a%b<1:print("multiple")
    if(a%b)*(b%a):print("neither")