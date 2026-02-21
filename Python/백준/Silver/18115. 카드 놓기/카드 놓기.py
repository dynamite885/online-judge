from collections import deque
n,*a,_=map(int,open(0).read().split())
b=deque()
t=p=1
for i in a[::-1]:
    p+=1
    if i==1:
        b.appendleft(t)
        t=p
    elif i==2:
        b.appendleft(p)
    else:
        b.append(p)

print(t,*b)