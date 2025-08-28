p={'@':'*3','%':'+5','#':'-7'}
for i in[*open(0)][1:]:
    n,*a=i.split()
    for j in a:
        n=str(eval(n+p[j]))
    print(f'{float(n):.2f}')