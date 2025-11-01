d, m = open(0).read().split('\n\n')
dic = {f: e for e, f in (line.split() for line in d.split('\n'))}
print('\n'.join(dic.get(w, 'eh') for w in m.split()))