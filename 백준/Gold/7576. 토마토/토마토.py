from collections import deque
import sys

m, n = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
queue = deque([])

answer = 0

di, dj = [1,-1,0,0] , [0,0,1,-1]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            queue.append([i, j])

while queue:
    x, y = queue.popleft()
    for i in range(4):
        ni, nj = di[i] + x, dj[i] + y
        if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == 0:
            arr[ni][nj] = arr[x][y] + 1
            queue.append([ni, nj])

for i in arr:
    for j in i:
        if j == 0:
            answer = -1
            break
    if answer == -1:
        break
    answer = max(answer, max(i))

if answer == -1:
    print(answer)
else:
    print(answer - 1)

