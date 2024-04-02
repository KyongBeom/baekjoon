from collections import deque
import sys

m, n, h = map(int, sys.stdin.readline().split())
arr = []
queue = deque([])

for i in range(h):
    s_arr = []
    for j in range(n):
        s_arr.append(list(map(int,sys.stdin.readline().split())))
        for k in range(m):
            if s_arr[j][k] == 1:
                queue.append([i,j,k])
    arr.append(s_arr)

answer = 0

di, dj, dk = [1,-1,0,0,0,0] , [0,0,1,-1,0,0], [0,0,0,0,1,-1]

while queue:
    x, y, z = queue.popleft()
    for i in range(6):
        ni, nj, nk = di[i] + x, dj[i] + y, dk[i] + z
        if 0 <= ni < h and 0 <= nj < n and 0 <= nk < m and arr[ni][nj][nk] == 0:
            arr[ni][nj][nk] = arr[x][y][z] + 1
            queue.append([ni, nj, nk])

for i in arr:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        answer = max(answer, max(j))

print(answer - 1)


