s = input()
pos = []
for i in range(len(s)):
    c = s[i]
    if c in 'aiueo':
        pos += [i]

if s[-1] not in 'aiueons':
    if pos:
        print(pos[-1] + 1)
    else:
        print(-1)
else:
    if 2 <= len(pos):
        print(pos[-2] + 1)
    else:
        print(-1)