for i in[*open(0)][1:]:
    a,b=i.split()
    a=float(a)
    if b=='kg':x=a*2.2046;y='lb'
    elif b=='l':x=a*0.2642;y='g'
    elif b=='lb':x=a*.4536;y='kg'
    elif b=='g':x=a*3.7854;y='l'
    x+=.0000001
    print('%.4f'%x,y)