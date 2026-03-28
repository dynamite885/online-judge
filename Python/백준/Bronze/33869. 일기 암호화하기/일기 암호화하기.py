w=input()
s=input()
t=[*map(lambda x:chr(x+65),range(26))]
w=''.join(w[i] for i in range(len(w))if w[i] not in w[:i])
for c in t:
    if c not in w:w+=c
d={i:j for i,j in zip(t,w)}
for c in s:
    print(end=d[c])