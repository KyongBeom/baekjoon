N, M = map(int, input().split())

arr =[]

def dfs(i):
    if len(arr) == M:
        print(*arr)
        return

    for j in range(i, N+1):
        arr.append(j)
        dfs(j)
        arr.pop()

dfs(1)
