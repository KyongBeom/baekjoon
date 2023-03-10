
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    i = 0
    j = 0
    arr[i][j] = 1
    delta = [(0,1),(1,0),(0,-1),(-1,0)]
    k = 0
    while True:
        x = delta[k][1]
        y = delta[k][0]
        ni = i+y
        nj = j+x
        if 0<= ni <N and 0<= nj <N and arr[ni][nj] == 0:
            arr[ni][nj] = arr[i][j] + 1
            i = ni
            j = nj
        else:
            k += 1
            if k == 4:
                k = 0
        if arr[i][j] == N**2:
            break
    print(f'#{tc}')
    for i in arr:
        print(*i)