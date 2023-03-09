T = int(input())
for tc in range(1,T+1):
    N ,M = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    res = 0
    # 범위 지정, N- M + 1

    for i in range(N-M+1):
        for j in range(N-M+1):
            total = 0
            for k in range(M):
                for l in range(M):
                    total += arr[i+k][j+l]
            if total > res:
                res = total
    print(f'#{tc} {res}')