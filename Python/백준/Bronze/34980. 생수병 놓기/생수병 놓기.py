_,a,b=open(0)
x,y=map(str.count,[a,b],'ww')
print([['Its fine','Manners maketh man','Oryang'][(x<y)-(y<x)],'Good'][a==b])