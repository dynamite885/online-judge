pi=3.1415927
mile=12*5280
i=0
for r,n,t in map(lambda x:map(eval,x.split()),[*open(0)][:-1]):
    print(f'Trip #{(i:=i+1)}: {(k:=r*n*pi/mile):.2f} {k*3600/t:.2f}')