from math import*
k=int(input())
t=ceil(log2(k))
print(2**t,t-int(log2(k&-k)))