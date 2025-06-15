from collections import deque
n=int(input())
d=deque(range(1,n+1))
while d:
    print(d.popleft(),end=' ')
    if d:d.append(d.popleft())