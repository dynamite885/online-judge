_,*x=open(0)
print('Gnomes:')
for i in x:
    a,b,c=map(int,i.split())
    print(['Uno','O'][sorted([a,b,c])[1]==b]+'rdered')