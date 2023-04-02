N, K = map(int, input().split())
visited = [0] * N
arr = []
cnt = 0
for i in range(N):
    arr.append(int(input()))
for j in range(N-1,-1,-1):
    if K >= arr[j]:
        while K >= arr[j]:
            K -= arr[j]
            cnt += 1
print(cnt)