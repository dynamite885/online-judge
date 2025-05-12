for i in[*open(0)][:-1]:
    a=c=0
    while a<float(i):
        c+=1
        a+=1/(c+1)
    print(c,'card(s)')