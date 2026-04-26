s=[*open(0)][1]
print(max(s.count(c)for c in{*s}if'`'<c))