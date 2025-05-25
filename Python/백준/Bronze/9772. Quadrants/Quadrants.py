for i in open(0):
    x,y=map(eval,i.split())
    if x*y==0:print('AXIS')
    elif x>0 and y>0:print('Q1')
    elif x<0 and y>0:print('Q2')
    elif x<0 and y<0:print('Q3')
    else:print('Q4')