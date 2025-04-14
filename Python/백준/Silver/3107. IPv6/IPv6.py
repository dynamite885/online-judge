s=input()
c=s.count(':')
s=s.replace('::',':0000'*(8-c)+':')
s=s.split(':')
s=[i.zfill(4) for i in s]
s=':'.join(s)
print(s)