import sys
sys.setrecursionlimit(10 ** 6)

n = int(input())
arr = [list(input()) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
di, dj = [1,-1,0,0], [0,0,1,-1]

answer_1 , answer_2 = 0, 0
def dfs(x,y):
    visited[x][y] = 1
    check = arr[x][y]

    for k in range(4):
        ni = x + di[k]
        nj = y + dj[k]
        if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == 0:
            if arr[ni][nj] == check:
                    dfs(ni,nj)

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            dfs(i,j)
            answer_1 += 1

for i in range(n):
    for j in range(n):
        if arr[i][j] == "G":
            arr[i][j] = "R"

visited = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            dfs(i,j)
            answer_2 += 1


print(answer_1, answer_2)