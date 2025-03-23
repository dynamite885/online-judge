for i in[*open(0)][1:]:
 a,b=i.split('-')
 x,y,z=map(lambda x:ord(x)-65,a)
 print((100<abs(x*26**2+y*26+z-int(b)))*'not '+'nice')