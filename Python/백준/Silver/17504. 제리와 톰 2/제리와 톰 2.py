*a,t=map(int,[*open(0)][k:=1].split())
for i in a[::-1]:t,k=i*t+k,t
print(t-k,t)