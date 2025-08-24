d={'A':0b000000,'B':0b001111,'C':0b010011,'D':0b011100,'E':0b100110,'F':0b101001,'G':0b110101,'H':0b111010}
n=int(input())
s=input()
ans=''
for i in range(n):
    t=int(s[i*6:i*6+6],2)
    for k,v in d.items():
        x=t^v
        if bin(x).count('1')<2:
            ans+=k
            break
    else:
        exit(print(i+1))
print(ans)