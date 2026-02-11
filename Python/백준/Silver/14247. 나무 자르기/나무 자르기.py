I=lambda:map(int,input().split())
I()
print(sum((*I(),*(i*v for i,v in enumerate(sorted(I()))))))