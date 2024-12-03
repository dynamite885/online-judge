N,T=map(int,input().split())
X=input()
t=2**(N-T)
a=""
p=0
while p<2**N:a=max(a,X[p:p+t]);p+=t
print(a)