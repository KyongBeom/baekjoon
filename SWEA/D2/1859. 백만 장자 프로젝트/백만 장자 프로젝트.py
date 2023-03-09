T = int(input())

for tc in range(1,T+1):
    N = int(input())
    sell = list(map(int, input().split()))
    res = 0
    maxs = sell[-1]
    for i in range(N-2, -1, -1):
        if sell[i] > maxs:
            maxs = sell[i]
        else:
            res += maxs-sell[i]
    print(f'#{tc} {res}')