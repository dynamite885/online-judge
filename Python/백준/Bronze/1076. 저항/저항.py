a,b,c=open(0).read().split()
d={'black':0,'brown':1,'red':2,'orange':3,'yellow':4,'green':5,'blue':6,'violet':7,'grey':8,'white':9}
print((d[a]*10+d[b])*(10**d[c]))