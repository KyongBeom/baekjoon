from collections import deque

n, m = map(int, input().split())

arr = [list(map(str, input())) for _ in range(m)]

dx = [0,0,1,-1]
dy = [1,-1, 0,0]

check = []
for i in range(m):
    for j in range(n):
        if arr[i][j] == "W":
            queue = deque()
            queue.append([i,j])
            arr[i][j] = 0
            count = 1
            while queue:
                x,y = queue.popleft()
                for k in range(4):
                    ni = x + dx[k]
                    nj = y + dy[k]
                    if 0 <= ni < m and 0 <= nj < n:
                        if arr[ni][nj] == "W":
                            arr[ni][nj] = 0
                            queue.append([ni,nj])
                            count += 1
            check.append(["W",count])
        elif arr[i][j] == "B":
            queue = deque()
            queue.append([i,j])
            arr[i][j] = 0
            count = 1
            while queue:
                x,y = queue.popleft()
                for k in range(4):
                    ni = x + dx[k]
                    nj = y + dy[k]
                    if 0 <= ni < m and 0 <= nj < n:
                        if arr[ni][nj] == "B":
                            arr[ni][nj] = 0
                            queue.append([ni,nj])
                            count += 1
            check.append(["B", count])
A , B = 0, 0
for i, j in check:
    if i =="W":
        A += j**2
    else:
        B += j**2
print(A, B)

