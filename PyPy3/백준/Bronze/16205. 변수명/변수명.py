import re
s = re.sub(r'(?<!^)([A-Z])', lambda m: '_' + m.group(1), input().split()[1]).lower()
t = s.split('_')
print(t[0] + ''.join(w.capitalize() for w in t[1:]))
print(s)
print(''.join(w.capitalize() for w in t))