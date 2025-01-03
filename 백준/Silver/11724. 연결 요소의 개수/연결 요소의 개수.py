def dfs(x, check):
    visited[x] = True
    for k in nodes[x]:
        if not visited[k]:
            dfs(k, check + 1)


n, m = map(int, input().split())

nodes = [ [] for _ in range(n+1)]

for _ in range(m):
    A,B = map(int, input().split())
    nodes[A].append(B)
    nodes[B].append(A)

visited = [False] *  (n+1)
count = 0
for i in range(1, n+1):
    if not visited[i]:
        if not nodes[i]:
            count += 1
            visited[i] = True
        else:
            dfs(i,0)
            count += 1

print(count)

