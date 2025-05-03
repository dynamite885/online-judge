N,K=map(int,input().split())
R=['?']*N
V=[0]*26
i=0
for _ in range(K):
    S,A=input().split()
    S=int(S)
    i+=S
    i%=N
    if R[i]=='?':
        if V[ord(A)-ord('A')]==1:
            exit(print("!"))
        R[i]=A
        V[ord(A)-ord('A')]=1
    elif R[i]!=A:
        exit(print("!"))
R=R[::-1]
idx=R.index(A)
print(''.join(R[idx:]+R[:idx]))