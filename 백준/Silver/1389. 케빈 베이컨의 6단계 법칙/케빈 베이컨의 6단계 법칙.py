from collections import deque

N, M = map(int, input().split())

graph = [[] for i in range(N+1)]
answer = []

for i in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

def bfs(graph, v):
    point = [0] * (N+1)

    H = deque()
    H.append(v)
    check[v] = 1
    while H:
        X = H.popleft()
        for i in graph[X]:
            if check[i] == 0:
                point[i] = point[X] + 1
                check[i] = 1
                H.append(i)

    return sum(point)


for i in range(1, N+1):
    check = [0] * (N+1)
    answer.append(bfs(graph, i))

print(answer.index(min(answer))+1)