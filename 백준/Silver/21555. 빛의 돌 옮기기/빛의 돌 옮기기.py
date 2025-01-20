N, K = map(int,input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [[0] * 2 for _ in range(N + 1)]

dp[1][0] = A[0]
dp[1][1] = B[0]


for i in range(2, N + 1):
    dp[i][0] = min(
        dp[i - 1][0] + A[i - 1], 
        dp[i - 1][1] + A[i - 1] + K 
    )
    dp[i][1] = min(
        dp[i - 1][1] + B[i - 1],
        dp[i - 1][0] + B[i - 1] + K
    )

print(min(dp[N][0],dp[N][1]))