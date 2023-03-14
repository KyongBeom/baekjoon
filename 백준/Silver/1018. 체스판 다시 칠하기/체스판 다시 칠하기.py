N , M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
res = []
for a in range(N - 7):
    for b in range(M - 7):
        ans1 = 0
        ans2 = 0
        for i in range(a, a + 8):
            for j in range(b, b + 8):
                if (i+j)%2 == 0:
                    if arr[i][j] != 'W':
                        ans1 += 1
                    elif arr[i][j] != 'B':
                        ans2 += 1
                else :
                    if arr[i][j] != 'B':
                        ans1 += 1
                    elif arr[i][j] != 'W':
                        ans2 += 1
        res.append(ans1)
        res.append(ans2)
print(min(res))


