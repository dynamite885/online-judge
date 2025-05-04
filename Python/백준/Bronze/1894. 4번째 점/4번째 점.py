for s in open(0):
    x1,y1,x2,y2,x3,y3,x4,y4=map(float,s.split())
    if x1==x3 and y1==y3:
        x1,y1,x2,y2=x2,y2,x1,y1
    if x1==x4 and y1==y4:
        x1,y1,x2,y2,x3,y3,x4,y4=x2,y2,x1,y1,x4,y4,x3,y3
    if x2==x4 and y2==y4:
        x3,y3,x4,y4=x4,y4,x3,y3
    print('%.3f'%(x1-x2+x4),'%.3f'%(y1-y2+y4))