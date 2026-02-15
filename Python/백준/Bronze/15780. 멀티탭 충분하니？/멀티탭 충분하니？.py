n,k,*a=map(int,open(0).read().split())
print("YNEOS"[sum(-~i//2 for i in a)<n::2])