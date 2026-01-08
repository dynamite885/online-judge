a=open(0).read()
print('YNEOS'[5>len({*a})or len({*a[::4],*'HP'})==3::2])