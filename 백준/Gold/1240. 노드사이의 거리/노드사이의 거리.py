from collections import deque

N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]

for i in range(N-1):
    node1, node2, length = map(int, input().split())
    arr[node1].append((node2, length))
    arr[node2].append((node1, length))

answer = []
for i in range(M):
    n1, n2 = map(int, input().split())

    queue = deque()
    queue.append((n1, 0))
    visited = [0] * (N+1)
    visited[n1] = 1
    while queue:
        s, c = queue.popleft()

        if s == n2:
            answer.append(c)

        for i, j in arr[s]:
            if not visited[i]:
                visited[i] = 1
                queue.append((i, c+j))

for i in answer:
    print(i)