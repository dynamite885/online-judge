for s in open(0):
    s,t=s.split()
    i=0
    for c in t:
        if i<len(s)and c==s[i]:i+=1
    print('YNeos'[i!=len(s)::2])