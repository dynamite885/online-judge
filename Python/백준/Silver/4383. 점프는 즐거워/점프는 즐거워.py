for s in open(0):
 n,t,*a=map(int,s.split())
 k=[0]*3000
 for i in a:k[abs(t-i)-1]=1;t=i
 print(['J','Not j'][0<k[:n-1].count(0)]+'olly')