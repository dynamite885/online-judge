n,a,b=map(int,open(0))
print(sum((0<-~i%a)^(0<-~i%b)for i in range(n)))