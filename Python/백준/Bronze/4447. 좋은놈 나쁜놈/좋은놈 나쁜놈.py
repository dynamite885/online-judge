for i in[*open(0)][1:]:
    g,b=i.lower().count('g'),i.lower().count('b')
    print(i[:-1],'is',['NEUTRAL','A BADDY','GOOD'][(g<b)-(g>b)])