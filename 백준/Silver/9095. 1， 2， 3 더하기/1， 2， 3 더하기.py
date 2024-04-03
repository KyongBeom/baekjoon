
tc = int(input())

for i in range(tc):
    cnt = 0
    number = int(input())
    dp = [0] * (number + 1)
    
    for i in range(1, number + 1):
        if i == 1:
            dp[1] = 1
        elif i == 2:
            dp[2] = 2
        elif i == 3:
            dp[3] = 4
        else:
            dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
    print(dp[-1])
    