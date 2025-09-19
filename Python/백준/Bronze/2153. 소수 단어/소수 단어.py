t=sum(ord(c)%32+26*(c<'a')for c in input())
print(f'It is {"not "*(0 in[t%i for i in range(2,t)])}a prime word.')