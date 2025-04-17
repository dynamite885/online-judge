*a,=map(int,[*open(0)][1].split())
y=-sum(~i//30 for i in a)*10
m=-sum(~i//60 for i in a)*15
print(*"YM"[(m<y):2-(y<m)],min(y,m))