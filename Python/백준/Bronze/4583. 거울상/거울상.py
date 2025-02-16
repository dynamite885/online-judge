import re
for i in[*open(0)][:-1]:
 if s:=re.findall('^[bdpqiovwx]*$',i[:-1]):print(s[0][::-1].replace(*'pQ').replace(*'qp').replace(*'Qq').replace(*'bD').replace(*'db').replace(*'Dd'))
 else:print('INVALID')