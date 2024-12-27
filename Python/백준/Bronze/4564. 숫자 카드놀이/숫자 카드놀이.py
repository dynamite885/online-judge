while int(s:=input()):
 while~-len(s):print(end=s+' ');s=str(eval('*'.join(s)))
 print(s)