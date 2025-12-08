from functools import cmp_to_key

def cmpstr(x, y):
    a, b = int(x+y), int(y+x)
    return (a<b) - (b<a)

n,*a=open(0).read().split()
a.sort(key=cmp_to_key(cmpstr))
print(int(''.join(a)))