from collections import deque

N, M = map(int, input().split())
arr = [list(map(str, input())) for i in range(N)]

di, dj = [1,-1,0,0], [0,0,1,-1]

visited = [[0]*M for i in range(N)]
si, sj = 0, 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == "I":
            si = i
            sj = j

visited[si][sj] = 1
que = deque()
que.append([si,sj])
cnt = 0
while que:
    dx, dy = que.popleft()
    for a in range(4):
        nx, ny = dx+ di[a], dy+dj[a]
        if 0 <= nx < N and 0<= ny < M and visited[nx][ny] == 0 and arr[nx][ny] != "X":
            que.append([nx,ny])
            visited[nx][ny] = 1
            if arr[nx][ny] =="P":
                cnt += 1
print(cnt if cnt else "TT")


