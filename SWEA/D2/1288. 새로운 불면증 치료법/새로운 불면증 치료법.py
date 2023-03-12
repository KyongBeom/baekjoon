T = int(input())

for tc in range(1 ,T+1):
    N = int(input())
    res = []
    i =1
    while True:
        cnt = i * N
        solve = str(cnt)
        for j in solve:
            res.append(j)
        ans = set(res)
        if len(ans) == 10:
            break
        i += 1
    print(f'#{tc} {cnt}')