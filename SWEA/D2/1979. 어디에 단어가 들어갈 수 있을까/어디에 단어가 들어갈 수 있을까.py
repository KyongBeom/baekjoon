T = int(input())
for tc in range(1,T+1):
    N, K = map(int,input().split())
    arr = [list(map(int, input().split())) +[0] for _ in range(N)]
    arr = arr + [[0] * (N+1)]
    res = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] == 1:
                cnt += 1
                if arr[i][j+1] == 0 and cnt == K:
                    res += 1
            else:
                cnt = 0
    for i in range(N):
        cnt2 = 0
        for j in range(N):
            if arr[j][i] == 1:
                cnt2 += 1
                if arr[j+1][i] == 0 and cnt2 == K:
                    res += 1
            else:
                cnt2 = 0
    print(f'#{tc} {res}')