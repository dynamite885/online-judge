for _ in range(int(input())):
    a,b=input().split()
    print("YNEOS"[a.count('P')!=b.count('P')or len(a)-len(a.rstrip('N'))!=len(b)-len(b.rstrip('N'))::2])