N = int(input())

arr = list(map(int, input().split()))
arr.sort()
ans = 0
for i in range(N):
    cnt = arr[i]
    for j in range(i):
        cnt += arr[j]
    ans += cnt
print(ans)