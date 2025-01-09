from collections import deque

def bfs(tlst):
    for i,j in tlst:
        arr[i][j] = 1

    q = deque()
    w = [[0]*m for _ in range(n)]
    CNT = cnt - 3
    for ti, tj in virus:
        q.append((ti, tj))
        w[ti][tj] = 1

    while q:
        ci, cj = q.popleft()
        for  di, dj in ((-1,0), (1,0), (0,1), (0,-1)):
            ni, nj = ci+di, cj+dj
            if 0<= ni < n and 0<=nj < m and arr[ni][nj] == 0 and w[ni][nj] == 0:
                q.append((ni,nj))
                w[ni][nj]=1
                CNT -= 1

    for i,j in tlst:
        arr[i][j] = 0

    return CNT


n ,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

lst = []
virus = []

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            lst.append((i, j))
        elif arr[i][j] == 2:
            virus.append((i, j))


cnt = len(lst)
check = [0] * cnt
ans = 0

for i in range(cnt-2):
    for j in range(i+1, cnt-1):
        for k in range(j+1, cnt):
            ans = max(ans, bfs([lst[i],lst[j],lst[k]]))
print(ans)