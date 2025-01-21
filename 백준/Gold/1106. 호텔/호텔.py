C, N = map(int,input().split())
lst = []
for _ in range(N):
    x, y = map(int,input().split())
    lst.append([x,y])
# print(lst)
dp = [1e7] * (C + 100)

dp[0] = 0

for i, j in lst:
    for k in range(j,100+C):
            dp[k] = min(dp[k],dp[k-j]+i)

print(min(dp[C:]))
