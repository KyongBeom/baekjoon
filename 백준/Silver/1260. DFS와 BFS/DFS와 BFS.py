def DFS(V):
    visited1[V] = 1
    print(V,end=' ')
    for i in range(1,N+1):
        if visited1[i] == 0 and arr[V][i] == 1:
            DFS(i)
def BFS(V):
    visited2[V] = 1
    queue = [V]
    while queue:
        a = queue.pop(0)
        print(a,end = ' ')
        for i in range(1,N+1):
            if visited2[i] == 0 and arr[a][i] == 1:
                queue.append(i)
                visited2[i] = 1

N, M, V = map(int,input().split())

arr = [[0] * (N + 1) for _ in range(N+1)]
visited1 = [0] * (N + 1)
visited2 = [0] * (N + 1)
for _ in range(M):
    A, B = map(int, input().split())
    arr[A][B] = arr[B][A] = 1
DFS(V)
print()
BFS(V)
