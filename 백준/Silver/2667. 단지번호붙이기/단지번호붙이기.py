from collections import deque

n = int(input())

arr = [list(map(int, input())) for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1, 0,0]

check = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            queue = deque()
            queue.append([i,j])
            arr[i][j] = 0
            count = 1
            while queue:
                x,y = queue.popleft()
                for k in range(4):
                    ni = x + dx[k]
                    nj = y + dy[k]
                    if 0 <= ni < n and 0 <= nj < n:
                        if arr[ni][nj] == 1:
                            arr[ni][nj] = 0
                            queue.append([ni,nj])
                            count += 1
            check.append(count)
check.sort()
print(len(check))
for i in check:
    print(i)



