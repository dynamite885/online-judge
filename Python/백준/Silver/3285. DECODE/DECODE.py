t="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
a={*t}
s=""
for i in input():s+=i;a-={i}
s+=''.join(sorted(a))
k=int(input())-1
s=s[-k:]+s[:-k]
p=input()
r = str.maketrans(s,t)
print(p.translate(r))