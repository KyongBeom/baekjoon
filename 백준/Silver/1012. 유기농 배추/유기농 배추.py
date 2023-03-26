import sys
sys.setrecursionlimit(10000)

T = int(sys.stdin.readline())

def DFS(x,y):
    d = [(1,0),(-1,0),(0,1),(0,-1)]
    for i,j in d:
        nx = x + i
        ny = y + j
        if 0 <= nx < N and 0 <= ny < M:
            if arr[nx][ny] == 1:
                arr[nx][ny] = -1
                DFS(nx, ny)


for _ in range(T):
    M, N, K =map(int,sys.stdin.readline().split())
    arr = [[0] * M for _ in range(N)]
    ans = 0

    for k in range(K):
        x, y = map(int,sys.stdin.readline().split())
        arr[y][x] = 1


    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                DFS(i,j)
                ans += 1
    print(ans)
