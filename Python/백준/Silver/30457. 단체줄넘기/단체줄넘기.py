a=[*open(0)][1].split()
print(sum(min(a.count(i),2)for i in{*a}))