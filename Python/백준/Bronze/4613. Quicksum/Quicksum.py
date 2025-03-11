for s in[*open(0)][:-1]:
 t=1;a=0
 for c in s[:-1]:a+=t*[0,ord(c)-64][c.isalpha()];t+=1
 print(a)