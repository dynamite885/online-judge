for i in open(0):
 s={*i};i=int(i);k=1
 while len(s)<11:k+=1;s|={*str(i*k)}
 print(k)