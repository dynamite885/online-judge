t=len(s:=b"%a"%input())//2
print("RLEUACDKYY"[sum(s[:t])==sum(s[t:])::2])