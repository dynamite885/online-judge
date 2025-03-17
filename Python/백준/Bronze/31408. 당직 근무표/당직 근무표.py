from collections import*
n,*a=map(int,open(0).read().split())
print('YNEOS'[-~n//2<max(Counter(a).values())::2])