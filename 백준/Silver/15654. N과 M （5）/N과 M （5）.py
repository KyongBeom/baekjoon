N, M = map(int, input().split())

arr =list(map(int, input().split()))
arr.sort()
check = []

def dfs(i):
    if len(check) == M:
        print(*check)
        return

    for j in arr:
        if not j in check:
            check.append(j)
            dfs(j)
            check.pop()

dfs(1)
