a=set()
for i in[*open(0)][1:]:
 a|={sum(10**(ord(j)-97)for j in i[:-1])}
print(len(a))