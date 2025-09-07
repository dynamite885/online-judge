a,b,c,d=map(int,open(0).read().split())
print(['Either','Hanyang Univ.','Yongdap'][(a+c<b+d)-(a+c>b+d)])