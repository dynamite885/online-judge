N = int(input())
S = [input().split() for _ in range(N)]
L = input().split()
d = dict()

for i in range(N):
    for j in range(len(S[i])):
        t = i * 10000 + j
        d[S[i][j]] = t
        S[i][j] = t

for i in range(len(L)):
    if L[i] not in d:
        exit(print("Impossible"))
    L[i] = d[L[i]]

revS = []
for sen in S:
    revS += [sen[::-1]]

revL = L[::-1]

t = revL[-1]

idx = 0

isPossible = True

while revS:
    if not revL or len(revS) <= idx:
        isPossible = False
        break
    if revL[-1] == revS[idx][-1]:
        revL.pop()
        revS[idx].pop()
        if not revS[idx]:
            revS.pop(idx)
        idx = 0
        continue
    idx += 1

print(["Impossible","Possible"][isPossible])