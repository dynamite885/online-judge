N,M=map(int,input().split())
if N<M:
    if N%2:print((N-1)//2,M-1-N//2)
    else:print((N-1)//2,N//2)
else:
    if M%2:print(N-1-M//2,M//2)
    else:print((M-1)//2,M//2)