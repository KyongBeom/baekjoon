n = int(input())
dp = [0, 1]

for i in range(2, n+1):
    check = 4
    point = 1

    while (point**2) <= i:
        check = min(check, dp[i-point**2])
        point += 1
        
    dp.append(check + 1)
print(dp[n])