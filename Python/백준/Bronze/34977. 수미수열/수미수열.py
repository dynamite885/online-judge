n,*l=map(int,open(0).read().split())
print('yneos'[all(l[:i+1]!=l[~i:]for i in range(n-1))::2])