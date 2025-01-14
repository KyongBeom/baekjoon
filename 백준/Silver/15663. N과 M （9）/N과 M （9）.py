N, M = map(int, input().split())

arr =list(map(int, input().split()))
arr.sort()
check = []
lst = [0] * N
def dfs():
    point = 0
    if len(check) == M:
            print(*check)
            return
    for i in range(N):
        if point != arr[i] and lst[i] == 0:
            check.append(arr[i])
            lst[i] = 1
            point = arr[i]
            dfs()
            check.pop()
            lst[i] = 0

dfs()
