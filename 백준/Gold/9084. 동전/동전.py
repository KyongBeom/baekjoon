T = int(input())

for _ in range(T):
    N = int(input())
    cnt = 0
    lst = list(map(int, input().split()))
    pay = int(input())
    dp = [0] * (pay+1)
    dp[0] = 1
    for i in lst:
        for j in range(1,pay+1):
            if j >= i:
                dp[j] += dp[j-i]
    print(dp[pay])

