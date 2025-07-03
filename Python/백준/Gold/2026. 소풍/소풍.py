N,*A = open(0)
K,N,F = map(int,N.split())
adj = [set()for _ in range(N+1)]
for i in A:
    u,v = map(int,i.split())
    adj[u].add(v)
    adj[v].add(u)

def dfs(depth,last):
    if depth == K:
        print(*sorted(students),sep='\n')
        exit()
    for i in range(last+1,N+1):
        flag = 1
        for s in students:
            if s not in adj[i]:
                flag = 0
                break
        if flag:
            students.add(i)
            dfs(depth+1,i)
            students.remove(i)

for i in range(1,N+1):
    students = {i}
    dfs(1,i)
print(-1)