*s,=map(int,open(0).read().split())
t=max(b:=[(sum(s[i::3]),s[i::3].count(3))for i in(1,2,3)])
print([b.index(t)+1,0][1<b.count(t)],t[0])